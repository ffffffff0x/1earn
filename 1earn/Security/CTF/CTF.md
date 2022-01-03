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
        * [美亚杯](#美亚杯)
        * [湖湘杯](#湖湘杯)
        * [祥云杯](#祥云杯)
        * [纵横杯](#纵横杯)
        * [陇剑杯](#陇剑杯)
        * 2020
        * 2019
    * [高校](#高校)
        * [CISCN](#ciscn)
        * 2020
        * 2019
        * 2018
        * 2016
    * [公司&行业](#公司&行业)
        * [XCTF](#xctf)
        * [DASCTF](#dasctf)
        * 2021
        * 2020
        * 2019
        * 2018
    * [国外](#国外)
        * 2020
        * 2019
        * 2016
    * [未分类](#未分类)

---

**平台**
- https://buuoj.cn/
- https://www.ctfhub.com/#/index
- http://www.hetianlab.com/CTFrace.html
- https://adworld.xctf.org.cn/
- https://www.ichunqiu.com/battalion?t=1
- http://ctf.bugku.com/
- https://www.wechall.net/
- https://ctftime.org/
- https://pwnhub.cn/index
- http://hackinglab.cn/
- https://new.bugku.com/

**学习资源**
- https://ctf-wiki.github.io/ctf-wiki/
- https://trailofbits.github.io/ctf/
- https://l1nwatch.gitbooks.io/ctf/content/
- https://yq.aliyun.com/articles/333082
- https://www.peerlyst.com/posts/ctf-write-ups-wiki-peerlyst
- https://github.com/L1nwatch/CTF
- https://ctf-wiki.github.io/ctf-wiki/misc/introduction-zh/
- https://github.com/M0cK1nG-b1Rd/CTF-Mind-maps

**工具合集**
- [zardus/ctf-tools](https://github.com/zardus/ctf-tools) - 安全研究工具的一些设置脚本。

**赛题收集**
- [sajjadium/ctf-archives](https://github.com/sajjadium/ctf-archives)

**Tips**
- 一些找 flag 姿势
    ```
    find / -name flag*
    find / -name * | grep "flag{"
    echo $PATH | grep "flag{"
    env | grep "flag"
    ```

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

# 知识点学习

## Web

- [CTF中的命令执行绕过](https://mp.weixin.qq.com/s/fs-IKJuDptJeZMRDCtbdkw)
- [wonderkun/CTF_web](https://github.com/wonderkun/CTF_web)

## Misc

- [ctf001 | Glun](http://www.glun.top/2020/05/23/ctf01/)
- [ctf03 | Glun](http://www.glun.top/2020/10/13/ctf03/)
- [CTF-MISC总结](https://ares-x.com/2017/11/07/CTF-Misc%E6%80%BB%E7%BB%93/)
- [BUUCTF的Misc（1-110题）](https://www.icode9.com/content-4-787951.html)

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

**2021**
- [虎符CTF Writeup by X1cT34m](http://wh1sper.com/%E8%99%8E%E7%AC%A6ctf-writeup-by-x1ct34m/)
- [2021虎符CTF逆向WP](https://www.cxyzjd.com/article/jxnu_666/115448655)
- [CTF | 2021 数字中国创新大赛虎符网络安全赛道 WriteUp](https://miaotony.xyz/2021/04/04/CTF_2021HFCTF/)

**2020**
- [虎符杯两道NodeJS题目的分析](https://xz.aliyun.com/t/7714)
- [数字中国创新大赛-虎符网络安全赛道Write up](https://mp.weixin.qq.com/s/ih2X8IXVFmrMVwJYuf5gng)
- [虎符 CTF Web 部分 Writeup](https://www.zhaoj.in/read-6512.html)
- [2020 虎符网络安全竞赛 web Writeup](https://www.anquanke.com/post/id/203417)
- [虎符ctf2020 crypto GM](http://39.106.50.81/index.php/archives/9/)

---

### 强网杯

**2021**
- [第五届“强网杯”全国网络安全挑战赛-线上赛Writeup](https://mochu.blog.csdn.net/article/details/117847706)
- [强网杯青少年专项赛选拔赛 wp](https://mp.weixin.qq.com/s/8AAkbk--b8ojA7Ffb8XAQw)
- [广东省强网杯企业组easy_pgsql writeup](https://mp.weixin.qq.com/s/NPD4cvlm9yJeL77ZvgStxA)
- [2021广东强网杯｜WEB及Crypto方向WP](https://mp.weixin.qq.com/s/VT2Ub7RmDPg1tzjQ__x23w)
- [2021广东强网杯｜Reverse及PWN方向WP](https://mp.weixin.qq.com/s/TWKQKMpV_UvJuVjHXywXzA)
- [2021广东强网杯｜MISC方向WP](https://mp.weixin.qq.com/s/kQtqYLlsuaEvr7-iEv9mBg)
- [“强网”拟态防御国际精英挑战赛 WP](https://mp.weixin.qq.com/s/2RErninC7_C_SzKEYfuUJw)

**2020**
- [强网杯部分题目WriteUp](https://l1near.top/index.php/2020/08/24/65.html)
- [强网杯 WRITEUP](https://mp.weixin.qq.com/s/5btNvwbuySvn_2h_3irvWQ)

**2019**
- [2019 第三届强网杯 Web 部分 WriteUp + 复现环境](https://www.zhaoj.in/read-5873.html)
- [强网杯Web部分writeup](https://www.freebuf.com/articles/network/205789.html)
- [2019强网杯部分题目记录](https://www.kkzevip.com/?post=47)
- [2019广东强网杯Writeup(MISC)](https://sec.thief.one/article_content?a_id=bd1f559d1f0ddfe66b69d767a0b6cb5a)
- [广东省第三届强网杯Writeup](https://www.hotbak.net/key/2019%E5%B9%BF%E4%B8%9C%E5%BC%BA%E7%BD%91%E6%9D%AFWriteupMISC.html)
- [广东省强网杯部分题目Writeup](https://www.t00ls.net/viewthread.php?tid=52782&highlight=writeup)
- [2019强网杯Web部分题解](https://nikoeurus.github.io/2019/05/29/2019%E5%BC%BA%E7%BD%91%E6%9D%AFWeb%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3/)

**2019 强网杯拟态挑战赛**
- [MIMIC Defense CTF 2019 final writeup](https://paper.seebug.org/932/)

**2018 强网杯**
- [2018 强网杯 CORE writeup 学习笔记](https://v1ckydxp.github.io/2019/08/27/2019-08-27-2018-%E5%BC%BA%E7%BD%91%E6%9D%AF-core/)

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
    - [网鼎杯（玄武）web2 WriteUp](https://www.t00ls.net/viewthread.php?tid=56484&highlight=writeup)

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
    - [2020网鼎杯朱雀组部分Web题wp](https://www.anquanke.com/post/id/205679)

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

**2021**
- [2021年“羊城杯”网络安全大赛部分Writeup](https://blog.csdn.net/qq_42815161/article/details/120260053)
- [羊城杯wp](https://mp.weixin.qq.com/s/6i5iel2I9rMV2BtwMRZfPQ)

**2020**
- [羊城杯-Reverse-WP](https://www.zrzz.site/2020/09/11/%E7%BE%8A%E5%9F%8E%E6%9D%AF-Reverse-WP/)
- [羊城杯Easy Java题解](https://zhzhdoai.github.io/2020/09/11/%E7%BE%8A%E5%9F%8E%E6%9D%AFEasy-Java%E9%A2%98%E8%A7%A3/)
- [羊城杯-WriteUp](https://mp.weixin.qq.com/s/ODYQ-vB5n-pebMcl4XxCzg)

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

### 湖湘杯

**2021**
- [湖湘杯-WriteUp](https://mp.weixin.qq.com/s/qbUbBBTYi_7ODxGmQKhABA)
- [第七届“湖湘杯”网络安全大赛线下总决赛WP](https://mp.weixin.qq.com/s/NpnqcUzFQqvKe1jDHAkUWQ)

**2020**
- [湖湘杯-WriteUp](https://mp.weixin.qq.com/s/MEX8eJ6LqO0ubnLMGN3K9w)
- [2020湖湘杯部分WriteUp](https://nosec.org/home/detail/4599.html)

**2019**
- [2019 湖湘杯Web部分题解WriteUp](https://nikoeurus.github.io/2019/11/10/2019%E6%B9%96%E6%B9%98%E6%9D%AFwp/)

**2018**
- [湖湘杯线下AWD记录](https://mp.weixin.qq.com/s/yv8Lsc1WqWqeH-GtWnXA5Q)

---

### 祥云杯

**2021**
- [2021第二届“祥云杯”网络安全大赛 部分Writeup](https://blog.csdn.net/qq_42815161/article/details/119867158)

**2020**
- [祥云杯-Writeup](https://mp.weixin.qq.com/s/D2hdFISbttaezhnqnHFEsQ)
- [祥云杯2020 部分WriteUp](https://mp.weixin.qq.com/s/CP3-W8VcLokQNYMSbXw9wg)

---

### 纵横杯

**2020**
- [纵横杯2020 部分WriteUp](https://mp.weixin.qq.com/s/mdFgQPY8-Zw49huj4F_klQ)

---

### 陇剑杯

**2021**
- [陇剑杯 个人 ’WriteUp‘](http://www.snowywar.top/?p=2554)
- [安全-陇剑杯2021（部分）](https://blog.csdn.net/smallfox233/article/details/120291706)
- [2021【线下】 陇剑杯wp](https://mp.weixin.qq.com/s/9fopUOhL0Met0lZxV-5S1A)
- [2021年陇剑杯线上赛](https://secgxx.com/ctf/competition/2021longjiancup/)
- [2021陇剑杯部分WP](https://blog.csdn.net/qq_40568770/article/details/120311122)

---

### 绿城杯

**2021**
- [2021 绿城杯 wp](https://mp.weixin.qq.com/s/sdPBAaWXZARMU2VlO7b1dg)
- [绿城杯-2021 部分WriteUp（晋级）](https://mp.weixin.qq.com/s/wRXs586qjoFdLx37xPNvjQ)
- [绿城杯-WriteUp](https://mp.weixin.qq.com/s/tulBiwucSYOJUkCa--0Wow)
- [2021 绿城杯 Crypto 部分wp](https://icode9.com/content-4-1158507.html)

---

### 鹤城杯

**2021**
- [2021鹤城杯｜WEB部分WP全](https://mp.weixin.qq.com/s/_9acgNlTA_yqMqZK_Std-A)
- [鹤城杯-WriteUp](https://mp.weixin.qq.com/s/TZt0oUkmgJYe21SbcS5Ybw)
- [2021鹤城杯｜PWN部分WP全](https://mp.weixin.qq.com/s/WGEjSSNDJuZcnqJJev5zGQ)
- [2021鹤城杯｜Reverse及MISC部分WP全](https://mp.weixin.qq.com/s/4ZbYy_Kl3A5XTmi1AlpPfQ)

---

### 长城杯

**2021**
- [长城杯线上赛WP](https://mp.weixin.qq.com/s/LxPQDJ8xvBq4Qc-89td1_A)
- [第一届"长城杯"网络安全大赛WP](https://mp.weixin.qq.com/s/CUJDx3x7nXpDYU8UdVOXfQ)
- [2021 第一届 长城杯ctf wp](https://mp.weixin.qq.com/s/xAn7QLmS2bNd0Iql59rsPQ)

---

### 赣网杯

**2021**
- [2021赣网杯WEB题目WP](https://mp.weixin.qq.com/s/OU5mnVCeCXwQ-oVnGkwW7Q)
- [2021年第二届赣网杯网络安全大赛MISC-Writeup](https://mp.weixin.qq.com/s/I_OyYVvlNOzmG2JnAGuYdg)
- [赣网杯 MISC Writeup](https://mp.weixin.qq.com/s/mbguu98sNMGM8IEjLHNNpg)

---

### 长安杯

**2021**
- [2021长安杯｜Web & Crypto 部分wp合集](https://mp.weixin.qq.com/s/OWLoMnaxfKcpP4-7QiBktw)
- [2021 长安杯 wp](https://mp.weixin.qq.com/s/tYcLkQ0Ay9_IYt1XJF9EFA)
- [长安杯-WriteUp](https://mp.weixin.qq.com/s/gORwuwOIZvwD6mZQePTHYQ)

---

### 2021

**2021 西湖论剑**
- [西湖论剑-WriteUp](https://mp.weixin.qq.com/s/HSLnu1pmTZ7AYxMM8oNBaw)
- [西湖论剑 部分wp](https://mp.weixin.qq.com/s/S_t02JOYnSg2ZB71WlhErA)
- [2021 西湖论剑CTF-wp](https://mp.weixin.qq.com/s/TR8FJ8ObZR3puQlZ9gIZOw)
- [西湖论剑2021中国杭州网络安全技能大赛writeup](https://mp.weixin.qq.com/s/q1KNC5F8qHDpTTZQcFaWZA)

**2021 第五空间**
- [第五空间-2021 部分WriteUp](https://mp.weixin.qq.com/s/9QzrQxy_oIqiZpFlld3oyw)
- [第三届第五空间网络安全大赛WP](https://mp.weixin.qq.com/s/0UwX26Ofi0exLv38kqFt_A)

---

### 2020

**宁波市第三届网络安全大赛**
- [宁波市第三届网络安全大赛线上赛部分题目-writeup](https://blog.csdn.net/qq_45628145/article/details/107183635)
- [2020宁波市第三届网络安全大赛 Web Writeup](https://www.cnblogs.com/skyxmao/p/13262594.html)
- [宁波市第三届网络安全大赛-WriteUp（Misc）](https://codingnote.cc/p/150404)

**2020 “第五空间”智能安全大赛**
- [2020 “第五空间”智能安全大赛初赛两道 RE 解题报告（writeup）](https://hx1997.github.io/2020/06/25/5space-2020-re-writeup/)
- [2020第五空间Final](https://blog.szfszf.top/article/47/)

**2020 极客巅峰**
- [极客巅峰2020 部分WriteUp](https://www.secpulse.com/archives/143078.html)

**2020 西湖论剑**
- [西湖论剑-WriteUp](https://mp.weixin.qq.com/s/dCi4n8lGhfxvPIdRn67reA)
- [“西湖论剑” 2020 WriteUp By NepNep](http://www.qfrost.com/CTF/%E8%A5%BF%E6%B9%96%E8%AE%BA%E5%89%91_2020/)

### 2019

**2019 西湖论剑**
- [从西湖论剑2019Storm_note看largebin attack](https://www.anquanke.com/post/id/176194)
- [杭州"西湖论剑"ctf-Web](https://nikoeurus.github.io/2019/04/11/%E6%9D%AD%E5%B7%9E%E2%80%9C%E8%A5%BF%E6%B9%96%E8%AE%BA%E5%89%91%E2%80%9Dctf-Web/)
- [2019西湖论剑杯writeup](https://ab-alex.github.io/2019/04/11/2019%E8%A5%BF%E6%B9%96%E8%AE%BA%E5%89%91%E6%9D%AFwriteup/)
- [西湖论剑2019 WriteUp](https://mp.weixin.qq.com/s/rlSyABoulRKygPmwfcUuXA)

**2019 第五空间**
- [“第五空间”网络安全线下赛PWN部分WRITEUP](https://xz.aliyun.com/t/6431)

---

## 教育

### CISCN

**2020**
- [CTF | 2020 CISCN初赛 Z3&LFSR WriteUp](https://miaotony.xyz/2020/08/27/CTF_2020CISCN_preliminary/)
- [2020CISCN-初赛Web](https://jwt1399.top/posts/17919.html)
- [2020国赛CTF审计题目babyunserialize](https://mp.weixin.qq.com/s/8VjFFYKzMIlTXuH2v2MRxQ)

**2019**
- [CISCN 2019 东北赛区 Day2 Web3 WriteUp](https://www.zhaoj.in/read-6057.html)
- [CISCN 2019 华东北赛区 Web2 WriteUp](https://www.zhaoj.in/read-6100.html)
- [全国第十二届大学生信息安全竞赛 线上初赛 Web 部分 WriteUp](https://www.zhaoj.in/read-5417.html)
- [CISCN 华北赛区 Day1 Web2 WriteUp](https://www.zhaoj.in/read-5946.html)
- [ciscn线下部分题解](https://ab-alex.github.io/2019/06/05/ciscn%E7%BA%BF%E4%B8%8B%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3/)

---

### 2021

**2021 hackergame**
- [USTC-Hackergame/hackergame2021-writeups](https://github.com/USTC-Hackergame/hackergame2021-writeups)

**2021 河南省第三届金盾信安杯**
- [河南省第三届“金盾信安杯”网络安全大赛Writeup](https://mp.weixin.qq.com/s/B6WWQ8aVe3Fb2D9dLWmMZA)

**2021 追日杯**
- [首届安徽"追日杯"大学生网络安全挑战赛WRITEUP](https://mp.weixin.qq.com/s/K5O4ADsQWMI0TEX6cnBNXg)
- [首届安徽"追日杯"大学生网络安全挑战赛wp](https://mp.weixin.qq.com/s/4MiFU0NdGcNchHXojlBsiQ)

**2021 东软杯**
- [东软杯-WriteUp](https://mp.weixin.qq.com/s/KgxHOFH52EE8z7NnMTSIDA)

**2021 安洵杯**
- [安洵杯-WriteUp](https://mp.weixin.qq.com/s/vC2bgJlYfA8wzXcmQFynlA)

**2021网络安全领军人才攻防大赛**
- [2021网络安全领军人才攻防大赛 ｜ Pwn方向WP](https://mp.weixin.qq.com/s/ZyzjHDUhA-u781F2IfcVUg)
- [2021网络安全领军人才攻防大赛 ｜ Crypto及Reverse方向WP合集](https://mp.weixin.qq.com/s/mhRWKQqnesVVDoJQktYIzA)
- [2021网络安全领军人才攻防大赛 ｜ Web方向WP](https://mp.weixin.qq.com/s/keTllFjA3kK9sMz_wPRvpg)

**“东华杯”2021年大学生网络安全邀请赛 暨第七届上海市大学生网络安全大赛线上赛**
- [“东华杯”2021年大学生网络安全邀请赛 暨第七届上海市大学生网络安全大赛线上赛MISC-Writeup](https://mp.weixin.qq.com/s/-2CrIBKB8BNJzwDDXe-b_Q)

### 2020

**2020 安洵杯**
- [安洵杯2020 官方Writeup(Web/Misc/Crypto) - D0g3](https://xz.aliyun.com/t/8581)

**2020重庆市教育系统网络安全攻防竞赛**
- [2020重庆市教育局网络安全攻防比赛](https://my.oschina.net/u/4411210/blog/4602798)
- [2020重庆市教育系统网络安全攻防竞赛决赛 - Web Writeup](https://www.0x002.com/2020/2020%E9%87%8D%E5%BA%86%E5%B8%82%E6%95%99%E8%82%B2%E7%B3%BB%E7%BB%9F%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%94%BB%E9%98%B2%E7%AB%9E%E8%B5%9B%E5%86%B3%E8%B5%9B%20-%20Web%20Writeup/)

**2020 NUAACTF**
- [CTF | 2020 NUAACTF 吸喵喵队 Writeup](https://miaotony.xyz/2020/05/30/CTF_2020NUAACTF/)

**2020 BJDCTF**
- [CTF | BJDCTF 2nd WriteUp](https://miaotony.xyz/2020/03/23/CTF_BJDCTF2nd/)
- [BJDCTF 2nd EasyAspDotNet WriteUp](https://www.zhaoj.in/read-6497.html)

**2020 Ha1cyon_CTF**
- [CTF | 2020 Ha1cyon_CTF公开赛 WriteUp](https://miaotony.xyz/2020/04/21/CTF_2020Ha1cyonCTF/)

**2020 WHUCTF**
- [WHUCTF2020出题记录](https://blog.szfszf.top/article/43/)

**2020 DMCTF**
- [DMCTF校赛思路总结](https://blog.csdn.net/qq_48175067/article/details/110896549)

**2020 CG-CTF**
- [南航 CG-CTF 题目WP](https://mp.weixin.qq.com/s/BdbGby1xY-I0NYjgucgwNw)

### 2019

**2019 浙江省大学生网络与信息安全竞赛**
- [2019浙江省大学生网络与信息安全竞赛决赛部分WriteUp](https://xz.aliyun.com/t/6458)

**2019 虎鲸杯**
- [2019 虎鲸杯电子取证大赛赛后复盘总结](https://www.anquanke.com/post/id/177714)

**2019 安洵杯**
- [2019 安洵杯Web部分题解WriteUp](https://nikoeurus.github.io/2019/11/30/2019%E5%AE%89%E8%AF%A2%E6%9D%AF-Web/)
- [2019 安洵杯线下赛awd-Web题解WriteUp](https://nikoeurus.github.io/2019/12/11/2019%E5%AE%89%E6%B4%B5%E6%9D%AF%E7%BA%BF%E4%B8%8B%E8%B5%9Bawd-Web%E9%A2%98%E8%A7%A3/)
- [2019安洵杯+2019广外比赛web部分题解](https://ab-alex.github.io/2019/12/01/2019%E5%AE%89%E6%B4%B5%E6%9D%AF-2019%E5%B9%BF%E5%A4%96%E6%AF%94%E8%B5%9Bweb%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3/)

**2019 百越杯**
- [2019 百越杯Web题解WriteUp](https://nikoeurus.github.io/2019/11/11/2019%E7%99%BE%E8%B6%8A%E6%9D%AF-Web/)

**2019 “应急挑战杯”大学生网络安全大学生网络安全邀请赛**
- [“应急挑战杯”大学生网络安全大学生网络安全邀请赛复盘](https://www.zhaoj.in/read-5525.html)

**2019 HDCTF**
- [HDCTF 2019 部分题目 WriteUp](https://www.zhaoj.in/read-5548.html)

**2019 GUET-CTF**
- [GUET-CTF 题目备份](https://www.zhaoj.in/read-5851.html)

**2019 ISCC**
- [ISCC 2019 部分题目 WriteUp](https://www.zhaoj.in/read-5629.html)
- [ISCC 2019 Writeup](https://nikoeurus.github.io/2019/05/25/ISCC2019/)

**湖南省第三届大学生信息安全技能竞赛**
- [湖南省第三届大学生信息安全水赛WriteUp](https://gksec.com/HNCTF2019-Final.html)

### 2018

**2018 HCTF**
- [2018 HCTF Web Writeup](https://skysec.top/2018/11/12/2018-HCTF-Web-Writeup/)
- [HCTF 2018 Official Writeup](https://www.secpulse.com/archives/82690.html)
- [HCTF 2018 WriteUp](https://impakho.com/post/hctf-2018-writeup)
- [HCTF 2018 Writeup](https://xz.aliyun.com/t/3242)
- [hctf2018web](https://ab-alex.github.io/2018/11/12/hctf2018web/)

**2018 ISCC**
- [ISCC 2018线上赛 writeup](https://www.cnblogs.com/semishigure/archive/2018/06/06/9013131.html)

**2018“骇极杯”上海大学生网络安全大赛**
- [2018“骇极杯”上海大学生网络安全大赛 Web题解](https://blog.szfszf.top/article/13/)
- [“骇极杯”全国大学生网络安全邀请赛WriteUp](https://cloud.tencent.com/developer/article/1369854?from=article.detail.1515395)

### 2016

**2016 HCTF**
- [HCTF 2016网络攻防大赛官方Writeup](https://www.freebuf.com/articles/web/121778.html)

**2016 第二届上海市大学生网络安全大赛**
- [【CTF攻略】第二届上海市大学生网络安全大赛Writeup](https://www.anquanke.com/post/id/84924)

---

## 公司&行业

### XCTF

**2021 L3HCTF**
- [L3HCTF-WriteUp](https://mp.weixin.qq.com/s/UvUNyZuK0kAcfyto06Xx4g)
- [2021-L3HCTF SpecialRain-Writeup](http://xibai.xyz/2021/11/15/2021-L3HCTF/)
- [L3HCTF luuuuua](https://0wl.site/2021/11/16/L3HCTF-luuuuua/)
- [l3hctf_part_wp](https://yimianweishi.github.io/2021/11/17/l3hctf-part-wp/index.html)
- [L3HCTF 2021 星盟ctf战队](https://mp.weixin.qq.com/s/RVGg0zW6mFBImZpvyMDwvw)

**2021 第四届“强网”拟态防御国际精英挑战赛**
- [第四届“强网”拟态防御国际精英挑战赛_wp（上）](https://mp.weixin.qq.com/s/xWgZKtQdsQ562EXLGiNDlg)
- [第四届强网拟态防御国际精英挑战赛线上预选赛MISC WRITEUP](https://mp.weixin.qq.com/s/qzxMiQaIWc1GNJqg6adzyQ)

**2021 RCTF**
- [RCTF-2021 部分WriteUp](https://mp.weixin.qq.com/s/EnncNONPhgrZCgeYDE5Q2A)

**2020 wmctf**
- [Nobody knows BaoTa better than me WriteUp](https://www.zhaoj.in/read-6660.html)
- [W&MCTF_Dalabengba](http://www.fzwjscj.xyz/index.php/archives/37/)
- [W&MCTF](http://wh1sper.cn/wmctf/)
- [W&MCTF-0RAYS](https://www.anquanke.com/post/id/212809)

**2020 高校战“疫”**
- [CTF | XCTF高校战“疫”网络安全分享赛 WriteUp](https://miaotony.xyz/2020/03/15/CTF_2020XCTF_gxzy/)

**2020 De1CTF**
- [CTF | 2020 De1CTF Misc Chowder WriteUp](https://miaotony.xyz/2020/05/04/CTF_2020De1CTF/)

**2020 GACTF**
- [CTF | 2020 GACTF 一点点WriteUp](https://miaotony.xyz/2020/08/31/CTF_2020GACTF/)
- [GACTF-WriteUp](https://mp.weixin.qq.com/s/uL2yEuSKJGNWGaNYsQIjsg)

**2020 SCTF**
- [SCTF 2020 Login Me Aagin WriteUp](https://www.zhaoj.in/read-6617.html)

**2020 RCTF**
- [[CTF]2020RCTF Swoole题解学习笔记](https://zhzhdoai.github.io/2020/06/02/CTF-2020RCTF-Swoole%E9%A2%98%E8%A7%A3%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)

**2019 xctf-finals**
- [2019 xctf-finals Web-lfi2019复现](https://nikoeurus.github.io/2019/11/04/lfi2019/)

**2019 SCTF**
- [SCTF2019 部分题目WriteUp](https://www.zhaoj.in/read-5985.html)

**2019 RCTF**
- [RCTF2019 jail WriteUp](https://blog.szfszf.top/article/31/)

**2019 De1CTF**
- [De1CTF2019 官方Writeup(Web/Misc) -- De1ta](https://xz.aliyun.com/t/5945)
- [De1CTF Web WriteUp](https://www.zhaoj.in/read-6170.html)

**2019 N1CTF**
- [分析N1CTF 2019中Crypto方向题目](https://www.anquanke.com/post/id/186525)

**2018 N1CTF**
- [2018n1ctf-esay-php复现](https://ab-alex.github.io/2019/08/06/2018n1ctf-esay-php%E5%A4%8D%E7%8E%B0/)

**2018 赛博地球杯工业互联网安全大赛**
- [“赛博地球杯”工业互联网安全大赛线上赛Writeup](https://www.xctf.org.cn/library/details/cyberearth-writeup/)
- [2018 XCTF-赛博地球杯工业互联网安全大赛web部分题解](https://skysec.top/2018/01/18/XCTF-%E8%B5%9B%E5%8D%9A%E5%9C%B0%E7%90%83%E6%9D%AF%E5%B7%A5%E4%B8%9A%E4%BA%92%E8%81%94%E7%BD%91%E5%AE%89%E5%85%A8%E5%A4%A7%E8%B5%9Bweb%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3/)

**2017 WHCTF**
- [WHCTF官方Writeup](https://www.xctf.org.cn/library/details/whctf-writeup/)

---

### DASCTF

**21.8**
- [2021DASCTF八月挑战赛Writeup](https://blog.csdn.net/qq_42815161/article/details/120010131)
- [DASCTF八月挑战赛 re](https://mp.weixin.qq.com/s/IMhP4UGrY2pwKI1tmf1vjA)

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
- [DASCTF_六月赛MISC部分wp](http://www.ga1axy.top/index.php/archives/42/)

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

### 2021

**2021 创安杯**
- [2021创安杯智能汽车信息公开赛-知识赛](https://mp.weixin.qq.com/s/M5cyp-mdVor8Ppb_xKtDZA)

**2021 美团CTF**
- [美团CTF-WriteUp](https://mp.weixin.qq.com/s/UKkneDKoFBmmUIlbC6bwvA)
- [第四届2021美团网络安全 MT-CTF writeup](https://mp.weixin.qq.com/s/tPI_c-Finz_6OP9WQJMrtQ)

**江西省2021年工业互联网安全技术技能大赛**
- [某省工业互联网安全技术技能大赛Writeup](https://mp.weixin.qq.com/s/W7EQQ8e9j3L-W4Wgmtf5gA)

**2021 天翼杯**
- [2021第二届“天翼杯”网络安全攻防大赛WP](https://mp.weixin.qq.com/s/TE6KokKr9mpjGtQ9mOe2MQ)

**2021 bilibili**
- [程序员节日挑战赛writeup](https://mp.weixin.qq.com/s/3O-fH6fcwEpSCK63yTb0ww)

**2021 春秋杯秋季赛**
- [2021春秋杯秋季赛-Writeup](https://mp.weixin.qq.com/s/9fSrQbSdhykkzoiEYGovJQ)

**2021 深育杯**
- [深育杯-WriteUp](https://mp.weixin.qq.com/s/HvyRjbLVPaMg7DBfdYmdJw)
- [2021深育杯线上初赛官方WriteUp](https://mp.weixin.qq.com/s/Iwj_zNgYZKZvJOYuhmlz3w)
- [深育杯-网络安全大赛专业竞赛WriteUp-IDLab](https://mp.weixin.qq.com/s/NvItuko9ZAUNTJaSzBpNKw)

**陇原战“疫”2021**
- [陇原战_疫_2021网络安全大赛](https://mp.weixin.qq.com/s/Lcq7h8VpZaHX3oFrr2E_uQ)
- [陇原战“疫”2021-WriteUp](https://mp.weixin.qq.com/s/O5cyHCvQsu6RNTp4A_Gp4w)
- [2021陇原战"疫" 部分赛题复现](https://mp.weixin.qq.com/s/KIkE50ELd2PBcbqZ_vUyQg)

**“枢网智盾-2021”智慧城市工控系统应急处置技术挑战赛线**
- [枢网智盾线上赛Writeup](https://mp.weixin.qq.com/s/Uub24ztAF_jKXz5dEK-dTw)

**2021 中科实数杯**
- [2021年中科实数杯团队赛手机部分考题write up](https://mp.weixin.qq.com/s/gx9s49dMxhKAHDZgYi-YOg)

**2021 Bytectf**
- [ByteCTF-WriteUp](https://mp.weixin.qq.com/s/k8wrSSra_NO165RLM_CrUw)
- [2021ByteCTF 北极星-writeup](https://mp.weixin.qq.com/s/OPWOKA9a9Ji_8vufV6QFYA)
- [ByteCTF 2021 By W&M（WEB）部分](https://mp.weixin.qq.com/s/s59xN-QI9oNPrkjhuXtPyw)
- [ByteCTF 2021 By W&M（PWN）部分](https://mp.weixin.qq.com/s/fqX-ICojKhe-FBGCLhWB0A)
- [ByteCTF 2021 By W&M（Crypto）部分](https://mp.weixin.qq.com/s/LpFb9qlrazb7o-zZFuZufw)
- [ByteCTF 2021 By W&M（MISC）部分](https://mp.weixin.qq.com/s/_A3TjeAZ0yAnpvxyn0wWCA)
- [ByteCTF 2021 By W&M（REVERSE）部分](https://mp.weixin.qq.com/s/h-wTnquhBTB8EzU5pYmPDg)
- [2021ByteCTF决赛wp—北极星战队](https://mp.weixin.qq.com/s/y5152EoQg_W6N7YCNtnNUA)
- [ByteCTF 2021 Final By W&M（WEB）部分](https://mp.weixin.qq.com/s/2lzx7ly6kB7UsulC1cUl-w)
- [ByteCTF 2021 Final By W&M（​Reverse）部分](https://mp.weixin.qq.com/s/CYiWly4jPYYEBon6xK6WFA)
- [ByteCTF 2021 Final By W&M（Crypto）部分](https://mp.weixin.qq.com/s/mqEM34zkCPhNBZ9sAS85Lg)
- [ByteCTF 2021 Final By W&M（MISC）部分](https://mp.weixin.qq.com/s/IXWBU-vXMan9mHerPCPPjQ)
- [ByteCTF 2021 Final By W&M（Mobile）部分](https://mp.weixin.qq.com/s/7HDLGC4irJZ2M6oKwyXmXg)

**2021年工业信息安全技能大赛**
- [2021年工业信息安全技能大赛线上赛](https://secgxx.com/ctf/competition/2021icsc/)
- [2021年⼯业信息安全技能⼤赛-线上第⼀场WriteUp](https://mp.weixin.qq.com/s/DFJaILmNxTl1EAyksqQZ9w)

**2021中国能源网络安全大赛**
- [CTF-2021中国能源网络WEB题目全解](https://mp.weixin.qq.com/s/aq1ZUKspmXIG8GKVV2xPuw)

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

**2020 Bytectf**
- [Bytectf2020 writeup by W&M](https://mp.weixin.qq.com/s/4OVC10crL1rBFrNf9wyUTg)
- [ByteCTF-WriteUp](https://mp.weixin.qq.com/s/GAlwjtqB79wq42ByxPblMw)

**2020 RoarCTF**
- [RoarCTF-WriteUp](https://mp.weixin.qq.com/s/Ipy-PCnxQWlctQk1oI9arw)

---

### 2019

**2019 NSCTF**
- [NSCTF 2019 TechWorld 信息安全挑战赛 WriteUp by impakho](https://impakho.com/post/nsctf-2019-techworld-writeup)

**2019年工业信息安全技能大赛**
- [2019工业信息安全技能大赛个人线上赛第一场(前5道)writeup](https://xz.aliyun.com/t/5960)
- [2019工业信息安全技能大赛个人线上赛第二场(5道) writeup](https://xz.aliyun.com/t/6445)
- [2019工业信息安全技能大赛个人线上赛第一场writeup](https://login546.github.io/2019/07/29/2019%E5%B7%A5%E4%B8%9A%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8%E6%8A%80%E8%83%BD%E5%A4%A7%E8%B5%9B%E4%B8%AA%E4%BA%BA%E7%BA%BF%E4%B8%8A%E8%B5%9BNO-1writeup/)

**2019 RealWorld CTF**
- [v8 exploit - RealWorld CTF2019 accessible](https://xz.aliyun.com/t/6507)

**2019 D^3 CTF**
- [2019 D^3 CTF-Web部分复现记录](https://nikoeurus.github.io/2019/11/26/D%5E3ctf-Web/)
- [2019 D^3 CTF-easyweb预期解复现](https://nikoeurus.github.io/2019/12/12/D%5E3ctf-easyweb/)
- [2019 D^3 CTF-ezts复现](https://nikoeurus.github.io/2019/12/18/D%5E3ctf-ezts/)

**2019 OPPO OGeek CTF**
- [OPPO OGeek CTF 2019 部分题目 WriteUp](https://www.zhaoj.in/read-6251.html)
- [OGeek CTF 2019 线下决赛 pwn 题解](https://www.anquanke.com/post/id/187516)
- [OGeek CTF 2019-Enjoy You Self](https://ab-alex.github.io/2019/09/04/OGeek-CTF-2019-Enjoy-You-Self/)

**2019 ByteCTF CTF**
- [字节跳动 ByteCTF 2019 Web RSS WriteUp](https://www.zhaoj.in/read-6310.html)

**2019 DDCTF**
- [DDCTF 2019 Web 部分 WriteUp](https://www.zhaoj.in/read-5269.html)
- [DDCTF2019两个逆向writeup ](https://www.freebuf.com/articles/network/202987.html)
- [DDCTF 2019 WriteUp](https://blog.szfszf.top/article/29/)
- [DDCTF2019官方Write Up——MISC篇](https://www.anquanke.com/post/id/178392)
- [DDCTF2019官方Write Up——Android篇](https://www.anquanke.com/post/id/178383)
- [DDCTF2019官方Write Up——Web篇](https://www.anquanke.com/post/id/178434)
- [DDCTF2019官方Write Up——Reverse篇](https://www.anquanke.com/post/id/178414)
- [DDCTF 2019 Web2 Writeup](https://github.red/ddctf-2019/)
- [DDCTF-Web](https://nikoeurus.github.io/2019/04/19/ddctf-Web/)

**2019 RoarCTF**
- [2019 RoarCTF部分题解WriteUp](https://nikoeurus.github.io/2019/10/14/RoarCTF/)
- [Roarctf 部分Writeup](https://www.anquanke.com/post/id/188785)
- [RoarCTF Web writeup](https://github.red/roarctf-web-writeup/)
- [RoarCTF2019 Web WriteUp](https://blog.szfszf.top/article/38/)
- [berTrAM888/RoarCTF-Writeup-some-Source-Code](https://github.com/berTrAM888/RoarCTF-Writeup-some-Source-Code)
- [Carry955/RoarCTF-Writeup-2019](https://github.com/Carry955/RoarCTF-Writeup-2019)
- [RoarCTF2019 Writeup](https://paper.seebug.org/1059/)

### 2018

**2018工业信息安全技能大赛**
- [2018工业信息安全技能大赛华东赛区初赛 第2题 writeup](https://www.bbsmax.com/A/gVdngBANzW/)

**金融业网络安全攻防比赛**
- [金融业网络安全攻防比赛热身赛writeup](https://www.secpulse.com/archives/74096.html)
- [金融业网络安全攻防比赛热身赛writeup](https://mp.weixin.qq.com/s/gwtdAeBy6dKViiZJbgKMSA)
- [金融业网络安全攻防大赛部分题目writeup](https://www.anquanke.com/post/id/154477)

**2018年民航网络安全职业技能竞赛**
- [wrlu/CAAC-CTF-2018-Primary](https://github.com/wrlu/CAAC-CTF-2018-Primary)

**2018 DDCTF**
- [DDCTF 2018 writeup(一) WEB篇](https://www.anquanke.com/post/id/144879)
- [DDCTF 2018 writeup(二) 逆向篇](https://www.anquanke.com/post/id/145553)
- [【知识库】DDCTF 2018 writeup(三) 安卓篇](https://www.anquanke.com/post/id/146536)

### 2017

**2017 0ctf**
- [2017 0ctf babyheap writeup](https://v1ckydxp.github.io/2019/04/14/2017_0ctf_babyheap/)

---

## 国外

### 2021

**2021 ractf**
- [Ractf 2021 解题思路分享](https://mp.weixin.qq.com/s/5qWO6Sw2uEjeqfcz-ydDkQ)

**2021 hxp CTF**
- [hxp CTF 2021 - A New Novel LFI](https://tttang.com/archive/1384/)

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
- [2019 GXYctf-Web题解WriteUp](https://nikoeurus.github.io/2019/12/21/2019GXYctf-wp/)

### SWPU

**2019**
- [2019 SWPU-ctf Web题解WriteUp](https://nikoeurus.github.io/2019/12/09/SWPU-ctf/)

### 极客大挑战

**2019**
- [2019 极客挑战-Web部分题解WriteUp](https://nikoeurus.github.io/2019/11/20/2019%E6%9E%81%E5%AE%A2%E6%8C%91%E6%88%98Web/)
- [2019极客大挑战RCE ME](https://ab-alex.github.io/2019/11/20/2019%E6%9E%81%E5%AE%A2%E5%A4%A7%E6%8C%91%E6%88%98RCE-ME/)

### 掘安杯

**2019**
- [2019掘安杯writeup](https://ab-alex.github.io/2019/04/09/2019%E6%8E%98%E5%AE%89%E6%9D%AFwriteup/)

### 嘉韦思杯

**2019**
- [2019“嘉韦思杯”上海市网络安全邀请赛WriteUp](https://cloud.tencent.com/developer/article/1515395)
- [2019年上海嘉韦思杯writeup](https://ab-alex.github.io/2019/04/01/2019%E5%B9%B4%E4%B8%8A%E6%B5%B7%E5%98%89%E9%9F%A6%E6%80%9D%E6%9D%AFwriteup/)

### i春秋

**2020新春战“疫”**
- [i春秋2020新春战“疫”网络安全公益赛GYCTF 两个 NodeJS 题 WriteUp](https://www.zhaoj.in/read-6462.html)
- [i春秋2020新春战“疫”网络安全公益赛 web Writeup](https://ab-alex.github.io/2020/02/24/i%E6%98%A5%E7%A7%8B2020%E6%96%B0%E6%98%A5%E6%88%98%E2%80%9C%E7%96%AB%E2%80%9D%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%85%AC%E7%9B%8A%E8%B5%9B-web-Writeup/)
