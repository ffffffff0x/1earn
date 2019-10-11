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
    <a href="https://en.wikipedia.org/wiki/The_Portrait_(Magritte)"><img src="../../../assets/img/运维/Linux/God-Linux.jpg" width="70%"></a>
</p>

---

# bash
``` bash
# 上一个命令的最后一个参数.例如：上一条命令(vim test.txt),cat !$ = cat test.txt
!$

# 以 root 身份运行最后一个命令
sudo !!

# 切换到上一个目录
cd -

# 一个命令创建项目的目录结构
mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}

# 筛选出命令中错误的输出,方便找到问题
yum list 1 > /dev/null

# 优雅的使用 linux
alias please="sudo"
```

## net
```bash
# 在当前目录起个 8080 端口的 HTTP 服务
python -m SimpleHTTPServer 8080

# 查看自己的外网地址
curl ifconfig.me
```

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

## VIM
``` bash
无 root 权限,保存编辑的文件
:w !sudo tee %
```

---

`真实的、永恒的、最高级的快乐,只能从三样东西中取得：工作、自我克制和爱.(罗曼·罗兰《托尔斯泰传》) `