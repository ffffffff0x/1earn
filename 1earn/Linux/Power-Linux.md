# Power-Linux🎓
`一起释放linux的巨大能量`
[TOC]

---

# net🏀
```vim
vi /etc/sysconfig/network-scripts/ifcfg-eth0
	DEVICE="enoXXXXXX"
	BOOTPROTO=static　　　　　　　#使用静态IP，而不是由DHCP分配IP
	IPADDR=172.16.102.61
	PREFIX=24
	GATEWAY=172.16.102.254
	HOSTNAME=dns1.abc.com

vi /etc/hosts
	127.0.0.1  test localhost  #修改localhost.localdomain为test，shutdown -r now重启使修改生效

	修改DNS
		vim /etc/resolv.conf
			nameserver 8.8.8.8
```
>service network restart

---

# 配置本地yum源,挂载,安装⚽
挂载到/mnt/cdrom

>	mkdir /mnt/cdrom
>	mount /dev/cdrom /mnt/cdrom/

设置一下自动挂载
```vim
vim /etc/fstab
	/dev/cdrom /mnt/cdrom iso9660 defaults 0 0
```

进入 /etc/yum.repos.d 目录,将其中三个改名或者移走留下 CentOS-Base.repo
```bash
cd /etc/yum.repos.d
rm  CentOS-Media.repo    
rm  CentOS-Vault.repo     
```

编辑 CentOS-Base.repo
```vim
vi CentOS-Base.repo
	baseurl=file:///mnt/cdrom/  #这里为本地源路径
	gpgcheck=0	
	enabled=1    #开启本地源

yum list  #看一下包
```

```bash
安装httpd、mod_ssl、vsftpd
yum -y install httpd
yum -y install mod_ssl
yum -y install vsftpd

安装bind、bind-utils、httpd、mod_ssl、ftp、bzip2软件包的安装
yum -y install bind
yum -y install bind-utils
yum -y install ftp
yum -y install bzip2	
yum -y install vim
```

---

# Vim
常用配置
`sudo vim /etc/vim/vimrc `
最后面直接添加你想添加的配置，下面是一些常用的（不建议直接复制这个货网上的，要理解每个的含义及有什么用，根据自己需要来调整）
```vim
set number #显示行号
set nobackup #覆盖文件时不备份
set cursorline #突出显示当前行
set ruler #在右下角显示光标位置的状态行
set shiftwidth=4 #设定 > 命令移动时的宽度为 4
set softtabstop=4 #使得按退格键时可以一次删掉 4 个空格
set tabstop=4 #设定 tab 长度为 4(可以改）
set smartindent #开启新行时使用智能自动缩进
set ignorecase smartcase #搜索时忽略大小写，但在有一个或以上大写字母时仍 保持对大小写敏感
下面这个没觉得很有用，在代码多的时候会比较好
#set showmatch #插入括号时，短暂地跳转到匹配的对应括号
#set matchtime=2 #短暂跳转到匹配括号的时间
```

---

# apache⚾
配置 http 服务，建立一个 web 站点；

0. 安装
> yum -y install httpd
> yum -y install mod_ssl

1. 使用www.abc.com作为域名进行访问；
>	nslookup www.abc.com

2. 网站根目录为 /var/www/html；
```bash
vi /etc/httpd/conf/httpd.conf
		DocumentRoot "/var/www/html" 
		ServerName  xx.xx.xx.xx:80     ////设置Web服务器的主机名和监听端口
```

3. Index.html内容使用Welcome to 2017 Computer Network Application contest!；
```vim
vi var/www/html/index.html 
	Welcome to 2017 Computer Network Application contest!

service httpd restart或systemctl start httpd
```
关防火墙
			
4. 配置 https 服务使原站点能使用 https 访问。

>查看证书密钥位置
>sed ‐n '/^SSLCertificateFile/p;/^SSLCertificateKeyFile/p '/etc/httpd/conf.d/ssl.conf

>删除原来的密钥
>cd /etc/pki/tls/private/
>rm ‐f localhost.key

>新建密钥文件
>openssl genrsa 1024 > localhost.key

>删除原来的证书
>cd ../certs
>rm ‐rf localhost.crt

>新建证书文件
>openssl req ‐new ‐x509 ‐days 365 ‐key ../private/localhost.key ‐out localhost.crt

>开下 https 防火墙，重启服务，测试


设置 SELINUX 状态为 Disabled；	
>setenforce 0 
```vim
vi /etc/selinux/config
	SELINUX=disabled
```
---

**18-I**
A
- 配置http服务，以虚拟主机的方式创建web站点
- 将/etc/httpd/conf.d/ssl.conf重命名为ssl.conf.bak
- 配置文件名为virthost.conf，放置在/etc/httpd/conf.d目录下；
- 配置https功能，https所用的证书httpd.crt、私钥httpd.key放置在/etc/httpd/ssl目录中（目录需自己创建）；
- 使用www.rj.com作为域名进行访问；
- 网站根目录为/data/web_data；
- 提供http、https服务，仅监听192.168.1XX.22的IP地址；（XX现场提供）
- index.html内容使用Welcome to 2018 Computer Network Application contest!；

安装
> yum -y install httpd
> yum -y install mod_ssl

配置虚拟主机文件
```bash
vim /etc/httpd/conf.d/virthost.conf
<VirtualHost 192.168.1xx.22:80>
	ServerName  www.rj.com     ////设置Web服务器的主机名和监听端口
	DocumentRoot "/data/web_data" 
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>

Listen 192.168.1XX.33:443 
<VirtualHost 192.168.1xx.22:443>
	ServerName  www.rj.com     ////设置Web服务器的主机名和监听端口
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
>mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.bak

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
touch index.txt  #索引问文件
touch serial    #给客户发证编号存放文件
echo 01 > serial

mkdir /etc/httpd/ssl
cd /etc/httpd/ssl
openssl genrsa 1024 > httpd.key 
openssl req -new -key httpd.key > httpd.csr
openssl ca -days 365 -in httpd.csr > httpd.crt 

使用cat /etc/pki/CA/index.txt查看openssl证书数据库文件
cat /etc/pki/CA/index.txt
```

```bash
httpd -t 检查配置
setenforce 0 
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --zone=public --add-service=https --permanent
firewall-cmd --reload
service httpd start 
```

curl http://www.rj.com
curl https://www.rj.com


B
配置http服务，以虚拟主机的方式创建web站点
将/etc/httpd/conf.d/ssl.conf重命名为ssl.conf.bak
配置文件名为virthost.conf，放置在/etc/httpd/conf.d目录下；
配置https功能，https所用的证书httpd.crt、私钥httpd.key放置在/etc/httpd/ssl目录中（目录需自己创建，httpd.crt、httpd.key均文件从serverA复制）；
使用www.rj.com作为域名进行访问；
提供http、https服务，仅监听192.168.1XX.33的地址。（XX现场提供）

