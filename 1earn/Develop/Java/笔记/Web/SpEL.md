# SpEL

---

## SpEL简介

在 Spring 3 中引入了 Spring 表达式语言（Spring Expression Language，简称 SpEL），这是一种功能强大的表达式语言，支持在运行时查询和操作对象图，可以与基于 XML 和基于注解的 Spring 配置还有 bean 定义一起使用。

在 Spring 系列产品中，SpEL 是表达式计算的基础，实现了与 Spring 生态系统所有产品无缝对接。Spring 框架的核心功能之一就是通过依赖注入的方式来管理 Bean 之间的依赖关系，而 SpEL 可以方便快捷的对 ApplicationContext 中的 Bean 进行属性的装配和提取。由于它能够在运行时动态分配值，因此可以为我们节省大量 Java 代码。

SpEL 有许多特性：
- 使用 Bean 的 ID 来引用 Bean
- 可调用方法和访问对象的属性
- 可对值进行算数、关系和逻辑运算
- 可使用正则表达式进行匹配
- 可进行集合操作

## SpEL 定界符——#{}

SpEL 使用 `#{}` 作为定界符，所有在大括号中的字符都将被认为是 SpEL 表达式，在其中可以使用 SpEL 运算符、变量、引用 bean 及其属性和方法等。

这里需要注意 `#{}` 和 `${}` 的区别：

- `#{}` 就是 SpEL 的定界符，用于指明内容未 SpEL 表达式并执行；
- `${}` 主要用于加载外部属性文件中的值；

两者可以混合使用，但是必须 `#{}` 在外面，`${}` 在里面，如 `#{'${}'}`，注意单引号是字符串类型才添加的；

## SpEL 表达式类型

### 字面值

最简单的 SpEL 表达式就是仅包含一个字面值。

下面我们在 XML 配置文件中使用 SpEL 设置类属性的值为字面值，此时需要用到 `#{}` 定界符，注意若是指定为字符串的话需要添加单引号括起来：
```xml
<property name="message1" value="#{666}"/>
<property name="message2" value="#{'test'}"/>
```

还可以直接与字符串混用：
```xml
<property name="message" value="the value is #{666}"/>
```

Java 基本数据类型都可以出现在 SpEL 表达式中，表达式中的数字也可以使用科学计数法：
```xml
<property name="salary" value="#{1e4}"/>
```

Demo
```java
// HelloWorld.java
package com.test;

public class HelloWorld {
    private String message;

    public void setMessage(String message){
        this.message  = message;
    }

    public void getMessage(){
        System.out.println("Your Message : " + message);
    }
}
```

```java
// MainApp.java
package com.test;

import com.test.service.AccountService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
        HelloWorld obj = (HelloWorld) context.getBean("helloWorld");
        obj.getMessage();
    }
}
```

Beans.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-3.0.xsd ">

    <bean id="helloWorld" class="com.test.HelloWorld">
        <property name="message" value="#{'test'} is #{666}" />
    </bean>

</beans>
```

运行输出：
```
Your Message : test is 666
```
