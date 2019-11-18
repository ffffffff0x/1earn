```
  ████████                              ██       ██       ██
 ██░░░░░░  ██████                      ░██      ░██      ░░
░██       ░██░░░██  █████   █████      ░██      ░██       ██ ███████  ██   ██ ██   ██
░█████████░██  ░██ ██░░░██ ██░░░██  ██████ █████░██      ░██░░██░░░██░██  ░██░░██ ██
░░░░░░░░██░██████ ░███████░███████ ██░░░██░░░░░ ░██      ░██ ░██  ░██░██  ░██ ░░███
       ░██░██░░░  ░██░░░░ ░██░░░░ ░██  ░██      ░██      ░██ ░██  ░██░██  ░██  ██░██
 ████████ ░██     ░░██████░░██████░░██████      ░████████░██ ███  ░██░░██████ ██ ░░██
░░░░░░░░  ░░       ░░░░░░  ░░░░░░  ░░░░░░       ░░░░░░░░ ░░ ░░░   ░░  ░░░░░░ ░░   ░░
```

`基础 Linux 命令、操作指南`

<p align="center">
    <a href="https://en.wikipedia.org/wiki/Pablo_Picasso"><img src="../../../assets/img/运维/Linux/Speed-Linux.jpg"></a>
</p>

---

## 大纲

`注: 未对 gitbook 页面链接跳转进行优化,见谅`

**👍Shell-Base**

