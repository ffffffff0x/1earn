# shell 编程

---

**shell 和 shell 脚本的区别**
- shell 是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。Ken Thompson 的 sh 是第一种 Unix Shell，Windows Explorer 是一个典型的图形界面 Shell。
- shell 脚本（shell script），是一种为 shell 编写的脚本程序。业界所说的 shell 通常都是指 shell 脚本，但是，shell 和 shell script 是两个不同的概念。

**常见问题**

-  Linux 下运行 bash 脚本显示": /usr/bin/env: "bash\r": 没有那个文件或目录

	这主要是因为 bash 后面多了 \r 这个字符的原因.在 linux 终端下,输出 \r 会什么都不显示,只是把光标移到行首.于是终端虽然输出了 /usr/bin/env bash,但是碰到\r后,光标会被移到行首,接着输出了:No such file or directory 把前面的覆盖掉了.于是出现了那个莫名其妙的出错信息了

	一般来说这是下载在 windows 下载 github 脚本后会遇到的问题,下载压缩包,在 linux 中解压,或直接使用 linux 下载

	或者用 vim 打开 sh 脚本文件, 重新设置文件的格式
    ```vim
	:set ff=unix
   :wq!
	```

- linux 运行 shell 出现未预期的符号 `$'do\r'' 附近有语法错误

	看上面应该是语法错误,但无论怎么改还是报错,经过一番探索发现,自己的文件是从 windows 里面拷贝到 linux 的,可能是两种系统格式不一样.

	解决方法如下:
	1. 打开 notepad++ 编辑 .sh 文件
   2. notepad++ 右下角将 windows 模式改为 linux 模式

**source 命令与 `.` 的区别**
- source 命令是 bash shell 的内置命令,从 C Shell 而来.
- source 命令的另一种写法是点符号,用法和 source 相同,从 Bourne Shell 而来.
- source 命令可以强行让一个脚本去立即影响当前的环境.
- source 命令会强制执行脚本中的全部命令,而忽略文件的权限.
- source 命令通常用于重新执行刚修改的初始化文件,如 .bash_profile 和 .profile 等等.
- source 命令可以影响执行脚本的父 shell 的环境,而 export 则只能影响其子 shell 的环境.
- source a.sh 同直接执行 ./a.sh 有什么不同呢,比如你在一个脚本里 `export $KKK=111` ,如果你用 ./a.sh 执行该脚本,执行完毕后,你运行 `echo $KKK` ,发现没有值,如果你用 `source` 来执行 ,然后再 `echo` ,就会发现 KKK=111.因为调用 ./a.sh 来执行 shell 是在一个子 shell 里运行的,所以执行后,结果并没有反应到父 shell 里,不过 source 不同,他就是在本 shell 中执行的,所以能看到结果.

**sast 工具**
- https://github.com/koalaman/shellcheck

**资源教程**
- [dylanaraps/pure-bash-bible](https://github.com/dylanaraps/pure-bash-bible#get-the-username-of-the-current-user)

**相关文章**
- [10分钟学会Bash调试](https://mp.weixin.qq.com/s/MQjqu55BN6LqSsIAvevRQA)
- [如何并发执行Linux命令](https://mp.weixin.qq.com/s/L3u2e-GKl_yL3saJMMFazA)
- [终于知道 Shell 中单引号双引号的区别了](https://mp.weixin.qq.com/s/tyHIlRsg1rYjw-E_h-C2rA)
- [Bash编程基础知识](https://mp.weixin.qq.com/s/tSWnoO3IAET3C7iYY7ns6Q)

---

## 大纲

* **[编译](#编译)**

* **[示例](#示例)**

* **[变量](#变量)**

* **[字符串](#字符串)**

* **[数组](#数组)**

* **[传递参数](#传递参数)**

* **[基本运算符](#基本运算符)**

* **[基础命令](#基础命令)**
   * [echo命令](#echo命令)
   * [printf命令](#printf命令)
   * [test命令](#test命令)

* **[流程控制](#流程控制)**
   * [if](#if)
   * [for](#for)
   * [while](#while)
   * [until](#until)
   * [case](#case)
   * [跳出循环](#跳出循环)

* **[函数](#函数)**

* **[输入输出重定向](#输入输出重定向)**

* **[文件包含](#文件包含)**

---

## 编译

```bash
mount -t tmpfs tmpfs ~/build -o size=1G		# 把文件放到内存上做编译
make -j		# 并行编译
ccache		# 把编译的中间结果进行缓存,以便在再次编译的时候可以节省时间.
# 在 /usr/local/bin 下建立 gcc,g++,c++,cc的 symbolic link,链到 /usr/bin/ccache 上.总之确认系统在调用 gcc 等命令时会调用到 ccache 就可以了(通常情况下 /usr/local /bin 会在 PATH 中排在 /usr/bin 前面).
```

**distcc**

使用多台机器一起编译
```bash
/usr/bin/distccd  --daemon --allow 10.64.0.0/16 # 默认的 3632 端口允许来自同一个网络的 distcc 连接.

export DISTCC_HOSTS="localhost 10.64.25.1 10.64.25.2 10.64.25.3"
# 把 g++,gcc 等常用的命令链接到 /usr/bin/distcc 上

make -j4		# 在 make 的时候,也必须用 -j 参数,一般是参数可以用所有参用编译的计算机 CPU 内核总数的两倍做为并行的任务数.
distccmon-text	# 查看编译任务的分配情况.
```

---

## 示例

```sh
#!/bin/sh                   # 第1行：指定脚本解释器，这里是用 /bin/sh 做解释器的
cd ~                        # 第2行：切换到当前用户的 home 目录
mkdir shell_tut             # 第3行：创建一个目录 shell_tut
cd shell_tut                # 第4行：切换到 shell_tut 目录

