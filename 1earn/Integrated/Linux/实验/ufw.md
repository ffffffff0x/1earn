# ufw

---

# 安装

```bash
sudo apt update && sudo apt install ufw
```

# 配置及使用

默认情况下，ufw 的配置文件在 `/etc/default/ufw` ，然后用户定义的防火墙规则文件会存在 `/etc/ufw/*.rules` 和 `/lib/ufw/*.rules`

UFW 默认允许所有出站连接，拒绝所有入站连接
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

**允许管理 IPv6**
```diff
sudo vim /etc/defaulf/ufw

++ IPV6=yes
```

**允许 SSH 连接**
```bash
sudo ufw allow ssh
# 等价于
sudo ufw allow 22
# 如果修改了SSH连接端口，记住相应的允许端口连接。
```

**允许 HTTP/HTTPS**
```bash
sudo ufw allow http
# 等价于
sudo ufw allow 80

sudo ufw allow https
sudo ufw allow 443
```

默认情况下 ufw allow 不加 in 是指允许入站连接，如果要允许出站，加上 out
```
sudo ufw allow in port
sudo ufw allow out port
```

**允许指定端口的协议**
```bash
sudo ufw allow ftp
# 等价于
sudo ufw allow 21/tcp
```

**允许指定范围的端口连接和协议**
```bash
sudo ufw allow 6000:6005/tcp
sudo ufw allow 7000:7005/udp
```

**允许指定的IP连接**

默认情况下相应的端口允许所有 IP 连接，通过 from 指定允许某 IP 的连接
```bash
sudo ufw allow from 123.45.67.89
sudo ufw allow from 123.45.67.89 to any port 22
```

如果要允许子网的连接
```bash
sudo ufw allow from 15.15.15.0/24
sudo ufw allow from 15.15.15.0/24 to any port 22
```

**拒绝连接**
```bash
# 和允许连接一样，只要将相应的 allow 换成 deny 即可

sudo ufw deny from 123.45.67.89
```

**查看规则**
```bash
sudo ufw status numbered
```

**删除规则**
```bash
# 每条规则前都有一个序号
sudo ufw delete [number]

sudo ufw delete allow http
# 等价于
sudo ufw delete allow 80
```

**查看 UFW 状态**
```bash
sudo ufw status verbose
sudo ufw show added
```

**启用禁用 UFW**
```bash
sudo ufw enable
sudo ufw disable

# ufw 默认会开机启动，如果没有，手动设置
sudo systemctl start ufw
sudo systemctl enable ufw
```

**启用日志**
```bash
sudo ufw logging on
sudo ufw logging off
sudo ufw logging low|medium|high    # 指定日志级别 日志文件在 /var/log/ufw.log
```

**重置防火墙**
```bash
sudo ufw reset
# 这条命令将禁用 ufw，并删除所有定义的规则,默认情况下， ufw 会备份规则。
```

---

**Source & Reference**
- [Linux 下的防火墙 ufw](http://einverne.github.io/post/2018/04/ufw.html)
