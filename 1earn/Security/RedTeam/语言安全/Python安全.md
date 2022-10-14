# Python安全

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

## 代码混淆

- [Hnfull/Intensio-Obfuscator: Obfuscate a python code 2.x and 3.x](https://github.com/Hnfull/Intensio-Obfuscator)

---

## 编译成二进制

- Pyinstaller
- py2exe
- [Nuitka/Nuitka](https://github.com/Nuitka/Nuitka)

---

## 隐藏 Traceback 信息

Python 运行报错时打印的 Trackback 信息也会泄露一些信息，可以使用如下方法隐藏：
```py
import sys
sys.stderr = open("/dev/null", 'w')
```

---

## pyc

### pyc 反编译

- [pyc反编译](./Python安全/pyc反编译.md)

### pyc 隐写

- [AngelKitty/stegosaurus](https://github.com/AngelKitty/stegosaurus) - Stegosaurus是一个隐写工具，它允许我们在Python字节码文件（pyc或pyo）中嵌入任意的Payloads。由于编码密度低，嵌入Payloads的过程不会改变源代码的运行行为，也不会改变源文件的文件大小。Payload 代码散布在字节码中，所以像 strings 这样的代码工具无法找到实际的 Payload。Python的dis模块返回源文件的字节码，然后我们可以使用Stegosaurus来嵌入Payload。Stegosaurus 仅支持 Python3.6 及其以下版本

---

## 沙箱逃逸

- [沙箱逃逸](./Python安全/沙箱逃逸.md)

---

## flask 安全

- [flask安全](./Python安全/flask安全.md)

---

## Python 代码审计

**相关工具**
- [PyCQA/bandit](https://github.com/PyCQA/bandit) - Bandit is a tool designed to find common security issues in Python code.
    ```bash
    pip3 install bandit
    bandit -r path/to/your/code
    ```

### 硬编码

**通用关键词**
- [APIkey/密钥信息通用关键词](../信息收集/信息收集.md#通用关键词)

### 命令执行

**审计函数**
```
os.system
os.popen
commands.getstatusoutput
```
