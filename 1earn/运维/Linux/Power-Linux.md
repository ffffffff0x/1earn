```
 ███████                                           ██       ██
░██░░░░██                                         ░██      ░░
░██   ░██  ██████  ███     ██  █████  ██████      ░██       ██ ███████  ██   ██ ██   ██
░███████  ██░░░░██░░██  █ ░██ ██░░░██░░██░░█ █████░██      ░██░░██░░░██░██  ░██░░██ ██
░██░░░░  ░██   ░██ ░██ ███░██░███████ ░██ ░ ░░░░░ ░██      ░██ ░██  ░██░██  ░██ ░░███
░██      ░██   ░██ ░████░████░██░░░░  ░██         ░██      ░██ ░██  ░██░██  ░██  ██░██
░██      ░░██████  ███░ ░░░██░░██████░███         ░████████░██ ███  ░██░░██████ ██ ░░██
░░        ░░░░░░  ░░░    ░░░  ░░░░░░ ░░░          ░░░░░░░░ ░░ ░░░   ░░  ░░░░░░ ░░   ░░
```

`Linux 下各种常见服务的搭建/配置指南`

`大部分适用于 Centos7`

`目前主要以安装搭建为主,更深一步的配置请自行研究`

<p align="center">
     <a href="https://www.wikiart.org/en/gustave-caillebotte/the-garden-at-petit-gennevilliers"><img src="../../../assets/img/运维/Linux/Power-Linux.jpg" width="70%"></a>
</p>

---

## 大纲

**系统配置**

