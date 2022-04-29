# JAVA安全

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**CTF writup**
- [BUU-Java逆向解密](https://blog.csdn.net/qq_42602454/article/details/108825608)

---

## 反编译

**在线反编译工具**
- [Java decompiler online](http://www.javadecompilers.com/)

**反编译工具**
- [skylot/jadx](https://github.com/skylot/jadx)
- [java-decompiler/jd-gui](https://github.com/java-decompiler/jd-gui)

---

## 技巧

### 判断框架

* web.xml
    - 看 filter
* pom.xml
    - 看依赖,找关键词 fastjson、strust2、spring

---

## JAVA代码审计

- [JAVA代码审计](./JAVA安全/JAVA代码审计.md)
