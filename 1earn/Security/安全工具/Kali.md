# Kali

<p align="center">
    <img src="../../../assets/img/logo/kali.png" width="40%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**官网**
- https://www.kali.org/downloads/

**教程 & Reference**
- [Kali-learning-notes Wiki](https://github.com/Keybird0/Kali-learning-notes/wiki)
- [Kali Linux 渗透测试的艺术（中文版）](https://jobrest.gitbooks.io/kali-linux-cn/content/table_of_contents.html)
- [大学霸 Kali Linux 安全渗透教程](https://wizardforcel.gitbooks.io/daxueba-kali-linux-tutorial/content/)

---

# 基础配置

- [kali基础配置](https://github.com/ffffffff0x/AboutSecurity/blob/master/VPS/Kali.md)

---

# 配置与设置
## apt

**换源**
```bash
# apt 换源
sudo tee /etc/apt/sources.list <<-'EOF'

# 清华源
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free

# 官方源
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib

# 中科大
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

# 浙大
deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
EOF
apt update
```

**更新系统**
```bash
apt update && apt -y full-upgrade
[ -f /var/run/reboot-required ] && reboot -f
```

---

## 显示

**切换 undercover 模式**
```bash
Kali Undercover Mode
```

**换界面显示语言**
```bash
dpkg-reconfigure locales
# 空格是选择,Tab是切换,*是选中
# 选中 en_US.UTF-8 和 zh_CN.UTF-8,确定后,将 en_US.UTF-8 选为默认,然后安装中文字体
```

**如果界面出现乱码,安装中文字体**
```bash
apt install xfonts-intl-chinese
apt install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy
reboot
```

**修改时区**
```bash
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

**kali 2020 添加 root 用户终端颜色**
```bash
cd /home/kali       # 切换到 kali 用户下
cp .bashrc /root    # 将 kali 用户的 .bashrc 复制到 root 用户目录下
cd /root            # 回到 root 用户目录下
cat .bashrc         # 查看 .bashrc 文件是否被替换，若已替换则说明成功
source .bashrc      # 终端颜色替换成功
```

---

## 网卡

**配置网卡**

- WM Ware(开机后)

    虚拟机->可移动设备->Ralink 802.11 n Wlan(显卡型号)->连接(断开与主机的连接)

- VBox

    虚拟机关机状态下->将设备插入主机->设置->USB 设备->添加->删除除了供应商标识(VendorID)和产品标识(ProductID)之外的参数->开机->插入设备

- 验证是否连接成功

    ```bash
    lsusb
    airmon-ng
    iwconfig
    ```
    出现无线网卡型号即为成功

---

## ncat

```bash
apt install ncat
update-alternatives --config nc
1
```

---

## 谷歌输入法

```bash
apt-get update && apt-get upgrade
apt-get install fcitx
apt-get install fcitx-googlepinyin
reboot

# 所有应用程序中选中 fcitx 输入法配置即可
```

---

## 虚拟机驱动

### vmtools

```bash
tar zxvf vmtools.tar.gz -C /root
cd /root/wmtools/
./vmware-install.pl
```

### virtualbox additions

```bash
mkdir /media/VBox
ls /media/VBox/
mount /dev/sr0 /media/VBox/
cd /media/VBox/
ls
sh VBoxLinuxAdditions.run
```

---

## 英伟达显卡驱动(物理机)
### 官方教程

网址 : https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/

```bash
apt update && apt dist-upgrade -y && reboot
lspci -v
apt install -y ocl-icd-libopencl1 nvidia-driver nvidia-cuda-toolkit # 安装OpenCL ICD加载程序,驱动程序和CUDA工具包.
nvidia-smi          # 验证是否安装成功
hashcat -I          # 确保是否能和hashcat协同工作
hashcat -b          # Benchmarking
```

如若不成功,进行故障排除:
```bash
apt install -y clinfo
dpkg -l |grep -i icd
```

如果安装了 mesa-opencl-icd:
```bash
apt remove mesa-opencl-icd
clinfo | grep -i "icd loader"
nvidia-smi -i 0 -q  # 查看详细信息
```

确认3D渲染是否启用:
```bash
glxinfo | grep -i "direct rendering"
direct rendering: Yes   # 出现 yes 成功
```

### 第二种方法

```bash
apt-get update
apt-get dist-upgrade
apt-get install -y linux-headers-$(uname -r)
apt-get install nvidia-kernel-dkms
sed 's/quiet/quiet nouveau.modeset=0/g' -i /etc/default/grub
update-grub
reboot
```

检测是否安装成功:
```bash
glxinfo | grep -i "direct rendering"
direct rendering: Yes   # 出现 yes 安装成功
```

检测原本的 Oclhashcat-plus 是否运行正常:
```bash
cd /usr/share/oclhashcat-plus/
./cudaHashcat-plus.bin -t 32 -a 7 example0.hash ?a?a?a?a example.dict
```

---


## Nessus

以安装 sc 版本为例,访问 https://www.tenable.com/downloads/nessus 下载安装包

我这里下的是 Nessus-8.8.0-ubuntu1110_amd64.deb

```bash
dpkg -i Nessus-8.8.0-ubuntu1110_amd64.deb
```

安装完成后
```bash
/etc/init.d/nessusd start   # 开启
/etc/init.d/nessusd status  # 查看状态
/etc/init.d/nessusd stop    # 关闭
```

然后访问 https://127.0.0.1:8834 即可打开Nessus主页,一路配置安装版本,账号密码

如果下载插件出错,就安装离线包,访问 https://www.tenable.com/downloads/nessus 下载离线包

我这里下的是 nessus-updates-8.8.0.tar.gz,复制到目录 /opt/nessus/sbin/ 下
```bash
./nessuscli update nessus-updates-8.8.0.tar.gz
./nessusd   # 重新启动下
```

**docker 部署**

```bash
docker run -d -p 3443:3443 -p 8834:8834  --name bobohacker -it yakoazz/bobohacker
```
- nesss地址 : https://127.0.0.1:8443 账号密码 bobohacker/bobohacker
- awvs地址 : https://127.0.0.1:3443 账号密码 bobo@hacker.com/B0bohacker
- nessus 应用自启 awvs13 要 attach 到容器里面 root 目录下运行下 awvs.sh

---

## rdesktop

kali 自带
```bash
rdesktop <目标IP>
```

---

# 用户管理

**kali Linux 2020.1 添加 root 用户**

安装 Kali Linux 2020.1 系统后，由于 root 用户的默认密码未知，所以需要在单用户模式下重新设置 root 用户密码。操作步骤如下：
```
1.开机选择第一项 Kali GNU/Linux 按键盘 e 键进入 Grub
2.找到 Linux 行，将 ro 修改为 rw，并在末尾添加 init=/bin/bash
3.Ctrl+X 或 f10 重启进单用户
4.用 passwd 命令修改密码
5.关机重启。登陆 root 用户
```
