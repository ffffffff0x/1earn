# CTF

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 大纲

* **[大型赛事Writeup](#大型赛事writeup)**
    * [部委&公安&网信](#部委&公安&网信)
        * [CNAS](#CNAS)
        * [ISG](#ISG)
        * [虎符杯](#虎符杯)
        * [强网杯](#强网杯)
        * [网鼎杯](#网鼎杯)
        * [羊城杯](#羊城杯)
        * 2020
    * [高校](#高校)
        * [CISCN](#ciscn)
        * 2020
        * 2019
        * 2018
        * 2016
    * [公司&行业](#公司&行业)
        * [XCTF](#xctf)
        * [DASCTF](#dasctf)
        * 2020
        * 2019
        * 2018
    * [国外](#国外)
        * 2020
        * 2019
        * 2016
    * [未分类](#未分类)
        * [GXYCTF](#gxyctf)

---

**平台**
- https://www.ichunqiu.com/battalion?t=1
- http://ctf.bugku.com/
- http://www.hetianlab.com/CTFrace.html
- https://www.wechall.net/
- https://ctftime.org/
- https://pwnhub.cn/index
- http://hackinglab.cn/
- https://new.bugku.com/
- https://buuoj.cn/

**学习资源**
- https://ctf-wiki.github.io/ctf-wiki/
- https://trailofbits.github.io/ctf/
- https://l1nwatch.gitbooks.io/ctf/content/
- https://yq.aliyun.com/articles/333082
- https://www.peerlyst.com/posts/ctf-write-ups-wiki-peerlyst
- https://github.com/L1nwatch/CTF
- https://ctf-wiki.github.io/ctf-wiki/misc/introduction-zh/

**工具合集**
- [zardus/ctf-tools](https://github.com/zardus/ctf-tools) - 安全研究工具的一些设置脚本。

**比赛经验**

团队协作，并灵活分工，选择自己擅长的，能做的。

看自己的侧重方向：
- WEB: WEB+MISC+CRYPTO
- PWN: PWN+REVERSE

如何稳定提分:
- 尽量拿高分，解不出来就跳过换下一个
- 学到东西，没弄懂的赛后弄懂
- 按题型攻克

快速学习的途径:
- 收集、复现各类比赛的 writeup(解题思路)
- 在各类平台上刷题，不断参与挑战各类 CTF 比赛

CTF
- Web
    - SQL
    - SSRF
    - SSTI

- Misc
    - 流量分析
    - 磁盘取证
    - 内存取证

- Crypto
    - 基本每场都有 RSA,不多说了

AWD
- 流量监控很重要, 注意观察其他队伍的 POC

办比赛的角度
1. 现场准备 Type C 转网卡的转换器，有大量轻薄本不自带网口需要转接器
2. 准备口罩、消毒液
3. 提前规划好静态、动态 flag
4. 尽量统一 flag 格式
5. 网段隔离
6. 信号屏蔽器、无线dos
7. 如果是需要自己拼出来的flag,尽量不要用 leet 形式

---

# 赛事运营

## AWD

**平台搭建**
- [mo-xiaoxi/AWD_CTF_Platform](https://github.com/mo-xiaoxi/AWD_CTF_Platform) - 一个简单的 AWD 训练平台
    - https://www.cnblogs.com/p201821440039/p/12290724.html
- [D0g3-Lab/H1ve](https://github.com/D0g3-Lab/H1ve) - An Easy / Quick / Cheap Integrated Platform
    - https://www.freebuf.com/sectool/221739.html
- [zhl2008/awd-platform](https://github.com/zhl2008/awd-platform) - platform for awd
    - https://mp.weixin.qq.com/s/ffh-Jkt9UUKHErxeUMw4aw
    - https://www.cnblogs.com/Triangle-security/p/11332223.html

**相关文章**
- [聊聊AWD攻防赛流程及准备经验](https://www.freebuf.com/articles/network/201222.html)

---

# 大型赛事Writeup

**赛事安排**
- https://ctftime.org/event/list/
- https://www.ichunqiu.com/competition/all?source=1

---

## 部委&公安&网信

### CNAS

**2018**
- [2018年CNAS网络安全等级保护测评能力验证与攻防大赛writeup](http://www.jdicsp.org/xinwengonggao/gongsixinwen/20181023/16.html)

**2017**
- [2017年CNAS网络安全等级保护测评能力验证与攻防大赛部分题目writeup](https://freewechat.com/a/MzIyNTI0ODcwMw==/2662122981/1)

---

### ISG

**2018**
- [ISG 2018 Web Writeup ](https://www.freebuf.com/articles/network/183413.html)

---

### 虎符杯

**2020**
- [虎符杯两道NodeJS题目的分析](https://xz.aliyun.com/t/7714)
- [数字中国创新大赛-虎符网络安全赛道Write up](https://mp.weixin.qq.com/s/ih2X8IXVFmrMVwJYuf5gng)
- [虎符 CTF Web 部分 Writeup](https://www.zhaoj.in/read-6512.html)

---

### 强网杯

**2019**
- [2019 第三届强网杯 Web 部分 WriteUp + 复现环境](https://www.zhaoj.in/read-5873.html)
- [强网杯Web部分writeup](https://www.freebuf.com/articles/network/205789.html)

**2019 广东强网杯**
- [2019广东强网杯Writeup(MISC)](https://sec.thief.one/article_content?a_id=bd1f559d1f0ddfe66b69d767a0b6cb5a)
- [广东省第三届强网杯Writeup](https://www.hotbak.net/key/2019%E5%B9%BF%E4%B8%9C%E5%BC%BA%E7%BD%91%E6%9D%AFWriteupMISC.html)

**2019 强网杯拟态挑战赛**
- [MIMIC Defense CTF 2019 final writeup](https://paper.seebug.org/932/)

---

### 网鼎杯

**2020**
- 青龙组
    - [2020网鼎杯青龙组部分wp](https://www.52pojie.cn/thread-1176169-1-1.html)
    - [2020网鼎杯第一场Crypto题解](https://blog.csdn.net/cccchhhh6819/article/details/106038866/)
    - [网鼎杯2020青龙组 web writeup](https://www.xuenixiang.com/thread-2208-1-1.html)
    - [网鼎杯 2020 Web Writeup](https://www.xmsec.cc/wang-ding-bei-2020-web-writeup/)
    - [网鼎杯 2020 第一场 signal writeup](http://dreamcracker.today/2020/05/11/%e7%bd%91%e9%bc%8e%e6%9d%af-2020-%e7%ac%ac%e4%b8%80%e5%9c%ba-signal-writeup/)
    - [2020-网鼎杯(青龙组)-Web题目-AreUserialz Writeup](https://mp.weixin.qq.com/s/16QfU8lZYChSckJWtcLiqg)
    - [网鼎杯-青龙组web题目writeup](https://mp.weixin.qq.com/s/E-lRUm1zPkEIxSoV7cHfow)
    - [2020网鼎杯青龙组_re_signal](https://mp.weixin.qq.com/s/uI2nLuM1K-J-fWBA-5Z7Zw)
    - [2020网鼎杯 青龙组 Android逆向题 rev01 WP](https://mp.weixin.qq.com/s/st6w3ax_DLHhd-AK5F509g)
    - [2020-网鼎杯(青龙组)_Web题目 FileJava Writeup](https://www.t00ls.net/viewthread.php?tid=56351&highlight=writeup)
    - [2020年第二届“网鼎杯”-网络安全大赛青龙组writeup](https://blog.fullstackpentest.com/2020-wang-ding-bei-writeup.html)

- 白虎组
    - [2020年第二届“网鼎杯”网络安全大赛 白虎组 部分题目Writeup](https://codingnote.cc/p/113802)
    - [网鼎杯2020白虎组Reverse-py,恶龙,幸运的数字 WP](https://www.52pojie.cn/thread-1180352-1-1.html)
    - [网鼎杯2020白虎组Crypto-rand,b64 WP](https://www.52pojie.cn/thread-1180315-1-1.html)
    - [网鼎杯2020白虎组web-picdown,张三的网站,starbucket WP](https://www.52pojie.cn/thread-1180274-1-1.html)
    - [网鼎杯2020白虎组misc-hidden,密码柜,boot WP](https://www.52pojie.cn/thread-1180202-1-1.html)
    - [网鼎杯2020白虎组misc-hack WP](https://www.52pojie.cn/thread-1180008-1-1.html)
    - [[原创]网鼎杯2020 白虎组 【恶龙】 解题](https://bbs.pediy.com/thread-259532.htm)
    - [网鼎杯CTF——白虎组 (week 4) ](https://l0x1c.github.io/2020/05/15/2020-5-14/#HERO)
    - [[原创]网鼎杯2020 白虎组 CY 解题](https://bbs.pediy.com/thread-259529.htm)
    - [网鼎杯白虎组部分题目复盘](https://www.secquan.org/Notes/1071122)
    - [网鼎杯2020白虎组Misc题目hidden总结](https://mp.weixin.qq.com/s/G1NttGYTUsQ1i8wNJQ667g)
    - [网鼎杯-白虎组web题目writeup](https://mp.weixin.qq.com/s/v2C4BtZSYJDT64_ByrDhoA)
    - [2020网鼎杯白虎组re 恶龙 wp](https://www.52pojie.cn/thread-1181663-1-1.html)

- 朱雀组
    - [2020网鼎杯朱雀组云顿WP(入门向)](https://mp.weixin.qq.com/s/TpKXezPMZLx3VlejxlFyiQ)
    - [【网鼎杯2020朱雀组】Web WriteUp](https://www.cnblogs.com/vege/p/12907941.html)
    - [[re]go语言逆向：2020网鼎杯朱雀组re what wp](https://blog.csdn.net/Breeze_CAT/article/details/106195499)
    - [2020网鼎杯朱雀组_PHPweb](https://blog.csdn.net/gd_9988/article/details/106181577)
    - [2020网鼎杯-朱雀组-部分wp](https://www.anquanke.com/post/id/205578)
    - [2020网鼎杯-朱雀组部分题目Writeup](https://www.kkzevip.com/?post=51)
    - [2020网鼎杯-朱雀组-Crypto、Misc(带视频) ](https://mp.weixin.qq.com/s/XYkgD_5Y0FcgsNqRAb_1Yw)
    - [2020网鼎杯朱雀组逆向2 tree](https://www.52pojie.cn/thread-1181476-1-1.html)

- 玄武组
    - [网鼎杯2020-玄武组签到题](https://blog.csdn.net/slavik_/article/details/106264509)
    - [网鼎杯玄武组部分web题解](https://mp.weixin.qq.com/s/Kr2AlygNpeM7UYiLPINcrA)
    - [网鼎杯-玄武组-writeup-简单思路讲究](https://mp.weixin.qq.com/s/PlpG6maNObxvRaXuaVSwIA)
    - [2020网鼎杯玄武组_babyvm](https://bbs.pediy.com/thread-259714.htm)
    - [2020网鼎杯玄武组部分题writeup（签到/vulcrack/java/js_on）](https://blog.csdn.net/w1590191166/article/details/106314499/)
    - [2020网鼎杯-玄武组-部分WriteUp](https://mp.weixin.qq.com/s/xNDUYkxCIEJuvHJWQwtflw)
    - [【CTF】网鼎杯【玄武组】CTF部分题](https://blog.csdn.net/God_XiangYu/article/details/106306773)

**2018**
- 青龙组
    - [【2018年 网鼎杯CTF 第一场】China H.L.B “网鼎杯” 部分WriteUp ](https://xz.aliyun.com/t/2611)
    - [【2018年 网鼎杯CTF 第一场】Web 题解 ](https://xz.aliyun.com/t/2607)
    - [ 网鼎杯2018第一场WEB&Misc WP ](https://v0w.top/2018/08/20/%E7%BD%91%E9%BC%8E%E6%9D%AF2018%E7%AC%AC%E4%B8%80%E5%9C%BAWEB&Misc%20WP/)
    - [2018网鼎杯部分WriteUp](https://cyto.top/2018/08/21/writeup-2018wangdingbei/)
    - [【2018年 网鼎杯CTF 第一场】教育组 WP — Lilac ](https://xz.aliyun.com/t/2608)
    - [2018网鼎杯第1场](https://github.com/hongriSec/CTF-Training/tree/master/2018/2018%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%AC%AC1%E5%9C%BA)

- 白虎组
    - [网鼎杯第二场wp](https://www.o2oxy.cn/1688.html)
    - [网鼎杯 2018 game writeup](http://dreamcracker.today/2020/05/12/%e7%bd%91%e9%bc%8e%e6%9d%af-2018-game-writeup/)
    - [“网鼎杯”第二场Write up](https://www.smi1e.top/%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%AC%AC%E4%BA%8C%E5%9C%BAwrite-up/)
    - [2018网鼎杯第2场](https://github.com/hongriSec/CTF-Training/tree/master/2018/2018%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%AC%AC2%E5%9C%BA)

- 朱雀组
    - [网鼎杯第三场wp](https://www.o2oxy.cn/1753.html)
    - [“网鼎杯”第三场Write up](https://www.smi1e.top/%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%AC%AC%E4%B8%89%E5%9C%BAwrite-up/)
    - [180828 逆向-网鼎杯（3-2）](https://blog.csdn.net/whklhhhh/article/details/82150041)
    - [2018网鼎杯第3场](https://github.com/hongriSec/CTF-Training/tree/master/2018/2018%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%AC%AC3%E5%9C%BA)

- 玄武组
    - [网鼎杯 第四场 部分WriteUp](https://www.anquanke.com/post/id/158386)
    - [网鼎杯第四场 shenyue2 writeup](https://www.secshi.com/16267.html)
    - [网鼎杯第四场wp](https://www.o2oxy.cn/1817.html)
    - [网鼎杯 2018 dalao writeup](http://dreamcracker.today/2020/05/13/%e7%bd%91%e9%bc%8e%e6%9d%af-2018-dalao-writeup/)
    - [2018网鼎杯第4场](https://github.com/hongriSec/CTF-Training/tree/master/2018/2018%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%AC%AC4%E5%9C%BA)

- 线下赛
    - [2018网鼎杯线下赛](https://github.com/hongriSec/CTF-Training/tree/master/2018/2018%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%BA%BF%E4%B8%8B%E8%B5%9B)

---

### 羊城杯

**2020**
- [羊城杯-Reverse-WP](https://www.zrzz.site/2020/09/11/%E7%BE%8A%E5%9F%8E%E6%9D%AF-Reverse-WP/)
- [羊城杯Easy Java题解](https://zhzhdoai.github.io/2020/09/11/%E7%BE%8A%E5%9F%8E%E6%9D%AFEasy-Java%E9%A2%98%E8%A7%A3/)

### 美亚杯

**2020**
- [20年美亚杯个人赛-Alice LG Phone部分WRITE UP](https://www.cnblogs.com/zhwyyswdg/p/14008424.html)
- [20年美亚杯个人赛-ALICE_USB部分WRITE UP](https://www.cnblogs.com/zhwyyswdg/p/14011629.html)
- [20年美亚杯个人赛-Alice_Laptop部分WRITE UP](https://www.cnblogs.com/zhwyyswdg/p/14006353.html)
- [20年美亚杯WRITE UP](https://www.cnblogs.com/zhwyyswdg/p/14006162.html)

**2018**
- [18年美亚杯团体赛-C部分 WRITE UP](https://www.cnblogs.com/zhwyyswdg/p/14002475.html)
- [18年美亚杯团体赛-B部分 WRITE UP](https://www.cnblogs.com/zhwyyswdg/p/14001433.html)

**2017**
- [电子取证 | 第三届美亚杯（2017）个人赛题解](https://www.cnblogs.com/zhwer/p/12230189.html)

---

### 2020

**宁波市第三届网络安全大赛**
- [宁波市第三届网络安全大赛线上赛部分题目-writeup](https://blog.csdn.net/qq_45628145/article/details/107183635)
- [2020宁波市第三届网络安全大赛 Web Writeup](https://www.cnblogs.com/skyxmao/p/13262594.html)
- [宁波市第三届网络安全大赛-WriteUp（Misc）](https://codingnote.cc/p/150404)

**2020 “第五空间”智能安全大赛**
- [2020 “第五空间”智能安全大赛初赛两道 RE 解题报告（writeup）](https://hx1997.github.io/2020/06/25/5space-2020-re-writeup/)
- [2020第五空间Final](https://blog.szfszf.top/article/47/)

---

## 教育

### CISCN

**2020**
- [CTF | 2020 CISCN初赛 Z3&LFSR WriteUp](https://miaotony.xyz/2020/08/27/CTF_2020CISCN_preliminary/)
- [2020CISCN-初赛Web](https://jwt1399.top/posts/17919.html)

**2019**
- [CISCN 2019 东北赛区 Day2 Web3 WriteUp](https://www.zhaoj.in/read-6057.html)
- [CISCN 2019 华东北赛区 Web2 WriteUp](https://www.zhaoj.in/read-6100.html)
- [全国第十二届大学生信息安全竞赛 线上初赛 Web 部分 WriteUp](https://www.zhaoj.in/read-5417.html)
- [CISCN 华北赛区 Day1 Web2 WriteUp](https://www.zhaoj.in/read-5946.html)

---

### 2020

**2020 NUAACTF**
- [CTF | 2020 NUAACTF 吸喵喵队 Writeup](https://miaotony.xyz/2020/05/30/CTF_2020NUAACTF/)

**2020 BJDCTF**
- [CTF | BJDCTF 2nd WriteUp](https://miaotony.xyz/2020/03/23/CTF_BJDCTF2nd/)
- [BJDCTF 2nd EasyAspDotNet WriteUp](https://www.zhaoj.in/read-6497.html)

**2020 Ha1cyon_CTF**
- [CTF | 2020 Ha1cyon_CTF公开赛 WriteUp](https://miaotony.xyz/2020/04/21/CTF_2020Ha1cyonCTF/)

**2020 WHUCTF**
- [WHUCTF2020出题记录](https://blog.szfszf.top/article/43/)

### 2019

**2019 “应急挑战杯”大学生网络安全大学生网络安全邀请赛**
- [“应急挑战杯”大学生网络安全大学生网络安全邀请赛复盘](https://www.zhaoj.in/read-5525.html)

**2019 HDCTF**
- [HDCTF 2019 部分题目 WriteUp](https://www.zhaoj.in/read-5548.html)

**2019 GUET-CTF**
- [GUET-CTF 题目备份](https://www.zhaoj.in/read-5851.html)

**2019 ISCC**
- [ISCC 2019 部分题目 WriteUp](https://www.zhaoj.in/read-5629.html)

**湖南省第三届大学生信息安全技能竞赛**
- [湖南省第三届大学生信息安全水赛WriteUp](https://gksec.com/HNCTF2019-Final.html)

### 2018

**2018 HCTF**
- [2018 HCTF Web Writeup](https://skysec.top/2018/11/12/2018-HCTF-Web-Writeup/)
- [HCTF 2018 Official Writeup](https://www.secpulse.com/archives/82690.html)
- [HCTF 2018 WriteUp](https://impakho.com/post/hctf-2018-writeup)
- [HCTF 2018 Writeup](https://xz.aliyun.com/t/3242)

**2018“骇极杯”上海大学生网络安全大赛**
- [2018“骇极杯”上海大学生网络安全大赛 Web题解](https://blog.szfszf.top/article/13/)

### 2016

**2016 HCTF**
- [HCTF 2016网络攻防大赛官方Writeup](https://www.freebuf.com/articles/web/121778.html)

---

## 公司&行业

### XCTF

**2020 wmctf**
- [Nobody knows BaoTa better than me WriteUp](https://www.zhaoj.in/read-6660.html)
- [W&MCTF_Dalabengba](http://www.fzwjscj.xyz/index.php/archives/37/)
- [W&MCTF](http://wh1sper.cn/wmctf/)
- [W&MCTF-0RAYS](https://www.anquanke.com/post/id/212809)

**2020 高校战“疫”**
- [CTF | XCTF高校战“疫”网络安全分享赛 WriteUp](https://miaotony.xyz/2020/03/15/CTF_2020XCTF_gxzy/)
- [i春秋2020新春战“疫”网络安全公益赛GYCTF 两个 NodeJS 题 WriteUp](https://www.zhaoj.in/read-6462.html)

**2020 De1CTF**
- [CTF | 2020 De1CTF Misc Chowder WriteUp](https://miaotony.xyz/2020/05/04/CTF_2020De1CTF/)

**2020 GACTF**
- [CTF | 2020 GACTF 一点点WriteUp](https://miaotony.xyz/2020/08/31/CTF_2020GACTF/)
- [GACTF-WriteUp](https://mp.weixin.qq.com/s/uL2yEuSKJGNWGaNYsQIjsg)

**2020 SCTF**
- [SCTF 2020 Login Me Aagin WriteUp](https://www.zhaoj.in/read-6617.html)

**2020 RCTF**
- [[CTF]2020RCTF Swoole题解学习笔记](https://zhzhdoai.github.io/2020/06/02/CTF-2020RCTF-Swoole%E9%A2%98%E8%A7%A3%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)

**2019 SCTF**
- [SCTF2019 部分题目WriteUp](https://www.zhaoj.in/read-5985.html)

**2019 RCTF**
- [RCTF2019 jail WriteUp](https://blog.szfszf.top/article/31/)

**2019 De1CTF**
- [De1CTF2019 官方Writeup(Web/Misc) -- De1ta](https://xz.aliyun.com/t/5945)
- [De1CTF Web WriteUp](https://www.zhaoj.in/read-6170.html)

**2018 赛博地球杯工业互联网安全大赛**
- [“赛博地球杯”工业互联网安全大赛线上赛Writeup](https://www.xctf.org.cn/library/details/cyberearth-writeup/)
- [2018 XCTF-赛博地球杯工业互联网安全大赛web部分题解](https://skysec.top/2018/01/18/XCTF-%E8%B5%9B%E5%8D%9A%E5%9C%B0%E7%90%83%E6%9D%AF%E5%B7%A5%E4%B8%9A%E4%BA%92%E8%81%94%E7%BD%91%E5%AE%89%E5%85%A8%E5%A4%A7%E8%B5%9Bweb%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3/)

**2017 WHCTF**
- [WHCTF官方Writeup](https://www.xctf.org.cn/library/details/whctf-writeup/)

---

### DASCTF

**20.8**
- [DASCTF 八月赛 Crypto 部分Writeup](https://www.anquanke.com/post/id/215484)
- [DASCTF八月赛学习](https://troyess.com/2020/09/07/DASCTF%E5%85%AB%E6%9C%88%E8%B5%9B%E5%AD%A6%E4%B9%A0/)
- [DASCTF八月赛 Web Writeup](https://ca0y1h.top/Web_security/ctf_writeup/23.DASCTF2020%E5%85%AB%E6%9C%88%E8%B5%9B/)
- [单身狗的七夕——安恒8月赛](http://www.fzwjscj.xyz/index.php/archives/38/)

**20.7**
- [DASCTF-7月赛](http://www.nopnoping.xyz/2020/07/25/DASCTF-7%E6%9C%88%E8%B5%9B/)
- [Dasctf 2020 07 pwn wp](https://ay3.ink/dasctf-2020-07-pwn-wp/)
- [DASCTF七月-虚假的签到题](https://www.jianshu.com/p/f3b4aaa4d357)
- [[DASCTF 2020.7]Write up](https://ha1c9on.top/2020/07/25/dasctf-2020-7write-up/)
- [[原创]DASCTF七月赛部分wp](https://bbs.pediy.com/thread-260967.htm)
- [DASCTF 7月赛部分write up](https://www.cnblogs.com/MisakaYuii-Z/p/13379712.html)
- [安恒七月赛——QRJoker](http://www.fzwjscj.xyz/index.php/archives/36/)

**20.6**
- [安恒6月月赛 DASCTF 6th Re 部分wp](https://blog.csdn.net/a_touhouer/article/details/106982172)
- [每日一练之"DASCTF 2020 6th Wp"](https://www.zrzz.site/2020/08/02/DASCTF-2020-6th-Wp/)
- [DASCTF 六月团队赛](https://lazzzaro.github.io/2020/06/26/match-DASCTF-%E5%85%AD%E6%9C%88%E5%9B%A2%E9%98%9F%E8%B5%9B/)
- [DASCTF六月团队赛(2020)-部分WP](https://blog.csdn.net/hiahiachang/article/details/106974553)

**20.5**
- [ [CTF]DASCTF五月三道逆向题](https://www.buaq.net/go-27321.html)
- [DASCTF五月月赛 暨 BJDCTF 3rd 部分WP](https://www.anquanke.com/post/id/206493)
- [DASCTF 5月 Re - ViQinere](https://blog.csdn.net/T_Luffy/article/details/106321561)
- [2020年DASCTF五月线上赛-ViQinere](https://blog.csdn.net/pkcjl/article/details/106327862)
- [[2020 DASCTF] 五月线上赛 - 部分 Web、Misc WriteUp](http://c0r1.com/2020/05/23/2020-DASCTF-%E4%BA%94%E6%9C%88%E7%BA%BF%E4%B8%8A%E8%B5%9B-%E9%83%A8%E5%88%86-Web%E3%80%81Misc-WriteUp/)
- [BJD3rd Test your nc 出题笔记 | DASCTF 安恒5月赛](http://taqini.space/2020/05/28/bjd3rd-testyournc/)
- [DASCTF May × BJDCTF 3rd 安恒五月赛](https://lazzzaro.github.io/2020/05/24/match-DASCTF-May-%C3%97-BJDCTF-3rd-%E5%AE%89%E6%81%92%E4%BA%94%E6%9C%88%E8%B5%9B/index.html)
- [DASCTF五月线上赛 BScript blink](https://www.cnblogs.com/harmonica11/p/12943773.html)
- [[原创][CTF]DASCTF五月部分逆向题.](https://bbs.pediy.com/thread-259707.htm)
- [安恒/DASCTF五月月赛&BJD3rd的wp及赛后复现（pwn部分）](https://www.1p0ch.cn/2020/05/24/%E5%AE%89%E6%81%922020%E5%B9%B45%E6%9C%88%E6%9C%88%E8%B5%9Bwp%E5%8F%8A%E5%A4%8D%E7%8E%B0/)
- [CTF | DASCTF May & BJDCTF3rd 部分WriteUp](https://miaotony.xyz/2020/05/24/CTF_BJDCTF3rd/)

**20.4**
- [CTF系列——DASCTF四月春季赛Writeup](https://cloud.tencent.com/developer/article/1625598)
- [CTF | 2020 DASCTF 四月春季战 Re&Misc WriteUp](https://miaotony.xyz/2020/04/25/CTF_2020DASCTF_April/)
- [安恒月赛2020年DASCTF——四月春季赛---Web-Writeup](https://blog.csdn.net/SopRomeo/article/details/105849403)
- [安恒月赛2020年DASCTF——四月春季战Writeup](https://www.gem-love.com/ctf/2275.html)

**19.7**
- [安恒七月月赛](https://jwt1399.top/posts/49404.html)

**19.6**
- [安恒杯6月赛web2 easypentest](https://blog.szfszf.top/article/33/)

**19.2**
- [2019安恒2月月赛Writeip-Web&Crypto&Misc](https://www.anquanke.com/post/id/171543)

**19.1**
- [安恒月赛mycard exp编写及详细分析](https://www.anquanke.com/post/id/170359)
- [2019安恒1月月赛Writeip-Web&Crypto&Misc](https://www.anquanke.com/post/id/170341)

**18.11**
- [2018安恒杯11月赛-Web&Crypto题解](https://www.anquanke.com/post/id/166492)

**18.9**
- [2018安恒杯 - 9月月赛Writeup](https://www.anquanke.com/post/id/160582)

---

### 2020

**2020 0CTF/TCTF**
- [0CTF/TCTF 2020 wp](https://blog.szfszf.top/article/46/)

**2020 DDCTF**
- [DDCTF-WriteUp](https://mp.weixin.qq.com/s/gtzWFiZprbRWFOGTxR47CQ)
- [2020DDCTF WP](https://zyazhb.github.io/2020/09/04/ctf-ddctf/)
- [2020DDCTF-wp](https://wulidecade.cn/2020/09/06/2020DDCTF-wp/)
- [DDCTF](https://iluem.xyz/passagesDDCTF/)

**GeekPwn2020**
- [GeekPwn2020 云安全挑战赛wp](https://blog.szfszf.top/article/45/)

**2020 天翼杯**
- [天翼杯-Re-Wp](https://www.zrzz.site/2020/08/01/%E5%A4%A9%E7%BF%BC%E6%9D%AF-Re-Wp/)
- [天翼杯2020_wp_by_LQers](https://www.freebuf.com/articles/network/245664.html)
- [天翼杯Crypto Write Up](https://www.anquanke.com/post/id/212635)

**2020 中国I²S峰会暨工业互联网安全大赛**
- [2020-11-I²S峰会暨工业互联网安全大赛writeup](https://www.t00ls.net/thread-58518-1-1.html)
- [WriteUp-首届中国I²S峰会暨工业互联网安全大赛](https://mp.weixin.qq.com/s/21pOfgGCmt5ijr66xpV1MA)

---

### 2019

**2019 OPPO OGeek CTF**
- [OPPO OGeek CTF 2019 部分题目 WriteUp](https://www.zhaoj.in/read-6251.html)

**2019 ByteCTF CTF**
- [字节跳动 ByteCTF 2019 Web RSS WriteUp](https://www.zhaoj.in/read-6310.html)

**2019 DDCTF**
- [DDCTF 2019 Web 部分 WriteUp](https://www.zhaoj.in/read-5269.html)
- [DDCTF2019两个逆向writeup ](https://www.freebuf.com/articles/network/202987.html)
- [DDCTF 2019 WriteUp](https://blog.szfszf.top/article/29/)

**2019 RoarCTF**
- [2019 RoarCTF部分题解WriteUp](https://nikoeurus.github.io/2019/10/14/RoarCTF/)
- [Roarctf 部分Writeup](https://www.anquanke.com/post/id/188785)
- [RoarCTF Web writeup](https://github.red/roarctf-web-writeup/)
- [RoarCTF2019 Web WriteUp](https://blog.szfszf.top/article/38/)
- [berTrAM888/RoarCTF-Writeup-some-Source-Code](https://github.com/berTrAM888/RoarCTF-Writeup-some-Source-Code)
- [Carry955/RoarCTF-Writeup-2019](https://github.com/Carry955/RoarCTF-Writeup-2019)

### 2018

**金融业网络安全攻防比赛**
- [金融业网络安全攻防比赛热身赛writeup](https://www.secpulse.com/archives/74096.html)
- [金融业网络安全攻防比赛热身赛writeup](https://mp.weixin.qq.com/s/gwtdAeBy6dKViiZJbgKMSA)
- [金融业网络安全攻防大赛部分题目writeup](https://www.anquanke.com/post/id/154477)

**2018年民航网络安全职业技能竞赛**
- [wrlu/CAAC-CTF-2018-Primary](https://github.com/wrlu/CAAC-CTF-2018-Primary)

---

## 国外

### 2020

**2020 BSidesSF**
- [BSidesSF 2020 CTF writeup](https://zhuanlan.zhihu.com/p/113862487)

**2020 Winja**
- [Winja CTF 2020: Write-up](https://medium.com/bugbountywriteup/winja-ctf-write-up-f33db5ee7afe)

**2020 Zer0pts CTF**
- [Zer0pts CTF 2020的web赛后记录+复现环境](https://mp.weixin.qq.com/s/Wb79jxc3lL6NJGFAJbbhkQ)

**2020 HexionCTF**
- [HexionCTF web&crypto&misc题目分析](https://mp.weixin.qq.com/s/aPxB8SSMBNw-HwLZL5bmWA)

**2020 PlaidCTF**
- [PlaidCTF 2020 Dragon Sector write-ups](https://docs.google.com/document/d/e/2PACX-1vRz1CKXJBbk8e72vveZ17vhA6dn0IV2ENCrLCVNuBIgNXGm9tB7RPrUEkTZ9j7GTfScRcJ8ag8_oAGs/pub)
- [Plaid CTF 2020 Catalog](https://blog.zeddyu.info/2020/04/24/Plaid-CTF-2020-Web-2/)
- [Plaid CTF 2020 Contrived Web Problem Write Up](https://blog.zeddyu.info/2020/04/20/Plaid-CTF-2020-Web-1/)

**2020 WPICTF**
- [NotWannasigh WPICTF 2020 Writeup](https://um.wtf/articles/04-notwannasigh-wpictf-2020-writeup.html)

---

### 2019

**2019 RITSEC**
- [RITSEC CTF 2019](https://abraxas.io/2019/11/20/ritsec-ctf-2019/)

---

### 2016

**2016 IceCTF**
- [IceCTF Root of All Evil Write Up](https://chrisissing.wordpress.com/2016/08/24/icectf-root-of-all-evil-write-up/)

---

## 未分类

### GXYCTF

**2019**
- [GXYCTF部分详细题解](https://mp.weixin.qq.com/s/liWyOvtSlVgXNeLbG-3fBw)
- [[GXYCTF2019]禁止套娃](https://blog.csdn.net/qq_41628669/article/details/106092047)
