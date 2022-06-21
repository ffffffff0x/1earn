# fastjson

---

## maven 依赖

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>x.x.x</version>
</dependency>
```

## Fastjson API

### 定义 Bean

Group.java
```java
public class Group {

    private Long       id;
    private String     name;
    private List<User> users = new ArrayList<User>();
}
```

User.java
```java
public class User {

    private Long   id;
    private String name;
}
```

### 初始化 Bean

```java
Group group = new Group();
group.setId(0L);
group.setName("admin");

User guestUser = new User();
guestUser.setId(2L);
guestUser.setName("guest");

User rootUser = new User();
rootUser.setId(3L);
rootUser.setName("root");

group.addUser(guestUser);
group.addUser(rootUser);
```

### 序列化

```java
String jsonString = JSON.toJSONString(group);
System.out.println(jsonString);
```

### 反序列化

```java
Group bean = JSON.parseObject(jsonString, Group.class);
```

---

## Fastjson 注解

### @JSONField

可以配置在属性（setter、getter）和字段（必须是 public field）上。

```java
@JSONField(name="ID")
public int getId() {return id;}

// 配置date序列化和反序列使用yyyyMMdd日期格式
@JSONField(format="yyyyMMdd")
public Date date1;

// 不序列化
@JSONField(serialize=false)
public Date date2;

// 不反序列化
@JSONField(deserialize=false)
public Date date3;

// 按ordinal排序
@JSONField(ordinal = 2)
private int f1;

@JSONField(ordinal = 1)
private int f2;
```

### @JSONType

* 自定义序列化：[ObjectSerializer](https://github.com/alibaba/fastjson/wiki/JSONType_serializer)
* 子类型处理：[SeeAlso](https://github.com/alibaba/fastjson/wiki/JSONType_seeAlso_cn)

JSONType.alphabetic 属性: fastjson 缺省时会使用字母序序列化，如果你是希望按照 java fields/getters 的自然顺序序列化，可以配置 JSONType.alphabetic，使用方法如下：

```java
@JSONType(alphabetic = false)
public static class B {
    public int f2;
    public int f1;
    public int f0;
}
```

---

## 案例

```xml
    <dependencies>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.73</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>compile</scope>
        </dependency>
    </dependencies>
```

### Map 转 JSON 字符串

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test1 {

    @Test
    public void test1() {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("key1", "One");
        map.put("key2", "Two");
        String mapJson = JSON.toJSONString(map);
        System.out.println(mapJson);//输出：{"key1":"One","key2":"Two"}
    }
}
```

### POJO List 转 JSON 字符串

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test6 {

    @Test
    public void test6() {
        Person person1 = new Person();
        person1.setName("张三");
        person1.setAge(28);
        person1.setBirthday(new Date());

        Person person2 = new Person();
        person2.setName("李四");
        person2.setAge(25);
        person2.setBirthday(new Date());

        List<Person> persons = new ArrayList<Person>();
        persons.add(person1);
        persons.add(person2);

        String object = JSON.toJSONString(persons);
        System.out.println(object);
        /**输出如下：
         * [{"age":28,"birthday":1530511546991,"name":"张三"},{"age":25,"birthday":1530511546991,"name":"李四"}]
         */
    }
}
```

```java
import javax.xml.crypto.Data;
import java.util.Date;

public class Person {
    public String name;
    public String Sex;
    public int Age;
    public Date Birthday;

    public void setName(String name) {
        this.name = name;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }

    public void setAge(int Age) {
        this.Age = Age;;
    }

    public void setBirthday(Date Birthday) {
        this.Birthday = Birthday;;
    }

}
```

### Json 字符串转 JsonObject

```java
import com.alibaba.fastjson.*;
        import org.junit.Test;
        import java.util.*;

public class test2 {

    @Test
    public void test2() {
        String jsonStr = "{\"key1\":\"One\",\"key2\":\"110\"}";
        JSONObject jsonObject = JSONObject.parseObject(jsonStr);
        System.out.println(jsonObject.getString("key1"));//输出one
        System.out.println(jsonObject.getInteger("key2"));//输出110
        System.out.println(jsonObject.getString("key3"));//输出null
    }
}
```

### JsonObject 转 Json 字符串

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test3 {
    @Test
    public void test3() {
        String jsonStr = "{\"key1\":\"One\",\"key2\":\"110\"}";
        JSONObject jsonObject = JSONObject.parseObject(jsonStr);
        System.out.println(jsonObject.getString("key1"));//输出：one
        System.out.println(jsonObject.getInteger("key2"));//输出：110
        System.out.println(jsonObject.getString("key3"));//输出：null
        String parserJsonStr = JSONObject.toJSONString(jsonObject);
        System.out.println(parserJsonStr);//输出：{"key1":"One","key2":"110"}
    }
}
```

### JSONArray 添加 JSONObject

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test4 {
    @Test
    public void test4() {
        JSONObject jsonObject1 = new JSONObject();
        jsonObject1.put("name", "张三");
        jsonObject1.put("age", 25);

        JSONObject jsonObject2 = new JSONObject();
        jsonObject2.put("name", "李四");
        jsonObject2.put("age", 28);

        JSONArray jsonArray = new JSONArray();
        jsonArray.add(jsonObject1);
        jsonArray.add(jsonObject2);

        String jsonArrStr = JSONArray.toJSONString(jsonArray);
        System.out.println(jsonArrStr);//输出：[{"name":"张三","age":25},{"name":"李四","age":28}]
    }
}
```

### Json 数组字符串转 JsonArray

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test5 {
    @Test
    public void test5() {
        String jsonArrStr = "[{\"name\":\"张三\",\"age\":25},{\"name\":\"李四\",\"age\":28}]";
        JSONArray jsonArray = JSONArray.parseArray(jsonArrStr);
        for (Object object : jsonArray) {
            JSONObject jsonObject = (JSONObject) object;
            System.out.println(jsonObject.getString("name"));
            System.out.println(jsonObject.getString("age"));
            System.out.println("--------------");
        }
    }
}
```

