# SDN 笔记

---

## ODL虚拟机基础配置

开完 ODL 虚拟机后先配置 IP
配置文件在 /etc/network/interface 目录下.
```bash
vim /etc/network/interface

iface eth0 inet static
address 172.16.9.100  # 修改成自己的 IP 地址
netmask 255.255.255.0 # 修改成自己的掩码地址
gateway 172.16.9.254  # 修改成自己的网关地址
```
建议虚拟机开 NAT 模式
然后 IP 配置同网段 vmnet 网卡 IP
再用 SecureCRT 开3个窗口 SSH 上去，一个窗口开 Opendaylight，一个窗口开 Mininet,一个配置流表

---

## OpenDaylight

```bash
cd ODL/bin/
sudo ./karaf

opendaylight-user@root> feature:install odl-restconf
opendaylight-user@root> feature:install odl-l2switch-switch-ui
opendaylight-user@root> feature:install odl-mdsal-apidocs
opendaylight-user@root> feature:install odl-dluxapps-applications

# 组件安装完成后，可以通过浏览器访问 OpenDaylight WEB 控制台，访问的 url 为:http://{controller_ip}:8181/index.html
# 登录用户名和密码都是 admin
# 其中{controller_ip}为 OpenDaylight 控制器的 IP 地址，如果是本机，则 ip 地址可以为 127.0.0.1.

# 如果是SSH开2窗口的就不用挂起后台运行了，下面2步仅针对单 session 操作
Ctrl+z  # 后台挂起
bg      # 后台运行，不然不好访问 web
```

---

## Mininet

使用 mininet 生成网络拓扑
> sudo mn --controller=remote,ip=xxx,xxx,xxx,xxx

显示 Mininet CLI 命令:
> mininet> help

显示节点:
> mininet> nodes

显示网络链接:
> mininet> net

输出所有节点的信息:
> mininet> dump

### 示例

**例1**
#### 单交换机(Single switch)

```
sudo mn --arp --topo single,3 --mac --switch ovsk --controller remote
- mac:自动设置 MAC 地址，MAC 地址与 IP 地址的最后一个字节相同
- arp:为每个主机设置静态ARP表，例如:主机1中有主机2和主机3的 IP 地址和 MAC 地址 ARP 表项，主机2和主机3依次类推.
- switch:使用 OVS 的核心模式
- controller:使用远程控制器，可以指定远程控制器的 IP 地址和端口号，如果不指定则默认为 127.0.0.1 和 6633
```

![](../../../../assets/img/Integrated/Network/sdn/1.png)

创建完拓扑后即可使用 ping 命令进行测试:h1 ping h2
(注意:如果没有指定控制器的话，是 ping 不通的)

**例2**

使用 Mininet 和 OpenVswitch 构建拓扑，采用采用 OVS 交换机格式，连接 ODL 的 6653 端口 Openflow1.3 协议

#### 深度2，扇出系数2

```
sudo mn --topo tree,2,2 --switch ovs,protocols=OpenFlow13 --controller remote,ip=127.0.0.1,port=6653
```

```
    s2 --- s1 ---  s3
h1  h2           h3 h4
```

```
pingall //测试
```

---

**例3**

使用 Mininet 构建拓扑，采用 ovsk 交换格式，连接 ODL 的远程地址为 192.168.10.128:6653,协议类型是 Openflow1.30

```
sudo mn --topo tree,2,2 --switch ovsk,protocols=OpenFlow13 --controller remote,ip=192.168.10.128,port=6653
```

```
    s2 --- s1 ---  s3
h1  h2           h3 h4
```

```
pingall //测试
```

---

**例4**

#### 两个线性连接的交换机

使用 Mininet 和 OpenVswitch 构建拓扑，连接 ODL 的 6653 端口采用 Openflow1.3 协议

*下面的命令创建具有2个交换机，两个交换机下面个连一个主机，交换机之间再互连起来.*

```
sudo mn --topo linear --protocols=OpenFlow13  --controller remote,ip=127.0.0.1,port=6653
```

```
  c0
s1--s2
h1  h2
```
```
pingall //测试
```

---

## 流表
### 示例

流表操作在第三个窗口上进行，当然在 mininet 中可以在命令前加上 sh 运行

***再提醒一下，流表操作在第三个窗口上进行,前面加 sudo***

***如果在 mininet 中可以在命令前加上 sh 运行***

**例1**

通过 OVS 下发流表，H1 与 H2 可以互通，H1 与 H3 不能互通，但 H3 和 H4 之间可以互通.

