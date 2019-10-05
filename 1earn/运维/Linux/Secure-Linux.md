# Secure-Linux👨🏻‍💻

`Linux 加固+维护+应急响应参考`

`文档内容和` [加固笔记](../../安全/笔记/加固笔记.md) `难免有重复的部分，建议2个都看看`

<p align="center">
    <a href="https://commons.wikimedia.org/wiki/File:William_J._McCloskey_(1859%E2%80%931941),_Wrapped_Oranges,_1889._Oil_on_canvas._Amon_Carter_Museum_of_American_Art.jpg"><img src="../../../assets/img/运维/Linux/Secure-Linux.png" width="90%"></a>
</p>

---

# 本地👮🏻‍
## 密码重置
**centos7**

1. 在启动菜单选择启动内核，按 e 编辑,找到 rhgb quiet 一行，把 `rhgb quiet` 替换为 `init=/bin/bash`（临时生效）
2. 按 `CTRL+X` 进入单用户模式
3. 挂载根文件系统: `mount -o remount,rw /`
4. 使用 `passwd` 命令直接设置 root 密码: `passwd root` 输入两次新密码。
5. 最后,执行如下命令更新 SELinux: `touch /.autorelabel`
6. 进入正常模式: `exec /sbin/init`  现在可以使用新设置的 root 密码登录了。

---

## 会话

**查**
```bash
who  # 查看当前登录用户
w   # 查看登录用户行为
last # 查看登陆用户历史
```

**防**
```bash
pkill -u linfengfeiye   # 直接剔除用户
ps -ef| grep pts/0  # 得到用户登录相应的进程号 pid 后执行
kill -9 pid # 安全剔除用户
```

---

## 加固
**查后门**
- **添加 root 权限后门用户**

   检查 `/etc/passwd` 文件是否有异常

- **vim 后门**

   检测对应 vim 进程号虚拟目录的 map 文件是否有 python 字眼。
   `netstat -antlp`
   例如发现 vim pid 为 12
   ```
   file /proc/12/exe
   more /proc/12/cmdline
   more /proc/12/maps | grep python
   ```

- **strace记录**

    通过排查 shell 的配置文件或者 `alias` 命令即可发现，例如 `~/.bashrc` 和 `~/.bash_profile` 文件查看是否有恶意的 alias 问题。

- **定时任务和开机启动项**

    一般通过 `crontab -l` 命令即可检测到定时任务后门。不同的 linux 发行版可能查看开机启动项的文件不大相同，Debian 系 linux 系统一般是通过查看 `/etc/init.d` 目录有无最近修改和异常的开机启动项。而 Redhat 系的 linux 系统一般是查看 `/etc/rc.d/init.d` 或者 `/etc/systemd/system` 等目录。

- **预加载型动态链接库后门 ld.so.preload**

    通过 `strace` 命令去跟踪预加载的文件是否为 `/etc/ld.so.preload` ，以及文件中是否有异常的动态链接库。以及检查是否设置 LD_PRELOAD 环境变量等。注意：在进行应急响应的时候有可能系统命令被替换或者关键系统函数被劫持（例如通过预加载型动态链接库后门），导致系统命令执行不正常，这个时候可以下载 busybox。下载编译好的对应平台版本的 busybox，或者下载源码进行编译通过U盘拷贝到系统上，因为 busybox 是静态编译的，不依赖于系统的动态链接库，busybox 的使用类似如下 busybox ls，busybox ps -a。

- **内核级rootkit**

    可以通过 unhide 等工具进行排查

- **深信服 Web 后门扫描**

    http://edr.sangfor.com.cn/backdoor_detection.html

