# JWT 安全

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

关于 JWT 认证的基本知识点可见笔记 [认证 & 授权](../../../../Develop/Web/笔记/认证&授权.md#JWT)

**相关文章**
- [全程带阻:记一次授权网络攻防演练 (上) ](https://www.freebuf.com/vuls/211842.html)
- [对jwt的安全测试方式总结](https://saucer-man.com/information_security/377.html)
- [攻击JWT的一些方法 ](https://xz.aliyun.com/t/6776)
- [JWT攻击手册：如何入侵你的Token](https://mp.weixin.qq.com/s/x43D718Tw3LZ4QGFxjLjuw)
- [JSON Web Token Validation Bypass in Auth0 Authentication API](https://insomniasec.com/blog/auth0-jwt-validation-bypass)

**Tips**

搜索 JWT 的正则,来自 以下正则来自 以下内容来自 <sup>[ [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool#tips) ]</sup>
```re
[= ]ey[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*           稳定的 JWT 版本
[= ]ey[A-Za-z0-9_\/+-]*\.[A-Za-z0-9._\/+-]*     所有 JWT 版本（可能误报）
```
python快速生成 jwt
```python
import jwt
jwt.encode({'字段1':'test','字段2':'123456'},algorithm='none',key='')
```

**相关工具**
- [JSON Web Tokens - jwt.io](https://jwt.io/) - 在线的 jwt 生成
- [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool) - 一个用于验证，伪造和破解JWT（JSON Web令牌）的工具包。
- [Ch1ngg/JWTPyCrack](https://github.com/Ch1ngg/JWTPyCrack)
- [crack JWT](https://pastebin.com/tv99bTNg)
- [brendan-rius/c-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker)
- [andresriancho/jwt-fuzzer](https://github.com/andresriancho/jwt-fuzzer)
- [ozzi-/JWT4B](https://github.com/ozzi-/JWT4B) - 即时操作 JWT 的 burp 插件
- [3v4Si0N/RS256-2-HS256](https://github.com/3v4Si0N/RS256-2-HS256) - JWT 攻击，将算法由 RS256 变为 HS256
- [x1sec/gojwtcrack](https://github.com/x1sec/gojwtcrack) - Fast JSON Web Token (JWT) cracker written in Go
    ```
    gojwtcrack -t token.txt -d ~/SecLists/Passwords/xato-net-10-million-passwords-1000000.txt
    ```
- [aress31/jwtcat](https://github.com/aress31/jwtcat) - A CPU-based JSON Web Token (JWT) cracker and - to some extent - scanner.
- [ahwul/jwt-hack](https://github.com/hahwul/jwt-hack) - jwt-hack is tool for hacking / security testing to JWT. Supported for En/decoding JWT, Generate payload for JWT attack and very fast cracking(dict/brutefoce)

---

# 绕过思路

**加密算法置空**
1. 捕获 JWT.
2. 修改 algorithm 为 None.
3. 在正⽂中⽤任何你想要的内容改变原本的内容，如: email: attacker@gmail.com
4. 使⽤修改后的令牌发送请求并检查结果。

**篡改加密算法**
1. 捕获 JWT token.
2. 如果算法是 RS256，就改成 HS256，然后⽤公钥签名（你可以通过访问 jwks Uri (https://YOUR_DOMAIN/.well-known/jwks.json) 来获得，⼤多数情况下是该网站 https 证书的公钥）。
3. 使⽤修改后的令牌发送请求并检查响应。

**检查服务器端会话终⽌是否正确 (OTG-SESS-006)**
1. 检查应用程序是否使用 JWT 令牌进行认证。
2. 如果是，登录到应用程序并捕获令牌。(⼤多数网络应⽤都会将令牌存储在浏览器的本地存储中)
3. 现在注销应用程序。
4. 用之前捕获的令牌向权限接口发出请求。
5. 有时，请求会成功，因为 Web 应用程序只是从浏览器中删除令牌，而不会在后端将令牌列⼊黑名单。
