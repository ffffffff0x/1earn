# nmap 小记

---

## Reference

- [Nmap参考指南(Man Page)](https://nmap.org/man/zh/)

---

# 用法
`nmap -T5 -A -vv xx.xx.xx.xx` 这条命令的意思是往死里扫，管 TM 封不封地址

## 常用参数

```
-F             端口扫描
-sT            tcp 端口扫描
-sU            udp 扫描
-A             综合扫描
-O             系统扫描
-p             指定端口扫描
-T             优化时间 1-5 强度
-sV            端口对应的服务探测
-sP            发现扫描网络存活主机
-sS            半隐藏式隐蔽扫描
--iL           从主机/网络列表输入
--tr           路由跟踪模式
-P0            (无 ping)
-sP            (Ping 扫描)

--script=vuln  利用脚本漏洞探测
--script=>>>>>>>   调用一个脚本
-oG  nmap.txt  将结果保存到 nmap.txt
```

---

## 基本操作

nmap 默认发送一个 ARP 的 PING 数据包，来探测目标主机 1-10000 范围内所开放的所有端口

`nmap <target ip>`

**详细的描述输出**

`namp -vv <target ip>`

**自定义扫描**

`nmap -p (range) <target IP>`

**指定端口扫描**

`nmap -p (port1,port2,…) <target IP>`

**ping 扫描**

`nmap -sP <target ip>`

**路由跟踪**

`nmap –traceroute <target IP>`

**扫描一个段**

`nmap -sP <network address> </CIDR>`

**探测操作系统类型**

`nmap -0 <target IP>`

**进攻性扫描**

`nmap -A <target ip>`

**混合式扫描**

`nmap -vv -p1-100 -O <target ip>`

**用一组 IP 地址掩盖真实地址**
`namp -D <IP地址1,IP地址2... IP地址> <target ip>`

**伪装 MAC 地址**

`nmap --spoof-mac <伪造 MAC IP地址> <target ip>`

**指定网卡进行扫描**

`nmap -e <iface> <target ip>`

**伪装成其他 IP 地址**
`nmap -S <伪造IP地址> <target ip>`

**指定源端口**

`nmap -g/--source-port <portnum> <target ip>`

**扫描速度**

`nmap -T<1-5> <target ip>`

---

## 脚本
**[smb-enum-users](https://nmap.org/nsedoc/scripts/smb-enum-users.html)**

用于枚举SMB用户

```
nmap --script smb-enum-users.nse -p445 <host>
sudo nmap -sU -sS --script smb-enum-users.nse -p U:137,T:139 <host>
```

