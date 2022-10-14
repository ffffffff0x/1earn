# xray

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/chaitin/xray

**官方文档**
- https://docs.xray.cool/

---

## 使用

**生成证书**
```
xray genca
```

**爬虫爬取**

```bash
xray webscan --basic-crawler http://testphp.vulnweb.com --html-output vuln.html
```

**被动扫描**

```bash
xray ws --listen 127.0.0.1:7777 --html-output proxy.html
```

---

## 漏洞扫描

**漏洞扫描**
```bash
xray ws -u http://testphp.vulnweb.com --html-output report.html
```

**批量poc**
```bash
xray ws -p /pentest/xray/pocs/\* --url-file target.txt --html-output report.html
```

**指定poc**
```bash
xray ws -p "./xxx.yml" -u http://example.com/?a=b
```

**shiro**
```bash
xray webscan --plugins shiro --url-file target.txt --html-output x.html
```

---

## 代理

**burp 转发给 xray**

xray 监听 127.0.0.1:7777

burp Upstream Proxy Servers 中配置 127.0.0.1 7777 即可转发

**转发给 burp 查看流量**

burp 监听 127.0.0.1:8080

config.yaml 中配置 proxy: "http://127.0.0.1:8080" ,在 burp 中查看流量即可
