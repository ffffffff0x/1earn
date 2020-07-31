# Wireshark

<p align="center">
    <img src="../../../assets/img/logo/wireshark.png" width="22%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**官网**
- https://www.wireshark.org/

**样本**
- [SpiderLabs/IOCs-IDPS](https://github.com/SpiderLabs/IOCs-IDPS) - 该存储库将保存与已知恶意软件样本相关的 PCAP IOC 数据
- [Web 2.0 for packets | pcapr](https://www.pcapr.net/home) - 提供大量样本的社区
- [automayt/ICS-pcap](https://github.com/automayt/ICS-pcap) - 各类工控的 pcap 包
- [ICS-Security-Tools/pcaps](https://github.com/ITI/ICS-Security-Tools/tree/master/pcaps) - 各类工控的 pcap 包

**在线分析**
- [NetworkTotal - Free Online Network Traffic Scanner](https://www.networktotal.com/index.html)
- [VirusTotal](https://www.virustotal.com/gui/home/upload)

**文章 & Reference**
- [wireshark基本用法及过虑规则](https://blog.csdn.net/hzhsan/article/details/43453251)
- [SampleCaptures - The Wireshark Wiki](https://wiki.wireshark.org/SampleCaptures)
- [CaptureSetup/USB - The Wireshark Wiki](https://wiki.wireshark.org/CaptureSetup/USB)
- [图解Wireshark协议分析实例](https://blog.csdn.net/bcbobo21cn/article/details/51454170)

**插件/增强工具**
- [pentesteracademy/patoolkit](https://github.com/pentesteracademy/patoolkit) - Wireshark 插件，增强分析能力
- [leolovenet/qqwry2mmdb](https://github.com/leolovenet/qqwry2mmdb) - 为 Wireshark 能使用纯真网络 IP 数据库(QQwry)而提供的格式转换工具,不支持 windows

---

# 安装

**Ubuntu**
```bash
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install wireshark
```

**Windows**

略

---

# 过滤语法

**比较操作符**
```bash
lt   <      # 小于
le   <=     # 小于等于
eq   ==     # 等于
gt   >      # 大于
ge   >=     # 大于等于
ne   !=     # 不等
and         # 两个条件同时满足
or          # 其中一个条件被满足
xor         # 有且仅有一个条件被满足
not         # 没有条件被满足
```

**快速使用**
```bash
http.request.method == "POST"       # POST 请求
tcp contains "http"                 # 显示 payload 中包括"http"字符串的 tcp 封包.
http.request.uri contains "online"  # 显示请求的 uri 包括"online"的 http 封包.
ip.addr == 1.1.1.1                  # IP 为 1.1.1.1 的流量

Ctrl+Alt+Shift+T,切换跟踪 tcp 流
```

**过滤 IP**

如来源 IP 或者目标 IP 等于某个 IP
```bash
ip.src eq 192.168.1.254 or ip.dst eq 192.168.1.254

或

ip.addr eq 192.168.1.254            # 都能显示来源 IP 和目标 IP
```

**过滤端口**

```bash
tcp.port eq 80                      # 不管端口是来源的还是目标的都显示
tcp.port == 80
tcp.port eq 2722
tcp.port eq 80 or udp.port eq 80
tcp.dstport == 80                   # 只显 tcp 协议的目标端口 80
tcp.srcport == 80                   # 只显 tcp 协议的来源端口 80

udp.port eq 15000
```

```bash
tcp.port >= 1 and tcp.port <= 80    # 过滤端口范围
```

**过滤协议**

```bash
tcp
udp
arp
icmp
http
smtp
ftp
dns
msnms
ip
ssl
oicq
bootp
```

排除 arp 包，如 `!arp` 或者 `not arp`

**过滤 MAC**

以太网头过滤
```bash
eth.dst == A0:00:00:04:C5:84    # 过滤目标 mac
eth.src eq A0:00:00:04:C5:84    # 过滤来源 mac
eth.dst==A0:00:00:04:C5:84
eth.dst==A0-00-00-04-C5-84
eth.addr eq A0:00:00:04:C5:84   # 过滤来源 MAC 和目标 MAC 都等于 A0:00:00:04:C5:84 的
```

**包长度过滤**

```bash
udp.length == 26                # 这个长度是指 udp 本身固定长度8加上 udp 下面那块数据包之和
tcp.len >= 7                    # 指的是 ip 数据包(tcp 下面那块数据),不包括 tcp 本身
ip.len == 94                    # 除了以太网头固定长度 14,其它都算是 ip.len,即从 ip 本身到最后
frame.len == 119                # 整个数据包长度,从 eth 开始到最后
```

**http 模式过滤**

```bash
http.request.method == “GET”
http.request.method == “POST”
http.request.uri == “/img/logo-edu.gif”
http contains “GET”
http contains “HTTP/1.”

# GET包
http.request.method == “GET” && http contains “Host: “
http.request.method == “GET” && http contains “User-Agent: “
# POST包
http.request.method == “POST” && http contains “Host: “
http.request.method == “POST” && http contains “User-Agent: “
# 响应包
http contains “HTTP/1.1 200 OK” && http contains “Content-Type: “
http contains “HTTP/1.0 200 OK” && http contains “Content-Type: “
```

**TCP 参数过滤**

```bash
tcp.flags                   # 显示包含 TCP 标志的封包。
tcp.flags.syn == 0x02       # 显示包含 TCP SYN 标志的封包。
tcp.flags.reset == 1        # 过滤 TCP RST 包。先找到 RST 包，然后右键 Follow -> TCP Stream 是常用的排障方式
tcp.window_size == 0 && tcp.flags.reset != 1
tcp.analysis.retransmission # 过滤所有的重传包
```

**包内容过滤**

```bash
tcp[20]                     # 表示从 20 开始，取 1 个字符
tcp[20:]                    # 表示从 20 开始，取 1 个字符以上
tcp[20:8]                   # 表示从 20 开始，取 8 个字符
```
```bash
udp[8:1]==32
udp[8:3]==81:60:03          # 偏移 8 个 bytes,再取 3 个数，是否与 == 后面的数据相等
eth.addr[0:3]==00:06:5B
```

matches(匹配)和 contains(包含某字符串)语法
```bash
ip.src==192.168.1.107 and udp[8:5] matches “\\x02\\x12\\x21\\x00\\x22″
ip.src==192.168.1.107 and udp contains 02:12:21:00:22
ip.src==192.168.1.107 and tcp contains “GET”
udp contains 7c:7c:7d:7d    # 匹配 payload 中含有 0x7c7c7d7d 的 UDP 数据包，不一定是从第一字节匹配。
```

---

# 捕获USB流量

**工具**
- [USBPcap - USB Packet capture for Windows](https://desowin.org/usbpcap/)
- [JohnDMcMaster/usbrply](https://github.com/JohnDMcMaster/usbrply) - 将 .pcap 文件（捕获的 USB 数据包）转换为 Python 或 C 代码，以重播捕获的 USB 命令。

**文章**
- [使用wireshark抓取USB包](https://blog.csdn.net/shiailan/article/details/97305163)
- [Wireshark如何捕获USB流量](https://www.freebuf.com/column/166711.html)

---

# 案例

- 更多案例参考 [流量分析](../实验/BlueTeam/流量分析.md)