安装
> yum -y install httpd
> yum -y install mod_ssl

配置虚拟主机文件
```bash
vim /etc/httpd/conf.d/virthost.conf
<VirtualHost 192.168.1xx.33:80>
	ServerName  www.rj.com     ////设置Web服务器的主机名和监听端口
	DocumentRoot "/data/web_data" 
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>

Listen 192.168.1XX.33:443 
<VirtualHost 192.168.1xx.33:443>
	ServerName  www.rj.com     ////设置Web服务器的主机名和监听端口
	DocumentRoot "/data/web_data" 
	
	SSLEngine on
	SSLCertificateFile /etc/httpd/ssl/httpd.crt
	SSLCertificateKeyFile /etc/httpd/ssl/httpd.key

	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>
```

>mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.bak

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
httpd -t 检查配置
setenforce 0 
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --zone=public --add-service=https --permanent
firewall-cmd --reload
service httpd start 
```

---


**18 B0**
配置http服务，以虚拟主机的方式建立一个web站点。
配置文件名为virthost.conf，放置在/etc/httpd/conf.d目录下；
使用www.rj.com作为域名进行访问；
网站根目录为/data/web_data；
index.html内容使用Welcome to 2018 Computer Network Application contest!

安装
> yum -y install httpd
> yum -y install mod_ssl

配置虚拟主机文件
```bash
vim /etc/httpd/conf.d/virthost.conf
<VirtualHost 192.168.1xx.33:80>
	ServerName  www.rj.com     ////设置Web服务器的主机名和监听端口
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
httpd -t 检查配置
setenforce 0 
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
service httpd start 
```

---

**18 J0**
配置http服务，以虚拟主机的方式建立一个web站点；
配置文件名为virthost.conf，放置在/etc/httpd/conf.d目录下；
仅监听192.168.2.22:8080端口；
使用www.rj.com作为域名进行访问；
网站根目录为/data/web_data；
index.html内容使用Welcome to 2018 Computer Network Application contest!。

安装
> yum -y install httpd
> yum -y install mod_ssl

配置虚拟主机文件
```bash
vim /etc/httpd/conf.d/virthost.conf
Listen 192.168.2.22:8080
<VirtualHost 192.168.2.22:8080>
	ServerName  www.rj.com     ////设置Web服务器的主机名和监听端口
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
httpd -t 检查配置
setenforce 0 
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload
service httpd start 
```

---

**18 C0**
配置openssl，为云主机A提供web证书。

创建证书
```bash
>cd /etc/pki/CA/private
>openssl genrsa 2048 > cakey.pem 
>openssl req -new -x509 -key cakey.pem > /etc/pki/CA/cacert.pem

cd /etc/pki/CA
touch index.txt  #索引问文件
touch serial    #给客户发证编号存放文件
echo 01 > serial

cd 
openssl genrsa 1024 > httpd.key 
openssl req -new -key httpd.key > httpd.csr
openssl ca -days 365 -in httpd.csr > httpd.crt 

openssl pkcs12 -export -out server.pfx -inkey httpd.key -in httpd.crt
自己想办法把server.pfx导出给windows2008主机
```

---

**2019 样**
配置http服务，以虚拟主机的方式建立一个web站点。
	- 将/etc/httpd/conf.d/ssl.conf重命名为ssl.conf.bak；
	- 配置文件名为virthost.conf，放置在/etc/httpd/conf.d目录下；
	- https所用的证书httpd.crt、私钥httpd.key、请求证书httpd.csr放置在/etc/httpd/ssl目录中（目录需自己创建）；
	- 监听80、443端口，分别配置http和https功能；
	- 使用www.rj.com作为域名进行访问；
	- 网站根目录为/data/web_data,index.html内容使用Welcome to 2018 Computer Network Application contest!


Openssl genrsa 2048 > httpd.key
openssl req -new -key httpd.key -out httpd.csr
通过这个csr文件在内部的windows CA服务器上申请证书

## ab
安装
`sudo apt install apache2-utils`
`yum install httpd-tools`

---

# Caddy
- 安装Caddy
```bash
curl https://getcaddy.com | bash -s personal
或
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubiBackup/doubi/master/caddy_install.sh && chmod +x caddy_install.sh && bash caddy_install.sh
或
https://caddyserver.com/download 进入到 caddy 官网的下载界面，选择平台和插件
下载后用 cp 命令放到 /usr/local/bin/caddy ,解压
```

- 运行
`caddy`然后打开浏览器输入： http://ip:2015 ，得到了一个404页面，Caddy 已经成功运行了

在无配置文件的情况下，Caddy 默认是映射当前程序执行的目录所有文件(即/usr/local/bin)，因此可以创建一个文件
`echo "<h1>Hello Caddy</h1>" >> index.html`

`caddy -port 80`改为运行在80端口

- 配置文件
```bash
chown -R root:www-data /usr/local/bin     #设置目录数据权限
vim /usr/local/bin/Caddyfile	#注.一般来说caddy路径都是这个,个别安装脚本可能有不同路径

echo -e ":80 {
	gzip	
	root /usr/local/bin/www
}" > /usr/local/bin/Caddyfile

echo "<h1>first</h1>" >> /usr/local/bin/www/index.html

caddy
```

- 反向代理
做一个ip跳转
```bash
echo ":80 {
	gzip
	proxy / http://www.baidu.com
}" > /usr/local/bin/Caddyfile

caddy
```

- HTTPS
为已经绑定域名的服务器自动从 Let’s Encrypt 生成和下载 HTTPS 证书，支持 HTTPS 协议访问，你只需要将绑定的 IP 换成 域名 即可
```bash
echo -e "xxx.com {
	gzip
    root /usr/local/bin/www
	tls xxxx@xxx.com  #你的邮箱
}" > /usr/local/bin/Caddyfile


```


---

# Haproxy🏐
**18-I**
配置Haproxy，使用listen实现http代理，使用frontend、backend实现https代理，具体要求如下：
	- listen的配置需求如下：
	- 名称：http
	- 监听地址：172.16.1XX.22:80（XX现场提供）
	- 后端server：serverA和serverB
	- frontend的配置需求如下：
	- 名称：https
	- 监听地址：172.16.1XX.22:443（XX现场提供）
	- 模式：tcp
	- 默认后端：web_server
	- backend的配置需求如下：
	- 名称：web_server
	- 模式：tcp
	- 负载均衡算法：roundrobin
	- 后端server：serverA和serverB。

1. 安装
>yum install -y haproxy

2. 创建HAProxy配置文件
```vim
vim /etc/haproxy/haproxy.cfg

listen http
    bind 172.16.101.22:80
    server a 192.168.101.22:80
    server b 192.168.101.33:80

