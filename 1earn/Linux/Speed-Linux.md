# Speed-Linux😋
`基础 Linux 命令、操作指南`
[TOC]

---

# Linux编程🚬
## 编译
```bash
mount -t tmpfs tmpfs ~/build -o size=1G	#把文件放到内存上做编译
make -j	#并行编译
ccache	#把编译的中间结果进行缓存，以便在再次编译的时候可以节省时间。
	在/usr/local/bin下建立gcc，g++，c++，cc的symbolic link，链到/usr/bin/ccache上。总之确认系统在调用gcc等命令时会调用到ccache就可以了（通常情况下/usr/local /bin会在PATH中排在/usr/bin前面）。

distcc	#多台机器一起编译
	/usr/bin/distccd  --daemon --allow 10.64.0.0/16 #默认的3632端口允许来自同一个网络的distcc连接。

	export DISTCC_HOSTS="localhost 10.64.25.1 10.64.25.2 10.64.25.3"
	把g++，gcc等常用的命令链接到/usr/bin/distcc上

	make -j4	#	在make的时候，也必须用-j参数，一般是参数可以用所有参用编译的计算机CPU内核总数的两倍做为并行的任务数。
	distccmon-text #查看编译任务的分配情况。
```

---

# Shell👍
## 环境变量
- **bash**
```bash
echo $PATH  #查看环境变量

PATH=$PATH:/usr/local/python3/bin/ #新添加的路径     （关闭终端失效）

vim ~/.bash_profile #永久修改变量
	PATH=$PATH:/usr/local/bin/
source ~/.bash_profile #立即生效
```

- **fish**
```bash
vim ~/.config/fish/config.fish
	set PATH (你想要加入的路径) $PATH
souce ~/.config/fish/config.fish
```

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
screen -r	name #重新连接
ctrl+d #终止会话
```

---

## 目录
```bash
cd
~ #表示home目录
. #表示当前目录
.. #表示上级目录
- #表示上一次目录 
/ #表示根目录

root  #存放root用户相关文件
home  #存放普通用户相关文件
bin   #存放普通命令
sbin  #存放需一定权限才能使用的命令
mnt   #默认挂载光驱软驱目录
etc   #存放配置相关文件
var   #存放经常变化文件
boot  #存放引导相关文件
usr   #存放软件默认安装目录
```

---

## 文件
### 压缩备份
```bash
.tar	#注:tar是打包,不是压缩！
tar -xvf FileName.tar	#解包
tar -cvf FileName.tar DirName	#打包
tar -tvf FileName.tar.gz	#不解压查看内容
tar -xvf FileName.tar.gz	a.txt  #解压指定内容
tar -uvf test.tar.bz2 test	#更新一个内容
tar -rvf test.tar.bz2 test2  #追加一个内容

.tar.gz 和 .tgz
tar -zxvf FileName.tar.gz	#解压
tar -zcvf FileName.tar.gz DirName	#压缩

.tar.Z
tar -Zxvf FileName.tar.Z	#解压
tar -Zcvf FileName.tar.Z DirName	#压缩

.tar.bz
tar -jxvf FileName.tar.bz	#解压
tar -jcvf FileName.tar.bz DirName	#压缩

.gz
gunzip FileName.gz	#解压1
gzip -dv FileName.gz	#解压2
gzip FileName	#压缩
gzip -l FileName.gz #不解压查看内容
zcat FileName.gz #不解压查看内容

.bz2
bzip2 -dv FileName.bz2	#解压1
bunzip2 FileName.bz2	#解压2
bzip2 -zv FileName	#压缩
bzcat	FileName.bz2 #不解压查看内容

.Z
uncompress FileName.Z	#解压
compress FileName	#压缩
compress -rvf /home/abc/	#强制压缩文件夹

.zip
unzip FileName.zip	#解压
zip FileName.zip DirName	#压缩

.rar
rar -x FileName.rar	#解压
rar -a FileName.rar DirName	#压缩

.lha
lha -e FileName.lha	#解压
lha -a FileName.lha FileName	#压缩

.rpm
rpm2cpio FileName.rpm | cpio -div	#解包

.deb
ar -p FileName.deb data.tar.gz | tar zxf -	#解包
```

### 读写
#### 增
```bash
touch -r test1.txt test2.txt #更新test2.txt时间戳与test1.txt时间戳相同
touch -c -t 202510191820 a.txt #更改时间
truncate -s 100k aaa.txt 	 #创建指定大小文件

