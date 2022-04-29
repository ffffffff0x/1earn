# Vary

---

## Vary 的作用

Vary 一般出现在 HTTP 请求的响应信息头部，比如像下面这样
```
HTTP/1.0 200 OK
Date: Fri, 24 Sep 2010 23:09:32 GMT
Content-Type: application/json;charset=UTF-8
Content-Language: en-US
Vary: Accept-Encoding,User-Agent
Age: 1235
X-Cache: HIT from cache.kolich.local
X-Cache-Lookup: HIT from cache.kolich.local:80
Content-Length: 25090
Connection: close
```

或者是这样
```
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 31 Dec 2013 16:34:48 GMT
Content-Type: application/x-javascript
Content-Length: 66748
Last-Modified: Tue, 31 Dec 2013 14:30:52 GMT
Connection: keep-alive
Vary: Accept-Encoding
ETag: "52c2d51c-104bc"
Expires: Fri, 29 Dec 2023 16:34:48 GMT
Cache-Control: max-age=315360000
Strict-Transport-Security: max-age=31536000
Accept-Ranges: bytes
```

**Vary 出现在响应信息中的作用是什么呢？**

首先这是由服务器端添加，添加到响应头部。大部分情况下是用在客户端缓存机制或者是缓存服务器在做缓存操作的时候，会使用到 Vary 头，会读取响应头中的 Vary 的内容，进行一些缓存的判断。

对于服务器提供的某个接口来说，有时候会出现不同种类的客户端对其进行网络请求获取数据，不同的客户端可能支持的压缩编码方式不同，可能有的客户端不支持压缩，那么服务器端返回的数据就不能压缩，有的支持 gzip 编码，那么服务器端就可以进行 gzip 编码返回给客户端，客户端获取到数据之后，做响应的 gzip 解码。还有种情况，对于不同的客户端，需要的内容不一样，比如针对特定，浏览器要求输出的内容不一样，比如在 IE6 浏览器上要输出不一样的内容，这就需要服务器端做不同的数据返回。所以说，服务器提供的同一个接口，客户端进行同样的网络请求，对于不同种类的客户端可能需要的数据不同，服务器端的返回方式返回数据也会不同。对于这个问题的解决，我们可以在请求信息添加 Accept-Encoding、User-Agent 等头部。

这些都没有问题，顺利的解决了我们上面提出的问题，然而，当使用到缓存的时候，就会有问题，比如要求针对 IE5 和 IE6 显示不同的数据，针对同一接口的同样的请求，缓存服务器中分别存储了 IE5 和 IE6 两份数据，由于同样的接口同样的请求，一旦服务器判定要从缓存中获取数据的话，很有可能会导致两个客户端的请求拿到同一份数据，这就会让那个数据展示出现问题；再比如说A类客户端支持压缩格式 gzip，B 类客户端不支持压缩，对于同一个接口同样的请求，如果服务器端打算从缓存服务器中取出数据返回的话，A、B 两类客户端可能会收到同样的数据，这样要就会导致编解码出错。

这时候我们的 Vary 响应头就登场了，Vary 的字面意思是“不一、多样化”，顾名思义，它的存在区分同样的网络请求的不同之处，其实就是通过头部信息来区分。

*一个简单的 Vary 头包括：*
```
Vary: Accept-Encoding

Vary: Accept-Encoding,User-Agent

Vary: X-Some-Custom-Header,Host

Vary: *
```

Vary 存在于响应头中，它的内容来自于请求头中相关字段，Vary 头的内容如果是多条则用 `,` 分割。缓存服务器会将某接口的首次请求结果缓存下来（包括响应头中的 Vary），后面在发生相同请求的时候缓存服务器会拿着缓存的 Vary 来进行判断。比如 Vary: Accept-Encoding,User-Agent，那么 Accept-Encoding 与 User-Agent 两个请求头的内容，就会作为判断是否返回缓存数据的依据，当缓存服务器中相同请求的缓存数据的编码格式、代理服务与当前请求的编码格式、代理服务一致，那就返回缓存数据，否则就会从服务器重新获取新的数据。当缓存服务器中已经缓存了该条请求，那么某次服务器端的响应头中如果 Vary 的值改变，则 Vary 会更新到该请求的缓存中去，下次请求会对比新的 Vary 内容。

*官方解释Vary头：*

告知下游的代理服务器，应当如何对以后的请求协议头进行匹配，以决定是否可使用已缓存的响应内容而不是重新从原服务器请求新的内容。

---

## Source & Reference

- [HTTP请求的响应头部Vary的理解](https://blog.csdn.net/qq_29405933/article/details/84315254)
