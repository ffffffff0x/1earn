# Exchange 搭建

---

**实验环境组成**
- VMware
- 一台 win2016 ,域控(为了你的身心健康着想,不要使用其他版本的 windows server 系统)

---

## 邮件服务器角色

在 exchange 2010 中，exchange 包含五个服务器角色，分别为邮箱服务器，客户端访问服务器，集线传输服务器，统一消息服务器，边缘传输服务器。

exchange 2013 中服务器为 3 个：邮箱服务器，客户端访问服务器，边缘传输服务器

exchange 2016 和 2019 中只有邮箱服务器和边缘传输服务器

---

## 接口和协议

**OWA**

owa 即 outlook web app, 即 outlook 的网页版。（outlook 是 exchange 的客户端软件，许多电脑都有所预装）

- https://localhost/owa

**ECP**

Exchange Administrative Center, 即 exchange 管理中心，管理员的 web 控制台

- https://localhost/ecp

**outlook anywhere**

作用是可以让外网用户直接通过 outlook anywhere 直接登录到 exchange 邮箱而无需使用 VPN。该特性在 exchange server 2013 中默认开启，也就是说在 exchange server 2013 以后 outlook 不再区分内外网环境。

**MAPI**

于 Exchange 2013 SP1 和 Outlook 2013 SP1 中被提出的一种新的 outlook 与 exchange 交互传输协议。

**EAS**

Exchange ActiveSync 是一种允许用户通过移动设备或其他便携式设备访问和管理邮件、联系人、日历等 Exchange 功能的同步协议，在 Windows 上使用时其进程名称为 wcesomm.exe。”

**EWS**

Exchange Web Service，是 exchange 提供的一套 API 编程接口，用于操作 exchange 相关功能，于 exchange server 2007 被提出。

---

## 功能和服务

**Autodiscover**

Autodiscover，自动发现，是exchange server 2007 推出的一个服务。

该服务目的是简化用户登录流程：用户只需要输入自己的电子邮件地址和密码，就能够通过Autodiscover服务获取运行客户端应用程序所需的配置信息，该服务运行在客户端访问服务器上。

**GAL**

GAL即全局地址表（global address list）

记录了域中用户的基本信息与其邮箱地址，以形成域用户与邮箱用户之间的关联。

---

## 搭建过程

先搭建好域控和 DNS 服务器

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/1.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/2.png)

然后一路下一步搭建完毕后,下载 .NET Framework 4.8 和几个依赖
- https://download.visualstudio.microsoft.com/download/pr/014120d7-d689-4305-befd-3cb711108212/0fd66638cde16859462a6243a4629a50/ndp48-x86-x64-allos-enu.exe
- https://www.microsoft.com/download/details.aspx?id=30679
    - 英文版
- https://www.microsoft.com/en-us/download/confirmation.aspx?id=34992
    - 英文版
- https://www.microsoft.com/download/details.aspx?id=40784
    - 英文版

管理员模式运行 powershell 安装所需组件
```
Install-WindowsFeature RSAT-ADDS
```

都安装完毕后重启,一定要重启

然后下载 Exchange Server 2016,运行 setup.exe 安装
- https://www.microsoft.com/zh-cn/download/confirmation.aspx?id=102114

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/3.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/4.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/5.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/6.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/7.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/8.png)

这里会走一个先决条件判断，有可能会失败，按照要求装补丁即可

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/9.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/10.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/11.png)

访问本地
- https://localhost/ecp
- https://localhost/owa

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/12.png)

![](../../../../assets/img/Integrated/Windows/实验/Exchange搭建/13.png)

---

**Source & Reference**
- [Exchange Server 2016 正式安装部署](https://blog.csdn.net/zhaowei198311/article/details/107391577)
- [Exchange系列文章——Exchange2019部署安装](https://www.xiaobei.us/archives/775.html)
- [规划和部署 Exchange Server 2019](https://docs.microsoft.com/zh-cn/exchange/plan-and-deploy/plan-and-deploy?view=exchserver-2019)
- [Exchange Server 2019 必备组件](https://docs.microsoft.com/zh-cn/exchange/plan-and-deploy/prerequisites?view=exchserver-2019)
- [Windows 2019 Server issues with Installing Exchange](https://www.reddit.com/r/sysadmin/comments/dg58ft/windows_2019_server_issues_with_installing/)
- [Enable UAC Prompt for Built-in Administrator in Windows 10](https://winaero.com/enable-uac-prompt-built-in-administrator-windows-10/)
- [在sever2019上安装exchange2016出错怎么解决](https://social.technet.microsoft.com/Forums/zh-CN/4f5566df-7b5a-4cd2-b846-27eee41ab230/22312sever2019199782343335013exchange2016209863816924590200403529920915?forum=exchangeserverzhchs)
- [Exchange Server 必备组件 2016](https://docs.microsoft.com/zh-cn/exchange/plan-and-deploy/prerequisites?view=exchserver-2016)