* [环境变量](#环境变量)
* [通配符-限制输出](#通配符-限制输出)
* [会话](#会话)
* [目录](#目录)
* [会话](#会话)
* [文件](#文件)
	* [压缩备份](#压缩备份)
	* [读写](#读写)
		* [增](#增)
		* [删](#删)
		* [查](#查)
		* [改](#改)

**📶网络管理**

* [配置](#配置)
* [查看](#查看)
* [抓包](#抓包)
* [传输-下载](#传输-下载)
	* [bt](#bt)
* [Firewall](#Firewall)
	* [Firewalld](#Firewalld)
	* [Iptables](#Iptables)
* [软件包管理](#软件包管理)
	* [源](#源)
	* [Binary](#Binary)
	* [dpkg](#dpkg)
	* [Pacman](#Pacman)
	* [rpm](#rpm)
	* [yum](#yum)
	* [apt](#apt)
	* [常用软件](#常用软件)

**🦋系统管理**

* [系统设置](#系统设置)
	* [时间](#时间)
	* [语言](#语言)
	* [启动项-计划任务](#启动项-计划任务)
	* [账号管控](#账号管控)
* [系统信息](#系统信息)
	* [进程管理](#进程管理)

**🛠设备管理**

* [硬盘-数据](#硬盘-数据)

**🚬Linux 编程**

* [编译](#编译)

---

# 👍Shell-Base
## 环境变量

- **bash**
	```bash
	echo $PATH  # 查看环境变量

	PATH=$PATH:/usr/local/python3/bin/ # 新添加的路径(关闭终端失效)
	```
	```vim
	vim ~/.bash_profile # 永久修改变量

	PATH=$PATH:/usr/local/bin/
	```
	`source ~/.bash_profile` 立即生效

- **fish**
	```vim
	vim ~/.config/fish/config.fish

	set PATH (你想要加入的路径) $PATH
	```
	`souce ~/.config/fish/config.fish`

- 图形模式登录时,顺序读取：`/etc/profile` 和 `~/.profile`
- 图形模式登录后,打开终端时,顺序读取：`/etc/bash.bashrc` 和 `~/.bashrc`
- 文本模式登录时,顺序读取：`/etc/bash.bashrc`,`/etc/profile` 和 `~/.bash_profile`

---

## 通配符-限制输出
```bash
head	# 显示文件的开头的内容.默认下,显示文件的头10行内容.
tail	# 显示文件中的尾部内容.默认下,显示文件的末尾10行内容.
<
>
grep	# 文本搜索工具,它能使用正则表达式搜索文本,并把匹配的行打印出来.
sort	# 将文件进行排序,并将排序结果标准输出.
uniq	# 用于报告或忽略文件中的重复行
awk
&
```

---

## 会话
```bash
who	# 显示目前登录系统的用户信息.
w	# 显示已经登陆系统的用户列表,并显示用户正在执行的指令.
last	# 显示用户最近登录信息
```
```bash
screen	# 会话管理软件
	yum -y install screen
	apt-get -y install screen
	screen -S <name>
	screen -ls
	screen -r <name>	# 重新连接
	ctrl+d	# 终止会话
```

---

## 目录
```bash
cd	# 切换工作目录
~	# 表示 home 目录
.	# 表示当前目录
..	# 表示上级目录
-	# 表示上一次目录

/	# 表示根目录
	root	# 超级用户目录,存放 root 用户相关文件
	home	# 存放普通用户相关文件
	bin	# (binaries)存放二进制可执行文件
	sbin	# (super user binaries)存放二进制可执行文件,只有root才能访问
	mnt	# (mount)系统管理员安装临时文件系统的安装点
	etc	# (etcetera)存放系统配置文件
	var	# (variable)用于存放运行时需要改变数据的文件
	boot	# 存放用于系统引导时使用的各种文件
	usr	# (unix shared resources)用于存放共享的系统资源
	dev	# (devices)用于存放设备文件
	lib	# (library)存放跟文件系统中的程序运行所需要的共享库及内核模块
	tmp	# (temporary)用于存放各种临时文件
```

---

## 文件
### 压缩备份
```bash
.tar	# 注:tar 是打包,不是压缩！
tar -xvf FileName.tar	# 解包
tar -cvf FileName.tar DirName	# 打包
tar -tvf FileName.tar.gz	# 不解压查看内容
tar -xvf FileName.tar.gz	a.txt  # 解压指定内容
tar -uvf test.tar.bz2 test	# 更新一个内容
tar -rvf test.tar.bz2 test2  # 追加一个内容

.tar.gz 和 .tgz
tar -zxvf FileName.tar.gz	# 解压
tar -zcvf FileName.tar.gz DirName	# 压缩

.tar.Z
tar -Zxvf FileName.tar.Z	# 解压
tar -Zcvf FileName.tar.Z DirName	# 压缩

.tar.bz
tar -jxvf FileName.tar.bz	# 解压
tar -jcvf FileName.tar.bz DirName	# 压缩

.gz
gunzip FileName.gz	# 解压1
gzip -dv FileName.gz	# 解压2
gzip FileName	# 压缩
gzip -l FileName.gz # 不解压查看内容
zcat FileName.gz # 不解压查看内容

.bz2
bzip2 -dv FileName.bz2	# 解压1
bunzip2 FileName.bz2	# 解压2
bzip2 -zv FileName	# 压缩
bzcat	FileName.bz2 # 不解压查看内容

.Z
uncompress FileName.Z	# 解压
compress FileName	# 压缩
compress -rvf /home/abc/	# 强制压缩文件夹

.zip
unzip FileName.zip	# 解压
zip FileName.zip DirName	# 压缩

.rar
rar x FileName.rar	# 解压
rar a FileName.rar DirName	# 压缩

.lha
lha -e FileName.lha	# 解压
lha -a FileName.lha FileName	# 压缩

.rpm
rpm2cpio FileName.rpm | cpio -div	# 解包

.deb
ar -p FileName.deb data.tar.gz | tar zxf -	# 解包
```

### 读写
#### 增
```bash
touch -r test1.txt test2.txt # 更新 test2.txt 时间戳与 test1.txt 时间戳相同
touch -c -t 202510191820 a.txt # 更改时间
truncate -s 100k aaa.txt 	 # 创建指定大小文件

mkdir -p /mnt/aaa/aaa/aaa 	# 创建指定路径一系列文件夹
mkdir -m 777 /test	# 创建时指定权限
```

#### 删
```bash
rm -i	# 确认
rmdir	# 删除空目录

# 删除巨大文件小 tips
	echo "" >  bigfile
	rm bigfile

	> access.log	# 通过重定向到 Null 来清空文件内容
	: > access.log
	true > access.log
	cat /dev/null > access.log
```

#### 查
**查看**
```bash
pwd -P	# 目录链接时,显示实际路径而非 link 路径
ls	# 第一个字符 -表示文件,d目录,l链接,b接口设备,c串口设备
ls -a	# 查看隐藏文件
tac	# 倒着读
od	# 二进制读
cat -n	# 带行号读
cat -b	# 带行号,越过空白行
less	# 允许用户向前或向后浏览文件
more +10 a.txt	# 从第10行读起
more -10 f1.txt	# 每次显示10行读取文件
head -n 1 文件名	# 读文件第一行
head -5 /etc/passwd	# 读取文件前5行
tail -10 /etc/passwd	# 读取文件后10行
sed -n '5,10p' /etc/passwd	# 读取文件第5-10行
du	# 文件大小
stat	# 文件属性
file	# 文件类型
id	# 显示真实有效的用户ID(UID)和组ID(GID)
```

**查找**
```bash
fd	# 文件查找工具
	wget https://github.com/sharkdp/fd/releases/download/v7.3.0/fd-musl_7.3.0_amd64.deb
	dpkg -i fd-musl_7.3.0_amd64.deb
	fd <文件>

find / -name conf*	# 快速查找根目录及子目录下所有 conf 文件
locate <文件>	# 查找文件或目录

which <命令>	# 查找并显示给定命令的绝对路径
```

#### 改
```bash
cp <源文件> <目标文件/目标路径>	# 复制
	cp -r <源目录> <目标目录/目标路径> # 带目录复制

mv <源文件> <目标文件/目标路径>	# 对文件或目录重命名,或移动

vi 	# 编辑器
nano	# 编辑器
gedit	# 图形化的编辑器
```

**Vim**

- **常用操作**
	```
	Normal 模式下 i 进入 insert 模式
	:wq 存盘+退出
	dd 删除当前行,并存入剪切板
	p 粘贴
	:q！强制退出
	:wq！强制保存退出
	:w !sudo tee %  无 root 权限,保存编辑的文件
	:saveas <path/to/file> 另存为
	按下 / 即可进入查找模式,输入要查找的字符串并按下回车. Vim 会跳转到第一个匹配.按下 n 查找下一个,按下 N 查找上一个.
	:%s/foo/bar 代表替换 foo 为 bar
	insert 模式按 ESC 键,返回 Normal 模式
	```

- **更多操作**
	- [Vim](./Power-Linux.md#Vim)

---

# 📶网络管理
## 配置
**Ubuntu**
```vim
vim /etc/network/interfaces

auto enp7s0	 # 使用的网络接口
iface enp7s0 inet static	# 静态 ip 设置
address 10.0.208.222
netmask 255.255.240.0
gateway 10.0.208.1
dns-nameservers 10.0.208.1
```
```bash
iface enp7s0 inet dhcp	# dhcp 配置
```
```bash
sudo ip addr flush enp7s0
sudo systemctl restart networking.service

systemctl restart NetworkManager
systemctl enable NetworkManager
```

- **修改 DNS**

	方法一
	```vim
	vim /etc/network/interfaces

	dns-nameservers 8.8.8.8
	```
	重启后DNS就生效了,这时候再看/etc/resolv.conf,最下面就多了一行

	方法二
	```vim
	vim /etc/resolv.conf

	nameserver 8.8.8.8
	```
	```bash
	chattr +i /etc/resolv.conf	# 限制用户(包括 root)删除、修改、增加、链接等操作.要修改的话要先删掉这个设置 chattr -i /etc/resolv.conf
	service network restart
	```

**Centos**
```vim
vim /etc/sysconfig/network-scripts/ifcfg-eth0	# 是不是 eth0 要看自己的网卡,使用 ip a

HOSTNAME=test
onboot=yes
HWADDR=00:0C:29:F1:2E:7B
BOOTPROTO=static	# 使用静态 IP,而不是由 DHCP 分配 IP
# BOOTPROTO=dhcp 这个是 DHCP 的配置,如果配这个那下面的就不需要配置了
IPADDR=172.16.102.61
PREFIX=24
GATEWAY=172.16.102.254
DNS1=223.5.5.5
```
```vim
vim /etc/hosts

127.0.0.1  test localhost	# 修改 localhost.localdomain 为 test,shutdown -r now 重启使修改生效
```
```bash
service network restart
systemctl restart NetworkManager	# 重启网络管理
systemctl enable NetworkManager
```

- **修改 DNS**
	```vim
	vim /etc/resolv.conf

	nameserver 8.8.8.8
	```
	```bash
	chattr +i /etc/resolv.conf	# 限制用户(包括 root)删除、修改、增加、链接等操作.要修改的话要先删掉这个设置 chattr -i /etc/resolv.conf
	service network restart
	```

**Arch**
```bash
ifconfig eth0 up	# 启动网卡
dhcpcd  eth0	# 获取 ip
```
`ifconfig -a` 查看下可用的网卡
```vim
vim /etc/rc.conf

interface=eth0
eth0="dhcp"
lo="lo 127.0.0.1"
eth0="eth0 192.168.0.2 netmask 255.255.255.0 broadcast 192.168.0.255"

INTERFACES=(eth0)
gateway="default gw 192.168.0.1"
ROUTES=(gateway)
```
`/etc/rc.d/network restart`

---

## 查看
**IP**
```bash
ifconfig
ip a	# 显示网络设备的运行状态
ip route	# 显示核心路由表
ip neigh	# 显示邻居表
```

**端口**
```bash
getent services # 查看所有服务的默认端口名称和端口号
ss -tnlp
```

**路由表**
```bash
route
ip r
```

---

## 抓包
**tcpdump**
```bash
# 安装
apt install tcpdump -y
yum install tcpdump -y

# 当我们在没用任何选项的情况下运行 tcpdump 命令时,它将捕获所有接口上的数据包
tcpdump -i {接口名}	# 指定接口

# 假设我们想从特定接口(如 enp0s3)捕获 12 个数据包
tcpdump -i enp0s3 -c 12

# 使用 -D 选项显示 tcpdump 命令的所有可用接口
tcpdump -D

# 默认情况下,在 tcpdump 命令输出中,不显示可读性好的时间戳,如果您想将可读性好的时间戳与每个捕获的数据包相关联,那么使用 -tttt 选项,示例如下所示
tcpdump -i enp0s3 -c 12 -tttt

# 使用 tcpdump 命令中的 -w 选项将捕获的 TCP/IP 数据包保存到一个文件中
tcpdump -i enp0s3 -c 12 -tttt -w test.pcap	# 注意：文件扩展名必须为 .pcap

# 捕获并保存大小大于 N 字节的数据包.
tcpdump -i enp0s3 -c 12 -tttt -w test.pcap greater 1024
# 捕获并保存大小小于 N 字节的数据包.
tcpdump -i enp0s3 -c 12 -tttt -w test.pcap less 1024

# 使用选项 -r 从文件中读取这些数据包
tcpdump -r test.pcap -tttt

# 只捕获特定接口上的 IP 地址数据包
tcpdump -i enp0s3 -n

# 使用 tcp 选项来只捕获 TCP 数据包
tcpdump -i enp0s3 tcp

# 从特定接口 enp0s3 上的特定端口(例如 22)捕获数据包
tcpdump -i enp0s3 port 22

# 使用 src 关键字后跟 IP 地址,捕获来自特定来源 IP 的数据包
tcpdump -i enp0s3 -n src 1.1.1.1

# 捕获来自特定目的 IP 的数据包
tcpdump -i enp0s3 -n dst 1.1.1.1

# 假设我想捕获两台主机 169.144.0.1 和 169.144.0.20 之间的 TCP 数据包
tcpdump -w test2.pcap -i enp0s3 tcp and \(host 169.144.0.1 or host 169.144.0.20\)

# 只捕获两台主机之间的 SSH 数据包流
tcpdump -w test3.pcap -i enp0s3 src 169.144.0.1 and port 22 and dst 169.144.0.20 and port 22

# 使用 tcpdump 命令,以 ASCII 和十六进制格式捕获 TCP/IP 数据包
tcpdump -c 10 -A -i enp0s3
```

---

## 传输-下载
**scp**
```bash
scp root@xx.xx.xx.xx:/test/123.txt /test/123.txt	# 文件传输
scp -r # 文件夹传输
```

**lrzsz**
```bash
yum install lrzsz
sz xxx   # 将选定的文件发送(send)到本地机器
rz # 运行该命令会弹出一个文件选择窗口,从本地选择文件上传到服务器(receive),需要远程软件支持
```

**wget**
```bash
wget example.com/big.file.iso	# 下载目标文件
wget --output-document=filename.html example.com	# 另行命名
wget -c example.com/big.file.iso	# 恢复之前的下载
wget --i list.txt	# 下载文件中的 url
wget -r example.com	# 递归下载
wget --no-check-certificate	# 不检查 https 证书
```

### bt
- Transmission
- rtorrent
- **[peerflix](https://github.com/mafintosh/peerflix)**
	```bash
	npm install -g peerflix
	peerflix "magnet:?xt=urn:btih:ef330b39f4801d25b4245212e75a38634bfc856e"
	```
- **[tget](https://github.com/jeffjose/tget)**
	```bash
	npm install -g t-get
	tget 'magnet:?xt=urn:btih:0403fb4728bd788fbcb67e87d6feb241ef38c75a'
	```

---

## Firewall
### Firewalld
```bash
firewall-cmd --zone=public --add-port=12345/tcp --permanent	# 开放端口
firewall-cmd --zone=public --add-service=http --permanent	# 开放服务
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" accept' --permanent	# 允许192.168.1.10所有访问所有端口
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" port port=22 protocol=tcp reject' --permanent	# 拒绝192.168.1.10所有访问TCP协议的22端口

firewall-cmd --reload	# 重新加载
firewall-cmd --list-services	# 查看防火墙设置
systemctl status firewalld	# 查看服务运行状态
systemctl start firewalld	# 开启服务
systemctl stop firewalld	# 关闭服务
```

**更多配置**

见 [Firewall.md](./实验/Firewall.md)

### Iptables
```bash
iptables-save > /root/firewall_rules.backup	# 先备份一下策略
iptables -A OUTPUT -p tcp -d bigmart.com -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j DROP
iptables -A INPUT -p tcp -s 10.0.3.1 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 22 -j DROP

iptables -L	# 查看防火墙规则
iptables-restore </root/firewall_rules.backup	# 规则恢复一下
```

---

## 软件包管理

**update-alternatives**
```bash
# update-alternatives 命令用于处理linux系统中软件版本的切换，在各个linux发行版中均提供了该命令，命令参数略有区别，但大致是一样的。

# 注册软件
	update-alternatives --install <link> <name> <path> <priority>
	update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_91/bin/java 200	# 以jdk为例，安装了jdk以后，先要在update-alternatives工具中注册
	update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_111/bin/java 300

	# 第一个参数 --install 表示注册服务名。
	# 第二个参数是注册最终地址，成功后将会把命令在这个固定的目的地址做真实命令的软链，以后管理就是管理这个软链；
	# 第三个参数：服务名，以后管理时以它为关联依据。
	# 第四个参数，被管理的命令绝对路径。
	# 第五个参数，优先级，数字越大优先级越高。

# 查看已注册列表
	update-alternatives --display java

# 修改命令版本
	update-alternatives --config java
	# 输入数字，选择相应版本
	update-alternatives --auto java	# 按照优先级高自动选择
	update-alternatives --set java /opt/jdk1.8.0_91/bin/java	# 直接指定
```

### 源
**本地 yum 源**

挂载到/mnt/cdrom
```bash
mkdir /mnt/cdrom
mount /dev/cdrom /mnt/cdrom/
```

进入 /etc/yum.repos.d 目录,将其中三个改名或者剩下所有都移走留下 CentOS-Base.repo
```bash
cd /etc/yum.repos.d
rm  CentOS-Media.repo
rm  CentOS-Vault.repo
```

编辑 CentOS-Base.repo
```vim
vim CentOS-Base.repo

baseurl=file:///mnt/cdrom/	# 这里为本地源路径
gpgcheck=0
enabled=1	# 开启本地源
```
`yum list` 看一下包

**Alibaba yum 源**

直接下载源
```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

刷新 YUM 的缓存状态:
```bash
yum clean all
yum makecache
```

**ubuntu 源**
```vim
lsb_release -c	# 查看系统版号

cd /etc/apt/
mv sources.list sources.list.bak
```
```vim
vim sources.list

deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

enable the “Universe” repository
```
sudo add-apt-repository universe
sudo apt-get update
```

**Kali 源**
```vim
vim /etc/apt/sources.list

# 清华源
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free

# 官方源
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib

# 中科大
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

# 浙大
deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free

# 东软大学
deb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
deb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
```
`apt-get update && apt-get upgrade && apt-get dist-upgrade`

**Pacman 源**
```bash
sudo pacman-mirrors -i -c China -m rank # 更新镜像排名
sudo pacman -Syy    # 更新数据源
sudo pacman -S archlinux-keyring
```

### Binary

```bash
yum install make
yum install gcc
yum install gcc-c++
./configure --prefix=/opt	# 配置,表示安装到/opt目录
make	# 编译
make install	# 安装
```

### dpkg

> dpkg 命令是 Debian Linux 系统用来安装、创建和管理软件包的实用工具.
```bash
# deb 是 debian linux的安装格式，跟 red hat 的 rpm 非常相似，最基本的安装命令是：dpkg -i file.deb

dpkg -i xxxxx.deb  # 安装软件
dpkg -R /usr/local/src	# 安装路径下所有包
dpkg -L # 查看软件安装位置
```

### Pacman

> pacman 是 Arch 的包管理工具.
```bash
pacman -S <package>	# 安装或者升级单个软件包
pacman -R <package>	# 删除单个软件包,保留其全部已经安装的依赖关系
pacman -Ss <package>	# 查询软件包

# 常用软件
pacman -S vim
pacman -S fish
```

### rpm

> rpm 命令是 RPM 软件包的管理工具.
```bash
rpm -qa 		# 搜索 rpm 包
rpm -qf /etc/my.conf	# 查询文件来自哪个包
rpm –ivh xxxx.rpm	# 安装本地包
rpm -e xxx	# 卸载
```

### yum

> yum 命令是在 Fedora 和 RedHat 以及 SUSE 中基于 rpm 的软件包管理器
```bash
yum update && yum upgrade # 更新和升级 rpm 软件包
yum repolist	# 查看仓库列表
yum provides ifconfig # 查看哪个包提供 ifconfig

# /var/run/yum.pid 已被锁定，PID 为 xxxx 的另一个程序正在运行。
rm -f /var/run/yum.pid	# 强制解锁占用

# 常用软件
yum groupinstall "Development Tools"
yum install openssl-devel
yum install git
yum install python
```

### apt

> apt 的全称是 Advanced Packaging Tool 是 Linux 系统下的一款安装包管理工具.
```bash
apt-get update && apt-get upgrade && apt-get dist-upgrade

# 无法获得锁 /var/lib/apt/lists/lock - open (11: 资源暂时不可用)
rm -rf /var/cache/apt/archives/lock
rm -rf /var/lib/dpkg/lock-frontend
rm -rf /var/lib/dpkg/lock	# 强制解锁占用

# 常用软件
apt install python
apt install gcc
apt install gcc-++
apt install g++
apt install make
apt install vim-common=2:7.4.1689-3ubuntu1.2
apt install vim
apt install git
apt install curl

apt-add-repository ppa:fish-shell/release-3
apt update
apt install fish
```

**Gdebi**

Gdebi 是一个安装 .deb 软件包的工具。提供了图形化的使用界面
```bash
apt update
apt install gdebi
```

### 常用软件

**bash-insulter**
```bash
git clone https://github.com/No-Github/bash-insulter.git bash-insulter
cp bash-insulter/src/bash.command-not-found /etc/
chmod 777 /etc/bash.command-not-found
source /etc/bash.command-not-found
```
```vim
vim /etc/bashrc

. /etc/bash.command-not-found
echo "$(tput cuf 10) $(tput setab 1)FBI WARNING$(tput sgr 0)"
echo ""
echo "Federal Law provides severe civil and criminal penalties for
the unauthorized reproduction, distribution, or exhibition of
copyrighted motion pictures (Title 17, United States Code,
Sections 501 and 508). The Federal Bureau of Investigation
investigates allegations of criminal copyright infringement"
echo "$(tput cuf 5) (Title 17, United States Code, Section 506)."
```

**Fish**
```bash
echo /usr/bin/fish | sudo tee -a /etc/shells	# 加默认
usermod -s /usr/bin/fish <USERNAME>
```

**zsh**
```bash
apt install zsh	# 安装 zsh

chsh -s /bin/zsh	# 切换默认的 shell 为 zsh

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"	# 安装 oh-my-zsh

git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions	# 下载命令补全插件

# zshrc 配置文件中修改如下内容
vim ~/.zshrc

plugins=(git zsh-autosuggestions)

zsh	# 重新加载 zsh 配置

# 更多主题见此 https://github.com/robbyrussell/oh-my-zsh/wiki/themes
```

**Powerline-shell**

`pip install powerline-shell`
```vim
vim ~/.config/fish/config.fish

function fish_prompt
	powerline-shell --shell bare $status
end
```

---

# 🦋系统管理
## 系统设置
### 时间

```bash
date	# 查看当前时间
date -R	# 查看当前时区
data -s "2019-03-31 13:12:29"	# 修改系统时间

ntpdate	# 设置本地日期和时间
	ntpdate 0.rhel.pool.ntp.org	# 网络同步时间

hwclock	   # 硬件时钟访问工具
	hwclock –w # 将系统时钟同步到硬件时钟,将当前时间和日期写入 BIOS,避免重启后失效
	hwclock -s # 将硬件时钟同步到系统时钟

cal	# 查看日历
```

**tips**
- **ntpd 与 ntpdate 的区别**
	- ntpd 在实际同步时间时是一点点的校准过来时间的,最终把时间慢慢的校正对.而 ntpdate 不会考虑其他程序是否会阵痛,直接调整时间.
	- 一个是校准时间,一个是调整时间.
	- https://blog.csdn.net/tuolaji8/article/details/79971591

### 语言

`echo  $LANG` 查看当前操作系统的语言
```vim
vim /etc/locale.conf

set LANG en_US.UTF-8	# 更改默认语言
	 zh_CN.UTF-8
```
`source   /etc/locale.conf`

### 启动项-计划任务

**crontab**
```vim
vim /etc/crontab	# 系统任务调度的配置文件

# 前5个星号分别代表:分钟,小时,几号,月份,星期几
* * * * * command	# 每1分钟执行一次 command
3,15 * * * * command	# 每小时的第3和第15分钟执行
@reboot	command	# 开机启动

# 例子
0 */2 * * * /sbin/service httpd restart	# 意思是每两个小时重启一次apache
50 7 * * * /sbin/service sshd start	# 意思是每天7：50开启ssh服务
50 22 * * * /sbin/service sshd stop	# 意思是每天22：50关闭ssh服务
0 0 1,15 * * fsck /home	# 每月1号和15号检查/home 磁盘
1 * * * * /home/bruce/backup	# 每小时的第一分执行 /home/bruce/backup这个文件
00 03 * * 1-5 find /home "*.xxx" -mtime +4 -exec rm {} \;	# 每周一至周五3点钟，在目录/home中，查找文件名为*.xxx的文件，并删除4天前的文件。
30 6 */10 * * ls	# 意思是每月的1、11、21、31日是的6：30执行一次ls命令
```

**at**

> 在特定的时间执行一次性的任务
```bash
at now +1 minutes
echo "test" > test.txt
<ctrl+d>

atq：列出用户的计划任务,如果是超级用户将列出所有用户的任务,结果的输出格式为：作业号、日期、小时、队列和用户名
atrm：根据 Job number 删除 at 任务
```

**/etc/rc.local**

在文件末尾 (exit 0 之前) 加上你开机需要启动的程序或执行的命令即可 (执行的程序需要写绝对路径,添加到系统环境变量的除外) ,如

**/etc/profile.d/**

将写好的脚本 (.sh 文件) 放到目录 `/etc/profile.d/` 下,系统启动后就会自动执行该目录下的所有 shell 脚本

### 账号管控

**账号**
```bash
id  # 当前用户
whoami	# 当前用户
groups	# 当前组
cut -d: -f1 /etc/passwd	# 查看系统所有用户

useradd -d /home/<用户名> -s /sbin/nologin <用户名>  # 创建用户
passwd <用户名>>	# 设置用户密码

addgroup <组名>	# 创建组
addgroup <用户名> <组名>	# 移动用户到组

newgrp <组名>	# 创建组

usermod -g <组名> <用户名>	# 修改用户的主组
usermod -G <附加组> <用户名>	# 修改用户的附加组
usermod -s /bin/bash <用户名>	# 修改用户登录的 Shell
usermod -L <用户名>  # 锁定用户
usermod -U <用户名>  # 解锁用户

userdel <用户名>	# 只删除用户不删除家目录
userdel -r <用户名>	# 同时删除家目录
userdel -f <用户名>	# 强制删除,即使用户还在登陆中
sudo passwd	# 配置 su 密码

chage	# 修改帐号和密码的有效期限
	chage -l <用户名> # 查看一下用户密码状态
	chage -d <用户名> # 把密码修改曰期归零了,这样用户一登录就要修改密码

passwd -l <用户名>  # 锁定用户
passwd -u <用户名>  # 解锁用户
```

**权限**
```bash
chown named.named <文件/文件夹>	# 将文件给指定用户及组

chmod <数字> <文件>	# 给文件权限
# 用户 rwx、组 rwx、其他用户 rwx  4.2.1 分别代表读,写,执行
	chmod 777 <文件>
	chmod o=rw <文件>	# 代表只给其他用户分配读写权限
	chmod u=rw,g=r,o= <文件>
	chown -R u+x <文件夹>	# 对文件夹及其子目录所有文件的所有者增加执行权限

	chmod u+s test_file    # 给文件增加 SUID 属性
	chmod g+s test_dir     # 给目录增加 SGID 属性
	chmod o+t test_dir     # 给目录增加 Sticky 属性

chgrp	# 改变文件或目录所属的用户组
	chgrp user1 file.txt	# Change the owning group of the file file.txt to the group named user1.
	chgrp -hR staff /office/files	# Change the owning group of /office/files, and all subdirectories, to the group staff.

umask 002	# 配置反码,代表创建文件权限是 664 即 rw-rw-r--,默认 0022(重启后消失)
# umask 值 002 所对应的文件和目录创建缺省权限分别为 6 6 4 和 7 7 5
# 需要长期修改,可以直接改 vim /etc/profile 中 umask 值

chattr	# 可修改文件的多种特殊属性
	chattr +i <文件>	# 增加后,使文件不能被删除、重命名、设定链接接、写入、新增数据
	chattr +a <文件>	# 增加该属性后,只能追加不能删除,非root用户不能设定该属性
	chattr +c <文件>	# 自动压缩该文件,读取时会自动解压.Note: This attribute has no effect in the ext2, ext3, and ext4 filesystems.

lsattr <文件>	# 该命令用来读取文件或者目录的特殊权限
```
```vim
visudo	# 加 sudo 权限

user1 ALL=(ALL)     ALL
```
加 sudo 权限(仅限 Ubuntu)
```bash
adduser user1 sudo	# 将 user1 加到 sudo 组中
deluser user1 sudo	# 将 user1 从 sudo 组中删除
```

**ACL**
```bash
setfacl -m u:apache:rwx <文件/文件夹>	# 配置 ACL
getfacl <文件/文件夹>	# 查看 ACL 权限
setfacl -b <文件/文件夹>	# 删除 ACL
```

### SELinux
**查看 SELinux 状态**
```bash
getenforce	# 查看 selinux 状态
/usr/sbin/sestatus	# 查看安全策略
```

**关闭 SELinux**
- 需要重启
	```vim
	vim /etc/selinux/config

	SELINUX=disabled
	```

- 不需要重启

	`setenforce 0`

---

## 系统信息

```bash
uname -a	# 打印当前系统相关信息
cat /etc/os-release
cat /proc/version

lshw	# 查看硬件信息
```

### 进程管理

**服务管理**
```bash
service <程序> status/start/restart/stop	# 控制系统服务的实用工具
systemctl # 系统服务管理器指令
	systemctl enable crond.service	# 让某个服务开机自启(.service 可以省略)
	systemctl disable crond	# 不让开机自启
	systemctl status crond	# 查看服务状态
	systemctl start crond	# 启动某个服务
	systemctl stop crond	# 停止某个服务
	systemctl restart crond	# 重启某个服务
	systemctl reload *	# 重新加载服务配置文件
	systemctl is-enabled crond	# 查询服务是否开机启动

chkconfig	# 检查、设置系统的各种服务
	chkconfig --list	# 列出所有的系统服务
	chkconfig --add httpd	# 增加 httpd 服务
	chkconfig --del httpd	# 删除 httpd 服务
	chkconfig --level httpd 2345 on	# 设置 httpd 在运行级别为 2、3、4、5 的情况下都是 on(开启)的状态,另外如果不传入参数 --level,则默认针对级别 2/3/4/5 操作.

# 从 CentOS7 开始,CentOS 的服务管理工具由 SysV 改为了 systemd,但即使是在 CentOS7 里,也依然可以使用 chkconfig 这个原本出现在 SysV 里的命令.
```

**进程处理**
```bash
ps -aux	# 查看进程

# 杀进程
kill
kill -s STOP <PID>	# 删除执行中的程序或工作
	kill -l	# 显示信号
	kill -HUP <pid>	# 更改配置而不需停止并重新启动服务
	kill -9 <PID> && kill -KILL <pid> # 信号(SIGKILL)无条件终止进程
killall <PID>	# 使用进程的名称来杀死进程

ctrl+z # 将前台运行的任务暂停,仅仅是暂停,而不是将任务终止.
bg	# 转后台运行
fg	# 转前台运行

# 查进程
jobs	# 显示 Linux 中的任务列表及任务状态
	jobs -l	# 显示进程号

pidof program	# 找出 program 程序的进程 PID
pidof -x script # 找出 shell 脚本 script 的进程 PID

cmdline
# 在Linux系统中,根据进程号得到进程的命令行参数,常规的做法是读取 /proc/{PID}/cmdline,并用'\0'分割其中的字符串得到进程的 args[],例如下面这个例子：
	# xxd /proc/7771/cmdline
	0000000: 2f69 746f 612f 6170 702f 6d61 7665 2f62  /itoa/app/mave/b
	0000010: 696e 2f6d 6176 6500 2d70 002f 6974 6f61  in/mave.-p./itoa
	0000020: 2f61 7070 2f6d 6176 6500                 /app/mave.
	通过分割其中的 0x00(C 语言字符串结束符),可以把这个进程 args[],解析出来：
	args[0]=/itoa/app/mave/bin/mave
	args[1]=-p
	args[2]=/itoa/app/mave

# 不挂断地运行命令
nohup	# nohup 命令运行由 Command参数和任何相关的 Arg参数指定的命令，忽略所有挂断（SIGHUP）信号。在注销后使用 nohup 命令运行后台中的程序。要运行后台中的 nohup 命令，添加 & （ 表示“and”的符号）到命令的尾部。
	nohup COMMAND &	# 使命令永久的在后台执行
	sh test.sh &	# 将 sh test.sh 任务放到后台 ，关闭xshell，对应的任务也跟着停止。
	nohup sh test.sh	# 将 sh test.sh 任务放到后台，关闭标准输入，终端不再能够接收任何输入（标准输入），重定向标准输出和标准错误到当前目录下的 nohup.out 文件，即使关闭 xshell 退出当前 session 依然继续运行。
	nohup sh test.sh  & # 将 sh test.sh 任务放到后台，但是依然可以使用标准输入，终端能够接收任何输入，重定向标准输出和标准错误到当前目录下的 nohup.out 文件，即使关闭 xshell 退出当前 session 依然继续运行。

setsid	# setsid 主要是重新创建一个 session,子进程从父进程继承了 SessionID、进程组 ID 和打开的终端,子进程如果要脱离父进程，不受父进程控制，我们可以用这个 setsid 命令
	setsid ping baidu.com	# setsid 后子进程不受终端影响，终端退出，不影响子进程
	# 别急,  ps -ef | grep ping   ,kill 相应的进程就可以关掉了😂

disown	# 使作业忽略 HUP 信号
	# 示例1,如果提交命令时已经用“&”将命令放入后台运行，则可以直接使用“disown”
	ping www.baidu.com &
	jobs
	disown -h %1
	ps -ef |grep ping

	# 示例2,如果提交命令时未使用“&”将命令放入后台运行，可使用 CTRL-z 和“bg”将其放入后台，再使用“disown”
	ping www.baidu.com
	bg %1
	jobs
	disown -h %1
	ps -ef |grep ping
```

**查询负载、进程监控**
```bash
top	# 实时动态地查看系统的整体运行情况
free	# 显示当前系统未使用的和已使用的内存数目
vmstat 1	# 显示虚拟内存状态
ps	# 报告当前系统的进程状态
	ps -aux #显示现在所有用户所有程序
	# 由于ps命令能够支持的系统类型相当的多,所以选项多的离谱,这里略
pidstat -u -p ALL	# 查看所有进程的 CPU 使用情况

watch <其他命令>	# 以周期性的方式执行给定的指令，指令输出以全屏方式显示。
	-n：指定指令执行的间隔时间（秒）；
	-d：高亮显示指令输出信息不同之处；
	-t：不显示标题。
```

---

# 🛠设备管理
## 硬盘-数据

**磁盘配额**
- quota

**分区**
```bash
fdisk ‐l		# 查看磁盘情况
fdisk /dev/sdb	# 创建系统分区
	n	# 添加一个分区
	p	# 建立主分区
	1	# 分区号
	后面都是默认,直接回车

	t	# 转换分区格式
	8e	# LVM 格式

	w	# 写入分区表
```

**挂载**
```bash
mount /dev/sdd1 /mnt/sdd	# 挂载新硬盘到操作系统的某个节点上
mount /dev/cdrom /mnt/cdrom/	# 挂载 CD 镜像
mount -t vfstype	# 指定文件系统的类型,通常不必指定.mount 会自动选择正确的类型.

vi /etc/fstab	# 自动挂载
/dev/cdrom /mnt/cdrom iso9660 defaults 0 0
```

**删除**
```bash
rm <文件>	# 删除指定文件
	rm -r <文件夹>	# 删除文件夹
	rm -i <文件>	# 删除前确认
	rm -f <文件>	# 强制删除
	rm -v <文件>	# 显示详细信息

shred -zvu -n  5 <文件>	# 主要用于文件覆盖内容,也可以删除
	# -z - 用零添加最后的覆盖以隐藏碎化
	# -v - 显示操作进度
	# -u - 覆盖后截断并删除文件
	# -n - 指定覆盖文件内容的次数(默认值为3)
```

**数据恢复**
- [数据恢复](./Secure-Linux.md#文件恢复)

**占用**
```bash
df	# 报告驱动器的空间使用情况
	df -H	# 以人类可读的格式进行显示
	df -ah	# 查看磁盘占用大的文件夹

du	# 报告目录的空间使用情况
	du -h /etc/yum | sort	# 以人类可读的格式进行显示,排序显示
	du -sh /etc/yum	# 特定目录的总使用量
	du --max-depth=1 -h	# 查看文件夹下各个文件夹的磁盘占用
```

**dd**
```bash
dd
	dd if=/dev/zero of=sun.txt bs=1M count=1
	# if 代表输入文件.如果不指定 if,默认就会从 stdin 中读取输入.
	# of 代表输出文件.如果不指定 of,默认就会将 stdout 作为默认输出.
	# ibs=bytes：一次读入 bytes 个字节,即指定一个块大小为 bytes 个字节.
	# obs=bytes：一次输出 bytes 个字节,即指定一个块大小为 bytes 个字节.
	# bs 代表字节为单位的块大小.
	# count 代表被复制的块数.
	# /dev/zero 是一个字符设备,会不断返回 0 值字节(\0).
```

**LVM**
```bash
pvcreate /dev/sdb1	# 初始化物理卷
vgcreate ‐s 16M datastore /dev/sdb1 # 创建物理卷
lvcreate ‐L 8G ‐n database datastore # 创建逻辑卷
lvdisplay # 查看逻辑卷的属性
```

**块设备信息**
```bash
lsblk	# 显示所有可用块设备的信息
	lsblk -m	# 显示设备所有者相关的信息,包括文件的所属用户、所属组以及文件系统挂载的模式

blkid   # 输出所有可用的设备、UUID、文件系统类型以及卷标
	blkid /dev/sda1
	blkid -U d3b1dcc2-e3b0-45b0-b703-d6d0d360e524
	blkid -po udev /dev/sda1	# 获取更多详细信息
	blkid -g	# 清理 blkid 的缓存
```

---

# 🚬Linux 编程
很多脚本第一行用来指定本脚本用什么解释器来执行

例如 `#!/usr/bin/python` 相当于写死了 python 路径.

而 `#!/usr/bin/env python` 会去环境设置寻找 python 目录,可以增强代码的可移植性,推荐这种写法.

**常见问题**

-  Linux 下运行 bash 脚本显示“: /usr/bin/env: "bash\r": 没有那个文件或目录

	这主要是因为 bash 后面多了 \r 这个字符的原因.在 linux 终端下,输出 \r 会什么都不显示,只是把光标移到行首.于是终端虽然输出了 /usr/bin/env bash,但是碰到\r后,光标会被移到行首,接着输出了:No such file or directory 把前面的覆盖掉了.于是出现了那个莫名其妙的出错信息了

	一般来说这是下载在 windows 下载 github 脚本后会遇到的问题,下载压缩包,在 linux 中解压,或直接使用 linux 下载

	或者用 vim 打开 sh 脚本文件, 重新设置文件的格式
    ```vim
	：set ff=unix
    ：wq!
	```

- linux 运行 shell 出现未预期的符号 `$'do\r'' 附近有语法错误

	看上面应该是语法错误,但无论怎么改还是报错,经过一番探索发现,自己的文件是从 windows 里面拷贝到 linux 的,可能是两种系统格式不一样.

	解决方法如下：

	 (1) 打开 notepad++ 编辑 .sh 文件

	 (2) notepad++ 右下角将 windows 模式改为 linux 模式

**source 命令与 `.` 的区别**

- source 命令是 bash shell 的内置命令,从 C Shell 而来.
- source 命令的另一种写法是点符号,用法和 source 相同,从 Bourne Shell 而来.
- source 命令可以强行让一个脚本去立即影响当前的环境.
- source 命令会强制执行脚本中的全部命令,而忽略文件的权限.
- source 命令通常用于重新执行刚修改的初始化文件,如 .bash_profile 和 .profile 等等.
- source 命令可以影响执行脚本的父 shell 的环境,而 export 则只能影响其子 shell 的环境.
- source a.sh 同直接执行 ./a.sh 有什么不同呢,比如你在一个脚本里 export $KKK=111 ,如果你用 ./a.sh 执行该脚本,执行完毕后,你运行 echo $KKK ,发现没有值,如果你用 source 来执行 ,然后再 echo ,就会发现 KKK=111.因为调用 ./a.sh 来执行 shell 是在一个子 shell 里运行的,所以执行后,结果并没有反应到父 shell 里,不过 source 不同,他就是在本 shell 中执行的,所以能看到结果.

## 编译
```bash
mount -t tmpfs tmpfs ~/build -o size=1G	# 把文件放到内存上做编译
make -j	# 并行编译
ccache	# 把编译的中间结果进行缓存,以便在再次编译的时候可以节省时间.

# 在 /usr/local/bin 下建立 gcc,g++,c++,cc的symbolic link,链到/usr/bin/ccache上.总之确认系统在调用 gcc 等命令时会调用到 ccache 就可以了(通常情况下 /usr/local /bin 会在 PATH 中排在 /usr/bin 前面).

distcc	# 多台机器一起编译
	/usr/bin/distccd  --daemon --allow 10.64.0.0/16 # 默认的 3632 端口允许来自同一个网络的 distcc 连接.

	export DISTCC_HOSTS="localhost 10.64.25.1 10.64.25.2 10.64.25.3"
	把 g++,gcc 等常用的命令链接到 /usr/bin/distcc 上

	make -j4	# 在 make 的时候,也必须用 -j 参数,一般是参数可以用所有参用编译的计算机 CPU 内核总数的两倍做为并行的任务数.
	distccmon-text # 查看编译任务的分配情况.
```

---

`为了自己想过的生活,勇于放弃一些东西.这个世界没有公正之处,你也永远得不到两全之计.若要自由,就得牺牲安全.若要闲散,就不能获得别人评价中的成就.若要愉悦,就无需计较身边人给予的态度.若要前行,就得离开你现在停留的地方.——《托斯卡纳艳阳下》`
