# LAMP

---

LAMP 指的 Linux（操作系统）、ApacheHTTP 服务器，MySQL（有时也指 MariaDB，数据库软件） 和 PHP（有时也是指 Perl 或 Python） 的第一个字母，一般用来建立 web 应用平台

# MairaDB

**安装**
```
yum install mariadb mariadb-server
systemctl start mariadb
mysql_secure_installation
```

**配置远程访问**

Mariadb 数据库授权 root 用户能够远程访问
```sql
systemctl start mariadb
mysql -u root -p
select User, host from mysql.user;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'IDENTIFIED BY 'toor' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

```bash
firewall-cmd --permanent --add-service=mysql
firewall-cmd --reload
```

---

# Apache+PHP

**安装**
```bash
yum install httpd
yum install php-* --skip-broken
```

**配置**
```vim
vim /etc/httpd/conf/httpd.conf

AddType application/x-httpd-php .php
# apache 解析 php 程序
PHPIniDir "/etc/php.ini"
# 指定 php.ini 配置文件路径
```
```bash
echo "<?php phpinfo(); ?>" > /var/www/html/index.php

service httpd start
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
```
