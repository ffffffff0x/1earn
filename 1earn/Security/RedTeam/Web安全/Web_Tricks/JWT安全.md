# JWT 安全

---

关于 JWT 认证的基本知识点可见笔记 [认证 & 授权](../../../../Develop/Web/笔记/认证&授权.md#JWT)

**相关文章**
- [全程带阻:记一次授权网络攻防演练 (上) ](https://www.freebuf.com/vuls/211842.html)
- [对jwt的安全测试方式总结](https://saucer-man.com/information_security/377.html)
- [攻击JWT的一些方法 ](https://xz.aliyun.com/t/6776)
- [JWT攻击手册：如何入侵你的Token](https://mp.weixin.qq.com/s/x43D718Tw3LZ4QGFxjLjuw)
- [JSON Web Token Validation Bypass in Auth0 Authentication API](https://insomniasec.com/blog/auth0-jwt-validation-bypass)

**Tips**

搜索 JWT 的正则,来自 以下正则来自 以下内容来自 <sup>[[ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool#tips)]</sup>
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
