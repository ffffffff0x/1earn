# firewalld 实验

---

## 区域

**防火墙各个区说明**
- **drop (丢弃)**

    任何接收的网络数据包都被丢弃,没有任何回复.仅能有发送出去的网络连接.

- **block (限制)**

    任何接收的网络连接都被 IPv4 的 icmp-host-prohibited 信息和 IPv6 的 icmp6-adm-prohibited 信息所拒绝.

- **public (公共)**

    在公共区域内使用,不能相信网络内的其他计算机不会对你的计算机造成危害,只能接收经过选取的连接.

- **external (外部)**

    特别是为路由器启用了伪装功能的外部网.你不能信任来自网络的其他计算,不能相信它们不会对你的计算机造成危害,只能接收经过选择的连接.

- **dmz (非军事区)**

    用于你的非军事区内的电脑,此区域内可公开访问,可以有限地进入你的内部网络,仅仅接收经过选择的连接.

- **work (工作)**

    用于工作区.你可以基本相信网络内的其他电脑不会危害你的电脑.仅仅接收经过选择的连接.

- **home (家庭)**

    用于家庭网络.你可以基本信任网络内的其他计算机不会危害你的计算机.仅仅接收经过选择的连接.

- **internal (内部)**

    用于内部网络.你可以基本上信任网络内的其他计算机不会威胁你的计算机.仅仅接受经过选择的连接.

- **trusted (信任)**

    可接受所有的网络连接.适合在故障排除的情况下或者是在你绝对信任的网络上使用.

---

## 常用命令

**服务管理**
```bash
systemctl status firewalld	# 查看服务运行状态
systemctl start firewalld	# 开启服务
systemctl stop firewalld	# 关闭服务
```

**查看**
```bash
firewall-cmd --state                    # 显示防火墙状态
firewall-cmd --get-zones                # 列出当前有几个 zone
firewall-cmd --get-active-zones         # 取得当前活动的 zones
firewall-cmd --get-default-zone         # 取得默认的 zone
firewall-cmd --get-service              # 取得当前支持 service
firewall-cmd --get-service --permanent  # 检查下一次重载后将激活的服务

firewall-cmd --zone=public --list-ports # 列出 zone public 端口
firewall-cmd --zone=public --list-all   # 列出 zone public 当前设置
```

**配置开放服务/端口**
```bash
firewall-cmd --zone=public --add-service=http       # 增加 zone public 开放http service
firewall-cmd --reload                               # 重新加载配置

firewall-cmd --zone=public --remove-service=http    # 从 zone 中移除 http 服务

firewall-cmd --zone=internal --add-port=443/tcp     # 增加 zone internal 开放 443/tcp 协议端口
firewall-cmd --zone=internal --remove-port=443/tcp  # 从 zone 中移除 443 端口
```

**设置黑/白名单**
```bash
firewall-cmd --permanent --zone=trusted --add-source=172.28.129.0/24    # 增加 172.28.129.0/24 网段到 zone trusted
firewall-cmd --permanent --zone=trusted --list-sources                  # 列出 zone truste 的白名单
firewall-cmd --reload
firewall-cmd --get-active-zones

firewall-cmd --permanent --zone=drop --add-source=172.28.13.0/24        # 添加 172.28.13.0/24 到 zone drop
firewall-cmd --reload
firewall-cmd --zone=drop --list-all

firewall-cmd --permanent --zone=drop --remove-source=172.28.13.0/24     # 从zone drop 中删除 172.28.13.0/24
```

- 使用命令的时候加上 --permanent 是永久生效的意思，在重启防火墙服务后依然生效.否则，只对重启服务之前有效.
- 我们执行的命令，结果其实都体现在具体的配置文件中，其实我们可以直接修改对应的配置文件即可.以 public zone 为例，对应的配置文件是 `/etc/firewalld/zones/public.xml`

**自定义区域**

你可以随意使用 firewalld 默认提供的这些区域，不过也完全可以创建自己的区域。比如如果希望有一个针对游戏的特别区域，你可以创建一个，然后只有在玩儿游戏的时候切换到该区域。

如果想要创建一个新的空白区域，你可以创建一个名为 game 的新区域，然后重新加载防火墙规则，这样你的新区域就启用了：
```bash
firewall-cmd --new-zone game --permanent
firewall-cmd --reload
```

