# VM-Plan

<p align="center">
    <a href="https://twitter.com/mittye97/status/1237293281202978817"><img src="../../assets/img/banner/VM-Plan.jpg" width="90%"></a>
</p>

---

## VMware

**Linux 虚拟机建议**
- 适用于 : 实验
  - [Centos](https://www.centos.org/)
- 适用于 : 渗透
  - [Kali](https://www.kali.org/)

**Windows 虚拟机建议**
- 适用于 : 渗透/靶机
  - [commando-vm](https://github.com/fireeye/commando-vm) - fireeye 出品的部署 Windows 的渗透测试虚拟机脚本
  - win2008
- 适用于 : 日常使用
  - 版本: Win10 2019 Ltsc
  - 版本: Win7

### VMware 常见问题

**关闭虚拟内存**

使用 VMWare 虚拟机,虚拟机启动后,会在虚拟机目录下建立一个与虚拟内存大小相同的 .vmem 文件,这个文件主要是将虚拟机内存的内容映射到磁盘,以支持在虚拟机的暂停等功能

- **对特定的虚拟机"禁用" vmem 文件**

  修改特定虚拟机目录下的 vmx 文件,在其中加上一行:
  `mainMem.useNamedFile = "FALSE"`

**VMTools**

如果没有装,一定要装.如果装不了,可以尝试这个方案 [open-vm-tools](https://github.com/vmware/open-vm-tools)
```bash
apt update
apt install open-vm-tools-desktop fuse
reboot  # 重启一下
```

**Centos 共享文件夹**

1. 需要 vm tool
2. 不能用 mount 工具挂载,而是得用 vmhgfs-fuse,需要安装工具包

```bash
yum install open-vm-tools-devel -y
有的源的名字并不一定为 open-vm-tools-devel(centos) ,而是 open-vm-dkms(unbuntu)
执行:vmhgfs-fuse .host:/ /mnt/hgfs
```

**常见报错**
- **该虚拟机似乎正在使用中.如果该虚拟机未在使用,请按"获取所有权(T)**

  将虚拟机路径下后缀为 .lck 的文件夹删除

- **无法将 Ethernet0 连接到虚拟网络"VMnet0"**

  在 vmware"编辑->虚拟网络设置"里面,点"恢复默认"可解决.

- **无法获得 VMCI 驱动程序的版本: 句柄无效.驱动程序"vmci.sys"的版本不正确.....**

  找到虚拟机路径下对应的 .vmx 文件,用编辑器打开,找到 `vmci0.present = "TRUE"`一项,将该项修改为:`vmci0.present = "FALSE"`

- **安装vmware-tools出现”what is the location of the “ifconfig”program on your machine?”**

  出现此问题的错误是因为网络问题,连通网络,安装 ifconfig 即可