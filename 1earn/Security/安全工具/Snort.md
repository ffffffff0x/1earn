### Snort

<p align="center">
    <img src="../../../assets/img/logo/Snort.webp" width="25%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**官网**
- https://www.snort.org/

**简介**

Snort 是开源的基于误用检测的网络入侵检测系统，采用规则匹配机制检测网络分组是否违反了事先配置的安全策略。安装在一台主机上就可以监测整个共享网段，一旦发现入侵和探测行为，具有将报警信息发送到系统日志、报警文件或控制台屏幕等多种实时报警方式。Snort 不仅能够检测各种网络攻击，还具有网络分组采集、分析和日志记录功能。相对于昂贵与庞大的商用产品而言，Snort 具有系统规模小、容易安装、容易配置、规则灵活和插件（plug-in）扩展等诸多优点。

**组成**

Snort 主要由分组协议分析器、入侵检测引擎、日志记录和报警模块组成。协议分析器的任务就是对协议栈上的分组进行协议解析，以便提交给入侵检测引擎进行规则匹配。入侵检测引擎根据规则文件匹配分组特征，当分组特征满足检测规则时，触发指定的响应操作。日志记录将解析后的分组以文本或 Tcpdump 二进制格式记录到日志文件，文本格式便于分组分析，二进制格式提高记录速度。报警信息可以发送到系统日志；也可以采用文本或 Tcpdump 二进制格式发送到报警文件；也容许选择关闭报警操作。记录到报警文件的报警信息有完全和快速两种方式，完全报警记录分组首部所有字段信息和报警信息，而快速报警只记录分组首部部分字段信息。