frontend https
	bind 172.16.101.22:443
	mode tcp
	default_backend web_server	#请求转发至名为 "web_server" 的后端服务

backend web_server  #后端服务web_server 
	mode tcp
	balance roundrobin
	server a 192.168.101.22:443
    server b 192.168.101.33:443
```

>service haproxy start

---

# mariadb🏈
**18 I0**
配置mariadb服务，修改/etc/my.cnf配置文件，实现以下需求：
服务仅监听在192.168.XX+1.33的IP地址上；
关闭数据库域名解析功能；
开启独立表空间模式；
数据库存储位置为/data/database；
Mariadb数据库授权root用户能够通过192.168.XX+1.0网段远程访问。

安装
>yum install mariadb mariadb-server

数据库初始化的操作
>systemctl start mariadb
>mysql_secure_installation


|配置流程 	|说明 |操作
------------ | ------------- | ------------
Enter current password for root (enter for none) |	输入 root 密码 	| 初次运行直接回车
Set root password? [Y/n] |	是设置 root 密码 |	可以 y 或者 回车
New password |	输入新密码 	
Re-enter new password |	再次输入新密码
Remove anonymous users? [Y/n] |	是否删除匿名用户 | 可以 y 或者回车 本题y
Disallow root login remotely? [Y/n]  |	是否禁止 root 远程登录 |  可以 y 或者回车 本题n
Remove test database and access to it? [Y/n]  |	是否删除 test 数据库 | y 或者回车 本题y
Reload privilege tables now? [Y/n] | 是否重新加载权限表 | y 或者回车 本题y



修改/etc/my.cnf配置文件
cp /usr/share/mysql/my-medium.cnf /etc/my.cnf
```vim
vim /etc/my.cnf

[mysqld]
skip-name-resolve  #关闭数据库域名解析功能
innodb_file_per_table = 1	#开启独立表空间模式

bind-address = 192.168.XX+1.33　　#监听的ip地址，就是自己的另一个网卡IP，要确保有这个ip，不然启动会报错

#skip-networking  #没有的话不管他，有的话注释掉
```

Mariadb数据库授权root用户能够通过192.168.XX+1.0网段远程访问。
```sql
systemctl start mariadb

mysql -u root -p <password>
select User, host from mysql.user;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.XX+1.%' IDENTIFIED BY 'passwd123' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

```bash
firewall-cmd --permanent --add-service=mysql
firewall-cmd --reload

systemctl enable mariadb
```


**修改数据库存储位置为/data/database**
***注：这一小问坑较多，建议放弃***
```vim
systemctl stop mariadb
mkdir -p /data/database
cp -r /var/lib/mysql/*　/data/database/
chown -R mysql:mysql /data/database

``vim
vim /etc/my.cnf
[client]
port = 3306　　#监听端口　　
socket=/data/database/mysql.sock

[mysqld]
port = 3306　　#监听端口　　
socket=/data/database/mysql.sock
datadir =  /data/database　 #数据库存储位置
```

---

/# nginx
**18 J0**
配置nginx服务，利用upstream模块实现负载均衡功能
- 定义负载均衡后端主机为云主机A和云主机B；
- 权重：云主机A=30，云主机B=60；
- 名称为web；
- 将访问192.168.1.22的所有流量反代至web。

---

/# phpmyadmin
pass

---

# RAID🏉
**18-I**
- 新建两个10G的云硬盘，名称分别为B-10-1、B-10-2，挂载到serverB；
- 使用mdadm将两块云硬盘创建RAID1阵列，设备文件名为md0；
- 将新建的RAID1格式化为xfs文件系统，编辑/etc/fstab文件实现以UUID的形式开机自动挂载至/data/ftp_data目录。

安装
>yum remove mdadm	#这个软件有点问题，建议先把原本的卸掉在装
>yum install mdadm

把两块盘分区
```bash
fdisk /dev/sdb
n 创建
p 主分区
接下来一路回车选默认值
w 写入

fdisk /dev/sdc
n 创建
p 主分区
接下来一路回车选默认值
w 写入
```

创建 RAID1 阵列
>mdadm -Cv /dev/md0 -a yes -l1 -n2 /dev/sd[b,c]1

- -Cv: 创建一个阵列并打印出详细信息。
- /dev/md0: 阵列名称。
-a　: 同意创建设备，如不加此参数时必须先使用mknod 命令来创建一个RAID设备，不过推荐使用-a yes参数一次性创建；
- -l1 (l as in “level”): 指定阵列类型为 RAID-1 。
- -n2: 指定我们将两个分区加入到阵列中去，分别为/dev/sdb1 和 /dev/sdc1

可以使用以下命令查看进度：
>cat /proc/mdstat 

另外一个获取阵列信息的方法是：
>mdadm -D /dev/md0)


格式化为xfs
 mkfs.xfs /dev/md0 

以UUID的形式开机自动挂载
>	mkdir /data/ftp_data
>	blkid	/dev/md0 查UUID值
```vim
vi /etc/fstab
	UUID=XXXXXXXXXXXXXXXXXXXXXXXXXX    /data/ftp_data  xfs defaults 0 0
```

重启验证
>shutdown -r now 
>mount | grep '^/dev'

---

**18 B0**
- 新建三个5G的云硬盘，名称分别为A-10-1、A-10-2、A-10-3，挂载到云主机A；
- 使用mdadm将三块云硬盘创建RAID5阵列，设备文件名为md0；
- 将新建的RAID5格式化为XFS文件系统，编辑/etc/fstab文件通过UUID的方式实现系统启动时能够自动挂载到/data/web_data目录。

安装
>yum install mdadm

把两块盘分区
```bash
fdisk /dev/sdb
n 创建
p 主分区
接下来一路回车选默认值
w 写入

fdisk /dev/sdc
n 创建
p 主分区
接下来一路回车选默认值
w 写入

fdisk /dev/sdd
n 创建
p 主分区
接下来一路回车选默认值
w 写入
```

创建 RAID5 阵列
>mdadm -Cv /dev/md0 -a yes -l5 -n3 /dev/sd[b,c,d]1

格式化为xfs
 mkfs.xfs /dev/md0 

以UUID的形式开机自动挂载
>	mkdir /data/web_data
>	blkid	查UUID值
```vim
vi /etc/fstab
	UUID=XXXXXXXXXXXXXXXXXXXXXXXXXX    /data/web_data  xfs defaults 0 0
```

重启验证
>shutdown -r now 
>mount | grep '^/dev'

---

# VSFTP🎱
0. 安装服务
>yum install vsftpd

创建虚拟用户文件，把这些用户名和密码存放在一个文件中。该文件内容格式是：用户名占用一行，密码占一行。
```vim
cd /etc/vsftp
vim login.list
	Ftpuser1
	123456
	Ftpuser2
	123456
	Ftpadmin
	123456
```

