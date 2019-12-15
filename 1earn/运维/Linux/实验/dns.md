# DNS 配置案例

---

# 基本配置

- www.abc.com 解析为 192.168.192.1
- 192.168.192.1 解析为 www.abc.com

- ftp.abc.com 解析为 192.168.192.2
- 192.168.192.2 解析为 ftp.abc.com

```vim
vim /etc/named.rfc1912.zones

zone "abc.com." IN {
        type master;
        file "z";
        allow-update { none; };
};

zone "192.168.192.in-addr.arpa" IN {
        type master;
        file "f";
        allow-update { none; };
};

```
```bash
cd /var/named/
cp named.localhost z
cp named.loopback f
chown named z
chown named f
```
```vim
vim /var/named/z

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
ftp    	A      192.168.192.2


vim /var/named/f

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
2 PTR ftp.abc.com.
```
```bash
systemctl restart named
```

---

## 案例 1
配置 DNS 服务，将相关主机名添加 A 记录，分别为 www.abc.com、ftp.abc.com、vpn.abc.com、web.abc.com;

**安装**
```bash
yum -y install bind-*
```

**修改主配置文件**
```vim
vim /etc/named.conf

options {
# 找到以下三个语句，将其括号中的内容修改为any
    listen-on port 53 { any; };
    listen-on-v6 port 53 { any; };
    allow-query     { any; };
```

**区域配置文件**
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

分别复制 named.localhost 和 named.loopback 为 www.localhost 和 www.loopback
```bash
cd /var/named/
cp named.localhost www.localhost
cp named.loopback www.loopback
chown named www.localhost
chown named www.loopback
# 因为配置文件是在 root 用户下建立的，所以启动 BIND 进程的 named 用户无法读取，会造成不能解析.
```

**域名正向反向解析配置文件**
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

!!!注意域名后面的 "点号" 不能少
```

**配置文件语法检查**
```bash
named-checkconf  						# 检查配置文件中的语法/etc/named.conf /etc/named.rfc1912.zones
named-checkzone abc.com www.localhost	# 解析库文件语法检查
named-checkzone abc.com www.loopback
```

**关闭安全措施**
```bash
setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload
service named start
```

---

## 案例 2
- 监听所有地址;
- 允许所有机器查询;
- 将 ftp.abc.com 解析至主机 B 公网 IP:1.1.1.1;
- 将 www.abc.com 解析至主机 A 公网 IP:1.1.2.1;
- 建立反向简析区域完成 ftp.abc.com，www.abc.com，域名的反向解析;
- 只允许主机 B 192.168.XX+1.22 的 ip 进行区域传送.

**安装**
```bash
yum -y install bind-*
```

**修改主配置文件**
```vim
vim /etc/named.conf

options {
# 找到以下三个语句，将其括号中的内容修改为any
    listen-on port 53 { any; };
    listen-on-v6 port 53 { any; };
    allow-query     { any; };
```

**区域配置文件**
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

分别复制 named.localhost 和 named.loopback 为 abc.localhost 和 abc.loopback 和 www.loopback
```bash
cd /var/named/
cp named.localhost abc.localhost
cp named.loopback abc.loopback
cp named.loopback www.loopback
chown named abc.localhost
chown named abc.loopback
chown named www.loopback
```

**域名正向反向解析配置文件**
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

**关闭安全措施**
```bash
setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload
```

---

## 案例 3
- 监听当前主机的所有地址;
- 允许所有主机查询和递归查询;
- 区域定义均配置在 /etc/named.conf 文件中;
- abc.com 的区域数据文件名为 abc.com.zone;
- 配置反向域数据文件名为 172.16.0.zone
- 为 www.abc.com 添加 A 记录解析，解析至 serverA 的公网 IP;
- 为 ftp.abc.com 添加 A 记录解析，解析至 serverB 的公网 IP.
- 为 serverA、serverB 的公网 IP 添加 www、ftp 的 PTR 解析记录

**安装**
```bash
yum -y install bind-*
```

**修改主配置文件,顺便加上区域**
```vim
vim /etc/named.conf

options {
    listen-on port 53 { any; };
    allow-query     { any; };
	recursion	yes;
}

zone "abc.com" IN {
        type master;
        file "abc.com.zone";
};

zone "0.16.172.in-addr.arpa" IN {
        type master;
        file "172.16.0.zone";
};
```

复制 named.localhost 和 named.loopback 为 abc.com.zone 和 172.16.0.zone
```bash
cd /var/named/
cp named.localhost abc.com.zone
cp named.loopback 172.16.0.zone
chown named abc.com.zone
chown named 172.16.0.zone
```

**域名正向反向解析配置文件**
```vim
vim /var/named/abc.com.zone

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
2 PTR ftp.abc.com.
1 PTR www.abc.com.
```
```bash
named-checkconf
named-checkzone abc.com abc.com.zone
named-checkzone abc.com 172.16.0.zone
service named restart
```

**关闭安全措施**
```bash
setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload
```

如果没有 dig 命令就用 `yum install bind-utils` 装一下
使用 dig www.abc.com 命令解析 A 记录
使用 dig -x 公网 IP 命令解析 PTR 记录

---


## 案例 4
- 配置 abc.com 域的从 DNS 服务，主 DNS 为主机 A;
- 配置 0.16.172 反向域的从 DNS 服务，主 DNS 为主机 A;
- 监听所有地址;
- 允许所有机器查询.(住:这会产生域传送漏洞)

**安装**
```bash
yum -y install bind-*
```

**修改主配置文件**
```vim
vim /etc/named.conf

options {
# 找到以下三个语句，将其括号中的内容修改为any
    listen-on port 53 { any; };
    listen-on-v6 port 53 { any; };
    allow-query     { any; };
```

**区域配置文件**
```vim
vim /etc/named.rfc1912.zones

zone "abc.com" IN {
        type slave;
        file "slaves/abc.com.zone";
        masters {192.168.xx.xx;};
};

zone "0.16.172.in-addr.arpa" IN {
        type slave;
        file "slaves/172.16.0.zone";
        masters {192.168.xx.xx;};
};
```

**给权限**
```bash
cd /var/named/
chown named:named slaves
chmod 770 slaves
```

**起服务**
```bash
service named start
setenforce 0
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload
```

**主 DNS 也重启下服务**
```bash
service named restart
```