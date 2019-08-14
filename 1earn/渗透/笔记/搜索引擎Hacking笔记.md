# 搜索引擎 Hacking

---

## Reference
- [【渗透神器系列】搜索引擎](https://thief.one/2017/05/19/1/)
- [Shodan新手入坑指南](https://www.freebuf.com/sectool/121339.html)
- [shodan-manual](https://b404.gitbooks.io/shodan-manual/)
- [How to Discover MongoDB and Elasticsearch Open Databases](https://habr.com/en/post/443132/)

---

# github
**例子**
```
create user identified by
create user zabbix@'%' identified by
```

---

# google
**例子**

常见
```
inurl:tw
inurl:jp

inurl:editor/db/
inurl:eWebEditor/db/
inurl:bbs/data/
inurl:databackup/
inurl:blog/data/
inurl:\boke\data
inurl:bbs/database/
inurl:conn.asp
inc/conn.asp
Server.mapPath(".mdb")
allinurl:bbs data
filetype:mdb inurl:database
filetype:inc conn
inurl:data filetype:mdb
intitle:"index of" data

intitle:"index of" etc
intitle:"Index of" .sh_history
intitle:"Index of" .bash_history
intitle:"index of" passwd
intitle:"index of" people.lst
intitle:"index of" pwd.db
intitle:"index of" etc/shadow
intitle:"index of" spwd
intitle:"index of" master.passwd
intitle:"index of" htpasswd
inurl:service.pwd
```

黑产
```
老虎机 site:*.gov.cn
澳门银行 site:*.gov.cn
万博亚洲官网 site:*.gov.cn
狗万app site:*.gov.cn
新万博官网 site:*.gov.cn
ylg9999 site:*.gov.cn
九州娱乐 site:*.gov.cn
```

漏洞
```
目录遍历漏洞
    site:xxx.com intitle:index.of

配置文件泄露
    site:xxx.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | extra | ext:ini

数据库文件泄露
    site:xxx.com ext:sql | ext:dbf | ext:mdb

日志文件泄露
    site:xxx.com ext:log

备份和历史文件
    site:xxx.com ext:bkf | ext:bkp | ext:bak | extld | ext:backup

SQL错误
    site:xxx.com intext:”sql syntax near” | intext:”syntax error has occurred” | intext:”incorrect syntax near” | intext:”unexpected end of SQL command” | intext:”Warning: mysql_connect()” | intext:”Warning: mysql_query()” | intext:”Warning: pg_connect()”

公开文件信息
    site:xxx.com ext:doc | ext:docx | extdt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv

phpinfo()
    site:xxx.com ext:php intitle:phpinfo “published by the PHP Group”

JIRA
    配置错误的JIRA设置  inurl:/UserPickerBrowser.jspa -intitle:Login -intitle:Log
    此查询列出了其URI中具有“UserPickerBrowser”的所有URL，以查找公开而且不需要经过身份验证的所有配置错误的 JIRA 用户选择器功能。

    inurl:/ManageFilters.jspa?filterView=popular AND ( intext:All users OR intext:Shared with the public OR intext:Public )
    此查询列出了所有在其URI中具有“Managefilters”并且文本为“Public”的URL，以便找到所有公开暴露且未经过身份验证的错误配置的JIRA过滤器。

    inurl:/ConfigurePortalPages!default.jspa?view=popular
    此查询列出其URI中具有“ConfigurePortalPages”的所有URL，以查找公开公开的所有JIRA仪表板。
```

---

# [Shodan](https://www.shodan.io)
**语法**
```bash
hostname：搜索指定的主机或域名,例如 hostname:"google"
port：搜索指定的端口或服务,例如 port:"21"
country：搜索指定的国家,例如 country:"CN"
city：搜索指定的城市,例如 city:"Hefei"
org：搜索指定的组织或公司,例如 org:"google"
isp：搜索指定的ISP供应商,例如 isp:"China Telecom"
product：搜索指定的操作系统/软件/平台,例如 product:"Apache httpd"
version：搜索指定的软件版本,例如 version:"1.6.2"
geo：搜索指定的地理位置,参数为经纬度,例如 geo:"31.8639, 117.2808"
before/after：搜索指定收录时间前后的数据,格式为dd-mm-yy,例如 before:"11-11-15"
net：搜索指定的IP地址或子网,例如 net:"210.45.240.0/24"
```

**例子**
```bash
# 友情提醒,请遵纪守法
misc
Server: uc-httpd 1.0.0 200 OK Country:"JP"
h3c net:"61.191.146.0/24"
country:US vuln:CVE-2014-0160
port:135,139,445 -hash:0    # 过滤一些主文本标题为空的搜索结果
Hikvision-Webs  # 海康威视

database
all:"mongodb server information" all:"metrics"  # 开放Mongodb数据库
port:27017 -all:"partially" all:"fs.files"  # 有点存货的Mongodb数据库
port:"9200" all:"elastic indices"   # 开放ElasticSearch数据库

ftp
230 'anonymous@' login ok   # 开放匿名ftp

vnc
port:5900 screenshot.label:loggedin # 无认证vnc
```

**外部工具**
```bash
Shodan cli
https://cli.shodan.io/

浏览器插件
https://chrome.google.com/webstore/detail/shodan/jjalcfnidlmpjhdfepjhjbhnhkbgleap
https://addons.mozilla.org/en-US/firefox/addon/shodan_io/

Metasploit
use auxiliary/gather/shodan_search
set SHODAN_APIKEY ********************
set QUERY ****

use auxiliary/gather/shodan_honeyscore  # 蜜罐检测
set SHODAN_APIKEY ********************
set TARGET your_target

Recon-ng
keys add shodan_api ********************
use recon/domains-hosts/shodan_hostname
show options
set SOURCE google
set LIMIT 1
```

---

# [censys](https://www.censys.io)
**例子**
```bash
23.0.0.0/8 or 8.8.8.0/24    # 可以使用and or not
80.http.get.status_code: 200    # 指定状态
80.http.get.status_code:[200 TO 300]    # 200-300之间的状态码
location.country_code: DE　　# 国家
protocols: ("23/telnet" or "21/ftp")    # 协议
tags: scada # 标签
80.http.get.headers.server：nginx   # 服务器类型版本
autonomous_system.description: University   # 系统描述
```

---

# [钟馗之眼](https://www.zoomeye.org/)
**语法**
```bash
app:nginx   # 组件名
ver:1.0 # 版本
os:windows  # 操作系统
country:"China" # 国家
city:"hangzhou" # 城市
port:80 # 端口
hostname:google # 主机名
site:google.com # 网站域名
desc:nmask  # 描述
keywords:passwd # 关键词
service:ftp # 服务类型
ip:8.8.8.8  # ip地址
cidr:8.8.8.8/24 # ip地址段
```

**例子**
```bash
city:tokyo + app:weblogic   # weblogic反序列化来一波？
```

---

# [FoFa](https://fofa.so)
**语法**
```bash
title="abc" # 从标题中搜索abc。例：标题中有北京的网站。
header="abc"    # 从http头中搜索abc。例：jboss服务器。
body="abc"  # 从html正文中搜索abc。例：正文包含Hacked by。
domain="qq.com" # 搜索根域名带有qq.com的网站。例： 根域名是qq.com的网站。
host=".gov.cn"  # 从url中搜索.gov.cn,注意搜索要用host作为名称。
port="443"  # 查找对应443端口的资产。例： 查找对应443端口的资产。
ip="1.1.1.1"    # 从ip中搜索包含1.1.1.1的网站,注意搜索要用ip作为名称。
protocol="https"    # 搜索制定协议类型(在开启端口扫描的情况下有效)。例： 查询https协议资产。
city="Beijing"  # 搜索指定城市的资产。例： 搜索指定城市的资产。
region="Zhejiang"   # 搜索指定行政区的资产。例： 搜索指定行政区的资产。
country="CN"    # 搜索指定国家(编码)的资产。例： 搜索指定国家(编码)的资产。
cert="google.com"   # 搜索证书(https或者imaps等)中带有google.com的资产。
```

**例子**
```bash
title="powered by" && title!=discuz
title!="powered by" && body=discuz
(body="content=\"WordPress" || (header="X-Pingback" && header="/xmlrpc.php" && body="/wp-includes/") ) && host="gov.cn"
```

---

# [Dnsdb](https://www.dnsdb.io/)
**语法**
```markdown
DnsDB 查询语法结构为条件1 条件2 条件3 …., 每个条件以空格间隔, DnsDB 会把满足所有查询条件的结果返回给用户.

域名查询条件
查询语法为 `domain:.`
域名查询是指查询顶级私有域名所有的 DNS 记录,
例如查询 google.com 的所有 DNS 记录: `domain:google.com.`
域名查询可以省略 domain:.

主机查询条件
查询语法:`host:`
例如查询主机地址为 mp3.example.com 的 DNS 记录:`host:map3.example.com`
主机查询条件与域名查询查询条件的区别在于, 主机查询匹配的是 DNS 记录的 Host 值

按 DNS 记录类型查询
查询语法: `type:.`
例如只查询 A 记录: `type:a`
使用条件 : 必须存在 domain: 或者 host: 条件,才可以使用 type: 查询语法

按 IP 限制
查询语法: `ip:`
查询指定 IP: `ip:8.8.8.8` 该查询与直接输入 8.8.8.8 进行查询等效
查询指定 IP 范围: `ip:8.8.8.8-8.8.255.255`
CIDR: `ip:8.8.0.0/24`
IP 最大范围限制 65536 个
```

**例子**

查询 google.com 的所有 A 记录: `google.com type:a`
