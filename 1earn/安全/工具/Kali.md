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

# 安装

**更新系统**
```bash
sudo tee /etc/apt/sources.list <<-'EOF'
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
EOF

apt update && apt -y full-upgrade
[ -f /var/run/reboot-required ] && reboot -f
```

**常用工具**
```bash
apt install lrzsz
apt install owasp-mantra-ff     # owasp 的集成浏览器
apt install parallel
```

## vmtools

```bash
tar zxvf vmtools.tar.gz -C /root
cd /root/wmtools/
./vmware-install.pl
```

---

## virtualbox additions

```bash
mkdir /media/VBox
ls /media/VBox/
mount /dev/sr0 /media/VBox/
cd /media/VBox/
ls
sh VBoxLinuxAdditions.run
```

---

## powershell

```bash
apt install powershell
pwsh            # 启动
$PSVersionTable # 测试一下
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

## ncat

```bash
apt install ncat
update-alternatives --config nc
1
```

---

## pip

```bash
wget https://bootstrap.pypa.io/get-pip.py	# 安装 pip3
python3 get-pip.py

pip install pyinstaller
```

**pip 指定版本安装**

检查一遍 pip 和 pip3 分别指向的 Python
```bash
pip -V
pip3 -V
```

在 linux 安装了多版本 python 时(例如 python2.6 和 2.7),pip 安装的包不一定是用户想要的位置,此时可以用 -t 选项来指定位置
```bash
pip install -t /usr/local/lib/python2.7/site-packages/ docker
```

---

## proxychains-ng

```bash
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure
make && make install
cp ./src/proxychains.conf /etc/proxychains.conf
cd .. && rm -rf proxychains-ng
```
```bash
vim /etc/proxychains.conf

socks5 127.0.0.1 1080   # 改成你懂的
```
在需要代理的命令前加上 proxychains4 ,如 : `proxychains4 wget https://www.google.com/`

---

## SSH

安装完毕后会自动启动,但是没有配置配置文件会无法登陆,修改下配置文件
```vim
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```
```bash
systemctl start ssh     # 启动 ssh
systemctl enable ssh    # 设置为开机自启

# 或

/etc/init.d/ssh start   # 启动 ssh
update-rc.d ssh enable  # 设置为开机自启
```
若在使用工具登录时,当输完用户名密码后提示 SSH 服务器拒绝了密码,就再试一遍.

这时不要着急,只需要在 Kali 控制端口重新生成两个秘钥即可.
```bash
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
ssh-keygen -t dsa -f /etc/ssh/ssh_host_rsa_key
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

# 配置与设置
## apt

```bash
# 配置源
vim /etc/apt/sources.list

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

# 东软大学
deb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
deb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
```
```bash
# 更新源:
apt-get update

# 对软件进行一次整体更新:
apt-get update & apt-get upgrade
apt-get dist-upgrade
apt-get clean

# 遇到报错 无法获得锁 /var/lib/apt/lists/lock - open (11: 资源暂时不可用)
rm -rf /var/cache/apt/archives/lock
rm -rf /var/lib/dpkg/lock-frontend
rm -rf /var/lib/dpkg/lock	# 强制解锁占用
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
apt install ttf-wqy-microhei
reboot
```

**修改时区**
```bash
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

---

## 网卡

**配置网卡**

- WM Ware(开机后)

    虚拟机->可移动设备->Ralink 802.11 n Wlan(显卡型号)->连接(断开与主机的连接)

- VBox

    虚拟机关机状态下->将设备插入主机->设置->USB设备->添加->删除除了供应商标识(VendorID)和产品标识(ProductID)之外的参数->开机->插入设备

- 验证是否连接成功

    ```bash
    lsusb
    airmon-ng
    iwconfig
    ```
    出现无线网卡型号即为成功

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
direct rendering: Yes   # 出现yes安装成功
```

检测原本的 Oclhashcat-plus 是否运行正常:
```bash
cd /usr/share/oclhashcat-plus/
./cudaHashcat-plus.bin -t 32 -a 7 example0.hash ?a?a?a?a example.dict
```
