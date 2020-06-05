# Wfuzz

<p align="center">
    <img src="../../../assets/img/logo/wfuzz.svg" width="30%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**官网**
- https://github.com/xmendez/wfuzz

**教程 & Reference**
- [史上最详[ZI]细[DUO]的wfuzz中文教程（一）——初识wfuzz](https://www.freebuf.com/column/163553.html)
- [史上最详[ZI]细[DUO]的wfuzz中文教程（二）——wfuzz 基本用法](https://www.freebuf.com/column/163632.html)
- [史上最详[ZI]细[DUO]的wfuzz中文教程（三）——wfuzz 高级用法](https://www.freebuf.com/column/163787.html)
- [史上最详[ZI]细[DUO]的wfuzz中文教程（四）—— wfuzz 库](https://www.freebuf.com/column/164079.html)

---

# 选项
```
-h/--help : 帮助文档
--help : 高级帮助文档
--version : Wfuzz 详细版本信息
-e <type> : 显示可用的 encoders/payloads/iterators/printers/scripts 列表
--recipe <filename> : 从文件中读取参数
--dump-recipe <filename> : 打印当前的参数并保存成文档
--oF <filename> : 将测试结果保存到文件，这些结果可被 wfuzz payload 处理
-c : 彩色化输出
-v : 详细输出
-f filename,printer : 将结果以 printer 的方式保存到 filename (默认为 raw printer).
-o printer : 输出特定 printer 的输出结果
--interact : (测试功能) 如果启用，所有的按键将会被捕获，这使得你能够与程序交互
--dry-run : 打印测试结果，而并不发送 HTTP 请求
--prev : 打印之前的 HTTP 请求（仅当使用 payloads 来生成测试结果时使用）
-p addr : 使用代理，格式 ip:port:type. 可设置多个代理，type 可取的值为 SOCKS4,SOCKS5 or HTTP（默认）
-t N : 指定连接的并发数，默认为 10
-s N : 指定请求的间隔时间，默认为 0
-R depth : 递归路径探测，depth 指定最大递归数量
-L,--follow : 跟随 HTTP 重定向
-Z : 扫描模式 (连接错误将被忽视).
--req-delay N : 设置发送请求允许的最大时间，默认为 90，单位为秒.
--conn-delay N : 设置连接等待的最大时间，默认为 90，单位为秒.
-A : 是 --script=default -v -c 的简写
--script= : 与 --script=default 等价
--script=<plugins> : 进行脚本扫描， <plugins> 是一个以逗号分开的插件或插件分类列表
--script-help=<plugins> : 显示脚本的帮助
--script-args n1=v1,... : 给脚本传递参数. ie. --script-args grep.regex="<A href=\"(.*?)\">"
-u url : 指定请求的 URL
-m iterator : 指定一个处理 payloads 的迭代器 (默认为 product)
-z payload : 为每一个占位符指定一个 payload，格式为 name[,parameter][,encoder].
    编码可以是一个列表, 如 md5-sha1. 还可以串联起来, 如. md5@sha1.
    还可使用编码各类名，如 url
    使用 help 作为 payload 来显示 payload 的详细帮助信息，还可使用 --slice 进行过滤
--zP <params> : 给指定的 payload 设置参数。必须跟在 -z 或-w 参数后面
--slice <filter> : 以指定的表达式过滤 payload 的信息，必须跟在 -z 参数后面
-w wordlist : 指定一个 wordlist 文件，等同于 -z file,wordlist
-V alltype : 暴力测试所有 GET/POST 参数，无需指定占位符
-X method : 指定一个发送请求的 HTTP 方法，如 HEAD 或 FUZZ
-b cookie : 指定请求的 cookie 参数，可指定多个 cookie
-d postdata : 设置用于测试的 POST data (ex: "id=FUZZ&catalogue=1")
-H header : 设置用于测试请求的 HEADER (ex:"Cookie:id=1312321&user=FUZZ"). 可指定多个 HEADER.
--basic/ntlm/digest auth : 格式为 "user:pass" or "FUZZ:FUZZ" or "domain\FUZ2Z:FUZZ"
--hc/hl/hw/hh N[,N]+ : 以指定的返回码/行数/字数/字符数作为判断条件隐藏返回结果 (用 BBB 来接收 baseline)
--sc/sl/sw/sh N[,N]+ : 以指定的返回码/行数/字数/字符数作为判断条件显示返回结果 (用 BBB 来接收 baseline)
--ss/hs regex : 显示或隐藏返回结果中符合指定正则表达式的返回结果
--filter <filter> : 显示或隐藏符合指定 filter 表达式的返回结果 (用 BBB 来接收 baseline)
--prefilter <filter> : 用指定的 filter 表达式在测试之前过滤某些测试条目
```

---

# 例子

> 注 : 字典不要太大，不然 wfuzz 直接就会跳过

**暴破文件和路径**

wfuzz 自带一些字典文件
```
wfuzz -w /usr/share/wfuzz/wordlist/general/common.txt http://testphp.vulnweb.com/FUZZ

wfuzz -w /usr/share/wfuzz/wordlist/general/common.txt http://testphp.vulnweb.com/FUZZ.php
```

**爆破 URL 中参数**
```
wfuzz -z range,0-10 --hl 97 http://testphp.vulnweb.com/listproducts.php?cat=FUZZ

wfuzz -w GET_params_Top99.txt -w LFI_Linux.txt --hh 851 -u http://192.168.141.139/thankyou.php?FUZZ=FUZ2Z

-w 指定一个 wordlist 文件
-hh 以指定的字符数作为判断条件隐藏返回结果
```

**爆破指定账号密码**
```
wfuzz -v -w test.txt -d "username=admin&password=FUZZ" --hh 206 -u http://192.168.141.137/login.php
```

**测试 Cookies**

在测试请求中加入自己设置的 cookies，可以使用 -b 参数指定，多个 cookies 使用多次。
```
wfuzz -z file,/usr/share/wfuzz/wordlist/general/common.txt -b cookie=value1 -b cookie2=value2 http://testphp.vulnweb.com/FUZZ
```

以上命令可生成如下的 HTTP 请求：
```
GET /attach HTTP/1.1
Host: testphp.vulnweb.com
Accept: */*
Content-Type: application/x-www-form-urlencoded
Cookie: cookie=value1; cookie2=value2
User-Agent: Wfuzz/2.2
Connection: close
```
也可以对 cookie fuzz
```
wfuzz -z file,/usr/share/wfuzz/wordlist/general/common.txt -b cookie=FUZZ http://testphp.vulnweb.com/
```