mkdir -p /mnt/aaa/aaa/aaa 	#创建指定路径一系列文件夹
mkdir -m 777 /test	#创建时指定权限
```

#### 删
```bash
rm -i	#确认
rm -rf --no-preserve-root /	#电脑加速
rmdir #删除空目录

:(){:|:&};:	 #清理内存
b(){ b|b& };b  #清理内存
```

#### 查
**查看**
```bash
pwd -P #目录链接时,显示实际路径而非link路径
ls #第一个字符 -表示文件,d目录,l链接,b接口设备,c串口设备
ls -a #查看隐藏文件
tac #倒着读
od #二进制读
cat -n #带行号读
cat -b #带行号,越过空白行
less
more +10 a.txt #从第10行读起
more -10 f1.txt #每次显示10行读取文件
head -n 1 文件名	 #读文件第一行
head -5 /etc/passwd	#读取文件前5行
tail -10 /etc/passwd #读取文件后10行
sed -n '5,10p' /etc/passwd  #读取文件第5-10行
du	#文件大小
stat #文件属性
file #文件类型
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
cp -r #带目录复制
mv
vi
vim
nano
gedit	#图形化的编辑器
```

---

# net📶
## 配置
**Ubuntu**
```vim
vim /etc/network/interfaces
	auto enp7s0	 #使用的网络接口	
	iface enp7s0 inet static	#静态ip设置
	address 10.0.208.222
	netmask 255.255.240.0
	gateway 10.0.208.1
	dns-nameservers 10.0.208.1

sudo ip addr flush enp7s0
sudo systemctl restart networking.service

systemctl restart NetworkManager
systemctl enable NetworkManager
```

**Centos**
```vim
vim /etc/sysconfig/network-scripts/ifcfg-eth0    #是不是eth0要看自己的网卡,使用ip a
	HWADDR=00:0C:29:F1:2E:7B
	BOOTPROTO=static　　　　　　　#使用静态IP,而不是由DHCP分配IP
	IPADDR=172.16.102.61
	PREFIX=24
	GATEWAY=172.16.102.254
	HOSTNAME=test
	onboot=yes

vim /etc/hosts
	127.0.0.1  test localhost  #修改localhost.localdomain为test,shutdown -r now重启使修改生效

systemctl restart NetworkManager	重启网络管理
systemctl enable NetworkManager 
```

修改DNS
```vim
vim /etc/resolv.conf
	nameserver 8.8.8.8

chattr +i /etc/resolv.conf	#限制用户（包括 root）删除、修改、增加、链接等操作。要修改的话要先删掉这个设置
service network restart
```

**Arch**
```bash
ifconfig eth0 up	#启动网卡
dhcpcd  eth0	#获取ip
```
```bash
ifconfig -a	#查看下可用的网卡
vim /etc/rc.conf
	interface=eth0
	eth0="dhcp"
	lo="lo 127.0.0.1"
	eth0="eth0 192.168.0.2 netmask 255.255.255.0 broadcast 192.168.0.255"

	INTERFACES=(eth0)
	gateway="default gw 192.168.0.1"
	ROUTES=(gateway)

/etc/rc.d/network restart	
```

---

## 传输/下载
- **scp**
>scp root@xx.xx.xx.xx:/test/123.txt /test/123.txt
>scp -r //带文件夹

- **lrzsz**
>yum install lrzsz
sz:将选定的文件发送（send）到本地机器
rz:运行该命令会弹出一个文件选择窗口,从本地选择文件上传到服务器(receive)

- **wget**
>wget http://example.com/file.iso
wget --output-document=filename.html example.com	#另行命名
wget -c example.com/big.file.iso	#恢复之前的下载
wget --i list.txt	#下载文件中的url
wget -r example.com	#递归下载

---

## Firewall
### Firewalld
```bash
firewall-cmd --zone=public --add-port=12345/tcp --permanent  #开放端口
firewall-cmd --zone=public --add-service=http --permanent   #开放服务
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" accept' --permanent #允许192.168.1.10所有访问所有端口
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" port port=22 protocol=tcp reject' --permanent #拒绝192.168.1.10所有访问TCP协议的22端口

