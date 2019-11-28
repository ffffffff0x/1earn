# Benchmark

`应用于主机性能判断`

---

## Reference

- https://www.oldking.net/893.html

---

## 版本信息
```bash
uname -r    # 查看系统
hostname    # 查看服务器主机名命令
cat /etc/os-release # 查看通用 Linux 发行版版本
cat /etc/issue  # 查看 Ubuntu Debian 系发行版版本命令
cat /etc/redhat-release # 查看 CentOS RedHat 系发行版版本命令
cat /proc/version   # 查看系统版本
```

---

## CPU
```bash
cat /proc/cpuinfo   # 查看 CPU 核心数，架构，名字，频率，缓存，指令集等
cat /proc/star  # CPU 使用
grep name /proc/cpuinfo # 查看 CPU 名字
grep cores /proc/cpuinfo    # 查看 CPU 核心数
grep MHz /proc/cpuinfo  # 查看 CPU 频率
```

---

## 内存
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

## 网络
```bash
ifconfig    # 查看网卡及本机 ip 情况命令(需要系统安装了 net-tools 工具)
ip a    # 网络信息
ip route    # 路由条目信息
route -n    # 查看路由表命令
iptables -L # 查看防火墙等相关情况命令
netstat -s  # 查看系统网络连接情况统计信息命令
netstat -tunlp  # 查看服务器端口监听使用情况命令
netstat -auntp  # 查看已经建立连接的端口情况命令
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

**speedtest-cli**

- 项目地址

    https://github.com/sivel/speedtest-cli

- 简介

    Speedtest.net 提供一个命令行版本——speedtest-cli，能够在终端中简单快速的测试出 linux 的网速

- 使用过程
    ```
    wget https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
    chmod a+rx speedtest.py
    mv speedtest.py /usr/local/bin/speedtest-cli
    chown root:root /usr/local/bin/speedtest-cli
    speedtest-cli
    ```

---

## 硬盘
```bash
df -h   # 查看硬盘分区以及占用情况
du -sh <路径>   # 查看指定路径文件或目录大小
fdisk -l    # 查看硬盘大小，数量，类型
```

---

## 进程相关
```bash
ps -aux # 列出所有进程以及相关信息命令
kill -9 [进程PID] # 从上命令取到相关进程的PID后，高权限kill杀死进程命令命令
top # 总览系统全面信息命令，Ctrl + C 退出界面
```

---

## 用户相关
```bash
w   # 查看系统时间，负载，登入用户，用户使用资源情况命令
cut -d: -f1 /etc/passwd # 查看系统所有用户命令
last    # 查看系统前几次登陆情况
crontab -l  # 查看用户计划任务情况命令
crontab -e  # 编辑计划任务命令
```

---

## 开机启动
```bash
chkconfig   # 查看开机启动服务命令
ls /etc/init.d  # 查看开机启动配置文件命令
cat /etc/rc.local   # 查看 rc 启动文件
```

