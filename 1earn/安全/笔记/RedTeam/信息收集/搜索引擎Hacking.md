# 搜索引擎 Hacking

<p align="center">
    <img src="../../../../../assets/img/banner/搜索引擎Hacking.jpg" width="90%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 大纲

* [Github](#github)
* [Google](#google)
* [Shodan](#shodan)
* [BinaryEdge](#binaryedge)
* [Censys](#censys)
* [Zoomeye](#zoomeye)
* [FoFa](#fofa)
* [Dnsdb](#dnsdb)
* [知风](#知风)
* [ONYPHE](#onyphe)
* [GreyNoise](#greynoise)
* [Thingful](#thingful)

---

**相关文章**
- [Shodan BinaryEdge ZoomEye 网络空间搜索引擎测评](https://paper.seebug.org/970/)

**常用搜索接口**
```
https://www.exploit-db.com/search?q=
https://habr.com/en/search/?q=
https://so.csdn.net/so/search/s.do?q=
http://so.51cto.com/?keywords=
```

---

# Github

<p align="center">
    <img src="../../../../../assets/img/logo/github.png" width="25%">
</p>

**文章**
- [Auditing GitHub users’ SSH key quality](https://blog.benjojo.co.uk/post/auditing-github-users-keys)

**语法**

| 限定词 	            | 案例 |
| - | - |
| in:name 	        | `in:name python` 查出仓库名中有 python 的项目（python in:name 也是一样的） |
| in:description 	    | `in:name,description python` 查出仓库名或者项目描述中有 python 的项目 |
| in:readme 	        | `in:readme python` 查出 `readme.md` 文件里有 python 的项目 |
| repo:owner/name 	| `repo:octocat/hello-world` 查出 octocat 的 hello-world 项目（指定了某个人的某个项目） |
| user:USERNAME 	    | `user:1335951413 stars:<10` 查出用户 1335951413 名下 stars 少于 10 的项目
| org:ORGNAME 	    | `org:github` 查出 github 名下的项目 |
| stars:n 	        | `stars:>=5` 查出 star数大于等于 5 个 的项目（支持大于小于区间等） |
| pushed:YYYY-MM-DD 	| `css pushed:>2013-02-01` 查出仓库中包含 css 关键字，并且在 2013年1月 之后更新过的项目 |
| language:LANGUAGE 	| `rails language:javascript` 查出仓库包含 rails 关键字，并且使用 javscript 语言的项目 |
| created:YYYY-MM-DD 	| `webos created:<2011-01-01` 查出仓库中包含 webos 关键字并且是在 2011 年之前创建的项目（也支持时分秒，支持大于小于区间等） |
| followers:n         | `followers:1000` 查出有 1000 个拥护者（followers） 的项目（支持大于小于区间等） |
| forks:n 	        | `forks:5` 查出有 5 个 forks 的项目（支持大于小于区间等） |
| topic:TOPIC         | `topic:jekyll` 查出含有 jekyll 这个 topic 的项目（项目描述下面的东西，相当于标签、分类） |
| topics:n 	        | `topics:>5` 查出有 5 个以上 topic 的项目（支持大于小于区间等） |
| archived:true/false | `archived:true GNOME` 查出已经封存了并且含有 GNOME 关键字的项目（已经不再维护了的项目） |
| license:LICENSE_KEYWORD | `license:apache-2.0` 查出仓库的开源协议是 apache-2.0 的 |
| size:n 	| `size:1000` 查出仓库大小等于 1MB 的项目 |
| size:n 	| `size:>=30000` 查出仓库大小至少大于 30MB 的项目 |
| size:n 	| `size:50..120` 查出仓库大小在 50KB 至 120KB 之间的项目 |
| is:public/private | `is:public org:github` 查出仓库所有组织是 github 并且公开的项目 |
| is:public/private | `is:private github` 查出含有 github 关键字并且是私有的项目（私有的别人看不到，所以这个是用来搜索自己的私有项目的） |

> 项目名字(name)里有 python 的
```
in:name python
```

> 名字(name)里有 python 的并且 stars 大于 3000 的
```
in:name python starts:>3000
```

> 名字(name)里有 python 的并且 stars 大于 3000 、forks 大于 200 的
```
in:name python starts:>3000 forks:>200
```

> 详情(readme)里面有 python 的并且 stars 大于 3000 的
```
in:readme python starts:>3000
```

> 描述(description)里面有 python 的并且 stars 大于 3000 的
```
in:description python starts:>3000
```

> 描述(description)里面有 python 的并且是 python 语言的
```
in:description python language:python
```

> 描述(description)里面有 python 的并且 2019-12-20 号之后有更新过的
```
in:description python pushed:>2019-12-20
```

**例子**
- 敏感信息
    ```
    create user identified by
    create user zabbix@'%' identified by
    各单位
    ```

    - [leaky-repo](https://github.com/Plazmaz/leaky-repo) - 仓库收集了泄露文件的案例

- 交流
    ```
    内部
    钉钉群
    ```

- 人名
    - [wainshine/Chinese-Names-Corpus](https://github.com/wainshine/Chinese-Names-Corpus) - 中文人名语料库。中文姓名,姓氏,名字,称呼,日本人名,翻译人名,英文人名。可用于中文分词、人名实体识别。

- 地名
    - [modood/Administrative-divisions-of-China: 中华人民共和国行政区划:省级(省份直辖市自治区)、 地级(城市)、 县级(区县)、 乡级(乡镇街道)、 村级(村委会居委会) ,中国省市区镇村二级三级四级五级联动地址数据 Node.js 爬虫.](https://github.com/modood/Administrative-divisions-of-China)

**工具**
- [BishopFox/GitGot](https://github.com/BishopFox/GitGot) - 快速搜索 GitHub 上公共数据的敏感信息
- [UKHomeOffice/repo-security-scanner](https://github.com/UKHomeOffice/repo-security-scanner)- 查找意外提交给 git 仓库的秘密的 CLI 工具,例如密码,私钥
- [gwen001/github-search](https://github.com/gwen001/github-search) - 在GitHub上执行基本搜索的工具。
- [eth0izzle/shhgit](https://github.com/eth0izzle/shhgit) - 实时的监控 github 寻找敏感信息
- [lightless233/geye](https://github.com/lightless233/geye) - 一款面向企业级以及白帽子的"More Fastest" Github监控工具
- [Securityautomation/DumpTheGit](https://github.com/Securityautomation/DumpTheGit) - 搜索公开的代码仓库, 查找敏感信息

---

- [cve-search/git-vuln-finder](https://github.com/cve-search/git-vuln-finder) - 从 git 提交消息中寻找潜在的软件漏洞

**同类代码托管网站**
```
https://usersnap.com/ | Usersnap - Customer Feedback & Visual Bug Tracking
https://www.assembla.com/home | Secure Git, Secure Software Development in the Cloud | Assembla
https://osdn.net/ | Develop and Download Open Source Software - OSDN
https://gitee.com/ | 码云 Gitee — 基于 Git 的代码托管和研发协作平台
https://xiaolvyun.baidu.com/#page1 | 百度效率云 | Git代码托管,版本管理,项目管理,持续集成,持续交付,研发工具云端解决方案
https://sourceforge.net/ | SourceForge - Download, Develop and Publish Free Open Source Software
https://launchpad.net/ | Launchpad
https://bitbucket.org/ | Bitbucket | The Git solution for professional teams
https://coding.net/ | CODING - 一站式软件研发管理平台
https://about.gitlab.com/ | The first single application for the entire DevOps lifecycle - GitLab | GitLab
```

**代码搜索网站**
```
https://searchcode.com/
```

---

# Google

<p align="center">
    <img src="../../../../../assets/img/logo/google.png" width="25%">
</p>

**案例**
- [GGvulnz — How I hacked hundreds of companies through Google Groups](https://medium.com/@milanmagyar/ggvulnz-how-i-hacked-hundreds-of-companies-through-google-groups-b69c658c8924) - 作者描述了如何通过 google group 的搜索结果获得未授权的访问链接

**搜索引擎语法**
- 包含关键字: `intitle:关键字`
- 包含多个关键字: `allintitle:关键字 关键字2`
- 搜索特定类型的文件: `关键字 filetype:扩展名` 例如 `人类简史 filetype:pdf`
- 搜索特定网站的内容: `关键字 site:网址`
- 排除不想要的结果: `关键字 -排查条件`,例如搜索 "运动相机",但只想看 GoPro 品牌以外的产品 `运动相机 -GoPro`
- 双引号的用处:例如: `"how to write a code"` 如果没有引号,搜索的大部分结果是以 `write code` 为关键字.包含引号后,会确保将完整的字符串做为期望的检索结果提交给搜索引擎.

**搜索语法合集**
- [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
- [K0rz3n/GoogleHacking-Page](https://github.com/K0rz3n/GoogleHacking-Page)
- [BullsEye0/google_dork_list](https://github.com/BullsEye0/google_dork_list)

**例子**
- **常见语法**
    ```
    site:*.site.com -www
    site:*.*.site.com -www
    site:*.*.*.site.com -www

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

- **黑产 seo 关键词**
    - 钱
        - 博彩
        - 私服
        - 页游
        - 棋牌
        - 网贷
        ```
        老虎机
        澳门银行
        万博亚洲官网
        狗万app
        新万博官网
        ylg9999
        九州娱乐
        澳门威尼斯人
        威尼斯人
        大红鹰葡京会
        振动盘
        澳门银河
        永利娱乐场
        太阳城集团
        金沙娱乐
        Bet365
        钱柜娱乐
        永利娱乐
        百家乐
        博必发
        亿鼎博
        六合彩
        pk10
        bet365
        扑克王
        金殿
        线上娱乐
        时时彩
        北京赛车
        开奖结果
        私家侦探
        特码
        枪改
        九鼎娱乐
        光速下载
        公平信誉
        千亿体育
        ```
    - 色
        - 视频网站
        - 直播
        - 论坛
        - 游戏
        ```
        商务模特
        会所推荐
        洗浴休闲
        找鸡上门
        外围女
        按摩服务
        大保健
        ```
    - [fwwdn/sensitive-stop-words](https://github.com/fwwdn/sensitive-stop-words) - 互联网常用敏感词、停止词词库
    - [observerss/textfilter](https://github.com/observerss/textfilter) - 敏感词过滤的几种实现+某1w词敏感词
    - [lining0806/TextMining](https://github.com/lining0806/TextMining) - 敏感词过滤系统
    - [funNLP/data/敏感词库](https://github.com/fighting41love/funNLP/tree/master/data/%E6%95%8F%E6%84%9F%E8%AF%8D%E5%BA%93) - 反动词表、暴恐词表
    - [IllegalWordsDetection/blob/master/MinGanCi.txt](https://github.com/NewbieGameCoder/IllegalWordsDetection/blob/master/MinGanCi.txt) - 敏感词
    - [Ldundun/DFA/blob/master/sw.txt](https://github.com/Ldundun/DFA/blob/master/sw.txt) - 敏感词
    - [qloog/sensitive_words](https://github.com/qloog/sensitive_words) - 敏感词库整理
    - [57ing/Sensitive-word](https://github.com/57ing/Sensitive-word) -  收集的一些敏感词汇，细分了暴恐词库、反动词库、民生词库、色情词库、贪腐词库、其他词库等
    - [bzvs1992/SensitiveWordFilter](https://github.com/bzvs1992/SensitiveWordFilter)
    - [adlered/DangerousSpamWords](https://github.com/adlered/DangerousSpamWords) - 超轻量的中文敏感字、敏感词库，字典词典

- **漏洞**
    ```
    目录遍历漏洞
        site:xxx.com intitle:index.of
        site:xxx.com intitle:转到父目录

    配置文件泄露
        site:xxx.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | extra | ext:ini

    数据库文件泄露
        site:xxx.com ext:sql | ext:dbf | ext:mdb

    日志文件泄露
        site:xxx.com ext:log

    备份和历史文件
        site:xxx.com ext:bkf | ext:bkp | ext:bak | extld | ext:backup

    SQL错误
        site:xxx.com intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"

    公开文件信息
        site:xxx.com ext:doc | ext:docx | extdt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv

    phpinfo()
        site:xxx.com ext:php intitle:phpinfo "published by the PHP Group"

    JIRA
        配置错误的 JIRA 设置  inurl:/UserPickerBrowser.jspa -intitle:Login -intitle:Log
        此查询列出了其 URI 中具有"UserPickerBrowser"的所有 URL,以查找公开而且不需要经过身份验证的所有配置错误的 JIRA 用户选择器功能.

        inurl:/ManageFilters.jspa?filterView=popular AND ( intext:All users OR intext:Shared with the public OR intext:Public )
        此查询列出了所有在其 URI 中具有"Managefilters"并且文本为"Public"的 URL,以便找到所有公开暴露且未经过身份验证的错误配置的 JIRA 过滤器.

        inurl:/ConfigurePortalPages!default.jspa?view=popular
        此查询列出其 URI 中具有"ConfigurePortalPages"的所有 URL,以查找公开公开的所有 JIRA 仪表板.
    ```

    ```
    找文章
        inurl:csdn.net CVE-2019-3403
        inurl:51cto.com VRRP
        inurl:habr.com powershell
        inurl:exploit-db.com docker
    ```

    ```
    工控
        inurl:/Portal/Portal.mwsl
        intitle:Miniweb Start Page | /CSS/Miniweb.css
        intitle:Rockwell Automation Device Name Uptime
        inurl:dtm.html intitle:1747-L552
        inurl:dtm.html intitle:1747-L551
        inurl:home.htm intitle:1766
    ```

**CSE**

> Google Custom Search(自定义搜索)是基于谷歌的核心搜索技术，对你的搜索引擎进行很多定制

- TikTok : https://cse.google.com/cse?cx=011444696387487602669:aqf7d9w73om
- IFTT : https://cse.google.com/cse?cx=000501358716561852263:xzfiqchwcj8
- Google Album archives : https://cse.google.com/cse?cx=006205189065513216365:vp0ly0owiou
- Social media : https://cse.google.com/cse?cx=016621447308871563343:0p9cd3f8p-k
- LinkedIn : https://cse.google.com/cse?cx=000470283453218169915:hcrzdwsiwrc
- Online bookmark sites : https://cse.google.com/cse?cx=005797772976587943970:3tu7im1-rdg
- Forums : https://cse.google.com/cse?cx=002396771074467716933:gkp6fzl_dv0

---

# Shodan

<p align="center">
    <img src="../../../../../assets/img/logo/shodan.png" width="35%">
</p>

> Shodan 是目前最为知名的黑客搜索引擎，它是由计算机程序员约翰·马瑟利（John Matherly）于2009年推出的，他在2003年就提出了搜索与 Internet 链接的设备的想法。发展至今已经变成搜索资源最全，搜索性能最强的网络资产搜索引擎。简述下 shodan 的工作原理：通过其强大的爬虫能力每隔一定时间扫描全互联网设备并抓取相应的 banner 信息建立索引，通过这些巨大的数据，你基本可以找到任何你想象得到的连接到互联网的东西。

**官网**
- https://www.shodan.io

> 搜索结果略不满意,会员实际较为鸡肋

> 无论付费用户还是免费用户，都可以使用shodan的搜索功能，只不过付费用户可以获得更多的搜索结果和导出、监控等更多高级功能。

**手册**
- [shodan-manual](https://b404.gitbooks.io/shodan-manual/content/)
- [Shodan Pentesting Guide](https://community.turgensec.com/shodan-pentesting-guide/)

**文章**
- [Shodan新手入坑指南](https://www.freebuf.com/sectool/121339.html)
- [How to Discover MongoDB and Elasticsearch Open Databases](https://habr.com/en/post/443132/)
- [Shodan新手入坑指南](https://www.freebuf.com/sectool/121339.html)
- [shodan-manual](https://b404.gitbooks.io/shodan-manual/)

**搜索语法合集**
- [jakejarvis/awesome-shodan-queries](https://github.com/jakejarvis/awesome-shodan-queries)

**语法**
```bash
hostname:搜索指定的主机或域名,例如 hostname:"google"
port:搜索指定的端口或服务,例如 port:"21"
country:搜索指定的国家,例如 country:"CN"
city:搜索指定的城市,例如 city:"Hefei"
org:搜索指定的组织或公司,例如 org:"google"
isp:搜索指定的 ISP 供应商,例如 isp:"China Telecom"
product:搜索指定的操作系统/软件/平台,例如 product:"Apache httpd"
version:搜索指定的软件版本,例如 version:"1.6.2"
geo:搜索指定的地理位置,参数为经纬度,例如 geo:"31.8639, 117.2808"
before/after:搜索指定收录时间前后的数据,格式为 dd-mm-yy,例如 before:"11-11-15"
net:搜索指定的 IP 地址或子网,例如 net:"210.45.240.0/24"
```

**例子**
```bash
# 友情提醒,请遵纪守法
misc
Server: uc-httpd 1.0.0 200 OK Country:"JP"
h3c net:"61.191.146.0/24"
country:US vuln:CVE-2014-0160
port:135,139,445 -hash:0                        # 过滤一些主文本标题为空的搜索结果
Hikvision-Webs                                  # 海康威视
title=“后台管理”
http.title:"后台管理"

database
all:"mongodb server information" all:"metrics"  # 开放 Mongodb 数据库
port:27017 -all:"partially" all:"fs.files"      # 有点存货的 Mongodb 数据库
port:"9200" all:"elastic indices"               # 开放 ElasticSearch 数据库

ftp
230 'anonymous@' login ok                       # 开放匿名ftp

vnc
port:5900 screenshot.label:loggedin             # 无认证vnc

rtsp
port:554 has_screenshot:true                    # rtsp 未授权访问

docker
port:"2375" country:"JP" Docker                 # docker-remote-api未授权

ICS
module: s7 port:102                             # S7设备
```

**外部工具/脚本**

- **Shodan cli**
    - [Shodan Command-Line Interface](https://cli.shodan.io/)

- **浏览器插件**
    - [chrome插件](https://chrome.google.com/webstore/detail/shodan/jjalcfnidlmpjhdfepjhjbhnhkbgleap)
    - [firefox插件](https://addons.mozilla.org/en-US/firefox/addon/shodan_io/)

- **Metasploit**
    ```bash
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

- **脚本**
    - [random-robbie/My-Shodan-Scripts](https://github.com/random-robbie/My-Shodan-Scripts)
    - [woj-ciech/LeakLooker](https://github.com/woj-ciech/LeakLooker) - 利用 shodan 寻找开放的数据库/服务

**其他功能**
- [ICS Radar](https://ics-radar.shodan.io/)

    > ICS Radar 是 Shodan 的工业控制系统（ICS）设备的 3D 地图。

- [Honeypot score](https://honeyscore.shodan.io/)

    > 这个服务叫 Honeypot or not?，这个服务会把 Honeyscore 归属到一个 IP 地址上，也就是成为蜜罐的可能性。

- [Shodan 2000](https://2000.shodan.io/#/)

    > Sodan 2000 是一个类似 Tron 的界面，可以随机显示一个主机。

---

# BinaryEdge

<p align="center">
    <img src="../../../../../assets/img/logo/binaryedge.png" width="15%">
</p>

> BinaryEdge 是一家来自瑞士的公司提供的资产搜索引擎，其为企业提供网络安全，工程和数据科学解决方案的评估。它利用机器学习技术收集有关基础设施的信息，并将收集的数据与从提要中获得的数据相关联。功能包括通过将发现结果与安全工具结合后从联网设备和运行于它们的服务中提取数据来提供通知，警报和报告功能。

**官网**
- https://www.binaryedge.io/

**语法**

- https://docs.binaryedge.io/search/
```bash
ip	                # 目标 IP,例如 ip：“ 149.202.178.130/16”
port	            # 端口,例如 port：80
country             # 目标国家/地区,例如国家/地区：FR
ASN                 # 目标的 AS 号，例如asn：1234
type	            # BinaryEdge 模块类型，例如类型：mongodb
product	            # 所寻找的产品名称，例如产品：apache2
ipv6	            # 过滤 ipv6 结果，例如 Ipv6：true 或 ipv6：false
tag	                # 可用标签列表：docs.binaryedge.io/search/#available-tags
```

**例子**
```bash
country:FR port:443                 # SSL from a Specific Organization Name
ip:"149.202.178.130/16" port:80     # CIDR 149.202.178.130/16 and Port 80
"Example Org" type:ssl              # France with Port 443
product:"Dropbear sshd"             # Product Dropbear sshd
```

---

# Censys

<p align="center">
    <img src="../../../../../assets/img/logo/censys.png" width="25%">
</p>

> Censys 搜索引擎能够扫描整个互联网，Censys 每天都会扫描 IPv4 地址空间，以搜索所有联网设备并收集相关的信息，并返回一份有关资源（如设备、网站和证书）配置和部署信息的总体报告。

**官网**
- https://www.censys.io

**例子**
```bash
23.0.0.0/8 or 8.8.8.0/24                    # 可以使用 and or not
80.http.get.status_code: 200                # 指定状态
80.http.get.status_code:[200 TO 300]        # 200-300之间的状态码
location.country_code: DE                   # 国家
protocols: ("23/telnet" or "21/ftp")        # 协议
tags: scada                                 # 标签
80.http.get.headers.server:nginx            # 服务器类型版本
autonomous_system.description: University   # 系统描述
```

**同类搜索引擎**
- [Spyse](https://spyse.com/search/cert) - 扫描完整的数字证书数据库，获取 TLS 和 SSL 证书的相关数据。
- [crt.sh](https://crt.sh/) - 证书搜索
- [Google Transparency Report](https://transparencyreport.google.com/https/certificates) - Google监控的证书透明日志

---

# Zoomeye

<p align="center">
    <img src="../../../../../assets/img/logo/zoomeye.png" width="25%">
</p>

> ZoomEye 是北京知道创宇公司发布的网络空间侦测引擎，积累了丰富的网络扫描与组件识别经验。在此网络空间侦测引擎的基础上，结合“知道创宇”漏洞发现检测技术和大数据情报分析能力，研制出网络空间雷达系统，为政府、企事业及军工单位客户建设全球网络空间测绘提供技术支持及产品支撑。

**官网**
- https://www.zoomeye.org/

**语法**
```bash
指定搜索的组件：
    app：组件名称
    ver：组件版本
    例：搜索 apache组件版本2.4：app:apache var:2.4
指定搜素的端口：
    port:22
指定搜索的操作系统：
    OS:Linux
指定搜索的服务：
    service：服务名称
    例：service：SSH
指定搜索的地理位置范围：
    country：国家名
    city:城市名
指定搜索的CIDR网段：
    cidr:网段
    例：CIDR：192.168.158.12/24
指定网站域名进行搜索：
    Site:网站域名
    例：site:www.baidu.com
指定主机名：
    Hostname:主机名
    例：hostname:zwl.cuit.edu.cn
指定设备名：
    device:设备名
    例：device:router
指定首页关键词：
    keyword:关键词
    例：keyword:technology
```

**例子**
```bash
city:tokyo + app:weblogic

port:102 +app:"Siemens S7 PLC"
```

**ZoomEye工控专题**
- https://www.zoomeye.org/topic?id=ics_project

---

# FoFa

<p align="center">
    <img src="../../../../../assets/img/logo/fofa.png" width="30%">
</p>

> FOFA 是白帽汇推出的一款网络空间搜索引擎，它通过进行网络空间测绘，能够帮助研究人员或者企业迅速进行网络资产匹配，例如进行漏洞影响范围分析、应用分布统计、应用流行度排名统计等。

**官网**
- https://fofa.so

**相关文章**
- [工具的使用 | 网络空间搜索引擎Fofa的简单使用](https://mp.weixin.qq.com/s/2uLSOZHvIX_KLTwpp9sGfA)

**语法**
```bash
title="abc"         # 从标题中搜索 abc.例:标题中有北京的网站.
header="abc"        # 从 http 头中搜索abc.例:jboss服务器.
body="abc"          # 从 html 正文中搜索abc.例:正文包含Hacked by.
domain="qq.com"     # 搜索根域名带有qq.com的网站.例: 根域名是qq.com的网站.
host=".gov.cn"      # 从 url 中搜索.gov.cn,注意搜索要用host作为名称.
port="443"          # 查找对应 443 端口的资产.例: 查找对应443端口的资产.
ip="1.1.1.1"        # 从ip中搜索包含 1.1.1.1 的网站,注意搜索要用ip作为名称.
protocol="https"    # 搜索制定协议类型(在开启端口扫描的情况下有效).例: 查询https协议资产.
city="Beijing"      # 搜索指定城市的资产.例: 搜索指定城市的资产.
region="Zhejiang"   # 搜索指定行政区的资产.例: 搜索指定行政区的资产.
country="CN"        # 搜索指定国家(编码)的资产.例: 搜索指定国家(编码)的资产.
cert="google.com"   # 搜索证书(https或者imaps等)中带有google.com的资产.
```

**例子**
```bash
title="powered by" && title!=discuz
title!="powered by" && body=discuz
(body="content=\"WordPress" || (header="X-Pingback" && header="/xmlrpc.php" && body="/wp-includes/") ) && host="gov.cn"

app="Solr" && title=="Solr Admin"   # 找 solr 服务
app="Coremail" &&  country=CN       # 查找使用 coremail 并且在中国境内的网站
title="管理后台" ||  title="登录后台"  # 查找 title 中含有管理后台或者登录后台的网站
port=”102″ && protocol==”s7″        # 找 S7comm设备
```

---

# Dnsdb

<p align="center">
    <img src="../../../../../assets/img/logo/dnsdb.png" width="30%">
</p>

> 这是一个搜索全网络所有 DNS 服务器的搜索引擎。

**官网**
- https://www.dnsdb.io/

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

---

# 知风

<p align="center">
    <img src="../../../../../assets/img/logo/zhifen.png" width="15%">
</p>

> “知风”提出了一种互联网联网工控资产自动化分析方式，基于分析结果将可真正帮助用户了解目前接入互联网的工控资产是何企业所属，接入时间，系统名称等。利用“知风”积累的企业和系统数据，您使用“知风”时只需输入企业简称或系统简称，即可了解目标系统企业和系统是否有工控资产联网情况，借助“知风”您也可以了解您的企业、系统是否存在遭受互联网攻击的可能。

**官网**
- https://zhifeng.io/monitor

---

# ONYPHE

<p align="center">
    <img src="../../../../../assets/img/logo/ONYPHE.png" width="5%">
</p>

>  很像Shodan，但除了扫描之外，它还可以从被动DNS查询、威胁列表查询和粘贴网站查询中抓取数据。不过免费版比起Shodan来说，它的局限性更大。

**官网**
- https://www.onyphe.io/

---

# GreyNoise

<p align="center">
    <img src="../../../../../assets/img/logo/greynoise.png" width="15%">
</p>

> 类似 shodan

**官网**
- https://viz.greynoise.io/

---

# Thingful

<p align="center">
    <img src="../../../../../assets/img/logo/thingful.png" width="20%">
</p>

> 仅针对物联网的搜索引擎

**官网**
- https://www.thingful.net/