### POJO 转 Json 字符串

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test7 {

    @Test
    public void test7() {
        Person person1 = new Person();
        person1.setName("张三");
        person1.setAge(26);
        person1.setBirthday(new Date());

        /**两种方式都行
         * 因为JSONObject继承了JSON*/
        String object = JSONObject.toJSONString(person1);
        /*String object = JSON.toJSONString(person1);*/

        System.out.println(object);
        /**输出如下：
         * {"age":26,"birthday":1530511790302,"name":"张三"}
         */
    }
}
```

### POJO 转 JsonObject

```java
import com.alibaba.fastjson.*;
        import org.junit.Test;
        import java.util.*;

public class test8 {
    @Test
    public void test8() {
        Person person1 = new Person();
        person1.setName("张三");
        person1.setAge(28);
        person1.setBirthday(new Date());

        /**方式一*/
        String jsonStr = JSONObject.toJSONString(person1);
        JSONObject jsonObject = JSONObject.parseObject(jsonStr);
        System.out.println(jsonObject.get("name"));//输出：张三

        /**方式二*/
        JSONObject jsonObject1 = (JSONObject)JSONObject.toJSON(person1);
        System.out.println(jsonObject1.get("age"));//输出：28
    }
}
```

### POJO List 转 JsonArray

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test9 {
    @Test
    public void test9() {
        Person person1 = new Person();
        person1.setName("张三");
        person1.setAge(28);
        person1.setBirthday(new Date());

        Person person2 = new Person();
        person2.setName("李四");
        person2.setAge(25);
        person2.setBirthday(new Date());

        List<Person> persons = new ArrayList<Person>();
        persons.add(person1);
        persons.add(person2);

        /**方式1*/
        String jsonArrStr = JSONArray.toJSONString(persons);
        JSONArray jsonArray = JSONArray.parseArray(jsonArrStr);
        JSONObject jsonObject1 = (JSONObject)jsonArray.get(0);
        System.out.println(jsonObject1.get("name"));//输出：张三

        /**方式2*/
        JSONArray jsonArray1 = (JSONArray)JSONArray.toJSON(persons);
        JSONObject jsonObject2 = (JSONObject)jsonArray1.get(1);
        System.out.println(jsonObject2.get("name"));//输出：李四
    }
}
```

### JsonObject 转 POJO

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test10 {
    @Test
    public void test10() {
        String content = "{\"PARENT_ID\":1,\"NAME\":\"正式\",\"CODE\":\"101\",\"LEVEL_NUM\":2,\"ID\":2}";
        Map map = JSONObject.parseObject(content, Map.class);//json 对象转 map
        System.out.println(map);//输出：{CODE=101, LEVEL_NUM=2, ID=2, PARENT_ID=1, NAME=国家级正职}
    }
}
```

将Json 对象 转 Java Bean
```java
@Test
public void test10_2() {
    Person person1 = new Person();
    person1.setName("张三");
    person1.setAge(28);
    person1.setBirthday(new Date());

    String jsonPOJOStr = JSON.toJSONString(person1);
    Person person = JSONObject.parseObject(jsonPOJOStr, Person.class);
    System.out.println(person);
    /**
     * 输出：Person{age=28, name='张三', birthday=Mon Jul 02 14:27:53 CST 2018}
     */
}
```

### JsonArray 转 POJO List

```java
import com.alibaba.fastjson.*;
import org.junit.Test;
import java.util.*;

public class test11 {
    @Test
    public void test2() {
        String content = "[{\"PARENT_ID\":1,\"NAME\":\"国家级正职\",\"CODE\":\"101\",\"LEVEL_NUM\":2,\"ID\":2},{\"PARENT_ID\":1,\"NAME\":\"国家级副职\",\"CODE\":\"102\",\"LEVEL_NUM\":2,\"ID\":3}]";
        //parseArray(String text, Class<T> clazz)：clazz 指定 list 中的元素类型
        List<Map> mapList = JSONArray.parseArray(content, Map.class);//json 转 List<Map>
        System.out.println(mapList);
    }
}
```

将Json 数组 转 Java List
```java
@Test
public void test11() {
    String jsonArrPOJOStr = "[{\"birthday\":1530512954968,\"name\":\"张三\",\"age\":28}," +
            "{\"birthday\":1530512954968,\"name\":\"李四\",\"age\":25}]";
    List<Person> personList = JSONArray.parseArray(jsonArrPOJOStr, Person.class);
    for (Person person : personList) {
        System.out.println(person);
    }
    /**
     * 输出：
     * Person{age=28, name='张三', birthday=Mon Jul 02 14:29:14 CST 2018}
     * Person{age=25, name='李四', birthday=Mon Jul 02 14:29:14 CST 2018}
     */
}
```

---

## Source & Reference

- https://dunwu.github.io/javatech/lib/serialized/javalib-json.html
- https://blog.csdn.net/wangmx1993328/article/details/80882745
