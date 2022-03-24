# MySQL

---

**常用语句**

```sql
select group_concat(table_name) from information_schema.tables where table_schema=database()
```

查看 xxx 的字段
```sql
select group_concat(column_name) from information_schema.columns where table_name='xxx'
```

读取字段的内容
```sql
select flag from fl4g
```

---

## MySQL 系统库表

**information_schema**

MySQL自带的系统数据库，当中大部分是我们需要了结的信息，比如字符集，权限相关，数据库实体对象信息，外检约束，分区，压缩表，表信息，索引信息，参数，优化，锁和事物等等。所以可以利用这个数据库来进行注入。

```sql
--存储mysql数据库下面的所有表名信息的表
information_schema.tables
    --数据库名 : table_schema
    --表名 : Table_name

-- 存储mysql数据库下面的所有列名信息的表
information_schema.columns
    -- 表名 : table_name
```

---

## MySQL 函数

### 常见系统函数和变量

- version() -- MySQL版本
- user() -- 数据库用户名
- database() -- 数据库名
- @@datadir -- 数据库路径
- @@basedir -- 安装路径
- @@version_compile_os -- 操作系统版本

---

### 常见连接函数

在 select 数据时，我们往往需要将数据进行连接后进行回显。很多的时候想将多个数据或者多行数据进行输出的时候，需要使用字符串连接函数。

**concat(str1,str2,...)**

没有分隔符地连接字符串

**concat_ws(separator,str1,str2,...)**

含有分隔符地连接字符串

**group_concat(str1,str2,...)**

连接一个组的所有字符串，并以逗号分隔每一条数据

https://www.cnblogs.com/lcamry/p/5715634.html

---

### 截取字符串常用函数

**mid()**

此函数为截取字符串一部分。

```sql
MID(column_name,start[,length])
-- column_name  : 必需。要提取字符的字段。
-- start        : 必需。规定开始位置（起始值是 1）。
-- length       : 可选。要返回的字符数。如果省略，则 MID() 函数返回剩余文本。
```

例如 : str="123456" mid(str,2,1) 结果为2

**substr()**

Substr() 和 substring() 函数实现的功能是一样的，均为截取字符串。

```sql
string substring(string, start, length)
string substr(string, start, length)
-- 参数描述同 mid() 函数，第一个参数为要处理的字符串，start 为开始位置，length 为截取的长度。
```

**Left()**

得到字符串左部指定个数的字符

```sql
Left ( string, n )
-- string 为要截取的字符串，n 为长度。
```

**ord()**

返回第一个字符的 ASCII 码

例如 : ORD(MID(DATABASE(),1,1))>114 意为检测 database() 的第一位 ASCII 码是否大于 114，也就是 'r'

---

### 字符串编码

**ASCII()**

返回字符的 ASCII 码值

```sql
select ASCII('hello')
```

**CHAR()**

把整数转换为对应的字符

```sql
SELECT CHAR(77,121,83,81,'76');
```

**Hex()**

返回十六进制值的字符串表示

```sql
SELECT HEX('mysql');
```

**Unhex()**

执行HEX(str)的逆运算

```sql
SELECT UNHEX('4D7953514C');
```

---

### 导入导出函数

**load_file()**

load_file()：以文本方式读取文件，在 Windows 中，路径设置为 \\

读取文件并返回该文件的内容作为一个字符串。

例如 : select 1,1,1,load_file(char(99,58,47,98,111,111,116,46,105,110,105))

---

## 安全加固

### 禁止远程访问

```sql
select user,host from user;
```

更新 root 账户，开启远程访问，配置如下：
```sql
use mysql;
update user set host = "%" where user = "root";
flush privileges;
```

更新root账户，关闭远程访问，配置如下：
```sql
use mysql;
update user set host = "localhost" where user = "root" and host= "%";
flush privileges;
```

### 禁止匿名账户登陆

检测是否存在匿名账户
```sql
select * from user where user='';
```

如有空记录存在，说明存在匿名用户，为了保证数据库安全，删除语法为：
```sql
delete from user where user='';
```

修改匿名用户
```sql
SET PASSWORD FOR ''@'localhost' = PASSWORD('newpwd');
```

### 最大连接数限制

MySQL 数据库经常会遇到这么一个问题，就是 “Can not connect to MySQL server. Too many connections”。这是由于访问 MySQL 且还未释放的连接数目已经达到 MySQL 的上限。通常，MySQL 的最大连接数默认是 100, 最大可以达到 16384。

查看最大连接数
```sql
show variables like 'max_connections';
```

修改最大连接数
```sql
set GLOBAL max_connections = 500;
```

查看所有用户的当前连接数
```sql
show processlist;
```

### 限制本地文件读取

MySQL 提供对本地文件的读取，使用的是 load data local infile 命令，MySQL5.0 以上的版本选项是默认打开的，该操作令会利用 MySQL 把本地文件读到数据库中，然后用户就可以非法获取敏感信息了，一般没有特殊的需要不要开启读取本地文件的选项。

配置Linux 下/etc/my.cnf文件
```
local-infile=0
```

或启动数据库时，加上 --local-infile=0&参数
```
/usr/local/mysql/bin/mysqld_safe --local-infile=0 &
```

---

## Source & Reference

- [Sql注入截取字符串常用函数](https://www.cnblogs.com/lcamry/p/5504374.html)
