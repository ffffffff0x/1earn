# Secure-Win

<p align="center">
    <a href="https://commons.wikimedia.org/wiki/File:William_J._McCloskey_(1859%E2%80%931941),_Wrapped_Oranges,_1889._Oil_on_canvas._Amon_Carter_Museum_of_American_Art.jpg"><img src="../../../assets/img/运维/Windows/Secure-Win.jpg" width="85%"></a>
</p>

- `windows 加固+维护+应急响应参考`

---

# 大纲

**[文件](#文件)**
* [可疑文件](#可疑文件)

**[系统](#系统)**
* [开机启动](#开机启动)
* [账号](#账号)
* [进程](#进程)
* [注册表](#注册表)
* [日志](#日志)
    * [系统日志](#系统日志)
    * [日志工具](#日志工具)
    * [第三方程序日志](#第三方程序日志)

**[Net](#Net)**
* [端口](#端口)

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
- ​Window 2008R2 : `C:\Users\`

**查看服务器是否存在隐藏账号、克隆账号**

使用D盾工具，集成了对克隆账号检测的功能。

## 进程

开始-运行，输入 `msinfo32` ，依次点击“软件环境→正在运行任务”就可以查看到进程的详细信息，比如进程路径、进程 ID、文件创建日期、启动时间等。

**服务**

开始-运行，输入 `services.msc`

**cmd 下使用**
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

**powershell 下使用**
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
**应用程序日志**

包含由应用程序或系统程序记录的事件，主要记录程序运行方面的事件，例如数据库程序可以在应用程序日志中记录文件错误，程序开发人员可以自行决定监视哪些事件。如果某个应用程序出现崩溃情况，那么我们可以从程序事件日志中找到相应的记录，也许会有助于你解决问题。

默认位置: `%SystemRoot%\System32\Winevt\Logs\Application.evtx`

**系统日志**

记录操作系统组件产生的事件，主要包括驱动程序、系统组件和应用软件的崩溃以及数据丢失错误等。系统日志中记录的时间类型由Windows NT/2000操作系统预先定义。

默认位置: `%SystemRoot%\System32\Winevt\Logs\System.evtx`

**安全日志**

包含由应用程序或系统程序记录的事件，主要记录程序运行方面的事件，例如数据库程序可以在应用程序日志中记录文件错误，程序开发人员可以自行决定监视哪些事件。如果某个应用程序出现崩溃情况，那么我们可以从程序事件日志中找到相应的记录，也许会有助于你解决问题。

默认位置: `%SystemRoot%\System32\Winevt\Logs\Application.evtx`

**转发事件**

日志用于存储从远程计算机收集的事件。若要从远程计算机收集事件，必须创建事件订阅。

默认位置: `%SystemRoot%\System32\Winevt\Logs\ForwardedEvents.evtx`

**事件查看**
开始-运行，输入 `eventvwr.msc`

| 事件ID | 说明                             |
| :----- | -------------------------------- |
| 4624   | 登录成功                         |
| 4625   | 登录失败                         |
| 4634   | 注销成功                         |
| 4647   | 用户启动的注销                   |
| 4672   | 使用超级用户（如管理员）进行登录 |
| 4720   | 创建用户                         |

每个成功登录的事件都会标记一个登录类型，不同登录类型代表不同的方式：

| 登录类型 | 描述                            | 说明                                             |
| :------- | ------------------------------- | ------------------------------------------------ |
| 2        | 交互式登录（Interactive）       | 用户在本地进行登录。                             |
| 3        | 网络（Network）                 | 最常见的情况就是连接到共享文件夹或共享打印机时。 |
| 4        | 批处理（Batch）                 | 通常表明某计划任务启动。                         |
| 5        | 服务（Service）                 | 每种服务都被配置在某个特定的用户账号下运行。     |
| 7        | 解锁（Unlock）                  | 屏保解锁。                                       |
| 8        | 网络明文（NetworkCleartext）    | 登录的密码在网络上是通过明文传输的，如FTP。      |
| 9        | 新凭证（NewCredentials）        | 使用带/Netonly参数的RUNAS命令运行一个程序。      |
| 10       | 远程交互，（RemoteInteractive） | 通过终端服务、远程桌面或远程协助访问计算机。     |
| 11       | 缓存交互（CachedInteractive）   | 以一个域用户登录而又没有域控制器可用             |

Windows 的日志以事件 id 来标识具体发生的动作行为，可通过下列网站查询具体 id 对应的操作
- https://docs.microsoft.com/en-us/windows/security/threat-protection/ 直接搜索 event + 相应的事件id 即可
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx?i=j

案例:查看系统账号登录情况
1. 开始-运行，输入 `eventvwr.msc`
2. 在事件查看器中，`Windows日志` --> `安全`，查看安全日志；
3. 在安全日志右侧操作中，点击 `筛选当前日志` ，输入事件 ID 进行筛选。
    - 4624  --登录成功
    - 4625  --登录失败
    - 4634 -- 注销成功
    - 4647 -- 用户启动的注销
    - 4672 -- 使用超级用户（如管理员）进行登录
4. 输入事件 ID：4625 进行日志筛选，发现事件 ID：4625，事件数 175904，即用户登录失败了 175904 次，那么这台服务器管理员账号可能遭遇了暴力猜解。

案例:查看计算机开关机的记录
1. 开始-运行，输入 `eventvwr.msc`
2. 在事件查看器中，`Windows日志` --> `系统`，查看系统日志；
3. 在系统日志右侧操作中，点击 `筛选当前日志` ，输入事件 ID 进行筛选。其中事件 ID 6006 ID6005、 ID 6009 就表示不同状态的机器的情况（开关机）。
    - 6005 信息 EventLog 事件日志服务已启动。(开机)
    - 6006 信息 EventLog 事件日志服务已停止。(关机)
    - 6009 信息 EventLog 按ctrl、alt、delete键(非正常)关机
4. 输入事件  ID：6005-6006进行日志筛选，发现了两条在 2018/7/6 17:53:51 左右的记录，也就是我刚才对系统进行重启的时间。

**审核策略**

Windows Server 2008 R2 系统的审核功能在默认状态下并没有启用 ，建议开启审核策略，若日后系统出现故障、安全事故则可以查看系统的日志文件，排除故障，追查入侵者的信息等。

开始 --> 管理工具 --> 本地安全策略 --> 本地策略 --> 审核策略

### 日志工具
**logparser**
`logparser` 是一款 windows 日志分析工具，访问这里下载 https://www.microsoft.com/en-us/download/details.aspx?id=24659

- 文章
    - [windows安全日志分析之logparser篇](https://wooyun.js.org/drops/windows%E5%AE%89%E5%85%A8%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E4%B9%8Blogparser%E7%AF%87.html)

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

下载地址：http://www.lizard-labs.com/log_parser_lizard.aspx

依赖包：Microsoft .NET Framework 4 .5，下载地址：https://www.microsoft.com/en-us/download/details.aspx?id=42642

**Event Log Explorer**

Event Log Explorer 是一款非常好用的 Windows 日志分析工具。可用于查看，监视和分析跟事件记录，包括安全，系统，应用程序和其他微软 Windows 的记录被记载的事件，其强大的过滤功能可以快速的过滤出有价值的信息。

下载地址：https://event-log-explorer.en.softonic.com/

### 第三方程序日志
**web日志**
- 内容见 [取证笔记](../../安全/笔记/BlueTeam/取证笔记.md#中间件服务器程序日志) 中间件服务器程序日志部分

**数据库日志**
- 内容见 [取证笔记](../../安全/笔记/BlueTeam/取证笔记.md#数据库取证) 数据库取证部分

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