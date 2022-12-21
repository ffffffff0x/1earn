# Python 代码审计

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关工具**
- [PyCQA/bandit](https://github.com/PyCQA/bandit) - Bandit is a tool designed to find common security issues in Python code.
    ```bash
    pip3 install bandit
    bandit -r path/to/your/code
    ```

**相关资源**
- [MisakiKata/python_code_audit](https://github.com/MisakiKata/python_code_audit)
- [bit4woo/python_sec](https://github.com/bit4woo/python_sec)

---

## 信息泄漏

**描述**

部分功能点开发者会采用 `print` 或者 `logging` 来输出调试日志。在实际生产环境中需要清除，特别是关键处的错误异常输出。对没必要的异常显示，需要做异常处理显示或者禁止异常输出。

---

## 硬编码

**通用关键词**
- [APIkey/密钥信息通用关键词](../信息收集/信息收集.md#通用关键词)

---

## 代码注入 & 命令执行

**审计函数**
```
exec
execfile
eval

os.system
os.popen
commands.getstatusoutput
commands.getoutput
commands.getstatus
subprocess
paramiko
```

---

## 依赖安全

**相关工具**
- [pyupio/safety](https://github.com/pyupio/safety) - Safety checks Python dependencies for known security vulnerabilities and suggests the proper remediations for vulnerabilities detected.
    ```bash
    pip3 install safety
    # 扫描整个环境
    safety check
    #仅检查当前项目的依赖项
    safety check -r requirements.txt
    # 检查某一个依赖项
    echo "insecure-package==0.1" | safety check --stdin
    ```

---

## SSRF

**审计函数**
```
pycurl
urllib
urllib3
requests
```

**相关文章**
- https://github.com/MisakiKata/python_code_audit/blob/master/SSRF.md

---

## 反序列化

**审计函数**
```
marshal
PyYAML
pickle
cpickle
shelve
PIL
```

**相关文章**
- https://github.com/MisakiKata/python_code_audit/blob/master/%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96.md
