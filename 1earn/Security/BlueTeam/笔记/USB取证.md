# USB取证

<p align="center">
    <img src="../../../../assets/img/banner/USB取证.jpg" width="90%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [USB - CTF Wiki](https://ctf-wiki.github.io/ctf-wiki/misc/traffic/protocols/USB-zh/)
- [USB流量取证分析](https://blog.csdn.net/qq_43431158/article/details/108717829)
- [USB流量取证分析](https://www.freebuf.com/articles/database/231809.html)
- [深入理解USB流量数据包的抓取与分析](https://www.cnblogs.com/ecjtuacm-873284962/p/9473808.html)
- [关于usb流量分析](https://www.jianshu.com/p/92064f2e9dcb)

**相关工具**
- [FzWjScJ/knm](https://github.com/FzWjScJ/knm) - 鼠标键盘流量包取证
- tshark
    ```bash
    tshark -r tmp.pcap -T fields -e usb.capdata > usbdata.txt
    # -r: 设置 tshark 分析的输入文件
    # -T: 设置解码结果输出的格式，包括 fileds,text,ps,psml 和 pdml，默认为 text

    # 如果提取出来的数据有空行，可以将命令改为如下形式：
    tshark -r tmp.pcap -T fields -e usb.capdata | sed '/^\s*$/d' > usbdata.txt
    ```
    > 提取出来的数据可能会带冒号，也可能不带，但是一般键盘映射的脚本都会按照有冒号的数据来识别，有冒号时提取数据的 [6:8]，无冒号时数据在 [4:6]，可以用如下脚本来加上冒号
    ```py
    # -*- coding: UTF-8 -*-
    f=open('usbdata.txt','r')
    fi=open('out.txt','w')
    while 1:
        a=f.readline().strip()
        if a:
            if len(a)==16:      # 键盘流量的话 len 改为 16, 鼠标流量改为 8
                out=''
                for i in range(0,len(a),2):
                    if i+2 != len(a):
                        out+=a[i]+a[i+1]+":"
                    else:
                        out+=a[i]+a[i+1]
                fi.write(out)
                fi.write('\n')
        else:
            break

    fi.close()
    ```

**CTF writup**
- [USB流量知识点小结](http://www.ga1axy.top/index.php/archives/22/)
- [记一道鼠标流量分析题](http://www.ga1axy.top/index.php/archives/23/)
- [记一道比较复杂的USB流量分析题](http://www.ga1axy.top/index.php/archives/10/)
- [【技术分享】从CTF中学USB流量捕获与解析](https://www.anquanke.com/post/id/85218)
- [USB流量分析](https://ares-x.com/2017/11/20/USB%E6%B5%81%E9%87%8F%E5%88%86%E6%9E%90/)
- [CTF流量分析常见题型(二)-USB流量](https://blog.csdn.net/qq_43625917/article/details/107723635)
- [CTF MISC-USB流量分析出题记录](https://www.cnblogs.com/hackxf/p/10670844.html)

---

## USB流量

USB 使用的三种方式
- USB UART : 这种方式下，设备只是简单的将 USB 用于接受和发射数据，除此之外就再没有, 其他通讯功能了。
- USB HID : 这一类通讯适用于交互式，有这种功能的设备有：键盘，鼠标，游戏手柄和数字显示设备。
- USB Memory : 数据存储

USB 协议版本有 USB1.0, USB1.1, USB2.0, USB3.1 等, 目前 USB2.0 比较常用。

每一个 USB 设备（尤其是 HID 或者 Memory ）都有一个供应商 ID（Vendor ID） 和产品识别码（Product Id） 。 Vendor ID 是用来标记哪个厂商生产了这个 USB 设备。 Product ID 则用来标记不同的产品.

> lsusb 命令用于显示本机的USB设备列表，以及USB设备的详细信息。

![](../../../../assets/img/Security/BlueTeam/笔记/USB取证/2.png)

- Bus 002: 指明设备连接到哪条总线
- Device 002: 表明这是连接到总线上的第二台设备
- ID : 设备的 ID
- VMware, Inc. Virtual Mouse: 生产商名字和设备名

USB 流量的捕获可以使用 wireshark 或 usbpcap 来进行，在 ctf 中通常会给出已经捕获好的流量包，而我们需要做的便是从流量包中还原捕获的数据。

用 wireshark 打开流量包, USB 协议的数据部分在 Leftover Capture Data 块中

![](../../../../assets/img/Security/BlueTeam/笔记/USB取证/1.png)

在蓝色部分可以看到这个区域，右键→应用为列，即可在上面显示出来这一列

键盘流量的数据长度为 8 个字节, 鼠标流量的数据长度为 4 个字节

---

### 键盘流量

键盘数据包的数据长度为 8 个字节，击键信息集中在第 3 个字节，每次击键都会产生一个数据包。所以如果看到给出的数据包中的信息都是 8 个字节，并且只有第 3 个字节不为 0000，那么几乎可以肯定是一个键盘流量了。

- 字节下标
    - 0 : 修改键(组合键)
    - 1 : OEM 保留
    - 2~7 : 按键码

- BYTE1
    - bit0:   Left Control      是否按下，按下为 1
    - bit1:   Left Shift        是否按下，按下为 1
    - bit2:   Left Alt          是否按下，按下为 1
    - bit3:   Left WIN/GUI      是否按下，按下为 1
    - bit4:   Right Control     是否按下，按下为 1
    - bit5:   Right Shift       是否按下，按下为 1
    - bit6:   Right Alt         是否按下，按下为 1
    - bit7:   Right WIN/GUI     是否按下，按下为 1
- BYTE2 - 暂不清楚，有的地方说是保留位
- BYTE3-BYTE8 - 这六个为普通按键

例如： 键盘发送 02 00 0e 00 00 00 00 00，表示同时按下了 Left Shift + 'k'，即大写 K。

具体键位对应 [Universal Serial Bus HID Usage Tables - USB-IF](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf) 53页~59页

> 还原 tshark 提取数据到键盘映射的脚本
```py
mappings = { 0x04:"A",  0x05:"B",  0x06:"C", 0x07:"D", 0x08:"E", 0x09:"F", 0x0A:"G",  0x0B:"H", 0x0C:"I",  0x0D:"J", 0x0E:"K", 0x0F:"L", 0x10:"M", 0x11:"N",0x12:"O",  0x13:"P", 0x14:"Q", 0x15:"R", 0x16:"S", 0x17:"T", 0x18:"U",0x19:"V", 0x1A:"W", 0x1B:"X", 0x1C:"Y", 0x1D:"Z", 0x1E:"1", 0x1F:"2", 0x20:"3", 0x21:"4", 0x22:"5",  0x23:"6", 0x24:"7", 0x25:"8", 0x26:"9", 0x27:"0", 0x28:"n", 0x2a:"[DEL]",  0X2B:"    ", 0x2C:" ",  0x2D:"-", 0x2E:"=", 0x2F:"[",  0x30:"]",  0x31:"\\", 0x32:"~", 0x33:";",  0x34:"'", 0x36:",",  0x37:"." }
nums = []
keys = open('out.txt')
for line in keys:
    if line[0]!='0' or line[1]!='0' or line[3]!='0' or line[4]!='0' or line[9]!='0' or line[10]!='0' or line[12]!='0' or line[13]!='0' or line[15]!='0' or line[16]!='0' or line[18]!='0' or line[19]!='0' or line[21]!='0' or line[22]!='0':
         continue
    nums.append(int(line[6:8],16))
    # 00:00:xx:....

keys.close()
output = ""
for n in nums:
    if n == 0 :
        continue
    if n in mappings:
        output += mappings[n]
    else:
        output += '[unknown]'
print('output :n' + output)
```

**相关工具**
- [WangYihang/UsbKeyboardDataHacker](https://github.com/WangYihang/UsbKeyboardDataHacker) - USB键盘流量包取证工具 , 用于恢复用户的击键信息

---

### 鼠标流量

鼠标移动时表现为连续性,与键盘击键的离散性不一样,不过实际上鼠标动作所产生的数据包也是离散的

鼠标数据包的数据长度为4个字节
- 第一个字节代表按键，当取 `0x00` 时，代表没有按键、为 `0x01` 时，代表按左键，为 `0x02` 时，代表当前按键为右键。
- 第二个字节可以看成是一个 signed byte 类型，其最高位为符号位，当这个值为正（小于127）时，代表鼠标水平右移多少像素，为负（补码负数，大于127小于255）时，代表水平左移多少像素。
- 第三个字节与第二字节类似，代表垂直上下移动的偏移。
- 第四个是扩展字节
    - 0 - 没有滚轮运动
    - 1 - 垂直向上滚动一下
    - 0xFF - 垂直向下滚动一下
    - 2 - 水平滚动右键一下
    - 0xFE - 水平滚动左键单击一下

例如： 鼠标发送 00 01 fc 00，表示鼠标右移 01 像素，垂直向下移动 124 像素.

> 还原 tshark 提取数据到鼠标偏移的脚本
```py
nums = []
keys = open('out.txt','r')
f = open('xy.txt','w')
posx = 0
posy = 0
for line in keys:
    if len(line) != 12 :
        continue
    x = int(line[3:5],16)
    y = int(line[6:8],16)
    if x > 127 :
        x -= 256
    if y > 127 :
        y -= 256
    posx += x
    posy += y
    btn_flag = int(line[0:2],16)  # 1 for left , 2 for right , 0 for nothing
    if btn_flag == 1 : # 1 代表左键
        f.write(str(posx))
        f.write(' ')
        f.write(str(posy))
        f.write('\n')

f.close()
```

配合 gnuplot 将坐标轴转换为图像
- [gnuplot学习笔记](../../../Develop/可视化/gnuplot/gnuplot学习笔记.md#读取文件) 读取文件部分

**相关工具**
- [WangYihang/UsbMiceDataHacker](https://github.com/WangYihang/UsbMiceDataHacker) - USB鼠标流量包取证工具 , 主要用于绘制鼠标移动以及拖动轨迹
