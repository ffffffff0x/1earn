# JAVA反序列化

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**简介**

序列化是让 Java 对象脱离 Java 运行环境的一种手段，可以有效的实现多平台之间的通信、对象持久化存储。

Java 程序使用 `ObjectOutputStream` 类的 `writeObject()` 方法可以实现序列化, 相应的，ObjectInputStream 对象的 `readObject()` 方法将反序列化数据转换为 java 对象。但当输入的反序列化的数据可被用户控制，那么攻击者即可通过构造恶意输入，让反序列化产生非预期的对象，在此过程中执行构造的任意代码。

**相关文章**
- [某java客服系统后续代码审计](https://mp.weixin.qq.com/s/Alj6MQmJv9ekGzcUNiIdeg)
- [基础知识｜反序列化命令执行漏洞](https://mp.weixin.qq.com/s/Q75rw573ME73enFsVY4ilA)

**相关工具**
- [java.lang.Runtime.exec() Payload Workarounds](http://www.jackson-t.ca/runtime-exec-payloads.html)
- [matthiaskaiser/jmet](https://github.com/matthiaskaiser/jmet)
- [frohoff/ysoserial](https://github.com/frohoff/ysoserial) - A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization.
    ```bash
    # 建议自己编译
    apt install -y maven
    git clone https://github.com/frohoff/ysoserial.git && cd ysoserial
    mvn clean package -DskipTests
    ```
- [su18/ysoserial](https://github.com/su18/ysoserial)

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

**搜索正则**
```
log4j
logger.info\(".*\{\}.*\)

fastjson
JSON.parse
```

**修复方案**

如果可以明确反序列化对象类的则可在反序列化时设置白名单，对于一些只提供接口的库则可使用黑名单设置不允许被反序列化类或者提供设置白名单的接口，可通过 Hook 函数 `resolveClass` 来校验反序列化的类从而实现白名单校验，示例如下：

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

也可以使用 Apache Commons IO Serialization 包中的 `ValidatingObjectInputStream` 类的 `accept` 方法来实现反序列化类白/黑名单控制，如果使用的是第三方库则升级到最新版本。更多修复方案可参考 [浅谈 Java 反序列化漏洞修复方案](https://xianzhi.aliyun.com/forum/topic/41/)。

---

## JNDI注入

**相关工具**
- [welk1n/JNDI-Injection-Exploit](https://github.com/welk1n/JNDI-Injection-Exploit)
- [mbechler/marshalsec](https://github.com/mbechler/marshalsec)
- [wh1t3p1g/ysomap](https://github.com/wh1t3p1g/ysomap)
- [pimps/JNDI-Exploit-Kit](https://github.com/pimps/JNDI-Exploit-Kit) - JNDI-Exploitation-Kit
- [r00tSe7en/JNDIMonitor/](https://github.com/r00tSe7en/JNDIMonitor/) - 一个LDAP请求监听器，摆脱dnslog平台
- [wyzxxz/jndi_tool](https://github.com/wyzxxz/jndi_tool) - JNDI服务利用工具 RMI/LDAP，支持部分场景回显、内存shell，高版本JDK场景下利用等，fastjson rce命令执行，log4j rce命令执行 漏洞检测辅助工具

---

## RMI反序列化

RMI(Remote Method Invocation) 远程方法调用是一种计算机之间利用远程对象互相调用实现双方通讯的一种通讯机制。使用这种机制，某一台计算机上的对象可以调用另外 一台计算机上的对象来获取远程数据，能让某个 Java 虚拟机上的对象调用另一个 java 虚拟机对象上的方法。RMI 能够让程序员开发出基于 java 的分布式应用。一个 rmi 对象是一个远程 java 对象，可以从另一个 java 虚拟机上调用他的方法，可以像调用本地 java 对象的方法一样调用远程对象的方法。使分布在不同的 JVM 中的对象外表和行为都像本地对象一样。默认端口 1099.

**MSF Modules**
```
use exploit/multi/misc/java_rmi_server
```

**ysoserial**
```
java -cp ysoserial.jar ysoserial.exploit.RMIRegistryExploit 127.0.0.1 8999 CommonsCollections1  "whoami"
```

---

## JDBC反序列化

**相关文章**
- [JDBC Connection URL 攻击](https://paper.seebug.org/1832/)
- [PostgreSQL JDBC Driver RCE](https://mp.weixin.qq.com/s/jb7mbPWdMp1vlgF8F1mshg)

**相关工具**
- [fnmsd/MySQL_Fake_Server](https://github.com/fnmsd/MySQL_Fake_Server) - 用于渗透测试过程中的假MySQL服务器，纯原生python3实现，不依赖其它包。

---

## 漏洞类型案例

- [fastjson](../../Web安全/实验/fastjson.md)
- [log4j](../../Web安全/实验/Log4j.md)
