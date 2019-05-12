# Misc-Plan
[TOC]

---

# 激活
注意：Windows系统和Micrsoft Office软件都必须是VOL版本。
**激活Windows**
用管理员权限运行CMD或PowerShell，输入如下命令：
```powershell
slmgr /skms xxx.xxx.xxx.xxx
slmgr /ato
slmgr /xpr
```
验证一下是否激活：
`slmgr.vbs -dlv`

**激活Office**
用管理员权限运行CMD或PowerShell，输入如下命令：
```powershell
# 进入office安装目录
cd “C:\Program Files(x86)\Microsoft Office\Office16”
# 注册kms服务器地址
cscript ospp.vbs /sethst:xxx.xxx.xxx.xxx
# 执行激活
cscript ospp.vbs /act
# 查看状态
CSCRIPT OSPP.VBS /DSTATUS
```

# DNS
**软件方案**
- DnsJumper（windows下快速配置DNS）
- Pcap_DNSProxy（本地自定义分割DNS解析请求）
    ```ini
    [DNS]
    Outgoing Protocol = IPv4 + TCP

    [Addresses]
    IPv4 Main DNS Address = 208.67.220.222:443
    IPv4 Alternate DNS Address = 208.67.220.220:53|208.67.222.222:5353
    IPv4 Local Main DNS Address = 119.29.29.29:53
    IPv4 Local Alternate DNS Address = 114.114.115.115:53
    ```

**服务器推荐**
- 国内:110.6.6.6、14.114.114.114
- 全球:208.67.222.222、208.67.220.220

---

# 各种代理/源
## git
```git
// 查看当前代理设置
git config --global http.proxy

// 设置当前代理为 http://127.0.0.1:1080 或 socket5://127.0.0.1:1080
git config --global http.proxy 'http://127.0.0.1:1080'
git config --global https.proxy 'http://127.0.0.1:1080'
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080' 

// 删除 proxy git config --global --unset http.proxy
git config --global --unset https.proxy
```

## Docker镜像加速
阿里云：https://cr.console.aliyun.com/#/accelerator
DaoCloud：https://www.daocloud.io/mirror#accelerator-doc

**linux**
```bash
sudo mkdir -p /etc/docker
```
```vim
vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://hpcqgbsb.mirror.aliyuncs.com"]
}
```
```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

`docker info` 检查加速器是否生效

**windows**
对于Windows 10以上的用户 推荐使用Docker for Windows
Windows安装文件：http://mirrors.aliyun.com/docker-toolbox/windows/docker-for-windows/

在系统右下角托盘图标内右键菜单选择 Settings，打开配置窗口后左侧导航菜单选择 Docker Daemon。编辑窗口内的JSON串，填写下方加速器地址：
{
  "registry-mirrors": ["https://hpcqgbsb.mirror.aliyuncs.com"]
}
编辑完成后点击 Apply 保存按钮，等待Docker重启并应用配置的镜像加速器。

## node&js
```bash
npm install -g nrm
nrm ls
nrm use taobao
nrm test
或
npm config set proxy=http://127.0.0.1:8087
```

## pip源
常用的国内镜像包括：
1. 阿里云 http://mirrors.aliyun.com/pypi/simple/
2. 豆瓣http://pypi.douban.com/simple/
3. 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
4. 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
5. 华中科技大学http://pypi.hustunique.com/

- 临时使用：
可以在使用pip的时候，加上参数-i和镜像地址`https://pypi.tuna.tsinghua.edu.cn/simple`
例如：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas`，这样就会从清华镜像安装pandas库。

- 永久修改，一劳永逸：
    1. Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)
    ```vim
    mkdir -p ~/.pip/
    vim ~/.pip/pip.conf
        [global]
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple
        [install]
        trusted-host = https://pypi.tuna.tsinghua.edu.cn
    ```

    2. windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，然后新建文件pip.ini，即 %HOMEPATH%\pip\pip.ini，在pip.ini文件中输入以下内容（以豆瓣镜像为例）：
    ```vim
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    [install]
    trusted-host = https://pypi.tuna.tsinghua.edu.cn
    ```

## 终端
**proxychains**
详细安装步骤请移步运维-->Linux-->[Power-Linux.md](../../运维/Linux/Power-Linux.md)
- 使用方法:
    在需要代理的命令前加上 proxychains4,如:
    `proxychains4 wget http://xxx.com/xxx.zip`

---

