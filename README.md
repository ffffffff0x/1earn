<p align="center">
    <img src="./assets/img/banner/logo.png">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Category-knowledge-red.svg">
    <img src="https://img.shields.io/github/repo-size/No-Github/1earn?color=yellow">
    <img src="https://img.shields.io/github/last-commit/No-Github/1earn.svg?color=blue">
    <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?color=brightgreen">
</p>

> 万事开头难,然后一直开头一直难...

<p align="center">
    <img src="./assets/img/banner/readme.jpg">
</p>

* **简介** : 本项目的初衷是分享知识资源,让更多人接触和了解安全、运维领域,但受限于本人能力有限,难免会有错误和借鉴的地方,对于内容中有疑问或建议请提交 issue.
* **定位** : ffffffff0x 团队维护的安全知识框架
* **更新时间** : 不定期
* **项目地址** : https://github.com/ffffffff0x/1earn
* **学习线路图** : 初学者或想快速构建知识结构请访问 [roadmap](roadmap.md)

---

## 项目文件一览

* **[Security](./1earn/Security/Power-PenTest.md)**

    * **[安全工具](https://github.com/No-Github/1earn/tree/master/1earn/Security/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7)** - 各类安全工具的使用介绍

    * **安全资源**
        * 靶机
            * HTB
            * VulnHub
                * [DC Serial](./1earn/Security/安全资源/靶机/VulnHub/DC) - DC 系列靶场,难度简单至中等,可以学习各种提权和CMS漏洞利用,推荐初学者挑战
                * [It’s_October](./1earn/Security/安全资源/靶机/VulnHub/It’s_October)
                * [Kioptrix Serial](./1earn/Security/安全资源/靶机/VulnHub/Kioptrix) - Kioptrix 系列靶场,难度简单至中等,推荐初学者挑战
                * [Mission-Pumpkin](./1earn/Security/安全资源/靶机/VulnHub/Mission-Pumpkin) - 难度适中,偏向于加解密比较多,漏洞利用内容较少
                * [symfonos Serial](./1earn/Security/安全资源/靶机/VulnHub/symfonos) - 挺有难度的靶场,内容丰富,难度中等,漏洞利用内容很多,推荐有一定经验者挑战
            * Wargames
                * [Bandit](./1earn/Security/安全资源/靶机/Wargames/Bandit/Bandit-WalkThrough.md)

    * **BlueTeam**
        * [分析](./1earn/Security/BlueTeam/分析.md) - 分析工具与分析案例
        * [加固](./1earn/Security/BlueTeam/加固.md) - 系统、应用加固的方法和工具资源
        * [监察](./1earn/Security/BlueTeam/监察.md) - 有关查杀、监控、蜜罐的资源
        * [取证](./1earn/Security/BlueTeam/取证.md) - 内容涉及操作系统的取证、web 的取证、文件的取证
        * [应急](./1earn/Security/BlueTeam/应急.md) - 应急资源、溯源案例
        * [笔记](https://github.com/No-Github/1earn/blob/master/1earn/Security/BlueTeam/%E7%AC%94%E8%AE%B0) - 涉及磁盘取证、内存取证、USB取证等内容
        * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/BlueTeam/%E5%AE%9E%E9%AA%8C) - 涉及流量分析实战、安防设施搭建等内容

    * **Crypto**
        * [Crypto](./1earn/Security/Crypto/Crypto.md) - 介绍各种编码和加密算法及相关的工具

    * **CTF**
        * [CTF](./1earn/Security/CTF/CTF.md) - 收集 CTF 相关的工具和 writeup 资源
        * [writeup](https://github.com/No-Github/1earn/tree/master/1earn/Security/CTF/writeup) - 自己参与的一些比赛记录

    * **ICS**
        * [工控协议](./1earn/Security/ICS/工控协议.md) - 总结各类工控协议的知识点
        * [上位机安全](./1earn/Security/ICS/上位机安全.md) - 总结上位机安全相关的知识点
        * [PLC攻击](./1earn/Security/ICS/PLC攻击.md) - 总结 PLC 攻击的相关知识点
        * [S7comm相关](./1earn/Security/ICS/S7comm相关.md) - 记录 S7comm 相关错误类型、功能码和相关参数
        * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/ICS/%E5%AE%9E%E9%AA%8C) - 仿真环境搭建和 PLC 攻击实验

    * **IOT**
        * 固件安全
            * [固件安全](./1earn/Security/IOT/固件安全/固件安全.md) - 记录 IOT 固件分析的知识点,包括固件提取、固件分析、固件解密等
            * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/IOT/%E5%9B%BA%E4%BB%B6%E5%AE%89%E5%85%A8/%E5%AE%9E%E9%AA%8C) - 分析固件实验
        * 无线电安全
            * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/IOT/%E6%97%A0%E7%BA%BF%E7%94%B5%E5%AE%89%E5%85%A8/%E5%AE%9E%E9%AA%8C)
            * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/IOT/%E6%97%A0%E7%BA%BF%E7%94%B5%E5%AE%89%E5%85%A8/%E5%AE%9E%E9%AA%8C) - 无线电安全实验
        * 硬件安全
            * [Device-Exploits](./1earn/Security/IOT/硬件安全/Device-Exploits.md) - 嵌入式设备相关漏洞利用,不太熟悉这一块,内容不多
            * [HID](https://github.com/No-Github/1earn/tree/master/1earn/Security/IOT/%E7%A1%AC%E4%BB%B6%E5%AE%89%E5%85%A8/HID) - 和组员制作的 HID 实物记录

    * **MobileSec**
        * [Android安全](./1earn/Security/MobileSec/Android安全.md) - 记录一些安卓安全相关的内容,这块掌握较少

    * **RedTeam**
        * 安防设备
            * [Bypass技巧](./1earn/Security/RedTeam/安防设备/Bypass技巧.md) - 记录 waf 绕过手段
            * [SecDevice-Exploits](./1earn/Security/RedTeam/安防设备/SecDevice-Exploits.md) - 常见的安全设备的漏洞利用方法
        * 后渗透
            * [后渗透](./1earn/Security/RedTeam/后渗透/后渗透.md) - 后渗透知识点的大纲
            * [权限提升](./1earn/Security/RedTeam/后渗透/权限提升.md) - 操作系统和数据库的提权方法
            * [权限维持](./1earn/Security/RedTeam/后渗透/权限维持.md) - 权限维持的各种方法和资源
            * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/RedTeam/%E5%90%8E%E6%B8%97%E9%80%8F/%E5%AE%9E%E9%AA%8C)
        * 软件服务安全
            * [CS-Exploits](./1earn/Security/RedTeam/软件服务安全/CS-Exploits.md) - 收集软件、业务应用服务漏洞的渗透手段和 cve 漏洞
            * [DesktopApps-Exploits](./1earn/Security/RedTeam/软件服务安全/DesktopApps-Exploits.md) - 收集桌面软件的渗透手段和 cve 漏洞
        * 协议安全
            * [Protocol-Exploits](./1earn/Security/RedTeam/协议安全/Protocol-Exploits.md) - 按照协议归类各种漏洞、攻击手段
            * [笔记](https://github.com/No-Github/1earn/tree/master/1earn/Security/RedTeam/%E5%8D%8F%E8%AE%AE%E5%AE%89%E5%85%A8/%E7%AC%94%E8%AE%B0)
        * 信息收集
            * [端口安全](./1earn/Security/RedTeam/信息收集/端口安全.md) - 记录端口渗透时的方法和思路
            * [空间测绘](./1earn/Security/RedTeam/信息收集/空间测绘.md) - 收集搜索引擎语法资源
            * [信息收集](./1earn/Security/RedTeam/信息收集/信息收集.md) - 记录信息收集方面各类技术，如漏扫、IP 扫描、端口扫描、DNS 枚举、目录枚举、指纹等
        * 语言安全
            * [语言安全](https://github.com/No-Github/1earn/tree/master/1earn/Security/RedTeam/%E8%AF%AD%E8%A8%80%E5%AE%89%E5%85%A8)
        * 云安全
            * [云安全](./1earn/Security/RedTeam/云安全/云安全.md) - 云主机利用工具,渗透案例,相关知识点
        * OS安全
            * [Linux安全](./1earn/Security/RedTeam/OS安全/Linux安全.md) - 包含 Linux 口令破解，漏洞利用、获取Shell
            * [OS-Exploits](./1earn/Security/RedTeam/OS安全/OS-Exploits.md) - 收集操作系统的 cve 漏洞
            * [Windows安全](./1earn/Security/RedTeam/OS安全/Windows安全.md) - 包含 windows pth、ptt，漏洞利用、提权、远程执行命令
            * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/RedTeam/OS%E5%AE%89%E5%85%A8/%E5%AE%9E%E9%AA%8C)
        * Web 安全
            * [前端攻防](./1earn/Security/RedTeam/Web安全/前端攻防.md) - 前端解密,绕过访问
            * [BS-Exploits](./1earn/Security/RedTeam/Web安全/BS-Exploits.md) - 全面收集 web 漏洞 POC | Payload | exp
            * [IDOR](./1earn/Security/RedTeam/Web安全/IDOR.md) - 整个部分结构大部分基于乌云的几篇密码找回、逻辑漏洞类文章,在其基础上记录和归纳
            * [靶场](https://github.com/No-Github/1earn/tree/master/1earn/Security/RedTeam/Web%E5%AE%89%E5%85%A8/%E9%9D%B6%E5%9C%BA)
            * [Web_Generic](https://github.com/No-Github/1earn/tree/master/1earn/Security/RedTeam/Web%E5%AE%89%E5%85%A8/Web_Generic)
            * [Web_Tricks](https://github.com/No-Github/1earn/tree/master/1earn/Security/RedTeam/Web%E5%AE%89%E5%85%A8/Web_Tricks)

    * **Reverse**
        * [Reverse](./1earn/Security/Reverse/Reverse.md)
        * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Security/Reverse/%E5%AE%9E%E9%AA%8C)
        * [FILE](https://github.com/No-Github/1earn/tree/master/1earn/Security/Reverse/FILE)

* **Develop**

    * **版本控制**
        * [Git学习笔记](./1earn/Develop/版本控制/Git学习笔记.md) - 记录 git 的用法和平时使用 github 遇到的问题

    * **标记语言**
        * [HTML](https://github.com/No-Github/1earn/tree/master/1earn/Develop/%E6%A0%87%E8%AE%B0%E8%AF%AD%E8%A8%80/HTML)
        * [JSON](https://github.com/No-Github/1earn/tree/master/1earn/Develop/%E6%A0%87%E8%AE%B0%E8%AF%AD%E8%A8%80/JSON)
        * [XML](https://github.com/No-Github/1earn/tree/master/1earn/Develop/%E6%A0%87%E8%AE%B0%E8%AF%AD%E8%A8%80/XML)

    * **可视化**
        * [gnuplot](https://github.com/No-Github/1earn/tree/master/1earn/Develop/%E5%8F%AF%E8%A7%86%E5%8C%96/gnuplot)

    * **正则**
        * [regex](./1earn/Develop/正则/regex.md) - 常用正则表达式和相关资源

    * **Web**
        * [Speed-Web](./1earn/Develop/Web/Speed-Web.md)
        * [HTTP](https://github.com/No-Github/1earn/tree/master/1earn/Develop/Web/HTTP)
        * [笔记](https://github.com/No-Github/1earn/tree/master/1earn/Develop/Web/%E7%AC%94%E8%AE%B0)

* **Integrated**

    * **数据库**
        * [Power-SQL](https://github.com/No-Github/1earn/blob/master/1earn/Integrated/%E6%95%B0%E6%8D%AE%E5%BA%93/Power-SQL.md)
        * [Speed-SQL](https://github.com/No-Github/1earn/blob/master/1earn/Integrated/%E6%95%B0%E6%8D%AE%E5%BA%93/Speed-SQL.md)
        * [笔记](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%AC%94%E8%AE%B0)
        * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/%E6%95%B0%E6%8D%AE%E5%BA%93/%E5%AE%9E%E9%AA%8C)

    * **虚拟化**
        * [Docker](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/%E8%99%9A%E6%8B%9F%E5%8C%96/Docker)

    * **Linux**
        * [God-Linux](./1earn/Integrated/Linux/God-Linux.md) - 记录 Linux 下的骚操作,收集的较少,后面会慢慢添加
        * [Power-Linux](./1earn/Integrated/Linux/Power-Linux.md) - 配置指南,记录各种服务搭建与配置过程
        * [Secure-Linux](./1earn/Integrated/Linux/Secure-Linux.md) - Linux 加固+维护+应急响应参考
        * [Speed-Linux](./1earn/Integrated/Linux/Speed-Linux.md) - 命令速查手册,记录各种基本命令操作
        * [笔记](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/Linux/%E7%AC%94%E8%AE%B0)
        * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/Linux/%E5%AE%9E%E9%AA%8C) - 各种 linux 服务的搭建过程和案例

    * **Network**
        * [不同厂商](./1earn/Integrated/Network/不同厂商.md) - 记录不同厂商配置服务命令的区别
        * [方向实验](./1earn/Integrated/Network/方向实验.md) - 按方向分类记录配置
        * [速查](./1earn/Integrated/Network/速查.md) - 速查各类帧、报文格式、掩码等
        * [SDN笔记](./1earn/Integrated/Network/SDN笔记.md) - 记录以前比赛时 SDN 的题目和命令
        * [TCP-IP](./1earn/Integrated/Network/TCP-IP.md) - 记录 TCP/IP 协议栈的协议
        * [VPN-Security](./1earn/Integrated/Network/VPN-Security.md) - 记录 VPN 领域的协议

    * **Windows**
        * [Secure-Win](./1earn/Integrated/Windows/Secure-Win.md) - Windows 加固+维护+应急响应参考
        * [Speed-Win](./1earn/Integrated/Windows/Speed-Win.md) - 记录 windows 下 CMD 常用命令
        * [笔记](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/Windows/%E7%AC%94%E8%AE%B0)
        * [实验](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/Windows/%E5%AE%9E%E9%AA%8C) -涉及域环境搭建、基础服务搭建
        * [Powershell](https://github.com/No-Github/1earn/tree/master/1earn/Integrated/Windows/PowerShell)

* **Plan**

    * [Misc-Plan](./1earn/Plan/Misc-Plan.md) - 各种小技巧
    * [Team-Plan](./1earn/Plan/Team-Plan.md) - 团队协作解决方案
    * [Thinking-Plan](./1earn/Plan/Thinking-Plan.md) - 问题解决方式的记录和学习
    * [VM-Plan](./1earn/Plan/VM-Plan.md) - VMWare 常见问题记录

---

## 三板斧

`收集、归纳、分享` 我认为这是知识学习的"三板斧"

收集,很好理解,比如收集各种学习的资源,看过的论文、文章,和各种工具

归纳,或者说是总结与分类,将自己学习过程中的心得体会记载下来,写成各种笔记,文章,将收集的资源整理归类

分享,在博客上传一篇文章也好,在 qq 群帮助群友解决一个问题也好,都是分享

没有收集和归纳的能力,整个学习的过程就像是在用一个菜篮子接水,留不住的,同样,如果不愿意分享,就像是在闭门造车,无法接触到不同的观点,没人指正你的问题,久而久之有可能想法变得偏执,并且固步自封

---

## 阅读建议

`本项目所有文档均在 VScode 编辑器中编写,故只兼容 VScode 侧边预览的 markdown 语法,暂不考虑兼容其他编辑器的 md 语法`

~~由于 github 的 markdown 引擎 kramdown 不支持 [TOC] 链接,以及各种不兼容的排版问题, 导致阅读体验极不友好, 因此~~ 建议还是下载/clone到本地阅读
```
git clone --depth 1 https://github.com/ffffffff0x/1earn.git
```

建议的阅读体验
* [VScode](https://code.visualstudio.com/) + [FiraCode](https://github.com/tonsky/FiraCode) (推荐,整个项目在vscode环境下编写,基本不会出现排版问题)
* [Typora](https://www.typora.io/)

> 如果 clone 速度太慢,可以先导入码云中(选择从 URL 中导入),再进行 clone ： https://blog.gitee.com/2018/06/05/github_to_gitee/?from=homepage

> 提高 release 速度,可以参考这几篇文章 https://jinfeijie.cn/post-805.html 、https://blog.csdn.net/weixin_44821644/article/details/107574297?utm_source=app

> 现在只需按下句号(.)键，即可启用 web 版 vscode 浏览本项目

---

以下是该项目的灵感来源

* [Micro8-渗透沉思录](https://www.secpulse.com/archives/98814.html)
* [Teach Yourself Programming in Ten Years](http://norvig.com/21-days.html)
* [To Find a Better Solution, Ask a Better Question  Member Feature Stories  Medium](https://medium.com/s/story/to-find-a-better-solution-ask-a-better-question-3be7fee5af65)
* [The Magpie Developer](https://blog.codinghorror.com/the-magpie-developer/)

---

## Attributions&Thanks

- [CONTRIBUTORS](./assets/CONTRIBUTORS.md)

---

## 联系我

- 如果你有任何其他方面的问题或建议，可以在 issue 提出或发送邮件至 D2hwakH7BS5E@protonmail.com

---

## Disclaimer&License

- <sup>本项目采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议.</sup>
    - <sup>共享 — 在任何媒介以任何形式复制、发行本作品。</sup>
    - <sup>演绎 — 修改、转换或以本作品为基础进行创作在任何用途下，甚至商业目的。</sup>
    - <sup>署名 — 您必须给出适当的署名，提供指向本许可协议的链接，同时标明是否（对原始作品）作了修改。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。</sup>
    - <sup>没有附加限制 — 您不得适用法律术语或者 技术措施 从而限制其他人做许可协议允许的事情。</sup>
- <sup>注: 本项目所有文件仅供学习和研究使用,请勿使用项目中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.</sup>

---

> create by ffffffff0x