for ((i=0; i<10; i++)); do  # 第5行：循环条件，一共循环10次
	touch test_$i.txt       # 第6行：创建一个 test_0…9.txt 文件
done                        # 第7行：循环体结束

# mkdir, touch 都是系统自带的程序，一般在 /bin 或者 /usr/bin 目录下。for, do, done 是 sh 脚本语言的关键字。
```

**编写**

新建一个文件，扩展名为 sh（sh 代表shell），扩展名并不影响脚本执行

输入一些代码
```sh
#!/bin/bash
#!/usr/bin/python
```
“#!”是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行。

很多脚本第一行用来指定本脚本用什么解释器来执行，例如 `#!/usr/bin/python` 相当于写死了 python 路径.

而 `#!/usr/bin/env python` 会去环境设置寻找 python 目录,可以增强代码的可移植性,推荐这种写法.

**运行**

运行 Shell 脚本有两种方法

- 作为可执行程序

    ```bash
    chmod +x test.sh
    ./test.sh
    ```

    注意，一定要写成 `./test.sh`，而不是 `test.sh`，运行其它二进制的程序也一样，直接写 test.sh，linux 系统会去 PATH 里寻找有没有叫 test.sh 的，而只有 /bin, /sbin, /usr/bin，/usr/sbin 等在 PATH 里，你的当前目录通常不在 PATH 里，所以写成 test.sh 是会找不到命令的，要用 ./test.sh 告诉系统说，就在当前目录找。

    通过这种方式运行 bash 脚本，第一行一定要写对，好让系统查找到正确的解释器。

- 作为解释器参数

    这种运行方式是，直接运行解释器，其参数就是 shell 脚本的文件名，如：
    ```bash
    /bin/sh test.sh
    /bin/php test.php
    ```
    这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。

---

## 变量

- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。
- 中间不能有空格，可以使用下划线（_）。
- 不能使用标点符号。
- 不能使用 bash 里的关键字（可用 help 命令查看保留关键字）。

> 注意，赋值号 = 的周围不能有空格!!!!!!!!!!!!!!!!!!!!!!!!!!

定义变量时，变量名不加美元符号（$），如：
```sh
name=test123    # 赋值
echo $name      # 引用
echo ${name}    # 变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界,推荐给所有变量加上花括号，这是个好的编程习惯。
```

使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变。
```sh
#!/bin/bash
name=test123
readonly name
name=test321    # name: readonly variable
```

使用 unset 命令可以删除变量。
```sh
name=test123
unset name
echo $name
```

**变量类型**

运行 shell 时，会同时存在三种变量：

1. 局部变量 : 局部变量在脚本或命令中定义，仅在当前 shell 实例中有效，其他 shell 启动的程序不能访问局部变量。
2. 环境变量 : 所有的程序，包括 shell 启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
3. shell 变量 : 由 shell 程序设置的特殊变量。shell 变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了 shell 的正常运行

**注释**

以“#”开头的行就是注释，会被解释器忽略，sh 里没有多行注释，只能每一行加一个 # 号。就像这样：
```sh
#1
##2
###3
####4
```

---

## 字符串

字符串是 shell 编程中最常用最有用的数据类型（除了数字和字符串，也没啥其它类型好用了），字符串可以用单引号，也可以用双引号，也可以不用引号。单双引号的区别跟 PHP 类似。

**单引号**

```sh
str='this is a string'
```

单引号字符串的限制：
- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的
- 单引号字串中不能出现单引号（对单引号使用转义符后也不行）

**双引号**

```sh
your_name='bog'
str="Hello, I know your are \"$your_name\"! \n"
echo -e $str
```

双引号的优点：
- 双引号里可以有变量
- 双引号里可以出现转义字符

**字符串操作**
- **拼接字符串**
    ```sh
    your_name="bog"
    # 使用双引号拼接
    greeting="hello, "$your_name" !"
    greeting_1="hello, ${your_name} !"
    echo $greeting  $greeting_1
    # 使用单引号拼接
    greeting_2='hello, '$your_name' !'
    greeting_3='hello, ${your_name} !'
    echo $greeting_2  $greeting_3
    ```

- **获取字符串长度**
    ```sh
    string="abcd"
    echo ${#string}     # 输出：4
    ```

- **提取子字符串**
    ```sh
    string="github.com is a great website"
    echo ${string:1:4}  # 输出：ithu
    ```

- **查找子字符串**
    ```sh
    string="github.com is a great website"
    echo `expr index "$string" is`  # 输出：2，这个语句的意思是：找出字符串is在这段话中的位置
    ```

---

## 数组

bash 支持一维数组（不支持多维数组），并且没有限定数组的大小。

类似于 C 语言，数组元素的下标由 0 开始编号。获取数组中的元素要利用下标，下标可以是整数或算术表达式，其值应大于或等于 0。

**定义数组**

在 Shell 中，用括号来表示数组，数组元素用"空格"符号分割开。定义数组的一般形式为：
```
数组名=(值1 值2 ... 值n)
```

例如
```sh
array_name=(value0 value1 value2 value3)

# 还可以单独定义数组的各个分量
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen

# 可以不使用连续的下标，而且下标的范围没有限制。
```

**读取数组**

读取数组元素值的一般格式是
```
${数组名[下标]}
```

