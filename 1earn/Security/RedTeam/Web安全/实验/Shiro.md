# Shiro

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

> 官网 : https://shiro.apache.org/

**简介**

Apache Shiro 是一个功能强大且灵活的开源安全框架,主要功能包括用户认证、授权、会话管理以及加密.

shiro 的漏洞参考 https://issues.apache.org/jira/projects/SHIRO/issues

**相关文章**
- [Apache Shiro回显poc改造计划](https://mp.weixin.qq.com/s/-ODg9xL838wro2S_NK30bw)
- [关于Shiro反序列化漏洞的延伸—升级shiro也能被shell](https://mp.weixin.qq.com/s/NRx-rDBEFEbZYrfnRw2iDw)
- [Shiro 100 Key](https://mp.weixin.qq.com/s/sclSe2hWfhv8RZvQCuI8LA)
- [Shiro组件漏洞与攻击链分析](https://mp.weixin.qq.com/s/j_gx9C_xL1LyrnuFFPFsfg)
- [shiro反序列化绕WAF之未知HTTP请求方法](https://mp.weixin.qq.com/s/1BuMtOTGIFdXrNtkUMm82g)
- [Shiro高版本默认密钥的漏洞利用](https://mp.weixin.qq.com/s/Su5VwfynSVx-PEPxSR_6iw)
- [Shiro反序列化漏洞利用笔记](https://www.cnblogs.com/Yang34/p/14122843.html)
- [Shiro权限验证绕过史](https://s31k31.github.io/2020/08/20/Shiro_Authentication_Bypass/)

**相关工具**
- [sv3nbeast/ShiroScan](https://github.com/sv3nbeast/ShiroScan) - Shiro<=1.2.4 反序列化,一键检测工具
- [wyzxxz/shiro_rce](https://github.com/wyzxxz/shiro_rce) - shiro rce 反序列 命令执行 一键工具
- [bigsizeme/shiro-check](https://github.com/bigsizeme/shiro-check) - Shiro反序列化检查 Burp 插件
- [feihong-cs/ShiroExploit-Deprecated](https://github.com/feihong-cs/ShiroExploit-Deprecated) - Shiro550/Shiro721 一键化利用工具，支持多种回显方式
- [j1anFen/shiro_attack](https://github.com/j1anFen/shiro_attack) - shiro 反序列化漏洞综合利用, 包含（回显执行命令 / 注入内存马）
- [Ares-X/shiro-exploit](https://github.com/Ares-X/shiro-exploit) - Shiro 反序列化利用工具，支持新版本 (AES-GCM)Shiro 的 key 爆破，配合 ysoserial，生成回显 Payload
- [wyzxxz/shiro_rce_tool](https://github.com/wyzxxz/shiro_rce_tool)
- [potats0/shiroPoc](https://github.com/potats0/shiroPoc)
- [SummerSec/ShiroAttack2](https://github.com/SummerSec/ShiroAttack2) - shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原版中NoCC的问题

**指纹**
- `set-Cookie: rememberMe=deleteMe`

---

## 绕过fuzz
- `/;/index`
- `/aaaa/..;/index/1`
- `/admin/%20`

---

## SHIRO-550 & CVE-2016-4437 | Shiro RememberMe 1.2.4 反序列化漏洞

- https://issues.apache.org/jira/projects/SHIRO/issues/SHIRO-550

**描述**

shiro 默认使用了 CookieRememberMeManager, 其处理 cookie 的流程是: 得到 rememberMe 的 cookie 值-->Base64 解码-->AES 解密-->反序列化.然而 AES 的密钥是硬编码的, 就导致了攻击者可以构造恶意数据造成反序列化的 RCE 漏洞。

**影响版本**
- 1.2.4(由于密钥泄露的问题, 部分高于 1.2.4 版本的 Shiro 也会受到影响)

**相关文章**
- [【漏洞分析】Shiro RememberMe 1.2.4 反序列化导致的命令执行漏洞](https://paper.seebug.org/shiro-rememberme-1-2-4/)

**POC | Payload | exp**
- [jas502n/SHIRO-550](https://github.com/jas502n/SHIRO-550)
- [https://vulhub.org/#/environments/shiro/CVE-2016-4437/](https://vulhub.org/#/environments/shiro/CVE-2016-4437/)
- [dr0op/shiro-550-with-NoCC](https://github.com/dr0op/shiro-550-with-NoCC)

---

## SHIRO-682 & CVE-2020-1957 | Shiro 权限绕过漏洞

**描述**

Apache Shiro 是企业常见的 Java 安全框架, 由于 Shiro 的拦截器和 spring(Servlet)拦截器对于 URI 模式匹配的差异, 导致出现鉴权问题。

**相关文章**
- [Shiro 权限绕过漏洞分析（CVE-2020-1957）](https://blog.riskivy.com/shiro-%e6%9d%83%e9%99%90%e7%bb%95%e8%bf%87%e6%bc%8f%e6%b4%9e%e5%88%86%e6%9e%90%ef%bc%88cve-2020-1957%ef%bc%89/)

**修复建议**
1. 升级 1.5.2 版本及以上。
2. 尽量避免使用 * 通配符作为动态路由拦截器的 URL 路径表达式。

---

## SHIRO-721 | Shiro RememberMe Padding Oracle Vulnerability RCE
- https://issues.apache.org/jira/browse/SHIRO-721

**描述**

cookie 的 cookiememeMe 已通过 AES-128-CBC 模式加密，这很容易受到填充 oracle 攻击的影响。

攻击者可以使用有效的 RememberMe cookie 作为 Padding Oracle Attack 的前缀，然后制作精心制作的 RememberMe 来执行 Java 反序列化攻击。

**影响版本**
- 1.2.5 ~ 1.2.6
- 1.3.0 ~ 1.3.2
- 1.4.0-RC2 ~ 1.4.1

**相关文章**
- [Shiro 721 Padding Oracle攻击漏洞分析](https://www.anquanke.com/post/id/193165)
- [Apache Shiro 远程代码执行漏洞复现](http://www.oniont.cn/index.php/archives/298.html)
- [Shiro RCE again（Padding Oracle Attack）](https://www.anquanke.com/post/id/192819)

**POC | Payload | exp**
- [3ndz/Shiro-721](https://github.com/3ndz/Shiro-721)
- [jas502n/SHIRO-721](https://github.com/jas502n/SHIRO-721)

---

## SHIRO-782 & CVE-2020-11989

**相关文章**
- [Apache Shiro权限绕过漏洞分析(CVE-2020-11989)](https://mp.weixin.qq.com/s/yb6Tb7zSTKKmBlcNVz0MBA)
- [Apache Shiro 身份验证绕过漏洞 (CVE-2020-11989)](https://xlab.tencent.com/cn/2020/06/30/xlab-20-002/)
- [CVE-2020-11989：Apache Shiro权限绕过复现](https://mp.weixin.qq.com/s/p1UzULYPoTKf6i_Chcj2VQ)
- [记一次Apache Shiro权限绕过实战](http://www.0dayhack.net/index.php/554/)
- [记一次前台任意文件下载漏洞挖掘](https://xz.aliyun.com/t/10328)

---

## CVE-2020-17523

**相关文章**
- [Apache Shiro身份认证绕过漏洞复现(CVE-2020-17523)](https://mp.weixin.qq.com/s/PHBG3wQUIPSrlmX_jsSXbA)
- [jweny/shiro-cve-2020-17523](https://github.com/jweny/shiro-cve-2020-17523)
