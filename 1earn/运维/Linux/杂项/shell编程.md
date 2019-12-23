# shell 编程

---

## Reference
- [Shell脚本编程30分钟入门](https://github.com/qinjx/30min_guides/blob/master/shell.md)
- [Shell 教程](https://www.runoob.com/linux/linux-shell.html)

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

---

## 示例

```sh
#!/bin/sh                   # 第1行：指定脚本解释器，这里是用/bin/sh做解释器的
cd ~                        # 第2行：切换到当前用户的home目录
mkdir shell_tut             # 第3行：创建一个目录shell_tut
cd shell_tut                # 第4行：切换到shell_tut目录

for ((i=0; i<10; i++)); do  # 第5行：循环条件，一共循环10次
	touch test_$i.txt       # 第6行：创建一个test_0…9.txt文件
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
    echo `expr index "$string" is`  # 输出：2，这个语句的意思是：找出字母i在这名话中的位置
    ```




https://www.runoob.com/linux/linux-shell-variable.html




https://github.com/qinjx/30min_guides/blob/master/shell.md#%E6%8B%BC%E6%8E%A5%E5%AD%97%E7%AC%A6%E4%B8%B2






