# Pyhon

---

**推荐工具/资源**

- [pycharm](https://www.jetbrains.com/pycharm/)
- [vscode](https://code.visualstudio.com/)
- [jackzhenguo/python-small-examples](https://github.com/jackzhenguo/python-small-examples)

---

## 安装/配置/报错
### 安装

**yum 安装**
```bash
yum install epel-release
或
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum -y install python36 python36-devel

wget https://bootstrap.pypa.io/get-pip.py	## 安装pip3
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
vim ~/.bash_profile ## 永久修改变量

PATH=$PATH:/usr/local/python3/bin/
```
`source ~/.bash_profile	`

检查 Python3 及 pip3 是否正常可用
```bash
python3 -V
pip3 -V
```

---

### 打包

**Pyinstaller**

安装 Pyinstaller
```bash
pip3 install PyInstaller
```

使用 Pyinstaller
```bash
python3 PyInstaller.py -F test.py
或
python -m PyInstaller -F test.py
## -F 表示生成单个可执行文件
## -w 表示去掉控制台窗口,这在GUI界面时非常有用.不过如果是命令行程序的话那就把这个选项删除吧
## -p 表示你自己自定义需要加载的类路径,一般情况下用不到
## -i 表示可执行文件的图标
```

文件中使用了第三方库的打包方式

在打包之前务必找到第三方库的包,把包复制到到跟 test.py 同目录下,然后再使用以上2种方式打包,否则会打包失败或者即使打包成功,程序也会闪退.

exe文件生成

如果程序打包过程没有报错,则会生成3个文件夹(有时候是2个),其中名为 dist 的文件夹中会有一个 test.exe 文件,运行一下,如果没有问题就打包成功,可以把这个 exe 文件单独拿出去用,其他的生成的文件夹可以删掉了.

**py2exe**

py2exe 就是将 python 代码打包成 windows 可执行程序的一个 python 开源项目。

安装
```
python -m pip install py2exe
```

基础方式 setup.py
```py
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
setup(console=["yourcode.py"])
```

```
python setup.py
```

进阶方法
```py
from distutils.core import setup
import py2exe
import sys

## 允许程序通过双击的形式执行。
sys.argv.append('py2exe')

py2exe_options = {
        ## 选项中 “includes” 是需要包含的文件，这里的”sip”是 PyQt 程序打包时需要添加的，如果不是 PyQt 程序不需要此项。
        "includes": ["sip"],
        ## “dll_excludes”是需要排除的 dll 文件，这里的”MSVCP90.dll”文件，如果不排除的话会报 error: MSVCP90.dll: No such file or directory 错误。
        "dll_excludes": ["MSVCP90.dll",],
        ## “compressed”为 1，则压缩文件
        "compressed": 1,
        ## “optimize”为优化级别，默认为 0。
        "optimize": 2,
        ## “ascii”指不自动包含 encodings 和 codecs。
        "ascii": 0,
        ## bundle_files”是指将程序打包成单文件（此时除了 exe 文件外，还会生成一个 zip 文件。如果不需要 zip 文件，还需要设置 zipfile = None）
        ## 1 表示 pyd 和 dll 文件会被打包到单文件中，且不能从文件系统中加载 python 模块；值为 2 表示 pyd 和 dll 文件会被打包到单文件中，但是可以从文件系统中加载 python 模块。64位的Py2exe不要添加本句。
        "bundle_files": 1,
        }

setup(
        name = 'PyQt Demo',
        version = '1.0',
        ## “myico.ico” 是程序图标,
        ## 将 setup 函数中的 console 改为 windows, 即没有命令行窗口出现，如果使用 console 则表示有命令行窗口出现。
        windows = [{ "script":'wordreplace.py',"icon_resources":[(1,"myico.ico")]}],
        zipfile = None,
        options = {'py2exe': py2exe_options}
      )

#如果 bundle_files 不为 1、2，则 dist 文件夹中还会包括一些 dll 文件和 pyd 文件（Python Dll 文件）。如果 bundle_files 为 2，dist 文件夹会包括一个 python##.dll 文件，如果为 1 则不会。
## 如果没有使用 zipfile=None，还会生成一个 library.zip 文件。
```

打包后的 exe 不可执行，是由于缺少两个必要的文件，msvcr90.dll 和 Microsoft.VC90.CRT.manifest，其中 msvcr90.dll 的版本为 9.0.21022.8，详细解释见官网，

解决方法：将上述两个文件 copy 进 dist 文件夹，或者见官网的解决方式（在打包前，将这两个文件作为资源，直接复制到 dist 文件夹下）。

打包后的 exe 报错，说缺少文件，这个问题的主要原因是 python 代码 import 文件时，使用了某些模块提供的所谓 lazy import，使得打包时，py2exe 找不到类库真正的路径

解决方法：重新 import 类库文件的真实路径，然后重新打包，问题解决。

当我们想要将一些 dll 打包进 exe 里面，就需要修改 py2exe 的默认配置

---

### 常见报错

- **UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 9: illegal multibyte sequence**
    - 在 Linux 环境下运行即可

- **UnicodeDecodeError: 'ascii' codec can't decode byte 0xce in position 7: ordinal not in range(128)**
    - 路径有中文,修改下即可

- **DLL load failed: %1 不是有效的 Win32 应用程序**
    - python 的版本是32位的,重装成64位的即可

- **TabError: inconsistent use of tabs and spaces in indentation**

    代码中空格和 tab 混用了

- **Python“Non-ASCII character 'xe5' in file”**

    Python 默认是以 ASCII 作为编码方式的，如果在自己的 Python 源码中包含了中文（或者其他非英语系的语言），此时即使你把自己编写的 Python 源文件以 UTF-8 格式保存了，但实际上，这依然是不行的。

    解决办法很简单，只要在文件开头加入下面代码就行了
    ```py
    ## -*- coding: UTF-8 -*-
    ```
    或
    ```py
    #coding:UTF-8
    ```

- **fatal error: Python.h: No such file or directory**

    For apt (Ubuntu, Debian...):
    ```bash
    sudo apt-get install python-dev   ## for python2.x installs
    sudo apt-get install python3-dev  ## for python3.x installs
    ```

    For yum (CentOS, RHEL...):
    ```bash
    sudo yum install python-devel   ## for python2.x installs
    sudo yum install python3-devel   ## for python3.x installs
    ```

    For dnf (Fedora...):
    ```bash
    sudo dnf install python2-devel  ## for python2.x installs
    sudo dnf install python3-devel  ## for python3.x installs
    ```

    For zypper (openSUSE...):
    ```bash
    sudo zypper in python-devel   ## for python2.x installs
    sudo zypper in python3-devel  ## for python3.x installs
    ```

    For apk (Alpine...):
    ```bash
    ## This is a departure from the normal Alpine naming
    ## scheme, which uses py2- and py3- prefixes
    sudo apk add python2-dev  ## for python2.x installs
    sudo apk add python3-dev  ## for python3.x installs
    ```

    For apt-cyg (Cygwin...):
    ```bash
    apt-cyg install python-devel   ## for python2.x installs
    apt-cyg install python3-devel  ## for python3.x installs
    ```

- **Python Pip broken wiith sys.stderr.write(f“ERROR: {exc}”)**

    由于 python 官方停止了对 python2 的维护，以后大部分和 pip2 有关的操作都会报这个错，我预估一下，这个应该是以后我们遇到最常见的问题之一
    ```bash
    curl https://bootstrap.pypa.io/2.7/get-pip.py --output get-pip.py
    python get-pip.py
    ```

- **requests.exceptions.ProxyError**

    ```python
    proxies = { "http": None, "https": None}
    requests.get("http://xxx.com", proxies=proxies)
    ```

- **Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed))**

    加上 verify=False
    ```python
    response = requests.get("https://127.0.0.1", verify=False)
    ```

- **return Command 'lsb_release -a' returned non-zero exit status 1**

    ```bash
    rm /usr/bin/lsb_release
    ```

- **/usr/lib/python3/dist-packages/secretstorage/dhcrypto.py:15: CryptographyDeprecationWarning: int_from_bytes is deprecated, use int.from_bytes instead**

    ```bash
    pip3 install cryptography==3.3.2
    ```

- **ModuleNotFoundError: No module named 'yaml'**

    ```
    pip install pyyaml
    ```

- **Centos7 pip2.7升级失败解决方法**

    升级跨度太大导致的问题，所以要解决这个问题只能通过升级至中间版本才可以解决
    ```
    wget https://files.pythonhosted.org/packages/0b/f5/be8e741434a4bf4ce5dbc235aa28ed0666178ea8986ddc10d035023744e6/pip-20.2.4.tar.gz
    tar -zxvf pip-20.2.4.tar.gz
    cd pip-20.2.4/
    sudo python setup.py install
    pip install -U pip

    python2 -m pip install --upgrade pip
    ```

---

## 包/模块管理
### import 与 from...import

在 python 用 import 或者 from...import 来导入相应的模块.
- 将整个模块(somemodule)导入,格式为: `import somemodule`
- 从某个模块中导入某个函数,格式为: `from somemodule import somefunction`
- 从某个模块中导入多个函数,格式为: `from somemodule import firstfunc, secondfunc, thirdfunc`
- 将某个模块中的全部函数导入,格式为: `from somemodule import *`

```py
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
```
```py
from sys import argv,path  ##  导入特定的成员

print('================python from import===================================')
print('path:',path) ## 因为已经导入path成员,所以此处引用时不需要加sys.path
```

---

### pip指定版本安装

检查一遍 pip 和 pip3 分别指向的 Python
```bash
pip -V
pip3 -V
```

在 linux 安装了多版本 python 时(例如 python2.6 和 2.7),pip 安装的包不一定是用户想要的位置,此时可以用 -t 选项来指定位置

`pip install -t /usr/local/lib/python2.7/site-packages/ xlrd`

或

```bash
python2 -m pip install xxxxx
```

---

### 虚拟环境 virtualenv

**安装virtualenv**

`pip install virtualenv`

**创建环境**

创建虚拟环境 `virtualenv envtest` 或指定版本 `virtualenv -p /usr/bin/python3  envtestv3`

进入虚拟环境的script路径,并执行 `activate` 就可以安装模块了

如果你的虚拟环境安装库的时候出问题,比如python3环境,需要安装 pip3

默认情况下,virtualenv会引用系统python环境中 site-­packages 中的库,并将其复制到虚拟python环境的库中.我们可以设置 --no-site-packages 参数取消对系统Python库的引用,以此来创建一个完全纯净的python环境.

---

### 离线安装

**压缩包**

```
python setup.py install
```

**whl 包**

- https://pypi.org/

```
pip install xxx.whl
```

---

### 自动生成 requirements.txt 文件

```bash
pip install pipreqs
pipreqs .
```

---

## 版本问题

### input()

python2中的`input()`函数:获取当前输入的内容,并将其作为指令来处理

python3中的`input()`函数:获取当前输入的内容,并将其作为字符串来处理

如果想在python2让`input`函数实现python3中相同的功能,就需要使用`raw_input()`函数

---

## 反编译

**在线工具**
- [python反编译](https://tool.lu/pyc/)

---

## 一些项目

**系统信息**
* [giampaolo/psutil](https://github.com/giampaolo/psutil)

**爬虫**
* [Scrapy](./笔记/爬虫.md#Scrapy)
* [VeNoMouS/cloudscraper](https://github.com/VeNoMouS/cloudscraper) - A Python module to bypass Cloudflare's anti-bot page.

**图像识别**
* 人脸识别
    * [face_recognition](./笔记/图像识别.md#face_recognition) - 人像识别
* ocr
    * [chineseocr_lite](./笔记/图像识别.md#chineseocr_lite) - 超轻量级中文ocr

**网络编程**
* [Urllib](./函数/网络编程.md#Urllib)
* [Requests](./函数/网络编程.md#Requests)

**文本处理**
* [ftfy](./函数/文本处理.md#ftfy)

**IO操作**
* [File](./函数/IO操作.md#File)

**可视化**
* pyecharts
* [big_screen](https://github.com/TurboWay/big_screen) - 数据大屏可视化

**集成**
* Fabric

**终端呈现方式**
* [tqdm/tqdm](https://github.com/tqdm/tqdm)
* [rsalmei/alive-progress](https://github.com/rsalmei/alive-progress)
* https://github.com/Textualize/rich

**语言**
* [mozillazg/python-pinyin](https://github.com/mozillazg/python-pinyin) - 汉字转拼音
* [lxneng/xpinyin](https://github.com/lxneng/xpinyin) - 汉字转拼音,比较旧了,不推荐
* [letiantian/Pinyin2Hanzi](https://github.com/letiantian/Pinyin2Hanzi) - 拼音转汉字， 拼音输入法引擎， pin yin -> 拼音
* [fxsjy/jieba](https://github.com/fxsjy/jieba) - 结巴中文分词

**正则**
- [asweigart/humre](https://github.com/asweigart/humre) - A human-readable regular expression module for Python.
