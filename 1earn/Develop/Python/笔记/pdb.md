# pdb

---

## Pdb命令列表

```
h: (help) 帮助
c: (continue) 继续执行
w: (where) 显示当前正在执行的代码行的上下文信息
a: (args) 打印当前函数的参数列表
s: (step) 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
n: (next) 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）
d: (down) 执行跳转到在当前堆栈的深一层
u: (up) 执行跳转到当前堆栈的上一层
l: (list) 列出源码
r: (return) 执行当前运行函数到结束
b: (break) 添加断点
p expression: (print) 输出expression的值
pp expression: 好看一点的p expression
q: (quit) 退出debug

单步跳过（next）和单步进入（step）的区别:
单步进入会进入当前行调用的函数内部并停在里面；
单步跳过会（几乎）全速执行完当前行调用的函数，并停在当前函数的下一行。
```

## 配置环境

**单步调试**

```bash
git clone https://github.com/ffffffff0x/name-fuzz.git
pip3 install pyreadline pypinyin
cd name-fuzz

python3 -m pdb name-fuzz.py
```

**设置断点**

```python
import pdb

s = '0'
n = int(s)
pdb.set_trace() #运行到这里会自动暂停
print(10/n)
```

运行上面的脚本在print前自动暂停调试

---

## Source & Reference

- [Flask debug 模式 PIN 码生成机制安全性研究笔记](https://zhuanlan.zhihu.com/p/32336971)
- [Python 调试器之pdb](https://www.cnblogs.com/xiaohai2003ly/p/8529472.html)
