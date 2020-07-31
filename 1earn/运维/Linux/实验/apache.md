# apache

---

**Apache 与 httpd 的区别与关系**

从我们仅仅web服务器使用者的角度说的话，它们是同一个东西。在 Apache 的网站上有两种安装包下载
httpd-2.0.50-i686-pc-linux-gnu.tar.gz   和 apache_1.3.33-i686-whatever-linux22.tar.gz
其实都是提供 Web 服务的，只是一个是早期版一个是新的版本模式。

httpd 是 apache 开源项目的一部分，如果只需要 web 服务器，现在只需安装 httpd2.* 就可以了。

早期的 Apache 小组，现在已经成为一个拥有巨大力量的 Apache 软件基金会，而 apache 现在成为 apache 基金会下几十种开源项目的标识。其中有一个项目做 HTTP Server，httpd 是 HTTP  Server 的守护进程，在 Linux 下最常用的是 Apache，所以一提到 httpd 就会想到 Apache HTTP Server。

他们把起家的 apache 更名为 httpd，也更符合其 http server 的特性。以前 apache 的 http server 在 1.3 的时候直接叫 apache_1.3.37，现在 2.* 版本的都叫 httpd_2.2.3。在 Linux 下最常用的是 Apache，所以一提到 httpd 就会想到 Apache HTTP Server。

---

# 案例1

- 配置 http 服务，以虚拟主机的方式建立一个 web 站点;
- 配置文件名为 virthost.conf，放置在 `/etc/httpd/conf.d` 目录下;
- 仅监听 192.168.2.22:8080 端口;
- 使用 www.abc.com 作为域名进行访问;
- 网站根目录为 `/data/web_data` ;
- index.html 内容使用 fubuki!!fubuki!!fubuki!!fubuki!!.

**安装**
```bash
yum -y install httpd
yum -y install mod_ssl
```

**配置虚拟主机文件**
```bash
vim /etc/httpd/conf.d/virthost.conf

Listen 192.168.2.22:8080
<VirtualHost 192.168.2.22:8080>
	ServerName  www.abc.com
	DocumentRoot "/data/web_data"
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>
```

index.html 内容使用 fubuki!!fubuki!!fubuki!!fubuki!!
```bash
mkdir -p /data/web_data
```
```vim
vim /data/web_data/index.html

fubuki!!fubuki!!fubuki!!fubuki!!
```

```bash
httpd -t # 检查配置
setenforce 0
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload
service httpd start
```

---

# 案例2
## A

- 配置 http 服务，以虚拟主机的方式创建 web 站点
- 将 `/etc/httpd/conf.d/ssl.conf` 重命名为 ssl.conf.bak
- 配置文件名为 virthost.conf，放置在 `/etc/httpd/conf.d` 目录下;
- 配置 https 功能，https 所用的证书 httpd.crt、私钥 httpd.key 放置在 `/etc/httpd/ssl` 目录中(目录需自己创建);
- 使用 www.abc.com 作为域名进行访问;
- 网站根目录为 `/data/web_data` ;
- 提供 http、https 服务，仅监听 192.168.1XX.22 的 IP 地址;
- index.html 内容使用 fubuki!!fubuki!!fubuki!!fubuki!!;

**安装**
```bash
yum -y install httpd
yum -y install mod_ssl
```

**配置虚拟主机文件**
```vim
vim /etc/httpd/conf.d/virthost.conf

<VirtualHost 192.168.1xx.22:80>
	ServerName  www.abc.com
	DocumentRoot "/data/web_data"
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>

Listen 192.168.1XX.33:443
<VirtualHost 192.168.1xx.22:443>
	ServerName  www.abc.com
	DocumentRoot "/data/web_data"

	SSLEngine on
	SSLCertificateFile /etc/httpd/ssl/httpd.crt
	SSLCertificateKeyFile /etc/httpd/ssl/httpd.key

	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>
```

!!!!注意，必须要改名，大坑
> mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.bak

index.html 内容使用 fubuki!!fubuki!!fubuki!!fubuki!!
```bash
mkdir -p /data/web_data
```
```vim
vim /data/web_data/index.html

fubuki!!fubuki!!fubuki!!fubuki!!
```

