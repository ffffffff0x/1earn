# Kali 笔记

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

# 安装
**更新**
```bash
cat </etc/apt/sources.list
deb http://http.kali.org/kali kali-rolling main non-free contrib
EOF

apt update && apt -y full-upgrade
[ -f /var/run/reboot-required ] && reboot -f
```

**常用工具**
```bash
apt install lrzsz
```

**安装Powershell**
```bash
apt update && apt -y install powershell
```

**安装谷歌输入法**
```bash
apt-get update && apt-get upgrade
apt-get install fcitx
apt-get install fcitx-googlepinyin
reboot

# 所有应用程序中选中 fcitx 输入法配置即可
```

**ncat 的安装和配置**
```bash
apt install ncat
update-alternatives --config nc
1
```

**proxychains**
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

socks5 127.0.0.1 1080 # 改成你懂的
```
在需要代理的命令前加上 proxychains4 ,如：`proxychains4 wget https://www.google.com/`

---

# 配置

**切换 undercover 模式**
```bash
Kali Undercover Mode
```

**换界面显示语言**
```bash
dpkg-reconfigure locales
# 空格是选择,Tab是切换,*是选中
# 选中en_US.UTF-8和zh_CN.UTF-8,确定后,将en_US.UTF-8选为默认,然后安装中文字体
```

**如果界面出现乱码,安装中文字体**
```bash
apt-get install xfonts-intl-chinese
apt-get install ttf-wqy-microhei
reboot
```

**修改时区**
```bash
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

**SSH**

安装完毕后会自动启动,但是没有配置配置文件会无法登陆,修改下配置文件
```vim
vim /etc/ssh/sshd_config

PasswordAuthentication yes
PermitRootLogin yes
```
```bash
service ssh restart # 启动ssh
systemctl enable ssh  # 设置为开机自启

# 或

/etc/init.d/ssh start # 启动ssh
update-rc.d ssh enable  # 设置为开机自启
```
若在使用工具登录时,当输完用户名密码后提示 SSH 服务器拒绝了密码,就再试一遍.

这时不要着急,只需要在 Kali 控制端口重新生成两个秘钥即可.
```bash
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
ssh-keygen -t dsa -f /etc/ssh/ssh_host_rsa_key
```
