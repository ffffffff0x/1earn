# 🐱‍👤Benchmark
`应用于主机性能判断`

---

## 🐶版本信息
```bash
uname -r    # 查看系统
cat /etc/os-release # 查看通用 Linux 发行版版本
cat /proc/version   # # 查看系统版本
```

---

## 🐲CPU
```bash
cat /proc/cpuinfo   # 查看 CPU 核心数，架构，名字，频率，缓存，指令集等
cat /proc/star  # CPU 使用
grep name /proc/cpuinfo # 查看 CPU 名字
grep cores /proc/cpuinfo    # 查看 CPU 核心数
grep MHz /proc/cpuinfo  # 查看 CPU 频率
```

---

## 🦓内存
```bash
cat /proc/meminfo   # 查看内存硬件相关信息
free -m # 查看内存总量，使用量，swap 信息等
swapon -s   # 查看 swap 交换分区的路径，大小
```

---

## 时间负载
```bash
uptime  # 查看开机时间，系统用户数，平均负载
cat /proc/loadavg   # 查看系统负载
w   # 查看系统时间，负载，登入用户，用户使用资源情况
top # 总览系统全面信息，Ctrl + C 退出界面
```

---

## 🐇网络
```bash
ip a    # 网络信息
ip route    # 路由条目信息
cat /proc/net/arp   # 查看 arp 信息
```

**BestTrace**
```bash
cd /home && mkdir tmp && cd tmp
wget https://cdn.ipip.net/17mon/besttrace4linux.zip
unzip besttrace4linux.zip
chmod +x besttrace
mv besttrace /usr/local/bin
cd /home && rm -rf /home/tmp
# 安装完成后，就可以用指令 besttrace IP/域名 来追踪路由了
```

---

## 🐢硬盘
```bash
df -h   # 查看硬盘分区以及占用情况
du -sh <路径>   # 查看指定路径文件或目录大小
fdisk -l    # 查看硬盘大小，数量，类型
```
