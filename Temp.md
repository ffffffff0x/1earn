# Temp
项目暂存地，这里的内容会被加入到各md文档中




pthon虚拟环境env
pip install virtualenv
创建一个文件夹
进入上一步创建的文件夹virtualenv envtest

进入虚拟环境的script文件夹，并执行activate
安装模块






VMware vCenter Server Struts组件安全漏洞(CVE-2014-0114)(VMSA-2014-0008.2)
use exploit/multi/http/struts_code_exec_classloader


VMware vCenter Server JMX RMI远程代码执行漏洞(CVE-2015-2342)(VMSA-2015-0007.6)
use exploit/multi/misc/java_jmx_server


902 vmware authentication服务
 VMware ESX/GSX 服务


SMTP
利用SMTP/VRFY命令可猜测目标主机上的用户名
telnet <target> 25
HELO nonexist
VRFY root


PHP 'php_zip.c' 目录遍历漏洞（CVE-2014-9767）
 PHP PharData类目录遍历漏洞(CVE-2015-6833)

SNMP服务存在可写口令(CVE-1999-0516)

Memcached 未授权访问漏洞

Elasticsearch 未授权访问

Redis 未授权访问漏洞

Hadoop 未授权访问

wget http://download.redis.io/releases/redis-3.2.0.tar.gz

CVE-2015-0240

FreeRDP

CVE-2017-7546

 vim 任意代码执行漏洞(CVE-2016-1248)

upnp





frp

如何知道自己网站使用了哪些http方法？
nmap -p 80 --script http-methods


https://www.secpulse.com/archives/61101.html
https://www.cnblogs.com/pannengzhi/p/2017-09-23-web-file-disclosure.html


http://www.91ri.org/15441.html

https://www.cnblogs.com/KevinGeorge/category/1145166.html
https://www.anquanke.com/post/id/85043
https://hellohxk.com/blog/php-deserialization/


docker
    CVE-2019-5736

CouchDB漏洞 	 CVE–2017–12635 CVE–2017–12636 
Jenkins Java反序列化远程代码执行漏洞 	CVE-2017-1000353

PHP-CGI Argument Injection Remote Code Execution 
JBoss反序列化命令执行漏洞 	CVE-2017-12149 	8220挖矿团伙

Drupal Drupalgeddon 2远程代码执行 	CVE-2018-7600 	8220挖矿团伙
 CVE-2018-7602 

VBScript引擎远程代码执行漏洞 	CVE-2018-8174 	
Rig Exploit Kit利用该漏洞分发门罗比挖矿代码

Hadoop Yarn REST API未授权漏洞利用

远程桌面协议远程代码执行漏洞 	 CVE-2017-0176

LNK代码执行漏洞 	 CVE–2017–8464





**Todo**
- [ ] badusb
- [ ] Vegile
- [ ] ssrf
- [ ] ASWCrypter
- [ ] VENOM
- [ ] namp脚本
- [ ] xunfeng




Apache





Tomcat
Tomcat默认端口为8080，也可能被改为其他端口，后台管理路径为/manager/html，后台默认弱口令admin/admin、tomcat/tomcat等，若果配置不当，可通过”Tomcat Manager”连接部署war包的方式获取webshell。


Elasticsearch

Apache Solr
https://github.com/mpgn/CVE-2019-0192/


Fastcgi




PHPCGI




IIS




Nginx


jenkins
https://wwws.nightwatchcybersecurity.com/2019/05/23/exploring-the-file-system-via-jenkins-credentials-plugin-vulnerability-cve-2019-10320/






老版本weblogic有一些常见的弱口令，比如weblogic、system、portaladmin和guest等，用户名密码交叉使用。



解析漏洞
IIS解析漏洞一般存在两种情况，一种是.asa和.asp目录下任意文件被当做asp文件来执行，另外一种是.asp;.jpg在IIS6中会被当做asp脚本来执行。
Apache解析漏洞是当遇到不认识的扩展名时，将会从后向前解析，直到碰到认识的扩展名为止，如果都不认识，则直接暴露文件源代码。 

上传漏洞
绕过客户端检测、绕过服务端检测、文本编辑器上传


**Todo**
- [ ] oracle 19c(https://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html)
(http://blog.itpub.net/29785807/viewspace-2633720/)
- [ ] [CouchDB](https://couchdb.apache.org/)
- [ ] [RavenDB](https://ravendb.net)
- [ ] [LiteDB](http://www.litedb.org/)
- [ ] [CockroachDB](https://www.cockroachlabs.com/)
- [ ] [cassandra](https://cassandra.apache.org/)
- [ ] [Elasticsearch](https://www.elastic.co/products/elasticsearch)
- [ ] [Splunk](https://www.splunk.com/)
- [ ] [Teradata](https://www.teradata.com/)
- [ ] [IBM DB2](https://www.ibm.com/analytics/us/en/db2/)
- [ ] [HBase](https://hbase.apache.org/)
- [ ] [Hive](https://hive.apache.org/)
- [ ] [Solr](https://lucene.apache.org/solr/)
`都不要拦着我，我和数据库杠上了`