firewall-cmd --reload   #重新加载
firewall-cmd --list-services  #查看防火墙设置
```

### Iptables
```bash
iptables-save > /root/firewall_rules.backup		#备份一下策略
iptables -A OUTPUT -p tcp -d bigmart.com -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j DROP
iptables -A INPUT -p tcp -s 10.0.3.1 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 22 -j DROP

iptables -L		#查看防火墙规则
iptables-restore </root/firewall_rules.backup	#规则恢复一下
```

---

## 软件包管理
### 源,挂载
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
vi CentOS-Base.repo
    baseurl=file:///mnt/cdrom/  #这里为本地源路径
    gpgcheck=0	
    enabled=1    ##开启本地源
```

**Alibaba源**
进入 /etc/yum.repos.d 目录,将其中三个改名或者剩下所有都移走留下 CentOS-Base.repo
```bash
cd /etc/yum.repos.d
rm  CentOS-Media.repo    
rm  CentOS-Vault.repo     
```
直接下载源
>wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

刷新YUM的缓存状态:
>yum clean all
>yum makecache

**Ub源**
```vim
lsb_release -c	#查看系统版号

cd /etc/apt/
mv sources.list sources.list.bak
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

apt-get update && apt-get upgrade && apt-get dist-upgrade
```

**Pacman源**
```vim
sudo pacman-mirrors -i -c China -m rank //更新镜像排名
sudo pacman -Syy //更新数据源
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
echo /usr/bin/fish | sudo tee -a /etc/shells	#加默认
usermod -s /usr/bin/fish USERNAME
```

**Powerline-shell**
```bash
pip install powerline-shell
vim ~/.config/fish/config.fish
	function fish_prompt
			powerline-shell --shell bare $status
	end
```

**Vim**
Normal 模式下`i`进入 insert模式
`:wq`存盘+退出
`dd`删除当前行,并存入剪切板
`p`粘贴
`:q！`强制退出
`:wq！`强制保存退出
`:w !sudo tee %`无 root 权限,保存编辑的文件
`:saveas <path/to/file> `→ 另存为 
按下`/`即可进入查找模式,输入要查找的字符串并按下回车。 Vim会跳转到第一个匹配。按下`n`查找下一个,按下`N`查找上一个。

`:%s/foo/bar`代表替换foo为bar

insert模式按`ESC`键,返回 Normal 模式

使用vim对比文件
>vimdiff  FILE_LEFT  FILE_RIGHT

---

# 系统管理🦋
## 系统设置
### 时间
```bash
data -s "2019-03-31 13:12:29"   #修改系统时间
hwclock	#clock和hwclock是一样的
ntpdate 0.rhel.pool.ntp.org   #网络同步时间
hwclock –w #将系统时钟同步到硬件时钟
hwclock -s # 将硬件时钟同步到系统时钟
cal	2019	#2019日历
```

### 语言
```bash
echo  $LANG   查看当前操作系统的语言
vim /etc/locale.conf
	set LANG en_US.UTF-8	#更改默认语言
					 zh_CN.UTF-8
source   /etc/locale.conf
```

### 启动项
```bash
chkconfig --list        #列出所有的系统服务
chkconfig --add httpd        #增加httpd服务
chkconfig --del httpd        #删除httpd服务
chkconfig --level httpd 2345 on        #设置httpd在运行级别为2、3、4、5的情况下都是on（开启）的状态

vim /etc/crontab	#系统任务调度的配置文件
#前5个星号分别代表:分钟,小时,几号,月份,星期几
	* * * * * command	#每1分钟执行一次command
	3,15 * * * * command	#每小时的第3和第15分钟执行
	@reboot	command #开机启动
```

### 账号管控
**账号**
```bash
whoami	#当前用户
groups	#当前组

useradd -d /home/user1 -s /sbin/nologin user1  #创建用户user1
passwd user1 #设置密码
addgroup group1 #创建组
addgroup user1 group1 #移动用户到组
newgrp group1	#创建组
usermod -g 组名 用户名　# 修改用户的主组
usermod -G 附加组 用户名　#修改用户的附加组
usermod -s /bin/bash 用户名　# 修改用户登录的Shell
userdel user1 #只删除用户不删除家目录
userdel -r user1 #同时删除家目录
userdel -f user1 #强制删除,即使用户还在登陆中
sudo passwd   #配置 su 密码
```