使用 db_load 命令生成 db 口令login数据库文件
>db_load -T -t hash -f login.list login.db

通过修改指定的配置文件，调整对该程序的认证方式
```vim
vim /etc/vsftpd/vsftpd.conf
	pam_service_name=vsftpd.vu  #设置PAM使用的名称,该名称就是/etc/pam.d/目录下vsfptd文件的文件名

cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.vu

vim /etc/pam.d/vsftpd.vu
	auth       required     pam_userdb.so db=/etc/vsftpd/login
	account    required     pam_userdb.so db=/etc/vsftpd/login
```
**注意：格式是db=/etc/vsftpd/login这样的，一定不要去掉源文件的.db后缀。**

1. 拒绝匿名访问，只允许本地系统用户登录；
```vim
vim /etc/vsftpd/vsftpd.conf
	anonymous_enable=NO        # 不允许匿名访问，禁用匿名登录
	local_enable=YES           # 允许使用本地帐户进行FTP用户登录验证
```

2. 所有用户主目录为 /home/ftp 宿主为 virtual 用户；
>useradd -d /home/ftp -s /sbin/nologin virtual  
>chmod -Rf 755 /home/ftp/
>cd /home/ftp/
>touch testfile

```vim
vim /etc/vsftpd/vsftpd.conf  
	guest_enable=YES      #表示是否开启vsftpd虚拟用户的功能，yes表示开启，no表示不开启。
	guest_username=virtual       # 指定虚拟用户的宿主用户  
	user_config_dir=/etc/vsftpd/user_conf     # 设定虚拟用户个人vsftpd服务文件存放路径
	allow_writeable_chroot=YES
```

3. 将用户使用文件的方式记录账号以及密码；
```vim
vim /etc/vsftpd/vsftpd.conf 
	xferlog_enable=YES         # 启用上传和下载的日志功能，默认开启。
	xferlog_file=/var/log/xferlog         # vsftpd的日志存放位置 
```

4. Ftpuser1 用户只能下载不能上传以及删除文件重命名操作；
```vim
>mkdir /etc/vsftpd/user_conf
cd /etc/vsftpd/user_conf/
vim Ftpuser1
	#默认虚拟用户只能下载文件，无其他权限
```

5. Ftpuser2 可以下载与上传文件以及删除重命名操作
```vim
vim Ftpuser2
	anon_upload_enable=YES
	anon_mkdir_wirte_enable=YES
	anon_other_wirte_enable=YES
```


6. Ftpadmin 可以下载与上传文件以及删除重命名操作，并且权限为 755
```vim
vim Ftpadmin
	anon_upload_enable=YES
	anon_mkdir_wirte_enable=YES
	anon_other_wirte_enable=YES
	anon_umask=022
	虚拟用户具有写权限（上传、下载、删除、重命名）

	#umask = 022 时，新建的目录 权限是755，文件的权限是 644
	#umask = 077 时，新建的目录 权限是700，文件的权限时 600
	#vsftpd的local_umask和anon_umask借鉴了它
	#默认情况下vsftp上传之后文件的权限是600，目录权限是700
	#想要修改上传之后文件的权限，有两种情况
	#如果使用vsftp的是本地用户
	#则要修改配置文件中的 local_umask 的值
	#如果使用vsftp的是虚拟用户
	#则要修改配置文件中的 anon_umask 的值
```


7. 配置文件要求:			
/etc/pam.d/vsftpd.vu，（pam 配置文件）
/etc/vsftpd/user_conf （该目录下 ftp 用户权限配置目录）
Ftpuser1，Ftpuser2，Ftpadmin 用户权限相关配置文件均在 /etc/vsftpd/user_conf 目录下。

```bash
setenforce 0
firewall-cmd --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

**18 I**
配置FTP服务，需求如下：
使用虚拟用户认证方式，创建用户virtftp，该用户的家目录为/data/ftp_data，shell为/sbin/nologin，并将虚拟用户映射至virtftp用户；
允许属主对/data/ftp_data有写权限；
关闭PASV模式的安全检查；
设置客户端最大连接数为100，每个IP允许3个连接数；
ftpuser虚拟用户可以下载与上传文件；
ftpadmin虚拟用户可以下载与上传文件以及删除重命名操作，上传文件的umask为022。
配置文件要求:
	以下文件除了vsftpd.conf文件其余文件均需要自行创建
	/etc/vsftpd/vsftpd.conf(ftp配置文件)/etc/pam.d/vsftpd.vu，（pam配置文件）
	/etc/vsftpd/vlogin.db,（用户数据库）
	/etc/vsftpd/ftp_user（该目录下ftp用户权限配置目录）
	ftpuser，ftpadmin用户权限相关配置文件均在/etc/vsftpd/ftp_user目录下。

0. 安装服务,配置虚拟用户认证
```vim
yum install vsftpd

cd /etc/vsftp
vim vlogin.list
	ftpuser
	123456
	ftpadmin
	123456

db_load -T -t hash -f vlogin.list vlogin.db	

cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.vu

vim /etc/pam.d/vsftpd.vu
	auth       required     pam_userdb.so db=/etc/vsftpd/vlogin
	account    required     pam_userdb.so db=/etc/vsftpd/vlogin
```

1. 修改配置文件
```vim
vim /etc/vsftpd/vsftpd.conf
	pam_service_name=vsftpd.vu  
	guest_enable=YES      
	guest_username=virtftp      
	user_config_dir=/etc/vsftpd/ftp_user    
	allow_writeable_chroot=YES

	pasv_promiscuous=YES
	max_clients=100
	max_per_ip=3
```

2. 创建家目录为/data/ftp_data，shell为/sbin/nologin 的 virtftp 用户；
>useradd -d /data/ftp_data -s /sbin/nologin virtftp
>chmod -Rf 755 /data/ftp_data
>cd /data/ftp_data 
>touch testfile

3. 配置权限文件
```vim
>mkdir /etc/vsftpd/ftp_user
cd /etc/vsftpd/ftp_user
vim ftpuser
	anon_upload_enable=YES

vim ftpadmin
	anon_upload_enable=YES
	anon_mkdir_wirte_enable=YES
	anon_other_wirte_enable=YES
	anon_umask=022
```

4. 起服务
```bash
setenforce 0
firewall-cmd --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

**18 A0**
配置FTP服务，实现WEB站点远程更新和文档下载的功能，需求如下：
	- 创建用户tom，密码为ruijie。
	- 为WEB网站创建FTP站点，具体要求如下：
	- FTP普通用户主目录：/data/web_data
	- FTP访问权限：通过扩展acl方式允许用户tom读取和写入
	- FTP访问路径为：ftp://tom:ruijie@公网IP/
	- 为产品资料下载创建FTP站点，具体要求如下：
	- FTP匿名用户主目录：/data/instructions
	- FTP访问权限：允许匿名用户读取
	- FTP访问路径为：ftp://公网IP/


