# Markdown学习手册

![image](https://user-images.githubusercontent.com/1908863/28227953-eb6eefa4-68a1-11e7-8769-96ea83facf3b.png)

列表
- Bulleted
- List
- **Markdown 代码块**
- **Python 代码块**
- **Ruby 代码块**
+ s
+ s
* a
* a

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item


正如 Kanye West 所说：
> We're living the future so
> the present is our past.
>>s
>>>a
>>>>b
>>>>>f

我觉得你应该在这里使用`<addr>` 才对。


&copy;

```sequence
起床->吃饭: 稀饭油条
吃饭->上班: 不要迟到了
上班->午餐: 吃撑了
上班->下班:
Note right of 下班: 下班了
下班->回家:
Note right of 回家: 到家了
回家-->>起床:
Note left of 起床: 新的一天
```

```sequence
A->>B: 你好
Note left of A: 我在左边     // 注释方向，只有左右，没有上下
Note right of B: 我在右边
B-->A: 很高兴认识你
```



<br/>
<h1>what the fuck</h1>
<h2>this is html</h2>



this is H1
===

this is H2
---


---

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
The HTML specification
is maintained by the W3C.

H~2~O
30^th^
:smile:
:fa-car:

==marked==

### 下面是 Markdown 代码块

```markdown

标题
# 一级标题
## 二级标题
### 三级标题


1. Numbered
2. List

3. a
2. a

\*literal asterisks\*

加粗和斜体
**加粗** 
*斜体*

代码块(去掉\)
\```
code
\```
```


### 下面是 Python 代码块
```python{.line-numbers}
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
```

### 下面是 Ruby 代码块
```ruby{.line-numbers}
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```



### Reference
1. [https://guides.github.com/features/mastering-markdown](https://guides.github.com/features/mastering-markdown)
2. [https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)
3. [Markdown 语法说明 (简体中文版)](https://www.appinn.com/markdown/)