**杀毒**
- **[ClamavNet](https://www.clamav.net/downloads)**

**Reference**
- [linux常见backdoor及排查技术](https://xz.aliyun.com/t/4090)

---

## SELinux
**关闭 SELinux**
- 需要重启
	```vim
	vim /etc/selinux/config

	SELINUX=disabled
	```

- 不需要重启

	`setenforce 0`

---

## 系统管理👨‍🎓
### 系统信息
#### 进程管理

**进程定位**
```bash
pidof name  # 定位程序的 pid
pidof -x name   # 定位脚本的 pid
```

**进程限制**
```bash
ulimit -u 20    # 临时性允许用户最多创建 20 个进程,预防类似 fork 炸弹
```

```vim
vim /etc/security/limits.conf
    user1 - nproc 20  # 退出后重新登录，就会发现最大进程数已经更改为 20 了
```

##### 负载

**查**
- **查询负载、进程监控**
    ```bash
    top
    free
    vmstat
    ps -aux

    ps aux | grep Z # 列出进程表中所有僵尸进程
    ```

**防**
- **清理缓存**
    ```bash
    sync    # sync 命令做同步，以确保文件系统的完整性，将所有未写的系统缓冲区写到磁盘中，包含已修改的 i-node、已延迟的块 I/O 和读写映射文件。否则在释放缓存的过程中，可能会丢失未保存的文件。
    echo 1 > /proc/sys/vm/drop_caches   # 清理 pagecache（页面缓存）
    echo 2 > /proc/sys/vm/drop_caches   # 清理 dentries（目录缓存）和inodes
    echo 3 > /proc/sys/vm/drop_caches   # 清理 pagecache、dentries 和 inodes
    sync
    ```

- **文章**
    - [Linux系统清除缓存](https://www.cnblogs.com/jiu0821/p/9854704.html)

---

# Net🕵🏻
## 端口

**查**
```bash
getent services # 查看所有服务的默认端口名称和端口号

lsof -i -P  # 显示进程使用端口使用情况
lsof -i:22  # 只查 22 端口

ss -tnlp
ss -tnlp | grep ssh
ss -tnlp | grep ":22"

etstat -tnlp
netstat -tnlp | grep ssh

nmap -sV -p 22 localhost
```

---

## Firewall
**查**
```bash
firewall-cmd --list-services  # 查看防火墙设置
```

**防**
```bash
firewall-cmd --permanent --zone=public --remove-service=ssh
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=internal --add-source=1.1.1.1
firewall-cmd --reload   # 重启防火墙服务
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

## 禁 ping
**临时性,重启后失效**
```bash
echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_all # 允许 ping
echo 1 >/proc/sys/net/ipv4/icmp_echo_ignore_all # 禁止 ping
```

**长期性**
```bash
vim /etc/rc.d/rc.local

echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all
```

或

```bash
vim /etc/sysctl.conf

net.ipv4.icmp_echo_ignore_all=1
```

`sysctl -p` 使新配置生效

---

## SSH

**查**
- **查看尝试暴力破解机器密码的人**
    ```bash
    # Debian 系的发行版
    sudo grep "Failed password for root" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | more

    # Red Hat 系的发行版
    sudo grep "Failed password for root" /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr | more
    ```

- **查看暴力猜用户名的人**
    ```bash
    # Debian 系的发行版
    sudo grep "Failed password for invalid user" /var/log/auth.log | awk '{print $13}' | sort | uniq -c | sort -nr | more

    # Red Hat 系的发行版
    sudo grep "Failed password for invalid user" /var/log/secure | awk '{print $13}' | sort | uniq -c | sort -nr | more
    ```

**防**
- **骚操作:ping 钥匙**
    - [使用 ping 钥匙临时开启 SSH:22 端口，实现远程安全 SSH 登录管理就这么简单](https://www.cnblogs.com/martinzhang/p/5348769.html)

    ```bash
    # 规则1 只接受Data为1078字节的ping包，并将源IP记录到自定义名为sshKeyList的列表中
    iptables -A INPUT -p icmp -m icmp --icmp-type 8 -m length --length 1078 -m recent --name sshKeyList --set -j ACCEPT

    # 规则2 若30秒内发送次数达到6次(及更高)，当发起SSH:22新连接请求时拒绝
    iptables -A INPUT -p tcp -m tcp --dport 22 --syn -m recent --name sshKeyList --rcheck --seconds 30 --hitcount 6 -j DROP

    # 规则3 若30秒内发送次数达到5次，当发起SSH:22新连接请求时放行
    iptables -A INPUT -p tcp -m tcp --dport 22 --syn -m recent --name sshKeyList --rcheck --seconds 30 --hitcount 5 -j ACCEPT

    # 规则4 对于已建立的连接放行
    iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT

    # 规则5 老规矩：最后的拒绝
    iptables -A INPUT -j DROP
    ```

- **更改默认端口**

    修改 `/etc/ssh/sshd_config` 文件，将其中的 Port 22 改为指定的端口

    `!!! 警告，记得防火墙要先放行端口，不然你的远程主机就连不上了🤣!!!`
    ```
    service ssh restart
    ```

- **配置使用 RSA 私钥登陆**

    1. 先生成你的客户端的密钥，包括一个私钥和公钥
    2. 把公钥拷贝到服务器上，注意，生成私钥的时候，文件名是可以自定义的，且可以再加一层密码，所以建议文件名取自己能识别出哪台机器的名字。
    3. 然后在服务器上，你的用户目录下，新建 `.ssh` 文件夹，并将该文件夹的权限设为 700
    4. 新建一个 authorized_keys，这是默认允许的 key 存储的文件。如果已经存在，则只需要将上传的 id_rsa.pub 文件内容追加进去即可，如果不存在则新建并改权限为 400 即可。 然后编辑 ssh 的配置文件

    ```bash
    ssh-keygen -t rsa
    scp id_rsa.pub root@XX.XX.XX.XX:~/
    ```
    ```bash
    cd /
    mkdir .ssh
    chmod 700 .ssh
    mv id_rsa.pub .ssh
    cd .ssh
    cat id_rsa.pub >> authorized_keys
    chmod 600 authorized_keys
    ```
    ```vim
    vim /etc/ssh/sshd_config

    RSAAuthentication yes   # RSA 认证
    PubkeyAuthentication yes    # 开启公钥验证
    AuthorizedKeysFile /root/.ssh/authorized_keys   # 验证文件路径
    PasswordAuthentication no   # 禁止密码登录
    ```

    `sudo service sshd restart` 重启 sshd 服务

- **禁止 root 用户登录**

    可以建一个用户来专门管理，而非直接使用 root 用户，修改 /etc/ssh/sshd_config
    ```vim
    vim /etc/ssh/sshd_config

    PermitRootLogin no
    ```

- **使用 Fail2ban**

    - [fail2ban](https://github.com/fail2ban/fail2ban) ,详细搭建步骤请移步 [Power-Linux](./Power-Linux.md##[Fail2ban](https://github.com/fail2ban/fail2ban))

---

`真正的人，真正的事，往往不及心中所想的那么好。（金庸《倚天屠龙记》）`