## 配置案例

**只允许 1.1.1.1 和 2.2.2.2 访问**
```bash
systemctl start firewalld
# 配置 IP 白名单
firewall-cmd --permanent --zone=trusted --add-source=1.1.1.1
firewall-cmd --permanent --zone=trusted --add-source=2.2.2.2
# 与此同时，你也要加入你自己的 IP 地址，否则白名单一旦生效，可能会将你阻挡在外而无法连接。
firewall-cmd --reload
# 确认 trusted 区域是否设置正确
firewall-cmd --zone=trusted --list-all

# 因为此时已经设置了 trusted 区域，所以还需要切换默认区域从 public 到 drop，以达到无视所有接入连接的目的
firewall-cmd --set-default-zone=drop

# 将默认网卡 ens33 分配给 drop 区域
firewall-cmd --permanent --zone=drop --change-interface=ens33
firewall-cmd --reload
```

**配置端口白名单**
```bash
# 查询端口是否开放
firewall-cmd --query-port=8080/tcp
# 新建永久规则，开放 8080 端口（TCP 协议）, 任何 ip 都可以访问
firewall-cmd --permanent --add-port=8080/tcp
# 移除上述规则
firewall-cmd --permanent --remove-port=8080/tcp
# 新建永久规则，批量开放一段端口（TCP 协议）
firewall-cmd --permanent --add-port=9001-9100/tcp

# 添加或者移除规则后重新加载 firewall 后配置才会生效
firewall-cmd --reload
```

**只允许 123.123.123.123/1.2.3.4/1.14.5.14/1.9.1.9 对 8888 的访问**
```

firewall-cmd --zone=public --add-port=1-18999/tcp --permanent
firewall-cmd --zone=public --add-port=19001-65535/tcp --permanent

firewall-cmd --zone=public --add-port=1-18999/udp --permanent
firewall-cmd --zone=public --add-port=19001-65535/udp --permanent


firewall-cmd --zone=public --remove-port=19000/tcp --permanent
firewall-cmd --zone=public --remove-port=19000/udp --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="123.123.123.123" port port=19000 protocol=tcp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="123.123.123.123" port port=19000 protocol=udp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="1.2.3.4" port port=19000 protocol=tcp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="1.2.3.4" port port=19000 protocol=udp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="1.14.5.14" port port=19000 protocol=tcp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="1.14.5.14" port port=19000 protocol=udp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="1.9.1.9" port port=19000 protocol=tcp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="1.9.1.9" port port=19000 protocol=udp accept' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="0.0.0.0/32" port port=19000 protocol=tcp reject' --permanent
firewall-cmd --zone=public --add-rich-rule 'rule family="ipv4" source address="0.0.0.0/32" port port=19000 protocol=udp reject' --permanent

firewall-cmd --reload
firewall-cmd --zone=public --list-all

firewall-cmd --get-active-zones
firewall-cmd --get-default-zone

firewall-cmd --set-default-zone=public
firewall-cmd --permanent --zone=public --change-interface=ens33

firewall-cmd --reload
```

---

## docker 与 firewalld/iptable 的冲突

由于docker在启动容器时，会向iptables注⼊一些端口映射的规则，当使用 firewalld 时会产生冲突
- https://wenku.baidu.com/view/3d8b2fe85cbfc77da26925c52cc58bd6318693c4.html
- https://blog.csdn.net/qq_31927797/article/details/109454314
- https://blog.csdn.net/rookie23rook/article/details/120297212

```bash
iptables -t nat -nL

# 删除对应的 docker 规则
iptables -t nat -D DOCKER 13
# 手动加个转发
iptables -t nat -A DOCKER -d 127.0.0.1 -p tcp -m tcp --dport 19000 -j DNAT --to-destination 192.168.16.2:80

iptables -A INPUT -p tcp --dport 19000 -j DROP
iptables -I INPUT -s 1.14.5.14 -p tcp --dport 19000 -j ACCEPT
iptables -I INPUT -s 1.9.1.9 -p tcp --dport 19000 -j ACCEPT
```

---

## Source & Reference

- [使用防火墙让你的 Linux 更加强大](https://linux.cn/article-11093-1.html)
- https://teddysun.com/566.html
- https://blog.csdn.net/avatar_2009/article/details/112512819
- https://blog.csdn.net/jnloverll/article/details/120333488