```
ovs-vsctl show
ovs-ofctl  -O Openflow13 add-flow s2 'dl_type=0x0800,nw_src=10.0.0.1,nw_dst=10.0.0.3, priority=27,table=0,actions=drop'
```

将主机1发给主机3的数据包丢弃

该流表项的匹配字段包括:
- dl_type=0x0800(MAC帧上一层为IP协议)
- nw_src=10.0.0.1(源IP地址为10.0.0.1)
- nw_dst=10.0.0.3(目的IP地址为10.0.0.3)
- 优先级 priority 设为27，高于其他流表，故优先执行;
- table id 为0，即将该流表项下发到table 0中.
- 该流表项表示:从主机 10.0.0.1 发往主机 10.0.0.3 的IP包将被抛弃.

查看控制器下发的流表项
```
ovs-ofctl dump-flows s2
```

```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 X h4
h2 -> h1 h3 h4
h3 -> X h2 h4
h4 -> h1 h2 h3
*** Results: 16% dropped (10/12 received)
```

---

**例2**
```
    s2 --- s1 ---  s3
h1  h2           h3 h4
```
H1 启动 HTTP-Server 功能，WEB 端口为 80，H2 作为 HTTP-Client，获取 H1 的 html 网页文件.
```
HTTPSERVER : h1 python -m SimpleHTTPServer 80 &
HTTPCLIENT: h2 curl h1
```

通过 OVS 手工命令在 openflow:1 虚拟交换机下发流表，只允许下发一条流表，优先级为 priority=50 实现如下需求:H1 与 H2 可以互通，H1 与 H3 不能互通，但 H3 和 H4 之间可以互通.
```
ovs-ofctl  -O Openflow13 add-flow s1 'dl_type=0x0800,nw_src=10.0.0.1,nw_dst=10.0.0.3, priority=50,table=0,actions=drop'
```
将主机1发给主机3的数据包丢弃

用 iperf 工具测试 H3 和 H4 的带宽.
```
iperf h3 h4
```

---

**例3**
```
    s1
h1  h2  h3
```

通过 OVS 手工下发流表，H1 可以 ping 通 H3，H1 无法 ping 通 H2.
```
ovs-ofctl  -O Openflow13 add-flow s1 'dl_type=0x0800,nw_src=10.0.0.1,nw_dst=10.0.0.2, priority=27,table=0,actions=drop'
```
将主机1发给主机2的数据包丢弃

---

**例4**
```
  s1
h1  h2
```
通过 OVS 手工下发流表，H1 和 H2 互通.H1 启动 HTTPSERVER 功能，WEB 端口为 4330，H2 作为 HTTPCLIENT，获取 H1 的 html 网页文件.
```
HTTPSERVER : h1 python -m SimpleHTTPServer 4330 &
HTTPCLIENT: h2 curl h1
```

下发流表使得 H1 和 H2 不通
```
ovs-ofctl  -O Openflow13 add-flow s1 'dl_type=0x0800,nw_src=10.0.0.1,nw_dst=10.0.0.2, priority=27,table=0,actions=drop'
```
将主机1发给主机2的数据包丢弃

---

**例5**
```
  c0
s1--s2
h1  h2
```

通过 OVS 给S2下发流表，使得 H1 与 H2 无法互通.
```
ovs-ofctl  -O Openflow13 add-flow s2 'dl_type=0x0800,nw_src=10.0.0.1,nw_dst=10.0.0.2, priority=27,table=0,actions=drop'
```
将主机1发给主机2的数据包丢弃

---

### 控制管理类

1. 查看网桥和端口
```
ovs-vsctl show
```

2. 创建一个网桥
```
ovs-vsctl add-br br0
ovs-vsctl set bridge br0 datapath_type=netdev
```

3. 添加/删除一个端口
```
# for system interfaces
ovs-vsctl add-port br0 eth1
ovs-vsctl del-port br0 eth1
# for DPDK
ovs-vsctl add-port br0 dpdk1 -- set interface dpdk1 type=dpdk
options:dpdk-devargs=0000:01:00.0
# for DPDK bonds
ovs-vsctl add-bond br0 dpdkbond0 dpdk1 dpdk2 \
-- set interface dpdk1 type=dpdk options:dpdk-devargs=0000:01:00.0 \
-- set interface dpdk2 type=dpdk options:dpdk-devargs=0000:02:00.0
```

4. 设置/清除网桥的 openflow 协议版本
```
ovs-vsctl set bridge br0 protocols=OpenFlow13
ovs-vsctl clear bridge br0 protocols
```

