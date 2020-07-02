# CTF

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

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
- https://cgctf.nuptsast.com/login
- https://ctf-wiki.github.io/ctf-wiki/
- https://trailofbits.github.io/ctf/
- https://l1nwatch.gitbooks.io/ctf/content/
- https://yq.aliyun.com/articles/333082
- https://www.peerlyst.com/posts/ctf-write-ups-wiki-peerlyst
- https://github.com/L1nwatch/CTF

**工具合集**
- [zardus/ctf-tools](https://github.com/zardus/ctf-tools) - 安全研究工具的一些设置脚本。

---

# Crypto

**基础知识**
- [Crypto 笔记](./Crypto.md)

**writup**
- [IDF实验室-特殊的日子](https://blog.csdn.net/ab748998806/article/details/46382017) - 知识点 : CRC
- [曼切斯特与差分曼切斯特](https://skysec.top/2017/07/10/%E6%9B%BC%E5%88%87%E6%96%AF%E7%89%B9%E4%B8%8E%E5%B7%AE%E5%88%86%E6%9B%BC%E5%88%87%E6%96%AF%E7%89%B9/) - 知识点 : 曼切斯特编码与差分曼切斯特编码

---

# Misc
## 取证

**取证通用工具**
- binwalk - 固件分析工具
    - kali 自带, 递归提取 `binwalk -Me xxx.bin`
- foremost - 文件分离工具
    - kali 自带, `foremost -i 1.png`

---

### 流量包取证

**流量包取证专用工具**
- Wireshark
    - [Wireshark 笔记](../../工具/Wireshark.md)

---

### 压缩包取证

**密码爆破工具**
- [pyrofex/breakzip](https://gitlab.com/pyrofex/breakzip) - 用于破解使用弱加密的加密压缩文件的实用工具。
- Advanced Archive Password Recovery - 一个灵活的，适用于 ZIP 和 RAR 档案的高度优化的口令恢复工具。
- Ziperello - zip 爆破工具

---

## 隐写
### 图片隐写

**文章**
- [CTF中常见图片隐写](http://zjw.dropsec.xyz/uncategorized/2016/08/18/CTF%E4%B8%AD%E5%B8%B8%E8%A7%81%E5%9B%BE%E7%89%87%E9%9A%90%E5%86%99.html)
- [隐写术总结](http://drops.xmd5.com/static/drops/tips-4862.html)
- [Steganography](http://datagenetics.com/blog/march12012/index.html)
- [misc-stegaBasic](https://www.jianshu.com/p/fe7a5fff2a95)

**图片隐写通用工具**
- Stegsolve - 隐写图片查看的利器
    - [stegsolve使用方法](https://www.cnblogs.com/cat47/p/11483478.html)
- [stegosuite](https://stegosuite.org/) - 一个用 Java 编写的免费和开源的图片隐写工具。使用 Stegosuite，你可以轻松地隐藏图像文件中的信息。
- [zsteg](https://github.com/zed-0xff/zsteg) - 图片隐写信息快速检测工具
    ```bash
    gem install zsteg
    zsteg 1.png --all
    ```

**writup**
- [[IceCTF 2016] [Stega 100 – Pretty Pixels] Write Up](https://0x90r00t.com/2016/08/26/icectf-2016-stega-100-pretty-pixels-write-up/)

**Tips**
- exif 信息
- 十六进制下搜文件头 `89504E47` 搜文件头数据块 `IHDR`
- strings 查看可见字符
- 有些会修改图片宽高，直接010打开改大点试试
- 2张图试试 xor

---

#### LSB隐写

> LSB(英文 least significant bit)即最低有效位，位于二进制数的最右侧。图像的每一个像素点都是由RGB（红、绿、蓝）三原色组成，每个颜色占8位(如#FFFFFF)。由于修改最后1位对人眼不敏感，这样一个像素点就可以携带3位信息。应用LSB算法的图像格式需为无损压缩数据格式，例如图像中的bmp、png格式和音频的wav格式。

**LSB隐写专用工具**
- [livz/cloacked-pixel](https://github.com/livz/cloacked-pixel) - LSB 隐写和检测
- [RobinDavid/LSB-Steganography](https://github.com/RobinDavid/LSB-Steganography) - 使用最低有效位将隐写文件转换为图像。

**文章**
- [隐写技巧——PNG文件中的LSB隐写](https://3gstudent.github.io/%E9%9A%90%E5%86%99%E6%8A%80%E5%B7%A7-PNG%E6%96%87%E4%BB%B6%E4%B8%AD%E7%9A%84LSB%E9%9A%90%E5%86%99/)

---

### 音频隐写

**音频隐写通用工具**
- [Detect DTMF Tones](http://dialabc.com/sound/detect/index.html) - 分析音频录音，并提供一些统计数字、图表和表格，显示数据中包含了哪些 DTMF 音调，以及在哪里。
- [Audacity](https://sourceforge.net/projects/audacity/) - 一款易于使用的多轨音频编辑器和记录器
- [MP3stego](https://www.petitcolas.net/steganography/mp3stego/) - MP3Stego 将在压缩过程中隐藏 MP3 文件中的信息。

**write**
- [音频隐写 MP3stego+wav隐写+题目](https://m3tar.github.io/2017/08/20/%E9%9F%B3%E9%A2%91%E9%9A%90%E5%86%99-MP3stego-wav%E9%9A%90%E5%86%99-%E9%A2%98%E7%9B%AE/)

---

# Web

![](../../../../assets/img/才怪.png)

---

# Reverse

![](../../../../assets/img/才怪.png)

---

# Pwn

![](../../../../assets/img/才怪.png)

---

# Writeup
## 网鼎杯

**2020**
- 青龙组
    - [2020网鼎杯青龙组部分wp](https://www.52pojie.cn/thread-1176169-1-1.html)
    - [2020网鼎杯第一场Crypto题解](https://blog.csdn.net/cccchhhh6819/article/details/106038866/)
    - [网鼎杯2020青龙组 web writeup](https://www.xuenixiang.com/thread-2208-1-1.html)
    - [网鼎杯 2020 Web Writeup](https://www.xmsec.cc/wang-ding-bei-2020-web-writeup/)
    - [网鼎杯青龙组2020部分题解](https://www.cnblogs.com/kevinbruce656/p/12869764.html)
    - [网鼎杯 2020 第一场 signal writeup](http://dreamcracker.today/2020/05/11/%e7%bd%91%e9%bc%8e%e6%9d%af-2020-%e7%ac%ac%e4%b8%80%e5%9c%ba-signal-writeup/)
    - [2020-网鼎杯(青龙组)-Web题目-AreUserialz Writeup](https://mp.weixin.qq.com/s/16QfU8lZYChSckJWtcLiqg)
    - [网鼎杯-青龙组web题目writeup](https://mp.weixin.qq.com/s/E-lRUm1zPkEIxSoV7cHfow)
    - [2020网鼎杯青龙组_re_signal](https://mp.weixin.qq.com/s/uI2nLuM1K-J-fWBA-5Z7Zw)
    - [2020网鼎杯 青龙组 Android逆向题 rev01 WP](https://mp.weixin.qq.com/s/st6w3ax_DLHhd-AK5F509g)

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

- 朱雀组
    - [2020网鼎杯朱雀组云顿WP(入门向)](https://mp.weixin.qq.com/s/TpKXezPMZLx3VlejxlFyiQ)
    - [【网鼎杯2020朱雀组】Web WriteUp](https://www.cnblogs.com/vege/p/12907941.html)
    - [[re]go语言逆向：2020网鼎杯朱雀组re what wp](https://blog.csdn.net/Breeze_CAT/article/details/106195499)
    - [2020网鼎杯朱雀组_PHPweb](https://blog.csdn.net/gd_9988/article/details/106181577)
    - [2020网鼎杯-朱雀组-部分wp](https://www.anquanke.com/post/id/205578)
    - [2020网鼎杯-朱雀组部分题目Writeup](https://www.kkzevip.com/?post=51)
    - [2020网鼎杯-朱雀组-Crypto、Misc(带视频) ](https://mp.weixin.qq.com/s/XYkgD_5Y0FcgsNqRAb_1Yw)

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
