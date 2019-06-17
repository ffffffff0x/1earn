# Secure-Linux👨🏻‍💻

`Linux加固+维护+应急响应参考`

[TOC]

---

# Shell👮🏻‍
## 会话

```bash
who  # 查看当前登录用户
w    # 查看登录用户行为
last # 查看登陆用户历史

pkill -u linfengfeiye # 直接剔除用户
ps -ef| grep pts/0  # 得到用户登录相应的进程号pid后执行
kill -9 pid # 安全剔除用户
```

---

# Net🕵🏻
## 端口

```bash
lsof -i -P # 显示进程使用端口使用情况
lsof -i:22  # 只查22端口

ss -tnlp
ss -tnlp | grep ssh
ss -tnlp | grep ":22"

etstat -tnlp
netstat -tnlp | grep ssh

nmap -sV -p 22 localhost
```

## Firewall

```bash
firewall-cmd --permanent --zone=public --remove-service=ssh
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=internal --add-source=1.1.1.1
firewall-cmd --reload
firewall-cmd --list-services  #查看防火墙设置
```

在上面的配置中，如果有人尝试从 1.1.1.1 去 ssh，这个请求将会成功，因为这个源区域（internal）被首先应用，并且它允许 ssh 访问。

如果有人尝试从其它的地址，如 2.2.2.2，去访问 ssh，它不是这个源区域的，因为和这个源区域不匹配。因此，这个请求被直接转到接口区域（public），它没有显式处理 ssh，因为，public 的目标是 default，这个请求被传递到默认动作，它将被拒绝。

如果 1.1.1.1 尝试进行 http 访问会怎样？源区域（internal）不允许它，但是，目标是 default，因此，请求将传递到接口区域（public），它被允许访问。

现在，让我们假设有人从 3.3.3.3 拖你的网站。要限制从那个 IP 的访问，简单地增加它到预定义的 drop 区域，正如其名，它将丢弃所有的连接：
```bash
firewall-cmd --permanent --zone=drop --add-source=3.3.3.3
firewall-cmd --reload
```
下一次 3.3.3.3 尝试去访问你的网站，firewalld 将转发请求到源区域（drop）。因为目标是 DROP，请求将被拒绝，并且它不会被转发到接口区域（public）。

`注:配置了 firewalld 服务后一定要去检查下规则，因为他不会阻掉正在进行的连接，只能阻掉配置命令后进行的连接，所以你不知道你的ssh会话会不会一断就再也连不上了，血的教训🤣`

---

# 系统管理👨‍🎓
## 进程管理

**进程定位**
```bash
pidof name # 定位程序的pid
pidof -x name # 定位脚本的pid
```

**进程限制**
```bash
ulimit -u 20 # 临时性允许用户最多创建 20 个进程,预防类似fork炸弹
```

```vim
vim /etc/security/limits.conf
    user1 - nproc 20  # 退出后重新登录，就会发现最大进程数已经更改为 20 了
```

## 负载

**查询负载、进程监控**
```bash
top
free
vmstat
ps -aux

ps aux | grep Z # 列出进程表中所有僵尸进程
```

**清理缓存**
```bash
sync    # sync命令做同步，以确保文件系统的完整性，将所有未写的系统缓冲区写到磁盘中，包含已修改的 i-node、已延迟的块 I/O 和读写映射文件。否则在释放缓存的过程中，可能会丢失未保存的文件。
echo 1 > /proc/sys/vm/drop_caches   # 清理pagecache（页面缓存）
echo 2 > /proc/sys/vm/drop_caches   # 清理dentries（目录缓存）和inodes
echo 3 > /proc/sys/vm/drop_caches   # 清理pagecache、dentries和inodes
sync
```

**Reference**
- [Linux系统清除缓存](https://www.cnblogs.com/jiu0821/p/9854704.html)

---

# 安全
## 加固

**查后门**

- **添加root权限后门用户**

   检查`/etc/passwd`文件是否有异常

- **vim后门**

   检测对应vim进程号虚拟目录的map文件是否有python字眼。
   `netstat -antlp`
   例如发现vim pid 为 12
   ```
   file /proc/12/exe
   more /proc/12/cmdline
   more /proc/12/maps | grep python
   ```

- **strace记录**

    通过排查shell的配置文件或者`alias`命令即可发现，例如`~/.bashrc`和`~/.bash_profile`文件查看是否有恶意的alias问题。

- **定时任务和开机启动项**

    一般通过`crontab -l`命令即可检测到定时任务后门。不同的linux发行版可能查看开机启动项的文件不大相同，Debian系linux系统一般是通过查看`/etc/init.d`目录有无最近修改和异常的开机启动项。而Redhat系的linux系统一般是查看`/etc/rc.d/init.d`或者`/etc/systemd/system`等目录。

- **预加载型动态链接库后门 ld.so.preload**

    通过`strace`命令去跟踪预加载的文件是否为`/etc/ld.so.preload`，以及文件中是否有异常的动态链接库。以及检查是否设置LD_PRELOAD环境变量等。注意：在进行应急响应的时候有可能系统命令被替换或者关键系统函数被劫持（例如通过预加载型动态链接库后门），导致系统命令执行不正常，这个时候可以下载busybox。下载编译好的对应平台版本的busybox，或者下载源码进行编译通过U盘拷贝到系统上，因为busybox是静态编译的，不依赖于系统的动态链接库，busybox的使用类似如下 busybox ls，busybox ps -a。

- **内核级rootkit**

    可以通过unhide等工具进行排查

- **深信服Web后门扫描**

    http://edr.sangfor.com.cn/backdoor_detection.html

**杀毒**

- **[ClamavNet](https://www.clamav.net/downloads)**

**Reference**
- [linux常见backdoor及排查技术](https://xz.aliyun.com/t/4090)

---

`真正的人，真正的事，往往不及心中所想的那么好。（金庸《倚天屠龙记》）`