5. 查看某网桥当前流表
```
ovs-ofctl dump-flows br0
ovs-ofctl -O OpenFlow13 dump-flows br0
ovs-appctl bridge/dump-flows br0
```

6. 设置/删除控制器
```
ovs-vsctl set-controller br0 tcp:1.2.3.4:6633
ovs-vsctl del-controller br0
```

7. 查看控制器列表
```
ovs-vsctl list controller
```

8. 设置/删除被动连接控制器
```
ovs-vsctl set-manager tcp:1.2.3.4:6640
ovs-vsctl get-manager
ovs-vsctl del-manager
```

9. 设置/移除可选选项
```
ovs-vsctl set Interface eth0 options:link_speed=1G
ovs-vsctl remove Interface eth0 options link_speed
```

10. 设置 fail 模式，支持 standalone 或者 secure

- standalone(default):清除所有控制器下发的流表，ovs 自己接管
- secure:按照原来流表继续转发

```
ovs-vsctl del-fail-mode br0
ovs-vsctl set-fail-mode br0 secure
ovs-vsctl get-fail-mode br0
```

11. 查看接口 id 等
```
ovs-appctl dpif/show
```

12. 查看接口统计
```
ovs-ofctl dump-ports br0
```

### 流表类
#### 流表操作

1. 添加普通流表
```
ovs-ofctl add-flow br0 in_port=1,actions=output:2
```

2. 删除所有流表
```
ovs-ofctl del-flows br0
```

3. 按匹配项来删除流表
```
ovs-ofctl del-flows br0 "in_port=1"
```

#### 匹配项

1. 匹配 vlan tag，范围为 0-4095
```
ovs-ofctl add-flow br0
priority=401,in_port=1,dl_vlan=777,actions=output:2
```

2. 匹配 vlan pcp，范围为 0-7
```
ovs-ofctl add-flow br0
priority=401,in_port=1,dl_vlan_pcp=7,actions=output:2
```

3. 匹配源/目的 MAC
```
ovs-ofctl add-flow br0
in_port=1,dl_src=00:00:00:00:00:01/00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow br0
in_port=1,dl_dst=00:00:00:00:00:01/00:00:00:00:00:01,actions=output:2
```

4. 匹配以太网类型，范围为 0-65535
```
ovs-ofctl add-flow br0 in_port=1,dl_type=0x0806,actions=output:2
```

5. 匹配源/目的 IP
条件:指定 dl_type=0x0800，或者 ip/tcp
```
ovs-ofctl add-flow br0
ip,in_port=1,nw_src=10.10.0.0/16,actions=output:2
ovs-ofctl add-flow br0
ip,in_port=1,nw_dst=10.20.0.0/16,actions=output:2
```

6. 匹配协议号，范围为 0-255
条件:指定 dl_type=0x0800 或者 ip/ICMP
```
ovs-ofctl add-flow br0 ip,in_port=1,nw_proto=1,actions=output:2
```

7. 匹配 IP ToS/DSCP，tos 范围为 0-255，DSCP 范围为 0-63
条件:指定 dl_type=0x0800/0x86dd，并且 ToS 低 2 位会被忽略(DSCP 值为
ToS 的高 6 位，并且低 2 位为预留位)
```
ovs-ofctl add-flow br0 ip,in_port=1,nw_tos=68,actions=output:2
ovs-ofctl add-flow br0 ip,in_port=1,ip_dscp=62,actions=output:2
```

8. 匹配 IP ecn 位，范围为 0-3
条件:指定 dl_type=0x0800/0x86dd
```
ovs-ofctl add-flow br0 ip,in_port=1,ip_ecn=2,actions=output:2
```

9. 匹配 IP TTL，范围为 0-255
```
ovs-ofctl add-flow br0 ip,in_port=1,nw_ttl=128,actions=output:2
```

10. 匹配 tcp/udp，源/目的端口，范围为 0-65535
```
# 匹配源 tcp 端口 179
ovs-ofctl add-flow br0 tcp,tcp_src=179/0xfff0,actions=output:2
# 匹配目的 tcp 端口 179
ovs-ofctl add-flow br0 tcp,tcp_dst=179/0xfff0,actions=output:2
# 匹配源 udp 端口 1234
ovs-ofctl add-flow br0 udp,udp_src=1234/0xfff0,actions=output:2
# 匹配目的 udp 端口 1234
ovs-ofctl add-flow br0 udp,udp_dst=1234/0xfff0,actions=output:2
```
11. 匹配 tcp flags
tcp flags=fin，syn，rst，psh，ack，urg，ece，cwr，ns
```
ovs-ofctl add-flow br0 tcp,tcp_flags=ack,actions=output:2
```

