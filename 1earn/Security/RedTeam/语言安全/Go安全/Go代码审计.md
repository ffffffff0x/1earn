## Go代码审计

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**环境搭建**

推荐 goland 配置远程 debug 调试,参考笔记 [goland 远程调试](../../../Develop/Golang/笔记/goland远程调试.md)

**相关工具**
- [praetorian-inc/gokart](https://github.com/praetorian-inc/gokart) - A static analysis tool for securing Go code
    ```bash
    go install github.com/praetorian-inc/gokart@latest
    gokart scan <directory>

    # 扫描远程项目
    gokart scan -r https://github.com/ShiftLeftSecurity/shiftleft-go-demo -v
    # 指定分支
    gokart scan -r https://github.com/ShiftLeftSecurity/shiftleft-go-demo -b actions_fix
    ```
- [madneal/sec-dog](https://github.com/madneal/sec-dog) - goland sca 插件

**相关文章**
- [trojan多用户管理部署程序审计学习](https://r0fus0d.blog.ffffffff0x.com/post/trojan-case/)
- [mayfly-go审计学习](https://r0fus0d.blog.ffffffff0x.com/post/mayfly-go/)

**相关靶场**
- [Hardw01f/Vulnerability-goapp](https://github.com/Hardw01f/Vulnerability-goapp)
    - https://xz.aliyun.com/t/7243
    - https://www.freebuf.com/articles/web/224363.html

---

## 硬编码

**通用关键词**
- [APIkey/密钥信息通用关键词](../../信息收集/信息收集.md#通用关键词)

---

## 命令执行

**审计函数**
```
exec.Command
```
