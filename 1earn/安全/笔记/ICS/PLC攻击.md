# PLC攻击

---

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**PLC的概念**

PLC 控制系统(Programmable Logic Controller，可编程逻辑控制器)，专为工业生产设计的一种数字运算操作的电子装置，它采用一类可编程的存储器，用于其内部存储程序，执行逻辑运算，顺序控制，定时，计数与算术操作等面向用户的指令，并通过数字或模拟式输入/输出控制各种类型的机械或生产过程。是工业控制的核心部分。简要的说，PLC 就是一部小型的工业电脑。

**PLC的使用介绍**
- [[图文]西门子S7-300教程 第1章](https://wenku.baidu.com/view/eb015e01b52acfc789ebc9cd)
- [[图文]西门子S7-300教程 第2章](https://wenku.baidu.com/view/86d25c104431b90d6c85c7cf.html)
- [[图文]西门子S7-300教程 第3章](https://wenku.baidu.com/view/9e1e454f852458fb770b56c9)

**相关文章**
- [从0~1学习PLC攻击](https://www.freebuf.com/column/238349.html) - 复现 DCCE MAC1100 PLC 任意程序覆盖漏洞
- [工控安全-初识西门子PLC~S7-200](https://www.freebuf.com/column/202499.html)
- [PLC编程与应用入门——（一）](https://www.freebuf.com/column/206084.html)
- [工控安全 | 西门子S7-300攻击分析](https://www.freebuf.com/articles/ics-articles/228770.html)
- [工控安全：S7-1200 PLC远程启停攻击实验](https://www.key1.top/index.php/archives/469/)
- [西门子S7通信过程及重放攻击分析](https://www.freebuf.com/articles/ics-articles/212283.html)
- [【工控安全】大工PLC-远程启停攻击实验](https://mp.weixin.qq.com/s/k9tSpQaaeJ7QKSa9cb_bWg)
- [当PLC偶遇老旧但不乏经典的高级组包工具Hping3](https://www.freebuf.com/vuls/230453.html)
- [施耐德PLC漏洞历险记](https://www.freebuf.com/articles/ics-articles/234714.html)
- [PLC攻击类型研究分析](https://www.freebuf.com/articles/ics-articles/238351.html)

**漏洞利用框架**
- [dark-lbp/isf](https://github.com/dark-lbp/isf) - 基于 Python 开发的工控方面漏洞利用框架,类似 MetaSploit

**设备解密**
- [管中窥豹之工控设备解密](https://www.freebuf.com/articles/ics-articles/240727.html)

---

# 仿真搭建

## siemens

**相关文章**
- [西门子PLC的网络仿真搭建方法探讨](https://www.freebuf.com/articles/ics-articles/236250.html)

**模拟器工具**
- [Snap7 Homepage](http://snap7.sourceforge.net/) - 一款开源的 32/64 位多平台以太网通信套件，用于与西门子 S7 PLC 进行本地连接。
- STEP7
    - http://www.laozhoucontrol.com/S7-PLCSIM-V5_4-SP5-UPD1.html
    - http://www.laozhoucontrol.com/STEP7-V5_5-CN-SP2-install.html
- plcsim
    - http://www.laozhoucontrol.com/S7-PLCSIM-V5_4-SP5-UPD1.html
- [NetToPLCSim](https://sourceforge.net/projects/nettoplcsim/)

**实验记录**
- [siemens仿真搭建实验](../../实验/ICS/siemens仿真搭建实验.md)

---

# PLC inject

**介绍**

PLC inject 可以通过公网 PLC 访问到深层次的工业网络。可以实现的方法就是将 PLC 变成网关，这种方法在缺乏适当的防护功能的 PLC 上是可行的。技术娴熟的攻击者拥有某一个 PLC 的访问权限时，可以往上面上传或者下载代码，只要 PLC 设备支持对应的编码格式。而且代码被上传到 PLC 中后，就有很难被发现的特点，因为它不会中断程序的运行。当恶意代码被注入到 PLC 中后，会增加 PLC 中的代码量，如果我们定时观测原有代码和注入恶意代码后的程序，这两者的运行效果有明显的差异，然而其对生产过程的影响微乎其微。除非管理者主动监听从 PLC 中发出的恶意访问流量，否则很难在生产过程中发现。

**攻击过程**

攻击者注入代码后，它会与 PLC 上的正常代码一起运行；对本地网络进行扫描，同时攻击者可以从 PLC 中下载扫描结果，之后在注入一个 socks 代理，攻击者可以通过通过充当代理的 PLC 访问本地网络内的所有 PLC。

**相关文章/资源**
- [关于PLC安全的一次实验](https://www.freebuf.com/articles/ics-articles/233938.html)
- [Black Hat USA 2015 - Internet Facing PLCs A New Back Orifice](https://www.youtube.com/watch?v=FN_8lASQhrs)

**相关工具**
- [SCADACS/PLCinject](https://github.com/SCADACS/PLCinject)

**实验记录**
- [S7-300启停实验](../../实验/ICS/S7-300启停实验.md)