例如
```sh
valuen=${array_name[n]}

# 使用 @ 符号可以获取数组中的所有元素
echo ${array_name[@]}
```

**获取数组的长度**

获取数组长度的方法与获取字符串长度的方法相同
```sh
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```

---

## 传递参数

我们可以在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：$n。n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……

以下实例我们向脚本传递三个参数，并分别输出，其中 $0 为执行的文件名：
```sh
#!/bin/bash

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
```
```bash
chmod +x test.sh
./test.sh 1 2 3
Shell 传递参数实例！
第一个参数为：1
参数个数为：3
传递的参数作为一个字符串显示：1 2 3
```

特殊字符用来处理参数

- `$#` : 传递到脚本的参数个数
- `$*` : 以一个单字符串显示所有向脚本传递的参数。 如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
- `$$` : 脚本运行的当前进程 ID 号
- `$!` : 后台运行的最后一个进程的 ID 号
- `$@` : 与 $* 相同，但是使用时加引号，并在引号中返回每个参数。 如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
- `$-` : 显示 Shell 使用的当前选项，与 set 命令功能相同。
- `$?` : 显示最后命令的退出状态。0 表示没有错误，其他任何值表明有错误。

```sh
#!/bin/bash

echo "Shell 传递参数实例！";
echo "第一个参数为：$1";

echo "参数个数为：$#";
echo "传递的参数作为一个字符串显示：$*";
```
```bash
chmod +x test.sh
./test.sh 1 2 3
Shell 传递参数实例！
第一个参数为：1
参数个数为：3
传递的参数作为一个字符串显示：1 2 3
```

传递的参数中如果包含空格，应该使用单引号或者双引号将该参数括起来，以便于脚本将这个参数作为整体来接收。

**$* 与 $@ 区别**
- 相同点：都是引用所有参数。
- 不同点：只有在双引号中体现出来。假设在脚本运行时写了三个参数 1、2、3，，则 " * " 等价于 "1 2 3"（传递了一个参数），而 "@" 等价于 "1" "2" "3"（传递了三个参数）。

```sh
#!/bin/bash

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
```
```
$ chmod +x test.sh
$ ./test.sh 1 2 3
-- $* 演示 ---
1 2 3
-- $@ 演示 ---
1
2
3
```

---

## 基本运算符

Shell 和其他编程语言一样，支持多种运算符，包括：
- 算数运算符
- 关系运算符
- 布尔运算符
- 字符串运算符
- 文件测试运算符

原生 bash 不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。

**算术运算符**

假定变量 a 为 10，变量 b 为 20
- `+` 加法 `expr $a + $b` 结果为 30。
- `-` 减法 `expr $a - $b` 结果为 -10。
- `*` 乘法 `expr $a \* $b` 结果为  200。
- `/` 除法 `expr $b / $a` 结果为 2。
- `%` 取余 `expr $b % $a` 结果为 0。
- `=` 赋值 `a=$b` 将把变量 b 的值赋给 a。
- `==` 相等 `[ $a == $b ]` 返回 false。
- `!=` 不相等 `[ $a != $b ]` 返回 true。

> 注意：条件表达式要放在方括号之间，并且要有空格，例如: `[$a==$b]` 是错误的，必须写成 `[ $a == $b ]`

```sh
#!/bin/bash

a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b` #  乘号(*)前边必须加反斜杠(\)才能实现乘法运算；
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi
```
```
a + b : 30
a - b : -10
a * b : 200
b / a : 2
b % a : 0
a 不等于 b
```

**关系运算符**

关系运算符只支持数字，不支持字符串，除非字符串的值是数字。

假定变量 a 为 10，变量 b 为 20
- `-eq` 检测两个数是否相等，相等返回 true。 `[ $a -eq $b ]` 返回 false。
- `-ne` 检测两个数是否不相等，不相等返回 true。 `[ $a -ne $b ]` 返回 true。
- `-gt` 检测左边的数是否大于右边的，如果是，则返回 true。 `[ $a -gt $b ]` 返回 false。
- `-lt` 检测左边的数是否小于右边的，如果是，则返回 true。 `[ $a -lt $b ]` 返回 true。
- `-ge` 检测左边的数是否大于等于右边的，如果是，则返回 true。 `[ $a -ge $b ]` 返回 false。
- `-le` 检测左边的数是否小于等于右边的，如果是，则返回 true。 `[ $a -le $b ]` 返回 true。

```sh
#!/bin/bash

a=10
b=20

if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
if [ $a -ne $b ]
then
   echo "$a -ne $b: a 不等于 b"
else
   echo "$a -ne $b : a 等于 b"
fi
if [ $a -gt $b ]
then
   echo "$a -gt $b: a 大于 b"
else
   echo "$a -gt $b: a 不大于 b"
fi
if [ $a -lt $b ]
then
   echo "$a -lt $b: a 小于 b"
else
   echo "$a -lt $b: a 不小于 b"
fi
if [ $a -ge $b ]
then
   echo "$a -ge $b: a 大于或等于 b"
else
   echo "$a -ge $b: a 小于 b"
fi
if [ $a -le $b ]
then
   echo "$a -le $b: a 小于或等于 b"
else
   echo "$a -le $b: a 大于 b"
