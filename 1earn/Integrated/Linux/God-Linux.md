```
   ████████                ██       ██       ██
  ██░░░░░░██              ░██      ░██      ░░
 ██      ░░   ██████      ░██      ░██       ██ ███████  ██   ██ ██   ██
░██          ██░░░░██  ██████ █████░██      ░██░░██░░░██░██  ░██░░██ ██
░██    █████░██   ░██ ██░░░██░░░░░ ░██      ░██ ░██  ░██░██  ░██ ░░███
░░██  ░░░░██░██   ░██░██  ░██      ░██      ░██ ░██  ░██░██  ░██  ██░██
 ░░████████ ░░██████ ░░██████      ░████████░██ ███  ░██░░██████ ██ ░░██
  ░░░░░░░░   ░░░░░░   ░░░░░░       ░░░░░░░░ ░░ ░░░   ░░  ░░░░░░ ░░   ░░
```

<p align="center">
    <a href="https://en.wikipedia.org/wiki/The_Portrait_(Magritte)"><img src="../../../assets/img/banner/God-Linux.jpg" width="90%"></a>
</p>

<p align="center">
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/Integrated/Linux/open-source.png" width="15%"></a>
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/Integrated/Linux/bash.png" width="15%"></a>
</p>

---

## bash

``` bash
# 判断当前是否是登陆式或非登陆式 shell
echo $0

# 上一个命令的最后一个参数.例如:上一条命令(vim test.txt),cat !$ = cat test.txt
!$

# 以 root 身份运行最后一个命令
sudo !!

# 一个命令创建项目的目录结构
mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}

# 筛选出命令中错误的输出,方便找到问题
yum list 1 > /dev/null

# 优雅的使用 linux
alias please="sudo"

# 没用但有趣的东西.
P=(' ' █ ░ ▒ ▓)
while :;do printf "\e[$[RANDOM%LINES+1];$[RANDOM%COLUMNS+1]f${P[$RANDOM%5]}";done

# 让 freebad 机器叫出声
echo “T250L8CE-GE-C” > /dev/speaker
echo “O1L15aO2L15bO3L15cO4L15d” > /dev/speaker

# 在不使用 chmod 的情况下运行脚本
. ./test.sh
{.,./test.sh}
bash < test.sh
cat test.sh|sh
curl -s file://`pwd`/test.sh | sh

# 直接覆盖预原文件
sudo tee xxx.txt <<-'EOF'
aaa
bbb
test
EOF

# hex 转 ASCII
echo -e "\x68\x65\x6c\x6c\x6f"
```

### cd

**切换到上一个目录**
```
cd -
```

**创建时进入文件夹**
```
mkdir /tmp/test && cd $_
```

**使用 CDPATH 定义 cd 命令的基本目录**
```bash
cd mail
-bash: cd: mail: No such file or directory

export CDPATH=/etc
cd mail
/etc/mail
```

**有效率的向上移动**
```bash
# cd ../../../../

alias ..4="cd ../../../.."
alias .....="cd ../../../.."
alias cd.....="cd ../../../.."
alias cd4="cd ../../../.."

..4
.....
cd.....
cd4
```

**使用 dirs, pushd 和 popd 操作目录堆栈**
```bash
# 如何使用 pushd 和 popd? 让我们首先创建一些临时目录，并将它们推入目录堆栈，如下所示。
mkdir /tmp/dir1
mkdir /tmp/dir2
mkdir /tmp/dir3
mkdir /tmp/dir4

cd /tmp/dir1
pushd .

cd /tmp/dir2
pushd .

cd /tmp/dir3
pushd .

cd /tmp/dir4
pushd .

dirs
# 在这个阶段，目录堆栈包含以下目录
# /tmp/dir4
# /tmp/dir3
# /tmp/dir2
# /tmp/dir1

# 最后一个被推送到堆栈中的目录将在顶部。当执行 popd 时，它会 cd 到堆栈中最上面的目录项，并将其从堆栈中删除。最后推送到栈中的目录是 /tmp/dir4，所以，当我们执行 popd 时，会 cd 到 /tmp/dir4，并从目录栈中删除，如下所示。

popd
pwd
# 在这个阶段，目录堆栈包含以下目录
# /tmp/dir3
# /tmp/dir2
# /tmp/dir1

popd
pwd
# 在这个阶段，目录堆栈包含以下目录
# /tmp/dir2
# /tmp/dir1

popd
pwd
# 在这个阶段，目录堆栈包含以下目录
# /tmp/dir1

popd
pwd
# 在 popd 后，目录 Stack 为空!

popd
-bash: popd: directory stack empty
```

