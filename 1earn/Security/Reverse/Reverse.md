# Reverse

---

**教程实验**
- [如何开始学习逆向以及分析恶意软件？](https://www.freebuf.com/articles/rookie/178382.html)

**相关资源**
- [MicrosoftDocs/sdk-api](https://github.com/MicrosoftDocs/sdk-api) - windows sdk-api 的官方文档

**CTF writup**
- [re学习笔记（1） BUUCTF-re xor](https://blog.csdn.net/palmer9/article/details/102784520)
- [「不一样的 flag」 题解](https://blog.y7n05h.xyz/%E4%B8%8D%E4%B8%80%E6%A0%B7%E7%9A%84flag/)
- [BUU—SimpleRev](http://91wxk.cn/index.php/archives/382/)
- [BUUCTF-刮开有奖](https://zhuanlan.zhihu.com/p/100934324)
- [BUU-刮开有奖](https://wdraemv.github.io/2021/06/10/BUU-%E5%88%AE%E5%BC%80%E6%9C%89%E5%A5%96/)

---

## 文件格式

- [文件头](./FILE/文件头.md)
- [BMP](./FILE/BMP.md)
- [ELF](./FILE/ELF.md)
- [JPG](./FILE/JPG.md)
- [PE](./FILE/PE.md)
- [PNG](./FILE/PNG.md)
- [RAR](./FILE/RAR.md)
- [ZIP](./FILE/ZIP.md)

---

## 文件系统



---

## 软件逆向

**相关资源**
- [mentebinaria/retoolkit](https://github.com/mentebinaria/retoolkit) - 离线逆向工具安装包合集

**相关工具**

- 反编译工具
    - [Hex-Rays IDA pro](../安全工具/IDA.md)
    - [Ghidra](../安全工具/Ghidra.md)

- 查壳
    - ExeinfoPe

- 十六进制编辑器
    - https://hexed.it/ - 在线的 Hex Editor
    - 010editor
    - [WerWolv/ImHex](https://github.com/WerWolv/ImHex)
    - WinHex
    - HxD
    - UltraEdit

---

## 各类语言

### python
- [Python安全](../RedTeam/语言安全/Python安全.md)

### WebAssembly

**相关工具**
- [WebAssembly/wabt](https://github.com/WebAssembly/wabt) - 将 wasm 文件转换成 c 文件
    ```
    wasm2c.exe test.wasm -o test.c
    ```

**CTF writup**
- [2021陇原战"疫" 部分赛题复现](https://mp.weixin.qq.com/s/KIkE50ELd2PBcbqZ_vUyQg)
- [wasm逆向](http://unbelievable.cool/2021/07/15/wasm%E9%80%86%E5%90%91/)

### Go

- [GO安全](../RedTeam/语言安全/GO安全.md)