12. 匹配 icmp code，范围为 0-255
条件:指定 icmp
```
ovs-ofctl add-flow br0 icmp,icmp_code=2,actions=output:2
```

13. 匹配 vlan TCI
TCI 低 12 位为 vlan id，高 3 位为 priority，例如 tci=0xf123 则 vlan_id 为 0x123
和 vlan_pcp=7
```
ovs-ofctl add-flow br0 in_port=1,vlan_tci=0xf123,actions=output:2
```

14. 匹配 mpls label
条件:指定 dl_type=0x8847/0x8848
```
ovs-ofctl add-flow br0 mpls,in_port=1,mpls_label=7,actions=output:2
```

15. 匹配 mpls tc，范围为 0-7
条件:指定 dl_type=0x8847/0x8848
```
ovs-ofctl add-flow br0 mpls,in_port=1,mpls_tc=7,actions=output:2
```

16. 匹配 tunnel id，源/目的 IP
```
# 匹配 tunnel id
ovs-ofctl add-flow br0 in_port=1,tun_id=0x7/0xf,actions=output:2
# 匹配 tunnel 源 IP
ovs-ofctl add-flow br0
in_port=1,tun_src=192.168.1.0/255.255.255.0,actions=output:2
# 匹配 tunnel 目的 IP
ovs-ofctl add-flow br0
in_port=1,tun_dst=192.168.1.0/255.255.255.0,actions=output:2
```

#### 指令动作

1. 动作为出接口
```bash
# 从指定接口转发出去
ovs-ofctl add-flow br0 in_port=1,actions=output:2
```

2. 动作为指定 group
```bash
# group id 为已创建的 group table
ovs-ofctl add-flow br0 in_port=1,actions=group:666
```

3. 动作为 normal
```bash
# 转为 L2/L3 处理流程
ovs-ofctl add-flow br0 in_port=1,actions=normal
```

4. 动作为 flood
```bash
# 从所有物理接口转发出去，除了入接口和已关闭 flooding 的接口
ovs-ofctl add-flow br0 in_port=1,actions=flood
```

5. 动作为 all
```bash
# 从所有物理接口转发出去，除了入接口
ovs-ofctl add-flow br0 in_port=1,actions=all
```

6. 动作为 local
```bash
# 一般是转发给本地网桥
ovs-ofctl add-flow br0 in_port=1,actions=local
```

7. 动作为 in_port
```bash
# 从入接口转发回去
ovs-ofctl add-flow br0 in_port=1,actions=in_port
```

8. 动作为 controller
```bash
# 以 packet-in 消息上送给控制器
ovs-ofctl add-flow br0 in_port=1,actions=controller
```

9. 动作为 drop
```bash
# 丢弃数据包操作
ovs-ofctl add-flow br0 in_port=1,actions=drop
```

10. 动作为 mod_vlan_vid
```bash
# 修改报文的 vlan id，该选项会使 vlan_pcp 置为 0
ovs-ofctl add-flow br0 in_port=1,actions=mod_vlan_vid:8,output:2
```

11. 动作为 mod_vlan_pcp
```bash
# 修改报文的 vlan 优先级，该选项会使 vlan_id 置为 0
ovs-ofctl add-flow br0 in_port=1,actions=mod_vlan_pcp:7,output:2
```

12. 动作为 strip_vlan
```bash
# 剥掉报文内外层 vlan tag
ovs-ofctl add-flow br0 in_port=1,actions=strip_vlan,output:2
```

13. 动作为 push_vlan
```bash
# 在报文外层压入一层 vlan tag，需要使用 openflow1.1 以上版本兼容
ovs-ofctl add-flow -O OpenFlow13 br0 in_port=1,actions=push_vlan:0x8100,set_field:4097-\>vlan_vid,output:2
# set field 值为 4096+vlan_id，并且 vlan 优先级为 0，即 4096-8191，对应的vlan_id 为 0-4095
```

14. 动作为 push_mpls
```bash
# 修改报文的 ethertype，并且压入一个 MPLS LSE
ovs-ofctl add-flow br0 in_port=1,actions=push_mpls:0x8847,set_field:10-\>mpls_label,output:2
```

15. 动作为 pop_mpls
```bash
# 剥掉最外层 mpls 标签，并且修改 ethertype 为非 mpls 类型
ovs-ofctl add-flow br0 mpls,in_port=1,mpls_label=20,actions=pop_mpls:0x0800,output:2
```