fi
```
```
10 -eq 20: a 不等于 b
10 -ne 20: a 不等于 b
10 -gt 20: a 不大于 b
10 -lt 20: a 小于 b
10 -ge 20: a 小于 b
10 -le 20: a 小于或等于 b
```

**布尔运算符**

假定变量 a 为 10，变量 b 为 20
- `!` 非运算，表达式为 true 则返回 false，否则返回 true。`[ ! false ]` 返回 true。
- `-o` 或运算，有一个表达式为 true 则返回 true。 `[ $a -lt 20 -o $b -gt 100 ]` 返回 true。
- `-a` 与运算，两个表达式都为 true 才返回 true。 `[ $a -lt 20 -a $b -gt 100 ]` 返回 false。

```sh
#!/bin/bash

a=10
b=20

if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a == $b: a 等于 b"
fi
if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a 小于 100 且 $b 大于 15 : 返回 true"
else
   echo "$a 小于 100 且 $b 大于 15 : 返回 false"
fi
if [ $a -lt 100 -o $b -gt 100 ]
then
   echo "$a 小于 100 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 100 或 $b 大于 100 : 返回 false"
fi
if [ $a -lt 5 -o $b -gt 100 ]
then
   echo "$a 小于 5 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 5 或 $b 大于 100 : 返回 false"
fi
```
```
10 != 20 : a 不等于 b
10 小于 100 且 20 大于 15 : 返回 true
10 小于 100 或 20 大于 100 : 返回 true
10 小于 5 或 20 大于 100 : 返回 false
```

**逻辑运算符**

假定变量 a 为 10，变量 b 为 20
- `&&` 逻辑的 AND `[[ $a -lt 100 && $b -gt 100 ]]` 返回 false
- `||` 逻辑的 OR `[[ $a -lt 100 || $b -gt 100 ]]` 返回 true

```sh
#!/bin/bash

a=10
b=20

if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi

