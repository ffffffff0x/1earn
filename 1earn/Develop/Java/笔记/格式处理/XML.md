# XML

---

## DOM

DOM 是 Document Object Model 的缩写，DOM 模型就是把 XML 结构作为一个树形结构处理，从根节点开始，每个节点都可以包含任意个子节点。

我们以下面的 XML 为例：
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<book id="1">
    <name>Java核心技术</name>
    <author>Cay S. Horstmann</author>
    <isbn lang="CN">1234567</isbn>
    <tags>
        <tag>Java</tag>
        <tag>Network</tag>
    </tags>
    <pubDate/>
</book>
```

如果解析为 DOM 结构，它大概长这样：
```
                      ┌─────────┐
                      │document │
                      └─────────┘
                           │
                           ▼
                      ┌─────────┐
                      │  book   │
                      └─────────┘
                           │
     ┌──────────┬──────────┼──────────┬──────────┐
     ▼          ▼          ▼          ▼          ▼
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  name   ││ author  ││  isbn   ││  tags   ││ pubDate │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
                                      │
                                 ┌────┴────┐
                                 ▼         ▼
                             ┌───────┐ ┌───────┐
                             │  tag  │ │  tag  │
                             └───────┘ └───────┘
```

注意到最顶层的 document 代表 XML 文档，它是真正的 “根”，而 `<book>` 虽然是根元素，但它是 document 的一个子节点。

Java 提供了 DOM API 来解析 XML，它使用下面的对象来表示 XML 的内容：

* Document：代表整个 XML 文档；
* Element：代表一个 XML 元素；
* Attribute：代表一个元素的某个属性。

使用 DOM API 解析一个 XML 文档的代码如下：
```java
InputStream input = Main.class.getResourceAsStream("/book.xml");
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(input);
```

`DocumentBuilder.parse()` 用于解析一个 XML，它可以接收 InputStream，File 或者 URL，如果解析无误，我们将获得一个 Document 对象，这个对象代表了整个 XML 文档的树形结构，需要遍历以便读取指定元素的值：

```java
void printNode(Node n, int indent) {
    for (int i = 0; i < indent; i++) {
        System.out.print(' ');
    }
    switch (n.getNodeType()) {
    case Node.DOCUMENT_NODE: // Document节点
        System.out.println("Document: " + n.getNodeName());
        break;
    case Node.ELEMENT_NODE: // 元素节点
        System.out.println("Element: " + n.getNodeName());
        break;
    case Node.TEXT_NODE: // 文本
        System.out.println("Text: " + n.getNodeName() + " = " + n.getNodeValue());
        break;
    case Node.ATTRIBUTE_NODE: // 属性
        System.out.println("Attr: " + n.getNodeName() + " = " + n.getNodeValue());
        break;
    default: // 其他
        System.out.println("NodeType: " + n.getNodeType() + ", NodeName: " + n.getNodeName());
    }
    for (Node child = n.getFirstChild(); child != null; child = child.getNextSibling()) {
        printNode(child, indent + 1);
    }
}
```

解析结构如下：

```
Document: #document
 Element: book
  Text: #text =

  Element: name
   Text: #text = Java核心技术
  Text: #text =

  Element: author
   Text: #text = Cay S. Horstmann
  Text: #text =

  Element: isbn
   Text: #text = 1234567
  Text: #text =

  Element: tags
   Text: #text =

   Comment: #comment =  this is comment
   Text: #text =

   Element: tag
    Text: #text = Java
   Text: #text =

   Element: tag
    Text: #text = Network
   Text: #text =

  Text: #text =

  Element: pubDate
  Text: #text =
