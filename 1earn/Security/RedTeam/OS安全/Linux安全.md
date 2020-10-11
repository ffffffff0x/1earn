# Linux 渗透

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**漏洞记录**
- [OS-Exploits](./OS-Exploits.md#Linux)

**渗透框架**
- [d4rk007/RedGhost](https://github.com/d4rk007/RedGhost) - linux 的后渗透框架,可用于权限维持、提权等操作，半图形化.实际测试感觉不太行。

---

# 口令破解

**文章**
- [How to Crack Shadow Hashes After Getting Root on a Linux System](https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/)
- [Linux下的密码Hash——加密方式与破解方法的技术整理](https://3gstudent.github.io/3gstudent.github.io/Linux%E4%B8%8B%E7%9A%84%E5%AF%86%E7%A0%81Hash-%E5%8A%A0%E5%AF%86%E6%96%B9%E5%BC%8F%E4%B8%8E%E7%A0%B4%E8%A7%A3%E6%96%B9%E6%B3%95%E7%9A%84%E6%8A%80%E6%9C%AF%E6%95%B4%E7%90%86/)

**工具**
- [huntergregal/mimipenguin](https://github.com/huntergregal/mimipenguin) - 从当前 Linux 用户转储登录密码的工具
- [Hashcat](../../安全工具/Hashcat.md#爆破shadow文件)