if [[ $a -lt 100 || $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi
```
```
返回 false
返回 true
```

**字符串运算符**

假定变量 a 为 "abc"，变量 b 为 "efg"
- `=` 检测两个字符串是否相等，相等返回 true。 `[ $a = $b ]` 返回 false。
- `!=` 检测两个字符串是否相等，不相等返回 true。 `[ $a != $b ]` 返回 true。
- `-z` 检测字符串长度是否为0，为0返回 true。 `[ -z $a ]` 返回 false。
- `-n` 检测字符串长度是否为0，不为0返回 true。 `[ -n "$a" ]` 返回 true。
- `$` 检测字符串是否为空，不为空返回 true。 `[ $a ]` 返回 true。

```sh
#!/bin/bash

a="abc"
b="efg"

if [ $a = $b ]
then
   echo "$a = $b : a 等于 b"
else
   echo "$a = $b: a 不等于 b"
fi
if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a != $b: a 等于 b"
fi
if [ -z $a ]
then
   echo "-z $a : 字符串长度为 0"
else
   echo "-z $a : 字符串长度不为 0"
fi
if [ -n "$a" ]
then
   echo "-n $a : 字符串长度不为 0"
else
   echo "-n $a : 字符串长度为 0"
fi
if [ $a ]
then
   echo "$a : 字符串不为空"
else
   echo "$a : 字符串为空"
fi
```
```
abc = efg: a 不等于 b
abc != efg : a 不等于 b
-z abc : 字符串长度不为 0
-n abc : 字符串长度不为 0
abc : 字符串不为空
```

**文件测试运算符**

- `-b file` 检测文件是否是块设备文件，如果是，则返回 true。 `[ -b $file ]` 返回 false。
- `-c file` 检测文件是否是字符设备文件，如果是，则返回 true。 `[ -c $file ]` 返回 false。
- `-d file` 检测文件是否是目录，如果是，则返回 true。 `[ -d $file ]` 返回 false。
- `-f file` 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 `[ -f $file ]` 返回 true。
- `-g file` 检测文件是否设置了 SGID 位，如果是，则返回 true。 `[ -g $file ]` 返回 false。
- `-k file` 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。 `[ -k $file ]` 返回 false。
- `-p file` 检测文件是否是有名管道，如果是，则返回 true。 `[ -p $file ]` 返回 false。
- `-u file` 检测文件是否设置了 SUID 位，如果是，则返回 true。 `[ -u $file ]` 返回 false。
- `-r file` 检测文件是否可读，如果是，则返回 true。 `[ -r $file ]` 返回 true。
- `-w file` 检测文件是否可写，如果是，则返回 true。 `[ -w $file ]` 返回 true。
- `-x file` 检测文件是否可执行，如果是，则返回 true。 `[ -x $file ]` 返回 true。
- `-s file` 检测文件是否为空（文件大小是否大于0），不为空返回 true。 `[ -s $file ]` 返回 true。
- `-e file` 检测文件（包括目录）是否存在，如果是，则返回 true。 `[ -e $file ]` 返回 true。
- -S: 判断某文件是否 socket。
- -L: 检测文件是否存在并且是一个符号链接。

变量 file 表示文件 `/var/www/test.sh`，它的大小为 100 字节，具有 rwx 权限。下面的代码，将检测该文件的各种属性：
```sh
#!/bin/bash

file="/var/www/test.sh"
if [ -r $file ]
then
   echo "文件可读"
else
   echo "文件不可读"
fi
if [ -w $file ]
then
   echo "文件可写"
else
   echo "文件不可写"
fi
if [ -x $file ]
then
   echo "文件可执行"
else
   echo "文件不可执行"
fi
if [ -f $file ]
then
   echo "文件为普通文件"
else
   echo "文件为特殊文件"
fi
if [ -d $file ]
then
   echo "文件是个目录"
else
   echo "文件不是个目录"
fi
if [ -s $file ]
then
   echo "文件不为空"
else
   echo "文件为空"
fi
if [ -e $file ]
then
   echo "文件存在"
else
   echo "文件不存在"
fi
```
```
文件可读
文件可写
文件可执行
文件为普通文件
文件不是个目录
文件不为空
文件存在
```

---

## 基础命令
### echo命令

Shell 的 echo 指令与 PHP 的 echo 指令类似，都是用于字符串的输出。命令格式：
```sh
echo string
```

**显示普通字符串**

```sh
echo "It is a test"
# 这里的双引号完全可以省略，以下命令与上面实例效果一致：
echo It is a test
```

**显示转义字符**

```sh
echo "\"It is a test\""
```
```
"It is a test"
```

**显示变量**

read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
```sh
#!/bin/sh
read name
echo "$name It is a test"
```

以上代码保存为 test.sh，name 接收标准输入的变量，结果将是:
```
./test.sh
OK                     #标准输入
OK It is a test        #输出
```

**显示换行**

```sh
echo -e "OK! \n" # -e 开启转义
echo "It is a test"
```
```
OK!

It is a test
```

**显示不换行**

```sh
#!/bin/sh
echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"
```
```
OK! It is a test
```

**显示结果定向至文件**

```
echo "It is a test" > myfile
```

**原样输出字符串，不进行转义或取变量(用单引号)**

```
echo '$name\"'
```
```
$name\"
```

**显示命令执行结果**

```
echo `date`
```

注意： 这里使用的是反引号 `, 而不是单引号 '。
结果将显示当前日期

---

### printf命令

- printf 命令模仿 C 程序库（library）里的 printf() 程序。
- printf 由 POSIX 标准所定义，因此使用 printf 的脚本比使用 echo 移植性好。
- printf 使用引用文本或空格分隔的参数，外面可以在 printf 中使用格式化字符串，还可以制定字符串的宽度、左右对齐方式等。默认 printf 不会像 echo 自动添加换行符，我们可以手动添加 \n。

```sh
printf  format-string  [arguments...]
# format-string: 为格式控制字符串
# arguments: 为参数列表。
```

```sh
$ echo "Hello, Shell"
Hello, Shell
$ printf "Hello, Shell\n"
Hello, Shell
$
```
```sh
#!/bin/bash

printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876
```
```
姓名     性别   体重kg
郭靖     男      66.12
杨过     男      48.65
郭芙     女      47.99
```
- %s %c %d %f 都是格式替代符
- %-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐），任何字符都会被显示在10个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。
- %-4.2f 指格式化为小数，其中.2指保留2位小数。

```sh
#!/bin/bash

# format-string 为双引号
printf "%d %s\n" 1 "abc"

# 单引号与双引号效果一样
printf '%d %s\n' 1 "abc"

# 没有引号也可以输出
printf %s abcdef

# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
printf %s abc def

printf "%s\n" abc def

printf "%s %s %s\n" a b c d e f g h i j

# 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
printf "%s and %d \n"
```
```
1 abc
1 abc
abcdefabcdefabc
def
a b c
d e f
g h i
j
 and 0
```

---

### test命令

test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

**数值测试**
- `-eq` 等于则为真
- `-ne` 不等于则为真
- `-gt` 大于则为真
- `-ge` 大于等于则为真
- `-lt` 小于则为真
- `-le` 小于等于则为真

```sh
num1=100
num2=100
if test $[num1] -eq $[num2]
then
    echo '两个数相等！'
else
    echo '两个数不相等！'
fi
```
```
两个数相等！
```

代码中的 [] 执行基本的算数运算
```sh
#!/bin/bash

a=5
b=6

result=$[a+b] # 注意等号两边不能有空格
echo "result 为： $result"
```
```
result 为： 11
```

**字符串测试**
- `=` 等于则为真
- `!=` 不相等则为真
- `-z 字符串` 字符串的长度为零则为真
- `-n 字符串` 字符串的长度不为零则为真

```sh
#!/bin/bash

num1="test"
num2="te5t"
if test $num1 = $num2
then
    echo '两个字符串相等!'
else
    echo '两个字符串不相等!'
fi
```
```
两个字符串不相等!
```

**文件测试**

- `-e 文件名` 如果文件存在则为真
- `-r 文件名` 如果文件存在且可读则为真
- `-w 文件名` 如果文件存在且可写则为真
- `-x 文件名` 如果文件存在且可执行则为真
- `-s 文件名` 如果文件存在且至少有一个字符则为真
- `-d 文件名` 如果文件存在且为目录则为真
- `-f 文件名` 如果文件存在且为普通文件则为真
- `-c 文件名` 如果文件存在且为字符型特殊文件则为真
- `-b 文件名` 如果文件存在且为块特殊文件则为真

```sh
cd /bin
if test -e ./bash
then
    echo '文件已存在!'
else
    echo '文件不存在!'
fi
```
```
文件已存在!
```

另外，Shell还提供了与( -a )、或( -o )、非( ! )三个逻辑操作符用于将测试条件连接起来，其优先级为："!"最高，"-a"次之，"-o"最低。例如：
```
cd /bin
if test -e ./notFile -o -e ./bash
then
    echo '至少有一个文件存在!'
else
    echo '两个文件都不存在'
fi
```
```
至少有一个文件存在!
```

---

## 流程控制

和 Java、PHP 等语言不一样，sh 的流程控制不可为空，如(以下为 PHP 流程控制写法)：
```php
<?php
if (isset($_GET["q"])) {
    search(q);
}
else {
    // 不做任何事情
}
```

在 sh/bash 里不行，如果 else 分支没有语句执行，就不要写这个 else。

### if

if 语句语法格式：
```sh
if condition
then
    command1
    command2
    ...
    commandN
fi
```
写成一行（适用于终端命令提示符）：
```sh
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
```
末尾的 fi 就是 if 倒过来拼写，后面还会遇到类似的。

if else 语法格式：
```sh
if condition
then
    command1
    command2
    ...
    commandN
else
    command
fi
```

if else-if else 语法格式：
```sh
if condition1
then
    command1
elif condition2
then
    command2
else
    commandN
fi
```
以下实例判断两个变量是否相等：
```sh
a=10
b=20
if [ $a == $b ]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi
```
```
a 小于 b
```

if else 语句经常与 test 命令结合使用，如下所示：
```sh
num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi
```
```
两个数字相等!
```

### for

for 循环一般格式为：
```sh
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```

写成一行：
```sh
for var in item1 item2 ... itemN; do command1; command2… done;
```

当变量值在列表里，for 循环即执行一次所有命令，使用变量名获取列表中的当前取值。命令可为任何有效的 shell 命令和语句。in 列表可以包含替换、字符串和文件名。

in 列表是可选的，如果不用它，for 循环使用命令行的位置参数。

例如，顺序输出当前列表中的数字：
```sh
for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done
```
```
The value is: 1
The value is: 2
The value is: 3
The value is: 4
The value is: 5
```

顺序输出字符串中的字符
```
for str in 'This is a string'
do
    echo $str
done
```
```
This is a string
```

### while

while 循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件。其格式为：
```sh
while condition
do
    command
done
```

以下是一个基本的 while 循环，测试条件是：如果 int 小于等于 5，那么条件返回真。int 从 0 开始，每次循环处理时，int 加 1。运行上述脚本，返回数字 1 到 5，然后终止。
```sh
#!/bin/bash
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
```
```
1
2
3
4
5
```

while 循环可用于读取键盘信息。下面的例子中，输入信息被设置为变量 FILM，按 `<Ctrl-D>` 结束循环。
```sh
echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
    echo "是的！$FILM 是一个好网站"
done
```

无限循环语法格式
```sh
while :
do
    command
done
```
```sh
for (( ; ; ))
```

### until

until 循环执行一系列命令直至条件为 true 时停止。

until 循环与 while 循环在处理方式上刚好相反。

一般 while 循环优于 until 循环，但在某些时候—也只是极少数情况下，until 循环更加有用。

until 语法格式
```sh
until condition
do
    command
done
```

condition 一般为条件表达式，如果返回值为 false，则继续执行循环体内的语句，否则跳出循环。

以下实例我们使用 until 命令来输出 0 ~ 9 的数字
```sh
#!/bin/bash

a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```
```
0
1
2
3
4
5
6
7
8
9
```

### case

case 的语法需要一个 esac（就是 case 反过来）作为结束标记，每个 case 分支用右圆括号，用两个分号表示 break

可以用 case 语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。case 语句格式如下：
```sh
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
```

case 工作方式如上所示。取值后面必须为单词 in，每一模式必须以右括号结束。取值可以为变量或常数。匹配发现取值符合某一模式后，其间所有命令开始执行直至 `;;`。

case支持合并匹配模式，即在每一个模式中，可以使用通配符或逻辑符号。

取值将检测匹配的每一个模式。一旦模式匹配，则执行完匹配模式相应命令后不再继续其他模式。如果无一匹配模式，使用星号 * 捕获该值，再执行后面的命令。

下面的脚本提示输入 1 到 4，与每一种模式进行匹配：
```sh
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```
```
输入 1 到 4 之间的数字:
你输入的数字为:
3
你选择了 3
```

### 跳出循环

在循环过程中，有时候需要在未达到循环结束条件时强制跳出循环，Shell 使用两个命令来实现该功能：break 和 continue。

**break**

break 命令允许跳出所有循环（终止执行后面的所有循环）。

下面的例子中，脚本进入死循环直至用户输入数字大于 5。要跳出这个循环，返回到 shell 提示符下，需要使用 break 命令。
```sh
#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字:"
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
            break
        ;;
    esac
done
```
```
输入 1 到 5 之间的数字:3
你输入的数字为 3!
输入 1 到 5 之间的数字:7
你输入的数字不是 1 到 5 之间的! 游戏结束
```

**continue**

continue 命令与 break 命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

对上面的例子进行修改
```sh
#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的!"
            continue
            echo "游戏结束"
        ;;
    esac
done
```

运行代码发现，当输入大于 5 的数字时，该例中的循环不会结束，语句 echo "游戏结束" 永远不会被执行。

**case ... esac**

case ... esac 与其他语言中的 switch ... case 语句类似，是一种多分枝选择结构，每个 case 分支用右圆括号开始，用两个分号 `;;` 表示 break，即执行结束，跳出整个 case ... esac 语句，esac（就是 case 反过来）作为结束标记。

case ... esac 语法格式如下：
```sh
case 值 in
模式1)
    command1
    command2
    command3
    ;;
模式2）
    command1
    command2
    command3
    ;;
*)
    command1
    command2
    command3
    ;;
esac
```

case 后为取值，值可以为变量或常数。

值后为关键字 in，接下来是匹配的各种模式，每一模式最后必须以右括号结束，模式支持正则表达式。
```sh
#!/bin/sh

site="github"

case "$site" in
   "github") echo "github"
   ;;
   "google") echo "Google"
   ;;
   "taobao") echo "taobao"
   ;;
esac
```
```
github
```

---

## 函数

linux shell 可以用户定义函数，然后在 shell 脚本中可以随便调用。

shell 中函数的定义格式如下
```sh
[ function ] funname [()]

{

    action;

    [return int;]

}
```

1. 可以带 `function fun()` 定义，也可以直接 `fun()` 定义,不带任何参数。
2. 参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。

下面的例子定义了一个函数并进行调用
```sh
#!/bin/bash

demoFun(){
    echo "这是我的第一个 shell 函数!"
}
echo "-----函数开始执行-----"
demoFun
echo "-----函数执行完毕-----"
```
```
-----函数开始执行-----
这是我的第一个 shell 函数!
-----函数执行完毕-----
```

下面定义一个带有 return 语句的函数
```sh
#!/bin/bash

funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
```
```
这个函数会对输入的两个数字进行相加运算...
输入第一个数字:
1
输入第二个数字:
2
两个数字分别为 1 和 2 !
输入的两个数字之和为 3 !
```
函数返回值在调用该函数后通过 `$?` 来获得。

注意：所有函数在使用前必须定义。这意味着必须将函数放在脚本开始部分，直至 shell 解释器首次发现它时，才可以使用。调用函数仅使用其函数名即可。

**函数参数**

在 Shell 中，调用函数时可以向其传递参数。在函数体内部，通过 `$n` 的形式来获取参数的值，例如，`$1` 表示第一个参数，`$2` 表示第二个参数...

带参数的函数示例
```sh
#!/bin/bash

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```
```
第一个参数为 1 !
第二个参数为 2 !
第十个参数为 10 !
第十个参数为 34 !
第十一个参数为 73 !
参数总数有 11 个!
作为一个字符串输出所有参数 1 2 3 4 5 6 7 8 9 34 73 !
```

注意，`$10` 不能获取第十个参数，获取第十个参数需要 `${10}`。当 n>=10 时，需要使用 `${n}` 来获取参数。

还有几个特殊字符用来处理参数
- `$#` 传递到脚本的参数个数
- `$*` 以一个单字符串显示所有向脚本传递的参数
- `$$` 脚本运行的当前进程 ID 号
- `$!` 后台运行的最后一个进程的 ID 号
- `$@` 与 $* 相同，但是使用时加引号，并在引号中返回每个参数。
- `$-` 显示 Shell 使用的当前选项，与 set 命令功能相同。
- `$?` 显示最后命令的退出状态。0 表示没有错误，其他任何值表明有错误。

---

## 输入输出重定向

大多数 UNIX 系统命令从你的终端接受输入并将所产生的输出发送回到你的终端。一个命令通常从一个叫标准输入的地方读取输入，默认情况下，这恰好是你的终端。同样，一个命令通常将其输出写入到标准输出，默认情况下，这也是你的终端。

重定向命令列表如下
- `command > file` 将输出重定向到 file。
- `command < file` 将输入重定向到 file。
- `command >> file` 将输出以追加的方式重定向到 file。
- `n > file` 将文件描述符为 n 的文件重定向到 file。
- `n >> file` 将文件描述符为 n 的文件以追加的方式重定向到 file。
- `n >& m` 将输出文件 m 和 n 合并。
- `n <& m` 将输入文件 m 和 n 合并。
- `<< tag` 将开始标记 tag 和结束标记 tag 之间的内容作为输入。

`需要注意的是文件描述符 0 通常是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。`

**输出重定向**

重定向一般通过在命令间插入特定的符号来实现。特别的，这些符号的语法如下所示: `command1 > file1`

上面这个命令执行 command1 然后将输出的内容存入 file1。

注意任何 file1 内的已经存在的内容将被新内容替代。如果要将新内容添加在文件末尾，请使用 `>>` 操作符。

执行下面的 who 命令，它将命令的完整的输出重定向在用户文件中(users):
```bash
who > users
```
执行后，并没有在终端输出信息，这是因为输出已被从默认的标准输出设备（终端）重定向到指定的文件。输出重定向会覆盖文件内容

**输入重定向**

和输出重定向一样，Unix 命令也可以从文件获取输入，语法为：
```bash
command1 < file1
```

这样，本来需要从键盘获取输入的命令会转移到文件读取内容。

注意：输出重定向是大于号(>)，输入重定向是小于号(<)。

统计 a.txt 文件的行数
```bash
wc -l a.txt
```
也可以将输入重定向到 a.txt 文件：
```bash
wc -l < a.txt
```
上面两个例子的结果不同：第一个例子，会输出文件名；第二个不会，因为它仅仅知道从标准输入读取内容。

```bash
command1 < infile > outfile
```
同时替换输入和输出，执行 command1，从文件 infile 读取内容，然后将输出写入到 outfile 中。


一般情况下，每个 Unix/Linux 命令运行时都会打开三个文件：
- 标准输入文件(stdin)：stdin 的文件描述符为 0，Unix 程序默认从 stdin 读取数据。
- 标准输出文件(stdout)：stdout 的文件描述符为 1，Unix 程序默认向 stdout 输出数据。
- 标准错误文件(stderr)：stderr 的文件描述符为 2，Unix 程序会向 stderr 流中写入错误信息。

默认情况下，command > file 将 stdout 重定向到 file，command < file 将stdin 重定向到 file。

`2` 表示标准错误文件(stderr)

如果希望 stderr 重定向到 file，可以这样写：
```bash
command 2> file
```

如果希望 stderr 追加到 file 文件末尾，可以这样写：
```sh
command 2>> file
```

如果希望将 stdout 和 stderr 合并后重定向到 file，可以这样写：
```sh
command > file 2>&1

# 或

command >> file 2>&1
```

如果希望对 stdin 和 stdout 都重定向，可以这样写：
```sh
command < file1 >file2
```
command 命令将 stdin 重定向到 file1，将 stdout 重定向到 file2。

**使用  > /dev/null 抑制标准输出**
```bash
cat file.txt > /dev/null
./shell-script.sh > /dev/null
```

**使用 2> /dev/null 抑制标准错误**
```bash
cat invalid-file-name.txt 2> /dev/null
./shell-script.sh 2> /dev/null
```

**Here Document**

Here Document 是 Shell 中的一种特殊的重定向方式，用来将输入重定向到一个交互式 Shell 脚本或程序。

它的基本的形式如下
```sh
command << delimiter
    document
delimiter
```

它的作用是将两个 delimiter 之间的内容(document) 作为输入传递给 command。
- 结尾的 delimiter 一定要顶格写，前面不能有任何字符，后面也不能有任何字符，包括空格和 tab 缩进。
- 开始的 delimiter 前后的空格会被忽略掉。

在命令行中通过 wc -l 命令计算 Here Document 的行数：
```
wc -l << EOF
    hello
    github
    www.github.com
EOF
```

将 Here Document 用在脚本中
```sh
#!/bin/bash

cat << EOF
欢迎来到
github
www.github.com
EOF
```

**/dev/null 文件**

如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 `/dev/null`：
```
command > /dev/null
```

`/dev/null` 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 `/dev/null` 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 stdout 和 stderr，可以这样写：
```sh
command > /dev/null 2>&1
```

---

## 文件包含

和其他语言一样，Shell 也可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。

Shell 文件包含的语法格式如下：
```sh
. filename   # 注意点号(.)和文件名中间有一空格

# 或

source filename
```

创建两个 shell 脚本文件。

test1.sh 代码如下
```sh
#!/bin/bash

url="http://www.github.com"
```

test2.sh 代码如下
```sh
#!/bin/bash

#使用 . 号来引用test1.sh 文件
. ./test1.sh

# 或者使用以下包含文件代码
# source ./test1.sh

echo "地址：$url"
```

> 注：被包含的文件 test1.sh 不需要可执行权限。

---

## 调式脚本

在 shell 脚本中添加 set -xv 来调试输出
```diff
vim test.sh

++ set -xv
```

或者在执行 shell 脚本时提供该设置
```bash
bash -xv test.sh
```

**trap**

trap命令用来在 Bash 脚本中响应系统信号。

最常见的系统信号就是 SIGINT（中断），即按 Ctrl + C 所产生的信号。trap命令的-l参数，可以列出所有的系统信号。
```
trap -l
```

“动作”是一个 Bash 命令，“信号”常用的有以下几个：
```
HUP：编号1，脚本与所在的终端脱离联系。
INT：编号2，用户按下 Ctrl + C，意图让脚本终止运行。
QUIT：编号3，用户按下 Ctrl + 斜杠，意图退出脚本。
KILL：编号9，该信号用于杀死进程。
TERM：编号15，这是kill命令发出的默认信号。
EXIT：编号0，这不是系统信号，而是 Bash 脚本特有的信号，不管什么情况，只要退出脚本就会产生。
```

trap命令响应EXIT信号的写法如下
```bash
trap 'rm -f "$TMPFILE"' EXIT
# 脚本遇到EXIT信号时，就会执行rm -f "$TMPFILE"
```

trap 命令的常见使用场景，就是在 Bash 脚本中指定退出时执行的清理命令。
```bash
trap 'rm -f "$TMPFILE"' EXIT

TMPFILE=$(mktemp) || exit 1
ls /etc > $TMPFILE
if grep -qi "kernel" $TMPFILE; then
  echo 'find'
fi

# 不管是脚本正常执行结束，还是用户按 Ctrl + C 终止，都会产生EXIT信号，从而触发删除临时文件。
```

注意，trap 命令必须放在脚本的开头。否则，它上方的任何命令导致脚本退出，都不会被它捕获。

如果 trap 需要触发多条命令，可以封装一个 Bash 函数。
```bash
function egress {
  command1
  command2
  command3
}

trap egress EXIT
```

---

## 错误处理

如果脚本里面有运行失败的命令(返回值非0),bash默认会继续执行后面的命令。

实际开发中，如果某个命令失败，往往需要脚本停止执行，防止错误累积。
```bash
command || exit 1

# 只要command有非零返回值，脚本就会停止执行。
```

如果停止执行之前需要完成多个操作，就要采用以下写法：
```bash
# 写法一
command || { echo "command failed"; exit 1; }

# 写法二
if ! command; then echo "command failed"; exit 1; fi

# 写法三
command
if [ "$?" -ne 0 ]; then echo "command failed"; exit 1; fi
```

另外，除了停止执行，还有一种情况。如果两个命令有继承关系，只有第一个命令成功了，才能继续执行第二个命令，那么就要采用下面的写法。
```bash
command1 && command2
```

---

## Source & Reference

- [Shell脚本编程30分钟入门](https://github.com/qinjx/30min_guides/blob/master/shell.md)
- [Shell 教程](https://www.runoob.com/linux/linux-shell.html)
- [Bash编程基础知识](https://mp.weixin.qq.com/s/tSWnoO3IAET3C7iYY7ns6Q)