* [Net](#Net)
* [RAID](#RAID)
* [Lvm](#Lvm)

**网络服务**

* [AdguardTeam](#AdguardTeam)
* [Chrony](#Chrony)
* [cloud-torrent](#cloud-torrent)
* [DHCP](#DHCP)
* [DNS](#DNS)
* [Kicktart](#Kicktart)
* [OpenVPN](#OpenVPN)
* [proxychains](#proxychains)
* [SSH](#SSH)

**web 服务**

* [Apache](#Apache)
* [Caddy](#Caddy)
* [npm & Node](#npm&Node)
* [PHP](#PHP)
* [Nginx](#Nginx)
* [phpMyAdmin](#phpMyAdmin)
* [Tomcat](#Tomcat)
* [Wordpress](#Wordpress)
* [Mijisou](#Mijisou)

**数据库**

* [Relational](#Relational)
  * [Oracle](#Oracle)
  * [Mariadb](#Mariadb)
  * [MySQL](#MySQL)
  * [Postgresql](#Postgresql)
* [Document](#Document)
  * [MongoDB](#MongoDB)
* [Key-value](#Key-value)
  * [Redis](#Redis)
  * [Memcached](#Memcached)

**文本工具**

* [Vim](#Vim)

**文件服务**

* [filebrowser](#filebrowser)
* [NFS](#NFS)
* [Samba](#Samba)
* [Vsftp](#Vsftp)

**编程语言**

* [C](#C)
* [Go](#Go)
* [JDK](#JDK)
* [Python3](#Python3)
* [Ruby](#Ruby)

**管理工具**

* [Supervisor](#Supervisor)
* [Webmin](#Webmin)

**系统监控**

* [Zabbix](#Zabbix)

**虚拟化**

* [Docker](#Docker)

**CI**

* [Jenkins](#Jenkins)

**堡垒机**

* [Jumpserver](#Jumpserver)

**安全服务**

* [ClamAV](#ClamAV)
* [Fail2ban](#Fail2ban)


**仓库**

* [Nexus](#Nexus)



---

# 系统配置
## Net

**centos 配置网卡**
```vim
vim /etc/sysconfig/network-scripts/ifcfg-eth0

DEVICE="enoXXXXXX"
BOOTPROTO=static  # 使用静态 IP,而不是由 DHCP 分配 IP
IPADDR=172.16.102.61
PREFIX=24
ONBOOT=yes
GATEWAY=172.16.102.254
HOSTNAME=dns1.abc.com
DNS1=223.5.5.5
```

**修改主机名**
```vim
vim /etc/hosts

127.0.0.1  test localhost # 修改 localhost.localdomain 为 test,shutdown -r now 重启使修改生效
```

**修改 DNS**
```vim
vim /etc/resolv.conf

nameserver 8.8.8.8
```
`service network restart`

---

## RAID

**安装**

`yum remove mdadm`	# 建议先把原本的卸掉重装

`yum install mdadm`

**分区**
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

**创建阵列**
- RAID1

	`mdadm -Cv /dev/md0 -a yes -l1 -n2 /dev/sd[b,c]1`
	- -Cv: 创建一个阵列并打印出详细信息.
	- /dev/md0: 阵列名称.
	-a　: 同意创建设备,如不加此参数时必须先使用 mknod 命令来创建一个 RAID 设备,不过推荐使用 -a yes 参数一次性创建；
	- -l1 (l as in "level"): 指定阵列类型为 RAID-1 .
	- -n2: 指定我们将两个分区加入到阵列中去,分别为/dev/sdb1 和 /dev/sdc1

- RAID5

	`mdadm -Cv /dev/md0 -a yes -l5 -n3 /dev/sd[b,c,d]1`

	可以使用以下命令查看进度：

	`cat /proc/mdstat`

	另外一个获取阵列信息的方法是：

	`mdadm -D /dev/md0`

**格式化为 xfs**

`mkfs.xfs /dev/md0`

**以 UUID 的形式开机自动挂载**
```bash
mkdir /data/ftp_data
blkid	/dev/md0 # 查 UUID 值
```
```vim
vim /etc/fstab
UUID=XXXXXXXXXXXXXXXXXXXXXXXXXX    /data/ftp_data  xfs defaults 0 0
```
```bash
shutdown -r now # 重启验证
mount | grep '^/dev'
```

---

## Lvm

```bash
fdisk ‐l		# 查看磁盘情况
fdisk /dev/sdb	# 创建系统分区
	n
	p
	1
	后面都是默认,直接回车

	t	# 转换分区格式
	8e

	w	# 写入分区表
```

**卷组**

创建一个名为 datastore 的卷组,卷组的PE尺寸为 16MB；
```bash
pvcreate /dev/sdb1	# 初始化物理卷
vgcreate ‐s 16M datastore /dev/sdb1 # 创建物理卷
```

**逻辑卷**

逻辑卷的名称为 database 所属卷组为 datastore,该逻辑卷由 50 个 PE 组成；
```bash
lvcreate ‐l 50 ‐n database datastore
```

逻辑卷的名称为database所属卷组为datastore,该逻辑卷大小为8GB；
```bash
lvcreate ‐L 8G ‐n database datastore
lvdisplay
```

**格式化**

将新建的逻辑卷格式化为 XFS 文件系统,要求在系统启动时能够自动挂在到 /mnt/database 目录.
```bash
mkfs.xfs /dev/datastore/database
mkdir /mnt/database
```
```vim
vi /etc/fstab
/dev/datastore/database /mnt/database/ xfs defaults 0 0
```

重启验证
```bash
shutdown -r now
mount | grep '^/dev'
```

**扩容**

将 database 逻辑卷扩容至 15GB 空间大小,以满足业务需求.
```bash
lvextend -L 15G /dev/datastore/database
lvs	# 确认有足够空间
resize2fs /dev/datastore/database
lvdisplay
```

---

# 网络服务
## AdguardTeam

`一个 DNS 去广告、去跟踪的服务`

**项目地址**
- https://github.com/AdguardTeam/AdGuardHome

**安装**
```bash
mkdir -p /opt/adguard && cd /opt/adguard
wget https://github.com/AdguardTeam/AdGuardHome/releases/download/v0.95-hotfix/AdGuardHome_v0.95-hotfix_linux_amd64.tar.gz
tar -xzvf AdGuardHome_v0.94_linux_amd64.tar.gz
cd AdGuardHome
./AdGuardHome -s install

systemctl stop firewalld
```

**其他管理命令**
```bash
./AdGuardHome -s uninstall
./AdGuardHome -s start
./AdGuardHome -s stop
./AdGuardHome -s restart
./AdGuardHome -s status
```
无误的话访问服务器 IP+端口 3000 就可以看到管理页面了

---

## Chrony

`一个时间同步软件,可用于搭建类 NTP 时间服务`

**官网**
- https://chrony.tuxfamily.org/

**简介**

它由两个程序组成：chronyd 和 chronyc.

chronyd 是一个后台运行的守护进程,用于调整内核中运行的系统时钟和时钟服务器同步.它确定计算机增减时间的比率,并对此进行补偿.

chronyc 是用来监控 chronyd 性能和配置其参数程序

**安装**
```bash
yum install chrony
```

**配置文件**
```vim
vim /etc/chrony.conf

server time1.aliyun.com iburst
server time2.aliyun.com iburst
server time3.aliyun.com iburst
server time4.aliyun.com iburst
server time5.aliyun.com iburst
server time6.aliyun.com iburst
server time7.aliyun.com iburst
# 或
server time1.google.com iburst
server time2.google.com iburst
server time3.google.com iburst
server time4.google.com iburst
```

**启服务**
```bash
systemctl stop ntpd
systemctl disable ntpd

systemctl enable chronyd.service
systemctl start chronyd.service
```

**查看同步状态**
```bash
chronyc sourcestats # 检查 ntp 源服务器状态
chronyc sources -v  # 检查 ntp 详细同步状态

chronyc # 进入交互模式
  activity
```

---

## cloud-torrent

`web torrent 下载服务`

**项目地址**
- https://github.com/jpillora/cloud-torrent

**安装**

`curl https://i.jpillora.com/cloud-torrent! | bash`

**运行**

`cloud-torrent -o`

`我日,就这么简单`

---

## DHCP

**安装**

`yum install dhcp`

**复制一份示例**

`cp /usr/share/doc/dhcp-4.1.1/dhcpd.conf.sample /etc/dhcp/dhcpd.conf `

**修改配置文件**
```vim
vim /etc/dhcp/dhcpd.conf

ddns-update-style interim;      # 设置 DNS 的动态更新方式为 interim
option domain-name "abc.edu";
option domain-name-servers  8.8.8.8;           # 指定 DNS 服务器地址
default-lease-time  43200;                          # 指定默认租约的时间长度,单位为秒
max-lease-time  86400;  # 指定最大租约的时间长度

# 以下为某区域的 IP 地址范围

subnet 192.168.1.0 netmask 255.255.255.0 {         # 定义 DHCP 作用域
	range  192.168.1.20 192.168.1.100;                # 指定可分配的 IP 地址范围
	option routers  192.168.1.254;                       # 指定该网段的默认网关
}
```
```bash
dhcpd -t    # 检测语法有无错误
service dhcpd start    # 开启 dhcp 服务

firewall-cmd --zone=public --add-service=dhcp --permanent
firewall-cmd --reload # 记得防火墙放行

cat /var/lib/dhcpd/dhcpd.leases # 查看租约文件,了解租用情况
```
---

## DNS

**安装**

`yum install bind-*`

**主配置文件**
```vim
vim /etc/named.conf

options {
    listen-on port 53 { any; };
    listen-on-v6 port 53 { any; };
    allow-query     { any; };
}
```

**区域配置文件**
```vim
vim /etc/named.rfc1912.zones

zone "abc.com" IN {
        type master;
        file "abc.localhost";
};

zone "1.1.1.in-addr.arpa" IN {
        type master;
        file "abc.loopback";
};

zone "2.1.1.in-addr.arpa" IN {
        type master;
        file "www.loopback";
};
```

**创建区域数据文件**
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
```
```vim
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
```
```vim
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

**启服务**
```bash
named-checkconf
named-checkzone abc.com abc.localhost
named-checkzone abc.com abc.loopback
named-checkzone abc.com www.loopback
service named restart

setenforce 0  # 关闭 selinux
firewall-cmd --zone=public --add-service=dns --permanent
firewall-cmd --reload
```

---

## Kicktart

`是 Kicktart 不是 kickstarter,这玩意不能众筹,这是用于联网安装系统时给 PXE 服务提供应答文件的`

- 调用服务:PXE + TFTP +FTP + DHCP + Kickstart
- 环境:VMWARE
- 1台无人值守系统——RHEL 7——192.168.10.10
- 1台客户端——未安装操作系统

注：vmware 中做实验需要在虚拟网络编辑器中将 dhcp 服务关闭

**配置 DHCP**

DHCP 服务程序用于为客户端主机分配可用的 IP 地址,而且这是服务器与客户端主机进行文件传输的基础

`yum -y install dhcp`

```vim
# 这里使用的配置文件有两个主要区别：允许了 BOOTP 引导程序协议,旨在让局域网内暂时没有操作系统的主机也能获取静态 IP 地址；在配置文件的最下面加载了引导驱动文件 pxelinux.0 (这个文件会在下面的步骤中创建) ,其目的是让客户端主机获取到 IP 地址后主动获取引导驱动文件,自行进入下一步的安装过程.
vim /etc/dhcp/dhcpd.conf

allow booting;
allow bootp;
ddns-update-style interim;
ignore client-updates;
subnet 192.168.0.0 netmask 255.255.255.0 {
        option subnet-mask 255.255.255.0;
        option domain-name-servers 192.168.10.10;
        range dynamic-bootp 192.168.10.100 192.168.10.200;
        default-lease-time 21600;
        max-lease-time 43200;
        next-server 192.168.10.10;
        filename "pxelinux.0";
}
```
```bash
systemctl restart dhcpd
systemctl enable dhcpd
```

**配置 TFTP 服务**

配置 TFTP 服务程序,为客户端主机提供引导及驱动文件.当客户端主机有了基本的驱动程序之后,再通过 vsftpd 服务程序将完整的光盘镜像文件传输过去.
```bash
yum -y install tftp-server xinetd
```
```vim
vim /etc/xinetd.d/tftp

service tftp
{
        socket_type = dgram
        protocol = udp
        wait = yes
        user = root
        server = /usr/sbin/in.tftpd
        server_args = -s /var/lib/tftpboot
        disable = no
        per_source = 11
        cps = 100 2
        flags = IPv4
}
```
```bash
systemctl restart xinetd
systemctl enable xinetd
firewall-cmd --permanent --add-port=69/udp  # 放行 tftp
firewall-cmd --reload
```

**配置 SYSLinux 服务**

SYSLinux 是一个用于提供引导加载的服务程序.与其说 SYSLinux 是一个服务程序,不如说更需要里面的引导文件,在安装好 SYSLinux 服务程序软件包后,/usr/share/syslinux 目录中会出现很多引导文件.
```bash
yum -y install syslinux

# 首先把 SYSLinux 提供的引导文件复制到 TFTP 服务程序的默认目录中,也就是 pxelinux.0,这样客户端主机就能够顺利地获取到引导文件.另外在 RHEL 7 系统光盘镜像中也有一些需要调取的引导文件.
cd /var/lib/tftpboot
cp /usr/share/syslinux/pxelinux.0 .
mkdir /media/cdrom
mount /dev/cdrom /media/cdrom
# 确认光盘镜像已经被挂载到 /media/cdrom 目录后,使用复制命令将光盘镜像中自带的一些引导文件也复制到 TFTP 服务程序的默认目录中.
cp /media/cdrom/images/pxeboot/{vmlinuz,initrd.img} .
cp /media/cdrom/isolinux/{vesamenu.c32,boot.msg} .

# 在 TFTP 服务程序的目录中新建 pxelinux.cfg 目录,虽然该目录的名字带有后缀,但依然也是目录,而非文件！将系统光盘中的开机选项菜单复制到该目录中,并命名为 default.这个 default 文件就是开机时的选项菜单.
mkdir pxelinux.cfg
cp /media/cdrom/isolinux/isolinux.cfg pxelinux.cfg/default
```
```vim
# 默认的开机菜单中有两个选项,要么是安装系统,要么是对安装介质进行检验.既然我们已经确定采用无人值守的方式安装系统,还需要为每台主机手动选择相应的选项,未免与我们的主旨 (无人值守安装) 相悖.现在我们编辑这个 default 文件,把第 1 行的 default 参数修改为 linux,这样系统在开机时就会默认执行那个名称为 linux 的选项了.对应的 linux 选项大约在 64 行,我们将默认的光盘镜像安装方式修改成 FTP 文件传输方式,并指定好光盘镜像的获取网址以及 Kickstart 应答文件的获取路径

# 修改第 1 行和第 64 行
vim pxelinux.cfg/default

1 default linux
64 append initrd=initrd.img inst.stage2=ftp://192.168.10.10 ks=ftp://192.168.10.10/pub/ks.cfg quiet
```

**配置 VSftpd 服务**
```bash
yum -y install vsftpd

systemctl restart vsftpd
systemctl enable vsftpd
ln -s '/usr/lib/systemd/system/vsftpd.service' '/etc/systemd/system/multi-user.target.wants/vsftpd.service'

cp -rvf /media/cdrom/* /var/ftp
firewall-cmd --permanent --add-service=ftp
firewall-cmd --reload
setsebool -P ftpd_connect_all_unreserved=on
```

**创建 KickStart 应答文件**
```bash
cp ~/anaconda-ks.cfg /var/ftp/pub/ks.cfg
chmod +r /var/ftp/pub/ks.cfg
```
```vim
#修改第 7、27、35 行
vim /var/ftp/pub/ks.cfg

url --url=ftp://192.168.0.105
timezone Asia/Shanghai --isUtc
clearpart --all --initlabel
# 如果觉得系统默认自带的应答文件参数较少,不能满足生产环境的需求,则可以通过 Yum 软件仓库来安装 system-config-kickstart 软件包.这是一款图形化的 Kickstart 应答文件生成工具,可以根据自己的需求生成自定义的应答文件,然后将生成的文件放到 /var/ftp/pub 目录中并将名字修改为 ks.cfg 即可.
```

**Reference**
- [第19章 使用 PXE+Kickstart 无人值守安装服务.](https://www.linuxprobe.com/chapter-19.html)

---

## OpenVPN

**官网**
- https://openvpn.net/

**docker 安装**
```bash
systemctl start docker
docker pull kylemanna/openvpn:2.4
mkdir -p /data/openvpn
docker run -v /data/openvpn:/etc/openvpn --rm kylemanna/openvpn:2.4 ovpn_genconfig -u udp://<你的IP>
```

**生成密钥文件**
```bash
docker run -v /data/openvpn:/etc/openvpn --rm -it kylemanna/openvpn:2.4 ovpn_initpki
输入私钥密码 (输入时是看不见的) ：
Enter PEM pass phrase:12345678
再输入一遍
Verifying - Enter PEM pass phrase:12345678
输入一个 CA 名称 (我这里直接回车)
Common Name (eg: your user, host, or server name) [Easy-RSA CA]:
输入刚才设置的私钥密码 (输入完成后会再让输入一次)
Enter pass phrase for /etc/openvpn/pki/private/ca.key:12345678
```

**生成客户端证书 (这里的 user 改成你想要的名字) **
```bash
docker run -v /data/openvpn:/etc/openvpn --rm -it kylemanna/openvpn:2.4 easyrsa build-client-full user nopass

输入刚才设置的密码
Enter pass phrase for /etc/openvpn/pki/private/ca.key:12345678
```

**导出客户端配置**
```bash
mkdir -p /data/openvpn/conf
docker run -v /data/openvpn:/etc/openvpn --rm kylemanna/openvpn:2.4 ovpn_getclient user > /data/openvpn/conf/user.ovpn
```

**启动 OpenVPN 服务**
```bash
docker run --name openvpn -v /data/openvpn:/etc/openvpn -d -p 1194:1194/udp --cap-add=NET_ADMIN kylemanna/openvpn:2.4

service firewalld stop
```

**将登录的证书下载到本地**
```bash
yum install lrzsz -y
sz /data/openvpn/conf/whsir.ovpn
```

在 openvpn 的安装目录下,有个 config 目录,将服务器上的 user.ovpn,放在该目录下,运行 OpenVPN GUI,右键 whsir 连接 connect

**Reference**
- [通过 docker 搭建 openvpn](https://blog.whsir.com/post-2809.html)

---

## proxychains

`通过 DLL 注入,使目标程序走代理`

**项目地址**
- https://github.com/rofl0r/proxychains-ng

**安装**
```bash
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure
make && make install
cp ./src/proxychains.conf /etc/proxychains.conf
cd .. && rm -rf proxychains-ng
```

**编辑配置**
```bash
vim /etc/proxychains.conf

socks5 127.0.0.1 1080 # 改成你懂的
```

**使用**

在需要代理的命令前加上 proxychains4 ,如：`proxychains4 wget https://www.google.com/`

---

## SSH

**官网**
- https://www.ssh.com

一般主机安装完毕后 SSH 是默认开启的,使用 `/etc/init.d/ssh status` 查看主机 SSH 状态

**Kali/Manjaro**

安装完毕后会自动启动,但是没有配置配置文件会无法登陆,修改下配置文件
```vim
vim /etc/ssh/sshd_config

PasswordAuthentication yes
PermitRootLogin yes
```
```bash
service ssh restart
systemctl enable ssh
```
若在使用工具登录时,当输完用户名密码后提示 SSH 服务器拒绝了密码,就再试一遍.

这时不要着急,只需要在 Kali 控制端口重新生成两个秘钥即可.
```bash
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
ssh-keygen -t dsa -f /etc/ssh/ssh_host_rsa_key
```

**Ubuntu**

如果没有就装一下,如果你只是想登陆别的机器的 SSH 只需要安装 openssh-client (ubuntu 有默认安装,如果没有则 `sudo
apt-get install openssh-client`) ,如果要使本机开放 SSH 服务就需要安装 openssh-server
```bash
apt install openssh-client=1:7.2p2-4ubuntu2.8
apt install openssh-server=1:7.2p2-4ubuntu2.8
apt install ssh
```
`service ssh restart` 然后重启 SSH 服务

**加固**

本部分内容移步[Secure-Linux](./Secure-Linux#SSH) SSH 部分

**排错**

0. 先排查是不是客户端(自己)的问题,再排查是不是服务端(对面)的问题,最后在排查是不是传输中(中间)的问题.
1. ping 试试,如果网络层可通,那么大概率是应用层的问题,检查 SSH 配置,是否有白名单限制,或者你他娘的意大利防火墙或selinux就没放行
2. 假设这么一种情况,应用层配置正常,主机一切正常,但路由器/交换机在 ACL 上禁用了 SSH 的流量,这样就是传输层的问题了.内网 IPS/IDS 阻断同理.
3. 麻烦你看下账号密码是不是写错了谢谢.或者是不是限制只使用密钥登陆的.

**motd**
- [Mithrilwoodrat/FBI-WARNING-in-console](https://github.com/Mithrilwoodrat/FBI-WARNING-in-console)
- [abcfy2/motd](https://github.com/abcfy2/motd)
- `vim /etc/motd`

```
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           佛祖保佑       永不死机
           心外无法       法外无心
```
```
  _      `-._     `-.     `.   \      :      /   .'     .-'     _.-'      _
   `--._     `-._    `-.    `.  `.    :    .'  .'    .-'    _.-'     _.--'
        `--._    `-._   `-.   `.  \   :   /  .'   .-'   _.-'    _.--'
  `--.__     `--._   `-._  `-.  `. `. : .' .'  .-'  _.-'   _.--'     __.--'
  __    `--.__    `--._  `-._ `-. `. \:/ .' .-' _.-'  _.--'    __.--'    __
    `--..__   `--.__   `--._ `-._`-.`_=_'.-'_.-' _.--'   __.--'   __..--'
  --..__   `--..__  `--.__  `--._`-q(-_-)p-'_.--'  __.--'  __..--'   __..--
        ``--..__  `--..__ `--.__ `-'_) (_`-' __.--' __..--'  __..--''
  ...___        ``--..__ `--..__`--/__/  \--'__..--' __..--''        ___...
        ```---...___    ``--..__`_(<_   _/)_'__..--''    ___...---'''
  ```-----....._____```---...___(__\_\_|_/__)___...---'''_____.....-----'''
```
```
############################################################################################################&
############################################################################################################&
############################################################################################################&
############################################################################################################&
############################################################################################################&
############################################################################################################&
############################################################################################################&
##########################################################@#################################################&
#####################################################$;`.:|%@###############################################&
#################################################$:....`:;;!$##$;::!@#######################################&
##############################################|`......':'':;|&%:':;:::'%####################################&
###########################################$'........``......`:;!;'`.''..'$#################################&
#######################################@$!`.........``........`'`...'::'...`|###############################&
###################################|'.`:'.........``.............``.....`'`...!#############################&
###############################&;....:;...............``..........``.......':`..;$@#########################&
############################@!.....`;:................``............``.....```'`..';$#######################&
##########################&:......'!'..........``.....``.............``.....``.`'`.```%#####################&
########################&:.......:;`..........''......`...............``......``.':`.`.`$###################&
######################@;........':`..........''......``................```.....``..''.`. '&#################&
#####################!........:!:`..........`'`......``..................`......``..``...  :@###############&
###################$'.....`!$%|!`...........':`..........''..............`'......``..``..`.  !##############&
##################!.....;$&%||!:...........`'``......``''`'`..............;;.....``...''..`.  .%############&
#######@%;|$@###@;....!&&%|||%;...........````.......`'':`  ..............`'......``...''..`. '|%@##########&
########&|!$%|&&;...`|$$$||||;`...........````.......```:.   .....................``....''.... `$###########&
#########$|$|!%||;.`:|%%|!||!'``.........``.``.......:!!|!`   ..............  ....::.....''..`` '&##########&
#########@$|%%|||%%%%%|||!|%;;!`.........``.``...'%&@@$|!;|&#&' ............  ....`:'.....``..'' ;##########&
###########$%%|!!%$%$%|||!||%%:.........``..``.`|&&!'.'$###!  |%. ..........   ....``.....``..`;:'$#########&
##########@$$%|!!!;:|%||||%$$!`........``....``:%!.`;@#######%.`;.   `......    ... .`..``.'`.'|&%$#########&
##########&%$$|!|%:.;%|%$||$$;.........``....''``..:$###@%$@##| ..     .`.`.   .|####|`.''.''.`%############&
##########&$$%$|!|:.;%!!$&&@&;........``.....`'....!##@@! .%##&`          .   ':``  .!|'`'`''.`%############&
##########@$&$$||%:.;%||$@|'''........``......''...|@####$$###$`             ..;#####!::`'`''.'|############&
#########%;%%$&%|;..;|'      .`......``.......`;'.``;&@#######;               ;######@!''.`:'.:;|###########&
########$'..`!%%!`.`         .'......``.......'`.``.  !#####&'                |##$';##$!:.`!;.:::&##########&
#######&:........`.          `;;.....''.......'`  :'                         .%#@$`:@#@%:.';:;:..!##########&
######&:..'`.....`.           `!:...``........'`                              ;#######%;'..`::`..'%#########&
#####&:.!|`......`.         . .`''..`'........'`                               !#####&'`'`.`'`....;@########&
####$:|#%`........`           .`..'````.......'`                                 '|!`   `;'...``..`%########&
###@@##$'..........`        . .`....`'`.......'`                                          ''..:!'..:&#######&
######$'............`.        .`.....``.......'.          '`...`'''`                      `'...|#!..!#######&
#####%`...............'`      .`..............`.                     !|                   ':...:&#&:.|######&
####%`...................`::` .`.::...........'`                    .|;                   ::....!###&:|#####&
###|..............``..........`'`;:...........'`                    ':                   ;;``...`%####@@####&
#@;.....````......''''.........`:'`...........'`         ..        ..                  .:`'%$:...'$#########&
%`...`';|:   .`....'` ':.......`:`''..........'`           `'   .`.                  `;'..!###&:..'$########&
#########&'     .`.'`   `;`...;%;':!'.........'`                                  .;:.....!######|`'$#######&
#&' `!@###|        `:.    .::':' .'::`........:'                              `;:`........|&&######@|$######&
##&'      '.        ..       '''    '!'.......;&&|'                     ';!;'''..........`%;`$##############&
###$`                         .:.     ::......:|%$%'          `%&&$!`...````.`'........'''!' :@#############&
                                        ''....'!|%$&$$$$&&$!: :|;!!:....``''.''`.......':;:   !###@#########&
#&'                                      ':`..'|%||%||||||%|;!|$&|!:.````:|:.||`......'`.;'   .%#&!$########&
####@;                                     ;;.'!|!||!|||||%|!||%$|!:```'!&|'!&|'.....'` `;`    :@%.!########&
####@$%!.                                   :|:;$|%$%%%%$$%!|%%$$$|:``!%|%!!$%!'....:'  ::      !; :@#######&
####&'                            .'         :$$$||;.               .`:!|%$%%%!'..`'.   ``         `$#######&
######%.   ';;'                               :|'                   ..     '|%;`.`.                .$#######&
######@&!.       .                             ''                   ..       :|:.                  .%#######&
######;             .                           .                    .       '%:                   ..'&#####&
######@:               .                        .`                   .       .:`                  .`';``$###&
######@%'                 .                      ';'.                         '.                  `''`   |##&
#####$'`;'           .    ..''                     .`.'!;`           ..    `%&:                  '` ``  `&##&
#####!..'|'             ..                          ........';!!`    .. :|!` `.                    ``  '&###&
#####&:.:;                  .                       ...............''`....'`                      ``  :@####&
######$!'        .             ..                  .`............``   .```'`                     .`  ;######&
######@:             .            .                 ''..........`'.  .``..'`                    .`  '&######&
######;                              .              ':``..........      ..`.                   ''   .%######&
###$%:                      .           .            ;%%!:'`......  `. ...'.                  ``     :@#####&
#$';:                                     .          :||%%%%|;'``.``.````;%'                .`        :@####&
#&%;                                         .       .!||%||%%%$&|:'.`;%|!!`               '.          ;####&
```

---

## ttyd

`在 web 上访问终端`

**项目地址**
- https://github.com/tsl0922/ttyd

**安装**
```bash
sudo apt-get install cmake g++ pkg-config git vim-common libwebsockets-dev libjson-c-dev libssl-dev
git clone https://github.com/tsl0922/ttyd.git
cd ttyd && mkdir build && cd build
cmake ..
make && make install
```

**运行**
```bash
ttyd -p 8080 bash -x  # 现在访问 http://localhost:8080 即可
```

---

# web 服务
## Apache

**官网**
- https://www.apache.org/

**安装**
```bash
yum install httpd
yum install mod_ssl
```

**配置文件**
```vim
vim /etc/httpd/conf/httpd.conf

DocumentRoot "/var/www/html"
ServerName  xx.xx.xx.xx:80
# 设置 Web 服务器的主机名和监听端口
```

**启服务**
```vim
vim var/www/html/index.html

Hello World!
```
```bash
service httpd restart
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
```

**虚拟主机**

配置虚拟主机文件
```vim
vim /etc/httpd/conf.d/virthost.conf

<VirtualHost 192.168.1xx.22:80>
	ServerName  www.abc.com
  # 设置 Web 服务器的主机名和监听端口
	DocumentRoot "/data/web_data"
	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>

Listen 192.168.1XX.33:443
<VirtualHost 192.168.1xx.22:443>
	ServerName  www.abc.com
  # 设置 Web 服务器的主机名和监听端口
	DocumentRoot "/data/web_data"

	SSLEngine on
	SSLCertificateFile /etc/httpd/ssl/httpd.crt
	SSLCertificateKeyFile /etc/httpd/ssl/httpd.key

	<Directory "/data/web_data">
		Require all granted
	</Directory>
</VirtualHost>
```
```bash
mkdir -p /data/web_data
echo 'Hello World!' >/data/web_data/index.html

service httpd restart
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
```

**mod_ssl**
- **为 linux 提供 web 证书**
  ```bash
  cd /etc/pki/CA/private
  openssl genrsa 2048 > cakey.pem
  openssl req -new -x509 -key cakey.pem > /etc/pki/CA/cacert.pem

  cd /etc/pki/CA
  touch index.txt  # 索引问文件
  touch serial    # 给客户发证编号存放文件
  echo 01 > serial

  mkdir /etc/httpd/ssl
  cd /etc/httpd/ssl
  openssl genrsa 1024 > httpd.key
  openssl req -new -key httpd.key > httpd.csr
  openssl ca -days 365 -in httpd.csr > httpd.crt

  # 使用 cat /etc/pki/CA/index.txt 查看 openssl 证书数据库文件
  cat /etc/pki/CA/index.txt
  ```

- **为 windows 提供 web 证书**
  ```bash
  cd /etc/pki/CA/private
  openssl genrsa 2048 > cakey.pem
  openssl req -new -x509 -key cakey.pem > /etc/pki/CA/cacert.pem

  cd /etc/pki/CA
  touch index.txt  # 索引问文件
  touch serial    # 给客户发证编号存放文件
  echo 01 > serial

  cd
  openssl genrsa 1024 > httpd.key
  openssl req -new -key httpd.key > httpd.csr
  openssl ca -days 365 -in httpd.csr > httpd.crt

  openssl pkcs12 -export -out server.pfx -inkey httpd.key -in httpd.crt
  # 自己把 server.pfx 导出给 windows2008 主机
  ```

- **向 windows CA 服务器申请证书**

  `Openssl genrsa 2048 > httpd.key`

  `openssl req -new -key httpd.key -out httpd.csr`

  通过这个 csr 文件在内部的 windows CA 服务器上申请证书

**ab**

安装
```bash
sudo apt install apache2-utils
yum install httpd-tools
```

---

## Caddy

**官网**
- https://caddyserver.com/

**安装 Caddy**
```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubiBackup/doubi/master/caddy_install.sh && chmod +x caddy_install.sh && bash caddy_install.sh
```

**配置文件**
```bash
chown -R root:www-data /usr/local/bin     # 设置目录数据权限
touch /usr/local/caddy/Caddyfile

echo -e ":80 {
	gzip
	root /usr/local/caddy/www/
}" > /usr/local/caddy/Caddyfile

mkdir /usr/local/caddy/www
echo "<h1>first</h1>" >> /usr/local/caddy/www/index.html

/etc/init.d/caddy start
# 如果启动失败可以看 Caddy 日志： tail -f /tmp/caddy.log
```

**反向代理**

做一个 ip 跳转
```bash
echo ":80 {
	gzip
	proxy / http://www.baidu.com
}" > /usr/local/caddy/Caddyfile

/etc/init.d/caddy start
```

**HTTPS**

为已经绑定域名的服务器自动从 Let’s Encrypt 生成和下载 HTTPS 证书,支持 HTTPS 协议访问,你只需要将绑定的 IP 换成 域名 即可
```bash
echo -e "xxx.com {
	gzip
    root /usr/local/bin/www
	tls xxxx@xxx.com  #你的邮箱
}" > /usr/local/caddy/Caddyfile

/etc/init.d/caddy start
```

---

## npm&Node

**官网**
- https://www.npmjs.com/
- https://nodejs.org

**包管理器方式**
- apt

  `apt-get install nodejs npm`

- yum

  `yum install epel-release`

  `yum install nodejs npm`

**源文件方式安装**

首先下载 NodeJS 的二进制文件,http://nodejs.org/download/ .在 Linux Binaries (.tar.gz) 行处根据自己系统的位数选择
```bash
# 解压到当前文件夹下运行
tar zxvf node-v0.10.26-linux-x64.tar.gz

进入解压后的目录 bin 目录下,执行 ls 会看到两个文件 node,npm. 然后执行 ./node -v ,如果显示出 版本号说明我们下载的程序包是没有问题的.依次运行如下三条命令
cd node-v0.10.26-linux-x64/bin
ls
./node -v
```
因为 /home/kun/mysofltware/node-v0.10.26-linux-x64/bin 这个目录是不在环境变量中的,所以只能到该目录下才能 node 的程序.如果在其他的目录下执行 node 命令的话 ,必须通过绝对路径访问才可以的

如果要在任意目录可以访问的话,需要将 node 所在的目录,添加 PATH 环境变量里面,或者通过软连接的形式将 node 和 npm 链接到系统默认的 PATH 目录下的一个
在终端执行 echo $PATH 可以获取 PATH 变量包含的内容,系统默认的 PATH 环境变量包括 /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin: ,冒号为分隔符.所以我们可以将 node 和 npm 链接到 /usr/local/bin 目录下如下执行
```bash
ln -s /home/kun/mysofltware/node-v0.10.26-linux-x64/bin/node /usr/local/bin/node
ln -s /home/kun/mysofltware/node-v0.10.26-linux-x64/bin/npm /usr/local/bin/npm
```

**加速**
- [node&js](../../Misc/Plan/Misc-Plan.md#node&js)

---

## PHP
**官网**
- https://www.php.net/

**安装**
```bash
若之前安装过其他版本 PHP,先删除
yum remove php*

rpm 安装 PHP7 相应的 yum 源
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
yum install php70w
php -v  # 查看PHP版本

service php-fpm start # 要运行 PHP 网页,要启动 php-fpm 解释器
```

---

## Nginx
**官网**
- https://nginx.org/

**安装**
- **yum 安装**
  ```bash
  yum install nginx
  systemctl start nginx.service
  ```

- **源代码编译安装**

  自己下载好包 https://nginx.org/en/download.html,传到服务器上,这里以1.14.2 举例

  ```bash
  tar -zxvf nginx-1.14.2.tar.gz
  cd nginx-1.14.2/
  ./configure
  make
  make install
  cd /usr/local/nginx/sbin
  ./nginx
  ```

  注:源代码安装你的默认目录在 /usr/local/nginx 下,配置文件在 conf/ 中,不要搞错了

```bash
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --reload
```

**虚拟主机**

在 /etc/nginx/conf.d/ 目录下新建一个站点的配置文件,列如：test.com.conf
```vim
vim /etc/nginx/conf.d/test.com.conf

server {
        listen 80;
        server_name www.test.com test.com;
        root /usr/share/nginx/test.com;
        index index.html;

        location / {
        }
}
```
`nginx -t ` 检测文件是否有误

```bash
mkdir /usr/share/nginx/test.com
echo "hello world!" > /usr/share/nginx/test.com/index.html
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --reload
systemctl start nginx.service
```

如果服务器网址没有注册,那么应该在本机电脑的 /etc/hosts 添加设置： `192.168.1.112   www.test.com test.com`

`curl www.test.com`

**https**
```bash
openssl req -new -x509 -nodes -days 365 -newkey rsa:1024  -out httpd.crt -keyout httpd.key # 生成自签名证书,信息不要瞎填,Common Name一定要输你的网址

mv httpd.crt /etc/nginx
mv httpd.key /etc/nginx
```
```vim
vim /etc/nginx/conf.d/test.com.conf

server {
        listen       443 ssl http2;
        server_name  www.test.com test.com;
        root         /usr/share/nginx/test.com;
        index index.html;

        ssl_certificate "/etc/nginx/httpd.crt";
        ssl_certificate_key "/etc/nginx/httpd.key";
        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
```
`systemctl restart nginx`

**添加 PHP/PHP-FPM 环境支持**
```bash
# 安装PHP源
rpm -ivh https://mirror.webtatic.com/yum/el7/epel-release.rpm
rpm -ivh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

# 安装 PHP7.0
yum install php70w php70w-fpm php70w-mysql php70w-mysqlnd

systemctl start php-fpm.service
netstat -tnlp # 检查 php-fpm 默认监听端口：9000
```
```vim
# 添加配置
vim /etc/nginx/conf.d/test.com.conf

        # php-fpm  (新增)
        location ~\.php$ {
                fastcgi_pass 127.0.0.1:9000;
                fastcgi_param SCRIPT_FILENAME$document_root$fastcgi_script_name;
                fastcgi_param PATH_INFO $fastcgi_script_name;
                include fastcgi_params;
          }
```
```bash
systemctl restart nginx
systemctl restart php-fpm
```
```vim
vim /usr/share/nginx/test.com/info.php

<?php
     phpinfo();
 ?>
```
`curl http://www.test.com/info.php` 测试

---

## phpMyAdmin

**官网**
- https://www.phpmyadmin.net/

**建议搭配上面的 nginx+php 扩展笔记**

**创建数据库和一个用户**
```bash
yum install mariadb mariadb-server
systemctl start mariadb
systemctl enable mariadb
mysql_secure_installation

mysql -u root -p

创建一个专给 WordPress 存数据的数据库
MariaDB [(none)]> create database idiota_info;  # 最后的"idiota_info"为数据库名

创建用于 WordPress 对应用户
MariaDB [(none)]> create user idiota@localhost identified by 'password';   # "idiota"对应创建的用户,"password"内填写用户的密码

分别配置本地登录和远程登录权限
MariaDB [(none)]> grant all privileges on idiota_info.* to idiota@'localhost' identified by 'password';
MariaDB [(none)]> grant all privileges on idiota_info.* to idiota@'%' identified by 'password';

刷新权限
MariaDB [(none)]> flush privileges;
```

**下载**
```bash
wget https://files.phpmyadmin.net/phpMyAdmin/4.8.5/phpMyAdmin-4.8.5-all-languages.zip
unzip phpMyAdmin-4.8.5-all-languages.zip
mv phpMyAdmin-4.8.5-all-languages phpMyAdmin
cp phpMyAdmin /usr/share/nginx/test.com/
cd /usr/share/nginx/test.com/phpMyAdmin

cp config.sample.inc.php config.inc.php

systemctl restart nginx
```

访问 `https://www.test.com/phpMyAdmin/index.php`

---

## Tomcat

**官网**
- https://tomcat.apache.org

**安装**

Tomcat 依赖 JDK,在安装 Tomcat 之前需要先安装 Java JDK.输入命令 java -version,如果显示 JDK 版本,证明已经安装了 JDK

默认情况下,CentOS 安装有 JDK,一般先卸载掉
```bash
rpm -qa | grep jdk # 查询本地 JDK
```

JDK 安装过程 见 [如下](##JDK)

下载 Tomcat 安装包 https://tomcat.apache.org/download-80.cgi 将安装包上传至服务器,我这里以 8.5.46 为例
```bash
tar -zvxf apache-tomcat-8.5.46.tar.gz
cd apache-tomcat-8.5.46
cd bin
./startup.sh
```

如果访问 http://ip:8080/ 失败,查看防火墙开放端口
```bash
firewall-cmd --permanent --zone=public --add-port=8080/tcp
firewall-cmd --reload
```

**设置 tomcat 的服务器启动和关闭**

```vim
vim /etc/rc.d/init.d/tomcat

#!/bin/bash
# /etc/rc.d/init.d/tomcat
# init script for tomcat precesses
# processname: tomcat
# description: tomcat is a j2se server
# chkconfig: 2345 86 16
# description: Start up the Tomcat servlet engine.

if [ -f /etc/init.d/functions ]; then
. /etc/init.d/functions
elif [ -f /etc/rc.d/init.d/functions ]; then
. /etc/rc.d/init.d/functions
else
echo -e "\atomcat: unable to locate functions lib. Cannot continue."
exit -1
fi
RETVAL=$?
CATALINA_HOME="/usr/local/root/tomcat"  # tomcat 安装目录,你安装在什么目录下就复制什么目录
case "$1" in
start)
if [ -f $CATALINA_HOME/bin/startup.sh ];
then
echo $"Starting Tomcat"
$CATALINA_HOME/bin/startup.sh
fi
;;
stop)
if [ -f $CATALINA_HOME/bin/shutdown.sh ];
then
echo $"Stopping Tomcat"
$CATALINA_HOME/bin/shutdown.sh
fi
;;
*)
echo $"Usage: $0 {start|stop}"
exit 1
;;
esac
exit $RETVAL
```
```bash
chmod 755 /etc/rc.d/init.d/tomcat
chkconfig --add /etc/rc.d/init.d/tomcat
```

以上所有工作顺利进行并且没有报错,则配置完成,你可以输入命令 `service tomcat start` 和 `service tomcat stop` 进行验证

**修改端口号**

进入 tomcat 的 conf 目录下,修改 server.xml 文件,可以修改端口,默认 8080

**设置用户名和密码登录**

修改 conf 目录下 tomcat-user.xml
```vim
<role rolename="admin-gui"/>
<role rolename="manager-gui"/>
<role rolename="manager-jmx"/>
<role rolename="manager-script"/>
<role rolename="manager-status"/>
<user username="admin" password="admin" roles="admin-gui,manager-gui,manager-jmx,manager-script,manager-status"/>
```

- manager-gui - 允许访问 HTML GUI 和状态页面
- manager-script - 允许访问文本界面和状态页面
- manager-jmx - 允许访问 JMX 代理和状态页面
- manager-status - 仅允许访问状态页面

```bash
service tomcat start
service tomcat stop
```

如果爆 403 错误,就注释掉 Tomcat/webapps/manager/META-INF/context.xml 文件中内容
```xml
<!-- <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />-->
```

自行重启服务

**发布测试**

tomcat 默认的发布 web 项目的目录是：webapps

将导出的 war 包直接上传到 webapps 根目录下,随着 tomcat 的启动,war 包可以自动被解析.

然后调用路径查询是否安装成功

---

## Wordpress

**官网**
- https://wordpress.org/

**下载 WordPress 安装包并解压**
```bash
wget https://wordpress.org/latest.tar.gz

tar -xzvf latest.tar.gz
```

**创建 WordPress 数据库和一个用户**
```bash
yum install mariadb mariadb-server
systemctl start mariadb
systemctl enable mariadb
mysql_secure_installation

mysql -u root -p

创建一个专给WordPress存数据的数据库
MariaDB [(none)]> create database idiota_info;  # 最后的"idiota_info"为数据库名

创建用于WordPress对应用户
MariaDB [(none)]> create user idiota@localhost identified by 'password';   # "idiota"对应创建的用户,"password"内填写用户的密码

分别配置本地登录和远程登录权限
MariaDB [(none)]> grant all privileges on idiota_info.* to idiota@'localhost' identified by 'password';
MariaDB [(none)]> grant all privileges on idiota_info.* to idiota@'%' identified by 'password';

刷新权限
MariaDB [(none)]> flush privileges;
```

**配置 PHP**
```bash
# 安装PHP源
rpm -ivh https://mirror.webtatic.com/yum/el7/epel-release.rpm
rpm -ivh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

# 安装 PHP7.0
yum install php70w
yum install php70w-mysql
yum install httpd

# 重启Apache
systemctl restart httpd

# 查看PHP版本
php -v
```

**设置 wp-config.php 文件**
```bash
cd wordpress
vim wp-config-sample.php
```
在标有 `// ** MySQL settings - You can get this info from your web host ** //` 下输入你的数据库相关信息
```
DB_NAME
    在第二步中为 WordPress 创建的数据库名称
DB_USER
    在第二步中创建的 WordPress 用户名
DB_PASSWORD
    第二步中为 WordPress 用户名设定的密码
DB_HOST
    第二步中设定的 hostname (通常是 localhost,但总有例外；参见编辑wp-config.php 文件中的"可能的 DB_HOST 值) .
DB_CHARSET
    数据库字符串,通常不可更改.
DB_COLLATE
    留为空白的数据库排序.
```

在标有 `* Authentication Unique Keys.` 的版块下输入密钥的值,保存 wp-config.php 文件,也可以不管这个

**上传文件**

接下来需要决定将博客放在网站的什么位置上：
- 网站根目录下 (如：http://example.com/)
- 网站子目录下 (如：http://example.com/blog/)

根目录

如果需要将文件上传到 web 服务器,可用 FTP 客户端将 wordpress 目录下所有内容 (无需上传目录本身) 上传至网站根目录

如果文件已经在 web 服务器中且希望通过 shell 访问来安装 wordpress,可将 wordpress 目录下所有内容 (无需转移目录本身) 转移到网站根目录

子目录

如果需要将文件上传到 web 服务器,需将 wordpress 目录重命名,之后用 FTP 客户端将重命名后的目录上传到网站根目录下某一位置

如果文件已经在 web 服务器中且希望通过shell访问来安装 wordpress,可将 wordpress 目录转移到网站根目录下某一位置,之后重命名 wordpress 目录

```bash
mv wordpress/* /var/www/html

setenforce 0  # 关闭 selinux
service httpd start
service firewalld stop
```

**运行安装脚本**

在常用的 web 浏览器中运行安装脚本.

将 WordPress 文件放在根目录下的用户请访问：http://example.com/wp-admin/install.php

将 WordPress 文件放在子目录 (假设子目录名为 blog) 下的用户请访问：http://example.com/blog/wp-admin/install.php

访问 `http://xxx.xxx.xxx.xxx/wp-admin/setup-config.php` 下面就略了,自己照着页面上显示的来

---

## Mijisou

`基于开源项目 Searx 二次开发的操作引擎`

**官网**
- https://mijisou.com/

**依赖**

自行安装 python3 pip redis

**安装**
```bash
systemctl start redis
systemctl enable redis
git clone https://github.com/entropage/mijisou.git
cd mijisou && pip install -r requirements.txt
```

**配置**
```yml
vim searx/settings_et_dev.yml

general:
    debug : False # Debug mode, only for development
    instance_name : "123搜索" # displayed name

search:
    safe_search : 0 # Filter results. 0: None, 1: Moderate, 2: Strict
    autocomplete : "" # Existing autocomplete backends: "baidu", "dbpedia", "duckduckgo", "google", "startpage", "wikipedia" - leave blank to turn it off by default
    language : "zh-CN"
    ban_time_on_fail : 5 # ban time in seconds after engine errors
    max_ban_time_on_fail : 120 # max ban time in seconds after engine errors

server:
    port : 8888
    bind_address : "0.0.0.0" # address to listen on
    secret_key : "123" # change this!
    base_url : False # Set custom base_url. Possible values: False or "https://your.custom.host/location/"
    image_proxy : False # Proxying image results through searx
    http_protocol_version : "1.0"  # 1.0 and 1.1 are supported

cache:
    cache_server : "127.0.0.1" # redis cache server ip address
    cache_port : 6379 # redis cache server port
    cache_time : 86400 # cache 1 day
    cache_type : "redis" # cache type
    cache_db : 0 # we use db 0 in dev env

ui:
    static_path : "" # Custom static path - leave it blank if you didn't change
    templates_path : "" # Custom templates path - leave it blank if you didn't change
    default_theme : entropage # ui theme
    default_locale : "" # Default interface locale - leave blank to detect from browser information or use codes from the 'locales' config section
    theme_args :
        oscar_style : logicodev # default style of oscar

# searx supports result proxification using an external service: https://github.com/asciimoo/morty
# uncomment below section if you have running morty proxy
result_proxy:
    url : ""  #morty proxy service
    key : Your_result_proxy_key
    server_name : ""

outgoing: # communication with search engines
    request_timeout : 2.0 # seconds
    useragent_suffix : "" # suffix of searx_useragent, could contain informations like an email address to the administrator
    pool_connections : 100 # Number of different hosts
    pool_maxsize : 10 # Number of simultaneous requests by host
# uncomment below section if you want to use a proxy
# see http://docs.python-requests.org/en/latest/user/advanced/#proxies
# SOCKS proxies are also supported: see http://docs.python-requests.org/en/master/user/advanced/#socks
#    proxies :
#        http : http://192.168.199.5:24000
#        http : http://192.168.199.5:3128
#        https: http://127.0.0.1:8080
# uncomment below section only if you have more than one network interface
# which can be the source of outgoing search requests
#    source_ips:
#        - 1.1.1.1
#        - 1.1.1.2
    haipproxy_redis:
      #host: 192.168.199.5
      #port: 6379
      #password: kckdkkdkdkddk
      #db: 0

engines:
  - name : duckduckgo
    engine : duckduckgo
    shortcut : ddg

  - name : duckduckgo images
    engine : duckduckgo_images
    shortcut : ddi

  - name : twitter
    engine : twitter
    shortcut : tw

  - name : mojeek
    shortcut: mjk
    engine: xpath
    paging : True
    search_url : https://www.mojeek.com/search?q={query}&s={pageno}
    results_xpath: /html/body//div[@class="results"]/ul[@class="results-standard"]/li
    url_xpath : ./h2/a/@href
    title_xpath : ./h2
    content_xpath : ./p[@class="s"]
    suggestion_xpath : /html/body//div[@class="top-info"]/p[@class="top-info spell"]/a
    first_page_num : 1
    page_size : 10

  - name : torrentz
    engine : torrentz
    shortcut : tor
    url: https://torrentz2.eu/
    timeout : 3.0

  - name : startpage
    engine : startpage
    shortcut : sp
    timeout : 6.0

  - name : baidu
    engine : baidu
    shortcut : bd

  - name : baidu images
    engine : baidu_images
    shortcut : bdi

  - name : baidu videos
    engine : baidu_videos
    shortcut : bdv

  - name : sogou images
    engine : sogou_images
    shortcut : sgi

  - name : sogou videos
    engine : sogou_videos
    shortcut : sgv

  - name : 360 images
    engine : so_images
    shortcut : 360i

  - name : bing
    engine : bing
    shortcut : bi

  - name : bing images
    engine : bing_images
    shortcut : bii

  - name : bing videos
    engine : bing_videos
    shortcut : biv

  - name : bitbucket
    engine : xpath
    paging : True
    search_url : https://bitbucket.org/repo/all/{pageno}?name={query}
    url_xpath : //article[@class="repo-summary"]//a[@class="repo-link"]/@href
    title_xpath : //article[@class="repo-summary"]//a[@class="repo-link"]
    content_xpath : //article[@class="repo-summary"]/p
    categories : it
    timeout : 4.0
    shortcut : bb

  - name : free software directory
    engine : mediawiki
    shortcut : fsd
    categories : it
    base_url : https://directory.fsf.org/
    number_of_results : 5
    search_type : title
    timeout : 5.0

  - name : gentoo
    engine : gentoo
    shortcut : ge

  - name : gitlab
    engine : json_engine
    paging : True
    search_url : https://gitlab.com/api/v4/projects?search={query}&page={pageno}
    url_query : web_url
    title_query : name_with_namespace
    content_query : description
    page_size : 20
    categories : it
    shortcut : gl
    timeout : 10.0

  - name : github
    engine : github
    shortcut : gh

  - name : stackoverflow
    engine : stackoverflow
    shortcut : st

  - name : wikipedia
    engine : wikipedia
    shortcut : wp
    base_url : 'https://en.wikipedia.org/'

locales:
    en : English
    ar : العَرَبِيَّة (Arabic)
    bg : Български (Bulgarian)
    cs : Čeština (Czech)
    da : Dansk (Danish)
    de : Deutsch (German)
    el_GR : Ελληνικά (Greek_Greece)
    eo : Esperanto (Esperanto)
    es : Español (Spanish)
    fi : Suomi (Finnish)
    fil : Wikang Filipino (Filipino)
    fr : Français (French)
    he : עברית (Hebrew)
    hr : Hrvatski (Croatian)
    hu : Magyar (Hungarian)
    it : Italiano (Italian)
    ja : 日本語 (Japanese)
    nl : Nederlands (Dutch)
    pl : Polski (Polish)
    pt : Português (Portuguese)
    pt_BR : Português (Portuguese_Brazil)
    ro : Română (Romanian)
    ru : Русский (Russian)
    sk : Slovenčina (Slovak)
    sl : Slovenski (Slovene)
    sr : српски (Serbian)
    sv : Svenska (Swedish)
    tr : Türkçe (Turkish)
    uk : українська мова (Ukrainian)
    zh : 简体中文 (Chinese, Simplified)
    zh_TW : 繁體中文 (Chinese, Traditional)

doi_resolvers :
  oadoi.org : 'https://oadoi.org/'
  doi.org : 'https://doi.org/'
  doai.io  : 'http://doai.io/'
  sci-hub.tw : 'http://sci-hub.tw/'

default_doi_resolver : 'oadoi.org'

sentry:
  dsn: https://xkdkkdkdkdkdkdkdk@sentry.xxx.com/2
```

**运行+caddy 反代**
```bash
mv searx/settings_et_dev.yml searx/settings.yml
gunicorn searx.webapp:app -b 127.0.0.1:8888 -D	# 一定要在mijisou目录下运行

wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubiBackup/doubi/master/caddy_install.sh && chmod +x caddy_install.sh && bash caddy_install.sh

echo "www.你的域名.com {
 gzip
 tls xxxx@xxx.com
 proxy / 127.0.0.1:8888
}" >> /usr/local/caddy/Caddyfile

/etc/init.d/caddy start
# 如果启动失败可以看 Caddy 日志：tail -f /tmp/caddy.log
```

**opensearch**
```xml
vim /root/mijisou/searx/templates/__common__/opensearch.xml

<?xml version="1.0" encoding="utf-8"?>
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>{{ instance_name }}</ShortName>
  <Description>a privacy-respecting, hackable metasearch engine</Description>
  <InputEncoding>UTF-8</InputEncoding>
  <Image>{{ urljoin(host, url_for('static', filename='img/favicon.png')) }}</Image>
   <LongName>searx metasearch</LongName>
  {% if opensearch_method == 'get' %}
     <Url type="text/html" method="get" template="https://www.你的域名.com/?q={searchTerms}"/>
  {% if autocomplete %}
  <Url type="application/x-suggestions+json" method="get" template="{{ host }}autocompleter">
      <Param name="format" value="x-suggestions" />
      <Param name="q" value="{searchTerms}" />
  </Url>
  {% endif %}
  {% else %}
  <Url type="text/html" method="post" template="{{ host }}">
    <Param name="q" value="{searchTerms}" />
  </Url>
  {% if autocomplete %}
  <!-- TODO, POST REQUEST doesn't work -->
  <Url type="application/x-suggestions+json" method="get" template="{{ host }}autocompleter">
  <Param name="format" value="x-suggestions" />
  <Param name="q" value="{searchTerms}" />
  </Url>
  {% endif %}
  {% endif %}
</OpenSearchDescription>
```

**修改**

`秘迹®️是熵加网络科技 (北京) 有限公司所持有的注册商标,任何组织或个人在使用代码前请去除任何和秘迹相关字段,去除秘迹搜索的UI设计,否则熵加网络科技 (北京) 有限公司保留追究法律责任的权利.`

配置文件中改下名字
`mijisou/searx/static/themes/entropage/img` 中的 logo 图标自己换一下

**管理**
```bash
ps -aux
看一下哪个是 gunicorn 进程
kill 杀掉
gunicorn searx.webapp:app -b 127.0.0.1:8888 -D  # 再次强调,在 /mijisou 目录下运行
```

**配合 Cloudflare 的 CDN**
1. Cloudflare 创建 site
2. 域名商改 nameserver
3. 修改 Caddy 配置
  ```bash
  echo "www.你的域名.com:80 {
  gzip
  proxy / 127.0.0.1:8888
  }" >> /usr/local/caddy/Caddyfile
  ```

**磁盘占用**

服务运行一段时间后,`/var/lib/redis` 路径下会有一些缓存文件(貌似),直接删了就行

**Thank**
- [asciimoo/searx](https://github.com/asciimoo/searx)
- [entropage/mijisou: Privacy-respecting metasearch engine](https://github.com/entropage/mijisou)
- [一个可以保护个人隐私的网络搜索服务：秘迹搜索搭建教程 - Rat's Blog](https://www.moerats.com/archives/922/)
- [OpenSearch description format | MDN](https://developer.mozilla.org/en-US/docs/Web/OpenSearch)
- [Add or remove a search engine in Firefox | Firefox Help](https://support.mozilla.org/en-US/kb/add-or-remove-search-engine-firefox)

---

# 数据库
## Relational
### Oracle

![image](../../../assets/img/才怪.png)

### Mariadb

**官网**
- https://mariadb.org/

**安装**

`yum install mariadb mariadb-server`

**数据库初始化**
```bash
systemctl start mariadb
mysql_secure_installation
```

|配置流程 	|说明 |操作|
|------------ | ------------- | ------------|
Enter current password for root (enter for none) |	输入 root 密码 	| 初次运行直接回车
Set root password? [Y/n] |	是设置 root 密码 |	可以 y 或者 回车
New password |	输入新密码
Re-enter new password |	再次输入新密码
Remove anonymous users? [Y/n] |	是否删除匿名用户 | 可以 y 或者回车 本题y
Disallow root login remotely? [Y/n]  |	是否禁止 root 远程登录 |  可以 y 或者回车 本题n
Remove test database and access to it? [Y/n]  |	是否删除 test 数据库 | y 或者回车 本题y
Reload privilege tables now? [Y/n] | 是否重新加载权限表 | y 或者回车 本题y

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

systemctl enable mariadb
```

**重置密码**

```bash
# 先关服务
systemctl stop mariadb

# 用以下命令在没有权限检查的情况下重新启动数据库
mysqld_safe --skip-grant-tables &

# 这里, --skip-grant-tables 选项让你在没有密码和所有权限的情况下进行连接.如果使用此选项启动服务器,它还会启用 --skip-networking 选项,这用于防止其他客户端连接到数据库服务器.并且,& 符号用于在后台运行命令,因此你可以在以下步骤中输入其他命令.请注意,上述命令很危险,并且你的数据库会变得不安全.你应该只在短时间内运行此命令以重置密码.

# 接下来,以 root 用户身份登录 MySQL/MariaDB 服务器：
mysql

# 在 mysql > 或 MariaDB [(none)] > 提示符下,运行以下命令重置 root 用户密码：
UPDATE mysql.user SET Password=PASSWORD('NEW-PASSWORD') WHERE User='root';

# 使用你自己的密码替换上述命令中的 NEW-PASSWORD.
# 然后,输入以下命令退出 mysql 控制台.

FLUSH PRIVILEGES;
exit

# 最后,关闭之前使用 --skip-grant-tables 选项运行的数据库.为此,运行：
mysqladmin -u root -p shutdown
# 系统将要求你输入在上一步中设置的 MySQL/MariaDB 用户密码.

systemctl start mariadb
mysql -u root -p
```

---

### MySQL

**官网**
- https://www.mysql.com

**安装**

和 Mariadb 差不多,看 Mariadb 的就行了
```bash
apt install mysql-server mysql-clien

service mysql start
```

---

### Postgresql

**官网**
- https://www.postgresql.org

**安装**
```bash
yum install postgresql-server
postgresql-setup initdb # 初始化数据库
service postgresql start  # 启动服务
```

PostgreSQL 安装完成后,会建立一下 ‘postgres’ 用户,用于执行 PostgreSQL,数据库中也会建立一个 'postgres' 用户,默认密码为自动生成,需要在系统中改一下.

**修改用户密码**
```sql
sudo -u postgres psql postgres
\l # 查看当前的数据库列表 
\password postgres  # 给 postgres 用户设置密码
\q  # 退出数据库
```

**开启远程访问**
```vim
vim /var/lib/pgsql/data/postgresql.conf

listen_addresses='*'
```
```vim
vim /var/lib/pgsql/data/pg_hba.conf

# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
host    all             all             0.0.0.0/0               md5

# 其中 0.0.0.0/0 表示运行任意 ip 地址访问.
# 若设置为 192.168.1.0/24 则表示允许来自 ip 为 192.168.1.0 ~ 192.168.1.255 之间的访问.
```

`service postgresql restart` 防火墙记得放行

---

## Document
### MongoDB

**官网**
- https://www.mongodb.com/

**安装**
```vim
vim /etc/yum.repos.d/mongodb-org-4.0.repo

[mongodb-org-4.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc
```

`yum install -y mongodb-org`

**配置远程访问**
```vim
vim /etc/mongod.conf

# Listen to all ip address
bind_ip = 0.0.0.0
```

`service mongod start`

**创建管理员用户**
```sql
mongo
>use admin
 db.createUser(
  {
    user: "myUserAdmin",
    pwd: "abc123",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
 )

> show dbs;	# 查看数据库
> db.version();	# 查看数据库版本
```

**启用权限管理**
```vim
vim /etc/mongod.conf

#security
security:
authorization: enabled
```

`service mongod restart	`

---

## Key-value
### Redis

**官网**
- https://redis.io/

**安装**
- **包管理器方式**

  在 CentOS 和 Red Hat 系统中,首先添加 EPEL 仓库,然后更新 yum 源:

  ```bash
  wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
  yum clean all
  yum makecache
  yum install redis
  ```

  在 debian 中

  `apt install redis-server`

  安装好后启动 Redis 服务即可

  `systemctl start redis`

- **源代码编译方式安装**

  在官网下载 tar.gz 的安装包,或者通过 wget 的方式下载

  `wget http://download.redis.io/releases/redis-5.0.5.tar.gz`

  安装
  ```bash
  tar -zxvf redis-5.0.5.tar.gz
  cd redis-5.0.5
  make
  yum install tcl tcl-devel -y
  make test
  make MALLOC=libc
  make install
  ```
  ```bash
  ./usr/local/bin/redis-server
  ctrl+z
  bg
  redis-cli
  ```

使用 redis-cli 进入 Redis 命令行模式操作
```bash
redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> exit
```

**开启远程访问**

为了可以使 Redis 能被远程连接,需要修改配置文件,路径为 /etc/redis.conf
```vim
vim /etc/redis.conf

#bind 127.0.0.1
requirepass 密码	#设置 redis 密码
```
`service redis restart` 当然还要记得开防火墙

`redis-cli -h <ip> -p 6379 -a <PASSWORD>`

**压测**

Redis-benchmark 是官方自带的 Redis 性能测试工具,可以有效的测试 Redis 服务的性能.
```bash
redis-benchmark -h 127.0.0.1 -p 6379 -c 100 -n 100000
# 100 个并发连接,100000 个请求,检测 host 为 localhost 端口为 6379 的 redis 服务器性能

redis-benchmark -h 127.0.0.1 -p 6379 -q -d 100
# 测试存取大小为100字节的数据包的性能

redis-benchmark -t set,lpush -n 100000 -q
# 只测试某些操作的性能

redis-benchmark -n 100000 -q script load "redis.call('set','foo','bar')"
# 只测试某些数值存取的性能
```

---

### Memcached

**官网**
- https://memcached.org/

**安装**
- **软件包安装**
  ```bash
  yum -y install memcached
  cat /etc/sysconfig/memcached
  ```

- **源代码编译方式安装**

  在官网下载 tar.gz 的安装包,或者通过 wget 的方式下载

  `wget http://memcached.org/latest`

  安装
  ```bash
  tar -zxvf memcached-1.x.x.tar.gz
  cd memcached-1.x.x
  ./configure --prefix=/usr/local/memcached
  make && make test
  make install
  ```

**运行**
```bash
systemctl start memcached
systemctl enable memcached

firewall-cmd --add-port=11211/tcp --permanent
firewall-cmd --reload
```

---

# 文本工具
## Vim

**常用配置**

`sudo vim /etc/vim/vimrc` 或 `sudo vim /etc/vimrc`
最后面直接添加你想添加的配置,下面是一些常用的 (不建议直接复制这个货网上的,要理解每个的含义及有什么用,根据自己需要来调整) 
```vim
set number # 显示行号
set nobackup # 覆盖文件时不备份
set cursorline # 突出显示当前行
set ruler # 在右下角显示光标位置的状态行
set shiftwidth=4 # 设定 > 命令移动时的宽度为 4
set softtabstop=4 # 使得按退格键时可以一次删掉 4 个空格
set tabstop=4 # 设定 tab 长度为 4(可以改) 
set smartindent # 开启新行时使用智能自动缩进
set ignorecase smartcase # 搜索时忽略大小写,但在有一个或以上大写字母时仍 保持对大小写敏感

下面这个没觉得很有用,在代码多的时候会比较好
#set showmatch # 插入括号时,短暂地跳转到匹配的对应括号
#set matchtime=2 # 短暂跳转到匹配括号的时间
```

**解决 ssh 后 vim 中不能使用小键盘的问题**
- xshell

  更改的方法: 在终端设置中选择终端类型为 linux

- ubuntu
  ```bash
  sudo apt-get remove vim-common
  sudo apt-get install vim
  ```

**[SpaceVim - 模块化的 Vim IDE](https://spacevim.org/cn/)**

---

# 文件服务
## filebrowser

`一个在线网盘服务,只能在线看图片,在线看视频是不支持的 ^w^`

**项目地址**
- https://github.com/filebrowser/filebrowser

**安装**

`curl -fsSL https://filebrowser.xyz/get.sh | bash`

**使用**

filebrowser -a <你自己的IP> -r <文件夹路径>

默认账号密码 admin

---

## NFS

**服务端**

安装
```bash
yum ‐y install nfs‐utils
```

修改配置文件
```vim
vim /etc/exports
/public 192.168.xxx.xxx(ro)
```

启服务
```bash
mkdir /public

vi /etc/selinux/config
	SELINUX=disabled

firewall-cmd --zone=public --add-service=rpc-bind --permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload

service rpcbind start
service nfs start
```

**客户端**

安装,创建用户
```bash
yum ‐y install nfs‐utils
mkdir /mnt/nfsfiles

useradd nfsuser1
passwd nfsuser1
```

验证共享是否成功

`showmount ‐e 192.168.xxx.xxx`

挂载共享目录
```vim
vim /etc/fstab

192.168.xxx.xxx:/public /mnt/nfsfiles/	nfs defaults 0 0
```

`su ‐l nfsuser1`

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

## Samba

**官网**
- https://www.samba.org

**服务端**

安装

`yum install samba `

修改配置文件
```vim
vim /etc/samba/smb.conf
[smbshare]
path = /smbshare	# 共享目录
public = yes
writeable=yes
hosts allow = 192.168.1xx.33/32	# 允许主机
hosts deny = all
create mask = 0770	# 创建文件的权限为 0770；
```

验证配置文件有没有错误

`testparm`

**用户配置**
```bash
# 添加用户,设置密码
useradd smb1
smbpasswd ‐a smb1(密码：smb123456)

# 将用户添加到 samba 服务器中,并设置密码
pdbedit ‐a smb1(密码：smb123456)

# 查看 samba 数据库用户
pdbedit ‐L
```

创建共享目录,设置所有者和所属组
```bash
mkdir /smbshare
chown smb1:smb1 /smbshare
```

关闭 selinux (需要重启) 
```vim
vim /etc/selinux/config
SELINUX=disabled
```
```bash
firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload

systemctl restart smb
```

**客户端**
```bash
yum install samba

mkdir /data/web_data
mount -t cifs -o username=smb1,password='smb123456' //192.168.xx+1.xx/webdata
/data/web_data
```

---

## Vsftp

**官网**
- https://security.appspot.com/vsftpd.html

**匿名访问**

|参数|作用|
| :------------- | :------------- |
|anonymous_enable=YES |	允许匿名访问模式 |
|anon_umask=022 |	匿名用户上传文件的umask值|
|anon_upload_enable=YES |	允许匿名用户上传文件|
|anon_mkdir_write_enable=YES |	允许匿名用户创建目录|
|anon_other_write_enable=YES |	允许匿名用户修改目录名称或删除目录|

```vim
vim /etc/vsftpd/vsftpd.conf

anonymous_enable=YES
anon_umask=022
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
```
```bash
setenforce 0  # 关闭 selinux
firewall-cmd --permanent --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

现在就可以在客户端执行 ftp 命令连接到远程的 FTP 服务器了.
在 vsftpd 服务程序的匿名开放认证模式下,其账户统一为 anonymous,密码为空.而且在连接到 FTP 服务器后,默认访问的是 /var/ftp 目录.
我们可以切换到该目录下的 pub 目录中,然后尝试创建一个新的目录文件,以检验是否拥有写入权限：
```bash
[root@linuxprobe ~]# ftp 192.168.10.10
Connected to 192.168.10.10 (192.168.10.10).
220 (vsFTPd 3.0.2)
Name (192.168.10.10:root): anonymous
331 Please specify the password.
Password:此处敲击回车即可
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

ftp> cd pub
250 Directory successfully changed.

ftp> mkdir files
257 "/pub/files" created

ftp> rename files database
350 Ready for RNTO.
250 Rename successful.

ftp> rmdir database
250 Remove directory operation successful.

ftp> exit
221 Goodbye.
```

---

**本地用户**

|参数 |	作用|
| :------------- | :------------- |
|anonymous_enable=NO 	|禁止匿名访问模式|
|local_enable=YES |	允许本地用户模式|
|write_enable=YES |	设置可写权限|
|local_umask=022 |	本地用户模式创建文件的umask值|
|userlist_deny=YES 	|启用"禁止用户名单",名单文件为 ftpusers 和 user_list|
|userlist_enable=YES |	开启用户作用名单文件功能|

```vim
vim /etc/vsftpd/vsftpd.conf

anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
```
```bash
setenforce 0  # 关闭 selinux
firewall-cmd --permanent --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```
按理来讲,现在已经完全可以本地用户的身份登录 FTP 服务器了.但是在使用 root 管理员登录后,系统提示如下的错误信息：
```bash
[root@linuxprobe ~]# ftp 192.168.10.10
Connected to 192.168.10.10 (192.168.10.10).
220 (vsFTPd 3.0.2)
Name (192.168.10.10:root): root
530 Permission denied.
Login failed.
ftp>
```
可见,在我们输入 root 管理员的密码之前,就已经被系统拒绝访问了.这是因为 vsftpd 服务程序所在的目录中默认存放着两个名为"用户名单"的文件 (ftpusers 和 user_list) .只要里面写有某位用户的名字,就不再允许这位用户登录到 FTP 服务器上.
```bash
[root@linuxprobe ~]# cat /etc/vsftpd/user_list

[root@linuxprobe ~]# cat /etc/vsftpd/ftpusers
```
如果你确认在生产环境中使用 root 管理员不会对系统安全产生影响,只需按照上面的提示删除掉 root 用户名即可.我们也可以选择 ftpusers 和 user_list 文件中没有的一个普通用户尝试登录 FTP 服务器
在采用本地用户模式登录FTP服务器后,默认访问的是该用户的家目录,也就是说,访问的是 /home/username 目录.而且该目录的默认所有者、所属组都是该用户自己,因此不存在写入权限不足的情况.

---

**虚拟用户**

安装

`yum install vsftpd`

认证

创建虚拟用户文件,把这些用户名和密码存放在一个文件中.该文件内容格式是：用户名占用一行,密码占一行.

`cd /etc/vsftp`

```vim
vim login.list

Ftpuser1
123456
Ftpuser2
123456
Ftpadmin
123456
```

使用 db_load 命令生成 db 口令 login 数据库文件

`db_load -T -t hash -f login.list login.db`

通过修改指定的配置文件,调整对该程序的认证方式
```vim
vim /etc/vsftpd/vsftpd.conf

pam_service_name=vsftpd.vu  # 设置 PAM 使用的名称,该名称就是 /etc/pam.d/ 目录下 vsfptd 文件的文件名
```
`cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.vu`
```vim
vim /etc/pam.d/vsftpd.vu

auth       required     pam_userdb.so db=/etc/vsftpd/login
account    required     pam_userdb.so db=/etc/vsftpd/login
# 注意：格式是 db=/etc/vsftpd/login 这样的,一定不要去掉源文件的 .db 后缀
```

配置文件
```vim
vim /etc/vsftpd/vsftpd.conf

anonymous_enable=NO
local_enable=YES
guest_enable=YES
guest_username=virtual
pam_service_name=vsftpd.vu
allow_writeable_chroot=YES
```

|参数 |	作用|
| :------------- | :------------- |
|anonymous_enable=NO 	|禁止匿名开放模式|
|local_enable=YES |	允许本地用户模式|
|guest_enable=YES |	开启虚拟用户模式|
|guest_username=virtual |	指定虚拟用户账户|
|pam_service_name=vsftpd.vu |	指定PAM文件|
|allow_writeable_chroot=YES |	允许对禁锢的FTP根目录执行写入操作,而且不拒绝用户的登录请求|

用户配置权限文件
所有用户主目录为 /home/ftp 宿主为 virtual 用户；
```bash
useradd -d /home/ftp -s /sbin/nologin virtual
chmod -Rf 755 /home/ftp/
cd /home/ftp/
touch testfile
```
```vim
vim /etc/vsftpd/vsftpd.conf

guest_enable=YES      # 表示是否开启 vsftpd 虚拟用户的功能,yes 表示开启,no 表示不开启.
guest_username=virtual       # 指定虚拟用户的宿主用户
user_config_dir=/etc/vsftpd/user_conf     # 设定虚拟用户个人 vsftpd 服务文件存放路径
allow_writeable_chroot=YES
```

编辑用户权限配置文件
```vim
vim Ftpadmin  # 创建 Ftpadmin 这个用户的配置文件

anon_upload_enable=YES
anon_mkdir_wirte_enable=YES
anon_other_wirte_enable=YES
anon_umask=022


# 要求虚拟用户具有写权限 (上传、下载、删除、重命名) 

# umask = 022 时,新建的目录 权限是755,文件的权限是 644
# umask = 077 时,新建的目录 权限是700,文件的权限时 600
# vsftpd的local_umask和anon_umask借鉴了它
# 默认情况下vsftp上传之后文件的权限是600,目录权限是700
# 想要修改上传之后文件的权限,有两种情况
# 如果使用vsftp的是本地用户
# 则要修改配置文件中的 local_umask 的值
# 如果使用vsftp的是虚拟用户
# 则要修改配置文件中的 anon_umask 的值
```

**启服务**
```bash
setenforce 0  # 关闭 selinux
firewall-cmd --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

**Reference**
- [第11章 使用Vsftpd服务传输文件.](https://www.linuxprobe.com/chapter-11.html)

---

# 编程语言
## C

```c
vim world.c

#include <stdio.h>
int main(void){
				printf("Hello World");
				return 0;
}
```
```bash
gcc helloworld.c -o execFile
./execFlie
```

---

## Go

**官网**
- https://golang.org/

**安装**
```bash
访问 https://golang.org/dl/ 下载最新版本包

tar -C /usr/local -xzf 相应文件.tar.gz

export GOROOT=$HOME/go
export PATH=$PATH:$GOROOT/bin
export GOPATH=$HOME/Applications/Go
source $HOME/.profile
# $GOPATH 可以包含多个工作目录,取决于你的个人情况.如果你设置了多个工作目录,那么当你在之后使用 go get (远程包安装命令) 时远程包将会被安装在第一个目录下.
go version
```

**Test your installation**
```bash
mkdir -p $HOME/Applications/Go
cd $HOME/Applications/Go
```
```vim
vim hello.go


package main

import "fmt"

func main() {
	fmt.Printf("hello, world\n")
}
```
```bash
go build
./hello
```

---

## JDK

**rpm 包方式安装**

下载
https://www.oracle.com/technetwork/java/javase/downloads/
```bash
chmod +x jdk-****.rpm
yum localinstall jdk-****.rpm
也可以
rpm -ivh jdk-****.rpm
```

**使用 ppa/源方式安装**
1. 添加 ppa

    `sudo add-apt-repository ppa:webupd8team/java`

    `sudo apt-get update`

2. 安装 oracle-java-installer

	jdk7

	`sudo apt-get install oracle-java7-installer`

	jdk8

	`sudo apt-get install oracle-java8-installer`

**编译安装**

自行下载 [oracle jdk](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

这里以 `jdk-8u212-linux-x64.tar.gz` 举例

```bash
bash
tar -xzvf jdk-8u212-linux-x64.tar.gz
mv jdk1.8.0_212/ /usr/local/lib/jvm/
cd /usr/local/lib/
mv jvm jdk
mv jdk jdk1.8
export JAVA_HOME=/usr/local/lib/jdk1.8/

export JRE_HOME=JAVAHOME/jreexportCLASSPATH=.:{JAVA_HOME}/lib:JREHOME/libexportPATH={JAVA_HOME}/bin:$PATH
update-alternatives --install /usr/bin/java java /usr/local/lib/jdk1.8/bin/java 1
update-alternatives --install /usr/bin/javac javac /usr/local/lib/jdk1.8/bin/javac 1

update-alternatives --set java /usr/local/lib/jdk1.8/bin/java

update-alternatives --set javac /usr/local/lib/jdk1.8/bin/javac
```

**测试**
```bash
java
javac
```

---

## Python3

**官网**
- https://www.python.org/

**yum 安装**
```bash
yum install epel-release
或
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum -y install python36 python36-devel

wget https://bootstrap.pypa.io/get-pip.py	# 安装pip3
python3 get-pip.py
```

**源代码编译方式安装**

安装依赖环境
```bash
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

下载Python3

`wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz`

安装python3
```bash
mkdir -p /usr/local/python3
tar zxvf Python-3.6.1.tgz
cd Python-3.6.1
./configure --prefix=/usr/local/python3
make
make install 或者 make && make install
```

添加到环境变量
```bash
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```
```vim
vim ~/.bash_profile # 永久修改变量

PATH=$PATH:/usr/local/python3/bin/
```
`source ~/.bash_profile`

检查 Python3 及 pip3 是否正常可用
```bash
python3 -V
pip3 -V
```

**加速**
- [pip](../../Misc/Plan/Misc-Plan.md#pip)

---

## Ruby

**官网**
- https://www.ruby-lang.org

**安装**

注:在 Ubuntu 下有点问题,不建议用 Ubuntu 做运维环境
下载 ruby 安装包,并进行编译安装
```bash
wget https://cache.ruby-lang.org/pub/ruby/2.6/ruby-2.6.2.tar.gz
tar xvfvz ruby-2.6.2.tar.gz
cd ruby-2.6.2
./configure
make
make install
```

将 ruby 添加到环境变量,ruby 安装在/usr/local/bin/目录下,因此编辑 ~/.bash_profile文件,添加一下内容:
```bash
vim ~/.bash_profile

export PATH=$PATH:/usr/local/bin/
```
`source ~/.bash_profile` 不要忘了生效一下

---

# 管理工具
## Supervisor

**官网**
- http://supervisord.org/

**安装**

因为 Supervisor 是 Python 开发的,安装前先检查一下系统否安装了 Python2.4 以上版本.

`pip install supervisor`

安装完成后,我们使用 echo_supervisord_conf 命令创建一个 Supervisor 配置文件

`echo_supervisord_conf > /etc/supervisord.conf`

**配置**

接着在 /etc/supervisord.conf 文件最下方加入目标程序的启动项目
```conf
vim /etc/supervisord.conf

; [program:xx]是被管理的进程配置参数,xx是进程的名称
[program:xx]
command=/opt/apache-tomcat-8.0.35/bin/catalina.sh run  ; 程序启动命令
autostart=true       ; 在 supervisord 启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出,就表示进程正常启动了,默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false],默认为 unexpected,表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数,默认是3
user=tomcat          ; 用哪个用户启动进程,默认是root
priority=999         ; 进程启动优先级,默认999,值小的优先启动
redirect_stderr=true ; 把 stderr 重定向到 stdout,默认 false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小,默认 50MB s
tdout_logfile_backups = 20   ; stdout 日志文件备份数,默认是10
; stdout 日志文件,需要注意当指定目录不存在时无法正常启动,所以需要手动创建目录 (supervisord 会自动创建日志文件) 
stdout_logfile=/opt/apache-tomcat-8.0.35/logs/catalina.out
stopasgroup=false     ;默认为 false,进程被杀死时,是否向这个进程组发送 stop 信号,包括子进程
killasgroup=false     ;默认为 false,向进程组发送 kill 信号,包括子进程
```

注意修改 user = tomcat

接着直接运行 Supervisor 即可让目标程序保持后台运行,运行服务时,需要指定 supervisor 配置文件

`supervisord -c /etc/supervisord.conf`

```bash
supervisorctl status
supervisorctl stop tomcat
supervisorctl start tomcat
supervisorctl restart tomcat
supervisorctl reread
supervisorctl update
```

**Reference**
- [Supervisor 安装与配置 (Linux/Unix 进程管理工具) ](https://blog.csdn.net/xyang81/article/details/51555473)

---

## Webmin

**官网**
- http://www.webmin.com/index.html

**安装**

在官网下载 RPM 包,上传至服务器,这里以 1.930-1 为例
```bash
yum -y install perl-Net-SSLeay
yum -y install perl-Encode-Detect
yum -y install perl-Data-Dumper
rpm -Uvh webmin-1.930-1.noarch.rpm

firewall-cmd --permanent --zone=public --add-port=10000/tcp
firewall-cmd --reload
```
安装完直接启动,访问 https://127.0.0.1:10000 注意,带 HTTPS

默认账号 root,密码与服务器一致

**修改密码**

```bash
/usr/libexec/webmin/changepass.pl /etc/webmin/ root 1234qwer
```

---

# 系统监控
## Zabbix

**官网**
- https://www.zabbix.com/

**安装依赖**
```bash
yum install mysql
yum install httpd
yum install php
yum install php-mysqlnd php-gd libjpeg* php-snmp php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-bcmath php-mhash php-common php-ctype php-xml php-xmlreader php-xmlwriter php-session php-mbstring php-gettext php-ldap php-mysqli --skip-broken
yum install wget telnet net-tools python-paramiko gcc gcc-c++ dejavu-sans-fonts python-setuptools python-devel sendmail mailx net-snmp net-snmp-devel net-snmp-utils freetype-devel libpng-devel perl unbound libtasn1-devel p11-kit-devel OpenIPMI unixODBC
```

**设置 mysql**
```vim
vim /etc/my.cnf

innodb_file_per_table = 1
innodb_status_file = 1
innodb_buffer_pool_size = 6G
innodb_flush_log_at_trx_commit = 2
innodb_log_buffer_size = 16M
innodb_log_file_size = 64M
innodb_support_xa = 0
default-storage-engine = innodb
bulk_insert_buffer_size = 8M
join_buffer_size = 16M
max_heap_table_size = 32M
tmp_table_size = 32M
max_tmp_tables = 48
read_buffer_size = 32M
read_rnd_buffer_size = 16M
key_buffer_size = 32M
thread_cache_size = 32
innodb_thread_concurrency = 8
innodb_flush_method = O_DIRECT
innodb_rollback_on_timeout = 1
query_cache_size = 16M
query_cache_limit = 16M
collation_server = utf8_bin
character_set_server = utf8
```
原则上 innodb_buffer_pool_size 需要设置为主机内存的 80%,如果主机内存不是 8GB,以上参数可依据相应比例进行调整,例如主机内存为 16GB,则 innodb_buffer_pool_size 建议设置为 12GB,innodb_log_buffer_size 建议设置为 32M,innodb_log_file_size 建议设置为 128M,以此类推.请注意 innodb_buffer_pool_size 的值必须是整数,例如主机内存是4G,那么 innodb_buffer_pool_size 可以设置为 3G,而不能设置为 3.2G
```bash
systemctl enable mysqld && systemctl start mysqld
grep 'temporary password' /var/log/mysqld.log # 获取 MySQL 的 root 初始密码
mysql_secure_installation # 初始化,改下密码
systemctl restart mysqld
mysql -u root -p
  create database zabbix character set utf8;
  exit;
mysql_upgrade -u root -p
mysql -u root -p
  create user zabbix@'%' identified by '{mysql_zabbix_password}';
  grant all privileges on zabbix.* to zabbix@'%';
  flush privileges;
  exit;
```

**安装 zabbix**
```bash
rpm -ivh https://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm
yum -y install zabbix-server-mysql zabbix-web-mysql zabbix-java-gateway zabbix-web
cd /usr/share/doc/zabbix-server-mysql-4.2.1
zcat create.sql.gz | mysql -uroot zabbix -p
```

- 配置 zabbix 参数
  ```vim
  vim /etc/zabbix/zabbix_server.conf

  DBPassword={mysql_zabbix_password}
  CacheSize=512M
  HistoryCacheSize=128M
  HistoryIndexCacheSize=128M
  TrendCacheSize=128M
  ValueCacheSize=256M
  Timeout=30
  ```
  如果需要监控 VMware 虚拟机,则还需要设置以下选项参数：
  ```vim
  StartVMwareCollectors=2
  VMwareCacheSize=256M
  VMwareTimeout=300
  ```

**配置 Apache 中的 PHP 参数**
```vim
vim /etc/httpd/conf.d/zabbix.conf

php_value max_execution_time 600
php_value memory_limit 256M
php_value post_max_size 32M
php_value upload_max_filesize 32M
php_value max_input_time 600
php_value always_populate_raw_post_data -1
date.timezone Asia/Shanghai
```

**配置 PHP 参数**
```vim
vim /etc/php.ini

php_value post_max_size 32M
max_execution_time 300
max_input_time 300
date.timezone Asia/Shanghai
```

**重启&起服务**
```bash
systemctl stop mysqld && reboot
systemctl start httpd && systemctl start zabbix-server
systemctl stop firewalld
setenforce 0  # 关闭 selinux
```
访问 `http://{ip地址}/zabbix/setup.php`

**Reference**
- [CentOS 7安装Zabbix 3.4](https://www.centos.bz/2017/11/centos-7%E5%AE%89%E8%A3%85zabbix-3-4/)

---

# 虚拟化
## Docker

**官网**
- https://www.docker.com

**centos 下安装**
```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
wget -O /etc/yum.repos.d/docker-ce.repo https://download.docker.com/linux/centos/docker-ce.repo
sed -i 's+download.docker.com+mirrors.tuna.tsinghua.edu.cn/docker-ce+' /etc/yum.repos.d/docker-ce.repo
yum makecache fast
yum install -y docker
```

or

`curl -sSL https://get.docker.com/ | sh`

or

Step 1 — Install Docker
```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce
sudo usermod -aG docker $(whoami)
sudo systemctl enable docker.service
sudo systemctl start docker.service
```

Step 2 — Install Docker Compose
```bash
sudo yum install epel-release
sudo yum install -y python-pip
sudo pip install docker-compose
sudo yum upgrade python*
docker-compose version

docker login
```

**debian 下安装**
```bash
sudo apt update
sudo apt install docker.io
docker login	# 讲道理,按官方文档说法并不需要账户并且登录,但有时候还是需要你登陆
```

**使用**

默认情况下,只有管理员权限能够运行 docker 命令.考虑到安全问题,你不会想用 root 用户或使用 sudo 来运行 Docker 的.要解决这个问题,你需要将自己的用户加入到 docker 组中.

`sudo usermod -a -G docker $USER`

完成操作后,登出系统然后再重新登录,应该就搞定了.不过若你的平台是 Fedora,则添加用户到 docker 组时会发现这个组是不存在的.那该怎么办呢？你需要首先创建这个组.命令如下：
```bash
sudo groupadd docker && sudo gpasswd -a ${USER} docker && sudo systemctl restart docker
newgrp docker
```

启动,暂停以及启用 Docker
```
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl stop docker
sudo systemctl restart docker
```

拉取镜像
```bash
docker images # 检查一下系统中已经有了哪些镜像
docker pull nginx # 拉取一个镜像
docker search nginx # 搜索 Docker Hub 中的所有 Nginx 镜像
docker pull jwilder/nginx-proxy # 从非官方源拉取镜像
```

**加速**
- [Docker 镜像加速](../../Misc/Plan/Misc-Plan.md#Docker)

---

# CI
## Jenkins

**官网**
- https://jenkins.io/

`注,Jenkins 需要 jdk 环境,请先行安装`

**rpm 包方式安装**

添加 Jenkins 源:
```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo http://jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key
```

使用 yum 命令安装 Jenkins:

`yum install jenkins`

**使用 ppa/源方式安装**
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -

sed -i "1ideb https://pkg.jenkins.io/debian binary/" /etc/apt/sources.list

sudo apt-get update
sudo apt-get install jenkins
```

安装后默认服务是启动的,默认是 8080 端口,在浏览器输入:http://127.0.0.1:8080/即可打开主页

查看密码

`cat /var/lib/jenkins/secrets/initialAdminPassword`

---

# 堡垒机
## Jumpserver

**官网**
- http://www.jumpserver.org/

**安装**

[官方文档](http://docs.jumpserver.org/zh/docs/setup_by_centos.html) 写的很详细了,在此我只记录重点

`注:鉴于国内环境,下面步骤运行中还是会出现 docker pull 镜像超时的问题,你懂的,不要问我怎么解决`

```bash
echo -e "\033[31m 1. 防火墙 Selinux 设置 \033[0m" \
  && if [ "$(systemctl status firewalld | grep running)" != "" ]; then firewall-cmd --zone=public --add-port=80/tcp --permanent; firewall-cmd --zone=public --add-port=2222/tcp --permanent; firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="172.17.0.0/16" port protocol="tcp" port="8080" accept"; firewall-cmd --reload; fi \
  && if [ "$(getenforce)" != "Disabled" ]; then setsebool -P httpd_can_network_connect 1; fi
```
```bash
echo -e "\033[31m 2. 部署环境 \033[0m" \
  && yum update -y \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
  && yum -y install kde-l10n-Chinese \
  && localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8 \
  && export LC_ALL=zh_CN.UTF-8 \
  && echo 'LANG="zh_CN.UTF-8"' > /etc/locale.conf \
  && yum -y install wget gcc epel-release git \
  && yum install -y yum-utils device-mapper-persistent-data lvm2 \
  && yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo \
  && yum makecache fast \
  && rpm --import https://mirrors.aliyun.com/docker-ce/linux/centos/gpg \
  && echo -e "[nginx-stable]\nname=nginx stable repo\nbaseurl=http://nginx.org/packages/centos/\$releasever/\$basearch/\ngpgcheck=1\nenabled=1\ngpgkey=https://nginx.org/keys/nginx_signing.key" > /etc/yum.repos.d/nginx.repo \
  && rpm --import https://nginx.org/keys/nginx_signing.key \
  && yum -y install redis mariadb mariadb-devel mariadb-server nginx docker-ce \
  && systemctl enable redis mariadb nginx docker \
  && systemctl start redis mariadb \
  && yum -y install python36 python36-devel \
  && python3.6 -m venv /opt/py3
```
```bash
echo -e "\033[31m 3. 下载组件 \033[0m" \
  && cd /opt \
  && if [ ! -d "/opt/jumpserver" ]; then git clone --depth=1 https://github.com/jumpserver/jumpserver.git; fi \
  && if [ ! -f "/opt/luna.tar.gz" ]; then wget https://demo.jumpserver.org/download/luna/1.4.9/luna.tar.gz; tar xf luna.tar.gz; chown -R root:root luna; fi \
  && yum -y install $(cat /opt/jumpserver/requirements/rpm_requirements.txt) \
  && source /opt/py3/bin/activate \
  && pip install --upgrade pip setuptools -i https://mirrors.aliyun.com/pypi/simple/ \
  && pip install -r /opt/jumpserver/requirements/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
  && curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io \
  && systemctl restart docker \
  && docker pull jumpserver/jms_coco:1.4.9 \
  && docker pull jumpserver/jms_guacamole:1.4.9 \
  && rm -rf /etc/nginx/conf.d/default.conf \
  && curl -o /etc/nginx/conf.d/jumpserver.conf https://demo.jumpserver.org/download/nginx/conf.d/jumpserver.conf
```
```bash
echo -e "\033[31m 4. 处理配置文件 \033[0m" \
  && if [ "$DB_PASSWORD" = "" ]; then DB_PASSWORD=`cat /dev/urandom | tr -dc A-Za-z0-9 | head -c 24`; fi \
  && if [ "$SECRET_KEY" = "" ]; then SECRET_KEY=`cat /dev/urandom | tr -dc A-Za-z0-9 | head -c 50`; echo "SECRET_KEY=$SECRET_KEY" >> ~/.bashrc; fi \
  && if [ "$BOOTSTRAP_TOKEN" = "" ]; then BOOTSTRAP_TOKEN=`cat /dev/urandom | tr -dc A-Za-z0-9 | head -c 16`; echo "BOOTSTRAP_TOKEN=$BOOTSTRAP_TOKEN" >> ~/.bashrc; fi \
  && if [ "$Server_IP" = "" ]; then Server_IP=`ip addr | grep inet | egrep -v '(127.0.0.1|inet6|docker)' | awk '{print $2}' | tr -d "addr:" | head -n 1 | cut -d / -f1`; fi \
  && if [ ! -d "/var/lib/mysql/jumpserver" ]; then mysql -uroot -e "create database jumpserver default charset 'utf8';grant all on jumpserver.* to 'jumpserver'@'127.0.0.1' identified by '$DB_PASSWORD';flush privileges;"; fi \
  && if [ ! -f "/opt/jumpserver/config.yml" ]; then cp /opt/jumpserver/config_example.yml /opt/jumpserver/config.yml; sed -i "s/SECRET_KEY:/SECRET_KEY: $SECRET_KEY/g" /opt/jumpserver/config.yml; sed -i "s/BOOTSTRAP_TOKEN:/BOOTSTRAP_TOKEN: $BOOTSTRAP_TOKEN/g" /opt/jumpserver/config.yml; sed -i "s/# DEBUG: true/DEBUG: false/g" /opt/jumpserver/config.yml; sed -i "s/# LOG_LEVEL: DEBUG/LOG_LEVEL: ERROR/g" /opt/jumpserver/config.yml; sed -i "s/# SESSION_EXPIRE_AT_BROWSER_CLOSE: false/SESSION_EXPIRE_AT_BROWSER_CLOSE: true/g" /opt/jumpserver/config.yml; sed -i "s/DB_PASSWORD: /DB_PASSWORD: $DB_PASSWORD/g" /opt/jumpserver/config.yml; fi
```
```bash
echo -e "\033[31m 5. 启动 Jumpserver \033[0m" \
  && systemctl start nginx \
  && cd /opt/jumpserver \
  && ./jms start all -d \
  && docker run --name jms_coco -d -p 2222:2222 -p 5000:5000 -e CORE_HOST=http://$Server_IP:8080 -e BOOTSTRAP_TOKEN=$BOOTSTRAP_TOKEN jumpserver/jms_coco:1.4.9 \
  && docker run --name jms_guacamole -d -p 8081:8081 -e JUMPSERVER_SERVER=http://$Server_IP:8080 -e BOOTSTRAP_TOKEN=$BOOTSTRAP_TOKEN jumpserver/jms_guacamole:1.4.9 \
  && echo -e "\033[31m 你的数据库密码是 $DB_PASSWORD \033[0m" \
  && echo -e "\033[31m 你的SECRET_KEY是 $SECRET_KEY \033[0m" \
  && echo -e "\033[31m 你的BOOTSTRAP_TOKEN是 $BOOTSTRAP_TOKEN \033[0m" \
  && echo -e "\033[31m 你的服务器IP是 $Server_IP \033[0m" \
  && echo -e "\033[31m 请打开浏览器访问 http://$Server_IP 用户名:admin 密码:admin \033[0m"
```

---

# 安全服务
## ClamAV

**官网**
- https://www.clamav.net

`本部分来自 https://blog.51cto.com/11199460/2083697,在此仅作排版调整`

**安装**
```bash
yum -y install epel-release
yum -y install clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd

# 在两个配置文件 /etc/freshclam.conf 和 /etc/clamd.d/scan.conf 中移除“Example”字符
cp /etc/freshclam.conf /etc/freshclam.conf.bak
sed -i -e "s/^Example/#Example/" /etc/freshclam.conf

cp /etc/clamd.d/scan.conf /etc/clamd.d/scan.conf.bak
sed -i -e "s/^Example/#Example/" /etc/clamd.d/scan.conf
```

**病毒库操作**

关闭自动更新
freshclam 命令通过文件 /etc/cron.d/clamav-update 来自动运行
```vim
vim /etc/cron.d/clamav-update
```

但默认情况下是禁止了自动更新功能,需要移除文件 /etc/sysconfig/freshclam 最后一行的配置才能启用
```vim
vim /etc/cron.d/clamav-update

# FRESHCLAM_DELAY=
```

定义服务器类型 (本地或者 TCP) ,在这里定义为使用本地 socket,将文件 /etc/clam.d/scan.conf 中的这一行前面的注释符号去掉：
```vim
vim /etc/clamd.d/scan.conf

LocalSocket /var/run/clamd.scan/clamd.sock
```

下载病毒库 https://www.clamav.net/downloads 将 main.cvd\daily.cvd\bytecode.cvd 三个文件下载后上传到 /var/lib/clamav 目录下
```vim
vim /etc/freshclam.conf

DatabaseDirectory /var/lib/clamav
```
```bash
systemctl enable clamd@scan.service
ln -s '/usr/lib/systemd/system/clamd@scan.service' '/etc/systemd/system/multi-user.target.wants/clamd@scan.service'
```

更新病毒库
```bash
vim /usr/lib/systemd/system/clam-freshclam.service

# Run the freshclam as daemon
[Unit]
Description = freshclam scanner
After = network.target

[Service]
Type = forking
ExecStart = /usr/bin/freshclam -d -c 4
Restart = on-failure
PrivateTmp = true

[Install]
WantedBy=multi-user.target
```
```bash
systemctl start clam-freshclam.service
systemctl status clam-freshclam.service
freshclam
systemctl enable clam-freshclam.service
cp /usr/share/clamav/template/clamd.conf /etc/clamd.conf
```
```vim
vim /etc/clamd.conf

TCPSocket 3310
TCPAddr 127.0.0.1
```
```bash
/usr/sbin/clamd restart
clamdscan -V

systemctl start clamd@scan.service
systemctl status clamd@scan.service
```

查杀病毒
```bash
clamscan -r /home # 扫描所有用户的主目录就使用
clamscan -r --bell -i / # 扫描所有文件并且显示有问题的文件的扫描结果
clamscan -r --remove  # 查杀当前目录并删除感染的文件
```

---

## Fail2ban

- https://github.com/fail2ban/fail2ban

`本部分来自 https://linux.cn/article-5067-1.html,在此仅作排版调整`

**安装**

RHEL: `yum install fail2ban`

Debian: `apt install fail2ban`

**编辑配置文件**
```vim
vim /etc/fail2ban/jail.conf

[DEFAULT]
# 以空格分隔的列表,可以是 IP 地址、CIDR 前缀或者 DNS 主机名
# 用于指定哪些地址可以忽略 fail2ban 防御
ignoreip = 127.0.0.1 172.31.0.0/24 10.10.0.0/24 192.168.0.0/24

# 客户端主机被禁止的时长 (秒) ,-1代表永远
bantime = 10m

# 客户端主机被禁止前允许失败的次数
maxretry = 5

# 间隔时间 (秒) ,间隔时间内超过最大尝试次数即被封锁
findtime = 10m

mta = sendmail

[ssh-iptables]
enabled = true
filter = sshd
action = iptables[name=SSH, port=ssh, protocol=tcp]
sendmail-whois[name=SSH, dest=your@email.com, sender=fail2ban@email.com]
# Debian 系的发行版
logpath = /var/log/auth.log
# Red Hat 系的发行版
logpath = /var/log/secure
# ssh 服务的最大尝试次数
maxretry = 3
```

根据上述配置,fail2ban 会自动禁止在最近 10 分钟内有超过 3 次访问尝试失败的任意 IP 地址.一旦被禁,这个 IP 地址将会在 24 小时内一直被禁止访问 SSH 服务.这个事件也会通过 sendemail 发送邮件通知.

**测试**
```bash
service fail2ban restart

# 为了验证 fail2ban 成功运行,使用参数'ping'来运行 fail2ban-client 命令. 如果 fail2ban 服务正常运行,你可以看到“pong (嘭) ”作为响应.
fail2ban-client ping
```

为了测试 fail2ban 是否能正常工作,尝试通过使用错误的密码来用 SSH 连接到服务器模拟一个暴力破解攻击.与此同时,监控 `/var/log/fail2ban.log` ,该文件记录在 fail2ban 中发生的任何敏感事件.

```bash
tail -f /var/log/fail2ban.log
2019-07-24 23:33:34,369 fail2ban.jail           [14760]: INFO    Initiated 'pyinotify' backend
2019-07-24 23:33:34,370 fail2ban.filter         [14760]: INFO      maxLines: 1
2019-07-24 23:33:34,372 fail2ban.server         [14760]: INFO    Jail ssh-iptables is not a JournalFilter instance
2019-07-24 23:33:34,373 fail2ban.filter         [14760]: INFO    Added logfile: '/var/log/auth.log' (pos = 0, hash = de62b1aacfb0f9a9082c515fe3cdb77214101d93)
2019-07-24 23:33:34,377 fail2ban.filter         [14760]: INFO      encoding: UTF-8
2019-07-24 23:33:34,378 fail2ban.filter         [14760]: INFO      maxRetry: 3
2019-07-24 23:33:34,378 fail2ban.filter         [14760]: INFO      findtime: 600
2019-07-24 23:33:34,378 fail2ban.actions        [14760]: INFO      banTime: 600
2019-07-24 23:33:34,381 fail2ban.jail           [14760]: INFO    Jail 'sshd' started
2019-07-24 23:33:34,382 fail2ban.jail           [14760]: INFO    Jail 'ssh-iptables' started
2019-07-24 23:35:58,780 fail2ban.filter         [14760]: INFO    [ssh-iptables] Found 192.168.72.130 - 2019-07-24 23:35:58
2019-07-24 23:36:00,397 fail2ban.filter         [14760]: INFO    [ssh-iptables] Found 192.168.72.130 - 2019-07-24 23:36:00
2019-07-24 23:36:03,811 fail2ban.filter         [14760]: INFO    [sshd] Found 192.168.72.130 - 2019-07-24 23:35:58
2019-07-24 23:36:03,812 fail2ban.filter         [14760]: INFO    [sshd] Found 192.168.72.130 - 2019-07-24 23:36:00
2019-07-24 23:36:04,266 fail2ban.filter         [14760]: INFO    [sshd] Found 192.168.72.130 - 2019-07-24 23:36:04
2019-07-24 23:36:04,310 fail2ban.filter         [14760]: INFO    [ssh-iptables] Found 192.168.72.130 - 2019-07-24 23:36:04
2019-07-24 23:36:04,778 fail2ban.actions        [14760]: NOTICE  [ssh-iptables] Ban 192.168.72.130
```

根据上述的日志文件,Fail2ban 通过检测 IP 地址的多次失败登录尝试,禁止了一个 IP 地址 192.168.72.130

**解禁 IP**

由于 fail2ban 的“ssh-iptables”监狱使用 iptables 来阻塞问题 IP 地址,你可以通过以下方式来检测当前 iptables 来验证禁止规则.
```bash
iptables --list -n
iptables -D fail2ban-SSH -s 192.168.72.130 -j DROP
```
当然你可以使用上述的 iptables 命令手动地检验和管理 fail2ban 的 IP 阻塞列表,但实际上有一个适当的方法就是使用 fail2ban-client 命令行工具.这个命令不仅允许你对"ssh-iptables"监狱进行管理,同时也是一个标准的命令行接口,可以管理其他类型的 fail2ban 监狱.
```bash
fail2ban-client status  # 检验 fail2ban 状态

fail2ban-client status ssh-iptables # 检验一个特定监狱的状态

fail2ban-client set ssh-iptables unbanip 192.168.72.130 # 解锁特定的IP地址
```
注意,如果你停止了 Fail2ban 服务,那么所有的 IP 地址都会被解锁.当你重启 Fail2ban,它会从 /etc/log/secure(或 /var/log/auth.log)中找到异常的 IP 地址列表,如果这些异常地址的发生时间仍然在禁止时间内,那么 Fail2ban 会重新将这些 IP 地址禁止.

---

# 仓库
## Nexus

**官网**
- https://www.sonatype.com/nexus-repository-oss

**安装**
- **JDK**
    ```bash
    tar xzf jdk-8u212-linux-x64.tar.gz
    ```
    ```vim
    vim /etc/profile

    export JAVA_HOME=/root/jdk1.8.0_212
    export PATH=$PATH:$JAVA_HOME/bin
    ```
    ```bash
    source /etc/profile
    java -version
    ```

- **Maven**
    ```bash
    tar xzf apache-maven-3.6.2-bin.tar.gz
    ```
    ```vim
    vim /etc/profile

    export MAVEN_HOME=/root/apache-maven-3.6.2
    export PATH=$PATH:$MAVEN_HOME/bin
    ```
    ```bash
    source /etc/profile
    mvn -version
    ```

- **Nexus**
    - 在官网下载 UNIX 安装包,上传至服务器,这里以 https://help.sonatype.com/repomanager2/download#Download-NexusRepositoryManager2OSS 2.14.14-01 为例

    ```bash
    tar -xf nexus-2.14.14-01-bundle.tar.gz -C /usr/local
    cd /usr/local/nexus-2.14.14-01/bin/
    export RUN_AS_USER=root

    ./nexus start
    firewall-cmd --add-port=8081/tcp --permanent
    firewall-cmd --reload
    ```
    ```bash
    curl http://127.0.0.1:8081/nexus/
    ```
    默认登录账号/密码为： admin/admin123

---

`"朋友的疏远大致分为两种.天各一方的两个人,慢慢的失掉了联系,彼此不再知道近况,多年之后再聚首往往就只是相对无言了.另一种就令人唏嘘的多了,两个朝夕得见的人,彼此的境遇竟因着造化相去渐远,这时心里也许会慢慢生出一种无力感来,因为无论怎么说怎么做也只能感觉心的距离越来越远了.——吴念真《这些人,那些事》`
