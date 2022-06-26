# vCenter

---

## 环境搭建

访问 https://customerconnect.vmware.com/patch 下载 iso

下载 VMware-VCSA-all-6.7.0-17028579.iso

![](../../../assets/img/Integrated/虚拟化/vCenter/1.png)

提取里面这个 ova 文件

![](../../../assets/img/Integrated/虚拟化/vCenter/2.png)

导入到 VMware 虚拟机安装，部署选项选择 Tiny 即可：

![](../../../assets/img/Integrated/虚拟化/vCenter/3.png)

然后按照引导安装，网络配置参考宿主机，设置成相同的网段、相同的网关和 DNS，以便后续顺利访问。

> 首先确认好自己的虚拟机桥接的网卡是哪张，以及桥接的网段 ip 是啥

我这边宿主机 IP 为 192.168.8.130，网关和 DNS 均为 192.168.8.1，子网掩码为 255.255.255.0，那虚拟机设置如下

![](../../../assets/img/Integrated/虚拟化/vCenter/4.png)

然后配置 sso 密码，和 root 密码，这里为了方便,就配置成 Abcd1234 了.

配置完后，点击导入，进行初始化,稍作等待,即可看到如下的界面

![](../../../assets/img/Integrated/虚拟化/vCenter/5.png)

此时域名为 photon-machine，没有对应的 DNS，需要手动修改域名为刚才设置的 IP（192.168.8.250）

按“F2”手动修改域名，“enter”进入网络配置：

![](../../../assets/img/Integrated/虚拟化/vCenter/6.png)

进入 DNS 配置将主机名从默认的 photon-machine 修改为 IP 地址（192.168.8.250）：

![](../../../assets/img/Integrated/虚拟化/vCenter/7.png)

保存，等它自动重启网络

回到开始的页面，这时之前的域名已经变成了 IP：

![](../../../assets/img/Integrated/虚拟化/vCenter/8.png)

接下来访问 https://192.168.8.250:5480/ 继续配置：

![](../../../assets/img/Integrated/虚拟化/vCenter/9.png)

选择设置后用 root 账号登陆, 按照向导继续配置，注意在网络配置阶段把系统名称修改为 IP：

![](../../../assets/img/Integrated/虚拟化/vCenter/10.png)

然后设置 SSO 密码，一路下一步

![](../../../assets/img/Integrated/虚拟化/vCenter/11.png)

安装完成会打开 443 端口，此时就可以正常访问 vCenter 了

![](../../../assets/img/Integrated/虚拟化/vCenter/12.png)

![](../../../assets/img/Integrated/虚拟化/vCenter/13.png)

---

## 开启 SSH

vcenter 的 ssh 要在后台配置才能访问

登录 5480 端口上的 vCenter VAMI 登录页面,点击 Access -- Edit.

开启 SSH Login 选项就行了

![](../../../assets/img/Integrated/虚拟化/vCenter/14.png)

---

## Source & Reference
- [VMware vCenter RCE 漏洞踩坑实录——一个简单的RCE漏洞到底能挖出什么知识](https://mp.weixin.qq.com/s/eamNsLY0uKHXtUw_fiUYxQ)
- https://blog.ukotic.net/2020/08/06/enable-ssh-on-vcenter-server-7/
- https://mp.weixin.qq.com/s/kPoYhbCPZb62t71-jbO1dA
