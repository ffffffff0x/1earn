# Secure-Linux👨🏻‍💻
`Linux加固+维护+应急响应参考`
[TOC]

**Todo**
- [ ] ssh加固
- [ ] 安全删除

---

# Shell👮🏻‍
## 会话
```bash
who  #查看当前登录用户
w    #查看登录用户行为
last #查看登陆用户历史

pkill -u linfengfeiye #直接剔除用户
ps -ef| grep pts/0  #得到用户登录相应的进程号pid后执行
kill -9 pid #安全剔除用户
```

---

# 系统管理👨‍🎓
## 进程管理
**进程定位**
```bash
pidof name #定位程序的pid
pidof -x name #定位脚本的pid
```

**进程限制**
```bash
ulimit -u 20 #临时性允许用户最多创建 20 个进程,预防类似fork炸弹
vim /etc/security/limits.conf
    user1 - nproc 20       #退出后重新登录，就会发现最大进程数已经更改为 20 了    
```

## 负载
**查询负载、进程监控**
```bash
top
free
vmstat
ps -aux 

ps aux | grep Z #列出进程表中所有僵尸进程
```

**清理缓存**
```bash
sync    #sync命令做同步，以确保文件系统的完整性，将所有未写的系统缓冲区写到磁盘中，包含已修改的 i-node、已延迟的块 I/O 和读写映射文件。否则在释放缓存的过程中，可能会丢失未保存的文件。
echo 1 > /proc/sys/vm/drop_caches   #清理pagecache（页面缓存）
echo 2 > /proc/sys/vm/drop_caches   #清理dentries（目录缓存）和inodes
echo 3 > /proc/sys/vm/drop_caches   #清理pagecache、dentries和inodes
sync
```

---

# Net🕵🏻
## 端口
```bash
lsof -i -P #显示进程使用端口使用情况
lsof -i:22  #只查22端口

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

`真正的人，真正的事，往往不及心中所想的那么好。（金庸《倚天屠龙记》）`
