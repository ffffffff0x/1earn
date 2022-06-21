# jackson

---

## jackson 解析器

在 Java 里面常见的 json 解析器有
```
Jsonlib，Gson，fastjson，jackson
```

常用方法

1. readValue(json 字符串数据, Class)      json 转换为 java 对象

2. writeValue(参数，obj):
    * File：将 obj 对象转换为 JSON 字符串，并保存到指定的文件中
    * Writer：将 obj 对象转换为 JSON 字符串，并将 json 数据填充到字符输出流中
    * OutputStream：将 obj 对象转换为 JSON 字符串，并将 json 数据填充到字节输出流中

3. writeValueAsString(obj): 将对象转为 json 字符串

## 对象转 Json

```java
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class jsonDemo {
    public static void main(String[] args) {
        Person person = new Person();
        person.setName("xiaoming");
        person.setSex("name");
        person.setAge(18);
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            String s = objectMapper.writeValueAsString(person);
            System.out.println(s);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }


    }
}
```

```java
public class Person {
    public String name;
    public String Sex;
    public int Age;

    public void setName(String name) {
        this.name = name;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }

    public void setAge(int Age) {
        this.Age = Age;;
    }

}
```

运行后显示数据
```
{"name":"xiaoming","Sex":"name","Age":18}
```

## list集合转换json

```java
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.ArrayList;
import java.util.List;

public class jsonDemo {
    public static void main(String[] args) {
        Person p1= new Person();
        p1.setName("xiaoming");
        p1.setSex("name");
        p1.setAge(18);
        Person p2= new Person();
        p2.setName("xiaoming");
        p2.setSex("name");
        p2.setAge(18);
        ObjectMapper objectMapper = new ObjectMapper();
        List<Person> list = new ArrayList<>();
        list.add(p1);
        list.add(p2);

        try {
            String s = objectMapper.writeValueAsString(list);
            System.out.println(s);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }
}
```

```
[{"name":"xiaoming","Sex":"name","Age":18},{"name":"xiaoming","Sex":"name","Age":18}]
```

## json转Java对象

```java
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class jsonDemo {
    public static void main(String[] args) throws IOException {
       String json = "{\"sex\":\"男\",\"age\":\"18\",\"name\":\"xiaoming\"}";
        ObjectMapper objectMapper = new ObjectMapper();
        Person person = objectMapper.readValue(json, Person.class);
        System.out.println(person.toString());
    }
}
```

---

## Source & Reference

- https://www.cnblogs.com/nice0e3/p/13552644.html