16. 动作为修改源/目的 MAC，修改源/目的 IP
```bash
# 修改源 MAC
ovs-ofctl add-flow br0
in_port=1,actions=mod_dl_src:00:00:00:00:00:01,output:2
# 修改目的 MAC
ovs-ofctl add-flow br0
in_port=1,actions=mod_dl_dst:00:00:00:00:00:01,output:2
# 修改源 IP
ovs-ofctl add-flow br0
in_port=1,actions=mod_nw_src:192.168.1.1,output:2
# 修改目的 IP
ovs-ofctl add-flow br0
in_port=1,actions=mod_nw_dst:192.168.1.1,output:2
```

17. 动作为修改 TCP/UDP/SCTP 源目的端口
```bash
# 修改 TCP 源端口
ovs-ofctl add-flow br0 tcp,in_port=1,actions=mod_tp_src:67,output:2
# 修改 TCP 目的端口
ovs-ofctl add-flow br0 tcp,in_port=1,actions=mod_tp_dst:68,output:2
# 修改 UDP 源端口
ovs-ofctl add-flow br0 udp,in_port=1,actions=mod_tp_src:67,output:2
# 修改 UDP 目的端口
ovs-ofctl add-flow br0 udp,in_port=1,actions=mod_tp_dst:68,output:2
```

18. 动作为 mod_nw_tos
```bash
# 条件:指定 dl_type=0x0800
# 修改 ToS 字段的高 6 位，范围为 0-255，值必须为 4 的倍数，并且不会去修改 ToS 低 2 位 ecn 值
ovs-ofctl add-flow br0 ip,in_port=1,actions=mod_nw_tos:68,output:2
```

19. 动作为 mod_nw_ecn
```bash
# 条件:指定 dl_type=0x0800，需要使用 openflow1.1 以上版本兼容
# 修改 ToS 字段的低 2 位，范围为 0-3，并且不会去修改 ToS 高 6 位的 DSCP 值
ovs-ofctl add-flow br0 ip,in_port=1,actions=mod_nw_ecn:2,output:2
```

20. 动作为 mod_nw_ttl
```bash
# 修改 IP 报文 ttl 值，需要使用 openflow1.1 以上版本兼容
ovs-ofctl add-flow -O OpenFlow13 br0 in_port=1,actions=mod_nw_ttl:6,output:2
```

21. 动作为 dec_ttl
```bash
# 对 IP 报文进行 ttl 自减操作
ovs-ofctl add-flow br0 in_port=1,actions=dec_ttl,output:2
```

22. 动作为 set_mpls_label
```bash
# 对报文最外层 mpls 标签进行修改，范围为 20bit 值
ovs-ofctl add-flow br0 in_port=1,actions=set_mpls_label:666,output:2
```

23. 动作为 set_mpls_tc
```bash
# 对报文最外层 mpls tc 进行修改，范围为 0-7
ovs-ofctl add-flow br0 in_port=1,actions=set_mpls_tc:7,output:2
```

24. 动作为 set_mpls_ttl
```bash
# 对报文最外层 mpls ttl 进行修改，范围为 0-255
ovs-ofctl add-flow br0 in_port=1,actions=set_mpls_ttl:255,output:2
```

25. 动作为 dec_mpls_ttl
```bash
# 对报文最外层 mpls ttl 进行自减操作
ovs-ofctl add-flow br0 in_port=1,actions=dec_mpls_ttl,output:2
```

26. 动作为 move NXM 字段
```bash
# 使用 move 参数对 NXM 字段进行操作
# 将报文源 MAC 复制到目的 MAC 字段，并且将源 MAC 改为 00:00:00:00:00:01
ovs-ofctl add-flow br0 in_port=1,actions=move:NXM_OF_ETH_SRC[]-\>NXM_OF_ETH_DST[],mod_dl_src:00:00:00:00:00:01,output:2
```

27. 动作为 load NXM 字段
```bash
# 使用 load 参数对 NXM 字段进行赋值操作
# push mpls label，并且把 10(0xa)赋值给 mpls label
ovs-ofctl add-flow br0 in_port=1,actions=push_mpls:0x8847,load:0xa-
\> oXM_OF_MPLS_LABEL[],output:2
# 对目的 MAC 进行赋值
ovs-ofctl add-flow br0 in_port=1,actions=load:0x001122334455-\> oXM_OF_ETH_DST[],output:2
```

28. 动作为 pop_vlan
```bash
# 弹出报文最外层 vlan tag
ovs-ofctl add-flow br0 in_port=1,dl_type=0x8100,dl_vlan=777,actions=pop_vlan,output:2
```
