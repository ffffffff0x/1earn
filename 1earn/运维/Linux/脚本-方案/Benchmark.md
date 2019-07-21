# Benchmark🐱‍👤
`应用于 vps 性能判断`

## 版本信息🐶

```bash
uname -r    # 查看系统
cat /etc/os-release # 查看通用 Linux 发行版版本命令
```

## CPU🐲

```bash
cat /proc/cpuinfo   # 查看 CPU 核心数，架构，名字，频率，缓存，指令集等命令
grep name /proc/cpuinfo  # 查看 CPU 名字命令
grep cores /proc/cpuinfo     # 查看 CPU 核心数命令
grep MHz /proc/cpuinfo  # 查看 CPU 频率命令
```

## 内存🦓

```bash
cat /proc/meminfo # 查看内存硬件相关信息命令
free -m # 查看内存总量，使用量，swap 信息等命令
swapon -s # 查看 swap 交换分区的路径，大小命令
```

## 时间负载

```bash
uptime # 查看开机时间，系统用户数，平均负载命令
cat /proc/loadavg # 查看系统负载命令
w # 查看系统时间，负载，登入用户，用户使用资源情况命令
top # 总览系统全面信息命令，Ctrl + C 退出界面
```

## 网络🐇

```bash

```

### BestTrace

```bash
cd /home && mkdir tmp && cd tmp
wget https://cdn.ipip.net/17mon/besttrace4linux.zip
unzip besttrace4linux.zip
chmod +x besttrace
mv besttrace /usr/local/bin
cd /home && rm -rf /home/tmp
安装完成后，就可以用指令besttrace IP/域名来追踪路由了
```

## 硬盘🐢

```bash
df -h # 查看硬盘分区以及占用情况命令
du -sh [指定路径] # 查看指定路径文件或目录大小命令
fdisk -l # 查看硬盘大小，数量，类型命令
```
