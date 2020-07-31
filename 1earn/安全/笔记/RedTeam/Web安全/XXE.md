# XXE

`xml 外部实体注入漏洞`

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [XXE 漏洞的学习与利用总结](https://www.cnblogs.com/r00tuser/p/7255939.html)
- [XXE 漏洞利用技巧:从 XML 到远程代码执行](https://www.freebuf.com/articles/web/177979.html)
- [XXE: XML eXternal Entity Injection vulnerabilities](https://www.gracefulsecurity.com/xml-external-entity-injection-xxe-vulnerabilities/)
- [浅谈 XXE 攻击](https://www.freebuf.com/articles/web/126788.html)

**相关案例**
- [XXE at ecjobs.starbucks.com.cn/retail/hxpublic_v6/hxdynamicpage6.aspx](https://hackerone.com/reports/500515)

**靶场**
- [c0ny1/xxe-lab: 一个包含 php,java,python,C# 等各种语言版本的 XXE 漏洞 Demo](https://github.com/c0ny1/xxe-lab)
- [TheTwitchy/vulnd_xxe](https://github.com/TheTwitchy/vulnd_xxe)

**payload**
- [bugbounty-cheatsheet/cheatsheets/xxe.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/xxe.md)

---

**概括**

XXE 就是 XML 外部实体注入。当允许引用外部实体时，通过构造恶意内容，就可能导致任意文件读取、系统命令执行、内网端口探测、攻击内网网站等危害。

**XML 基础知识**
- [XML笔记](../../../../开发/标记语言/XML/XML.md)
