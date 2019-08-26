## apache+mod_ssl⚾
配置 http+https 服务，建立一个 web 站点；

0. 安装
```bash
yum -y install httpd
yum -y install mod_ssl
```

1. 使用 www.abc.com 作为域名进行访问；
```bash
nslookup www.abc.com
```

2. 网站根目录为 /var/www/html；
```vim
vim /etc/httpd/conf/httpd.conf
		DocumentRoot "/var/www/html"
		ServerName  xx.xx.xx.xx:80     ////设置Web服务器的主机名和监听端口
```

3. Index.html 内容使用 fubuki!fubuki!fubuki!fubuki!；
```vim
vim var/www/html/index.html
	fubuki!fubuki!fubuki!fubuki!

service httpd restart 或 systemctl start httpd
```
关防火墙

4. 配置 https 服务使原站点能使用 https 访问。

	> 查看证书密钥位置
	> sed ‐n '/^SSLCertificateFile/p;/^SSLCertificateKeyFile/p '/etc/httpd/conf.d/ssl.conf

	> 删除原来的密钥
	> cd /etc/pki/tls/private/
	> rm ‐f localhost.key

	> 新建密钥文件
	> openssl genrsa 1024 > localhost.key

	> 删除原来的证书
	> cd ../certs
	> rm ‐rf localhost.crt

	> 新建证书文件
	> openssl req ‐new ‐x509 ‐days 365 ‐key ../private/localhost.key ‐out localhost.crt

	> 开下 https 防火墙，重启服务，测试

设置 SELINUX 状态为 Disabled；
> setenforce 0

```vim
vim /etc/selinux/config
	SELINUX=disabled
```
---

**18-I**
A
- 配置 http 服务，以虚拟主机的方式创建 web 站点
- 将 /etc/httpd/conf.d/ssl.conf 重命名为 ssl.conf.bak
- 配置文件名为 virthost.conf，放置在 /etc/httpd/conf.d 目录下；
- 配置 https 功能，https 所用的证书 httpd.crt、私钥 httpd.key 放置在 /etc/httpd/ssl目录中（目录需自己创建）；
- 使用 www.abc.com 作为域名进行访问；
- 网站根目录为 /data/web_data；
- 提供 http、https 服务，仅监听 192.168.1XX.22 的 IP 地址；
- index.html 内容使用 Welcome to 2018 Computer Network Application contest!；

安装
```bash
yum -y install httpd
yum -y install mod_ssl
```

配置虚拟主机文件
```vim
vim /etc/httpd/conf.d/virthost.conf
<VirtualHost 192.168.1xx.22:80>
	ServerName  www.abc.com     ////设置 Web 服务器的主机名和监听端口
	DocumentRoot "/data/web_data"
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>

Listen 192.168.1XX.33:443
<VirtualHost 192.168.1xx.22:443>
	ServerName  www.abc.com     ////设置 Web 服务器的主机名和监听端口
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

index.html 内容使用 Welcome to 2018 Computer Network Application contest!
```vim
mkdir -p /data/web_data
vim /data/web_data/index.html
	Welcome to 2018 Computer Network Application contest!
```

创建证书
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

curl http://www.abc.com
curl https://www.abc.com


B
配置 http 服务，以虚拟主机的方式创建 web 站点
将 /etc/httpd/conf.d/ssl.conf 重命名为 ssl.conf.bak
配置文件名为 virthost.conf，放置在 /etc/httpd/conf.d目录下；
配置 https 功能，https 所用的证书httpd.crt、私钥 httpd.key 放置在 /etc/httpd/ssl 目录中（目录需自己创建，httpd.crt、httpd.key 均文件从 serverA 复制）；
使用 www.abc.com 作为域名进行访问；
提供 http、https 服务，仅监听 192.168.1XX.33 的地址。

安装
```
yum -y install httpd
yum -y install mod_ssl
```

配置虚拟主机文件
```bash
vim /etc/httpd/conf.d/virthost.conf
<VirtualHost 192.168.1xx.33:80>
	ServerName  www.abc.com     ////设置 Web 服务器的主机名和监听端口
	DocumentRoot "/data/web_data"
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>

Listen 192.168.1XX.33:443
<VirtualHost 192.168.1xx.33:443>
	ServerName  www.abc.com     ////设置 Web 服务器的主机名和监听端口
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

index.html 内容使用 Welcome to 2018 Computer Network Application contest!
```vim
mkdir -p /data/web_data
vim /data/web_data/index.html
	Welcome to 2018 Computer Network Application contest! B
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

配置 http 服务，以虚拟主机的方式建立一个 web 站点；
配置文件名为 virthost.conf，放置在 /etc/httpd/conf.d 目录下；
仅监听 192.168.2.22:8080 端口；
使用 www.abc.com 作为域名进行访问；
网站根目录为 /data/web_data；
index.html 内容使用 Welcome to 2018 Computer Network Application contest!。

安装
```bash
yum -y install httpd
yum -y install mod_ssl
```

配置虚拟主机文件
```bash
vim /etc/httpd/conf.d/virthost.conf
Listen 192.168.2.22:8080
<VirtualHost 192.168.2.22:8080>
	ServerName  www.abc.com     ////设置 Web 服务器的主机名和监听端口
	DocumentRoot "/data/web_data"
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>
```

index.html 内容使用 Welcome to 2018 Computer Network Application contest!
```vim
mkdir -p /data/web_data
vim /data/web_data/index.html
	Welcome to 2018 Computer Network Application contest! B
```

```bash
httpd -t # 检查配置
setenforce 0
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload
service httpd start
```
