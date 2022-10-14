# PHP代码审计

---

**环境搭建**

推荐用 phpstudy 搭建 php 代码审计的环境，简单快捷，切换 php 版本也很方便，再配置好 Xdebug 在 PHPstorm 即可远程调试。
- 下载地址: https://www.xp.cn/download.html

相关文章
- [PHP代码审计_搭建及其环境配置](https://www.modb.pro/db/184384)

如果是云服务器,推荐使用 aapanel 部署 lnmp 环境,很方便

**相关工具**
- [LoRexxar/Kunlun-M](https://github.com/LoRexxar/Kunlun-M)
    ```bash
    git clone --depth 1 https://github.com/LoRexxar/Kunlun-M.git
    cd Kunlun-M
    pip3 install -r requirements.txt
    cp Kunlun_M/settings.py.bak Kunlun_M/settings.py    # 配置文件迁移
    python3 kunlun.py init initialize                   # 初始化数据库，默认采用sqlite作为数据库
    python3 kunlun.py config load                       # 加载规则进数据库（每次修改规则文件都需要加载）
    python3 kunlun.py -h
    python3 kunlun.py scan -t ./tests/vulnerabilities/
    ```
- [ecriminal/phpvuln](https://github.com/ecriminal/phpvuln)

**相关文章**
- [PHP WebShell代码后门的一次检查](https://www.freebuf.com/articles/web/182156.html)
- [记一次渗透测试](https://www.t00ls.net/articles-58440.html)
- [webshell8.com 最新过waf大马分析。继续分析级去后门方法！](https://www.t00ls.net/thread-44654-1-1.html)
- [报告，我已打入地方内部](https://mp.weixin.qq.com/s/OCGgWAbpWgrrj_UPmGvYLQ)
- [某客户关系管理系统代码审计](https://mp.weixin.qq.com/s/wMvYqcFqy4BGDLh42C5JYg)
- [代码审计-常见php威胁函数（上）](https://mp.weixin.qq.com/s/DdhiHBdOMLIOsa8qMXURHA)
- [代码快速审计详解](https://mp.weixin.qq.com/s/ki-aVPU4FtmjtkZFuK4v-A)

**相关靶场**
- [yaofeifly/PHP_Code_Challenge](https://github.com/yaofeifly/PHP_Code_Challenge)

**php代码解密**
- [php免费在线解密-PHP在线解密](http://dezend.qiling.org/free.html)

---

## 硬编码

**通用关键词**
- [APIkey/密钥信息通用关键词](../../信息收集/信息收集.md#通用关键词)

---

## 文件包含

**描述**

include 将会包含语句并执行指定文件

**条件**

PHP 的配置文件 allow_url_fopen 和 allow_url_include 设置为 ON

**漏洞示例**

```php
<?php
    highlight_file('index.php');
    $file = $_GET['file'];
    include $file;
?>
```

**更多内容**
- [文件包含](../../Web安全/Web_Generic/Web_Generic.md#文件包含)

---

## 文件操作

**相关文章**
- [The End of AFR](https://blog.zeddyu.info/2022/09/27/2022-09-28-TheEndOfAFR/)

**相关工具**
- [wupco/PHP_INCLUDE_TO_SHELL_CHAR_DICT](https://github.com/wupco/PHP_INCLUDE_TO_SHELL_CHAR_DICT)

**相关案例**
- https://github.com/Taiwan-Tech-WebSec/Bug-Report/issues/91

**ctf writeup**
- [Solving "includer's revenge" from hxp ctf 2021 without controlling any files](https://gist.github.com/loknop/b27422d355ea1fd0d90d6dbc1e278d4d)

**文件操作类威胁函数**
```
file_put_contents
file_put_contents($file, $string);
copy highlight_file()
fopen()
read file()
fread()
fgetss()
fgets()
parse_ini_file()
show_source()
file()
file_get_contents
```

**关键词**
```
+filename+
+file+
&file_name=
&filename=
&file=
```

---

## PHP反序列化

**反序列化威胁函数**
```
__construct()
__destruct()
__sleep()
__wakeup()
__toString()
__get()
__set()
__isset()
__unset()
__invoke()
__call()
__callStatic()
```

**更多内容**
- [PHP反序列化](./PHP反序列化.md)

---

## SSRF

**漏洞示例**

curl()
```php
function curl($url){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_exec($ch);
    curl_close($ch);
}

$url = $_GET['url'];
curl($url);
```

file_get_contents()
```php
$url = $_GET['url'];;
echo file_get_contents($url);
```

fsockopen()
```php
function GetFile($host,$port,$link)
{
    $fp = fsockopen($host, intval($port), $errno, $errstr, 30);
    if (!$fp)
    {
        echo "$errstr (error number $errno) \n";
    }
    else
    {
        $out = "GET $link HTTP/1.1\r\n";
        $out .= "Host: $host\r\n";
        $out .= "Connection: Close\r\n\r\n";
        $out .= "\r\n";
        fwrite($fp, $out);
        $contents='';
        while (!feof($fp))
        {
            $contents.= fgets($fp, 1024);
        }
        fclose($fp);
        return $contents;
    }
}
```

**审计函数**
```
cURL
file_get_contents
fsockopen()
curl_exec()
```

**关键词**
```
file_get_contents($
```

**更多内容**
- [SSRF](../../Web安全/Web_Generic/SSRF.md)

### cURL

cURL 支持 http、https、ftp、gopher、telnet、dict、file 和 ldap 等协议,利用 gopher,dict 协议，我们可以构造出相应 payload 直接攻击内网的 redis 服务。

curl/libcurl 7.43 版本上 Gopher 协议存在 bug 即 %00 截断，经测试 7.49 版本可用；

curl_exec() 默认不跟踪跳转；

### file_get_contents

file_get_contents() 支持 php://input 协议

file_get_contents 的 gopher 协议不能 UrlEncode

---

## PHP弱类型

- [弱类型](./弱类型.md)

---

## PHP变量覆盖

- [变量覆盖](./变量覆盖.md)

---

## PHP伪协议

- [PHP伪协议](./伪协议.md)

---

## PHP反序列化

- [PHP反序列化](./PHP反序列化.md)

---

## 命令执行

**审计函数**
```
exec()
system()
shell_exec()
passthru()
pcntl_exec()
popen()
proc_open()
```

---

## 代码执行

**审计函数**
```
eval()
assert()
create_function()
array_map()
call_user_func()
call_user_func_array()
array_filter()
usort()
uasort()
```
