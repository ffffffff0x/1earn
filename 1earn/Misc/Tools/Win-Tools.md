# Win-Tools

`天下苦阿三久矣`

**注:下列所有软件默认以名称顺序排列,不分先后高低**

**注:工具用的再出神入化也是工具,真正重要的还是人(使用者、开发者)**

**Thank**

没有他们就不会有这篇记录,感谢
- [Awesome-Windows](https://github.com/Awesome-Windows/Awesome/blob/master/README-cn.md#windows-10-%E8%AE%BE%E7%BD%AE)
- [AmazingApps/Amazing-Windows-Apps](https://github.com/AmazingApps/Amazing-Windows-Apps/blob/master/zh-CN/README.md)
- [老殁 | 殁漂遥 | 互联网分享精神，专注收藏分享](https://www.laomoit.com/)
- [大眼仔旭 | 爱软件 爱汉化 爱分享 - 博客型软件首页](http://www.dayanzai.me/)
- [【重灌狂人】](https://briian.com/)
- [Yanu - 分享优秀、纯净、绿色、实用的精品软件。](http://www.ccav1.com/)
- [胡萝卜周-欢迎访问胡萝卜周博客](http://www.carrotchou.blog/)
- [软件缘 - 精品绿软，品鉴独特！](https://www.appcgn.com/)

---

# Speed
一部分软件由于平时使用频率过高,为了方便寻找,特地单独列出这一部分

**clover**

仅纪念,综合考虑,现在(2019年至以后)不推荐使用

**DuktoR6**

**Everything**

**Listary**

**NetSpeedMonitor**

**notepad++**

**QTranslate**

**RightMenuMgr**

**Wox**

**添加管理员取得所有权**

**虚拟键盘**

## Compare
**Beyond Compare**

**Duplicate Cleaner**

**VisiPics**

**Wise Duplicate Finder**

## pdf
**SumatraPDF**

## trouble shooting
**17monipdb**

**cports**

**子网计数器**

### dns
**dnschooser**

**DnsJumper**

**Pcap_DNSProxy**

**SimpleDNSCrypt64**

### ipconfig
**NetSetMan**

### ping
**pinginfoview**

**逗比超级Ping**

**科来Ping工具**

### snmp
**Paessler_SNMP_Tester**

### 安全
**火绒-sysdiag**

**智量-WiseVector**

#### ark tool
**PCHunter**

**PowerTool**

**WinObj**

#### 行为分析
**ProcessExplorer**

**ProcessMonitor**

**Total_Uninstall**

#### 审计
**GlassWireSetup**

**PrivateWin10**

**SterJo NetStalker**

**TCPView**

#### 系统优化
**CCleaner**

**DiskMax**

**Dism++**

**geek**

**金山垃圾清理**

### 护眼
**flux**

**fmminst**

**护眼宝**

**LightBulb**

### 浏览器
**Firefox**

**Chrome**

**chromium**

**ungoogled-chromium**

**Brave**

**Vivaldi**

### 视频播放器
**PotPlayer**

**VLC**

**WebTorrent**

### 鼠标手势
**WGestures**

**StrokeIt**

**strokesplus**

### 图片查看
**JPEGview**

**HONEYVIEW**

配合油猴脚本可以查看pixiv动图

**ImageGlass**

**XnView**

### 小窗预览
**OnTopReplica**

**PiP-Tool**

### 虚拟鼠标
**mouse**

**sharkmouse**

### 压缩
**7z**

**CompactGUI**

**winrar**

---

# 辅助+工作
## bat脚本
**重建图标缓存**
```sh
rem 关闭Windows外壳程序explorer
taskkill /f /im explorer.exe
rem 清理系统图标缓存数据库
attrib -h -s -r "%userprofile%\AppData\Local\IconCache.db"
del /f "%userprofile%\AppData\Local\IconCache.db"
attrib /s /d -h -s -r "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\*"
del /f "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db"
del /f "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db"
del /f "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_102.db"
del /f "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db"
del /f "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db"
del /f "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db"
del /f "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db"
rem 清理 系统托盘记忆的图标
echo y|reg delete "HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify" /v IconStreams
echo y|reg delete "HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify" /v PastIconsStream
rem 重启Windows外壳程序explorer
start explorer
```

## 活动演示
**ZoomIt**

**星韵全能抽奖**

## 美化
**changesize**

**DisplayFusion+Pro+**

**Fliqlo**

**rainmeter**

**StartIsBack**

**Windows10_DPI_FIX**

**媒体控制栏**

## 文档写作
**myBase**

**pandoc**

### markdown
**typora**

**yu-writer**


## 文件夹
**Multrin**

**Q-Dir**

**Total Commander**

**WindowTabs**

## 右键
**Files 2 Folder**

**任意地方打开CMD**

**ControlPanel**

**unlocker**

## 增强功能
**Switcheroo**

文件夹互换姓名

**FastCopy & FastCopy-M**

加速文件复制

**Textify**

复制无法选中的文本

**Ditto**

剪贴板增强

**DeskPin**

将窗口钉在最上层

**QuickLook**

空格预览文件

**Seer**

空格预览文件

**Renamer**

批量更名

**FileLocator Pro**

搜索文件的内容

**SpaceSniffer**

图形显示硬盘文件

**TreeSizeFree**

图形显示硬盘文件

**AltTabTer**

增强Alt+Tab时的效果

**rolan2**

**Traymond**

---

# 本地专用
## Shell-起服务
**finalshell**

**MobaXterm**

**SecureCRT**

**VNC**

**Xshell**


### ftp
**3CD**

**FlashFXP**

**Xftp**

### http
**hfs265**

**netbox**


## U盘相关
**ChipGenius**

### 启动盘制作
**dd**

**Etcher**

**LinuxLive USB Creator**

**MBROSTool**

**rufus**

**UltraISO**

**WePE**

**win32diskimager**


## 安全
**Windows Install Clean Up**

### Win10
**W10Privacy**

**Wub**

**wumt**

**wushowhide.diagcab**

### 管理启动项
**Autoruns**

### 加密
**FileLocker**

### 驱动
**3DM游戏运行库合集**


**aio-runtimes**

**DDU**

**EasyDrv系列**

itsk出品的驱动安装包,安装前记住装个火绒,帮你拦截下捆绑

### 系统
#### 备份系统
**EasyBackup**

**OneKey**

#### 封装
**nLite**

**NTLite**

#### 引导记录
**EasyBCD**

**主引导记录编辑器**

#### 硬盘分区
**DiskGenius**

**PAGreen**

### 注册表
**RegJump**

## 局域网传输/远程控制
**AnyDesk**

**Dukto**

**内网通-nwt**

**SendAnywhere**

**SoundWire**

**spacedesk**

**SWYH**

**TeamViewer**


## 跑分/硬件检测
**3DMark**

**AIDA64**

**HWiNFO**

**memtest86**

### 测CPU的
**CINEBENCHR**

**cpu-z**

**Fritz Chess Benchmark**

**super_pi**

### 测显卡的
**FurMark**

**nvidiaInspector**

### 硬盘测试
**AS+SSD+Benchmark**

**ATTO Disk Benchmarks**

**CrystalDiskInfo**

**HDTunePro**

**SSDlife Pro**

## 音频图像
### 视频处理
**ffmpeg**

**HandBrake**

**格式工厂**

**小丸工具箱**

### 图片处理
**Metanull**

**Ulead GIF Animator**

#### ASCII
**Ascgen2**

图片像素化

**Textaizer Pro**

制作文字和 ASCII 拼图

#### ico图标制作
**icofx**

#### 二维码生成
**myqr**

#### 截图工具
**FSCapture**

**GifCam**

**licecap**

**ShareX**

**Snipaste**

**WINSNAP**

#### 晶片化图像
**ImageTriangulator5**

#### 屏幕取色
**ColorPix**

#### 去水印
**InPaintPortable**

#### 思维简图
**MindManager**

**DesktopNaotu**

**XMind-ZEN**

#### 图片放大
**PhotoZoom**

#### 图片压缩
**Imagine**

**pinga**

**GiffingTool**

---

# 联网专用
## sync
**坚果云-Nutstore**

**Resilio-Sync**

**OneDrive**

**google drive**

## 浏览器
### 插件
**沙拉查词**

**隐私獾**

**Adblock**

**Archive URL**

**Cookie AutoDelete**

**Decentraleyes**

**FoxyProxy Standard**

**HTTPS Everywhere**

**Imagus**

**LastPass: Free Password Manager**

**Octotree**

**OneTab**

**Pixiv Batch Downloader**

**Save To The Wayback Machine**

**Stylus**

**Tampermonkey**

**User-Agent Switcher**

**View Image**

**Zoom Page WE**

#### 推荐但不常使用
**NoScript**
**uBlock Origin**

## 下载
**annie**

**aria2**

**FDM**

**IDM**

**persepolis**

**you-get**