**创建证书**
```bash
>cd /etc/pki/CA/private
>openssl genrsa 2048 > cakey.pem
>openssl req -new -x509 -key cakey.pem > /etc/pki/CA/cacert.pem

cd /etc/pki/CA
touch index.txt	# 索引问文件
touch serial	# 给客户发证编号存放文件
echo 01 > serial

mkdir /etc/httpd/ssl
cd /etc/httpd/ssl
openssl genrsa 1024 > httpd.key
openssl req -new -key httpd.key > httpd.csr
openssl ca -days 365 -in httpd.csr > httpd.crt

# 查看 openssl 证书数据库文件
cat /etc/pki/CA/index.txt
```

```bash
httpd -t	# 检查配置
setenforce 0
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --zone=public --add-service=https --permanent
firewall-cmd --reload
service httpd start
```
```bash
curl http://www.abc.com
curl https://www.abc.com
```

## B

- 配置 http 服务，以虚拟主机的方式创建 web 站点
- 将 `/etc/httpd/conf.d/ssl.conf` 重命名为 ssl.conf.bak
- 配置文件名为 virthost.conf，放置在 `/etc/httpd/conf.d` 目录下;
- 配置 https 功能，https 所用的证书httpd.crt、私钥 httpd.key 放置在 `/etc/httpd/ssl` 目录中(目录需自己创建，httpd.crt、httpd.key 均文件从 serverA 复制);
- 使用 www.abc.com 作为域名进行访问;
- 提供 http、https 服务，仅监听 192.168.1XX.33 的地址.

**安装**
```
yum -y install httpd
yum -y install mod_ssl
```

**配置虚拟主机文件**
```vim
vim /etc/httpd/conf.d/virthost.conf

<VirtualHost 192.168.1xx.33:80>
	ServerName  www.abc.com
	DocumentRoot "/data/web_data"
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>

Listen 192.168.1XX.33:443
<VirtualHost 192.168.1xx.33:443>
	ServerName  www.abc.com
	DocumentRoot "/data/web_data"

	SSLEngine on
	SSLCertificateFile /etc/httpd/ssl/httpd.crt
	SSLCertificateKeyFile /etc/httpd/ssl/httpd.key

	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>
```

> mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.bak

index.html 内容使用 fubuki!!fubuki!!fubuki!!fubuki!!
```bash
mkdir -p /data/web_data
```
```vim
vim /data/web_data/index.html

fubuki!!fubuki!!fubuki!!fubuki!!
```

```bash
mkdir /etc/httpd/ssl
cd /etc/httpd/ssl

scp root@192.168.1xx.22:/etc/httpd/ssl/httpd.key /etc/httpd/ssl/httpd.key
scp root@192.168.1xx.22:/etc/httpd/ssl/httpd.crt /etc/httpd/ssl/httpd.crt
```

```bash
httpd -t	# 检查配置
setenforce 0
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --zone=public --add-service=https --permanent
firewall-cmd --reload
service httpd start
```

---

# 目录结构

**apache2**

`/etc/apache2`

- apache2.conf : 这是服务器的主要配置文件。几乎所有的配置都可以在这个文件中完成，不过为了简单起见，建议使用单独的指定文件。这个文件将配置默认值，是服务器读取配置细节的中心点。

- ports.conf : 这个文件用于指定虚拟主机应该监听的端口。如果你在配置 SSL，请务必检查这个文件是否正确。

- conf.d/ : 这个目录用于控制 Apache 配置的特定方面。例如，它经常被用来定义 SSL 配置和默认安全选择。

- sites-available/ : 这个目录包含了所有定义不同网站的虚拟主机文件。这些文件将确定哪些内容被服务于哪些请求。这些是可用的配置，而不是活动的配置。

- sites-enabled/ : 这个目录确定了实际使用的虚拟主机定义。通常，这个目录由 "sites-available"目录中定义的文件的符号链接组成。

- mods-[enabled,available]/ : 这些目录在功能上与网站目录类似，但它们定义了可以选择加载的模块。

---

# apache+mod_ssl

- 配置 http+https 服务，建立一个 web 站点;

0. 安装
```bash
yum -y install httpd
yum -y install mod_ssl
```

1. 使用 www.abc.com 作为域名进行访问;
```bash
nslookup www.abc.com
```

2. 网站根目录为 /var/www/html;
```vim
vim /etc/httpd/conf/httpd.conf

	DocumentRoot "/var/www/html"
	ServerName  xx.xx.xx.xx:80
```