```

对于 DOM API 解析出来的结构，我们从根节点 Document 出发，可以遍历所有子节点，获取所有元素、属性、文本数据，还可以包括注释，这些节点被统称为 Node，每个 Node 都有自己的 Type，根据 Type 来区分一个 Node 到底是元素，还是属性，还是文本，等等。

使用 DOM API 时，如果要读取某个元素的文本，需要访问它的 Text 类型的子节点，所以使用起来还是比较繁琐的。

---

## SAX

使用 DOM 解析 XML 的优点是用起来省事，但它的主要缺点是内存占用太大。

另一种解析 XML 的方式是 SAX。SAX 是 Simple API for XML 的缩写，它是一种基于流的解析方式，边读取 XML 边解析，并以事件回调的方式让调用者获取数据。因为是一边读一边解析，所以无论 XML 有多大，占用的内存都很小。

SAX 解析会触发一系列事件：
* startDocument：开始读取 XML 文档；
* startElement：读取到了一个元素，例如 `<book>`；
* characters：读取到了字符；
* endElement：读取到了一个结束的元素，例如 `</book>`；
* endDocument：读取 XML 文档结束。

如果我们用 SAX API 解析 XML，Java 代码如下：

```java
InputStream input = Main.class.getResourceAsStream("/book.xml");
SAXParserFactory spf = SAXParserFactory.newInstance();
SAXParser saxParser = spf.newSAXParser();
saxParser.parse(input, new MyHandler());
```

关键代码 `SAXParser.parse()` 除了需要传入一个 InputStream 外，还需要传入一个回调对象，这个对象要继承自 DefaultHandler：

```java
class MyHandler extends DefaultHandler {
    public void startDocument() throws SAXException {
        print("start document");
    }

    public void endDocument() throws SAXException {
        print("end document");
    }

    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        print("start element:", localName, qName);
    }

    public void endElement(String uri, String localName, String qName) throws SAXException {
        print("end element:", localName, qName);
    }

    public void characters(char[] ch, int start, int length) throws SAXException {
        print("characters:", new String(ch, start, length));
    }

    public void error(SAXParseException e) throws SAXException {
        print("error:", e);
    }

    void print(Object... objs) {
        for (Object obj : objs) {
            System.out.print(obj);
            System.out.print(" ");
        }
        System.out.println();
    }
}
```

运行 SAX 解析代码，可以打印出下面的结果：

```
start document
start element:  book
characters:

start element:  name
characters: Java核心技术
end element:  name
characters:

start element:  author
characters: Cay S. Horstmann
end element:  author
characters:

start element:  isbn
characters: 1234567
end element:  isbn
characters:

start element:  tags
characters:

characters:

start element:  tag
characters: Java
end element:  tag
characters:

start element:  tag
characters: Network
end element:  tag
characters:

end element:  tags
characters:

start element:  pubDate
end element:  pubDate
characters:

end element:  book
end document
```

如果要读取 `<name>` 节点的文本，我们就必须在解析过程中根据 `startElement()` 和 `endElement()` 定位当前正在读取的节点，可以使用栈结构保存，每遇到一个 `startElement()` 入栈，每遇到一个 `endElement()` 出栈，这样，读到 `characters()` 时我们才知道当前读取的文本是哪个节点的。可见，使用 SAX API 仍然比较麻烦。

---

# Jackson

Jackson 的开源的第三方库可以轻松做到 XML 到 JavaBean 的转换。我们要使用 Jackson，先添加两个 Maven 的依赖：
```xml
		<dependency>
			<groupId>com.fasterxml.jackson.dataformat</groupId>
			<artifactId>jackson-dataformat-xml</artifactId>
			<version>2.10.1</version>
		</dependency>
		<dependency>
			<groupId>org.codehaus.woodstox</groupId>
			<artifactId>woodstox-core-asl</artifactId>
			<version>4.4.1</version>
		</dependency>
```

然后，定义好 JavaBean，就可以用下面几行代码解析：
```java
InputStream input = Main.class.getResourceAsStream("/book.xml");
JacksonXmlModule module = new JacksonXmlModule();
XmlMapper mapper = new XmlMapper(module);
Book book = mapper.readValue(input, Book.class);
System.out.println(book.id);
System.out.println(book.name);
System.out.println(book.author);
System.out.println(book.isbn);
System.out.println(book.tags);
System.out.println(book.pubDate);
```

```java
public class Book {
    public long id;
    public String name;
    public String author;
    public String isbn;
    public List<String> tags;
    public String pubDate;
}
```

注意到 XmlMapper 就是我们需要创建的核心对象，可以用 readValue(InputStream, Class) 直接读取 XML 并返回一个 JavaBean。运行上述代码，就可以直接从 Book 对象中拿到数据：
```
1
Java核心技术
Cay S. Horstmann
1234567
[Java, Network]
null
```

如果要解析的数据格式不是 Jackson 内置的标准格式，那么需要编写一点额外的扩展来告诉 Jackson 如何自定义解析。

---

## Source & Reference

- https://www.liaoxuefeng.com/wiki/1252599548343744/1320418577219618
- https://www.liaoxuefeng.com/wiki/1252599548343744/1320414976409634
- https://www.liaoxuefeng.com/wiki/1252599548343744/1320418596093986
