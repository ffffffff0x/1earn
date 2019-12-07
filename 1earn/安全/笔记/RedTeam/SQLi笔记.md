# SQLi 笔记

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

**教程**
- [SQL 注入 - CTF Wiki](https://ctf-wiki.github.io/ctf-wiki/web/sqli/)
- [Beyond SQLi: Obfuscate and Bypass](https://www.exploit-db.com/papers/17934)
- [aleenzz/MSSQL_SQL_BYPASS_WIKI](https://github.com/aleenzz/MSSQL_SQL_BYPASS_WIKI)
- [aleenzz/MYSQL_SQL_BYPASS_WIKI](https://github.com/aleenzz/MYSQL_SQL_BYPASS_WIKI)

**payload**
- [trietptm/SQL-Injection-Payloads](https://github.com/trietptm/SQL-Injection-Payloads)

**SQLi 测试**
- http://demo.testfire.net/
- https://juice-shop.herokuapp.com/#/search
- https://sqlchop.chaitin.cn/demo/

**靶场**

![image](../../../../assets/img/才怪.png)

**sqlmap**
- **笔记**
    - [sqlmap 笔记](../../工具/sqlmap笔记.md)

---

按 SQLMap 中的分类来看，SQL 注入类型有以下 5 种：
```
UNION query SQL injection(可联合查询注入)
Stacked queries SQL injection(可多语句查询注入)
Boolean-based blind SQL injection(布尔型注入)
Error-based SQL injection(报错型注入)
Time-based blind SQL injection(基于时间延迟注入)
```

**SQL 注入常规利用思路**
```
1. 寻找注入点，可以通过 web 扫描工具实现
2. 通过注入点，尝试获得关于连接数据库用户名、数据库名称、连接数据库用户权限、操作系统信息、数据库版本等相关信息。
3. 猜解关键数据库表及其重要字段与内容(常见如存放管理员账户的表名、字段名等信息)
4. 可以通过获得的用户信息，寻找后台登录。
5. 利用后台或了解的进一步信息，上传 webshell 或向数据库写入一句话木马，以进一步提权，直到拿到服务器权限。
```

---

# 按库
## MYSQL
**手动注入**
- 手工注入思路

    自动化的注入神器 sqlmap 固然好用，但还是要掌握一些手工注入的思路，下面简要介绍手工注入(非盲注)的步骤。
    ```
    1.判断是否存在注入，注入是字符型还是数字型
    2.猜解 SQL 查询语句中的字段数
    3.确定显示的字段顺序
    4.获取当前数据库
    5.获取数据库中的表
    6.获取表中的字段名
    7.下载数据
    ```

- 显注
    1. 在参数中输入一个单引号 `’`，引起执行查询语句的语法错误，得到服务器的错误回显，从而判断服务器的数据库类型信息。
    2. 根据数据库类型构造 sql 注入语句。例如一个 get 方式的 url `http://www.xxx.com/abc.asp?p=YY` 修改 p 的参数值 `http://www.xxx.com/abc.asp?p=YY and user>0 ` ，就可以判断是否是 SQL-SERVER，而还可以得到当前连接到数据库的用户名。`http://www.xxx.com/abc.asp?p=YY&n … db_name()>0` 不仅可以判断是否是 SQL-SERVER，而还可以得到当前正在使用的数据库名 。

- 盲注，大部分时候 web 服务器关闭了错误回显。
    1. `http://www.xxx.com/abc.asp?p=1 and 1=2` sql 命令不成立，结果为空或出错 ；
    2. `http://www.xxx.com/abc.asp?p=1 and 1=1` sql 命令成立，结果正常返回 。

    两个测试成功后，可以判断负载的 sql 被执行，存在 sql 注入漏洞。

---

## MSSQL

![image](../../../../assets/img/才怪.png)

---

## ORACLE

![image](../../../../assets/img/才怪.png)

---

# 按类型
## UA注入
**文章**
- [User Agent注入攻击及防御](https://www.freebuf.com/articles/web/105124.html)

**案例**
- [m.17u.cn一处SQL注入](https://sec.ly.com/bugdetail?id=009063229194078153174131073236159115161105151152)