**使 cd 不区分大小写**
```bash
bind "set completion-ignore-case on"
```

---

## net

```bash
# 在当前目录起个 8000 端口的 HTTP 服务
python -m SimpleHTTPServer 8000

# 查看自己的外网地址
curl ifconfig.me
```

**无依赖下载(仅支持http)**
- [linux在没有curl和wget的情况下如何用shell实现下载功能](https://zgao.top/linux%e5%9c%a8%e6%b2%a1%e6%9c%89curl%e5%92%8cwget%e7%9a%84%e6%83%85%e5%86%b5%e4%b8%8b%e5%a6%82%e4%bd%95%e7%94%a8shell%e5%ae%9e%e7%8e%b0%e4%b8%8b%e8%bd%bd%e5%8a%9f%e8%83%bd/)

```bash
#!/bin/bash
# 无依赖的http下载
# https://zgao.top/linux%e5%9c%a8%e6%b2%a1%e6%9c%89curl%e5%92%8cwget%e7%9a%84%e6%83%85%e5%86%b5%e4%b8%8b%e5%a6%82%e4%bd%95%e7%94%a8shell%e5%ae%9e%e7%8e%b0%e4%b8%8b%e8%bd%bd%e5%8a%9f%e8%83%bd/
# https://github.com/c4pr1c3/cuc-ns/blob/master/chap0x07/exp/webgoat/wget.sh

function DOWNLOAD() {

    local URL=$1

    if [ -z "${URL}" ]; then
        printf "Usage: %s \"URL\" [e.g.: %s http://www.xxx.com/test.json]" \
            "${FUNCNAME[0]}" "${FUNCNAME[0]}"
        return 1;
    fi

    read proto server path <<< "${URL//"/"/ }"
    DOC=/${path// //}
    HOST=${server//:*}
    PORT=${server//*:}
    [[ x"${HOST}" == x"${PORT}" ]] && PORT=80

    exec 3<>/dev/tcp/${HOST}/$PORT
    echo -en "GET ${DOC} HTTP/1.0\r\nHost: ${HOST}\r\n\r\n" >&3
    while IFS= read -r line ; do
        [[ "$line" == $'\r' ]] && break
    done <&3
    nul='\0'
    while IFS= read -d '' -r x || { nul=""; [ -n "$x" ]; }; do
        printf "%s$nul" "$x"
    done <&3
    exec 3>&-
}

DOWNLOAD "$1"
```

---

## shell

**fork 炸弹**
```bash
:(){:|:&};:
```

**[Thanos](https://github.com/hotvulcan/Thanos.sh)**

This command could delete half your files randomly
```bash
#!/bin/sh
let i=`find . -type f | wc -l`/2 ; find . -type f -print0 | shuf -z -n $i | xargs -0 -- cat

# Explaination
## Step 1: Get the count of files in current path divided by two.
## Step 2: Get all the files in current path and print in one line.
## Step 3: Turn half of the second step output into standard input randomly.
## Step 4: Show half of the files in terminal.

# Key Point
## If you want to make delete, what you need to do is turn 'cat' into 'rm'.
```

---

## VIM

``` bash
无 root 权限,保存编辑的文件
:w !sudo tee %
```

---

## 性能

```bash
sync    # sync 命令做同步,以确保文件系统的完整性,将所有未写的系统缓冲区写到磁盘中,包含已修改的 i-node、已延的块 I/O 和读写映射文件.否则在释放缓存的过程中,可能会丢失未保存的文件.
echo 1 > /proc/sys/vm/drop_caches   # 清理 pagecache(页面缓存)
echo 2 > /proc/sys/vm/drop_caches   # 清理 dentries(目录缓存)和inodes
echo 3 > /proc/sys/vm/drop_caches   # 清理 pagecache、dentries 和 inodes
sync

# 取消开启文件数限制
ulimit -n 65535

# 优化内存
echo 128 > /proc/sys/vm/nr_hugepages        # 默认为0
sysctl -w vm.nr_hugepages=128
```

---

## 文本

**计算文本文件中的单词出现次数**
```bash
grep -o -i test example.txt | wc -l         # 计算"test"出现在文件中的次数
```
