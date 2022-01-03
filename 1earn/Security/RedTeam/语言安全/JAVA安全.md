# JAVA安全

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**CTF writup**
- [BUU-Java逆向解密](https://blog.csdn.net/qq_42602454/article/details/108825608)

---

## 反编译

**在线反编译工具**
- [Java decompiler online](http://www.javadecompilers.com/)

**反编译工具**
- [skylot/jadx](https://github.com/skylot/jadx)
- [java-decompiler/jd-gui](https://github.com/java-decompiler/jd-gui)

---

## 技巧

### 判断框架

* web.xml
    - 看 filter
* pom.xml
    - 看依赖,找关键词 fastjson、strust2、spring
* strtus.xml
    - 这种就是直接告诉你有 s2

### 命名

无论是 struts 还是 springmvc/boot，为了方便区分和后续其他开发，除非另类命名，在整个请求处理流程中对于类名的前置命名都是一致的，比如 `NovyController->NovyService->(NovyServiceImpl->)NovyMapper.xml` 而不会出现 `NovyController->TestService->(WhyServiceImpl->)OasdMapper.xml` 这种情况，所以在审计过程中跟进代码时利用 idea 的全局搜索能更好的提高审计效率

![](../../../../assets/img/Security/RedTeam/语言安全/JAVA安全/1.png)

### 方法的跟进

通常调用方法时都是类名. 方法名，比如 `Test.method`，此时就是 `Test` 类里的 `method` 方法来处理接收的数据，当（`test.method`）开头为小写时 `test` 为前面被定义的接口，比如: `private Test test`; 这样 `test` 就可以用到 `Test` 里的方法，

例如 : 某个项目有一个序列化工具类 `SerializeUtil`，在该类里有一个 `deserialize` 方法来反序列化接收的 `request` 数据

![](../../../../assets/img/Security/RedTeam/语言安全/JAVA安全/2.png)

然后在 `controller` 中定义 `private SerializeUtil fvlh;`

![](../../../../assets/img/Security/RedTeam/语言安全/JAVA安全/3.png)

然后进行调用 `fvlh.deserialize(request);`

![](../../../../assets/img/Security/RedTeam/语言安全/JAVA安全/4.png)

---

## JAVA代码审计

**相关文章**
- [一次从内网到外网，黑盒到白盒的批量挖洞经历](http://www.0dayhack.net/index.php/1957/)
- [java审计基础](https://mp.weixin.qq.com/s/cHMNjKDSjK5aSoMHjRWUcg)
- [简单java代码审计？](https://mp.weixin.qq.com/s/88Tsr8NBX03sFlG1Vfz-aw)
- [代码审计_Sylon的博客-CSDN博客_代码审计](https://blog.csdn.net/qq_41770175/article/details/93486383)

**相关资源**
- [Cryin/JavaID](https://github.com/Cryin/JavaID)

### XXE

**漏洞示例**

此处以 org.dom4j.io.SAXReader 为例，仅展示部分代码片段：

```java
String xmldata = request.getParameter("data");
SAXReader sax = new SAXReader();
// 创建一个SAXReader对象
Document document = sax.read(new ByteArrayInputStream(xmldata.getBytes()));
// 获取document对象,如果文档无节点，则会抛出Exception提前结束
Element root = document.getRootElement(); //获取根节点
List rowList = root.selectNodes("//msg");
Iterator<?> iter1 = rowList.iterator();
if (iter1.hasNext()) {
    Element beanNode = (Element) iter1.next();
    modelMap.put("success",true);
    modelMap.put("resp",beanNode.getTextTrim());
}
...
```

**审计函数**

XML 解析一般在导入配置、数据传输接口等场景可能会用到，涉及到 XML 文件处理的场景可留意下 XML 解析器是否禁用外部实体，从而判断是否存在 XXE。部分 XML 解析接口如下：

```
javax.xml.parsers.DocumentBuilder
javax.xml.stream.XMLStreamReader
org.jdom.input.SAXBuilder
org.jdom2.input.SAXBuilder
javax.xml.parsers.SAXParser
org.dom4j.io.SAXReader 
org.xml.sax.XMLReader
javax.xml.transform.sax.SAXSource 
javax.xml.transform.TransformerFactory 
javax.xml.transform.sax.SAXTransformerFactory 
javax.xml.validation.SchemaFactory
javax.xml.bind.Unmarshaller
javax.xml.xpath.XPathExpression
...
```

**修复方案**

使用 XML 解析器时需要设置其属性，禁止使用外部实体，以 SAXReader 为例，安全的使用方式如下:

```java
sax.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
sax.setFeature("http://xml.org/sax/features/external-general-entities", false);
sax.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
```

其它XML解析器的安全使用可参考[OWASP XML External Entity (XXE) Prevention Cheat Sheet](https://www.owasp.org/index.php/XML_External_Entity_%28XXE%29_Prevention_Cheat_Sheet#Java)

---

### 反序列化

**简介**

序列化是让 Java 对象脱离 Java 运行环境的一种手段，可以有效的实现多平台之间的通信、对象持久化存储。

Java 程序使用 ObjectOutputStream 类的 writeObject() 方法可以实现序列化, 相应的，ObjectInputStream 对象的 readObject() 方法将反序列化数据转换为 java 对象。但当输入的反序列化的数据可被用户控制，那么攻击者即可通过构造恶意输入，让反序列化产生非预期的对象，在此过程中执行构造的任意代码。

**相关文章**
- [某java客服系统后续代码审计](https://mp.weixin.qq.com/s/Alj6MQmJv9ekGzcUNiIdeg)
- [基础知识｜反序列化命令执行漏洞](https://mp.weixin.qq.com/s/Q75rw573ME73enFsVY4ilA)

**相关工具**
- [java.lang.Runtime.exec() Payload Workarounds](http://www.jackson-t.ca/runtime-exec-payloads.html)
- [matthiaskaiser/jmet](https://github.com/matthiaskaiser/jmet)
- [frohoff/ysoserial](https://github.com/frohoff/ysoserial) - A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization.

**漏洞示例**

漏洞代码示例如下：

```java
......
//读取输入流,并转换对象
InputStream in=request.getInputStream();
ObjectInputStream ois = new ObjectInputStream(in);
//恢复对象
ois.readObject();
ois.close();
```

上述代码中，程序读取输入流并将其反序列化为对象。此时可查看项目工程中是否引入不安全的基础库
```
commons-fileupload 1.3.1
commons-io 2.4
commons-collections 3.1
commons-logging 1.2
commons-beanutils 1.9.2
org.slf4j:slf4j-api 1.7.21
com.mchange:mchange-commons-java 0.2.11
org.apache.commons:commons-collections 4.0
com.mchange:c3p0 0.9.5.2
org.beanshell:bsh 2.0b5
org.codehaus.groovy:groovy 2.3.9
org.springframework:spring-aop 4.1.4.RELEASE
```

**审计函数**

反序列化操作一般在导入模版文件、网络通信、数据传输、日志格式化存储、对象数据落磁盘或DB存储等业务场景,在代码审计时可重点关注一些反序列化操作函数并判断输入是否可控，如下：

```
ObjectInputStream.readObject
ObjectInputStream.readUnshared
XMLDecoder.readObject
Yaml.load
XStream.fromXML
ObjectMapper.readValue
JSON.parseObject
...
```

**修复方案**

如果可以明确反序列化对象类的则可在反序列化时设置白名单，对于一些只提供接口的库则可使用黑名单设置不允许被反序列化类或者提供设置白名单的接口，可通过 Hook 函数 resolveClass 来校验反序列化的类从而实现白名单校验，示例如下：

```java
public class AntObjectInputStream extends ObjectInputStream{
    public AntObjectInputStream(InputStream inputStream)
            throws IOException {
        super(inputStream);
    }

    /**
     * 只允许反序列化SerialObject class
     */
    @Override
    protected Class<?> resolveClass(ObjectStreamClass desc) throws IOException,
            ClassNotFoundException {
        if (!desc.getName().equals(SerialObject.class.getName())) {
            throw new InvalidClassException(
                    "Unauthorized deserialization attempt",
                    desc.getName());
        }
        return super.resolveClass(desc);
    }
}
```

也可以使用 Apache Commons IO Serialization 包中的 ValidatingObjectInputStream 类的 accept 方法来实现反序列化类白/黑名单控制，如果使用的是第三方库则升级到最新版本。更多修复方案可参考 [浅谈 Java 反序列化漏洞修复方案](https://xianzhi.aliyun.com/forum/topic/41/)。

#### JNDI注入

**相关工具**
- [welk1n/JNDI-Injection-Exploit](https://github.com/welk1n/JNDI-Injection-Exploit)
- [mbechler/marshalsec](https://github.com/mbechler/marshalsec)
- [wh1t3p1g/ysomap](https://github.com/wh1t3p1g/ysomap)
- [pimps/JNDI-Exploit-Kit](https://github.com/pimps/JNDI-Exploit-Kit) - JNDI-Exploitation-Kit
- [r00tSe7en/JNDIMonitor/](https://github.com/r00tSe7en/JNDIMonitor/) - 一个LDAP请求监听器，摆脱dnslog平台

#### RMI反序列化

RMI(Remote Method Invocation) 远程方法调用是一种计算机之间利用远程对象互相调用实现双方通讯的一种通讯机制。使用这种机制，某一台计算机上的对象可以调用另外 一台计算机上的对象来获取远程数据，能让某个 Java 虚拟机上的对象调用另一个 java 虚拟机对象上的方法。RMI 能够让程序员开发出基于 java 的分布式应用。一个 rmi 对象是一个远程 java 对象，可以从另一个 java 虚拟机上调用他的方法，可以像调用本地 java 对象的方法一样调用远程对象的方法。使分布在不同的 JVM 中的对象外表和行为都像本地对象一样。默认端口 1099

RMI 传输 100% 基于反序列化，因此就可能造成 rce 漏洞

**MSF Modules**
```
use exploit/multi/misc/java_rmi_server
```

**ysoserial**
```
java -cp ysoserial.jar ysoserial.exploit.RMIRegistryExploit 127.0.0.1 8999 CommonsCollections1  "whoami"
```

---

### SSRF

**简介**

SSRF 形成的原因大都是由于代码中提供了从其他服务器应用获取数据的功能但没有对目标地址做过滤与限制。比如从指定 URL 链接获取图片、下载等。

**漏洞示例**

此处以 HttpURLConnection 为例，示例代码片段如下:

```java
String url = request.getParameter("picurl");
StringBuffer response = new StringBuffer();

URL pic = new URL(url);
HttpURLConnection con = (HttpURLConnection) pic.openConnection();
con.setRequestMethod("GET");
con.setRequestProperty("User-Agent", "Mozilla/5.0");
BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
String inputLine;
while ((inputLine = in.readLine()) != null) {
     response.append(inputLine);
}
in.close();
modelMap.put("resp",response.toString());
return "getimg.htm";
```

**审计函数**

程序中发起 HTTP 请求操作一般在获取远程图片、页面分享收藏等业务场景, 在代码审计时可重点关注一些 HTTP 请求操作函数，如下：

```
HttpClient.execute
HttpClient.executeMethod
HttpURLConnection.connect
HttpURLConnection.getInputStream
URL.openStream
...
```

**修复方案**
* 使用白名单校验 HTTP 请求 url 地址
* 避免将请求响应及错误信息返回给用户
* 禁用不需要的协议及限制请求端口, 仅仅允许 http 和 https 请求等

---

### SQLi

**简介**

注入攻击的本质，是程序把用户输入的数据当做代码执行。这里有两个关键条件，第一是用户能够控制输入；第二是用户输入的数据被拼接到要执行的代码中从而被执行。sql 注入漏洞则是程序将用户输入数据拼接到了 sql 语句中，从而攻击者即可构造、改变 sql 语义从而进行攻击。

**漏洞示例**

```sql
select * from books where id= ${id}
```

**修复方案**

Mybatis 框架 SQL 语句安全写法应使用 `#{}` , 避免使用动态拼接形式 `${}` ，ibatis 则使用 `#` 变量 `#` 。安全写法如下:

```sql
select * from books where id= #{id}
```

---

### 文件上传漏洞

**简介**

文件上传过程中，通常因为未校验上传文件后缀类型，导致用户可上传 jsp 等一些 webshell 文件。代码审计时可重点关注对上传文件类型是否有足够安全的校验，以及是否限制文件大小等。

**漏洞示例**

此处以 MultipartFile 为例，示例代码片段如下:

```java
public String handleFileUpload(MultipartFile file){
    String fileName = file.getOriginalFilename();
    if (fileName==null) {
        return "file is error";
    }
    String filePath = "/static/images/uploads/"+fileName;
    if (!file.isEmpty()) {
        try {
            byte[] bytes = file.getBytes();
            BufferedOutputStream stream =
                    new BufferedOutputStream(new FileOutputStream(new File(filePath)));
            stream.write(bytes);
            stream.close();
            return "OK";
        } catch (Exception e) {
            return e.getMessage();
        }
    } else {
        return "You failed to upload " + file.getOriginalFilename() + " because the file was empty.";
    }
}
```

**审计函数**
```
MultipartFile
```

**修复方案**
* 使用白名单校验上传文件类型、大小限制

---

### URL重定向

**简介**

由于 Web 站点有时需要根据不同的逻辑将用户引向到不同的页面，如典型的登录接口就经常需要在认证成功之后将用户引导到登录之前的页面，整个过程中如果实现不好就可能导致 URL 重定向问题，攻击者构造恶意跳转的链接，可以向用户发起钓鱼攻击。

**漏洞示例**

此处以 Servlet 的 redirect 方式为例，示例代码片段如下:

```java
String site = request.getParameter("url");
if(!site.isEmpty()){
	response.sendRedirect(site);
}
```

**审计函数**

java 程序中 URL 重定向的方法均可留意是否对跳转地址进行校验、重定向函数如下：

```
sendRedirect
setHeader
forward
...
```

**修复方案**

* 使用白名单校验重定向的 url 地址
* 给用户展示安全风险提示，并由用户再次确认是否跳转

---

### CSRF

**简介**

跨站请求伪造（Cross-Site Request Forgery，CSRF）是一种使已登录用户在不知情的情况下执行某种动作的攻击。因为攻击者看不到伪造请求的响应结果，所以 CSRF 攻击主要用来执行动作，而非窃取用户数据。当受害者是一个普通用户时，CSRF 可以实现在其不知情的情况下转移用户资金、发送邮件等操作；但是如果受害者是一个具有管理员权限的用户时 CSRF 则可能威胁到整个 Web 系统的安全。

**漏洞示例**

由于开发人员对 CSRF 的了解不足，错把 “经过认证的浏览器发起的请求” 当成 “经过认证的用户发起的请求”，当已认证的用户点击攻击者构造的恶意链接后就“被” 执行了相应的操作。例如，一个博客删除文章是通过如下方式实现的：

```
GET http://blog.com/article/delete.jsp?id=102
```

当攻击者诱导用户点击下面的链接时，如果该用户登录博客网站的凭证尚未过期，那么他便在不知情的情况下删除了 id 为 102 的文章，简单的身份验证只能保证请求发自某个用户的浏览器，却不能保证请求本身是用户自愿发出的。

**漏洞审计**

此类漏洞一般都会在框架中解决修复，所以在审计 csrf 漏洞时。首先要熟悉框架对 CSRF 的防护方案，一般审计时可查看增删改请求重是否有 token、formtoken 等关键字以及是否有对请求的 Referer 有进行校验。手动测试时, 如果有 token 等关键则替换 token 值为自定义值并重放请求，如果没有则替换请求 Referer 头为自定义链接或置空。重放请求看是否可以成功返回数据从而判断是否存在 CSRF 漏洞。

**修复方案**

* Referer 校验，对 HTTP 请求的 Referer 校验，如果请求 Referer 的地址不在允许的列表中，则拦截请求。
* Token 校验，服务端生成随机 token，并保存在本次会话 cookie 中，用户发起请求时附带 token 参数，服务端对该随机数进行校验。如果不正确则认为该请求为伪造请求拒绝该请求。
* Formtoken 校验，Formtoken 校验本身也是 Token 校验，只是在本次表单请求有效。
* 对于高安全性操作则可使用验证码、短信、密码等二次校验措施
* 增删改请求使用 POST 请求

---

### 命令执行

**简介**

由于业务需求，程序有可能要执行系统命令的功能，但如果执行的命令用户可控，业务上有没有做好限制，就可能出现命令执行漏洞。

**漏洞示例**

此处以 getRuntime 为例，示例代码片段如下:

```java
String cmd = request.getParameter("cmd");
Runtime.getRuntime().exec(cmd);
```

**审计函数**

这种漏洞原理上很简单，重点是找到执行系统命令的函数，看命令是否可控。在一些特殊的业务场景是能判断出是否存在此类功能，这里举个典型的实例场景, 有的程序功能需求提供网页截图功能，笔者见过多数是使用 phantomjs 实现，那势必是需要调用系统命令执行 phantomjs 并传参实现截图。而参数大多数情况下应该是当前 url 或其中获取相关参数，此时很有可能存在命令执行漏洞，还有一些其它比较特别的场景可自行脑洞。

java 程序中执行系统命令的函数如下：

```
Runtime.exec
ProcessBuilder.start
GroovyShell.evaluate
...
```

**修复方案**

* 避免命令用户可控
* 如需用户输入参数，则对用户输入做严格校验，如&&、|、;等

---

### 权限控制

**简介**

越权漏洞可以分为水平、垂直越权两种,程序在处理用户请求时未对用户的权限进行校验，使的用户可访问、操作其他相同角色用户的数据，这种情况是水平越权；如果低权限用户可访问、操作高权限用户则的数据，这种情况为垂直越权。

**漏洞示例**

```java
@RequestMapping(value="/getUserInfo",method = RequestMethod.GET)
public String getUserInfo(Model model, HttpServletRequest request) throws IOException {
    String userid = request.getParameter("userid");
    if(!userid.isEmpty()){
        String info=userModel.getuserInfoByid(userid);
        return info;
    }
    return "";
}
```

**审计函数**

水平、垂直越权不需关注特定函数，只要在处理用户操作请求时查看是否有对当前登陆用户权限做校验从而确定是否存在漏洞

**修复方案**

获取当前登陆用户并校验该用户是否具有当前操作权限，并校验请求操作数据是否属于当前登陆用户，当前登陆用户标识不能从用户可控的请求参数中获取。

---

### 批量请求

**简介**

业务中经常会有使用到发送短信校验码、短信通知、邮件通知等一些功能，这类请求如果不做任何限制，恶意攻击者可能进行批量恶意请求轰炸，大量短信、邮件等通知对正常用户造成困扰，同时也是对公司的资源造成损耗。

除了短信、邮件轰炸等，还有一种情况也需要注意，程序中可能存在很多接口，用来查询账号是否存在、账号名与手机或邮箱、姓名等的匹配关系，这类请求如不做限制也会被恶意用户批量利用，从而获取用户数据关系相关数据。对这类请求在代码审计时可关注是否有对请求做鉴权、和限制即可大致判断是否存在风险。

**漏洞示例**

```java
@RequestMapping(value="/ifUserExit",method = RequestMethod.GET)
public String ifUserExit(Model model, HttpServletRequest request) throws IOException {
    String phone = request.getParameter("phone");
    if(! phone.isEmpty()){
        boolean ifex=userModel.ifuserExitByPhone(phone);
        if (!ifex)
            return "用户不存在";
    }
    return "用户已被注册";
}
```

**修复方案**

* 对同一个用户发起这类请求的频率、每小时及每天发送量在服务端做限制，不可在前端实现限制

---

### 第三方组件安全

**简介**

这个比较好理解，诸如 Struts2、不安全的编辑控件、XML 解析器以及可被其它漏洞利用的如 commons-collections:3.1 等第三方组件，这个可以在程序 pom 文件中查看是否有引入依赖。即便在代码中没有应用到或很难直接利用，也不应该使用不安全的版本，一个产品的周期很长，很难保证后面不会引入可被利用的漏洞点。

**修复方案**

* 使用最新或安全版本的第三方组件

---

### SPel注入

**简介**

Spel 是 Spring 框架 el 表达式的缩写，当使用 SpelExpressionParser 解析 spel 表达式，且表达式可被外部控制，则可能导致 SPel 表达式注入从而造成 RCE，如 [CVE-2018-1260](https://github.com/Cryin/Paper/blob/master/CVE-2018-1260%20spring-security-oauth2%20RCE%20Analysis.md) 就是 spring-security-oauth2 的一个 SPel 注入导致的 RCE 。

**漏洞示例**

```java
@RequestMapping(path = "/elinjection")
public class SPelInjectionController {
    @RequestMapping(value="/spel.html",method= RequestMethod.GET)
    public String SPelInjection(ModelMap modelMap, HttpServletRequest request, HttpServletResponse response) throws IOException {
        String el=request.getParameter("el");
        //el="T(java.lang.Runtime).getRuntime().exec(\"open /Applications/Calculator.app\")";
        ExpressionParser PARSER = new SpelExpressionParser();
        Expression exp = PARSER.parseExpression(el);
        return (String)exp.getValue();
    }
}
```

**修复方案**

* 解析 el 表达式时，参数不要由外部用户输入

---

### Autobinding

**简介**

Autobinding-自动绑定漏洞，根据不同语言/框架，该漏洞有几个不同的叫法，如下：

* Mass Assignment: Ruby on Rails, NodeJS
* Autobinding: Spring MVC, ASP.NET MVC
* Object injection: PHP(对象注入、反序列化漏洞)

软件框架有时允许开发人员自动将 HTTP 请求参数绑定到程序代码变量或对象中，从而使开发人员更容易地使用该框架。这里攻击者就可以利用这种方法通过构造 http 请求，将请求参数绑定到对象上，当代码逻辑使用该对象参数时就可能产生一些不可预料的结果。

**相关文章**
- [【技术分享】自动绑定漏洞和Spring MVC](https://www.anquanke.com/post/id/86278)
- [自动绑定漏洞](https://blog.csdn.net/qq_34101364/article/details/109732337)
- [Spring MVC Autobinding漏洞实例初窥](https://xz.aliyun.com/t/1089)

**漏洞示例**

示例代码以 [ZeroNights-HackQuest-2016](https://github.com/GrrrDog/ZeroNights-HackQuest-2016) 的 demo 为例，把示例中的 justiceleague 程序运行起来，可以看到这个应用菜单栏有 about，reg，Sign up，Forgot password 这 4 个页面组成。我们关注的点是密码找回功能，即怎么样绕过安全问题验证并找回密码。

1）首先看 reset 方法，把不影响代码逻辑的删掉。这样更简洁易懂：

```java
@Controller
@SessionAttributes("user")
public class ResetPasswordController {

private UserService userService;
...
@RequestMapping(value = "/reset", method = RequestMethod.POST)
public String resetHandler(@RequestParam String username, Model model) {
		User user = userService.findByName(username);
		if (user == null) {
			return "reset";
		}
		model.addAttribute("user", user);
		return "redirect: resetQuestion";
	}
```

这里从参数获取 username 并检查有没有这个用户，如果有则把这个 user 对象放到 Model 中。因为这个 Controller 使用了 `@SessionAttributes("user")`，所以同时也会自动把 user 对象放到 session 中。然后跳转到 resetQuestion 密码找回安全问题校验页面。

2）resetQuestion 密码找回安全问题校验页面有 `resetViewQuestionHandler` 这个方法展现

```java
@RequestMapping(value = "/resetQuestion", method = RequestMethod.GET)
	public String resetViewQuestionHandler(@ModelAttribute User user) {
		logger.info("Welcome resetQuestion ! " + user);
		return "resetQuestion";
	}
```

这里使用了 `@ModelAttribute User user`，实际上这里是从 session 中获取 user 对象。但存在问题是如果在请求中添加 user 对象的成员变量时则会更改 user 对象对应成员的值。
所以当我们给 resetQuestionHandler 发送 GET 请求的时候可以添加 “answer=hehe” 参数，这样就可以给 session 中的对象赋值，将原本密码找回的安全问题答案修改成“hehe”。这样在最后一步校验安全问题时即可验证成功并找回密码

**审计函数**

这种漏洞一般在比较多步骤的流程中出现，比如转账、找密等场景，也可重点留意几个注解如下：

```
@SessionAttributes
@ModelAttribute
...
```

更多信息可参考[Spring MVC Autobinding漏洞实例初窥](https://xianzhi.aliyun.com/forum/topic/1089/)

**修复方案**

Spring MVC 中可以使用 @InitBinder 注解，通过 WebDataBinder 的方法 setAllowedFields、setDisallowedFields 设置允许或不允许绑定的参数。