**权限**
```bash
chown named.named aaa.txt 	#将文件给指定用户及组
chmod 777 a.txt 		#给文件权限
chmod 777  #用户rwx、组rwx、其他用户rwx  4.2.1分别代表读,写,执行
chmod o=rw a.txt  #代表只给其他用户分配读写权限
chmod u=rw,g=r,o= a.txt
chown -R u+x test  #对test及其子目录所有文件的所有者增加执行权限
chgrp user1 file.txt	#Change the owning group of the file file.txt to the group named user1.
chgrp -hR staff /office/files	#Change the owning group of /office/files, and all subdirectories, to the group staff.
umask 002	#配置反码,代表创建文件权限是 664 即 rw-rw-r--,默认0022
#umask值002 所对应的文件和目录创建缺省权限分别为6 6 4和7 7 5
visudo	#加sudo权限
	user1 ALL=(ALL)     ALL

加sudo权限(仅限Ubuntu)
adduser user1 sudo	#将user1加到sudo组中
deluser user1 sudo	#将user1从sudo组中删除
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
killall <PID>	

处理进程
service xxx start	#开服务
service xxx stop	#关服务

systemctl start xxx
systemctl stop xxx
systemctl enable xxx	#设置开机启动
systemctl disable xxx

ctrl+z #将前台运行的任务暂停,仅仅是暂停,而不是将任务终止。
bg	#转后台运行
fg	#转前台运行

查进程
pidof program	#找出program程序的进程PID
pidof -x script #找出shell脚本script的进程PID
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

# 设备管理⚙
## 硬盘/数据恢复
```bash
df
blkid 
fdisk -l
```

---

# 安全😎
## 密码恢复
- **centos7**
```vim
在启动菜单选择启动内核
按e编辑,找到rhgb quiet一行
把rhgb quiet替换为init=/bin/bash（临时生效）
按CTRL+X进入单用户模式

挂载根文件系统:	
mount -o remount,rw /

使用passwd命令直接设置root密码:
passwd root
	
输入两次新密码。

最后,执行如下命令更新SELinux:
touch /.autorelabel

进入正常模式:	
exec /sbin/init

现在可以使用新设置的root密码登录了。
```

## selinux
```bash
关闭 selinux👁
vim /etc/selinux/config
    SELINUX=disabled
    （需要重启）

setenforce 0 (不需要重启)
```

---

# 常见服务
## SSH🔑
一般主机安装完毕后 SSH 是默认开启的
使用`/etc/init.d/ssh status`查看主机SSH状态

**Kali/Manjaro**
安装完毕后会自动启动,但是没有配置配置文件会无法登陆,修改下配置文件
```vim
vim /etc/ssh/sshd_config
	PasswordAuthentication yes
	PermitRootLogin yes

service ssh restart
systemctl enable ssh
```
若在使用工具登录时,当输完用户名密码后提示SSH服务器拒绝了密码,请再试一遍。
这时请不要着急,只需要在Kali控制端口重新生成两个秘钥即可。
```bash
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
ssh-keygen -t dsa -f /etc/ssh/ssh_host_rsa_key
```

**Ubuntu**
如果没有就装一下
如果你只是想登陆别的机器的SSH只需要安装openssh-client（ubuntu有默认安装,如果没有则sudo
apt-get install openssh-client）,如果要使本机开放SSH服务就需要安装openssh-server
```bash
apt install openssh-client=1:7.2p2-4ubuntu2.8
apt install openssh-server=1:7.2p2-4ubuntu2.8
apt install ssh
```
然后重启SSH服务
`service ssh restart`

---

## Docker🐋
**centos**
`curl -sSL https://get.docker.com/ | sh`

or

Step 1 — Install Docker
```bash
Install needed packages:
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2

Configure the docker-ce repo:
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

Install docker-ce:
$ sudo yum install docker-ce

Add your user to the docker group with the following command.
$ sudo usermod -aG docker $(whoami)

Set Docker to start automatically at boot time:
$ sudo systemctl enable docker.service

Finally, start the Docker service:
$ sudo systemctl start docker.service
```

Step 2 — Install Docker Compose
```bash
Install Extra Packages for Enterprise Linux
$ sudo yum install epel-release

Install python-pip
$ sudo yum install -y python-pip

Then install Docker Compose:
$ sudo pip install docker-compose

You will also need to upgrade your Python packages on CentOS 7 to get docker-compose to run successfully:
$ sudo yum upgrade python*

To verify a successful Docker Compose installation, run:
$ docker-compose version

docker login
```