1. 修改配置文件
```vim
vim /etc/vsftpd/vsftpd.conf
	local_root=/data/web_data
	anon_root=/data/instructions
	anon_upload_enable=NO
```

2. 创建用户与acl；
```bash
useradd tom
passwd tom 
cd /data/web_data
chmod -Rf 755 /data/web_data
setfacl -R -m u:tom:rwx .
touch success
```

3. 起服务
```bash
setenforce 0
firewall-cmd --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

**18 B0**
配置FTP服务，需求如下：
	- 拒绝匿名访问，只允许本地系统用户登录；
	- 使用被动模式，设置云主机B公网IP为被动模式数据传输地址
	- 所有用户主目录为/data/ftp_data宿主为virtual用户；
	- 将用户使用文件的方式记录账号以及密码；
	- ftpuser1用户只能下载不能上传以及删除文件重命名操作；
	- ftpuser2可以下载与上传文件以及删除重命名操作；
	- ftpadmin可以下载与上传文件以及删除重命名操作，上传文件的umask为022；
	- 配置文件要求:
	以下文件除了vsftpd.conf文件其余文件均需要自行创建：
	/etc/vsftpd/vsftpd.conf(ftp配置文件)/etc/pam.d/vsftpd.vu，（pam配置文件）
	/etc/vsftpd/vlogin.db,（用户数据库）
	/etc/vsftpd/user_conf（该目录下ftp用户权限配置目录）
	ftpuser1，ftpuser2，ftpadmin用户权限相关配置文件均在/etc/vsftpd/user_conf目录下。

0. 安装服务,配置虚拟用户认证
```vim
yum install vsftpd

cd /etc/vsftp
vim vlogin.list
	ftpuser1
	123456
	ftpuser2
	123456
	ftpadmin
	123456

db_load -T -t hash -f vlogin.list vlogin.db	

cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.vu

vim /etc/pam.d/vsftpd.vu
	auth       required     pam_userdb.so db=/etc/vsftpd/vlogin
	account    required     pam_userdb.so db=/etc/vsftpd/vlogin
```

1. 修改配置文件
```vim
vim /etc/vsftpd/vsftpd.conf
	anonymous_enable=NO

	pam_service_name=vsftpd.vu 

	guest_enable=YES      
	guest_username=virtual  
	user_config_dir=/etc/vsftpd/ftp_user    
	allow_writeable_chroot=YES

	pasv_enable=YES         # 启用 pasv 模式
	pasv_min_port=30000     # pasv 端口起始号
	pasv_max_port=40000     # pasv 端口结束号

	xferlog_enable=YES         # 启用上传和下载的日志功能，默认开启。
	xferlog_file=/var/log/xferlog         # vsftpd的日志存放位置 
```

2. 创建家目录为/data/ftp_data 的 virtual 用户；
```bash
useradd -d /data/ftp_data -s /sbin/nologin virtual
chmod -Rf 755 /data/ftp_data
cd /home/ftp/
touch testfile
grep virtftp /etc/passwd
```

3. 配置权限文件
```vim
>mkdir /etc/vsftpd/ftp_user
cd /etc/vsftpd/ftpuser1
vim ftpuser

vim ftpuser2
	anon_upload_enable=YES
	anon_mkdir_wirte_enable=YES
	anon_other_wirte_enable=YES

vim ftpadmin
	anon_upload_enable=YES
	anon_mkdir_wirte_enable=YES
	anon_other_wirte_enable=YES
	anon_umask=022
```

4. 起服务
```bash
setenforce 0
firewall-cmd --zone=public --add-port=30000-40000/tcp --permanent
firewall-cmd --zone=public --add-port=30000-40000/udp --permanent
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

**18 I0**
配置FTP服务，实现WEB站点远程更新和文档下载的功能，需求如下：
	- 创建用户tom，密码为ruijie；
	- 禁止匿名用户登录；
	- 使用被动模式，设置云主机B公网IP为被动模式数据传输地址；
	- 为mariadb数据库创建FTP站点，具体要求如下：
	- FTP普通用户主目录：/data/mariadb_data；
	- FTP访问权限：通过扩展acl方式设置用户tom拥有读、写、执行权限；
	- FTP访问路径为：ftp://tom:ruijie@公网IP/。

1. 修改配置文件
```vim
vim /etc/vsftpd/vsftpd.conf
	anonymous_enable=NO
	local_root=/data/mariadb_data

	pasv_enable=YES         # 启用 pasv 模式
	pasv_min_port=30000     # pasv 端口起始号
	pasv_max_port=40000     # pasv 端口结束号
```

2. 创建用户与acl；
```bash
useradd tom
passwd tom
cd /data/mariadb_data
chmod -Rf 755 /data/mariadb_data
setfacl -R -m u:tom:rwx .
touch success
```

4. 起服务
```bash
setenforce 0
firewall-cmd --zone=public --add-port=30000-40000/tcp --permanent
firewall-cmd --zone=public --add-port=30000-40000/udp --permanent
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

# lvm物理卷🎳
```bash
fdisk ‐l		查看磁盘情况
fdisk /dev/sdb	创建系统分区
	n
	p
	1
	后面都是默认，直接回车
		
	t	转换分区格式
	8e

	w	写入分区表
```

1.创建一个名为 datastore 的卷组，卷组的PE尺寸为 16MB；
>	pvcreate /dev/sdb1	创建物理卷
>	vgcreate ‐s 16M datastore /dev/sdb1	

2.逻辑卷的名称为 database 所属卷组为 datastore，该逻辑卷由 50 个 PE 组成；
>	lvcreate ‐l 50 ‐n database datastore

3.将新建的逻辑卷格式化为 XFS 文件系统，要求在系统启动时能够自动挂在到 /mnt/database 目录。	
>	mkfs.xfs /dev/datastore/database
>	mkdir /mnt/database
```vim
vi /etc/fstab
	/dev/datastore/database /mnt/database/ xfs defaults 0 0
```

重启验证
>shutdown -r now 
>mount | grep '^/dev'


逻辑卷的名称为web_data所属卷组为datastore，该逻辑卷大小为10G；
>	lvcreate ‐L 10G ‐n web_data datastore

将新建的逻辑卷格式化为XFS文件系统，编辑/etc/fstab文件通过UUID的方式实现系统启动时能够自动挂载到/data/web_data目录。
>	mkfs.xfs /dev/datastore/web_data		
>	mkdir /data/web_data
>	blkid	查UUID值
```vim
vi /etc/fstab
	UUID=XXXXXXXXXXXXXXXXXXXXXXXXXX     /data/web_data/ xfs defaults 0 0