3. Index.html 内容使用 fubuki!fubuki!fubuki!fubuki!;
```vim
vim var/www/html/index.html

fubuki!fubuki!fubuki!fubuki!
```
```bash
service httpd restart 或 systemctl start httpd
记得关防火墙
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload
```

4. 配置 https 服务使原站点能使用 https 访问.
```bash
# 查看证书密钥位置
sed -n '/^SSLCertificateFile/p;/^SSLCertificateKeyFile/p '/etc/httpd/conf.d/ssl.conf

# 删除原来的密钥
cd /etc/pki/tls/private/
rm -f localhost.key

# 新建密钥文件
openssl genrsa 1024 > localhost.key

# 删除原来的证书
cd ../certs
rm -rf localhost.crt

# 新建证书文件
openssl req -new -x509 -days 365 -key ../private/localhost.key -out localhost.crt

防火墙放行 https，重启服务，测试
```
设置 SELINUX 状态为 Disabled;
```bash
setenforce 0
```
```vim
vim /etc/selinux/config

SELINUX=disabled
```

---

# 配置https

**使用 Let’s Encrypt 直接上 https**
```bash
yum install -y yum-utils
yum-config-manager --enable rhui-REGION-rhel-server-extras rhui-REGION-rhel-server-optional
yum install -y certbot python2-certbot-apache

certbot --apache
firewall-cmd --zone=public --add-service=https --permanent
firewall-cmd --reload
```

**mod_ssl 为 linux 提供 web 证书**

```bash
cd /etc/pki/CA/private
openssl genrsa 2048 > cakey.pem
openssl req -new -x509 -key cakey.pem > /etc/pki/CA/cacert.pem

cd /etc/pki/CA
touch index.txt     # 索引问文件
touch serial        # 给客户发证编号存放文件
echo 01 > serial

mkdir /etc/httpd/ssl
cd /etc/httpd/ssl
openssl genrsa 1024 > httpd.key
openssl req -new -key httpd.key > httpd.csr
openssl ca -days 365 -in httpd.csr > httpd.crt

# 使用 cat /etc/pki/CA/index.txt 查看 openssl 证书数据库文件
cat /etc/pki/CA/index.txt
```

**mod_ssl 为 windows 提供 web 证书**

```bash
cd /etc/pki/CA/private
openssl genrsa 2048 > cakey.pem
openssl req -new -x509 -key cakey.pem > /etc/pki/CA/cacert.pem

cd /etc/pki/CA
touch index.txt   # 索引问文件
touch serial      # 给客户发证编号存放文件
echo 01 > serial

cd
openssl genrsa 1024 > httpd.key
openssl req -new -key httpd.key > httpd.csr
openssl ca -days 365 -in httpd.csr > httpd.crt

openssl pkcs12 -export -out server.pfx -inkey httpd.key -in httpd.crt
# 自己把 server.pfx 导出给 windows2008 主机
```

**向 windows CA 服务器申请证书**

```bash
Openssl genrsa 2048 > httpd.key
openssl req -new -key httpd.key -out httpd.csr
```
通过这个 csr 文件在内部的 windows CA 服务器上申请证书

---

# 配置php

<p align="center">
    <img src="../../../../assets/img/logo/php.svg" width="20%">
</p>

```bash
若之前安装过其他版本 PHP,先删除
yum remove php*

rpm 安装 PHP7 相应的 yum 源
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
yum install php70w php70w-fpm

php -v                # 查看PHP版本

service php-fpm start # 要运行 PHP 网页,要启动 php-fpm 解释器
```
```bash
vim /etc/httpd/conf/httpd.conf

# 将Require all denied 改为Require all granted
<Directory />
    AllowOverride none
    Require all granted
</Directory>

# 增加一行 AddType application/x-httpd-php .php
    AddType application/x-httpd-php .php

# 增加索引页 index.php,在 DirectoryIndex index.html 后面 增加索引页 index.php
<IfModule dir_module>
    DirectoryIndex index.html index.php
</IfModule>
```

检查配置文件 httpd.conf 的语法是否正确
```bash
apachectl -t
```

检测 php 是否正常解析
```
echo "<?php phpinfo(); ?>"  > /var/www/html/1.php

service httpd restart
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
```

访问 `机器相应ip/1.php`

---

**Source & Reference**
- [Linux下Apache与httpd的区别与关系](https://blog.csdn.net/yxfabcdefg/article/details/32324035)