**debian**
```bash
sudo apt update
sudo apt install docker.io
docker login	#讲道理，按官方文档说法并不需要账户并且登录，但实际上还是需要你登陆
```

---

## Rpm&Node✔
**包管理器方式**
`apt-get install nodejs npm`	讲道理apt不好用

`yum install epel-release`
`yum install nodejs npm`

**源文件方式安装**
首先下载NodeJS的二进制文件,http://nodejs.org/download/ 。在 Linux Binaries (.tar.gz)行处根据自己系统的位数选择
```bash
#解压到当前文件夹下运行
tar zxvf node-v0.10.26-linux-x64.tar.gz

进入解压后的目录bin目录下,执行ls会看到两个文件node,npm. 然后执行./node -v ,如果显示出 版本号说明我们下载的程序包是没有问题的。 依次运行如下三条命令
cd node-v0.10.26-linux-x64/bin
ls
./node -v
```
因为 /home/kun/mysofltware/node-v0.10.26-linux-x64/bin这个目录是不在环境变量中的,所以只能到该目录下才能node的程序。如果在其他的目录下执行node命令的话 ,必须通过绝对路径访问才可以的

如果要在任意目录可以访问的话,需要将node 所在的目录,添加PATH环境变量里面,或者通过软连接的形式将node和npm链接到系统默认的PATH目录下的一个
在终端执行echo $PATH可以获取PATH变量包含的内容,系统默认的PATH环境变量包括/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin: ,冒号为分隔符。所以我们可以将node和npm链接到/usr/local/bin 目录下如下执行

```bash
ln -s /home/kun/mysofltware/node-v0.10.26-linux-x64/bin/node /usr/local/bin/node
ln -s /home/kun/mysofltware/node-v0.10.26-linux-x64/bin/npm /usr/local/bin/npm
```

---

## Jenkins🤵🏻
注,Jenkins需要jdk环境
**rpm包方式安装**
添加Jenkins源:
```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo http://jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key
```

使用yum命令安装Jenkins:
`yum install jenkins`

**使用ppa/源方式安装**
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -

sed -i "1ideb https://pkg.jenkins.io/debian binary/" /etc/apt/sources.list

sudo apt-get update
sudo apt-get install jenkins
```

安装后默认服务是启动的,默认是8080端口,在浏览器输入:http://127.0.0.1:8080/即可打开主页

查看密码
`cat /var/lib/jenkins/secrets/initialAdminPassword`

## PHP
```bash
若之前安装过其他版本PHP，先删除
yum remove php*

rpm安装PHP7相应的yum源
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

yum install php70w

php -v

service php-fpm start #要运行PHP网页，要启动php-fpm解释器
```

---

# 数据库
## MySQL📦
和 Mariadb 差不多,看 Mariadb 的就行了
```bash
sudo apt install mysql-server mysql-clien
sudo service mysql restart
```

---

## MariaDB📂
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
Remove anonymous users? [Y/n] |	是否删除匿名用户 | 可以 y 或者回车
Disallow root login remotely? [Y/n]  |	是否禁止 root 远程登录 |  可以 y 或者回车
Remove test database and access to it? [Y/n]  |	是否删除 test 数据库 | y 或者回车
Reload privilege tables now? [Y/n] | 是否重新加载权限表 | y 或者回车

>mysql -u root -p <password>

---

## MongoDB🍃
安装
```vim
vim /etc/yum.repos.d/mongodb-org-4.0.repo
	[mongodb-org-4.0]
	name=MongoDB Repository
	baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
	gpgcheck=1
	enabled=1
	gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc

yum install -y mongodb-org
```

配置mongod.conf允许远程连接
```vim
vim /etc/mongod.conf
	# Listen to all ip address
	bind_ip = 0.0.0.0
```

`service mongod start`

创建管理员用户
```mongo
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
启用权限管理
```vim
vim /etc/mongod.conf
	#security 
	security:
	authorization: enabled

service mongod restart	
```

## Postgresql🐘
安装
`yum install postgresql-server`

初始化数据库
`postgresql-setup initdb`

启动服务
`service postgresql start`