```

重启验证
>shutdown -r now 
>mount | grep '^/dev'

---


新建一个20GB的云硬盘
分区
```bash
fdisk ‐l		查看磁盘情况
fdisk /dev/sdb	创建系统分区
	n
	p
	1
	后面都是默认，直接回车
	t	转换分区格式
	8e
	w	写入分区表
```

创建一个名为datastore的卷组，卷组的PE尺寸为16MB；
>	pvcreate /dev/sdb1	创建物理卷
>	vgcreate ‐s 16M datastore /dev/sdb1	

逻辑卷的名称为database所属卷组为datastore，该逻辑卷大小为8GB；
>	lvcreate ‐L 8G ‐n database datastore
>	lvdisplay

将新建的逻辑卷database格式化为XFS文件系统，编辑配置文件实现以UUID的形式将逻辑卷开机自动挂载至/data/web_data目录；
>	mkfs.xfs /dev/datastore/database
>	mkdir /data/web_data
>	blkid	查UUID值
```vim
vi /etc/fstab
	UUID=XXXXXXXXXXXXXXXXXXXXXXXXXX     /data/web_data/ xfs defaults 0 0
```

业务扩增，导致database逻辑卷空间不足，现需将database逻辑卷扩容至15GB空间大小，以满足业务需求。（注意扩容前后截图）
>lvextend -L 15G /dev/datastore/database
>lvs	#确认有足够空间
>resize2fs /dev/datastore/database
>lvdisplay

---

# firewall🥌
配置基于WEB、FTP的firewall防火墙
```bash
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --zone=public --add-service=https --permanent
firewall-cmd --zone=public --add-service=ftp --permanent
firewall-cmd --reload
```

---

# 归档备份⛳
将 /etc/sysconfig 目录打包备份至 /home 目录下文件名为 sysconfig.tar.bz2。

>yum install -y bzip2
>tar jcvf /home/sysconfig.tar.bz2 /etc/sysconfig 
j:bzip2
c:创建一个压缩包
v:显示详情
f:指定文件

---


# DNS🛶
配置DNS服务，将相关主机名添加A记录，分别为www.abc.com、ftp.abc.com、vpn.abc.com、web.abc.com；

0. 安装
>yum -y install bind*

1. 修改主配置文件
```vim
vim /etc/named.conf
options {
# 找到以下三个语句，将其括号中的内容修改为any
    listen-on port 53 { any; };
    listen-on-v6 port 53 { any; };
    allow-query     { any; };
```

2. 区域配置文件
```vim
vim /etc/named.rfc1912.zones
zone "abc.com." IN {        
        type master;
        file "www.localhost";
};

zone "1.192.168.192.in-addr.arpa" IN {       
        type master;
        file "www.loopback";
};
```

3. 分别复制 named.localhost 和 named.loopback 为 www.localhost 和 www.loopback
>cd /var/named/
cp named.localhost www.localhost
cp named.loopback www.loopback

>chown named www.localhost 
chown named www.loopback
**因为配置文件是在 root 用户下建立的，所以启动 BIND 进程的 named 用户无法读取，会造成不能解析。**

4. 域名正向反向解析配置文件
```vim
vim /var/named/www.localhost
	$TTL 1D
	@      IN SOA  @ rname.invalid. (
                                        	0      ; serial
                                        	1D      ; refresh
                                        	1H      ; retry
                                        	1W      ; expire
                                        	3H )    ; minimum
	       	NS     @
       		A      127.0.0.1
	    	AAAA   ::1
	www    	A      192.168.192.1
	ftp    	A      192.168.192.1
	vpn     A      192.168.192.1
	web     A      192.168.192.1

！！！注意域名后面的 ”点号“

vim /var/named/www.loopback 
	$TTL 1D
	@ 		IN SOA  @ rname.invalid. (
    	                                    0 ; serial
                                        	1D ; refresh
                                        	1H ; retry
                                        	1W ; expire
                                        	3H ) ; minimum
        	NS	@
        	A 	127.0.0.1
        	AAAA	::1
        	PTR 	localhost.

	1 PTR www.abc.com.
	1 PTR ftp.abc.com.
	1 PTR vpn.abc.com.
	1 PTR web.abc.com.
```

配置文件语法检查
```
named-checkconf  #检查配置文件中的语法/etc/named.conf /etc/named.rfc1912.zones
named-checkzone abc.com www.localhost #解析库文件语法检查
named-checkzone abc.com www.loopback 
```


5.关闭安全措施
>setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload
service named start

---

监听所有地址；
允许所有机器查询；		
将ftp.abc.com解析至云主机B公网IP:1.1.1.1；
将www.abc.com解析至云主机A公网IP:1.1.2.1；
建立反向简析区域完成ftp.abc.com，www.abc.com，域名的反向解析；
只允许云主机B 192.168.XX+1.22 的 ip 进行区域传送。

0. 安装
>yum -y install bind*

1. 修改主配置文件
```vim
vim /etc/named.conf
options {
# 找到以下三个语句，将其括号中的内容修改为any
    listen-on port 53 { any; };
    listen-on-v6 port 53 { any; };
    allow-query     { any; };
```

2. 区域配置文件
```vim
vim /etc/named.rfc1912.zones
zone "abc.com" IN { 
        type master;
        file "abc.localhost";
        allow-transfer{192.168.37.22;};
};

zone "1.1.1.in-addr.arpa" IN { 
        type master;
        file "abc.loopback";
        allow-transfer{192.168.37.22;};
};

zone "2.1.1.in-addr.arpa" IN { 
        type master;
        file "www.loopback";
        allow-transfer{192.168.37.22;};
};
```

3. 分别复制 named.localhost 和 named.loopback 为 abc.localhost 和 abc.loopback 和 www.loopback
>cd /var/named/
cp named.localhost abc.localhost
cp named.loopback abc.loopback
cp named.loopback www.loopback

>chown named abc.localhost 
chown named abc.loopback
chown named www.loopback

4. 域名正向反向解析配置文件
```vim
vim /var/named/abc.localhost
	$TTL 1D
	@      IN SOA  @ rname.invalid. (
                                        	0      ; serial
                                        	1D      ; refresh
                                        	1H      ; retry
                                        	1W      ; expire
                                        	3H )    ; minimum
	       	NS     @
       		A      127.0.0.1
	    	AAAA   ::1
	ftp    	A      1.1.1.1
	www     A      1.1.2.1

vim /var/named/abc.loopback 
	$TTL 1D
	@	IN SOA  @ rname.invalid. (
    	                                    0 ; serial
                                        	1D ; refresh
                                        	1H ; retry
                                        	1W ; expire
                                        	3H ) ; minimum
        	NS 		@
        	A 		127.0.0.1
        	AAAA	::1
        	PTR 	localhost.
	1 PTR ftp.abc.com.

vim /var/named/www.loopback 
	$TTL 1D
	@ 		IN SOA  @ rname.invalid. (
    	                                    0 ; serial
                                        	1D ; refresh
                                        	1H ; retry
                                        	1W ; expire
                                        	3H ) ; minimum
        	NS 		@
        	A 		127.0.0.1
        	AAAA	::1
        	PTR 	localhost.
	1 PTR www.abc.com.
```

```bash
named-checkconf
named-checkzone abc.com abc.localhost
named-checkzone abc.com abc.loopback 
named-checkzone abc.com www.loopback 
service named restart
```
关闭安全措施
>setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload

---

**18 I**
监听当前主机的所有地址；
允许所有主机查询和递归查询；
区域定义均配置在/etc/named.conf文件中；
rj.com的区域数据文件名为rj.com.zone；
配置反向域数据文件名为172.16.0.zone
为www.rj.com添加A记录解析，解析至serverA的公网IP；
为ftp.rj.com添加A记录解析，解析至serverB的公网IP。
为serverA、serverB的公网IP添加www、ftp的PTR解析记录

0. 安装
>yum -y install bind*

1. 修改主配置文件,顺便加上区域
```vim
vim /etc/named.conf
options {
    listen-on port 53 { any; };
    allow-query     { any; };
	recursion	yes;
}

zone "rj.com" IN { 
        type master;
        file "rj.com.zone";
};

zone "0.16.172.in-addr.arpa" IN { 
        type master;
        file "172.16.0.zone";
};
```

2. 复制 named.localhost 和 named.loopback 为 rj.com.zone 和 172.16.0.zone
>cd /var/named/
cp named.localhost rj.com.zone
cp named.loopback 172.16.0.zone

>chown named rj.com.zone
chown named 172.16.0.zone

4. 域名正向反向解析配置文件
```vim
vim /var/named/rj.com.zone
	$TTL 1D
	@      IN SOA  @ rname.invalid. (
                                        	0      ; serial
                                        	1D      ; refresh
                                        	1H      ; retry
                                        	1W      ; expire
                                        	3H )    ; minimum
	       	NS     @
       		A      127.0.0.1
	    	AAAA   ::1
	ftp    	A      172.16.0.2
	www     A      172.16.0.1

vim /var/named/172.16.0.zone
	$TTL 1D
	@	IN SOA  @ rname.invalid. (
    	                                    0 ; serial
                                        	1D ; refresh
                                        	1H ; retry
                                        	1W ; expire
                                        	3H ) ; minimum
        	NS 		@
        	A 		127.0.0.1
        	AAAA	::1
        	PTR 	localhost.
	2 PTR ftp.rj.com.
	1 PTR www.rj.com.
```
```bash
named-checkconf
named-checkzone rj.com rj.com.zone
named-checkzone rj.com 172.16.0.zone
service named restart
```
关闭安全措施
>setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload

如果没有dig命令就用`yum install bind-utils`装一下
使用dig www.rj.com命令解析A记录
使用dig -x 公网IP 命令解析PTR记录

---


**18 C0**
配置DNS服务：
	- 配置rj.com域的从DNS服务，主DNS为云主机A；
	- 配置0.16.172反向域的从DNS服务，主DNS为云主机A；
	- 监听所有地址；
	- 允许所有机器查询。

0. 安装
>yum -y install bind*

1. 修改主配置文件
```vim
vim /etc/named.conf
options {
# 找到以下三个语句，将其括号中的内容修改为any
    listen-on port 53 { any; };
    listen-on-v6 port 53 { any; };
    allow-query     { any; };
```

2. 区域配置文件
```vim
vim /etc/named.rfc1912.zones
zone "rj.com" IN { 
        type slave;
        file "slaves/rj.com.zone";
        masters {192.168.xx.xx;};
};

zone "0.16.172.in-addr.arpa" IN { 
        type slave;
        file "slaves/172.16.0.zone";
        masters {192.168.xx.xx;};
};
```

3. 给权限
```bash
cd /var/named/
chown named:named slaves
chmod 770 slaves
```

4. 起服务
```bash
service named start
setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload
```

5. 主DNS也重启下服务
>service named restart

---


# smb🏓
配置 smb 服务，共享目录为 /smbshare，
共享名必须为 smbshare，
只有本网段内的所有主机可以访问，
smbshare 必须是可以浏览的，
用户 smb1 必须能够读取共享中的内容，
（用户名需要自己创建，密码为 smb123456）；

>yum -y install samba 

```vim	
vim /etc/samba/smb.conf
[smbshare]
	path = /smbshare
	public = yes
	writeable=yes
	hosts allow = 192.168.xx.
	hosts deny = all
```

验证配置文件有没有错误
>	testparm

添加用户,设置密码
>	useradd smb1
>	smbpasswd ‐a smb1(密码：smb123456)

将用户添加到 samba 服务器中，并设置密码
>	pdbedit ‐a smb1(密码：smb123456)

查看 samba 数据库用户
>	pdbedit ‐L

创建共享目录，设置所有者和所属组
>	mkdir /smbshare
>	chown smb1:smb1 /smbshare

关闭 selinux（需要重启）
```vim
vim /etc/selinux/config
SELINUX=disabled

firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload

systemctl restart smb
```

---

**18-I**
配置samba服务
A
- 修改工作组为WORKGROUP
- 注释[homes]和[printers]相关的所有内容
- 共享名为webdata
- webdata可以浏览且webdata可写
- 共享目录为/data/web_data，且apache用户对该目录有读写执行权限，用setfacl命令配置目录权限。
- 只有192.168.1XX.33的主机可以访问。（XX现场提供）
- 添加一个apache用户（密码自定义）对外提供Samba服务。

>yum -y install samba 

```vim
vim /etc/samba/smb.conf
[global]
	workgroup = WORKGROUP

[webdata]
	path = /data/web_data
	public = yes
	writable=yes
	hosts allow = 192.168.1xx.33/32
	hosts deny = all
```

```bash
testparm
useradd -s /sbin/nologin apache
smbpasswd ‐a apache(密码：smb123456)
pdbedit ‐a apache(密码：smb123456)
pdbedit ‐L

mkdir /data/web_data
cd /data/web_data/
setfacl -m u:apache:rwx .
getfacl /deta/web_data/
```

```vim
setenforce 0

firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload

systemctl start smb
```


B
- 配置smb，使用apache用户挂载serverA共享的目录至/data/web_data目录下，作为http服务网站根目录使用。

```bash
yum -y install samba 

mkdir /data/web_data
mount -t cifs -o username=apache,password='ruijie' //192.168.xx+1.xx/webdata 
/data/web_data
```

---

**18 J0**
A
配置smb服务
- 修改工作组为WORKGROUP；
- 注释[homes]和[printers]的内容；
- 共享目录为/data/web_data；
- 共享名必须为webdata；
- 只有192.168.XX+1.0/24网段内的所有主机可以访问；
- webdata必须是可以浏览的；
- webdata必须是可写的；
- 创建文件的权限为0770；
- 仅允许用户apache访问且apache是该共享的管理者（用户名需要自己创建，密码为ruijie）。

>yum -y install samba 

```vim
vim /etc/samba/smb.conf
[global]
	workgroup = WORKGROUP

[webdata]
	path = /data/web_data
	public = yes
	writable=yes
	hosts allow = 192.168.xx+1.
	hosts deny = all
	create mask = 0770
```

```bash
testparm
useradd apache
smbpasswd ‐a apache(密码：ruijie)
pdbedit ‐a apache(密码：ruijie)
pdbedit ‐L

mkdir /data/web_data
cd /data/web_data/

```

```vim
setenforce 0
firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload
systemctl start smb
```


B
- 配置smb，使用apache用户挂载云主机A共享的目录至/data/web_data目录下。

```bash
yum -y install samba 

mkdir /data/web_data
mount -t cifs -o username=apache,password='ruijie' //192.168.xx+1.xx/webdata 
/data/web_data
```

---


# nfs🏸
1. 在Centos上配置nfs服务以只读的形式方式共享目录／public（目录需要自己创建）。
```bash
yum ‐y install nfs‐utils
vim /etc/exports
	/public 192.168.xxx.xxx(ro)
		
mkdir /public

vi /etc/selinux/config
	SELINUX=disabled
		
firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload 

service rpcbind start
service nfs start	
```


客户端挂载 nfs；
1. 访问使用 nfsuser1 进行访问（用户需要自己创建）；				
2. 在 Centos 上挂载来自 Centos 的 nfs 共享,将共享目录挂载到 /mnt/nfsfiles，修改 rpc 版本号改为 4.2,启动时自动挂载。
```bash
yum ‐y install nfs‐utils
mkdir /mnt/nfsfiles

useradd nfsuser1
passwd nfsuser1
```

验证共享是否成功
>showmount ‐e 192.168.xxx.xxx

挂载共享目录
```vim
vim /etc/fstab
	192.168.xxx.xxx:/public /mnt/nfsfiles/	nfs defaults 0 0
```

>su ‐l nfsuser1

**验证**
服务器
```bash
[root@localhost ~]# cd /public/
[root@localhost public]# echo "hello" > hello.txt
```
客户端
```bash
[nfsuser1@localhost ~]$ cd /mnt/nfsfiles/
[nfsuser1@localhost nfsfiles]$ cat hello.txt
```

---

1. 将云主机 1 配置为 nfs 服务器，把 /var/www/html 作为共享目录，
```bash
yum ‐y install nfs‐utils
vim /etc/exports
	/var/www/html 192.168.xxx.xxx(rw)

firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload 

service rpcbind start
service nfs start	
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

2. 将云主机 2 配置为 nfs 客户端，并在其上查看共享目录，并挂载到本地目录/test
```bash
mount.nfs 192.168.xxx.xxx:/var/www/html /test
```

3. 同时将 /test 文件夹内容拷贝到云主机2下的 /home/www，并创建一个归档备份
```bash
cp /test /home/www
```

4. 将云主机2的 /home/www 目录打包备份至 /home 目录下文件名为 www.tar.bz2，备份周期为每天凌晨2点开始。
```bash
cd /
yum install -y bzip2

vim back.sh		#编写备份脚本文件
	tar jcvf /home/www.tar.bz2 /home/www

chmod -x back.sh	#编辑脚本文件为可执行文件

crontab -e	#编写定时任务crontab脚本
0 2 * * * /back.sh
#每天的02点00分自动执行脚本文件

#跟踪执行结果
tail -f /var/log/cron  #跟踪查询定时任务是否执行
cat /var/spool/cron/root #查询root下有那些定时任务
```

---


1. 启动 nfs 服务和设置开机启动；
```bash
firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload 

service rpcbind start
service nfs start	
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

2. 将以上挂载的云硬盘格式化为 ext4 格式并挂载到 /mnt 目录上；
```bash
fdisk ‐l		查看磁盘情况
fdisk /dev/sdb	创建系统分区
	n
	p
	1
	后面都是默认，直接回车

	w	写入分区表

mkfs.ext4 /dev/sdb1
mkdir /mnt/sdb1
mount /dev/sdd1 /mnt/sdb1
```

3. 在云主机2上发布共享 /public 目录（需自行创建）和 /mnt 目录，/mnt 目录允许所有用户访问，但不能写入，/public 目录允许 192.168.11.0/24 网段的用户读写。
```bash
yum ‐y install nfs‐utils

vim /etc/exports
	/mnt *(ro)
	/public 192.168.11.*(rw)
		
mkdir /public

firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload 

service rpcbind start
service nfs start	
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

---

**18 E0**
A
配置NFS服务，以读写访问方式将/data/web_data目录仅共享给192.168.XX+1.0/24网段的所有用户，且不挤压root用户的权限。

```bash
yum ‐y install nfs‐utils

vim /etc/exports
	/data/web_data 192.168.XX+1.*(rw,no_root_squash)
		
mkdir -p /data/web_data

firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload 

service rpcbind start
service nfs start	
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```


B
配置NFS服务，将云主机A共享的目录挂载至/data/web_data目录下。
```bash
yum ‐y install nfs‐utils

firewall-cmd --zone=public --add-service=nfs --permanent
firewall-cmd --reload 

service rpcbind start
service nfs start	
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

验证共享是否成功
>showmount ‐e 192.168.xxx.xxx

```
mkdir -p /data/web_data
mount.nfs 192.168.xxx.xxx:/data/web_data /data/web_data
```

---


# DHCP🏏
>yum install -y dhcp

复制一份示例
>cp /usr/share/doc/dhcp-4.1.1/dhcpd.conf.sample /etc/dhcp/dhcpd.conf 

```vim
vim /etc/dhcp/dhcpd.conf
	ddns-update-style interim;      # 设置DNS的动态更新方式为interim
	option domain-name "abc.edu";
	option domain-name-servers  8.8.8.8;           # 指定DNS服务器地址
	default-lease-time  43200;                          # 指定默认租约的时间长度，单位为秒
	max-lease-time  86400;  # 指定最大租约的时间长度
```

以下为某区域的 IP 地址范围
```bash
subnet 192.168.1.0 netmask 255.255.255.0 {         # 定义DHCP作用域
	range  192.168.1.20 192.168.1.100;                # 指定可分配的IP地址范围
	option routers  192.168.1.254;                       # 指定该网段的默认网关
}
```

>dhcpd -t    #检测语法有无错误
>service dhcpd start    #开启 dhcp 服务

记得防火墙放行

查看租约文件，了解租用情况
>cat /var/lib/dhcpd/dhcpd.leases

