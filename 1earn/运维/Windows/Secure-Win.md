# Secure-Win

<p align="center">
    <img src="../../../assets/img/banner/Secure-Win.jpg" width="90%">
</p>

- `windows 加固+维护+应急响应参考`

---

# 大纲

* **[文件](#文件)**
    * [可疑文件](#可疑文件)

* **[系统](#系统)**
    * [开机启动](#开机启动)
    * [账号](#账号)
    * [进程](#进程)
    * [注册表](#注册表)
    * [日志](#日志)
        * [系统日志](#系统日志)
        * [日志工具](#日志工具)
        * [第三方程序日志](#第三方程序日志)

* **[Net](#Net)**
    * [端口](#端口)
    * [RDP](#rdp)
    * [DNS](#dns)


---

# 文件
## 可疑文件

- 回收站
- 浏览器下载目录
- 浏览器历史记录

**最近文件**

开始-运行，输入 `%UserProfile%\Recent`
- `C:\Documents and Settings\Administrator\Recent`
- `C:\Documents and Settings\Default User\Recent`

查看指定时间范围包括上传文件夹的访问请求：
```
findstr /s /m /I “UploadFiles” *.log
```

**临时文件**
- `c:\windows\temp\`

---

# 系统

开启组策略编辑器 `gpedit.msc`

**信息**

开始-运行，输入 `systeminfo`

## 开机启动

开始-运行，输入 `msconfig`

- `(ProfilePath)\Start Menu\Programs\Startup`

**注册表项**

在 cmd 下使用
```
REG query HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
REG query HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Runonce
REG query HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\policies\Explorer\Run
REG query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
REG query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
REG query HKLM\Software\Microsoft\Windows\CurrentVersion\RunonceEx
```

**服务自启动**

开始-运行，输入 `services.msc`

**计划任务**
- `C:\Windows\System32\Tasks\`
- `C:\Windows\SysWOW64\Tasks\`
- `C:\Windows\tasks\`

开始-运行，输入 `taskschd.msc`

- **cmd 下使用**
    ```
    schtasks
    ```

## 账号

开始-运行，输入 `lusrmgr.msc`

**cmd 下使用**
- `net user` : 显示用户账号信息
- `wmic UserAccount get` : 列出当前系统所有账户

**注册表项**
```
REG query HKEY_LOCAL_MACHINE/SAM/SAM/Domains/Account/Users
```

**查看用户目录**

新建账号会在以下目录生成一个用户目录，查看是否有新建用户目录。
- Window 2003 : `C:\Documents and Settings`
- Window 2008R2 : `C:\Users\`

**查看服务器是否存在隐藏账号、克隆账号**

可以使用 D 盾工具，其集成了对克隆账号检测的功能。

**加固**

- Microsoft本地管理员密码解决方案（LAPS）
    - 参考文章:[Microsoft Local Administrator Password Solution (LAPS)](https://adsecurity.org/?p=1790)

## 进程

开始-运行，输入 `msinfo32` ，依次点击“软件环境→正在运行任务”就可以查看到进程的详细信息，比如进程路径、进程 ID、文件创建日期、启动时间等。

**服务**

开始-运行，输入 `services.msc`

**cmd 下查看可疑进程**
```
tasklist /svc | findstr pid
netstat -ano

wmic process | find "Proccess Id" > proc.csv
wmic process get caption,commandline /value
wmic process where caption=”svchost.exe” get caption,commandline /value
wmic service get name,pathname,processid,startname,status,state /value
wmic process get CreationDate,name,processid,commandline,ExecutablePath /value
wmic process get name,processid,executablepath| findstr "7766"
```

**powershell 下查看可疑进程**
```
Get-WmiObject -Class Win32_Process
Get-WmiObject -Query "select * from win32_service where name='WinRM'" -ComputerName Server01, Server02 | Format-List -Property PSComputerName, Name, ExitCode, Name, ProcessID, StartMode, State, Status
```

**查看可疑的进程及其子进程内容**
- 没有签名验证信息的进程
- 没有描述信息的进程
- 进程的属主
- 进程的路径是否合法
- CPU 或内存资源占用长时间过高的进程

**令牌假冒防御**

禁止 Domain Admins 登录对外且未做安全加固的服务器，因为一旦服务器被入侵，域管理员的令牌可能会被攻击者假冒，从控制 DC。

如果想清除假冒令牌，重启服务器即可。

## 注册表

开始-运行，输入 `regedit`

**cmd 下运行**
```
REG query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList
REG query HKLM\Software\Microsoft\Windows\CurrentVersion\Run\ HKEY_CLASSES_ROOT\exefile\shell\open\command
```

---

## 日志

### 系统日志

系统日志基本知识见 [日志](./笔记/日志.md)

**导出日志**
- 文章
    - [Export corrupts Windows Event Log files](https://blog.fox-it.com/2019/06/04/export-corrupts-windows-event-log-files/) - 导出损坏的 Windows 事件日志文件

**恢复 eventlogedit 删除的记录**
- 文章
    - [Detection and recovery of NSA’s covered up tracks](https://blog.fox-it.com/2017/12/08/detection-and-recovery-of-nsas-covered-up-tracks/)

- 工具
    - [fox-it/danderspritz-evtx](https://github.com/fox-it/danderspritz-evtx) - 解析 evtx 文件并检测 DanderSpritz eventlogedit 模块的使用

**Windows Defender 日志**
- Windows Defender 应用程序使用 `MpCmdRun.log` 和 `MpSigStub.log` 两个日志文件，在 `C:\Windows\Temp` 文件夹下。该文件夹为默认的 SYSTEM 账户临时文件夹，但是每一个用户都拥有写权限。Administrators （管理员）和 SYSTEM 账户拥有这个文件夹的所有权限，一般用户甚至没有读的权限。

### 日志工具

**Sysmon**
- [Sysmon](../../安全/工具/Sysmon.md)

**logparser**

`logparser` 是一款 windows 日志分析工具，访问这里下载 https://www.microsoft.com/en-us/download/details.aspx?id=24659

- 文章
    - [windows安全日志分析之logparser篇](https://wooyun.js.org/drops/windows%E5%AE%89%E5%85%A8%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E4%B9%8Blogparser%E7%AF%87.html)

- 使用

    登录成功的所有事件
    ```
    LogParser.exe -i:EVT –o:DATAGRID "SELECT * FROM c:\Security.evtx where EventID=4624"
    ```

    指定登录时间范围的事件
    ```
    LogParser.exe -i:EVT –o:DATAGRID "SELECT * FROM c:\Security.evtx where TimeGenerated>'2018-06-19 23:32:11' and TimeGenerated<'2018-06-20 23:34:00' and EventID=4624"
    ```

    提取登录成功的用户名和IP
    ```
    LogParser.exe -i:EVT –o:DATAGRID "SELECT EXTRACT_TOKEN(Message,13,' ') as EventType,TimeGenerated as LoginTime,EXTRACT_TOKEN(Strings,5,'|') as Username,EXTRACT_TOKEN(Message,38,' ') as Loginip FROM c:\Security.evtx where EventID=4624"
    ```

    登录失败的所有事件
    ```
    LogParser.exe -i:EVT –o:DATAGRID "SELECT * FROM c:\Security.evtx where EventID=4625"
    ```

    提取登录失败用户名进行聚合统计
    ```
    LogParser.exe -i:EVT "SELECT EXTRACT_TOKEN(Message,13,' ') as EventType,EXTRACT_TOKEN(Message,19,' ') as user,count(EXTRACT_TOKEN(Message,19,' ')) as Times,EXTRACT_TOKEN(Message,39,' ') as Loginip FROM c:\Security.evtx where EventID=4625 GROUP BY Message”
    ```

    系统历史开关机记录
    ```
    LogParser.exe -i:EVT –o:DATAGRID "SELECT TimeGenerated,EventID,Message FROM c:\System.evtx where EventID=6005 or EventID=6006"
    ```

**LogParser Lizard**

对于 GUI 环境的 Log Parser Lizard，其特点是比较易于使用，甚至不需要记忆繁琐的命令，只需要做好设置，写好基本的 SQL 语句，就可以直观的得到结果。

下载地址 : http://www.lizard-labs.com/log_parser_lizard.aspx

依赖包：Microsoft .NET Framework 4 .5，下载地址：https://www.microsoft.com/en-us/download/details.aspx?id=42642

**Event Log Explorer**

Event Log Explorer 是一款非常好用的 Windows 日志分析工具。可用于查看，监视和分析跟事件记录，包括安全，系统，应用程序和其他微软 Windows 的记录被记载的事件，其强大的过滤功能可以快速的过滤出有价值的信息。

下载地址 : https://event-log-explorer.en.softonic.com/

**Win-Logs-Parse-tool**

Python 开发的解析 windows 日志文件的工具，可采用手动添加文件的方式进行解析，解析后的文件为 XML，HTML 两种格式，HTML 已采用Bootstrap 架进行界面可视化优化，可直接查看重点日志数据，解析后的 HTML 数据文件保存在执行文件下的 logs/ 文件夹下 ( 自动创建 )，XML 数据文件保存在执行文件下的 logs/xml/ 文件夹下，

项目地址 : https://github.com/Clayeee/Win-Logs-Parse-tool

### 第三方程序日志

**web日志**
- 内容见 [取证](../../安全/笔记/BlueTeam/取证.md#中间件服务器程序日志) 中间件服务器程序日志部分

**数据库日志**
- 内容见 [取证](../../安全/笔记/BlueTeam/取证.md#数据库取证) 数据库取证部分

**应用程序日志**
- 内容见 [取证](../../安全/笔记/BlueTeam/取证.md#应用程序取证) 应用程序取证部分

---

# Net
## 端口

查看目前的网络连接，定位可疑的 ESTABLISHED
```
netstat -ano

- CLOSED:无连接活动或正在进行
- LISTEN:监听中等待连接
- SYN_RECV:服务端接收了 SYN
- SYN_SENT:请求连接等待确认
- ESTABLISHED:连接建立数据传输
- FIN_WAIT1:请求中止连接，等待对方 FIN
- FIN_WAIT2:同意中止，请稍候
- ITMED_WAIT:等待所有分组死掉
- CLOSING:两边同时尝试关闭
- TIME_WAIT:另一边已初始化一个释放
- LAST_ACK:等待原来的发向远程 TCP 的连接中断请求的确认
- CLOSE-WAIT:等待关闭连接
```

根据 netstat 定位出的 pid，进行进程定位
```
tasklist  | findstr “PID”
```

---

## RDP

**防爆破**
- [y11en/BlockRDPBrute](https://github.com/y11en/BlockRDPBrute) - [HIPS]RDP(3389)爆破防护

**连接记录**
- [Windows RDP 连接记录](../../安全/笔记/RedTeam/Windows渗透.md#连接记录)

---

## DNS

很多时候需要通过某个恶意域名来判断主机失陷情况。

**文章**
- [哪个进程在访问这个恶意域名???](https://mp.weixin.qq.com/s/mcK06AOWVkwOVR67_n4OGw)
- [DNS日志记录方法](https://green-m.me/2017/08/21/windows-dns-log/)

**工具**
- **Sysmon**
    - [Sysmon查看DNS记录](../../安全/工具/Sysmon.md#DNS记录)

- **DNSQuerySniffer**

    DNSQuerySniffer 是网络嗅探工具，显示 DNS 查询发送你的系统。每个 DNS 查询，显示以下信息：主机名，端口号，编号查询，请求类型（A，AAAA，NS，和 MX，等等），请求响应时间，时间，响应代码，数量的记录，并返回的 DNS 记录的内容。通过 DNSQuerySniffer 我们先确定访问恶意域名的端口号。这个工具的优点是可以将主机访问过的所有域名记录下来。

    下载地址 : https://www.nirsoft.net/utils/dns_query_sniffer.html

    配合 Process Monitor 可以定位进程

- **[dnsdataview](https://www.nirsoft.net/utils/dns_records_viewer.html)** - 记录 DNS 记录

**DNS cache log**
- 文章
    - [开启DNS Client Service日志](http://blog.nsfocus.net/open-dns-client-service-log/)

- 开启命令
    ```
    net stop dnscache

    type nul > %systemroot%\system32\dnsrsvlr.log
    type nul > %systemroot%\system32\dnsrslvr.log
    type nul > %systemroot%\system32\asyncreg.log

    cacls %systemroot%\system32\dnsrsvlr.log /E /G "NETWORK SERVICE":W
    cacls %systemroot%\system32\dnsrslvr.log /E /G "NETWORK SERVICE":W
    cacls %systemroot%\system32\asyncreg.log /E /G "NETWORK SERVICE":W

    net start dnscache
    ```

**ETW consumers**

windows 8.1 和 windows server 2012 R2 及以上版本的操作系统，可以下载补丁直接以标准的 windows 日志格式记录 dns log，windows server 2016 可以直接开启。

微软官方文档 : https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800669(v=ws.11)

**DNS Client Cached**
- 文章
    - [Getting DNS Client Cached Entries with CIM/WMI](https://www.darkoperator.com/blog/2020/1/14/getting-dns-client-cached-entries-with-cimwmi)

- 工具
    - https://github.com/PSGumshoe/PSGumshoe/blob/master/CIM/Get-CimDNSCache.ps1
        ```powershell
        .\Get-CimDNSCache.ps1 # include file
        Get-CimDNSCache -Name *microsoft* -Type A
        ```