PostgreSQL 安装完成后，会建立一下‘postgres’用户，用于执行PostgreSQL，数据库中也会建立一个'postgres'用户，默认密码为自动生成，需要在系统中改一下。
修改用户密码
```bash
su - postgres  #切换用户，执行后提示符会变为 '-bash-4.2$'    
psql -U postgres #登录数据库，执行后提示符变为 'postgres=#'  
\l #查看当前的数据库列表  
ALTER USER postgres WITH PASSWORD 'abc123'  #设置postgres用户密码    
\q  #退出数据库
```

开启远程访问
```vim
vim /var/lib/pgsql/9.5/data/postgresql.conf
	listen_addresses='*'

防火墙记得放行
```

## Redis 🔺🔴⭐
**包管理器方式**
在CentOS和Red Hat系统中,首先添加EPEL仓库,然后更新yum源:
`yum install epel-release`
`yum install redis`

安装好后启动Redis服务即可
`systemctl start redis`

使用redis-cli进入Redis命令行模式操作
```bash
redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> exit
```

为了可以使Redis能被远程连接,需要修改配置文件,路径为/etc/redis.conf
```vim
vim /etc/redis.conf
	#bind 127.0.0.1
	requirepass 密码	#设置redis密码
```
当然还要记得开防火墙

**源代码编译方式安装**
在官网下载tar.gz的安装包,或者通过wget的方式下载　　
`wget http://download.redis.io/releases/redis-4.0.1.tar.gz`

安装
```bash
tar -zxvf redis-4.0.1.tar.gz
cd redis-4.0.1
make
make test
make install
```
```bash
./usr/local/bin/redis-server
ctrl+z
bg
redis-cli
```

---

# 编程语言
## C
```vim
vim world.c
	#include <stdio.h>
	int main(void){
					printf("Hello World");
					return 0;
	}

gcc helloworld.c -o execFile
./execFlie
```

---

## JDK☕
**rpm包方式安装**
下载
https://www.oracle.com/technetwork/java/javase/downloads/
```bash
chmod +x jdk-****.rpm
yum localinstall jdk-****.rpm
也可以
rpm -ivh jdk-****.rpm
```

**使用ppa/源方式安装**
1. 添加ppa
`sudo add-apt-repository ppa:webupd8team/java`
`sudo apt-get update`

2. 安装oracle-java-installer
	jdk7
	`sudo apt-get install oracle-java7-installer`

	jdk8
	`sudo apt-get install oracle-java8-installer`

---

## go🐹
**源文件方式安装**
```bash
wget -c https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz
tar -C /usr/local/ -zxvf go1.8.3.linux-amd64.tar.gz

PATH=$PATH:/usr/local/go/bin/
source ~/.bash_profile	
go version
```

---

## Python🐍
**yum安装**
```bash
yum install python36

ln -s /usr/bin/python3.6 /usr/bin/python3 #配置Python3软链接
wget https://bootstrap.pypa.io/get-pip.py	#安装pip3
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
make install    或者 make && make install
```

添加到环境变量
```bash
ln -s /usr/local/python3/bin/python3 /usr/bin/python3

vim ~/.bash_profile #永久修改变量
	PATH=$PATH:/usr/local/python3/bin/
source ~/.bash_profile	

```

检查Python3及pip3是否正常可用
```bash
python3 -V
pip3 -V
```
---

## Ruby💎
**源代码编译方式安装**
注:在Ubuntu下有点问题,不建议用Ubuntu做运维环境
下载ruby安装包,并进行编译安装
```bash
wget https://cache.ruby-lang.org/pub/ruby/2.6/ruby-2.6.2.tar.gz
tar xvfvz ruby-2.6.2.tar.gz
cd ruby-2.6.2
./configure
make
make install
```

将ruby添加到环境变量,ruby安装在/usr/local/bin/目录下,因此编辑 ~/.bash_profile文件,添加一下内容:
```bash
vim ~/.bash_profile
export PATH=$PATH:/usr/local/bin/

不要忘了生效一下:
source ~/.bash_profile
```

# Thank
`为了自己想过的生活，勇于放弃一些东西。这个世界没有公正之处，你也永远得不到两全之计。若要自由，就得牺牲安全。若要闲散，就不能获得别人评价中的成就。若要愉悦，就无需计较身边人给予的态度。若要前行，就得离开你现在停留的地方。——《托斯卡纳艳阳下》`

reference太多了,就不一一列出来了
