# JSON 学习笔记

---

**在线 JSON 格式化**
- https://www.json.cn/
- http://www.bejson.com/
- https://github.com/jsonhero-io/jsonhero-web
    - https://jsonhero.io/

**JSONPath 在线查询工具**
- http://jsonpath.com/

**文章**
- [WORKING WITH DATA IN JSON FORMAT](https://www.trustedsec.com/blog/working-with-data-in-json-format/)

---

**什么是 JSON ？**

JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）,一种轻量级的文本数据交换格式,是存储和交换文本信息的语法。类似 XML。

JSON 独立于语言：JSON 使用 Javascript语法来描述数据对象，但是 JSON 仍然独立于语言和平台。JSON 解析器和JSON 库支持许多不同的编程语言。 目前非常多的动态（PHP，JSP，.NET）编程语言都支持JSON。

JSON 具有自我描述性，更易理解,比 XML 更小、更快，更易解析。
```json
{
    "sites": [
    { "name":"test" , "url":"www.test.com" },
    { "name":"google" , "url":"www.google.com" },
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}
```
这个 sites 对象是包含 3 个站点记录（对象）的数组。

JSON 文本格式在语法上与创建 JavaScript 对象的代码相同。

由于这种相似性，无需解析器，JavaScript 程序能够使用内建的 `eval()` 函数，用 JSON 数据来生成原生的 JavaScript 对象。

JSON 文件的文件类型是 ".json"

JSON 文本的 MIME 类型是 "application/json"

**与 XML 对比**

- **与 XML 相同之处**
    - JSON 是纯文本
    - JSON 具有"自我描述性"（人类可读）
    - JSON 具有层级结构（值中存在值）
    - JSON 可通过 JavaScript 进行解析
    - JSON 数据可使用 AJAX 进行传输

- **与 XML 不同之处**
    - 没有结束标签
    - 更短
    - 读写的速度更快
    - XML 需要使用 XML 解析器来解析，JSON 可以使用标准的 JavaScript 函数来解析。
    - 使用数组
    - 不使用保留字

---

## 语法

JSON 语法是 JavaScript 语法的子集。
- 数据在名称/值对中
- 数据由逗号分隔
- 大括号保存对象
- 中括号保存数组

**JSON 名称/值对**

JSON 数据的书写格式是：名称/值对。

名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：
```json
"name" : "test"
```

这很容易理解，等价于这条 JavaScript 语句：
```js
name = "test"
```

**JSON 值**

JSON 值可以是：
- 数字（整数或浮点数）
- 字符串（在双引号中）
- 逻辑值（true 或 false）
- 数组（在中括号中）
- 对象（在大括号中）
- null

**JSON 数字**

JSON 数字可以是整型或者浮点型：
```json
{ "age":30 }
```

**JSON 对象**

JSON 对象在大括号 `{}` 中书写：

对象可以包含多个名称/值对：
```json
{ "name":"test" , "url":"www.test.com" }
```

这一点也容易理解，与这条 JavaScript 语句等价：
```js
name = "test"
url = "www.test.com"
```

**JSON 数组**

JSON 数组在中括号中书写：

数组可包含多个对象：
```json
{
"sites": [
{ "name":"test" , "url":"www.test.com" },
{ "name":"google" , "url":"www.google.com" },
{ "name":"微博" , "url":"www.weibo.com" }
]
}
```

在上面的例子中，对象 "sites" 是包含三个对象的数组。每个对象代表一条关于某个网站（name、url）的记录。

**JSON 布尔值**

JSON 布尔值可以是 true 或者 false：
```json
{ "flag":true }
```

**JSON null**

JSON 可以设置 null 值：
```json
{ "test":null }
```

**JSON 使用 JavaScript 语法**

因为 JSON 使用 JavaScript 语法，所以无需额外的软件就能处理 JavaScript 中的 JSON。

通过 JavaScript，你可以创建一个对象数组，并像这样进行赋值：
```js
var sites = [
    { "name":"test" , "url":"www.test.com" },
    { "name":"google" , "url":"www.google.com" },
    { "name":"微博" , "url":"www.weibo.com" }
];
```

可以像这样访问 JavaScript 对象数组中的第一项（索引从 0 开始）：
```js
sites[0].name;
```

返回的内容是：
```
test
```

可以像这样修改数据：
```js
sites[0].name="test";
```

---

## 对象

**对象语法**
```json
{ "name":"test", "alexa":10000, "site":null }
```

JSON 对象使用在大括号 `{}` 中书写。

对象可以包含多个 key/value（键/值）对。

key 必须是字符串，value 可以是合法的 JSON 数据类型（字符串, 数字, 对象, 数组, 布尔值或 null）。

key 和 value 中使用冒号 `:` 分割。

每个 key/value 对使用逗号 `,` 分割。

**访问对象值**

你可以使用点号 `.` 来访问对象的值：
```html
<p id="demo"></p>

<script>

var myObj, x;
myObj = { "name":"test", "alexa":10000, "site":null };
x = myObj.name;
document.getElementById("demo").innerHTML = x;

</script>
```

你也可以使用中括号 `[]` 来访问对象的值：
```js
var myObj, x;
myObj = { "name":"test", "alexa":10000, "site":null };
x = myObj["name"];
```

**循环对象**

你可以使用 for-in 来循环对象的属性：
```html
<p id="demo"></p>

<script>
var myObj = { "name":"test", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += x + "<br>";
}
</script>
```

在 for-in 循环对象的属性时，使用中括号 `[]` 来访问属性的值：
```js
var myObj = { "name":"test", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += myObj[x] + "<br>";
}
```

**嵌套 JSON 对象**

JSON 对象中可以包含另外一个 JSON 对象：
```json
myObj = {
    "name":"test",
    "alexa":10000,
    "sites": {
        "site1":"www.test.com",
        "site2":"m.test.com",
        "site3":"c.test.com"
    }
}
```

你可以使用点号 `.` 或者中括号 `[]` 来访问嵌套的 JSON 对象。
```html
<p id="demo"></p>

<script>
myObj = {
	"name":"test",
	"alexa":10000,
	"sites": {
		"site1":"www.test.com",
		"site2":"m.test.com",
		"site3":"c.test.com"
	}
}
document.getElementById("demo").innerHTML += myObj.sites.site1 + "<br>";
// 或者
document.getElementById("demo").innerHTML += myObj.sites["site1"];
</script>
```

**修改值**

你可以使用点号 `.` 来修改 JSON 对象的值：
```html
<p id="demo"></p>

<script>
var myObj, i, x = "";
myObj = {
    "name":"test",
    "alexa":10000,
    "sites": {
        "site1":"www.test.com",
        "site2":"m.test.com",
        "site3":"c.test.com"
    }
}
myObj.sites.site1 = "www.google.com";

for (i in myObj.sites) {
    x += myObj.sites[i] + "<br>";
}

document.getElementById("demo").innerHTML = x;

</script>
```

你可以使用中括号 `[]` 来修改 JSON 对象的值：
```js
myObj.sites["site1"] = "www.google.com";
```

**删除对象属性**

我们可以使用 delete 关键字来删除 JSON 对象的属性：
```html
<p id="demo"></p>

<script>
var myObj, i, x = "";
myObj = {
    "name":"test",
    "alexa":10000,
    "sites": {
        "site1":"www.test.com",
        "site2":"m.test.com",
        "site3":"c.test.com"
    }
}
delete myObj.sites.site1;

for (i in myObj.sites) {
    x += myObj.sites[i] + "<br>";
}

document.getElementById("demo").innerHTML = x;

</script>
```

你可以使用中括号 `[]` 来删除 JSON 对象的属性：
```js
delete myObj.sites["site1"]
```

## JSON.parse()

JSON 通常用于与服务端交换数据。

在接收服务器数据时一般是字符串。

我们可以使用 `JSON.parse()` 方法将数据转换为 JavaScript 对象。

```js
JSON.parse(text[, reviver])
```

- text:必需， 一个有效的 JSON 字符串。
- reviver: 可选，一个转换结果的函数， 将为对象的每个成员调用此函数。

**JSON 解析实例**

例如我们从服务器接收了以下数据：
```json
{
    "name":"test",
    "alexa":10000,
    "site":"www.test.com"
}
```

我们使用 `JSON.parse()` 方法处理以上数据，将其转换为 JavaScript 对象：
```js
var obj = JSON.parse('{ "name":"test", "alexa":10000, "site":"www.test.com" }');
```

解析完成后，我们就可以在网页上使用 JSON 数据了：
```js
<p id="demo"></p>

<script>
var obj = JSON.parse('{ "name":"test", "alexa":10000, "site":"www.test.com" }');
document.getElementById("demo").innerHTML = obj.name + "：" + obj.site;
</script>
```

**从服务端接收 JSON 数据**

我们可以使用 AJAX 从服务器请求 JSON 数据，并解析为 JavaScript 对象。
```html
<p id="demo"></p>

<script>

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myObj = JSON.parse(this.responseText);
        document.getElementById("demo").innerHTML = myObj.name;
    }
};
xmlhttp.open("GET", "/ajax/json_demo.txt", true);
xmlhttp.send();

</script>

<p>查看 JSON 文件数据 <a href="/ajax/json_demo.txt" target="_blank">json_demo.txt</a></p>
```

json_demo.txt
```json
{
    "name":"网站",
    "num":3,
    "sites": [
        { "name":"Google", "info":[ "Android", "Google 搜索", "Google 翻译" ] },
        { "name":"Taobao", "info":[ "淘宝", "网购" ] }
    ]
}
```

**从服务端接收数组的 JSON 数据**

如果从服务端接收的是数组的 JSON 数据，则 `JSON.parse` 会将其转换为 JavaScript 数组：
```html

<p id="demo"></p>

<script>

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myArr = JSON.parse(this.responseText);
        document.getElementById("demo").innerHTML = myArr[1];
    }
};
xmlhttp.open("GET", "/ajax/json_demo_array.txt", true);
xmlhttp.send();

</script>

<p>查看服务端数据 <a href="/ajax/json_demo_array.txt" target="_blank">json_demo_array.txt</a></p>
```

json_demo_array.txt
```json
[ "Google", "test", "Taobao" ]
```

**异常**

JSON 不能存储 Date 对象。

如果你需要存储 Date 对象，需要将其转换为字符串。

之后再将字符串转换为 Date 对象。
```html
<p id="demo"></p>

<script>

var text = '{ "name":"test", "initDate":"2013-12-14", "site":"www.test.com"}';
var obj = JSON.parse(text);
obj.initDate = new Date(obj.initDate);

document.getElementById("demo").innerHTML = obj.name + "创建日期: " + obj.initDate;

</script>
```

我们可以启用 `JSON.parse` 的第二个参数 reviver，一个转换结果的函数，对象的每个成员调用此函数。
```html
<p id="demo"></p>

<script>

var text = '{ "name":"test", "initDate":"2013-12-14", "site":"www.test.com"}';
var obj = JSON.parse(text, function (key, value) {
	if (key == "initDate") {
	    return new Date(value);
	} else {
	    return value;
}});

document.getElementById("demo").innerHTML = obj.name + "创建日期：" + obj.initDate;

</script>
```

**解析函数**

JSON 不允许包含函数，但你可以将函数作为字符串存储，之后再将字符串转换为函数。
```html
<p id="demo"></p>

<script>

var text = '{ "name":"test", "alexa":"function () {return 10000;}", "site":"www.test.com"}';
var obj = JSON.parse(text);
obj.alexa = eval("(" + obj.alexa + ")");

document.getElementById("demo").innerHTML = obj.name + " Alexa 排名：" + obj.alexa();

</script>
```

不建议在 JSON 中使用函数。

---

## JSON.stringify()

JSON 通常用于与服务端交换数据。

在向服务器发送数据时一般是字符串。

我们可以使用 `JSON.stringify()` 方法将 JavaScript 对象转换为字符串。
```js
JSON.stringify(value[, replacer[, space]])
```

参数说明：
- value : 必需， 要转换的 JavaScript 值（通常为对象或数组）。
- replacer : 可选。用于转换结果的函数或数组。

    如果 replacer 为函数，则 JSON.stringify 将调用该函数，并传入每个成员的键和值。使用返回值而不是原始值。如果此函数返回 undefined，则排除成员。根对象的键是一个空字符串：""。

    如果 replacer 是一个数组，则仅转换该数组中具有键值的成员。成员的转换顺序与键在数组中的顺序一样。当 value 参数也为数组时，将忽略 replacer 数组。
- space : 可选，文本添加缩进、空格和换行符，如果 space 是一个数字，则返回值文本在每个级别缩进指定数目的空格，如果 space 大于 10，则文本缩进 10 个空格。space 也可以使用非数字，如：\t。

**对象转换**

例如我们向服务器发送以下数据：
```js
var obj = { "name":"test", "alexa":10000, "site":"www.test.com"};
```

我们使用 `JSON.stringify()` 方法处理以上数据，将其转换为字符串：
```js
var myJSON = JSON.stringify(obj);
```
myJSON 为字符串。

我们可以将 myJSON 发送到服务器：
```html
<p id="demo"></p>

<script>

var obj = { "name":"test", "alexa":10000, "site":"www.test.com"};
var myJSON = JSON.stringify(obj);
document.getElementById("demo").innerHTML = myJSON;

</script>
```

**数组转换**

我们也可以将 JavaScript 数组转换为 JSON 字符串：
```js
var arr = [ "Google", "test", "Taobao", "Facebook" ];
var myJSON = JSON.stringify(arr);
```

myJSON 为字符串。

我们可以将 myJSON 发送到服务器：
```html
<p id="demo"></p>

<script>

var arr = [ "Google", "test", "Taobao", "Facebook" ];
var myJSON = JSON.stringify(arr);
document.getElementById("demo").innerHTML = myJSON;

</script>
```

**异常**

JSON 不能存储 Date 对象。

`JSON.stringify()` 会将所有日期转换为字符串。

```html
<p id="demo"></p>

<script>

var obj = { "name":"test", "initDate":new Date(), "site":"www.test.com"};
var myJSON = JSON.stringify(obj);
document.getElementById("demo").innerHTML = myJSON;

</script>
```

之后你可以再将字符串转换为 Date 对象。

**解析函数**

JSON 不允许包含函数，`JSON.stringify()` 会删除 JavaScript 对象的函数，包括 key 和 value。
```html
<p id="demo"></p>

<script>

var obj = { "name":"test", "alexa":function () {return 10000;}, "site":"www.test.com"};
var myJSON = JSON.stringify(obj);
document.getElementById("demo").innerHTML = myJSON;

</script>
```

我们可以在执行 `JSON.stringify()` 函数前将函数转换为字符串来避免以上问题的发生：
```html
<p id="demo"></p>

<script>

var obj = { "name":"test", "alexa":function () {return 10000;}, "site":"www.test.com"};
obj.alexa = obj.alexa.toString();
var myJSON = JSON.stringify(obj);
document.getElementById("demo").innerHTML = myJSON;

</script>
```

不建议在 JSON 中使用函数。

---

## JSON 使用

JSON 最常见的用法之一，是从 web 服务器上读取 JSON 数据（作为文件或作为 HttpRequest），将 JSON 数据转换为 JavaScript 对象，然后在网页中使用该数据。

**JSON 实例 - 来自字符串的对象**

创建包含 JSON 语法的 JavaScript 字符串：
```js
var txt = '{ "sites" : [' +
'{ "name":"test" , "url":"www.test.com" },' +
'{ "name":"google" , "url":"www.google.com" },' +
'{ "name":"微博" , "url":"www.weibo.com" } ]}';
```

由于 JSON 语法是 JavaScript 语法的子集，JavaScript 函数 `eval()` 可用于将 JSON 文本转换为 JavaScript 对象。

`eval()` 函数使用的是 JavaScript 编译器，可解析 JSON 文本，然后生成 JavaScript 对象。必须把文本包围在括号中，这样才能避免语法错误：
```js
var obj = eval ("(" + txt + ")");
```

在网页中使用 JavaScript 对象：
```html
<p>
网站名: <span id="name"></span><br>
网站地址: <span id="url"></span><br>
</p>

<script>
var txt = '{ "sites" : [' +
'{ "name":"test" , "url":"www.test.com" },' +
'{ "name":"google" , "url":"www.google.com" },' +
'{ "name":"微博" , "url":"www.weibo.com" } ]}';

var obj = eval ("(" + txt + ")");

document.getElementById("name").innerHTML=obj.sites[0].name
document.getElementById("url").innerHTML=obj.sites[0].url
</script>
```

**JSON 解析器**

`eval()` 函数可编译并执行任何 JavaScript 代码。这隐藏了一个潜在的安全问题。

使用 JSON 解析器将 JSON 转换为 JavaScript 对象是更安全的做法。JSON 解析器只能识别 JSON 文本，而不会编译脚本。

在浏览器中，这提供了原生的 JSON 支持，而且 JSON 解析器的速度更快。

较新的浏览器和最新的 ECMAScript (JavaScript) 标准中均包含了原生的对 JSON 的支持。

---

## jsonl

`jsonlines`

- https://jsonlines.org/examples/

---

## Source & Reference

- [JSON 教程](https://www.runoob.com/json/json-tutorial.html)
- [.jsonl，jsonlines比json格式更好用的文件格式](https://blog.csdn.net/ykf173/article/details/107351057)
