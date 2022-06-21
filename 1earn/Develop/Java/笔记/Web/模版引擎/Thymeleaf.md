# Thymeleaf

Thymeleaf 中的表达式有好几种
- 变量表达式： ${...}
- 选择变量表达式： *{...}
- 消息表达： #{...}
- 链接 URL 表达式： @{...}
- 片段表达式： ~{...}

## 片段表达式

片段表达式可以用于引用公共的目标片段比如 footer 或者 header

比如在 `/WEB-INF/templates/footer.html` 定义一个片段，名为 copy。 `<div th:fragment="copy">`
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
  <body>
    <div th:fragment="copy">
      &copy; 2011 The Good Thymes Virtual Grocery
    </div>
  </body>
</html>
```

在另一 template 中引用该片段 `<div th:insert="~{footer :: copy}"></div>`
```html
<body>
  ...
  <div th:insert="~{footer :: copy}"></div>
</body>
```

片段表达式语法：
1. `~{templatename::selector}` ，会在 `/WEB-INF/templates/` 目录下寻找名为 templatename 的模版中定义的 fragment，如上面的 `~{footer :: copy}`
2. `~{templatename}` ，引用整个 templatename 模版文件作为 fragment
3. `~{::selector}` 或 `~{this::selector}` ，引用来自同一模版文件名为 selector 的 fragmnt

其中 selector 可以是通过 th:fragment 定义的片段，也可以是类选择器、ID 选择器等。

当 `~{}` 片段表达式中出现 `::`，则 `::` 后需要有值，也就是 selector。

## 预处理

语法：`__${expression}__`

除了所有这些用于表达式处理的功能外，Thymeleaf 还具有预处理表达式的功能。

预处理是在正常表达式之前完成的表达式的执行，允许修改最终将执行的表达式。

预处理的表达式与普通表达式完全一样，但被双下划线符号（如 `__${expression}__` ）包围。
FreeMarker