# Connection

---

**Connection 的作用**

此 header 的 含义是当 client 和 server 通信时对于长链接如何进行处理。

**Connection: close 的作用**

有的网站会在服务器运行一段时间后 down 掉，有很多原因可能造成这种现象：比如 tomcat 堆和非堆内存设置不足，程序没能释放内存空间造成内存溢出，或者某些进程一直运行没能释放，造成 cup 资源大量消耗。

但除了程序本身的原因，还有可能是客服端访问造成（当然这个客户端也包含如蜘蛛软件等搜索引擎），如果服务器和客户端建立的是长链接 (可以用 "netstat -a" 命令查看网络访问信息)，这就需要对 http 响应头的 connection 做一定的设置。

**Connection: keep-alive 的作用**

如果你用过 Mysql，应该知道 Mysql 的连接属性中有一个与 KeepAlive 类似的 Persistent Connection，即：长连接 (PConnect)。该属性打开的话，可以使一次 TCP 连接为同一用户的多次请求服务，提高了响应速度。

**Connection: close 和 keep-alive 的区别**

KeepAlive=On 时，每次用户访问，打开一个 TCP 连接，Apache 都会保持该连接一段时间，以便该连接能连续为同一 client 服务，在 KeepAliveTimeOut 还没到期并且 MaxKeepAliveRequests 还没到阈值之前，Apache 必然要有一个 httpd 进程来维持该连接，httpd 进程不是廉价的，他要消耗内存和 CPU 时间片的。假如当前 Apache 每秒响应 100 个用户访问，KeepAliveTimeOut=5，此时 httpd 进程数就是 100x5=500 个 (prefork 模式)，一个 httpd 进程消耗 5M 内存的话，就是 500x5M=2500M=2.5G，夸张吧？当然，Apache 与 Client 只进行了 100 次 TCP 连接。如果你的内存够大，系统负载不会太高，如果你的内存小于 2.5G，就会用到 Swap，频繁的 Swap 切换会加重 CPU 的 Load。

现在我们关掉 KeepAlive ，Apache 仍然每秒响应 100 个用户访问，因为我们将图片、js、css 等分离出去了，每次访问只有 1 个 request，此时 httpd 的进程数是 100x1=100 个，使用内存 100x5M=500M，此时 Apache 与 Client 也是进行了 100 次 TCP 连接。性能却提升了太多。

**如何选择**

当你的 Server 内存充足时，KeepAlive =On 还是 Off 对系统性能影响不大。

当你的 Server 上静态网页 (Html、图片、Css、Js) 居多时，建议打开 KeepAlive。

当你的 Server 多为动态请求(因为连接数据库，对文件系统访问较多)，KeepAlive 关掉，会节省一定的内存，节省的内存正好可以作为文件系统的 Cache(vmstat 命令中 cache 一列)，降低 I/O 压力。

当 KeepAlive=On 时，KeepAliveTimeOut 的设置其实也是一个问题，设置的过短，会导致 Apache 频繁建立连接，给 Cpu 造成压力，设置的过长，系统中就会堆积无用的 Http 连接，消耗掉大量内存，具体设置多少，可以进行不断的调节，因你的网站浏览和服务器配置而异。

---

**Source & Reference**
- [Connection: close和keep-alive之间的区别](https://developer.aliyun.com/article/277977)
- [关于设置http响应头connection的作用](https://blog.csdn.net/minghaitang/article/details/83567259)
