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
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/运维/Linux/open-source.png" width="15%"></a>
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/运维/Linux/bash.png" width="15%"></a>
</p>

`基础 Linux 命令、操作指南`

---

# 大纲

* **[👍 基础使用](#基础使用)**
	* [环境变量](#环境变量)
	* [符号](#符号)
	* [会话](#会话)
	* [文件和目录](#文件和目录)
		* [查看](#查看)
		* [创建](#创建)
		* [删除](#删除)
		* [查询](#查询)
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
	* [Firewall](#Firewall)
		* [Firewalld](#Firewalld)
		* [Iptables](#Iptables)
	* [软件包管理](#软件包管理)
		* [apt](#apt)
		* [Binary](#Binary)
		* [dpkg](#dpkg)
		* [Pacman](#Pacman)
		* [rpm](#rpm)
		* [snap](#snap)
		* [yum](#yum)
		* [常用软件](#常用软件)

* **[🦋 系统管理](#系统管理)**
	* [系统信息](#系统信息)
		* [日志](#日志)
	* [系统设置](#系统设置)
		* [时间](#时间)
		* [语言](#语言)
		* [启动项-计划任务](#启动项-计划任务)
		* [SELinux](#SELinux)
	* [账号管控](#账号管控)
	* [进程管理](#进程管理)
	* [设备管理](#设备管理)
		* [硬盘-数据](#硬盘-数据)

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

- **bash**
	```bash
	echo $PATH  						# 查看环境变量

	PATH=$PATH:/usr/local/python3/bin/	# 新添加的路径(关闭终端失效)
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

- 图形模式登录时,顺序读取 : `/etc/profile` 和 `~/.profile`
- 图形模式登录后,打开终端时,顺序读取 : `/etc/bash.bashrc` 和 `~/.bashrc`
- 文本模式登录时,顺序读取 : `/etc/bash.bashrc` , `/etc/profile` 和 `~/.bash_profile`

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

**grep**
```bash
grep		# 文本搜索工具,它能使用正则表达式搜索文本,并把匹配的行打印出来.
# 参数解释
# -a ： 将 binary 文件以 text 文件的方式进行搜寻
# -c ： 计算找到个数
# -i ： 忽略大小写
# -n ： 输出行号
# -v ： 反向选择，亦即显示出没有 搜寻字符串 内容的那一行
# --color=auto ：找到的关键字加颜色显示
```

**awk**
```bash
awk			# 可以根据字段的某些条件进行匹配，例如匹配字段小于某个值的那一行数据。
awk '条件类型 1 {动作 1} 条件类型 2 {动作 2} ...' filename
# awk 每次处理一行，处理的最小单位是字段，每个字段的命名方式为：\$n，n 为字段号，从 1 开始，\$0 表示一整行。
```

**其他符号工具**
```bash
head		# 显示文件的开头的内容.默认下,显示文件的头 10 行内容.
tail		# 显示文件中的尾部内容.默认下,显示文件的末尾 10 行内容.
sort		# 将文件进行排序,并将排序结果标准输出.
uniq		# 用于报告或忽略文件中的重复行
```

---

## 会话

```bash
id
who			# 显示目前登录系统的用户信息.
w			# 显示已经登陆系统的用户列表,并显示用户正在执行的指令.
last		# 显示用户最近登录信息
```
```bash
Ctrl+S		# 终止显示的信号/指令
Ctrl+Q		# 恢复显示的信号/指令
alt+F1-F6	# 切换虚拟控制台
Alt+F7		# 图形界面
```

**screen**

screen 是一个会话管理软件，用户可以通过该软件同时连接多个本地或远程的命令行会话，并在其间自由切换。
```bash
yum -y install screen
apt-get -y install screen
screen -S <name>
screen -ls
screen -r <name>	# 重新连接
ctrl+d				# 终止会话
```

**历史记录**
```bash
cat ~/.bash_history
cat ~/.nano_history
cat ~/.atftp_history
cat ~/.mysql_history
cat ~/.php_history
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
更多内容参考笔记 [文件](./笔记/文件.md#/)

### 查看

**目录、文件信息**
```bash
ls			# 查看目录下文件
	ls -a						# 查看目录隐藏文件

pwd			# 以绝对路径的方式显示用户当前工作目录
	pwd -P						# 目录链接时,显示实际路径而非 link 路径

wc			# wc 将计算指定文件的行数、字数，以及字节数
du			# 查看文件大小
stat		# 查看文件属性
file		# 探测给定文件的类型
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

tac			# 是 cat 的反向操作，从最后一行开始打印
less		# 允许用户向前或向后浏览文件
```

**二进制相关**
```bash
objdump		# 显示目标文件的信息,可以通过参数控制要显示的内容
	objdump -p 					# 显示文件头内容
	objdump -T					# 查看动态符号表的内容

od			# 以字符或者十六进制的形式显示二进制文件
strings		# 在对象文件或二进制文件中查找可打印的字符串
ldd			# 可以显示程序或者共享库所需的共享库
nm			# 显示目标文件的符号
```

### 创建

```bash
touch								# 创建文件
	touch -r test1.txt test2.txt 		# 更新 test2.txt 时间戳与 test1.txt 时间戳相同
	touch -c -t 202510191820 a.txt 		# 更改时间

truncate -s 100k aaa.txt			# 创建指定大小文件

mkdir								# 创建文件夹
	mkdir -p /mnt/aaa/aaa/aaa 			# 创建指定路径一系列文件夹
	mkdir -m 777 /test					# 创建时指定权限
```

### 删除

```bash
rm			# 删除
	rm -r		# 递归，对目录及其下的内容进行递归操作
	rm -f		# 强制删除,无需确认操作
	rm -i		# 确认
```
rm 命令有一对专门针对根目录的选项 `--preserve-root` 和 `--no-preserve-root`
- `--preserve-root`：保护根目录，这是默认行为。
- `--no-preserve-root`：不保护根目录。
这对选项是后来添加到 rm 命令的。可能几乎每个系统管理员都犯过操作错误，而这其中删除过根目录的比比皆是

那为什么还会专门出现 --no-preserve-root 选项呢？这可能主要是出于 UNIX 哲学的考虑，给予你想要的一切权力，犯傻是你的事情，而不是操作系统的事情。万一，你真的想删除根目录下的所有文件呢？

```bash
rmdir		# 删除空目录
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

### 查询

**搜索命令**
```bash
which <Command>		# 指令搜索,查找并显示给定命令的绝对路径
```

**搜索文件**
```bash
find / -name conf*	# 快速查找根目录及子目录下所有 conf 文件
locate <File>		# 查找文件或目录
```

```bash
fd					# 文件查找工具
	wget https://github.com/sharkdp/fd/releases/download/v7.3.0/fd-musl_7.3.0_amd64.deb
	dpkg -i fd-musl_7.3.0_amd64.deb
	fd <File>
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
	yum install epel-release && yum install rdfind
	# 或
	apt-get install rdfind

	rdfind -dryrun true /home			# 结果会保存在 results.txt 文件中
	rdfind -deleteduplicates true /home	# 删除
	```

- fdupes
	```bash
	yum install epel-release && yum install fdupes
	# 或
	apt install fdupes

	fdupes /home
	fdupes -r /			# 递归扫描目录,包括子目录
	fdupes -rd /		# 删除重复内容
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
	```

- **更多操作**
	- [Vim](./Power-Linux.md#Vim)

### 比较

```bash
diff <变动前的文件> <变动后的文件>
```
```bash
vimdiff <变动前的文件> <变动后的文件>
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

**软连接**

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

```bash
.tar	# 注:tar 是打包,不是压缩!
tar -xvf FileName.tar						# 解包
tar -cvf FileName.tar DirName				# 打包
tar -tvf FileName.tar.gz					# 不解压查看内容
tar -xvf FileName.tar.gz a.txt  			# 解压指定内容
tar -uvf test.tar.bz2 test					# 更新一个内容
tar -rvf test.tar.bz2 test2 				# 追加一个内容

.tar.gz 和 .tgz
tar -zxvf FileName.tar.gz					# 解压
tar -zcvf FileName.tar.gz DirName			# 压缩

.tar.xz
tar -xvJf FileName.tar.xz					# 解压

.tar.Z
tar -Zxvf FileName.tar.Z					# 解压
tar -Zcvf FileName.tar.Z DirName			# 压缩

.tar.bz
tar -jxvf FileName.tar.bz					# 解压
tar -jcvf FileName.tar.bz DirName			# 压缩

.gz
gunzip FileName.gz							# 解压1
gzip -dv FileName.gz						# 解压2
gzip FileName								# 压缩
gzip -l FileName.gz 						# 不解压查看内容
zcat FileName.gz 							# 不解压查看内容

.bz2
bzip2 -dv FileName.bz2						# 解压1
bunzip2 FileName.bz2						# 解压2
bzip2 -zv FileName							# 压缩
bzcat FileName.bz2							# 不解压查看内容

.Z
uncompress FileName.Z						# 解压
compress FileName							# 压缩
compress -rvf /home/abc/					# 强制压缩文件夹

.zip
unzip FileName.zip							# 解压
zip FileName.zip DirName					# 压缩

.rar
rar x FileName.rar							# 解压
rar a FileName.rar DirName					# 压缩

.lha
lha -e FileName.lha							# 解压
lha -a FileName.lha FileName				# 压缩

.rpm
rpm2cpio FileName.rpm | cpio -div			# 解包

.deb
ar -p FileName.deb data.tar.gz | tar zxf -	# 解包
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

**端口**
```bash
getent services 		# 查看所有服务的默认端口名称和端口号
ss -tnlp				# 获取 socket 统计信息
lsof -i					# 列出当前系统打开文件
netstat -antup
netstat -antpx
netstat -tulpn
```

**路由表**
```bash
route					# 查看路由表
ip route				# 显示核心路由表
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
	apt install resolvconf

	vim /etc/resolvconf/resolv.conf.d/head

	nameserver 8.8.8.8
	```
	```
	resolvconf -u
	```

**修改IP**
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

**配置DHCP**
- Ubuntu
	```bash
	iface enp7s0 inet dhcp		# dhcp 配置
	```

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

---

## 抓包

**tcpdump**
```bash
# Debian安装
apt install tcpdump -y

# Redhat安装
yum install tcpdump -y

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
yum install lrzsz
sz xxx		# 将选定的文件发送(send)到本地机器
rz 			# 运行该命令会弹出一个文件选择窗口,从本地选择文件上传到服务器(receive),需要远程软件支持
```

**wget**
```bash
wget example.com/big.file.iso						# 下载目标文件
wget --output-document=filename.html example.com	# 另行命名
wget -c example.com/big.file.iso					# 恢复之前的下载
wget --i list.txt									# 下载文件中的 url
wget -r example.com									# 递归下载
wget --no-check-certificate							# 不检查 https 证书
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
```

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
apt install alien			# 安装 alien
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
```

**无法获得锁 /var/lib/apt/lists/lock - open (11: 资源暂时不可用)**
```bash
rm -rf /var/cache/apt/archives/lock
rm -rf /var/lib/dpkg/lock-frontend
rm -rf /var/lib/dpkg/lock		# 强制解锁占用
rm /var/lib/dpkg/lock
rm /var/lib/apt/lists/lock
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

**Ubuntu apt 换源**
```vim
vim /etc/apt/sources.list

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

**Debain apt 换源**
```vim
vim /etc/apt/sources.list

# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb http://mirrors.aliyun.com/debian/ buster main contrib non-free
# deb-src http://mirrors.aliyun.com/debian/ buster main contrib non-free
deb http://mirrors.aliyun.com/debian/ buster-updates main contrib non-free
# deb-src http://mirrors.aliyun.com/debian/ buster-updates main contrib non-free
deb http://mirrors.aliyun.com/debian/ buster-backports main contrib non-free
# deb-src http://mirrors.aliyun.com/debian/ buster-backports main contrib non-free
deb http://mirrors.aliyun.com/debian-security buster/updates main contrib non-free
# deb-src http://mirrors.aliyun.com/debian-security buster/updates main contrib non-free
```

**Kali apt 换源**
```vim
vim /etc/apt/sources.list

# 清华源
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src http://mirrors.aliyun.com/kali kali-rolling main contrib non-free

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

**enable the "Universe" repository**
```bash
add-apt-repository universe
apt-get update
```

**Gdebi**

> Gdebi 是一个安装 .deb 软件包的工具.提供了图形化的使用界面

```bash
apt update
apt install gdebi
```

### Binary

```bash
yum install make
yum install gcc
yum install gcc-c++
./configure --prefix=/opt	# 配置,表示安装到 /opt 目录
make						# 编译
make install				# 安装
```

### dnf

> DNF(Dandified Yum)是一种的 RPM 软件包管理器。

**安装 dnf**
```bash
yum install epel-release
yum install dnf
```

### dpkg

> dpkg 命令是 Debian Linux 系统用来安装、创建和管理软件包的实用工具.

**基本用法**
```bash
dpkg -i xxxxx.deb  			# 安装软件
dpkg -R /usr/local/src		# 安装路径下所有包
dpkg -L 					# 查看软件安装位置
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
rpm –ivh xxxx.rpm			# 安装本地包
rpm -e xxx					# 卸载
rpm -U						# 升级
rpm -V						# 验证
```

### snap

> Snappy 是一个软件部署和软件包管理系统，最早由 Canonical 公司为了 Ubuntu 移动电话操作系统而设计和构建。其包称为“snap”，工具名为“snapd”，可在多种 Linux 发行版上运行，完成发行上游主导的软件部署。该系统的设计面向手机、云、物联网和台式机。

**Centos下安装snap**
```bash
sudo yum install epel-release
sudo yum install snapd
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
```

**kali下安装snap**
```bash
sudo apt-get update
sudo apt install snapd
systemctl start snapd
export PATH=$PATH:/snap/bin
```

**Ubuntu下安装snap**
```bash
sudo apt-get update
sudo apt install snapd
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

**配置 Alibaba yum 源**

直接下载源
```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

刷新 YUM 的缓存状态:
```bash
yum clean all
yum makecache
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
apt install zsh		# 安装 zsh
chsh -s /bin/zsh	# 切换默认的 shell 为 zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"	# 安装 oh-my-zsh
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions	# 下载命令补全插件

# zshrc 配置文件中修改如下内容
vim ~/.zshrc

plugins=(git zsh-autosuggestions)

zsh					# 重新加载 zsh 配置

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

```bash
date							# 查看当前时间
date -R							# 查看当前时区
data -s "2019-03-31 13:12:29"	# 修改系统时间

ntpdate		# 设置本地日期和时间
	ntpdate 0.rhel.pool.ntp.org	# 网络同步时间

hwclock	   	# 硬件时钟访问工具
	hwclock –w 					# 将系统时钟同步到硬件时钟,将当前时间和日期写入 BIOS,避免重启后失效
	hwclock -s 					# 将硬件时钟同步到系统时钟

cal			# 查看日历
```

**Tips**
- **ntpd 与 ntpdate 的区别**
	- ntpd 在实际同步时间时是一点点的校准过来时间的,最终把时间慢慢的校正对.而 ntpdate 不会考虑其他程序是否会阵痛,直接调整时间.
	- 一个是校准时间,一个是调整时间.
	- https://blog.csdn.net/tuolaji8/article/details/79971591

### 语言

**查看系统语言**
```bash
echo  $LANG 			# 查看当前操作系统的语言
```

**修改系统语言**
```bash
vim /etc/locale.conf

set LANG en_US.UTF-8	# 更改默认语言
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
apt install xfonts-intl-chinese
apt install ttf-wqy-microhei
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

**crontab**
```bash
crontab -l   			# 列出某个用户 cron 服务的详细内容
crontab -r   			# 删除每个用户 cront 任务(谨慎：删除所有的计划任务)
crontab -e   			# 使用编辑器编辑当前的 crontab 文件

vim /etc/crontab		# 编辑系统任务调度的配置文件

# 前5个星号分别代表:分钟,小时,几号,月份,星期几
* * * * * command		# 每1分钟执行一次 command
3,15 * * * * command	# 每小时的第3和第15分钟执行
@reboot	command			# 开机启动

# 例子
0 */2 * * * /sbin/service httpd restart	# 意思是每两个小时重启一次 apache
50 7 * * * /sbin/service sshd start		# 意思是每天7:50开启 ssh 服务
50 22 * * * /sbin/service sshd stop		# 意思是每天22:50关闭 ssh 服务
0 0 1,15 * * fsck /home					# 每月1号和15号检查 /home 磁盘
1 * * * * /home/bruce/backup			# 每小时的第一分执行 /home/bruce/backup 这个文件
00 03 * * 1-5 find /home "*.xxx" -mtime +4 -exec rm {} \;	# 每周一至周五3点钟,在目录 /home 中,查找文件名为 *.xxx 的文件,并删除4天前的文件.
30 6 */10 * * ls						# 意思是每月 1、11、21、31 日的 6:30 执行一次 ls 命令
```

**at**

> 在特定的时间执行一次性的任务
```bash
at now +1 minutes
echo "test" > test.txt
<ctrl+d>

atq		# 列出用户的计划任务,如果是超级用户将列出所有用户的任务,结果的输出格式为:作业号、日期、小时、队列和用户名
atrm	# 根据 Job number 删除 at 任务
```

**/etc/rc.local**

在文件末尾 (exit 0 之前) 加上你开机需要启动的程序或执行的命令即可 (执行的程序需要写绝对路径,添加到系统环境变量的除外) ,如

**/etc/profile.d/**

将写好的脚本 (.sh 文件) 放到目录 `/etc/profile.d/` 下,系统启动后就会自动执行该目录下的所有 shell 脚本

### SELinux

**查看 SELinux 状态**
```bash
getenforce			# 查看 selinux 状态
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

## 账号管控

**账号**
```bash
id									# 显示真实有效的用户 ID(UID)和组 ID(GID)
whoami								# 当前用户
groups								# 当前组
cut -d: -f1 /etc/passwd				# 查看系统所有用户

useradd <username>					# 创建用户
useradd -d /home/<username> -s /sbin/nologin <username>		# 创建用户并指定家目录和 shell
passwd <username>					# 设置用户密码

addgroup <groupname>				# 创建组
addgroup <username> <groupname>		# 移动用户到组

newgrp <groupname>					# 创建组

usermod -g <groupname> <username>	# 修改用户的主组
usermod -G <supplementary> <username>	# 修改用户的附加组
usermod -s /bin/bash <username>		# 修改用户登录的 Shell
usermod -L <username>  				# 锁定用户
usermod -U <username> 				# 解锁用户

userdel <username>					# 只删除用户不删除家目录
userdel -r <username>				# 同时删除家目录
userdel -f <username>				# 强制删除,即使用户还在登陆中
sudo passwd							# 配置 su 密码

chage		# 修改帐号和密码的有效期限
	chage -l <username>				# 查看一下用户密码状态
	chage -d <username>				# 把密码修改曰期归零了,这样用户一登录就要修改密码

passwd -l <username>  				# 锁定用户
passwd -u <username>  				# 解锁用户

su <username>						# 切换账号
su - <username>                     # 切换账号并改变工作目录至使用者的家目录
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
	chattr +i <File>		# 增加后,使文件不能被删除、重命名、设定链接接、写入、新增数据
	chattr +a <File>		# 增加该属性后,只能追加不能删除,非root用户不能设定该属性
	chattr +c <File>		# 自动压缩该文件,读取时会自动解压.Note: This attribute has no effect in the ext2, ext3, and ext4 filesystems.

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
sudo -v # 查看 sudo 信息
sudo -l # 查看当前权限
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
```bash
service <程序> status/start/restart/stop	# 控制系统服务的实用工具
systemctl	# 系统服务管理器指令
	systemctl enable crond.service	# 让某个服务开机自启(.service 可以省略)
	systemctl disable crond			# 不让开机自启
	systemctl status crond			# 查看服务状态
	systemctl start crond			# 启动某个服务
	systemctl stop crond			# 停止某个服务
	systemctl restart crond			# 重启某个服务
	systemctl reload *				# 重新加载服务配置文件
	systemctl is-enabled crond		# 查询服务是否开机启动

chkconfig	# 检查、设置系统的各种服务
	chkconfig --list		# 列出所有的系统服务
	chkconfig --add httpd	# 增加 httpd 服务
	chkconfig --del httpd	# 删除 httpd 服务
	chkconfig --level httpd 2345 on	# 设置 httpd 在运行级别为 2、3、4、5 的情况下都是 on(开启)的状态,另外如果不传入参数 --level,则默认针对级别 2/3/4/5 操作.

# 从 CentOS7 开始,CentOS 的服务管理工具由 SysV 改为了 systemd,但即使是在 CentOS7 里,也依然可以使用 chkconfig 这个原本出现在 SysV 里的命令.
```

**监视进程**

```bash
ps -aux	    # 查看进程
ps aux | grep root	# 查看 root 运行的程序
ps -ef | grep root	# 查看 root 运行的程序

jobs	    # 显示 Linux 中的任务列表及任务状态
	jobs -l		    # 显示进程号

pidof program	    # 找出 program 程序的进程 PID
pidof -x script     # 找出 shell 脚本 script 的进程 PID

top					# 实时动态地查看系统的整体运行情况

free
free -h			# 显示当前系统未使用的和已使用的内存数目

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

```bash
# 杀进程
kill
kill -s STOP <PID>						# 删除执行中的程序或工作
	kill -l								# 显示信号
	kill -HUP <pid>						# 更改配置而不需停止并重新启动服务
	kill -9 <PID> && kill -KILL <pid> 	# 信号(SIGKILL)无条件终止进程
killall <PID>							# 使用进程的名称来杀死进程

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
```bash
nohup	# nohup 命令运行由 Command参数和任何相关的 Arg参数指定的命令,忽略所有挂断(SIGHUP)信号.在注销后使用 nohup 命令运行后台中的程序.要运行后台中的 nohup 命令,添加 & ( 表示"and"的符号)到命令的尾部.
	nohup COMMAND &			# 使命令永久的在后台执行
	sh test.sh &			# 将 sh test.sh 任务放到后台 ,关闭xshell,对应的任务也跟着停止.
	nohup sh test.sh		# 将 sh test.sh 任务放到后台,关闭标准输入,终端不再能够接收任何输入(标准输入),重定向标准输出和标准错误到当前目录下的 nohup.out 文件,即使关闭 xshell 退出当前 session 依然继续运行.
	nohup sh test.sh  & 	# 将 sh test.sh 任务放到后台,但是依然可以使用标准输入,终端能够接收任何输入,重定向标准输出和标准错误到当前目录下的 nohup.out 文件,即使关闭 xshell 退出当前 session 依然继续运行.

setsid		# setsid 主要是重新创建一个 session,子进程从父进程继承了 SessionID、进程组 ID 和打开的终端,子进程如果要脱离父进程,不受父进程控制,我们可以用这个 setsid 命令
	setsid ping baidu.com	# setsid 后子进程不受终端影响,终端退出,不影响子进程
	# 别急,  ps -ef | grep ping ,找到 PID kill 相应的 PID 就可以关掉了😂

disown		# 使作业忽略 HUP 信号
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

## 设备管理
### 硬盘-数据

**磁盘的文件名**

Linux 中每个硬件都被当做一个文件，包括磁盘。磁盘以磁盘接口类型进行命名，常见磁盘的文件名如下：
- IDE 磁盘 : /dev/hd[a-d]
- SATA/SCSI/SAS 磁盘 : /dev/sd[a-p]
其中文件名后面的序号的确定与系统侦测到磁盘的顺序有关，而与磁盘所插入的插槽位置无关。

**磁盘配额**
- quota : 能对某一分区下指定用户或用户组进行磁盘限额。

**分区**
```bash
fdisk -l			# 查看磁盘情况
fdisk /dev/sdb		# 创建系统分区
	n	# 添加一个分区
	p	# 建立主分区
	1	# 分区号
	后面都是默认,直接回车

	t	# 转换分区格式
	8e	# LVM 格式

	w	# 写入分区表
```

如果机器没有安装 swap 分区可以自己分配一个
```bash
dd if=/dev/zero of=/home/swap bs=1024 count=512000
/sbin/mkswap /home/swap
/sbin/swapon /home/swap
```
```bash
free -h	# 查看 swap 分区
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
```bash
df	# 报告驱动器的空间使用情况
	df -H	# 以人类可读的格式进行显示
	df -ah	# 查看磁盘占用大的文件夹

du	# 报告目录的空间使用情况
	du -h . | sort			# 以人类可读的格式进行显示,排序显示
	du -hd 1 / | sort -hr
	du -sh /etc/yum			# 特定目录的总使用量
	du --max-depth=1 -h		# 查看文件夹下各个文件夹的磁盘占用
```

**dd**

> dd 主要功能为转换和复制文件。

```bash
dd
	dd if=/dev/zero of=sun.txt bs=1M count=1
	# if 代表输入文件.如果不指定 if,默认就会从 stdin 中读取输入.
	# of 代表输出文件.如果不指定 of,默认就会将 stdout 作为默认输出.
	# ibs=bytes:一次读入 bytes 个字节,即指定一个块大小为 bytes 个字节.
	# obs=bytes:一次输出 bytes 个字节,即指定一个块大小为 bytes 个字节.
	# bs 代表字节为单位的块大小.
	# count 代表被复制的块数.
	# /dev/zero 是一个字符设备,会不断返回 0 值字节(\0).
```

**LVM**

> LVM 是 Logical Volume Manager 的缩写，中文一般翻译为 "逻辑卷管理"，它是 Linux 下对磁盘分区进行管理的一种机制。LVM 是建立在磁盘分区和文件系统之间的一个逻辑层，系统管理员可以利用 LVM 在不重新对磁盘分区的情况下动态的调整分区的大小。如果系统新增了一块硬盘，通过 LVM 就可以将新增的硬盘空间直接扩展到原来的磁盘分区上。

```bash
pvcreate /dev/sdb1						# 初始化物理卷
vgcreate -s 16M datastore /dev/sdb1		# 创建物理卷
lvcreate -L 8G -n database datastore	# 创建逻辑卷
lvdisplay 								# 查看逻辑卷的属性
```

**块设备信息**
```bash
lsblk	# 显示所有可用块设备的信息
	lsblk -m	# 显示设备所有者相关的信息,包括文件的所属用户、所属组以及文件系统挂载的模式

blkid   # 输出所有可用的设备、UUID、文件系统类型以及卷标
	blkid /dev/sda1
	blkid -U d3b1dcc2-e3b0-45b0-b703-d6d0d360e524
	blkid -po udev /dev/sda1	# 获取更多详细信息
	blkid -g					# 清理 blkid 的缓存
```
