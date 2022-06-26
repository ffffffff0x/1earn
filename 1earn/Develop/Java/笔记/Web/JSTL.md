# JSTL

---

JSTL全称是JavaServer Pages Tag Library JSP标准标签库

导入 jstl 包
```java
<%@taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
```

* if 标签 ，test 必须属性，接受 boolean 表达式
* choose: 相当于 java 代码的 switch 语句
    1. 使用 choose 标签声明         			相当于 switch 声明
    2. 使用 when 标签做判断         			相当于 case
    3. 使用 otherwise 标签做其他情况的声明    	相当于 default
* foreach: 相当于 java 代码的 for 语句

遍历 list 代码：

```java
<%@ page import="java.util.List" %>
<%@ page import="java.util.ArrayList" %><%--

--%>
<%@ page contentType="text/html;charset=UTF-8" language="java"  %>
<html>
  <head>
    <title>$Title$</title>
  </head>
  <%@taglib prefix="c" uri="http://java.sun.com/jstl/core" %>

  <%
    List list = new ArrayList();
    list.add("aaa");
    list.add("bbb");
    list.add("ccc");

    request.setAttribute("list",list);


  %>

  <c:forEach begin="1" end="10" var="i" step="2" varStatus="s">
    ${i} <h3>${s.index}</h3> <h4> ${s.count} </h4><br>

    </c:forEach>

  </body>
</html>
```

---

## Source & Reference

- https://www.cnblogs.com/nice0e3/p/13544143.html
