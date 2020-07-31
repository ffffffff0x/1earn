# siemens 仿真搭建实验

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**实验环境**

`环境仅供参考`

- [服务器] Microsoft Windows 7 专业版 6.1.7601 Service Pack 1 Build 7601(已激活)(安装 DotNetFramework_4.0)
- [客户机] Microsoft Windows 10 企业版 LTSC - 10.0.17763
- VMware® Workstation 15 Pro - 15.0.0 build-10134415

---

服务器下载软件
- STEP7
    - http://www.laozhoucontrol.com/S7-PLCSIM-V5_4-SP5-UPD1.html
    - http://www.laozhoucontrol.com/STEP7-V5_5-CN-SP2-install.html
- plcsim
    - http://www.laozhoucontrol.com/S7-PLCSIM-V5_4-SP5-UPD1.html
- [NetToPLCSim](https://sourceforge.net/projects/nettoplcsim/)

**STEP7**

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/9.png)

先安装 STEP7

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/1.png)

打开,要求你先重启计算机

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/2.png)

重启,再次打开,注意,右键-以管理员权限运行,然后一路下一步

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/3.png)

许可证这里选择,否,以后再传送许可证密钥,下面一路下一步

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/4.png)

这里由于没有以管理员权限运行,所以运行到安装 step7 时报错,然后我以管理员权限运行重新打开了一次

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/5.png)

等到所有组件安装完毕后,这里需要手动中止安装.

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/6.png)

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/7.png)

然后在这个界面,我等了10分钟都没有反应,就直接资源管理器杀掉安装进程了,后续使用时没有发现有任何影响.

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/8.png)

安装完毕后,记得用 Simatic_EKB_Install_2013_03_01_test 激活,短密钥或长密钥随便安装一个

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/10.png)

接下来继续安装 plcsim

**plcsim**

安装 plcsim

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/11.png)

打开,要求你先重启计算机

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/12.png)

重启,再次打开,注意,右键-以管理员权限运行,然后一路下一步,等待安装完毕

**服务器使用 plcsim**

打开 SIMATIC Manager 软件，新建项目 test2

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/13.png)

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/14.png)

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/15.png)

在新建项目 test2 点击插入新对象，并选择 SIMATIC 300 站点

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/16.png)

选择 SIMATIC300（1）打开对象

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/17.png)

在 HW Config 界面下选择 SIMATIC 300,并选择 RACK-300 下的 Rail

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/18.png)

UR(0)对话框中的序号槽1中右键

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/19.png)

插入对象PS 307 2A

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/20.png)

在序号槽2中点击右键插入对象 CPU 314C-2PN/DP V3.3

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/21.png)

新建子网设置 ip 地址为本机的 IP 地址

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/22.png)

启动 S7-PLCSIM

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/23.png)

进入 S7-PLCSIM 界面，选择 PLCSIM(TCP/IP)

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/24.png)

回到 HW Config 对话框，选择下载到模块

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/25.png)

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/26.png)

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/27.png)

待下载完成，PLCSIM 会显示 PLC 的地址为之前设置的 IP 地址

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/28.png)

然后下载 NetToPLCSim,解压,打开 NetToPLCSim.exe

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/29.png)

点击 add,弹出 station 对话框，在 Network IP Address 及 Plcsim IP Address 中选择 IP 地址为之前设置的 ip 地址

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/30.png)

点击 Start Server，PLC#001 进入运行状态

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/31.png)

回到 S7-PLCSIM ,勾选 RUN

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/32.png)

**客户机连接**

在客户机中打开 Snap7 Client Demo 工具，填写仿真 PLC 的 IP 地址如：192.168.141.131，点击 Connect

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/33.png)

如果这里连接失败,应该是因为服务器防火墙开着,关闭防火墙即可

再在 control 下点击 stop 按钮即停止 PLC 的命令

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/34.png)

查看靶机中仿真 PLC 的状态从 run 变为 stop

![](../../../../assets/img/安全/实验/ICS/siemens仿真搭建实验/35.png)

---

**Source & Reference**
- [西门子PLC的网络仿真搭建方法探讨](https://www.freebuf.com/articles/ics-articles/236250.html)
