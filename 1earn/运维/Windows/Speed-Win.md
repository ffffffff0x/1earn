# Speed-Win

<p align="center">
    <a href="https://www.pixiv.net/en/artworks/45083849"><img src="../../../assets/img/banner/Speed-Win.jpg" width="90%"></a>
</p>

---

# 大纲

* **[基础使用](#基础使用)**
	* [环境变量](#环境变量)
	* [符号](#符号)
	* [会话](#会话)
	* [文件和目录](#文件和目录)
		* [查看](#查看)
		* [创建](#创建)
		* [删除](#删除)
		* [查询](#查询)
		* [修改](#修改)
		* [链接](#链接)

* **[网络管理](#网络管理)**
    * [查看网络信息](#查看网络信息)
    * [网络排错工具](#网络排错工具)
    * [防火墙](#防火墙)

* **[系统管理](#系统管理)**
    * [系统信息](#系统信息)
		* [日志](#日志)
	* [系统设置](#系统设置)
		* [时间](#时间)
        * [注册表](#注册表)
        * [计划任务](#计划任务)
        * [组策略](#组策略)
    * [账号管控](#账号管控)
	* [进程管理](#进程管理)
	* [设备管理](#设备管理)
		* [硬盘-数据](#硬盘-数据)

* **[域](#域)**

---

# 基础使用

```cmd
echo "Hello World"      输出 Hello World 到终端屏幕
cls                     清除屏幕
```

**shutdown**
```cmd
shutdown    关闭、重启、注销、休眠计算机
    shutdown -s -t 60       60秒后关机
    shutdown -s -t 3600     1小时后关机
    tsshutdn                60秒后关机
    shutdown -s -f          强制关机
    shutdown -s -t          时间
    shutdown -a             取消 关机命令
```

**运行脚本**
```cmd
cscript     执行 vbs 脚本
    cscript /Nologo test.vbs    执行 test.vbs 脚本

call ff.bat                     调用执行 ff.bat 脚本（ff.bat 脚本执行完原脚本才会往下执行）

start  运行某程序或命令
    start /max notepad.exe          最大化的方式启动记事本
    start /min calc.exe             最小化的方式启动计算器
    start /min "" d:\Proxifier.exe  最小化的方式启动 Proxifier 代理工具
    start  tasklist                 启动一个 cmd 实例窗口，并运行 tasklist
    start explorer f:\              调用资源管理器打开f盘
    strat iexplore "www.qq.com"     启动 ie 并打开 www.qq.com 网址
    start ff.bat                    启动开始执行 ff.bat（启动 ff.bat 脚本后，原脚本继续执行，不会等 ff.bat 脚本执行完）
```

## 环境变量

```cmd
set         显示当前用户所有的环境变量

    set path            查看 path 的环境变量值（准确的说是查看以 path 开头的环境变量）
    set path=           清空 path 变量

    set path=d:\execute
    将 path 变量设置为 d:\execute（注：修改的 path 只会影响当前回话，也不会存储到系统配置中去；当前 cmd 窗口关闭，新设置的 path 也就不存在了）

    set path=%path%;d:\execute
    在 path 变量中添加 d:\execute（注：修改的 path 只会影响当前回话，也不会存储到系统配置中去；当前 cmd 窗口关闭，新设置的 path 也就不存在了）

path        显示当前 path 变量的值

    path ;              清除所有搜索路径设置并指示 cmd.exe 只在当前目录中搜索
    path d:\xxx;%PATH%  将 d:\xxx 路径添加到 path 中
```

---

## 符号

**&**
```cmd
顺序执行多条命令，而不管命令是否执行成功

cd /d d:\src&work.exe /o c:\result.txt
先将当前工作目录切换到d:\src下，然后执行work.exe /o c:\result.txt命令
```

**&&**
```cmd
顺序执行多条命令，当碰到执行出错的命令后将不执行后面的命令

find "ok" c:\test.txt && echo 成功
如果找到了"ok"字样，就显示"成功"，找不到就不显示
```

**||**
```cmd
顺序执行多条命令，当碰到执行正确的命令后将不执行后面的命令

find "ok" c:\test.txt || echo 不成功
如果找不到"ok"字样，就显示"不成功"，找到了就不显示
```

**|**
```cmd
管道命令

dir *.* /s/a | find /c ".exe"
先执行 dir 命令，然后对输出结果（stdout）执行 find 命令（输出当前文件夹及所有子文件夹里的 .exe 文件的个数）

dir *.* /s/a 2>&1 | find /c ".exe"
先执行 dir 命令，然后对输出结果（stdout）和错误信息（stderr）执行 find 命令（输出当前文件夹及所有子文件夹里的.exe文件的个数）
```

**>**
```cmd
将当前命令输出以覆盖的方式重定向

tasklist > p1.txt
将 tasklist 的输出结果（stdout）以覆盖的方式重定向到 p1.txt 文件中（注：tasklist 的输出结果就不会打印到屏幕上了）

tasklist 1> p1.txt
等同于：tasklist > p1.txt

dir bin 2> p1.txt
输出结果（stdout）打印在屏幕上，错误信息（stderr）以覆盖的方式重定向到 p1.txt 中（注：bin 目录不存在时，会输出错误信息）

dir bin > p1.txt 2>&1
将错误信息（stderr）重定向到输出结果（stdout），然后将输出结果（stdout）以覆盖的方式重定向到 p1.txt 中（注：bin 目录不存在时，会输出错误信息）

dir bin 2> p1.txt 1>&2
将输出结果（stdout）重定向到错误信息（stderr），然后将错误信息（stderr）以覆盖的方式重定向到 p1.txt 中（注：bin 目录不存在时，会输出错误信息） 注：与上条命令结果一致

tasklist >nul
屏幕上不打印 tasklist 的输出结果（stdout），错误信息（stderr）仍会打印

dir bin 2>nul
屏幕上不打印命令的错误信息（stderr），输出结果（stdout）仍会打印（注：bin 目录不存在时，会输出错误信息）

dir bin >nul 2>&1
将命令的错误信息（stderr）重定向到输出结果（stdout），然后不打印输出结果（stdout）[屏幕上错误信息（stderr）和输出结果（stdout）都不打印]（注：bin 目录不存在时，会输出错误信息）

dir bin 2>nul 1>&2
将命令的输出结果（stdout）重定向到错误信息（stderr），然后不打印错误信息（stderr）[屏幕上错误信息（stderr）和输出结果（stdout）都不打印]（注：bin 目录不存在时，会输出错误信息）
```

**>>**
```cmd
将当前命令输出以追加的方式重定向

tasklist >> p2.txt
将 tasklist 的输出结果（stdout）以追加的方式重定向到 p2.txt 文件中（注：tasklist 的输出结果就不会打印到屏幕上了）

tasklist 1>> p2.txt
等同于：tasklist >> p2.txt

dir bin 2>> p2.txt
输出结果（stdout）打印在屏幕上，错误信息（stderr）以追加的方式重定向到 p2.txt 中（注：bin 目录不存在时，会输出错误信息）

dir bin >> p2.txt 2>&1
将错误信息（stderr）重定向到输出结果（stdout），然后将输出结果（stdout）以追加的方式重定向到 p2.txt 中（注：bin 目录不存在时，会输出错误信息）

dir bin 2>> p2.txt 1>&2
将输出结果（stdout）重定向到错误信息（stderr），然后将错误信息（stderr）以追加的方式重定向到 p2.txt 中（注：bin 目录不存在时，会输出错误信息） 注：与上条命令结果一致
```

**<**
```cmd
从文件中获得输入信息，而不是从屏幕上，一般用于 date time label 等需要等待输入的命令

date <temp.txt
temp.txt 中的内容为 2005-05-01
```

**@**
```cmd
命令修饰符  在执行命令前，不打印出该命令的内容

@cd /d d:\me
执行该命令时，不打印出命令的内容：cd /d d:/me
```

**,**
```cmd
在某些特殊的情况下可以用来代替空格使用

dir,c:\
相当于：dir c:\
```

**;**
```cmd
当命令相同的时候,可以将不同的目标用 ; 隔离开来但执行效果不变。如执行过程中发生错误则只返回错误报告但程序还是会继续执行

dir c:\;d:\;e:\
相当于顺序执行：dir c:\    dir d:\     dir e:\
```

---

## 会话

**会话信息**
```cmd
query user                                  查看会话
```

**踢下线**
```
logoff <ID号>                               踢掉
```

**会话设置**
```cmd
title 正在做命令行测试        修改当前 cmd 窗口的标题栏文字为正在做命令行测试
prompt orz:                 将命令提示符修改为 orz:

exit    退出当前 cmd 窗口实例

    exit 0                  退出当前 cmd 窗口实例，并将过程退出代码设置为 0（0 表示成功，非 0 表示失败）
    exit /B 1               退出当前 bat 脚本，并将 ERRORLEVEL 系统变量设置为 1

pause   暂停批处理程序，并显示出：请按任意键继续....

color   设置当前 cmd 窗口背景色和前景色（前景色即为字体的颜色）
    color                   恢复到缺省设置
    color 02                将背景色设为黑色，将字体设为绿色

chcp    查看命令行环境字符编码（为一个全局设置）
    936 -- GBK(一般情况下为默认编码)
    437 -- 美国英语
    65001 -- utf-8
    1200 -- utf-16
    1201 -- utf-16(Big-Endian)
    12000 -- utf-32
    12001 -- utf-32(Big-Endian)
```

**永久修改 CMD 的默认字符集**

regedit

[HKEY_CURRENT_USER\Console] "CodePage"=dword:0000fde9


---

## 文件和目录

**目录**
```cmd
cd              切换目录
    cd ..               进入父目录
    cd /d d:            进入上次d盘所在的目录（或在直接输入：d:）
    cd /d d:\           进入d盘根目录
    cd d:               显示上次d盘所在的目录
    cd /d d:\src        进入 d:\src 目录
    cd prj\src\view     进入当前目录下的 prj\src\view 文件夹
```

### 查看

**目录、文件信息**
```cmd
dir             显示目录中的内容
    dir                 显示当前目录中的子文件夹与文件
    dir /b              只显示当前目录中的子文件夹与文件的文件名
    dir /p              分页显示当前目录中的子文件夹与文件
    dir /ad             显示当前目录中的子文件夹
    dir /a-d            显示当前目录中的文件
    dir c:\test         显示 c:\test 目录中的内容
    dir keys.txt        显示当前目录中 keys.txt 的信息
    dir /S              递归显示当前目录中的内容
    dir key*            显示当前目录下以 key 开头的文件和文件夹的信息
    dir /AH /OS         只显示当前目录中隐藏的文件和目录，并按照文件大小从小到大排序

tree            显示目录结构
    tree d:\myfiles     显示 d:\myfiles 目录结构

attrib          查看或修改文件或目录的属性  [A：存档  R：只读  S：系统  H：隐藏]
    attrib 1.txt        查看当前目录下 1.txt 的属性
    attrib -R 1.txt     去掉 1.txt 的只读属性
    attrib +H movie     隐藏 movie 文件夹
```

**文件内容**
```cmd
type            显示文本文件内容
    type c:\11.txt          显示c盘中11.txt的文本内容
    type conf.ini           显示当前目录下conf.ini的文本内容
    type c:\11.txt | more   分页显示c盘中11.txt的文本内容

more            逐屏的显示文本文件内容

    more conf.ini       逐屏的显示当前目录下conf.ini的文本内容   [空格：下一屏 q：退出 ]
```

---

### 创建

```cmd
md              用于创建文件夹，不能创建文本文档或者其他
    md movie music          在当前目录中创建名为 movie 和 music 的文件夹
    md c:\aaa               在 C 盘的根目录下创建名为 aaa 的子目录；
    md c:\aaa\USER          在 aaa 子目录下再创建 USER 子目录。
```

---

### 删除

```cmd
del             删除文件   注意：目录及子目录都不会删除
    del test
    删除当前目录下的 test 文件夹中的所有非只读文件（子目录下的文件不删除；删除前会进行确认；等价于 del test\*）

    del /f test
    删除当前目录下的 test 文件夹中的所有文件（含只读文件；子目录下的文件不删除；删除前会进行确认；等价于 del /f test\*）

    del /f /s /q test d:\test2\*.doc
    删除当前目录下的 test 文件夹中所有文件及 d:\test2 中所有 doc 文件（含只读文件；递归子目录下的文件；删除前不确认）

    del /ar *.*             删除当前目录下所有只读文件
    del /a-s *.*            删除当前目录下除系统文件以外的所有文件

```

---

### 查询

```cmd
find        文件中搜索字符串
    find /N /I "pid" 1.txt  在 1.txt 文件中忽略大小写查找 pid 字符串，并带行号显示查找后的结果
    find /C "exe" 1.txt     只显示在 1.txt 文件中查找到 exe 字符串的次数
    find /V "exe" 1.txt     显示未包含 1.txt 文件中未包含 exe 字符串的行

findstr     文件中搜索字符串
    findstr "hello world" 1.txt         在 1.txt 文件中搜索 hello 或 world
    findstr /c:"hello world" 1.txt      在 1.txt 文件中搜索 hello world
    findstr /c:"hello world" 1.txt nul  在 1.txt 文件中搜索 hello world，并在每行结果前打印出1.txt:   注：findstr 只有在2个及以上文件中搜索字符串时才会打印出每个文件的文件名，nul 表示一个空文件
    findstr /s /i "Hello" *.*           不区分大小写，在当前目录和所有子目录中的所有文件中的 hello
    findstr  "^[0-9][a-z]" 1.txt        在 1.txt 中搜索以1个数字+1个小写字母开头子串的行
```

---

### 修改

```cmd
ren             文件或目录重命名
    ren rec.txt rec.ini     将当前目录下的 rec.txt 文件重命名为 rec.ini
    ren c:\test test_01     将 c 盘下的 test 文件夹重命名为 test_01

copy            拷贝文件
    copy /Y key.txt c:\doc  将当前目录下的 key.txt 拷贝到 c:\doc 下（不询问，直接覆盖写）
    copy key.txt +          复制文件到自己，实际上是修改了文件日期

    copy key.txt c:\doc
    将当前目录下的 key.txt 拷贝到 c:\doc 下（若doc中也存在一个 key.txt 文件，会询问是否覆盖）

    copy jobs c:\doc
    将当前目录下 jobs 文件夹中文件（不递归子目录）拷贝到 c:\doc 下（若 doc 中也存在相应的文件，会询问是否覆盖）

    copy key.txt c:\doc\key_bak.txt
    将当前目录下的 key.txt 拷贝到 c:\doc 下，并重命名为 key_bak.txt（若 doc 中也存在一个 key_bak.txt 文件，会询问是否覆盖）

    copy /Y key1.txt + key2.txt key.txt
    将当前目录下的 key1.txt 与 key2.txt 的内容合并写入 key.txt 中（不询问，直接覆盖写）

    copy /B art_2.7z.* art_2.7z
    将当前目录下的 art_2.7z. 开头的所有文件（按照名称升序排序）依次合并生成 art_2.7z

    copy /B art_2.7z.001+art_2.7z.002 art_2.7z
    将当前目录下的 art_2.7z.001、art_2.7z.002 文件合并生成 art_2.7z

    copy test.txt \\host\c$\windows\temp\test.txt       远程拷贝

xcopy           更强大的复制命令
    xcopy c:\bat\hai d:\hello\ /y /h /e /f /c
    将 c:\bat\hai 中的所有内容拷贝到 d:\hello 中  注意：需要在 hello 后加上 \ 表示 hello 为一个目录，否则 xcopy 会询问 hello 是 F，还是 D

    xcopy c:\bat\hai d:\hello\ /d:12-29-2010
    将 c:\bat\hai 中的2010年12月29日后更改的文件拷贝到 d:\hello 中

robocopy        更强大的复制命令
    robocopy .\Plugins .\PluginsDest /MIR /xd Intermediate Binaries
    将当前目录下 Plugins 中所有内容（排除名为 Intermediate 和 Binaries 的文件夹）保留目录结构拷贝到当前目录下的 PluginsDest 中（PluginsDest 不存在会自动创建）

    robocopy c:\test d:\test2 /MIR /xd Intermediate /xf UE4Editor-SGame-Win64-DebugGame.dll *.pdb
    将c:\test中所有内容（排除名为 UE4Editor-SGame-Win64-DebugGame.dll 和 pdb 后缀的文件）保留目录结构拷贝到 d:\test2中（d:\test2 不存在会自动创建）

move            移动文件
    move *.png test
    将当前目录下的 png 图片移动到当前目录下 test 文件夹中 （若 test 中也存在同名的 png 图片，会询问是否覆盖）

    move /Y *.png test
    将当前目录下的 png 图片移动到当前目录下 test 文件夹中 （不询问，直接覆盖写）

    move 1.png d:\test\2.png
    将当前目录下的 1.png 移动到 d 盘 test 文件夹中，并重命名为 2.png （若 test 中也存在同名的png图片，会询问是否覆盖）

    move test d:\new
    若 d 盘中存在 new 文件夹，将当前目录下的 test 文件夹移动到 d 盘 new 文件夹中；若不存在，将当前目录下的 test 文件夹移动到 d 盘，并重命名为 new

replace         替换文件[即使这个文件在使用，仍然可以替换成功]
    replace d:\love.mp3 d:\mp3
    使用 d 盘下的 love.mp3 强制替换 d 盘 mp3 目录中的 love.mp3 文件
```

```cmd
assoc           设置'文件扩展名'关联到的'文件类型'
    assoc                   显示所有'文件扩展名'关联
    assoc .txt              显示.txt代表的'文件类型'，结果显示.txt=txtfile
    assoc .doc              显示.doc代表的'文件类型'，结果显示.doc=Word.Document.8
    assoc .exe              显示.exe代表的'文件类型'，结果显示.exe=exefile
    assoc .txt=txtfile      恢复.txt的正确关联

ftype           设置'文件类型'关联到的'执行程序和参数'
    ftype                                           显示所有'文件类型'关联
    ftype exefile                                   显示exefile类型关联的命令行，结果显示 exefile="%1" %*
    ftype txtfile=C:\Windows\notepad.exe %1         设置txtfile类型关联的命令行为：C:\Windows\notepad.exe %1

    当双击一个.txt文件时，windows并不是根据.txt直接判断用notepad.exe打开
    而是先判断.txt属于txtfile'文件类型'；再调用txtfile关联的命令行：txtfile=%SystemRoot%\system32\NOTEPAD.EXE %1

forfiles        递归目录执行命令

    forfiles /p . /m .svn /s /c "cmd /c svn up -r12005"
    在当前目录下查找含有.svn的文件或目录（递归子目录），并对该目录执行指定版本号svn更新

    forfiles /p c:\myfiles /m .svn /s /c "cmd /c svn up -r12005"
    在c:\myfiles目录下查找含有.svn的文件或目录（递归子目录），并对该目录执行指定版本号svn更新
```

### 链接

win7 下的 mklink 命令通过指定参数可以建立出不同形式的文件或目录链接，分为硬链接(hard link)、符号链接(symbolic link)和目录联接(junction)三种。

- 符号链接(symbolic link)

    建立一个软链接相当于建立一个文件（或目录），这个文件（或目录）用于指向别的文件（或目录），和 win 的快捷方式有些类似。删除这个链接，对原来的文件（或目录）没有影像没有任何影响；而当你删除原文件（或目录）时，再打开链接则会提示“位置不可用”。

- 目录联接(junction)

    作用基本和符号链接类似。区别在于，目录联接在建立时会自动引用原目录的绝对路径，而符号链接允许相对路径的引用。

- 硬链接(hard link)

    建立一个硬链接相当于给文件建立了一个别名，例如对 1.txt 创建了名字为 2.txt 的硬链接；

    若使用记事本对 1.txt 进行修改，则 2.txt 也同时被修改，若删除 1.txt，则 2.txt 依然存在，且内容与 1.txt 一样。

建立链接请注意：
1. 建立文件或目录链接限于 NTFS 文件系统；符号链接（目录联接）的建立可以跨分区（如：在 d 盘可以建立 c 盘文件或目录的链接），硬链接只能建立同一分区内的文件指向
2. 硬链接只能用于文件，不能用于目录；目录联接只能用于目录；符号链接则均可以；
3. 硬链接不允许对空文件建立链接，符号（软链接可以。
）
```cmd
mklink          创建符号链接（win7 引入）；创建的符号链接文件上会有一个类似快捷方式的箭头
    mklink /j "C:\Users" "D:\Users"     创建 D 盘 Users 目录联接到 C 盘，并命名为 Users
```

---

# 网络管理

**net**
```cmd
net use \\IP\ipc$ " " /user:" "             建立 IPC 空链接
net use \\IP\ipc$ "密码" /user:"用户名"       建立 IPC 非空链接
net use z: \\ip\ipc$ "pass" /user:"user"    直接登陆后映射对方 C: 到本地为 H:
net use h: ipc$                             登陆后映射对方 C: 到本地为 H:
net use \\IP\ipc$ /del                      删除 IPC 链接
net use h: /del                             删除映射对方到本地的为 H: 的映射
net user 用户名　密码　/add                    建立用户
net user guest /active:yes                  激活 guest 用户
net user                                    查看有哪些用户
net user 帐户名                              查看帐户的属性
net localgroup administrators 用户名 /add    把"用户"添加到管理员中使其具有管理员权限
net start                                   查看开启了哪些服务
net start 服务名　                           开启服务;(如:net start telnet, net start schedule)
net stop 服务名                              停止某服务
net time 目标ip                              查看对方时间
net time 目标ip /set                         设置本地计算机时间与"目标IP"主机的时间同步,加上参数 /yes 可取消确认
net view                                    查看本地局域网内开启了哪些共享
net view <ip>                               查看对方局域网内开启了哪些共享
net config                                  显示系统网络设置
net logoff                                  断开连接的共享
net pause 服务名                             暂停某服务
net send ip "文本信息"                       向对方发信息
net ver                                     局域网内正在使用的网络连接类型和信息
net share                                   查看本地开启的共享
net share ipc$                              开启 ipc$ 共享
net share db$=d:\config                     开启一个共享名为 db$，在 d:\config
net share ipc$ /del                         删除 ipc$ 共享
net share c$ /del                           删除 C: 共享
net user guest 12345                        用 guest 用户登陆后用将密码改为 12345
net password 密码                            更改系统登陆密码
```

## 查看网络信息

**ipconfig**
```cmd
ipconfig /all       显示完整配置信息
ipconfig /release   释放指定适配器的 IPv4 地址
ipconfig /release6  释放指定适配器的 IPv6 地址
ipconfig /renew     更新指定适配器的 IPv4 地址
ipconfig /renew6    更新指定适配器的 IPv6 地址
ipconfig /flushdns  清除 DNS 解析程序缓存
```

**netstat**
```cmd
netstat -a          查看开启了哪些端口,常用 netstat -an
netstat -n          查看端口的网络连接情况,常用 netstat -an
netstat -v          查看正在进行的工作
netstat -p 协议名    例:netstat -p tcq/ip 查看某协议使用情况
netstat -s          查看正在使用的所有协议使用情况
netstat -A ip       对方136到139其中一个端口开了的话,就可查看对方最近登陆的用户名

netstat -bn         查看每个程序的连接
```

**route**
```cmd
route print
route print 192.*
route add 0.0.0.0 mask 0.0.0.0 192.168.6.1          增加网关
route delete 0.0.0.0 mask 0.0.0.0 192.168.6.1       删除网关
route change 16.21.0.0 mask 255.255.0.0 16.28.0.25  将 16.21.0.0 段的网关改为 0.25
```

**arp**
```cmd
arp -a      查看全部 arp 条目
arp -d ip   删除
```

**nslookup**
```cmd
nslookup domain [dns-server]            查询域名A记录
nslookup -qt=type domain [dns-server]   查询其他记录
    A           地址记录
    AAAA        地址记录
    AFSDB       Andrew文件系统数据库服务器记录
    ATMA        ATM地址记录
    CNAME       别名记录
    HINFO       硬件配置记录,包括 CPU、操作系统信息
    ISDN        域名对应的 ISDN 号码
    MB          存放指定邮箱的服务器
    MG          邮件组记录
    MINFO       邮件组和邮箱的信息记录
    MR          改名的邮箱记录
    MX          邮件服务器记录
    NS          名字服务器记录
    PTR         反向记录
    RP          负责人记录
    RT          路由穿透记录
    SRV         TCP服务器信息记录
    TXT         域名对应的文本信息
    X25         域名对应的X.25地址记录
```

## 网络排错工具

**ping**
```cmd
ping ip(或域名)          向对方主机发送默认大小为32字节的数据
ping -l 数据包大小 ip
ping -n                 发送数据次数 ip
ping -t ip              一直 ping.
ping -t -l 65500 ip     发送大于64K的文件并一直 ping
```

**tracert**
```cmd
-d                 不将地址解析成主机名.
-h maximum_hops    搜索目标的最大跃点数.
-j host-list       与主机列表一起的松散源路由(仅适用于 IPv4).
-w timeout         等待每个回复的超时时间(以毫秒为单位).
-R                 跟踪往返行程路径(仅适用于 IPv6).
-S srcaddr         要使用的源地址(仅适用于 IPv6).
-4                 强制使用 IPv4.
-6                 强制使用 IPv6.
```

---

## 防火墙

**netsh**

查看防火墙状态
```cmd
netsh firewall show state
netsh advfirewall show allprofiles
```

开启防火墙
```cmd
netsh firewall set opmode enable
netsh firewall set allprofiles state on
```

关闭防火墙
```cmd
netsh firewall set opmode disable
netsh advfirewall set allprofiles state off
```

设置防火墙日志路径
```cmd
netsh advfirewall set currentprofile logging filename "C:\Windows\firewall.log"
```

添加防火墙规则
```cmd
netsh advfirewall firewall add rule name="Remote Desktop" dir=in action=allow protocol=tcp localport=3389
```

删除防火墙规则
```cmd
netsh advfirewall firewall delete rule name="rule_name"
```

添加端口规则
```cmd
netsh firewall portopening tcp 1234 rule_name
```

删除端口规则
```cmd
netsh firewall delete portopening tcp 1234
```

添加程序规则
```cmd
netsh firewall add allowedprogram "C:\\nc.exe" "allow nc" enable
```

删除程序规则
```cmd
netsh firewall delete allowedprogram "C:\\nc.exe"
```

添加端口转发
```cmd
netsh interface portproxy add v4tov4 [listenaddress=victim_ip] listenport=victim_port connectaddress=attack_ip connectport=attack_port
```

删除端口转发
```cmd
netsh interface portproxy delete v4tov4 [listenaddress=victim_ip] listenport=victim_port
```

查看端口转发
```cmd
netsh interface portproxy show all
netsh interface portproxy show v4tov4
netsh interface portproxy show v4tov6
netsh interface portproxy show v6tov4
netsh interface portproxy show v6tov6
```

安装 IPv6
```cmd
netsh interface ipv6 install
```

查看无线网络信息
```cmd
netsh wlan show profiles
```

查看指定 WIFI 密码
```cmd
netsh wlan show profiles wifi_name key=clear
```

---

# 系统管理

## 系统信息

- 内容参见 [信息](./笔记/信息.md)

### 日志

- 内容参见 [日志](./笔记/日志.md)

---

## 系统设置

### 时间

```cmd
time    显示或设置当前时间

    time /t             显示当前时间
    time                设置新的当前时间（格式：hh:mm:ss），直接回车则表示放弃设置

date    显示或设置当前日期

    date /t             显示当前日期
    date                设置新的当前日期（格式：YYYY/MM/DD），直接回车则表示放弃设置
```

### 注册表

reg 注册表相关操作

参数说明：
```
KeyName [\Machine]FullKey
           Machine 为远程机器的机器名 - 忽略默认到当前机器。
           远程机器上只有 HKLM 和 HKU。
           FullKey ROOTKEY+SubKey
           ROOTKEY [ HKLM | HKCU | HKCR | HKU | HKCC ]
           SubKey 所选ROOTKEY下注册表项的完整名
/v          所选项之下要添加的值名
/ve         为注册表项添加空白值名<无名称>
/t          RegKey 数据类型
           [ REG_SZ | REG_MULTI_SZ | REG_DWORD_BIG_ENDIAN |
           REG_DWORD | REG_BINARY | REG_DWORD_LITTLE_ENDIAN |
           REG_NONE | REG_EXPAND_SZ ]
           如果忽略，则采用 REG_SZ
/s          指定一个在 REG_MULTI_SZ 数据字符串中用作分隔符的字符；如果忽略，则将""用作分隔符
/d          要分配给添加的注册表 ValueName 的数据
/f          不提示，强行改写现有注册表项
```
```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v MyApp /t REG_SZ /d "c:\tools\myapp.exe" /f
强制添加一条开机启动 c:\tools\myapp.exe 程序的注册表项

reg add "HKLM\SOFTWARE\ScmClient" /v AgreementConfirmed /t REG_SZ /d 1 /f
解决 32 位 xp 打开 ioa 后，弹出的框关不掉问题

reg add "HKCU\ControlPanel\Desktop" /v WaitToKIllAppTimeOut /t REG_SZ /d 10000 /f
强制添加一条加速关闭应用程序的注册表项

reg add "hkcu\software\Unity Technologies\Unity Editor 4.x" /v JdkPath_h4127442381 /t REG_SZ /f
将 JdkPath_h4127442381 设置为空

reg add "HKCR\*\shell\WinDbg\command" /t REG_SZ /d "\"D:\Program Files (x86)\windbg\windbg.exe\" -z \"%1\" " /f
强制添加 windbg 打开 dump 文件到右键菜单的注册表项（不指明 /v，键值将写入默认值名中）

reg add "HKCR\*\shell\WinHex\command" /t REG_SZ /d "\"D:\software-setup\system\winhex\winhex.exe\"  \"%1\" " /f
强制添加 winhex 到右键菜单的注册表项（不指明 /v，键值将写入默认值名中）

reg add "hkcu\software\microsoft\windows\currentversion\internet settings" /v AutoConfigURL /t REG_SZ /d "http://txp-01.tencent.com/proxy.pac" /f
为 IE 设置代理：http://txp-01.tencent.com/proxy.pac

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f
关闭 IE 代理服务器选项

reg add "hkcu\software\Sysinternals\Process Monitor" /v EulaAccepted /t REG_DWORD /d 1 /f
为 Procmon.exe 工具（Process Monitor 为其属性面板上的描述名）添加 License 同意

reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v MyApp /f
强制删除值名的 MyApp 的注册表项

reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\taskmgr.exe" /f
强制删除让任务栏里的任务管理器为灰色的注册表项

reg delete HKEY_CURRENT_USER\Environment /v HTTP_proxy /f
删除 http 代理

reg delete HKEY_CURRENT_USER\Environment /v HTTPS_proxy /f
删除 https 代理

reg copy "hkcu\software\microsoft\winmine" "hkcu\software\microsoft\winminebk" /s /f
强制复制 winmine 下所有的子项与值到 winminebk 中

reg export "hkcu\software\microsoft\winmine" c:\regbak\winmine.reg
导出 winmine 下所有的子项与值到 c:\regbak\winmine.reg 文件中

reg import c:\regbak\winmine.reg
导入 c:\regbak\winmine.reg 文件到注册表中

reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\IEXPLORE.EXE" /s
查询 ie 的安装路径

reg query HKCR\.dsw /ve
查询 .dsw 默认值

reg query HKEY_CURRENT_USER\Software\Tencent\QQGame\SYS /v GameDirectory
查询 QQGame 安装路径
```

### 计划任务

**at**
```cmd
at id号                           开启已注册的某个计划任务
at /delete                        停止所有计划任务,用参数 /yes 则不需要确认就直接停止
at id号 /delete                   停止某个已注册的计划任务
at                                查看所有的计划任务
at ip time 程序名(或一个命令) /r    在某时间运行对方某程序并重新启动计算机
```

**[Schtasks.exe](https://docs.microsoft.com/en-us/windows/win32/taskschd/schtasks)**

创建计划任务 "gametime",在每月的第一个星期天运行"空当接龙".
```cmd
SCHTASKS /Create /SC MONTHLY /MO first /D SUN /TN gametime /TR c:\windows\system32\freecell

- /SC   schedule     指定计划频率.有效计划任务:  MINUTE、 HOURLY、DAILY、WEEKLY、MONTHLY, ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.
- /MO   modifier     改进计划类型以允许更好地控制计划重复周期.有效值列于下面"修改者"部分中.
- /D    days         指定该周内运行任务的日期.有效值:MON、TUE、WED、THU、FRI、SAT、SUN和对 MONTHLY 计划的 1 - 31(某月中的日期).通配符"*"指定所有日期.
- /TN   taskname     以路径\名称形式指定对此计划任务进行唯一标识的字符串.
- /TR   taskrun      指定在这个计划时间运行的程序的路径和文件名.例如: C:\windows\system32\calc.exe
```
```
schtasks /query /fo LIST /v             以较为详细易于阅读的格式显示本机所有任务计划信息

schtasks /delete /tn "Soda Build" /f    强制删除 Soda Build 名称的任务计划（不进行确认）
schtasks /run /tn "Soda Build"          执行名为 Soda Build 的任务计划
schtasks /end /tn "Soda Build"          终止执行名为 Soda Build 的任务计划

schtasks /create /sc minute /mo 20 /tn "Soda Build" /tr d:\check.vbs
创建一个名为 Soda Build 的任务计划：该任务计划每 20 分钟执行一下 d:\check.vbs 脚本

schtasks /create /tn "Soda Build" /tr D:\updateall.bat /sc daily /st 02:06 /f
强制创建一个名为 Soda Build 的任务计划（不进行确认）：该任务计划每天凌晨 2 点 06 分执行一下 D:\updateall.bat 脚本

schtasks /change /tn "Soda Build" /tr d:\check2.vbs
将名为 Soda Build 的任务计划的执行脚本修改为 d:\check2.vbs
```

### 组策略

**强制更新组策略**
```
gpupdate /force
```

---

## 账号管控

**账号**
```
net user test 1234abcd /add                 添加用户
net localgroup administrators test /add     将用户添加到管理组

net user test /del                          删除用户
```

---

## 进程管理

**进程信息**
```cmd
wmic process where Caption="buyticket.exe" get commandline,ExecutablePath,ProcessId,ThreadCount /value
查看名为"buyticket.exe"所有进程命令行，exe 全路径，PID 及线程数

wmic process where Caption="buyticket.exe" get ExecutablePath,HandleCount /value
查看名为"buyticket.exe"所有进程的 exe 全路径及当前打开的句柄数

wmic process where Caption="buyticket.exe" get ExecutablePath,VirtualSize,WorkingSetSize /value
查看名为"buyticket.exe"所有进程的 exe 全路径、当前虚拟地址空间占用及物理内存工作集

tasklist    显示所有进程及其服务

    tasklist /svc

    tasklist /fi "pid eq 1234" /svc         显示指定进程信息
    tasklist /fi "status eq running" /svc
    tasklist /fi "status eq running" /fi "username eq nt authority\system" /svc

    tasklist /m xxx.dll     显示使用给定 exe/dll 名称的所有进程

    tasklist /s ip /u username /p password /svc     显示远程主机的进程信息
```

**进程处理**
```cmd
taskkill    终止指定的进程及其子进程（根据进程名称）

    taskkill /f /im notepad.exe /t
    taskkill /f /pid 1234 /t        终止指定进程及其子进程（根据进程 ID）
    taskkill /f /fi "pid eq 1234" /t

    taskkill /s ip /u username /p password /pid 1234 /t     终止远程主机的指定进程
    taskkill /s ip /u username /p password /fi "pid eq 1234" /t
```

---

## 设备管理

### 硬盘-数据

**卷标设置**
```cmd
vol         显示当前分区的卷标
label       显示当前分区的卷标，同时提示输入新卷标
    label c:system      设置 c 盘的卷标为 system
```

**格式化**
```cmd
format      格式化磁盘
    format J: /FS:ntfs      以 ntfs 类型格式化 J 盘 [类型有:FAT、FAT32、exFAT、NTFS 或 UDF]
    format J: /FS:fat32 /Q  以 fat32 类型快速格式化J盘
```

**状态检查**
```cmd
chkdsk /f D:    检查磁盘 D 并显示状态报告；加参数/f表示同时会修复磁盘上的错误
```

**磁盘映射**
```cmd
subst   磁盘映射  -- 磁盘映射信息都保存在注册表以下键值中：HKEY_CURRENT_USER\Network
    subst                   显示目前所有的映射
    subst z: \\com\software 将 \\com\software 共享映射为本地 z 盘
    subst y: e:\src         将 e:\src 映射为本地 y 盘
    subst z: /d             删除 z 盘映射
```

---

# 域

**添加域管理员账号**
```
net user mstlab mstlab /add /domain             添加用户并设置密码
net group "Domain Admins" lemon /add /domain    将普通域用户提升为域管理员
net user guest /active:yes                      激活 guest 用户
net user guest mstlab                           更改 guest用户的密码
```

**修改指定域用户的密码**
```
dsquery user -samid username | dsmod user -pwd new_password
```
