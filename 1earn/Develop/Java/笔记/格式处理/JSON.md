# JSON

---

通过 Jackson 解析 json

Maven依赖
```xml
		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artifactId>jackson-databind</artifactId>
			<version>2.10.0</version>
		</dependency>
```

使用下面的代码解析一个 JSON 文件
```java
InputStream input = Main.class.getResourceAsStream("/book.json");
ObjectMapper mapper = new ObjectMapper();
// 反序列化时忽略不存在的JavaBean属性:
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
Book book = mapper.readValue(input, Book.class);
```

核心代码是创建一个 `ObjectMapper` 对象。关闭 `DeserializationFeature`.`FAIL_ON_UNKNOWN_PROPERTIES` 功能使得解析时如果 JavaBean 不存在该属性时解析不会报错。

---

把 JSON 解析为 JavaBean 的过程称为反序列化。如果把 JavaBean 变为 JSON，那就是序列化。要实现 JavaBean 到 JSON 的序列化，只需要一行代码：

```java
String json = mapper.writeValueAsString(book);
```

要把 JSON 的某些值解析为特定的 Java 对象，例如 `LocalDate`，也是完全可以的。例如：
```json
{
    "name": "Java核心技术",
    "pubDate": "2016-09-01"
}
```

要解析为：

```java
public class Book {
    public String name;
    public LocalDate pubDate;
}
```

只需要引入标准的 JSR 310 关于 JavaTime 的数据格式定义至 Maven：

```xml
		<dependency>
			<groupId>com.fasterxml.jackson.datatype</groupId>
			<artifactId>jackson-datatype-jsr310</artifactId>
			<version>2.10.0</version>
		</dependency>
```

然后，在创建 `ObjectMapper` 时，注册一个新的 `JavaTimeModule`：

```java
ObjectMapper mapper = new ObjectMapper().registerModule(new JavaTimeModule());
```

有些时候，内置的解析规则和扩展的解析规则如果都不满足我们的需求，还可以自定义解析。

举个例子，假设 `Book` 类的 `isbn` 是一个 `BigInteger`：

```java
public class Book {
	public String name;
	public BigInteger isbn;
}
```

但 JSON 数据并不是标准的整形格式：

```json
{
    "name": "Java核心技术",
    "isbn": "978-7-111-54742-6"
}
```

直接解析，肯定报错。这时，我们需要自定义一个 `IsbnDeserializer`，用于解析含有非数字的字符串：

```java
public class IsbnDeserializer extends JsonDeserializer<BigInteger> {
    public BigInteger deserialize(JsonParser p, DeserializationContext ctxt) throws IOException, JsonProcessingException {
        // 读取原始的JSON字符串内容:
        String s = p.getValueAsString();
        if (s != null) {
            try {
                return new BigInteger(s.replace("-", ""));
            } catch (NumberFormatException e) {
                throw new JsonParseException(p, s, e);
            }
        }
        return null;
    }
}
```

然后，在 Book 类中使用注解标注：

```java
public class Book {
    public String name;
    // 表示反序列化isbn时使用自定义的IsbnDeserializer:
    @JsonDeserialize(using = IsbnDeserializer.class)
    public BigInteger isbn;
}
```

类似的，自定义序列化时我们需要自定义一个 IsbnSerializer，然后在 Book 类中标注 `@JsonSerialize(using = ...)` 即可。

---

## Source & Reference

- https://www.liaoxuefeng.com/wiki/1252599548343744/1320418650619938