**相关文章**
- [工控安全：入侵检测snort-安装配置及pcap规则编写思路](https://www.key1.top/index.php/archives/526/)

**安装**
- **rpm 包安装**

    这里以 2.9.16-1 为例,最新版访问官网了解 https://www.snort.org
    ```bash
    yum install -y https://www.snort.org/downloads/snort/snort-2.9.16-1.centos7.x86_64.rpm
    ```
    > 注；如果下载失败,有可能是官方更新了，每次snort更新原来的包地址就访问不了，去官网看下更新下载地址即可。

    安装 snort 的时候可能会报错 : `缺少 libnghttp2.so.14()(64bit)`
    ```bash
    yum install -y epel-release -y
    yum install -y nghttp2
    ```

    测试: `snort` ,如果没有报错则安装成功.

    如果报错 `snort: error while loading shared libraries: libdnet.1: cannot open shared object file: No such file or directory`
    ```bash
    wget http://prdownloads.sourceforge.net/libdnet/libdnet-1.11.tar.gz
    tar -xzvf libdnet-1.11.tar.gz
    cd libdnet-1.11
    ./configure
    make && make install
    ```

- **Centos 下源代码编译安装**

    安装依赖
    ```bash
    yum install -y gcc flex bison zlib zlib-devel libpcap libpcap-devel pcre pcre-devel libdnet libdnet-devel tcpdump openssl openssl-devel
    ```

    下载 snort
    ```bash
    wget https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz
    wget https://www.snort.org/downloads/snort/snort-2.9.15.tar.gz
    ```
    ```bash
    tar xvzf daq-2.0.6.tar.gz

    cd daq-2.0.6
    ./configure && make && make install
    cd ../
    ```
    ```bash
    wget http://luajit.org/download/LuaJIT-2.0.5.tar.gz
    tar xvzf LuaJIT-2.0.5.tar.gz
    cd LuaJIT-2.0.5
    make install
    ```
    ```bash
    tar xvzf snort-2.9.15.tar.gz

    cd snort-2.9.15
    ./configure --enable-sourcefire && make && make install
    ```

    测试: `snort` ,如果没有报错则安装成功.

- **Ubuntu 下源代码编译安装**
    ```
    apt update
    apt install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev bison flex zlib1g-dev liblzma-dev openssl libssl-dev libnghttp2-dev autoconf libtool
    mkdir ~/snort_src
    cd ~/snort_src
    wget https://snort.org/downloads/snort/daq-2.0.7.tar.gz
    tar -xvzf daq-2.0.7.tar.gz
    cd daq-2.0.7
    ./configure
    autoreconf -vfi
    make
    make install

    cd ~/snort_src
    wget https://snort.org/downloads/snort/snort-2.9.16.tar.gz
    tar -xvzf snort-2.9.16.tar.gz
    cd snort-2.9.16
    ./configure --disable-open-appid
    make
    make install
    ldconfig
    ln -s /usr/local/bin/snort /usr/sbin/snort
    ```

    测试: `snort` ,如果没有报错则安装成功.

> 注 : 如果安装中还是遇到报错的问题可以参考 https://blog.csdn.net/rdgfdd/article/details/83420811

**配置**

在使用 snort 之前，需要根据保护网络环境和安全策略对 snort 进行配置，主要包括网络变量、预处理器、输出插件及规则集的配置，位于 etc 的 snort 配置文件 snort.conf 可用任意文本编辑器打开。除内部网络环境变量 HOME_NET 之外，在大多数情况下，可以使用 snort.conf 的默认配置。

由于我们不想使用 root 权限来运行 snort，所以需要创建相关用户。同时也需要建立工作目录。
```bash
# Create the snort user and group:
groupadd snort
useradd snort -r -s /sbin/nologin -c SNORT_IDS -g snort

# Create the Snort directories:
mkdir /etc/snort
mkdir /etc/snort/rules
mkdir /etc/snort/rules/iplists
mkdir /etc/snort/preproc_rules
mkdir /usr/local/lib/snort_dynamicrules
mkdir /etc/snort/so_rules

# Create some files that stores rules and ip lists
touch /etc/snort/rules/iplists/black_list.rules
touch /etc/snort/rules/iplists/white_list.rules
touch /etc/snort/rules/local.rules
touch /etc/snort/sid-msg.map

# Create our logging directories:
mkdir /var/log/snort
mkdir /var/log/snort/archived_logs

# Adjust permissions:
chmod -R 5775 /etc/snort
chmod -R 5775 /var/log/snort
chmod -R 5775 /var/log/snort/archived_logs
chmod -R 5775 /etc/snort/so_rules
chmod -R 5775 /usr/local/lib/snort_dynamicrules

# Change Ownership on folders:
chown -R snort:snort /etc/snort
chown -R snort:snort /var/log/snort
chown -R snort:snort /usr/local/lib/snort_dynamicrules
```

移动配置文件
```bash
cd ~/snort_src/snort-2.9.16/etc/
cp *.conf* /etc/snort
cp *.map /etc/snort
cp *.dtd /etc/snort
cd ~/snort_src/snort-2.9.16/src/dynamic-preprocessors/build/usr/local/lib/snort_dynamicpreprocessor/
cp * /usr/local/lib/snort_dynamicpreprocessor/
sed -i "s/include \$RULE\_PATH/#include \$RULE\_PATH/" /etc/snort/snort.conf
```

修改配置文件，将 HOME_NET 更改为自己电脑所在的 CIDR 地址
```bash
vim /etc/snort/snort.conf

ipvar HOME_NET 10.0.0.0/24

...104

var RULE_PATH /etc/snort/rules
var SO_RULE_PATH /etc/snort/so_rules
var PREPROC_RULE_PATH /etc/snort/preproc_rules
var WHITE_LIST_PATH /etc/snort/rules/iplists
var BLACK_LIST_PATH /etc/snort/rules/iplists

...564

include $RULE_PATH/local.rules
```

**测试使用**

```bash
vim /etc/snort/rules/local.rules

alert icmp any any -> $HOME_NET any (msg:"ICMP test detected"; GID:1; sid:10000001; rev:001; classtype:icmp-event;)
```

```bash
/usr/local/bin/snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i eth0
```
启动,此时用其他机器 Ping Snort 主机可以看到日志信息

![](../../../assets/img/Security/安全工具/Snort/1.png)

也可以直接读取 pcap 包
```bash
/usr/local/bin/snort  -c /etc/snort/snort.con -r foo.pcap
```

注意：snort 只能识别 pcap 后缀的包文件，用 wireshark 的 pcapng 后缀会报错 需要再另存为一下 修改文件格式 不是直接改后缀

**规则下载**

Snort 官方提供的三类规则

- Community rules : 无需注册 or 购买,可直接下载使用
- Registered rules : 需要注册才可以下载
- Subscriber rules : 需要注册花钱购买

访问官网 https://www.snort.org/ 下载规则

下载完,解压至相应目录
```
cd /etc/snort/rules/
wget https://www.snort.org/downloads/community/community-rules.tar.gz -O community-rules.tar.gz
tar -xvf community-rules.tar.gz
mv /etc/snort/rules/community-rules/community.rules /etc/snort/rules/


vim /etc/snort/snort.conf

include $RULE_PATH/community.rules
```

**其他 Snort 规则**

> PLC inject

```
alert tcp any any -> $any 502 (msg:”plcinject”; content:”|d0 9d 00 00 00 06 01 03 00 80 00 01|”; sid:001111111; GID:001; priority:0;)
```
