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

<p align="center">
    <a href="https://en.wikipedia.org/wiki/Pablo_Picasso"><img src="../../../assets/img/banner/Speed-Linux.jpg" width="90%"></a>
</p>

<p align="center">
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/Integrated/Linux/open-source.png" width="15%"></a>
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/Integrated/Linux/bash.png" width="15%"></a>
</p>

`基础 Linux 命令、操作指南`

---

# 大纲

* **[👍 基础使用](#基础使用)**
	* [环境变量](#环境变量)
	* [符号](#符号)
	* [会话](#会话)
		* [历史记录](#历史记录)
	* [文件和目录](#文件和目录)
		* [查看](#查看)
		* [创建](#创建)
		* [删除](#删除)
		* [搜索](#搜索)
		* [修改](#修改)
		* [比较](#比较)
		* [链接](#链接)
		* [压缩备份](#压缩备份)

* **[📶 网络管理](#网络管理)**
	* [查看网络信息](#查看网络信息)
	* [配置](#配置)
	* [抓包](#抓包)
	* [传输-下载](#传输-下载)
		* [bt](#bt)
		* [远程访问](#远程访问)
	* [Firewall](#firewall)
		* [Firewalld](#firewalld)
		* [Iptables](#iptables)
		* [ufw](#ufw)
	* [软件包管理](#软件包管理)
		* [apt](#apt)
		* [Binary](#binary)
		* [dnf](#dnf)
		* [dpkg](#dpkg)
		* [Pacman](#pacman)
		* [rpm](#rpm)
		* [snap](#snap)
		* [yum](#yum)
			* 配置 yum 源
			* 配置 EPEL 源
		* [常用软件](#常用软件)

* **[🦋 系统管理](#系统管理)**
	* [系统信息](#系统信息)
		* [日志](#日志)
	* [系统设置](#系统设置)
		* [时间](#时间)
		* [时区](#时区)
		* [语言](#语言)
		* [启动项-计划任务](#启动项-计划任务)
		* [SELinux](#selinux)
	* [账号管控](#账号管控)
	* [进程管理](#进程管理)
	* [内核管理](#内核管理)
	* [设备管理](#设备管理)
		* [内存](#内存)
		* [磁盘](#磁盘)
		* [无线网卡](#无线网卡)
		* [蓝牙](#蓝牙)
		* [外接硬盘](#外接硬盘)
		* CD & DVD

---

**在线查询命令**
- [Linux命令搜索引擎](https://wangchujiang.com/linux-command/) - 非常牛逼,推荐
- [Linux命令大全(手册)](https://man.linuxde.net/)

---

# 基础使用

**帮助**
```bash
man		# man 是 manual 的缩写，将指令的具体信息显示出来。
	man ls	# 显示 ls 命令的手册,按 q 退出
```

**命令风格**
- Unix 风格的参数,前面加单破折线,例如: `-H`
- BSD 风格的参数,前面不加破折线,例如: `h`
- GNU 风格的长参数,前面加双破折线,例如: `--help`

**关机**
```bash
shutdown	# 关机命令
	shutdown now	# 立刻关机(需要 root 权限)
# 选项说明
# -k ： 不会关机，只是发送警告信息，通知所有在线的用户
# -r ： 将系统的服务停掉后就重新启动
# -h ： 将系统的服务停掉后就立即关机
# -c ： 取消已经在进行的 shutdown 指令内容

halt		# 立刻关机(无需 root 权限)
poweroff	# 立刻关机(无需 root 权限)
reboot 		# 重启
```

**别名**

如果要执行命令太长又不符合用户的习惯，那么我们可以为它指定一个别名
```bash
alias please="sudo"						# 临时将 please 作为 sudo 的别名

# 想让其永久生效只需要将这些 alias 别名设置保存到文件： ~/.bashrc 里面就可以了
```

**运行脚本**
```bash
source <filename>						# 在当前 bash 环境下读取并执行 FileName 中的命令。
./xxx.sh								# 运行 xxx.sh 脚本
bash xxx.sh								# 运行 xxx.sh 脚本
```

## 环境变量

```bash
set
env
printenv

cat /proc/1/environ
cat /proc/$PID/environ
cat /proc/self/environ
```

- 图形模式登录时,顺序读取 : `/etc/profile` 和 `~/.profile`
- 图形模式登录后,打开终端时,顺序读取 : `/etc/bash.bashrc` 和 `~/.bashrc`
- 文本模式登录时,顺序读取 : `/etc/bash.bashrc` , `/etc/profile` 和 `~/.bash_profile`

**登录交互式 shell .bash_* files 的执行顺序**
```bash
execute /etc/profile
IF ~/.bash_profile exists THEN
    execute ~/.bash_profile
ELSE
    IF ~/.bash_login exist THEN
        execute ~/.bash_login
    ELSE
        IF ~/.profile exist THEN
            execute ~/.profile
        END IF
    END IF
END IF
```

**注销交互式 shell .bash_* files 的执行顺序**
```bash
IF ~/.bash_logout exists THEN
    execute ~/.bash_logout
END IF
```

**各变量文件区别**
- /etc/profile: 此文件为系统的每个用户设置环境信息。当用户登录时，该文件被执行一次，并从 /etc/profile.d 目录的配置文件中搜集shell 的设置。一般用于设置所有用户使用的全局变量。
- /etc/bashrc: 当 bash shell 被打开时，该文件被读取。也就是说，每次新打开一个终端 shell，该文件就会被读取。
- ~/.bash_profile 或 ~/.profile: 只对单个用户生效，当用户登录时该文件仅执行一次。用户可使用该文件添加自己使用的 shell 变量信息。另外在不同的LINUX操作系统下，这个文件可能是不同的，可能是 ~/.bash_profile， ~/.bash_login 或 ~/.profile 其中的一种或几种，如果存在几种的话，那么执行的顺序便是：~/.bash_profile、 ~/.bash_login、 ~/.profile。比如 Ubuntu 系统一般是 ~/.profile 文件。
- ~/.bashrc: 只对单个用户生效，当登录以及每次打开新的 shell 时，该文件被读取。

**bash 设置环境变量**
```bash
echo $PATH  						# 查看环境变量
```

- 一次性添加(关闭终端失效)
	```bash
	PATH=$PATH:/usr/local/python3/bin/
	```

- 永久修改变量(重启后生效)
	```diff
	vim ~/.bash_profile		在 Ubuntu 没有此文件，与之对应的是 /etc/bash.bashrc

	++ PATH=$PATH:/usr/local/bin/
	```
	```bash
	source ~/.bash_profile # 立即生效
	```

**fish 设置环境变量**
```vim
vim ~/.config/fish/config.fish

set PATH (你想要加入的路径) $PATH
```
```bash
souce ~/.config/fish/config.fish
```

**特殊变量**

bash 存在一些特殊变量，这些变量的值由shell提供，用户不能进行赋值。
```bash
$?   		# 为上一个命令的退出码，用来判断上一个命令是否执行成功。返回值是0，表示上一个命令执行成功；如果是非零，上一个命令执行失败。
$$   		# 为当前shell的进程ID。
$_   		# 为上一个命令的最后一个参数。
$!   		# 为最后一个后台执行的异步命令的进程ID。
$0   		# 为当前shell的名称(在命令行直接执行时)或者脚本名(在脚本中执行时)。
$-   		# 为当前shell的启动参数。
$@ 和 $#   	# $#表示脚本的参数数量，$@表示脚本的参数值。
```

**变量的默认值**

bash提供四个特殊语法，跟变量的默认值有关，目的是保证变量不为空。
```
{varname:-wore}
如果变量varname存在且不为空，则返回它的值，否则返回word。它的目的是返回一个默认值，比如${count:-0}表示变量count不存在时返回0。
```
```
{varname:=word}
如果变量varname存在且不为空，则返回它的值，否则将它设为word，并且返回word。它的目的是设置变量的默认值，比如${count:=0}表示变量count不存在时返回0，且将count设为0。
```
```
{varname:?message}
如果变量varname存在且不为空，则返回它的值，否则打印出varname: message，并中断脚本的执行。如果省略了message，则输出默认的信息“parameter null or not set.”。它的目的是防止变量未定义，比如${count:?"undefined!"}
表示变量count未定义时就中断执行，抛出错误，返回给定的报错信息undefined!。
```
```
{carnage:+word}
如果变量名存在且不为空，则返回word，否则返回空值。它的目的是测试变量是否存在，比如${count:+1}表示变量count存在时返回1（表示true），否则返回空值。
```

例如
```bash
filename=${1:?"filename missing."}

# 1 表示脚本的第一个参数。如果该参数不存在，就退出脚本并报错。
```

**declare**

declare 命令可以声明一些特殊类型的变量，为变量设置一些限制，比如声明只读类型的变量和整数类型的变量。

declare 命令如果用在函数中，声明的变量只在函数内部有效，等同于 local 命令。不带任何参数时，declare 命令输出当前环境的所有变量，包括函数在内，等同于不带有任何参数的 set 命令。

```
declare -i aaaaaa=1 bbbbbb=2
declare -i result
result=aaaaaa+bbbbbb
echo $result
```

**readonly**

readonly 命令等同于 declare -r，用来声明只读变量，不能改变变量值，也不能 unset 变量。

```bash
-f	# 声明的变量为函数名。
-p	# 打印出所有的只读变量。
-a	# 声明的变量为数组
```

```bash
readonly foo=1
foo=2
echo $?
```

---

## 符号

**基本符号**
```bash
<				# 重定向输入
>				# 重定向输出
>>				# 末尾添加
&				# 与
|				# 管道符
```

```bash
*				# 匹配任意多个字符
	*.txt       	# 匹配全部后缀为 .txt 的文件

# * 这个通配符代表不以点 “.” 开头的所有文件。以 “.” 开头的文件默认属于 Linux 下的隐藏文件。
# 因此，不会删除目录下以 . 开头的隐藏文件，以及 . 和 .. 两个目录。但是在递归操作时，会递归地删除子目录下除了 . 和 .. 目录之外的所以文件和子目录——无论是否以 . 开头——因为递归操作不是由 Bash 等 shell 进行通配展开的。
# 至于为什么不在删除目录下的内容时也将 . 和 .. 一视同仁？因为自从 1979 年 rm 命令开始有删除目录的能力时，就专门避开了这两个特殊目录。

**				# 匹配任意级别目录(bash 4.0以上版本支持，shopt -s globstar)
	/etc/**/*.conf  # 查找 /etc/ 下所有 .conf 文件
?				# 匹配单个字符
	file?.log		# 匹配 file1.log, file2.log, ...
[]				# 匹配一个单字符范围,如[a-z],[0-9]
	[a-z]*.log  	# 匹配 a-z 开头的 .log 文件

# 反斜杠(\)或引号(', ")都会使通配符失效。
```

- grep
	```bash
	# 文本搜索工具,它能使用正则表达式搜索文本,并把匹配的行打印出来.

	# 选项释义
		# -a ： 将 binary 文件以 text 文件的方式进行搜寻
		# -c ： 计算找到个数
		# -i ： 忽略大小写
		# -n ： 输出行号
		# -v ： 反向选择，亦即显示出没有 搜寻字符串 内容的那一行
		# --color=auto ：找到的关键字加颜色显示

	# e.g.
	grep John /etc/passwd		# 在 /etc/passwd 文件中查找文本 John 并显示所有匹配的行
	grep -i john /etc/passwd	# 忽略大小写
	grep -ri john /home/users 	# 递归搜索目录中的匹配文本
	```

- awk
	```bash
	# 可以根据字段的某些条件进行匹配，例如匹配字段小于某个值的那一行数据。
	awk '条件类型 1 {动作 1} 条件类型 2 {动作 2} ...' filename
	# awk 每次处理一行，处理的最小单位是字段，每个字段的命名方式为：\$n，n 为字段号，从 1 开始，\$0 表示一整行。

	# e.g.
	cat /proc/cpuinfo | grep name | awk '{print $3}'		# 查询 cpuinfo 信息合并输入第 3 列
	```

- cut
	```bash
	# 剪切命令可用于仅显示文本文件或其他命令输出中的特定列

	# e.g.
	cut -d: -f 1,3 names.txt	# 显示冒号分隔文件中的第一和第三字段
	cut -c 1-8 names.txt		# 仅显示文件中每行的前 8 个字符
	cut -d: -f1 /etc/passwd		# 显示系统中所有用户的 UNIX 登录名
	```

- uniq
	```bash
	# 用于报告或忽略文件中的重复行

	# e.g.
	sort namesd.txt | uniq		# 使用 uniq 命令从文件中删除重复项
	sort namesd.txt | uniq -c	# 使用 Uniq 显示重复的行数
	sort namesd.txt | uniq -cd	# 使用 Uniq 仅显示重复的行
	grep name /proc/cpuinfo | uniq	# 查询 cpuinfo 信息合并成一条
	cat /proc/cpuinfo | grep name |cut -f2 -d ":" | uniq		# 查询 cpuinfo 信息合并成一条并只输出: 后的内容
	```

- sort
	```bash
	# 将文件进行排序,并将排序结果标准输出.

	# e.g.
	sort names.txt		# 以升序对文本文件进行排序
	sort -r names.txt	# 以降序对文本文件进行排序
	sort -t: -k 3n /etc/passwd | more	# 按第 3 个字段（数字用户 ID）对 passwd 文件进行排序
	sort -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n /etc/hosts	# 按 IP 地址对 /etc/hosts 文件进行排序
	```

- xargs
	```bash
	# 接收命令的输出并将其作为另一个命令的参数传递

	# e.g.
	find ~ -name '*.tmp' -print0 | xargs -0 rm -f	# 尝试使用 rm 删除所有 tmp 文件
	find /etc -name "*.conf" | xargs ls -l			# 获取 /etc/ 下所有 *.conf 文件的列表
	cat url-list.txt | xargs wget -c				# 如果需要从文件读取要下载的 URL 列表
	find / -name *.jpg -type f -print | xargs tar -cvzf images.tar.gz	# 找出所有 jpg 图像并将其存档
	ls *.jpg | xargs -n1 -i cp {} /external-hard-drive/directory 		# 将所有图像复制到外部硬盘驱动器
	```

- tee
	```bash
	# tee 命令用于存储和查看（同时）任何其他命令的输出,默认下输出将覆盖原文件

	# e.g.
	ls | tee file 				# 将输出既写入屏幕（stdout），又写入文件
	ls | tee file1 file2 file3	# 输出写入多个文件
	ls | tee -a file			# 追加而不是覆盖
	crontab -l | tee crontab-backup.txt | sed 's/old/new/' | crontab -	# 对 crontab 条目进行备份，并将 crontab 条目作为 sed 命令的输入，由 sed 命令进行替换。替换后，它将被添加为一个新的cron作业。
	```

- paste
	```bash
	# paste 可以将两个不同的文件合并到一个多列文件中。
	paste aaa.txt bbb.txt
	```

- fold
	```bash
	# 限制输出的长度
	cat /etc/passwd | fold -w 16
	```

---

## 会话

**清屏**
```bash
clear		# 刷新屏幕，本质上只是让终端显示页向后翻了一页，如果向上滚动屏幕还可以看到之前的操作信息
reset		# 完全刷新终端屏幕
printf "\033c"
```

**查看用户信息**
```bash
id
who			# 显示目前登录系统的用户信息.
w			# 显示已经登录系统的用户列表,并显示用户正在执行的指令.
last		# 显示用户最近登录信息
```

**快捷键**
```bash
Ctrl+S		# 终止显示的信号/指令
Ctrl+Q		# 恢复显示的信号/指令
Ctrl+R		# 搜索历史命令
Ctrl+P		# 切换上一个命令
alt+F1-F6	# 切换虚拟控制台
Alt+F7		# 图形界面
Ctrl+L		# 清除命令
```

**screen**

screen 是一个会话管理软件，用户可以通过该软件同时连接多个本地或远程的命令行会话，并在其间自由切换。
```bash
# RedHat 系安装
	yum -y install screen

# Debian 系安装
	apt-get -y install screen

screen -S <name>
screen -ls
screen -r <name>	# 重新连接
ctrl+d				# 终止会话
```

### 历史记录

**history 记录的行数**
```bash
echo $HISTSIZE
```

**修改默认记录的行数**
```
vim /etc/profile

HISTSIZE=1000
```

**查看历史记录**
```bash
history

cat ~/.bash_history
cat ~/.nano_history
cat ~/.atftp_history
cat ~/.mysql_history
cat ~/.php_history
```

**清除历史记录**
```bash
history -c
```

**centos 下更改历史记录文件名**
```bash
vim ~/.bash_profile

HISTFILE=/root/.his
```

**Ubuntu 下配置不记录 history 方法**
```bash
vim ~/.bashrc

# 可选配置如下：
HISTCONTROL=ignoredups		# 忽略连续重复的命令。
HISTCONTROL=ignorespace		# 忽略以空白字符开头的命令。
HISTCONTROL=ignoreboth		# 同时忽略以上两种。
HISTCONTROL=erasedups		# 忽略所有历史命令中的重复命令。
```

**查看是否配置历史命令信息**
```bash
cat /etc/profile
cat ~/.bash_profile
cat ~/.bashrc
```

---

## 文件和目录

**目录**

```bash
cd	# 切换工作目录
~	# 表示 home 目录
.	# 表示当前目录
..	# 表示上级目录
-	# 表示上一次目录

/	# 表示根目录
	root	# 超级用户目录,存放 root 用户相关文件
	home	# 存放普通用户相关文件
	bin		# (binaries)存放二进制可执行文件
	sbin	# (super user binaries)存放二进制可执行文件,只有 root 才能访问
	mnt		# (mount)系统管理员安装临时文件系统的安装点
	etc		# (etcetera)存放系统配置文件
	var		# (variable)用于存放运行时需要改变数据的文件
	boot	# 存放用于系统引导时使用的各种文件
	usr		# (unix shared resources)用于存放共享的系统资源
	dev		# (devices)用于存放设备文件
	lib		# (library)存放跟文件系统中的程序运行所需要的共享库及内核模块
	tmp		# (temporary)用于存放各种临时文件
```
更多内容参考笔记 [文件](./笔记/文件.md#目录结构)

### 查看

**目录、文件信息**
```bash
ls			# 查看目录下文件
	ls -a						# 查看目录隐藏文件
	ls -lah						# 查看的内容更新详细

pwd			# 以绝对路径的方式显示用户当前工作目录
	pwd -P						# 目录链接时,显示实际路径而非 link 路径

wc			# wc 将计算指定文件的行数、字数，以及字节数
du			# 查看文件大小
stat		# 查看文件属性
file		# 探测给定文件的类型
	file xxx.log
```

**文件内容**
```bash
cat			# 连接文件并打印到标准输出设备上
	cat -n						# 带行号读
	cat -b						# 带行号,越过空白行

more		# 一个基于 vi 编辑器文本过滤器，它以全屏幕的方式按页显示文本文件的内容
	more +10 a.txt				# 从第10行读起
	more -10 f1.txt				# 每次显示10行读取文件

head		# 用于显示文件的开头的内容,默认情况下显示文件的头10行内容
	head -n 1 a.txt				# 读文件第一行
	head -5 /etc/passwd			# 读取文件前5行

tail		# 用于显示文件的尾部的内容,默认情况下显示文件的尾部10行内容
	tail -10 /etc/passwd		# 读取文件后10行

sed			# 一种流编辑器，它是文本处理中非常中的工具，能够完美的配合正则表达式使用
	sed -n '5,10p' /etc/passwd	# 读取文件第5-10行
	sed '/^$/d' test.txt		# 删除文件空行

tac			# 是 cat 的反向操作，从最后一行开始打印
less		# 允许用户向前或向后浏览文件

nl			# 用来在 linux 系统中打印文件中行号
	nl /etc/passwd
	nl -b a /etc/passwd		# 空行也加上行号
```

**二进制相关**
```bash
objdump		# 显示目标文件的信息,可以通过参数控制要显示的内容
	objdump -p 					# 显示文件头内容
	objdump -T					# 查看动态符号表的内容

od			# 以字符或者十六进制的形式显示二进制文件
	od -c test.txt
	od -b test.txt

strings		# 在对象文件或二进制文件中查找可打印的字符串
	strings start.bin | grep -a "pass"
	strings .* | grep -a "root"
	strings -o start.bin 		# 获取所有 ASCII 字符偏移

ldd			# 可以显示程序或者共享库所需的共享库
	ldd /bin/cat

nm			# 显示目标文件的符号
	# -A：每个符号前显示文件名；
	# -D：显示动态符号；
	# -g：仅显示外部符号；
	# -r：反序显示符号表。
```

### 创建

- touch
	```bash
	# 创建文件
	touch -r test1.txt test2.txt 		# 更新 test2.txt 时间戳与 test1.txt 时间戳相同
	touch -c -t 202510191820 a.txt 		# 更改时间
	```

- truncate
	```bash
	# 创建指定大小文件
	truncate -s 100k aaa.txt

- mkdir
	```bash
	# 创建文件夹
	mkdir -p /test						# 若 test 目录原本不存在，则建立一个
	mkdir -p /mnt/aaa/aaa/aaa 			# 创建指定路径一系列文件夹
	mkdir -m 777 /test					# 创建时指定权限
	```

### 删除

- rm
	```bash
	# 删除文件和目录的命令
	rm [options] <filename>

	# 选项释义
	-r		# 递归，对目录及其下的内容进行递归操作
	-f		# 强制删除,无需确认操作
	-i		# 确认
	-v		# 详细显示进行的步骤
	```

	rm 命令有一对专门针对根目录的选项 `--preserve-root` 和 `--no-preserve-root`
	- `--preserve-root`：保护根目录，这是默认行为。
	- `--no-preserve-root`：不保护根目录。
	这对选项是后来添加到 rm 命令的。可能几乎每个系统管理员都犯过操作错误，而这其中删除过根目录的比比皆是

	那为什么还会专门出现 --no-preserve-root 选项呢？这可能主要是出于 UNIX 哲学的考虑，给予你想要的一切权力，犯傻是你的事情，而不是操作系统的事情。万一，你真的想删除根目录下的所有文件呢？

- rmdir
	```bash
	# 删除空目录
	rmdir
	```

**删除巨大文件的技巧**
```bash
echo "" >  bigfile
rm bigfile

> access.log			# 通过重定向到 Null 来清空文件内容
: > access.log
true > access.log
cat /dev/null > access.log
```

### 搜索

**搜索命令**
```bash
which <Command>		# 指令搜索,查找并显示给定命令的绝对路径
```

**搜索文件**

- find
	```bash
	# 用于基于多种条件在UNIX文件系统中查找文件的常用命令

	# e.g.
	find / -name conf*	# 查找根目录及子目录下所有 conf 文件
	find / -name site-packages -d	# 查找 site-packages 目录
	find . -mtime -2				# 查找最近两天在当前目录下修改过的所有文件
	find / -type f -size + 100M		# 列出系统中大于100MB的所有文件
	```

- locate
	```bash
	# 查找文件或目录
	locate <File>
	```

- fd
	```bash
	# 文件查找工具
	wget https://github.com/sharkdp/fd/releases/download/v7.3.0/fd-musl_7.3.0_amd64.deb
	dpkg -i fd-musl_7.3.0_amd64.deb
	fd <File>
	```

- fzf
	```bash
	git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
	~/.fzf/install
	fzf
	```

**找出重复文件**

- jdupes
	- https://github.com/jbruchon/jdupes
	```bash
	git clone https://github.com/jbruchon/jdupes
	cd jdupes
	make
	./jdupes -r /home	# 递归扫描目录,包括子目录
	./jdupes -dr /home	# 挨个确认删除
	```

- rdfind
	```bash
	yum install -y epel-release && yum install -y rdfind
	# 或
	apt-get install -y rdfind

	rdfind -dryrun true /home			# 结果会保存在 results.txt 文件中
	rdfind -deleteduplicates true /home	# 删除
	```

- fdupes
	```bash
	yum install -y epel-release && yum install -y fdupes
	# 或
	apt install -y fdupes

	fdupes /home
	fdupes -r /			# 递归扫描目录,包括子目录
	fdupes -rd /		# 删除重复内容
	```

- fslint
	```bash
	# fslint 命令可以被特地用来寻找重复文件
	fslint .
	```

**lsof**

> 可以使用 lsof 命令来了解某人是否正在使用文件

```bash
lsof /dev/null			# Linux 中所有已打开文件的列表
lsof -u root			# root 打开的文件列表
lsof -i TCP:22			# 找出进程监听端口
```

### 修改

**复制**
```bash
cp <源文件> <目标文件/目标路径>			# 复制
	cp -r <源目录> <目标目录/目标路径>	# 带目录复制
```

**移动**
```bash
mv <源文件> <目标文件/目标路径>			# 对文件或目录重命名,或移动
```

**编辑**
```bash
vi 									# 编辑器
nano								# 编辑器
gedit								# 图形化的编辑器
```

**Vim**
- **常用操作**
	```bash
	Normal 模式下 i 进入 insert 模式
	:wq 					# 存盘+退出
	dd  					# 删除当前行,并存入剪切板
	p   					# 粘贴
	:q! 					# 强制退出
	:wq!					# 强制保存退出
	:w !sudo tee %  		# 无 root 权限,保存编辑的文件
	:saveas <path/to/file>  # 另存为
	按下 / 即可进入查找模式,输入要查找的字符串并按下回车. Vim 会跳转到第一个匹配.按下 n 查找下一个,按下 N 查找上一个.
	:%s/foo/bar 			# 代表替换 foo 为 bar
	insert 模式按 ESC 键,返回 Normal 模式

	vim -r xxx.swp			# 恢复上次异常退出的文件
	```
- **更多操作**
	- [Vim](./Power-Linux.md#Vim)

**objcopy**

objcopy 用于将 object 的部分或全部内容拷贝到另一个 object，从而可以实现格式的变换。

objcopy 可用用于将文件转换成 S-record 格式或者 raw 二进制格式。

```bash
objcopy -O srec main main.srec								# 将文件转换成 S-record 格式
objcopy -O binary main main.bin    							# 将文件转换成 rawbinary 格式
objcopy -I binary -O binary --reverse-bytes=4 1.out 2.out	# 转换为小端序
```

**tr**

tr 命令将文件转换为全大写
```bash
cat employee.txt

100 Jason Smith
200 John Doe
300 Sanjay Gupta
400 Ashok Sharma

tr a-z A-Z < employee.txt

100 JASON SMITH
200 JOHN DOE
300 SANJAY GUPTA
400 ASHOK SHARMA
```

**joe**

`这个目前比较少见了`

```shell
joe test.txt			# 编辑文件

Ctrl-K Q				# 退出
Ctrl-K H				# 查看帮助
```

**split**

`对文件进行分割`

```bash
# 按文件大小切割
split -b 2M test 		# 把 test 文件分割成若干个小文件，每个文件大小为 2M

# 按文件行数切割
split -l 100 test out_	# 把 numfile 文件切割成若干文件，每个文件 100 行, 并且新生成的文件名字前缀为 "out_"

# 按文件数量切割
split -d -n 5 test 		# 是把 test 文件切割成 5 个小文件
```

**fallocate**

```bash
fallocate -l 10G allocatefile	# 创建一个 10G 大小的文件
```

**truncate**

`缩小或者扩展文件至指定大小`

```bash
truncate -s 1G testfile
```

### 比较

- diff
	```bash
	diff [options] <file1> <file2>
		e.g. : diff -w name_list.txt name_list_new.txt
	```

- vimdiff
	```bash
	vimdiff <变动前的文件> <变动后的文件>
	```

- comm
	```bash
	comm [options] ... FILE1 FILE2

	# e.g.
	comm -12 1.txt 2.txt	# 查看两个文件共有的部分
	comm -23 1.txt 2.txt	# 仅查看 file1 中有,file2 中没有的行
	comm -13 1.txt 2.txt	# 仅查看 file2 中有,file1 中没有的行
	```

### 链接

**inode**

inode 是指在许多“类 Unix 文件系统”中的一种数据结构。每个 inode 保存了文件系统中的一个文件系统对象（包括文件、目录、设备文件、socket、管道, 等等）的元信息数据，但不包括数据内容或者文件名。

文件系统中每个“文件系统对象”对应一个“inode”数据，并用一个整数值来辨识。这个整数常被称为 inode 号码（“i-number”或“inode number”）。由于文件系统的 inode 表的存储位置、总条目数量都是固定的，因此可以用 inode 号码去索引查找 inode 表。

简而言之
- inode 存储的是文件的元数据
- inode 是文件在磁盘上的索引编号
- inode 是文件的唯一标示符(主键), 而非文件名

Linux 系统中，显示文件的 inode 使用 `ls -i`，使用 `df -i` 可以显示当前挂载列表中 inode 使用情况

**软链接**

符号链接文件保存着源文件所在的绝对路径，在读取时会定位到源文件上，可以理解为 Windows 的快捷方式。

软连接是一类特殊的文件， 其包含有一条以绝对路径或者相对路径的形式指向其它文件或者目录的引用。 符号链接最早在 4.2BSD 版本中出现（1983年）。今天 POSIX 操作系统标准、大多数类 Unix 系统、Windows Vista、Windows 7 都支持符号链接。Windows 2000 与 Windows XP 在某种程度上也支持符号链接。

符号链接的操作是透明的：对符号链接文件进行读写的程序会表现得直接对目标文件进行操作。某些需要特别处理符号链接的程序（如备份程序）可能会识别并直接对其进行操作。

一个符号链接文件仅包含有一个文本字符串，其被操作系统解释为一条指向另一个文件或者目录的路径。它是一个独立文件，其存在并不依赖于目标文件。如果删除一个符号链接，它指向的目标文件不受影响。如果目标文件被移动、重命名或者删除，任何指向它的符号链接仍然存在，但是它们将会指向一个不复存在的文件。这种情况被有时被称为被遗弃。

在 Linux 中，创建软连接的方法是使用 `ln -s`
```bash
ln -s /etc/bashrc /tmp/bashrc
```
查看软连接的指向可以用 `ls -l`

删除软连接就如同删除普通文件一样，使用 `rm symlink` 即可。

- 报错 : Too many levels of symbolic links
	- 在使用 ln -s 命令时，使用绝对路径取代相对路径

**硬链接**

它和普通文件类似，实体链接文件的 inode 都指向源文件所在的 block 上，也就是说读取文件直接从源文件的 block 上读取。

指通过索引节点来进行连接。在 Linux 的文件系统中，保存在磁盘分区中的文件不管是什么类型都给它分配一个编号，称为索引节点号(Inode Index)。在 Linux 中，多个文件名指向同一索引节点是存在的。一般这种连接就是硬连接。硬连接的作用是允许一个文件拥有多个有效路径名，这样用户就可以建立硬连接到重要文件，以防止“误删”的功能。其原因如上所述，因为对应该目录的索引节点有一个以上的连接。只删除一个连接并不影响索引节点本身和其它的连接，只有当最后一个连接被删除后，文件的数据块及目录的连接才会被释放。也就是说，文件真正删除的条件是与之相关的所有硬连接文件均被删除。

删除任意一个条目，文件还是存在，只要引用数量不为 0。

在 Linux 中，创建硬链接的方法是 ln:
```bash
ln file1 file2
```

创建硬链接之后，源文件和目标文件将拥有完全相同的 inode 编号，权限，内容等。

硬链接的几个限制:
- 硬链接创建时要求源文件必须存在
- 不允许给目录创建硬链接(注意是不能通过 ln 的方式)
- 只有在同一文件系统才能创建硬链接

### 压缩备份

- .tar
	```bash
	# 注:tar 是打包,不是压缩!
	tar -xvf FileName.tar						# 解包
	tar -cvf FileName.tar DirName				# 打包
	tar -tvf FileName.tar.gz					# 不解压查看内容
	tar -xvf FileName.tar.gz a.txt  			# 解压指定内容
	tar -uvf test.tar.bz2 test					# 更新一个内容
	tar -rvf test.tar.bz2 test2 				# 追加一个内容
	```

- .tar.gz 和 .tgz
	```bash
	tar -zxvf FileName.tar.gz					# 解压
	tar -zcvf FileName.tar.gz DirName			# 压缩
	```

- .tar.xz
	```bash
	tar -xvJf FileName.tar.xz					# 解压
	```

- .tar.Z
	```bash
	tar -Zxvf FileName.tar.Z					# 解压
	tar -Zcvf FileName.tar.Z DirName			# 压缩
	```

- .tar.bz
	```bash
	tar -jxvf FileName.tar.bz					# 解压
	tar -jcvf FileName.tar.bz DirName			# 压缩
	```

- .tar.bz2
	```bash
	tar -jxvf test.tar.bz2						# 解压
	```

- .gz
	```bash
	gunzip FileName.gz							# 解压1
	gzip -dv FileName.gz						# 解压2
	gzip FileName								# 压缩
	gzip -l FileName.gz 						# 不解压查看内容
	zcat FileName.gz 							# 不解压查看内容
	```

- .bz2
	```bash
	bzip2 -dv FileName.bz2						# 解压1
	bunzip2 FileName.bz2						# 解压2
	bzip2 -zv FileName							# 压缩
	bzcat FileName.bz2							# 不解压查看内容
	```

- .Z
	```bash
	uncompress FileName.Z						# 解压
	compress FileName							# 压缩
	compress -rvf /home/abc/					# 强制压缩文件夹
	```

- .zip
	```bash
	unzip FileName.zip							# 解压
	zip FileName.zip DirName					# 压缩
	zip -s 4m myzip.zip --out zip				# 分卷压缩
	cat zip.z* > myzip.zip && unzip myzip.zip	# zip 分卷解压缩
	```

- .rar
	```bash
	rar x FileName.rar							# 解压
	rar a FileName.rar DirName					# 压缩
	```

- .lha
	```bash
	lha -e FileName.lha							# 解压
	lha -a FileName.lha FileName				# 压缩
	```

- .rpm
	```bash
	rpm2cpio FileName.rpm | cpio -div			# 解包
	```

- .deb
	```bash
	ar -p FileName.deb data.tar.gz | tar zxf -	# 解包
	```

- asar
	```bash
	npm install --engine-strict asar
	asar e xxx.asar xxx							# 解包
	```

**7z**
```bash
apt install -y p7zip

7z a -t7z -r manager.7z /home/manager/*		# 压缩文件
	# a 代表添加文件／文件夹到压缩包
	# -t 是指定压缩类型 一般我们定为7z
	# -r 表示递归所有的子文件夹，manager.7z 是压缩好后的压缩包名，/home/manager/* 是要压缩的目录，＊是表示该目录下所有的文件。
7z x manager.7z -r -o /home/xx				# 解压文件
	# x 代表解压缩文件，并且是按原始目录解压（还有个参数 e 也是解压缩文件，但其会将所有文件都解压到根下，而不是自己原有的文件夹下）manager.7z 是压缩文件，这里大家要换成自己的。如果不在当前目录下要带上完整的目录
	# -r 表示递归所有的子文件夹
	# -o 是指定解压到的目录，这里大家要注意-o后是没有空格的直接接目录
```

**pigz**

pigz 命令可以用来解压缩文件，最重要的是支持多线程并行处理
```bash
tar -cvf - dir1 dir2 dir3 | pigz -p 8 > xxx.tgz		# 结合 tar 使用, 压缩命令
pigz -p 8 -d xxx.tgz		# 解压命令
tar -xzvf xxx.tgz			# 如果是 gzip 格式，也支持用 tar 解压
```

---

# 网络管理
## 查看网络信息

**主机名**
```bash
hostname				# 查看本机的hostname
```

**IP 地址**
```bash
ifconfig				# ifconfig 命令已经被弃用，不应该使用
ip a					# 显示网络设备的运行状态
hostname -I
netstat -a
cat /proc/net/fib_trie
cat /etc/sysconfig/network
sudo -v
```

**测试连通性**

- ping
	```bash
	ping [options] <target>
		e.g. : ping 127.0.0.1

	# -d 使用 Socket 的 SO_DEBUG 功能。
	# -f 极限检测。大量且快速地送网络封包给一台机器，看它的回应。
	# -n 只输出数值。
	# -q 不显示任何传送封包的信息，只显示最后的结果。
	# -r 忽略普通的 Routing Table，直接将数据包送到远端主机上。通常是查看本机的网络接口是否有问题。
	# -R 记录路由过程。
	# -v 详细显示指令的执行过程。
	# -c 数目：在发送指定数目的包后停止。
	# -i 秒数：设定间隔几秒送一个网络封包给一台机器，预设值是一秒送一次。
	# -I 网络界面：使用指定的网络界面送出数据包。
	# -l 前置载入：设置在送出要求信息之前，先行发出的数据包。
	# -p 范本样式：设置填满数据包的范本样式。
	# -s 字节数：指定发送的数据字节数，预设值是 56，加上 8 字节的 ICMP 头，一共是 64ICMP 数据字节。
	# -t 存活数值：设置存活数值 TTL 的大小。
	```

- traceroute
	```bash
	traceroute [options] <target>
		e.g. : traceroute www.baidu.com

	# -d 使用 Socket 层级的排错功能
	# -f 设置第一个检测数据包的存活数值 TTL 的大小。
	# -F 设置勿离断位。
	# -g 设置来源路由网关，最多可设置 8 个。
	# -i 使用指定的网络界面送出数据包。
	# -I 使用 ICMP 回应取代 UDP 资料信息。
	# -m 设置检测数据包的最大存活数值 TTL 的大小。
	# -n 直接使用 IP 地址而非主机名称。
	# -p 设置 UDP 传输协议的通信端口。
	# -r 忽略普通的 Routing Table，直接将数据包送到远端主机上。
	# -s 设置本地主机送出数据包的 IP 地址。
	# -t 设置检测数据包的 TOS 数值。
	# -v 详细显示指令的执行过程。
	# -w 设置等待远端主机回报的时间。
	# -x 开启或关闭数据包的正确性检验。
	```

**端口**
```bash
getent services 		# 查看所有服务的默认端口名称和端口号
ss -tnlp				# 获取 socket 统计信息
lsof -i					# 列出当前系统打开文件
netstat -antup
netstat -antpx
netstat -tulpn
fuser -v 22/tcp			# 查询进程使用的文件和网络套接字
```

**路由表**
```bash
route					# 显示/操作IP路由表
ip route				# 显示/操纵路由，设备，策略路由和隧道
ip neigh				# 显示邻居表
```

**DNS**
```bash
cat /etc/resolv.conf	# 查看 DNS 解析配置文件
```

**arp 条目**
```bash
arp -e					# 以 Linux 的显示风格显示 arp 缓冲区中的条目
```

---

## 配置

**修改主机名**
```bash
vim /etc/hosts

127.0.0.1  test localhost		# 修改 localhost.localdomain 为 test,shutdown -r now 重启使修改生效
```
或
```bash
hostnamectl set-hostname test	# 修改 hostname 立即生效且重启也生效
```

**修改 DNS**

- 通用(一次性,重启失效)
	```vim
	vim /etc/resolv.conf

	nameserver 8.8.8.8
	```

- 通用(长期)
	```vim
	apt install -y resolvconf

	vim /etc/resolvconf/resolv.conf.d/head

	nameserver 8.8.8.8
	```
	```
	resolvconf -u
	```

**修改 IP**
 - Ubuntu
	```bash
	vim /etc/network/interfaces

	auto enp7s0	 				# 使用的网络接口
	iface enp7s0 inet static	# 静态 ip 设置
	address 10.0.208.222
	netmask 255.255.240.0
	gateway 10.0.208.1
	```
	```bash
	ip addr flush enp7s0
	systemctl restart networking.service

	systemctl restart NetworkManager
	systemctl enable NetworkManager
	```

- ubuntu 17.10 引入的新方式 netplan

	网卡信息配置在 /etc/netplan/01-network-manager-all.yaml 文件中，如果这个 yaml 文件不存在，可以使用以下的命令创建出来。
	```bash
	sudo netplan generate
	```
	创建出来的名字可能略有不同，但是 /etc/netplan/ 这个目录下面所有的 yaml 文件都可以生效。
	```bash
	vim /etc/netplan/01-network-manager-all.yaml
	```
	```yaml
		network:
			ethernets:
				ens33:
					addresses:
						- 192.168.2.222/24
					gateway4: 192.168.1.1
					nameservers:
							addresses:
								- 8.8.8.8
			version: 2
	```

	```bash
	netplan apply	# 使配置生效
	```

	> 注意 : ip 配置信息要使用 yaml 语法格式

- Centos
	```bash
	vim /etc/sysconfig/network-scripts/ifcfg-eth0	# 配置文件名称和网卡对应,可使用 ip a 查看所有网卡名称

	HOSTNAME=test
	onboot=yes			# 激活网络
	HWADDR=00:0C:29:F1:2E:7B
	BOOTPROTO=static	# 使用静态 IP,而不是由 DHCP 分配 IP
	# BOOTPROTO=dhcp 这个是 DHCP 的配置,如果配这个那下面的就不需要配置了
	IPADDR=172.16.102.61
	PREFIX=24
	GATEWAY=172.16.102.254
	DNS1=223.5.5.5
	```
	```bash
	service network restart
	systemctl restart NetworkManager	# 重启网络管理
	systemctl enable NetworkManager
	```

- Arch
	```bash
	ifconfig -a			# 查看下可用的网卡
	ifconfig eth0 up	# 启动网卡
	dhcpcd  eth0		# 获取 ip
	```
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
	```bash
	/etc/rc.d/network restart
	```

**配置 DHCP**
- Ubuntu
	```bash
	iface enp7s0 inet dhcp		# dhcp 配置
	```

**ethtool**

`ethool 是一个实用的工具，用来给系统管理员以大量的控制网络接口的操作。`
```bash
ethtool eth0		# 显示关于该网卡的基本设置
ethtool -i eth0		# 查询该网卡的驱动相关信息
ethtool -d eth0		# 查询 eth0 网口注册性信息
ethtool -S eth0		# 查询网口收发包统计
ethtool -s eth0 speed 100 autoneg off	# -s 选项可以修改网卡配置
# 以上命令将 eth0 网卡的自协商传输模式关闭，传输速率改为 100Mb/s。命令执行后需要重新启动 eth0 网卡：
ifup eth0

# 通过以上命令修改网卡配置，在机器重启后配置将不再生效
```

**设置包转发**

在 CentOS 中默认的内核配置已经包含了路由功能，但默认并没有在系统启动时启用此功能。开启 Linux 的路由功能可以通过调整内核的网络参数来实现。要配置和调整内核参数可以使用 sysctl 命令
```bash
sysctl -w net.ipv4.ip_forward=1
```

这样设置之后，当前系统就能实现包转发，但下次启动计算机时将失效。为了使在下次启动计算机时仍然有效，需要将下面的行写入配置文件 /etc/sysctl.conf
```diff
vim /etc/sysctl.conf

++ net.ipv4.ip_forward = 1
```

**修改路由**
```bash
route	# 查看路由表

# 添加到主机的路由
route add -host 192.168.1.2 dev eth0
route add -host 10.20.30.148 gw 10.20.30.40

# 添加到网络的路由
route add -net 10.20.30.40 netmask 255.255.255.248 eth0
route add -net 10.20.30.48 netmask 255.255.255.248 gw 10.20.30.41
route add -net 192.168.1.0/24 eth1

# 添加默认路由
route add default gw 192.168.1.1

# 删除路由
route del -host 192.168.1.2 dev eth0:0
route del -host 10.20.30.148 gw 10.20.30.40
route del -net 192.168.1.0/24 eth1
route del default gw 192.168.1.1
```

---

## 抓包

**tcpdump**
```bash
# Debian安装
apt install -y tcpdump

# Redhat安装
yum install -y tcpdump

# 当我们在没用任何选项的情况下运行 tcpdump 命令时,它将捕获所有接口上的数据包
tcpdump -i {接口名}	# 指定接口

# 假设我们想从特定接口(如 enp0s3)捕获 12 个数据包
tcpdump -i enp0s3 -c 12

# 使用 -D 选项显示 tcpdump 命令的所有可用接口
tcpdump -D

# 默认情况下,在 tcpdump 命令输出中,不显示可读性好的时间戳,如果你想将可读性好的时间戳与每个捕获的数据包相关联,那么使用 -tttt 选项,示例如下所示
tcpdump -i enp0s3 -c 12 -tttt

# 使用 tcpdump 命令中的 -w 选项将捕获的 TCP/IP 数据包保存到一个文件中
tcpdump -i enp0s3 -c 12 -tttt -w test.pcap	# 注意:文件扩展名必须为 .pcap

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
scp /home/space/music/1.mp3 root@192.168.1.1:/home/root/others/music	# 本地文件复制到远程
scp root@192.168.1.1:/home/root/others/music /home/space/music/1.mp3	# 远程文件复制到本地

scp -r 		# 文件夹传输
	scp -r /home/space/music/ root@192.168.1.1:/home/root/others/	# 将本地 music 目录复制到远程 others 目录下
```

**lrzsz**
```bash
yum install -y lrzsz
sz xxx		# 将选定的文件发送(send)到本地机器
rz 			# 运行该命令会弹出一个文件选择窗口,从本地选择文件上传到服务器(receive),需要远程软件支持
```

**wget**
```bash
# 用于下载文件的工具
wget [options] [target]

# e.g.
wget example.com/big.file.iso								# 下载目标文件
wget -O filename.html example.com							# 另行命名
wget -c example.com/big.file.iso							# 恢复之前的下载
wget -i list.txt											# 下载文件中的 url
wget -r example.com											# 递归下载
wget --no-check-certificate									# 不检查 https 证书
wget ftp://user:password@host:/path-to-file/file.txt		# ftp 下载
wget -br ftp://user:password@ftp-host:/path-for-download/	# 递归下载 ftp 目录下文件
```

**curl**
```bash
curl -o wordpress.zip https://wordpress.org/latest.zip		# 另行命名
curl -C - O https://wordpress.org/latest.zip				# 恢复之前的下载
```

**Aria2**
```bash
aria2c http://releases.ubuntu.com/18.10/ubuntu-18.10-desktop-amd64.iso.torrent		# 下载磁力链接
aria2c -i downloadurls.txt									# 下载文件中的 url
aria2c -c http://releases.ubuntu.com/18.10/ubuntu-18.10-desktop-amd64.iso.torrent	# 恢复之前的下载
aria2c -max-download-limit=100K http://releases.ubuntu.com/disco/ubuntu-19.04-desktop-amd64.iso.torrent		# 设置最大速度限制
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

### 远程访问

**ssh**
```bash
ssh [options] <target>
	e.g. : ssh 127.0.0.1

	ssh -V	# 识别 SSH 客户端版本
	ssh-v	# 调试 ssh 会话
```

---

## Firewall
### Firewalld

```bash
firewall-cmd --zone=public --add-port=12345/tcp --permanent		# 开放端口
firewall-cmd --zone=public --add-service=http --permanent		# 开放服务
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" accept' --permanent						# 允许192.168.1.10所有访问所有端口
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="192.168.1.10" port port=22 protocol=tcp reject' --permanent	# 拒绝192.168.1.10所有访问TCP协议的22端口

firewall-cmd --reload			# 重新加载
firewall-cmd --list-services	# 查看防火墙设置
systemctl status firewalld		# 查看服务运行状态
systemctl start firewalld		# 开启服务
systemctl stop firewalld		# 关闭服务
```

**更多配置**

见 [Firewall.md](./实验/Firewall.md)

### Iptables

```bash
iptables-save > /root/firewall_rules.backup		# 先备份一下策略
iptables -A OUTPUT -p tcp -d bigmart.com -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j DROP
iptables -A INPUT -p tcp -s 10.0.3.1 --dport 22 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 22 -j DROP

iptables -L			# 查看防火墙规则
iptables-restore </root/firewall_rules.backup	# 恢复规则

# 以下为清除所有策略并允许所有流量通过防火墙。这和你停止防火墙效果一样,生产环境请不要使用
iptables -F  		# 清除防火墙配置
iptables -X
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
```

**更多配置**

见 [Iptables.md](./实验/Iptables.md)

### ufw

**Ubuntu 关闭防火墙**
```bash
ufw disable
```

更多内容见 [ufw.md](./实验/ufw.md)

---

## 软件包管理

**查看安装的程序**
```bash
ls -alh /usr/bin/
ls -alh /sbin/
dpkg -l
rpm -qa
ls -alh /var/cache/apt/archivesO
ls -alh /var/cache/yum/
```

**update-alternatives**
```bash
# update-alternatives 命令用于处理 linux 系统中软件版本的切换,在各个 linux 发行版中均提供了该命令,命令参数略有区别,但大致是一样的.

# 注册软件
	update-alternatives --install <link> <name> <path> <priority>
	update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_91/bin/java 200
	# 以jdk为例,安装了 jdk 以后,先要在 update-alternatives 工具中注册
	update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_111/bin/java 300

	# 第一个参数 --install 表示注册服务名.
	# 第二个参数是注册最终地址,成功后将会把命令在这个固定的目的地址做真实命令的软链,以后管理就是管理这个软链;
	# 第三个参数:服务名,以后管理时以它为关联依据.
	# 第四个参数,被管理的命令绝对路径.
	# 第五个参数,优先级,数字越大优先级越高.

# 查看已注册列表
	update-alternatives --display java

# 修改命令版本
	update-alternatives --config java
	# 输入数字,选择相应版本
	update-alternatives --auto java								# 按照优先级高自动选择
	update-alternatives --set java /opt/jdk1.8.0_91/bin/java	# 直接指定
```

**alien**

alien 是一个用于在各种不同的 Linux 包格式相互转换的工具，其最常见的用法是将 .rpm 转换成 .deb（或者反过来）。
```bash
apt install -y alien			# 安装 alien
alien --to-deb oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm	# 将 oracle Basic Package 从 rpm 转为 deb 格式
```

### apt

> apt 的全称是 Advanced Packaging Tool 是 Linux 系统下的一款安装包管理工具.

**安装软件**
```bash
apt install <package>
apt-get install <package>
```

**更新**
```bash
# 更新源:
apt-get update

# 对软件进行一次整体更新:
apt-get update & apt-get upgrade
apt-get dist-upgrade
apt-get clean

apt-key list		# 查看仓库密钥
```

**无法获得锁 /var/lib/apt/lists/lock - open (11: 资源暂时不可用)**
```bash
rm -rf /var/cache/apt/archives/lock
rm -rf /var/lib/dpkg/lock-frontend
rm -rf /var/lib/dpkg/lock		# 强制解锁占用
rm /var/lib/dpkg/lock
rm /var/lib/apt/lists/lock
```

**E: Unable to correct problems, you have held broken packages.**
```bash
aptitude install <packagename>	# 该工具会想方设法的帮助你安装(提示依赖、其他安装包等等)
```

**dpkg: error: parsing file '/var/lib/dpkg/updates/0023' near line 0**
```bash
rm /var/lib/dpkg/updates/*
apt-get update
```

**debconf: DbDriver "config": /var/cache/debconf/config.dat is locked by another process: Resource temporarily unavailable**
```bash
rm /var/cache/debconf/*.dat
apt --fix-broken install
```

**禁用 Ubuntu 自动更新**
```bash
nano /etc/apt/apt.conf.d/20auto-upgrades

# 如果你不希望系统自动检查更新
    APT::Periodic::Update-Package-Lists "0";
    APT::Periodic::Unattended-Upgrade "0";

# 果你希望它检查更新但不自动安装无人值守的升级
    APT::Periodic::Update-Package-Lists "1";
    APT::Periodic::Unattended-Upgrade "0";
```

**enable the "Universe" repository**
```bash
add-apt-repository universe
apt-get update
```

**Gdebi**

> Gdebi 是一个安装 .deb 软件包的工具.提供了图形化的使用界面

```bash
apt update
apt install -y gdebi
```

#### Ubuntu apt 换源

**20.04**
```bash
tee /etc/apt/sources.list <<-'EOF'
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
EOF
apt update
```

**18.04**
```bash
tee /etc/apt/sources.list <<-'EOF'
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
EOF
apt update
```

**16.04**
```bash
tee /etc/apt/sources.list <<-'EOF'
deb http://mirrors.aliyun.com/ubuntu/ xenial main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security universe
EOF
apt update
```

#### Debain apt 换源

**10**
```bash
tee /etc/apt/sources.list <<-'EOF'
deb http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb http://mirrors.aliyun.com/debian-security buster/updates main
deb-src http://mirrors.aliyun.com/debian-security buster/updates main
deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
EOF
apt update
```

**9**
```bash
tee /etc/apt/sources.list <<-'EOF'
deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ stretch main non-free contrib
deb http://mirrors.aliyun.com/debian-security stretch/updates main
deb-src http://mirrors.aliyun.com/debian-security stretch/updates main
deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib
deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib
EOF
apt update
```

**8**
```bash
tee /etc/apt/sources.list <<-'EOF'
deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib
deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ jessie main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib
EOF
apt update
```

**7**
```bash
tee /etc/apt/sources.list <<-'EOF'
deb http://mirrors.aliyun.com/debian/ wheezy main non-free contrib
deb http://mirrors.aliyun.com/debian/ wheezy-proposed-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ wheezy main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ wheezy-proposed-updates main non-free contrib
EOF
apt update
```

#### Kali apt 换源
```bash
tee /etc/apt/sources.list <<-'EOF'

# 阿里源
deb https://mirrors.aliyun.com/kali kali-rolling main non-free contrib
deb-src https://mirrors.aliyun.com/kali kali-rolling main non-free contrib

# 清华源
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free

# 官方源
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib

EOF
apt update
```

### Binary

```bash
yum install -y make
yum install -y gcc
yum install -y gcc-c++
./configure --prefix=/opt	# 配置,表示安装到 /opt 目录
make						# 编译
make install				# 安装
```

### dnf

> DNF(Dandified Yum)是一种的 RPM 软件包管理器。

**安装 dnf**
```bash
yum install -y epel-release
yum install -y dnf
```

### dpkg

> dpkg 命令是 Debian Linux 系统用来安装、创建和管理软件包的实用工具.

**基本用法**
```bash
dpkg -i xxxxx.deb  			# 安装软件
dpkg -R /usr/local/src		# 安装路径下所有包
dpkg -L xxxx				# 查看软件安装位置

dpkg -l						# 查看已经安装的软件
dpkg -r xxxx				# 卸载
```

### Pacman

> pacman 是 Arch 的包管理工具.

**基本用法**
```bash
pacman -S <package>			# 安装或者升级单个软件包
pacman -R <package>			# 删除单个软件包,保留其全部已经安装的依赖关系
pacman -Ss <package>		# 查询软件包
```

**Pacman 换源**
```bash
pacman-mirrors -i -c China -m rank		# 更新镜像排名
pacman -Syy    							# 更新数据源
pacman -S archlinux-keyring
```

### rpm

> rpm 命令是 RPM 软件包的管理工具.

```bash
rpm -qa 					# 搜索 rpm 包
rpm -qf /etc/my.conf		# 查询文件来自哪个包
rpm -ivh xxxx.rpm			# 安装本地包
rpm -e xxx					# 卸载
rpm -U						# 升级
rpm -V						# 验证
```

### snap

> Snappy 是一个软件部署和软件包管理系统，最早由 Canonical 公司为了 Ubuntu 移动电话操作系统而设计和构建。其包称为“snap”，工具名为“snapd”，可在多种 Linux 发行版上运行，完成发行上游主导的软件部署。该系统的设计面向手机、云、物联网和台式机。

**Centos 下安装 snap**
```bash
yum install -y epel-release
yum install -y snapd
systemctl enable --now snapd.socket
ln -s /var/lib/snapd/snap /snap
```

**kali 下安装 snap**
```bash
apt-get update
apt install -y snapd
systemctl start snapd
export PATH=$PATH:/snap/bin
```

**Ubuntu 下安装 snap**
```bash
apt-get update
apt install -y snapd
```

### yum

> yum 是在 Fedora 和 RedHat 以及 SUSE 中基于 rpm 的软件包管理器.

**基础使用**
```bash
yum update && yum upgrade 	# 更新和升级 rpm 软件包
yum repolist				# 查看仓库列表
yum provides ifconfig 		# 查看哪个包提供 ifconfig

# /var/run/yum.pid 已被锁定,PID 为 xxxx 的另一个程序正在运行.
rm -f /var/run/yum.pid		# 强制解锁占用
```

**配置本地 yum 源**

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
enabled=1					# 开启本地源
```
```bash
yum list    #  看一下包
```

#### 配置 yum 源

**8**
```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-8.repo
```

**7**
```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

**6**
```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-6.repo
```

**刷新 YUM 的缓存状态**
```bash
yum clean all
yum makecache
```

#### 配置 EPEL 源

**RHEL 8**
```bash
yum install -y https://mirrors.aliyun.com/epel/epel-release-latest-8.noarch.rpm
sed -i 's|^#baseurl=https://download.fedoraproject.org/pub|baseurl=https://mirrors.aliyun.com|' /etc/yum.repos.d/epel*
sed -i 's|^metalink|#metalink|' /etc/yum.repos.d/epel*
```

**RHEL 7**
```bash
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
```

**RHEL 6**
```bash
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-6.repo
```

### 常用软件

**bash-insulter**

> 一个在你打错命令时候嘴臭你的工具

```bash
git clone https://github.com/No-Github/bash-insulter.git bash-insulter
cp bash-insulter/src/bash.command-not-found /etc/
chmod 777 /etc/bash.command-not-found
source /etc/bash.command-not-found
```
```bash
vim /etc/bashrc 或 vim /etc/bash.bashrc

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

> 一个挺好用的 shell 环境

```bash
echo /usr/bin/fish | sudo tee -a /etc/shells	# 加默认
usermod -s /usr/bin/fish <USERNAME>
```

**zsh**

> 一个挺好用的 shell 环境

```bash
apt install -y zsh		# 安装 zsh
chsh -s /bin/zsh		# 切换默认的 shell 为 zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"	# 安装 oh-my-zsh
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions	# 下载命令补全插件

# zshrc 配置文件中修改如下内容
vim ~/.zshrc

plugins=(git zsh-autosuggestions)

zsh						# 重新加载 zsh 配置

# 更多主题见此 https://github.com/robbyrussell/oh-my-zsh/wiki/themes
```

**Powerline-shell**

> 用于美化 shell 环境

```bash
pip install powerline-shell
```
```vim
vim ~/.config/fish/config.fish

function fish_prompt
	powerline-shell --shell bare $status
end
```

更多关于 linux 工具的内容参考笔记 [工具](./笔记/工具.md)

---

# 系统管理

## 系统信息

- 内容参见 [信息](./笔记/信息.md)

### 日志

- 内容参见 [日志](./笔记/日志.md)

---

## 系统设置
### 时间

- date
	```bash
	# date 命令用于查看当前时间
	date							# 不带任何参数的 date 仅用于查看时间
	date -R							# 查看当前时区
	data -s "2019-03-31 13:12:29"	# 修改系统时间
	date +%s						# 获取现在的 Unix 时间戳

	# e.g. : 例如，将系统日期设置为2009年1月31日，晚上10：19，53秒
	date 013122192009.53
	date +%Y%m%d -s "20090131"

	# e.g. : 各种格式显示当前日期和时间的方法
	date '+Current Date: %m/%d/%y%nCurrent Time:%H:%M:%S'
	date +"%d-%m-%Y"
	date +"%A,%B %d %Y"
	date --date="1 year ago"
	date --date="yesterday"
	date --date="10 months 2 day ago"
	date -d "last friday"
	date --date='3 seconds'
	date --date='4 hours'
	```

- ntpdate
	```bash
	# ntpdate 命令可以用于设置本地日期和时间
	ntpdate 0.rhel.pool.ntp.org		# 网络同步时间
	```

- hwclock
	```bash
	# hwclock 设置硬件日期和时间
	hwclock					# 使用不带任何参数的 hwclock 查看当前硬件日期和时间
	hwclock -w 				# 将系统时钟同步到硬件时钟,将当前时间和日期写入 BIOS,避免重启后失效
	hwclock -s 				# 将硬件时钟同步到系统时钟
	```

- cal
	```bash
	# cal 用于查看日历
	cal
	```

**ntp 服务**
- 安装
	```bash
	yum install ntp			# 安装 ntp 服务
	chkconfig ntpd on		# 开启 ntpd 服务
	cat /etc/ntp.conf		# 查看 ntp 服务配置


	ntpq –p     			# 查看本机和上层服务器的时间同步结果
	ntptrace     			# 可以用來追踪某台时间服务器的时间对应关系
	ntpdate IP   			# 客户端要和 NTP server 进行时钟同步。
	/var/log/ntp/ntp.log	# 查看 ntp 日志
	```

	ntp.conf 的具体配置参考 http://www.ntp.org/ntpfaq/NTP-s-config.htm#S-CONFIG-BASIC

	也可以查看 [文件](./笔记/文件.md#etc)

**Tips**
- ntpd 与 ntpdate 的区别
	- ntpd 在实际同步时间时是一点点的校准过来时间的,最终把时间慢慢的校正对.而 ntpdate 不会考虑其他程序是否会阵痛,直接调整时间.
	- 一个是校准时间,一个是调整时间.
	- https://blog.csdn.net/tuolaji8/article/details/79971591

### 时区

**查看时区**
```bash
timedatectl
```

**修改时区**
```bash
timedatectl set-timezone Asia/Shanghai		# 将时区设置为 Asia/Shanghai

或

cp  /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
```

### 语言

**查看系统语言**
```bash
echo  $LANG 				# 查看当前操作系统的语言
```

**修改系统语言**
```bash
vim /etc/locale.conf

set LANG en_US.UTF-8		# 更改默认语言
	 zh_CN.UTF-8
```
```bash
source   /etc/locale.conf
```

**换界面显示语言**
```bash
dpkg-reconfigure locales
# 空格是选择,Tab是切换,*是选中
# 选中 en_US.UTF-8 和 zh_CN.UTF-8,确定后,将 en_US.UTF-8 选为默认,然后安装中文字体
```

**如果界面出现乱码,安装中文字体**
```bash
apt install -y xfonts-intl-chinese
apt install -y ttf-wqy-microhei
reboot
```

### 启动项-计划任务

**查看**
```bash
chkconfig                   # 查看开机启动服务命令
ls /etc/init.d              # 查看开机启动配置文件命令
cat /etc/rc.local           # 查看 rc 启动文件
ls /etc/rc.d/rc[0~6].d

runlevel                    # 查看运行级别命令

service crond status		# 查看 cron 服务状态
```

**计划任务**
```bash
ls -alh /var/spool/cron     # 默认编写的 crontab 文件会保存在 /var/spool/cron/用户名 下
ls -al /etc/ | grep cron
ls -al /etc/cron*
cat /etc/cron*
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny
cat /etc/crontab
cat /etc/anacrontab
cat /var/spool/cron/crontabs/root
```

**crontab 命令**
```bash
crontab -l   				# 列出某个用户 cron 服务的详细内容
crontab -r   				# 删除每个用户 cront 任务(谨慎：删除所有的计划任务)
crontab -e   				# 使用编辑器编辑当前的 crontab 文件

# 前5个星号分别代表:分钟,小时,几号,月份,星期几
* * * * * command			# 每1分钟执行一次 command
3,15 * * * * command		# 每小时的第3和第15分钟执行
@reboot	command				# 开机启动

# 例子
0 */2 * * * /sbin/service httpd restart	# 意思是每两个小时重启一次 apache
50 7 * * * /sbin/service sshd start		# 意思是每天7:50开启 ssh 服务
50 22 * * * /sbin/service sshd stop		# 意思是每天22:50关闭 ssh 服务
0 0 1,15 * * fsck /home					# 每月1号和15号检查 /home 磁盘
1 * * * * /home/bruce/backup			# 每小时的第一分执行 /home/bruce/backup 这个文件
00 03 * * 1-5 find /home "*.xxx" -mtime +4 -exec rm {} \;	# 每周一至周五3点钟,在目录 /home 中,查找文件名为 *.xxx 的文件,并删除4天前的文件.
30 6 */10 * * ls						# 意思是每月 1、11、21、31 日的 6:30 执行一次 ls 命令

# 周与日月不可同时并存,可以分别以周或者是日月为单位作为循环，但你不可使用「几月几号且为星期几」的模式工作
30 12 11 9 5 echo "just test" # 这是错误的写法
```

可以使用在线的 CRON 表达式工具辅助 : https://tool.lu/crontab/

crontab 命令相当于就是修改 `/var/spool/cron/crontabs/usename` 的文件

**/etc/crontab 文件**

`/etc/crontab` 默认是控制 `/etc/cron.*`, 如 `/etc/cron.daily`, `/etc/cron.weekly`, `/etc/cron.monthly` 这些

格式如下:
```
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
```

**/etc/crontab 文件和 crontab -e 的区别**

* 使用范围

	修改 `/etc/crontab` 这种方法只有 root 用户能用，这种方法更加方便与直接直接给其他用户设置计划任务，而且还可以指定执行 shell 等等，

	crontab -e 这种所有用户都可以使用，普通用户也只能为自己设置计划任务。然后自动写入 `/var/spool/cron/usename`

* 服务重启

	```bash
	/etc/init.d/crond restart

	service crond restart
	```

* 语法格式

	crontab -e 与 `/etc/crontab` 修改语法格式不一样，后者多一个 user 指定

**/etc/cron.d/**

`/etc/cron.d/` 目录下也是存放 crontab 的配置文件.

`/etc/crontab` 和 `/etc/cron.d/` 在配置定时任务时，需要指定用户是 root，而 `/var/spool/cron/crontabs/` 已经是属于用户控制的, 所以不需要指定用户, 这是格式上的区别.

cron 设置的默认环境变量:
```
$SHELL: /bin/sh
$PATH: /usr/bin:/bin
```
如果没有设置相关的环境变量，会造成如 $PATH 问题导致的命令找不到.

可以在 cron 配置文件顶部加上:
```
SHELL=/bin/bash
PATH=/usr/bin:/bin:/sbin:/usr/sbin
*/5 * * * * root ./run.sh >/dev/null 2>&1
```

**/etc/rc.local**

在文件末尾 (exit 0 之前) 加上你开机需要启动的程序或执行的命令即可 (执行的程序需要写绝对路径,添加到系统环境变量的除外) ,如

**/etc/profile.d/**

将写好的脚本 (.sh 文件) 放到目录 `/etc/profile.d/` 下,系统启动后就会自动执行该目录下的所有 shell 脚本

**at**

> 在特定的时间执行一次性的任务
```bash
at now +1 minutes
echo "test" > test.txt
<ctrl+d>

atq		# 列出用户的计划任务,如果是超级用户将列出所有用户的任务,结果的输出格式为:作业号、日期、小时、队列和用户名
atrm	# 根据 Job number 删除 at 任务
```

### SELinux

**查看 SELinux 状态**
```bash
getenforce							# 查看 selinux 状态
/usr/sbin/sestatus					# 查看安全策略
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

## 账号管控

**用户**
```bash
id									# 显示真实有效的用户 ID(UID)和组 ID(GID)
	id -un

whoami								# 当前用户
cut -d: -f1 /etc/passwd				# 查看系统所有用户

useradd <username>					# 创建用户
useradd -d /home/<username> -s /sbin/nologin <username>		# 创建用户并指定家目录和 shell
passwd <username>					# 设置用户密码

userdel <username>					# 只删除用户不删除家目录
userdel -r <username>				# 同时删除家目录
userdel -f <username>				# 强制删除,即使用户还在登录中

usermod -g <groupname> <username>	# 修改用户的主组
usermod -G <supplementary> <username>	# 修改用户的附加组
usermod -s /bin/bash <username>		# 修改用户登录的 Shell
usermod -L <username>  				# 锁定用户
usermod -U <username> 				# 解锁用户

chage								# 修改帐号和密码的有效期限
	chage -l <username>				# 查看一下用户密码状态
	chage -d <username>				# 把密码修改曰期归零了,这样用户一登录就要修改密码

passwd								# 配置 su 密码
	passwd -l <username>  			# 锁定用户
	passwd -u <username>  			# 解锁用户

su <username>						# 切换账号
su - <username>                     # 切换账号并改变工作目录至使用者的家目录

compgen -c                  		# 列出所有可用的命令

ulimit								# 查看、设置、获取文件打开的状态和配置详情
	ulimit -a                   	# 显示登录用户的资源限制
	ulimit -n 						# 显示打开文件数限制
	ulimit -c 						# 显示核心转储文件大小
	ulimit -u 						# 显示登录用户的最大用户进程数限制
	ulimit -f 						# 显示用户可以拥有的最大文件大小
	ulimit -m 						# 显示登录用户的最大内存大小
	ulimit -v 						# 显示最大内存大小限制
```

**组**
```bash
groups								# 当前组

groupadd <groupname>				# 创建组
groupadd <username> <groupname>		# 移动用户到组

newgrp <groupname>					# 创建组
```

**权限**
```bash
chown named.named <File/Folder>		# 将文件给指定用户及组

chmod <number> <File>				# 给文件权限
# 用户 rwx、组 rwx、其他用户 rwx  4.2.1 分别代表读,写,执行
	chmod 777 <File>
	chmod o=rw <File>				# 代表只给其他用户分配读写权限
	chmod u=rw,g=r,o= <File>
	chown -R u+x <Folder>			# 对文件夹及其子目录所有文件的所有者增加执行权限

	chmod u+s test_file				# 给文件增加 SUID 属性
	chmod g+s test_dir     			# 给目录增加 SGID 属性
	chmod o+t test_dir     			# 给目录增加 Sticky 属性

chgrp				# 改变文件或目录所属的用户组
	chgrp user1 file.txt			# Change the owning group of the file file.txt to the group named user1.
	chgrp -hR staff /office/files	# Change the owning group of /office/files, and all subdirectories, to the group staff.

umask 002			# 配置反码,代表创建文件权限是 664 即 rw-rw-r--,默认 0022(重启后消失)
# umask 值 002 所对应的文件和目录创建缺省权限分别为 6 6 4 和 7 7 5
# 需要长期修改,可以直接改 vim /etc/profile 中 umask 值

chattr				# 可修改文件的多种特殊属性
	chattr +i <File>				# 增加后,使文件不能被删除、重命名、设定链接接、写入、新增数据
	chattr +a <File>				# 增加该属性后,只能追加不能删除,非root用户不能设定该属性
	chattr +c <File>				# 自动压缩该文件,读取时会自动解压.Note: This attribute has no effect in the ext2, ext3, and ext4 filesystems.

lsattr <File>		# 该命令用来读取文件或者目录的特殊权限
```
```bash
visudo	# 加 sudo 权限

user1 ALL=(ALL)     ALL
```
加 sudo 权限(仅限 Ubuntu)
```bash
adduser user1 sudo	# 将 user1 加到 sudo 组中
deluser user1 sudo	# 将 user1 从 sudo 组中删除
```
```bash
sudo -v 			# 查看 sudo 信息
sudo -l 			# 查看当前权限
```

**ACL**
```bash
setfacl -m u:apache:rwx <File/Folder>	# 配置 ACL
getfacl <File/Folder>					# 查看 ACL 权限
setfacl -b <File/Folder>				# 删除 ACL
```

关于 linux 的账号和认证更多内容参考笔记 [认证](./笔记/认证.md)

---

## 进程管理

**服务管理**

- service
	```bash
	# 控制系统服务的实用工具
	service <程序> status/start/restart/stop
	```

- systemctl
	```bash
	# 系统服务管理器指令
	systemctl enable crond.service	# 让某个服务开机自启(.service 可以省略)
	systemctl disable crond			# 不让开机自启
	systemctl status crond			# 查看服务状态
	systemctl start crond			# 启动某个服务
	systemctl stop crond			# 停止某个服务
	systemctl restart crond			# 重启某个服务
	systemctl reload *				# 重新加载服务配置文件
	systemctl is-enabled crond		# 查询服务是否开机启动
	```

- chkconfig

	从 CentOS7 开始,CentOS 的服务管理工具由 SysV 改为了 systemd,但即使是在 CentOS7 里,也依然可以使用 chkconfig 这个原本出现在 SysV 里的命令.
	```bash
	# 检查、设置系统的各种服务
	chkconfig --list		# 列出所有的系统服务
	chkconfig --add httpd	# 增加 httpd 服务
	chkconfig --del httpd	# 删除 httpd 服务
	chkconfig --level httpd 2345 on	# 设置 httpd 在运行级别为 2、3、4、5 的情况下都是 on(开启)的状态,另外如果不传入参数 --level,则默认针对级别 2/3/4/5 操作.
	```

**监视进程**

- ps
	```bash
	# 查看进程
	ps -l 			# 长格式显示详细的信息
	ps -a 			# 显示一个终端的所有进程，除会话引线外
	ps -A 			# 显示所有进程信息
	ps -u root 		# 指定用户的所有进程信息
	ps -e 			# 显示所有进程信息
	ps aux 			# 查看系统中所有的进程显示所有包含其他使用者的行程
	ps -axjf 		# 以程序树的方式显示
	ps -eLf 		# 显示线程信息
	ps -ef | grep queue | grep -v grep | wc -l # 查找含有 queue 关键词的进程（-v 去掉 grep 本身），输出找到的进程数量。
	ps -aux | awk '$2~/S/ {print $0}' #统计 sleep 状态的进程

	ps aux | grep root	# 查看 root 运行的程序
	ps -ef | grep root	# 查看 root 运行的程序
	```

```bash
jobs	    # 显示 Linux 中的任务列表及任务状态
	jobs -l		    # 显示进程号

pidof program	    # 找出 program 程序的进程 PID
pidof -x script     # 找出 shell 脚本 script 的进程 PID

top					# 实时动态地查看系统的整体运行情况

free
free -h				# 显示当前系统未使用的和已使用的内存数目

vmstat 1			# 显示虚拟内存状态

ps					# 报告当前系统的进程状态
	ps -aux			# 显示现在所有用户所有程序
	# 由于ps命令能够支持的系统类型相当的多,所以选项多的离谱,这里略
pidstat -u -p ALL	# 查看所有进程的 CPU 使用情况

watch <Command>		# 以周期性的方式执行给定的指令,指令输出以全屏方式显示.
	-n : 指定指令执行的间隔时间(秒);
	-d : 高亮显示指令输出信息不同之处;
	-t : 不显示标题.
```

**进程处理**

- kill
	```bash
	# 杀死进程
	kill -s <PID>							# 删除执行中的程序或工作
		kill -l								# 显示信号
		kill -HUP <pid>						# 更改配置而不需停止并重新启动服务
		kill -9 <PID> && kill -KILL <pid>	# 信号(SIGKILL)无条件终止进程
	killall <PID>							# 使用进程的名称来杀死进程
	```

- pkill
	```bash
	# pkill 用于杀死一个进程，与 kill 不同的是它会杀死指定名字的所有进程
	pkill -9 php-fpm	# 结束所有的 php-fpm 进程
	```

```bash
ctrl+z	# 将前台运行的任务暂停,仅仅是暂停,而不是将任务终止.
bg		# 转后台运行
fg		# 转前台运行
```
```bash
cmdline
# 在Linux系统中,根据进程号得到进程的命令行参数,常规的做法是读取 /proc/{PID}/cmdline,并用'\0'分割其中的字符串得到进程的 args[],例如下面这个例子:
	# xxd /proc/7771/cmdline
	0000000: 2f69 746f 612f 6170 702f 6d61 7665 2f62  /itoa/app/mave/b
	0000010: 696e 2f6d 6176 6500 2d70 002f 6974 6f61  in/mave.-p./itoa
	0000020: 2f61 7070 2f6d 6176 6500                 /app/mave.
	通过分割其中的 0x00(C 语言字符串结束符),可以把这个进程 args[],解析出来:
	args[0]=/itoa/app/mave/bin/mave
	args[1]=-p
	args[2]=/itoa/app/mave
```

**不挂断地运行命令**
- nohup
	```bash
	# nohup 命令运行由 Command 参数和任何相关的 Arg 参数指定的命令, 忽略所有挂断 (SIGHUP) 信号. 在注销后使用 nohup 命令运行后台中的程序. 要运行后台中的 nohup 命令, 添加 & ( 表示 "and" 的符号)到命令的尾部.
	nohup [COMMAND] &			# 使命令永久的在后台执行

	# e.g.
		sh test.sh &		# 将 sh test.sh 任务放到后台 , 关闭 xshell, 对应的任务也跟着停止.
		nohup sh test.sh	# 将 sh test.sh 任务放到后台, 关闭标准输入, 终端不再能够接收任何输入(标准输入), 重定向标准输出和标准错误到当前目录下的 nohup.out 文件, 即使关闭 xshell 退出当前 session 依然继续运行.
		nohup sh test.sh  &	# 将 sh test.sh 任务放到后台, 但是依然可以使用标准输入, 终端能够接收任何输入, 重定向标准输出和标准错误到当前目录下的 nohup.out 文件, 即使关闭 xshell 退出当前 session 依然继续运行.
	```

- setsid
	```bash
	# setsid 主要是重新创建一个 session,子进程从父进程继承了 SessionID、进程组 ID 和打开的终端,子进程如果要脱离父进程,不受父进程控制,我们可以用这个 setsid 命令
		setsid [options] <program> [arguments ...]
			e.g. : setsid ping baidu.com	# setsid 后子进程不受终端影响,终端退出,不影响子进程
			# 别急,  ps -ef | grep ping ,找到 PID kill 相应的 PID 就可以关掉了😂
	```

- disown
	```bash
	# 使作业忽略 HUP 信号
	disown [-h] [-ar] [jobspec ... | pid ...]
		# 示例1,如果提交命令时已经用"&"将命令放入后台运行,则可以直接使用"disown"
		ping www.baidu.com &
		jobs
		disown -h %1
		ps -ef |grep ping

		# 示例2,如果提交命令时未使用"&"将命令放入后台运行,可使用 CTRL-z 和"bg"将其放入后台,再使用"disown"
		ping www.baidu.com
		bg %1
		jobs
		disown -h %1
		ps -ef |grep ping
	```

更多进程管理内容参考笔记 [进程](./笔记/进程.md)

---

## 内核管理

**rmmod**

用于从当前运行的内核中移除指定的内核模块。执行 rmmod 指令，可删除不需要的模块。
```bash
rmmod [options] [arguments ...]

# 选项释义
	# -v：显示指令执行的详细信息；
	# -f：强制移除模块，使用此选项比较危险；
	# -w：等待着，直到模块能够被除时在移除模块；
	# -s：向系统日志（syslog）发送错误信息。

# e.g.
	lsmod | grep raid1
	rmmod raid1			# 卸载正在使用的Linux内核模块
	# 警告 : 在你不确定这个内核模块是干什么的之前,不要卸载
```

**dmesg**

dmesg 可用于找出内核最新消息中的错误和警告
```bash
dmesg | less
```

**nmi_watchdog**

“看门狗NMI中断”的机制。（NMI：Non Maskable Interrupt. 这种中断即使在系统被锁住时，也能被响应）。这种机制可以被用来调试内核锁住现象。通过周期性地执行NMI中断，内核能够监测到是否有CPU被锁住。当有处理器被锁住时，打印调试信息。
```bash
echo '0' >/proc/sys/kernel/nmi_watchdog 			# 关闭linux 看门狗
echo 'kernel.nmi_watchdog=0' >>/etc/sysctl.conf   	# 重启自动关闭
```

---

## 设备管理

更多内容见笔记 [信息](./笔记/信息.md#硬件)

### 内存

**虚拟内存**

```bash
free -h	# 查看 swap 分区
vmstat
swapon -s
```

如果机器没有安装 swap 分区可以自己分配一个
```bash
# 创建一个 swap 文件, 大小为 1G
dd if=/dev/zero of=/home/f8xswap bs=1M count=1024

# 将文件格式转换为 swap 格式的
mkswap /home/f8xswap

# 把这个文件分区挂载 swap 分区
swapon /home/f8xswap
```

长期挂载
```
echo "/home/f8xswap swap swap default 0 0" >> /etc/fstab
```

### 磁盘

**磁盘的文件名**

Linux 中每个硬件都被当做一个文件，包括磁盘。磁盘以磁盘接口类型进行命名，常见磁盘的文件名如下：
- IDE 磁盘 : /dev/hd[a-d]
- SATA/SCSI/SAS 磁盘 : /dev/sd[a-p]
其中文件名后面的序号的确定与系统侦测到磁盘的顺序有关，而与磁盘所插入的插槽位置无关。

**磁盘配额**
- quota : 能对某一分区下指定用户或用户组进行磁盘限额。

**分区**
```bash
fdisk -l			# 查看磁盘情况
fdisk /dev/sdb		# 创建系统分区
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
cat /etc/fstab
mount

mount /dev/sdd1 /mnt/sdd		# 挂载新硬盘到操作系统的某个节点上
mount /dev/cdrom /mnt/cdrom/	# 挂载 CD 镜像
mount -t vfstype				# 指定文件系统的类型,通常不必指定.mount 会自动选择正确的类型.

vi /etc/fstab					# 自动挂载
/dev/cdrom /mnt/cdrom iso9660 defaults 0 0

findmnt							# 显示Linux中当前挂载的文件系统
```

**删除**
```bash
rm <File>	# 删除指定文件
	rm -r <Folder>	# 删除文件夹
	rm -i <File>	# 删除前确认
	rm -f <File>	# 强制删除
	rm -v <File>	# 显示详细信息

shred -zvu -n  5 <File>	# 主要用于文件覆盖内容,也可以删除
	# -z - 用零添加最后的覆盖以隐藏碎化
	# -v - 显示操作进度
	# -u - 覆盖后截断并删除文件
	# -n - 指定覆盖文件内容的次数(默认值为3)
```

**数据恢复**
- [数据恢复](./Secure-Linux.md#文件恢复)

**占用**
- df
	```bash
	# 报告驱动器的空间使用情况
	df [options] [arguments ...]

	# e.g.
		df -H	# 以人类可读的格式进行显示
		df -ah	# 查看磁盘占用大的文件夹
	```

- du
	```bash
	# 报告目录的空间使用情况
	du [options] [arguments ...]

	# e.g.
		du -H . | sort			# 以人类可读的格式进行显示,排序显示
		du -Hd 1 / | sort -hr
		du -sH /etc/yum			# 特定目录的总使用量
		du --max-depth=1 -H		# 查看文件夹下各个文件夹的磁盘占用
	```

**dd**

```bash
# 主要功能为转换和复制文件。
dd [options]
	e.g. : dd if=/dev/zero of=out.txt bs=1M count=1
	# if 代表输入文件.如果不指定 if,默认就会从 stdin 中读取输入.
	# of 代表输出文件.如果不指定 of,默认就会将 stdout 作为默认输出.
	# ibs=bytes:一次读入 bytes 个字节,即指定一个块大小为 bytes 个字节.
	# obs=bytes:一次输出 bytes 个字节,即指定一个块大小为 bytes 个字节.
	# bs 代表字节为单位的块大小.
	# count 代表被复制的块数.
	# /dev/zero 是一个字符设备,会不断返回 0 值字节(\0).

	# e.g. 截取地址 925888（0xe20c0）之后的数据，保存到 out.bin
	dd if=test.trx bs=1 skip=925888 of=out.bin

	# e.g. 文件分块合并,文件分为 1 2 3 4 5 每个文件 无用头信息 364 字节,去掉头信息合并
	dd if=1 bs=1 skip=364 of=11
	dd if=2 bs=1 skip=364 of=22
	dd if=3 bs=1 skip=364 of=33
	dd if=4 bs=1 skip=364 of=44
	dd if=5 bs=1 skip=364 of=55
	cat 11 22 33 44 55 > fly.rar
```

**LVM**

> LVM 是 Logical Volume Manager 的缩写，中文一般翻译为 "逻辑卷管理"，它是 Linux 下对磁盘分区进行管理的一种机制。LVM 是建立在磁盘分区和文件系统之间的一个逻辑层，系统管理员可以利用 LVM 在不重新对磁盘分区的情况下动态的调整分区的大小。如果系统新增了一块硬盘，通过 LVM 就可以将新增的硬盘空间直接扩展到原来的磁盘分区上。

- **物理卷**

	创建物理卷
	```bash
	pvcreate /dev/sda5
	```

	查看物理卷
	```bash
	pvdisplay
	```

	物理卷数据转移
	```bash
	pvmove /dev/sda4 /dev/sda5  # 把 / dev/sda4 物理卷数据转移到 / dev/sda5 物理卷上，注意转移的时候查看物理卷大小
	```

	删除物理卷
	```bash
	pvremove /dev/sda4
	```

- **卷组**

	卷组可以由一个或多个物理卷组成,当卷组空间不够时可以再新增物理卷扩容.

	创建卷组
	```bash
	vgcreate vg1 /dev/sda5
	```

	新增卷组
	```bash
	vgextend vg1 /dev/sda6
	```

	删除卷组
	```bash
	vgremove vg1
	```

	查看卷组
	```bash
	vgdisplay
	vgs
	```

	移除某块物理卷
	```bash
	vgremove vg1 /dev/sda6
	```

- **逻辑卷**

	逻辑卷建立在卷组基础之上的,所以在创建逻辑卷的时候一定要指定卷组名称.

	创建逻辑卷
	```bash
	lvcreate -L 3G -n lvdisk1 vg1
	```

	显示逻辑卷
	```bash
	lvdisplay
	lvs
	```

	挂载逻辑卷
	```bash
	# 这里需要注意的是格式化的格式与挂载要进行匹配，否则会出现问题；挂载之后重启会失效，请查看下面让重启自动挂载的做法。

	mkfs.ext4 -t /dev/vg1/lvdisk1
	mount -t ext4 /dev/vg1/lvdisk1 /hehe
	mkfs.xfs -f /dev/vg1/lvdisk1
	mount -t xfs /dev/vg1/lvdisk1 /hehe
	```

	删除逻辑卷
	```bash
	lvremove /dev/vg1/lvdisk1
	```

	扩容逻辑卷(卷组的可用范围内的容量值)
	```bash
	lvextend -L +1G /dev/vg1/lvdisk1
	lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
	```

	收缩逻辑卷容量
	```bash
	# 提示：使用以下命令时注意数据可能会丢失，请注意备份数据之后进行操作。

	lvreduce -L -20G /dev/vg1/lvdisk1
	```

	扩容生效
	```bash
	resize2fs /dev/vg1/lvdisk1
	xfs_growfs /dev/vg1/lvdisk1
	# 注意：resize2fs 主要针对 ext4 目录格式进行处理，而 xfs_growfs 主要针对 xfs 目录格式。
	```

	挂载重启失效问题
	```bash
	# 利用 root 权限编辑 / etc/fstab 文件加入挂载点，这样开机会自动挂载。

	/dev/vg1/lvdisk1 /hehe ext4    defaults    0  0
	```

**块设备信息**

- lsblk
	```bash
	# 显示所有可用块设备的信息
	lsblk -m	# 显示设备所有者相关的信息,包括文件的所属用户、所属组以及文件系统挂载的模式
	```

- blkid
	```bash
   	# 输出所有可用的设备、UUID、文件系统类型以及卷标

	# e.g.
	blkid /dev/sda1
	blkid -U d3b1dcc2-e3b0-45b0-b703-d6d0d360e524
	blkid -po udev /dev/sda1	# 获取更多详细信息
	blkid -g					# 清理 blkid 的缓存
	```

- partx
	```bash
	# 显示磁盘上分区的存在和编号
	partx --show /dev/sda
	partx --show /dev/sda1
	```

---

### 无线网卡

**配置无线网卡**
- WM Ware(开机后)

    虚拟机->可移动设备->Ralink 802.11 n Wlan(显卡型号)->连接(断开与主机的连接)

- VBox

    虚拟机关机状态下->将设备插入主机->设置->USB设备->添加->删除除了供应商标识(VendorID)和产品标识(ProductID)之外的参数->开机->插入设备

- 验证是否连接成功

    ```bash
    lsusb
    airmon-ng
    ifconfig
    iwconfig
    ```
    出现无线网卡型号即为成功

---

### 蓝牙

**启动蓝牙服务**
```bash
service bluetooth start
systemctl start bluetooth
```

**查看蓝牙设备**
```bash
hciconfig			# 查看蓝牙设备

hcitool dev
	hcitool --help
	hcitool lescan	# 扫描周围低功耗设备(BLE)
	hcitool scan	# 扫描周围蓝牙设备
	hcitool -i hci0 dev	# 查看蓝牙设备信息

gattool				# 对 BLE 数据进行精细化管理的话，就需要用到 gattool，使用 gattool 对蓝牙设备发送指令的操作上要比 hcitool 的 cmd 齐全很多
	gattool -h
```

**激活蓝牙设备**
```bash
# hciconfig 命令如 ifconfig 一样，可以控制蓝牙设备的开启与关闭
hciconfig hci0 up	# 激活蓝牙设备
hciconfig hci0 down	# 设备关闭
hciconfig hci0		# 查看属性
	# 第二行中的 “BD Address”，这是蓝牙设备的MAC地址
```

**关闭本地 pin 验证**
```bash
hciconfig hci0 noauth
```

**设置连接 pin 码**
```bash
/var/lib/bluetooth/XX:XX:XX:XX:XX:XX/pincodes	# XX:XX:XX:XX:XX:XX 为本地设备地址

文件格式为: XX:XX:XX:XX:XX:XX 1234				# XX:XX:XX:XX:XX:XX 为目标设备地址
```

**bluetoothctl**
```bash
bluetoothctl		# 蓝牙工具软件
	bluetoothctl scan on						# 主动搜索可以连接的蓝牙设备
	bluetoothctl discoverable on				# 使蓝牙适配器可被搜索
	bluetoothctl pair FC:69:47:7C:9D:A3			# 对指定设备进行配对
	bluetoothctl connect FC:69:47:7C:9D:A3		# 配对后,连接指定设备
	bluetoothctl paired-devices					# 查看已配对的设备
	bluetoothctl devices						# 列出计算机蓝牙范围内的设备
	bluetoothctl trust FC:69:47:7C:9D:A3		# 对指定设备进行信任
	bluetoothctl untrust FC:69:47:7C:9D:A3		# 取消对指定设备的信任

	bluetoothctl remove FC:69:47:7C:9D:A3		# 删除已配对的设备
	bluetoothctl disconnect FC:69:47:7C:9D:A3	# 断开指定设备的连接
	bluetoothctl block FC:69:47:7C:9D:A3		# 将指定设备加入黑名单
```

**rfcomm**
```bash
cat /etc/bluetooth/rfcomm.conf

rfcomm --help

# 输出字符到蓝牙串口
echo y>/dev/rfcomm0
```

---

### 外接硬盘

```bash
fdisk -l			# 查看磁盘情况

mkdir -p /mnt/usb1
mount /dev/sdb1 /mnt/usb1
cd /mnt/usb1

umount /mnt/usb1	# 取消挂在
```

**[NTFS-3G](https://jp-andre.pagesperso-orange.fr/advanced-ntfs-3g.html)**
```bash
yum install -y fuse-devel

cd /tmp
wget https://jp-andre.pagesperso-orange.fr/ntfs-3g-2017.3.23AR.5-1.el7.x86_64.rpm
rpm -ivh ntfs-3g-2017.3.23AR.5-1.el7.x86_64.rpm

fdisk -l
mkdir -p /mnt/ntfsusb
mount -t ntfs-3g /dev/sda1 /mnt/ntfsusb
```

### CD & DVD

**刻录 CD**
```bash
cdrecord -V -eject dev=/dev/cdrom data-backup.iso
```

**刻录 DVD**
```bash
growisofs -dvd-compat -Z /dev/dvdrw=data.iso
```

**从 CD 或 DVD 创建 ISO 文件**
```bash
isoinfo -d -i /dev/cdrom

dd if=/dev/cdrom bs=2048 count=1825 of=mydata.iso
```