# 搜索引擎语法
- 包含关键字:`intitle:关键字`
- 包含多个关键字:`allintitle:关键字 关键字2`
- 搜索特定类型的文件:`关键字 filetype:扩展名` 例如`人类简史 filetype:pdf`
- 搜索特定网站的内容:`关键字 site:网址`
- 排除不想要的结果:`关键字 - 排查条件`,例如搜索 “运动相机”，但只想看 GoPro 品牌以外的产品`运动相机 -GoPro`
- 双引号的用处:例如：`"how to write a code"` 如果没有引号，搜索的大部分结果是以 `write code` 为关键字。包含引号后，会确保将完整的字符串做为期望的检索结果提交给搜索引擎。

---

# vscode 配置
```yml
"editor.fontFamily": "Fira Code Retina, 'Microsoft YaHei UI', Arial Black"
"editor.fontLigatures": true
```

---

# ffmpeg
**视频合并**
```bash
file '0.flv'
file '1.flv'
file '2.flv'
file '3.flv'
ffmpeg -f concat -i filelist.txt -c copy output.mkv
```

**视频压缩**
`ffmpeg.exe -i "E:\Temp\002.mp4" -r 10 -b:a 32k "E:\Temp\002_mod.mp4"`常规用法
`ffmpeg -y -i /mnt/sdcard/demo1.mp4 -strict -2 -vcodec libx264 -preset ultrafast -crf 24 -acodec aac -ar 44100 -ac 2 -b:a 96k -s 360x640 -aspect 16:9 /mnt/sdcard/democompress.mp4`优秀用法

```bash
`ffmpeg -y -i in.mp4 -s 176x144 -vcodec libx264 -vpre fast -b 800000 out.mp4`
in.mp4是960 x 540，H.264 / AVC，30fps，大小为149.3 MB。
转出来的out.mp4是176 x 144，H.264 / AVC，30fps，大小为21.0 MB。

y: 当已存在out.mp4是，不提示是否覆盖。
-i in.mp4: 输入文件名。
-s 176x144: 输出分辨率。 
-vcodec -libx264: 输出文件使用的编解码器。
-vpre fast: 使用libx264做为编解码器时，需要带上这个参数。
-b 800000: 码率，单位是字节，不是k字节。
out.mp4: 输出文件名。
以上参数的使用细节，ffmpeg的help里有更详细的描述。 
```

```bash
ffmpeg -y -i in.out -vcodec xvid -s 176x144 -r 29.97 -b 1500 -acodec aac -ac 2 -ar 48000 -ab 128 -vol 100 -f mp4 out.mp4
-r 29.97 帧数 (一般用25就可以了)
-b 1500 视频数据流量，用-b xxx表示使用固定码率，数字可更改；还可以用动态码率如：-qscale 4和-qscale 6，4的质量比6高（一般用800就可以了，否则文件会很大）
-acodec aac 音频编码用AAC
-ac 2 声道数1或2
-ar 48000 声音的采样频率
-ab 128 音频数据流量，一般选择32、64、96、128#-vol 200 200%的音量，可更改（如果源文件声音很小，可以提升10到20倍(1000%~2000%)，我试过，效果还行！但不能太大，200000%我也试验过，但嘈杂声太大了）
```

**Reference**
- [使用ffmpeg合并视频文件的三种方法](https://blog.csdn.net/u012587637/article/details/51670975)
- [FFmpeg压缩MP4视频](https://blog.csdn.net/lakeheart879/article/details/78736634)
- [怎样用ffmpeg 压缩视频](https://blog.csdn.net/lakeheart879/article/details/78736634)

---

# Reference
- [Wind4/vlmcsd: KMS Emulator in C (currently runs on Linux including Android, FreeBSD, Solaris, Minix, Mac OS, iOS, Windows with or without Cygwin)](https://github.com/Wind4/vlmcsd)
- [基于 vlmcsd 搭建 KMS 服务器 - 简书](https://www.jianshu.com/p/11d51983852e)
- [chengr28/Pcap_DNSProxy: Pcap_DNSProxy, a local DNS server based on packet capturing](https://github.com/chengr28/Pcap_DNSProxy)
- [git 配置代理命令 - 阿兴的平凡世界 - 博客园](https://www.cnblogs.com/gx1069/p/6840413.html)
- [npm 配置镜像、设置代理 - MockingBird 博客 - SegmentFault 思否](https://segmentfault.com/a/1190000002589144)
- [将 pip 源更换到国内镜像 - LittleBee的博客 - CSDN博客](https://blog.csdn.net/sinat_21591675/article/details/82770360)
- [你真的会使用搜索引擎吗？](https://mp.weixin.qq.com/s/le_zYcDfhSLvbuu99LprMQ)
- [VSCode 好看字体](https://blog.csdn.net/s1124yy/article/details/82315988)
- [tonsky/FiraCode](https://github.com/tonsky/FiraCode)
