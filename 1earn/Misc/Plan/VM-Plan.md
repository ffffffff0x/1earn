# VM-Plan

<p align="center">
    <a href="https://www.flickr.com/photos/sofi01/4667759854"><img src="../../../assets/img/Misc/VM-Plan.jpg" width="70%"></a>
</p>

---

## VMware

**Linux 虚拟机建议**
- [Centos](https://www.centos.org/)
- [Kali-xfce](https://www.kali.org/)
- [Manjaro-kde](https://manjaro.org)
- [Parrot-kde](https://www.parrotsec.org/)

**Windows 虚拟机建议**
- 渗透/靶机-[commando-vm](https://github.com/fireeye/commando-vm)
- 日用-Win10 2019 Ltsc

**关闭虚拟内存**

使用 VMWare 虚拟机，虚拟机启动后，会在虚拟机目录下建立一个与虚拟内存大小相同的 .vmem 文件,这个文件主要是将虚拟机内存的内容映射到磁盘，以支持在虚拟机的暂停等功能

- **对特定的虚拟机"禁用" vmem 文件**

  修改特定虚拟机目录下的 vmx 文件，在其中加上一行：
  `mainMem.useNamedFile = "FALSE"`

**VMTools**

如果没有装，一定要装.如果装不了，可以尝试这个方案 [open-vm-tools](https://github.com/vmware/open-vm-tools)

**Centos 共享文件夹**

1. 需要 vm tool
2. 不能用 mount 工具挂载，而是得用 vmhgfs-fuse，需要安装工具包

```bash
yum install open-vm-tools-devel -y
有的源的名字并不一定为 open-vm-tools-devel(centos) ，而是 open-vm-dkms(unbuntu)
执行：vmhgfs-fuse .host:/ /mnt/hgfs
```

**常见报错**
- **该虚拟机似乎正在使用中。如果该虚拟机未在使用，请按“获取所有权(T)**

    将虚拟机路径下后缀为 .lck 的文件夹删除

- **无法将 Ethernet0 连接到虚拟网络"VMnet0"**

    在 vmware“编辑->虚拟网络设置”里面，点“恢复默认”可解决。

- **无法获得 VMCI 驱动程序的版本: 句柄无效。驱动程序“vmci.sys”的版本不正确.....**

    找到虚拟机路径下对应的 .vmx 文件，用编辑器打开，找到 `vmci0.present = “TRUE”`一项,将该项修改为：`vmci0.present = “FALSE”`

---

## Linux 虚拟机定制建议

1.预装软件(持续更新)
```bash
bzip2
vim
python2
python3
make
gcc
gcc-c++
curl
git
SSH
lrzsz
proxychains

Centos
  "Development Tools"
```

2.桌面需求
```bash
设定屏幕超时时间永不超时
换个不辣眼睛的壁纸(然并卵,反正日常在 ssh 下使用)
默认终端 fish 或 on my zsh
终端配置 powerline-shell
```

3.网络设置
```bash
dns:208.67.222.222 114.114.114.114
软件包换源:aliyun 源或 163、tuna 源
pip 换源
docker 换源
终端看情况走代理，预先配置好 proxychains
```

4.硬件设施
```bash
CPU:1-2核
mem:1-2-4G
disk:40G
```

---

## Windows 定制建议

1.预装软件
```bash
Dism+
7zip
notepad++
geek
chrome

日用
  微信
  TIM
  钉钉
  360杀毒(虚拟机运行,用来测免杀)
  360浏览器(为了兼容部分 IE、flash 网页，尼玛的弹广告是真的烦)

渗透/靶机
  python
  java
  CTF工具
    ctftools
  各类扫描工具(exe/python/go)
  burp
    常见插件
    JPython(为了运行插件)
    JRuby(同上)
  phpstudy(为了方便搭建环境)
  dvwa
  pikachu
  xxe-lab
```

2.桌面需求
```bash
屏幕超时时间永不超时
换个不辣眼睛的壁纸
```

3.网络设置
```bash
dns:208.67.222.222 114.114.114.114
```

4.硬件设施
```bash
CPU:1-2-4核
mem:2-4-8G
disk:60G
```

5.功能要求
```bash
开启 RDP
开启 ssh，telnet 功能(客户端、服务端)

更新到最新版本，打好补丁
记得激活(笑
```

## Reference

- [VMWare 禁用vmem虚拟内存文件](https://www.cnblogs.com/guyk/p/9747764.html)
- [vmware/open-vm-tools](https://github.com/vmware/open-vm-tools)
- [怎么解决VMware“该虚拟机似乎正在使用中”问题_百度经验](https://jingyan.baidu.com/article/4ae03de3fa2ae93eff9e6bb0.html)
- [无法将 Ethernet0 连接到虚拟网络"VMnet0" 详细信息可以在 vmware.log](https://blog.csdn.net/qq_26479655/article/details/51794520)
- [关于VMware问题：无法获得 VMCI 驱动程序的版本: 句柄无效。驱动程序“vmci.sys”的版本不正确......](https://blog.csdn.net/mononoke111/article/details/79010700)
- [未通过ovf规范一致性或虚拟硬件合规性检查](https://blog.51cto.com/joket/1790244)
- [Vmware10 Centos7 共享文件夹设置方法](https://www.cnblogs.com/zejin2008/p/7144514.html)