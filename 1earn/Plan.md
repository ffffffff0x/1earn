# Plan
[TOC]

---

## 激活
注意：Windows系统和Micrsoft Office软件都必须是VOL版本。
**激活Windows**
用管理员权限运行CMD或PowerShell，输入如下命令：
```
slmgr /skms xxx.xxx.xxx.xxx
slmgr /ato
slmgr /xpr
```
验证一下是否激活：
`slmgr.vbs -dlv`

**激活Office**
用管理员权限运行CMD或PowerShell，输入如下命令：
```
# 进入office安装目录
cd “C:\Program Files\Microsoft Office\Office16”
# 注册kms服务器地址
cscript ospp.vbs /sethst:xxx.xxx.xxx.xxx
# 执行激活
cscript ospp.vbs /act
# 查看状态
CSCRIPT OSPP.VBS /DSTATUS
```

## DNS
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

## 各种代理/源
### git
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

### node&js
```bash
npm install -g nrm
nrm ls
nrm use taobao
nrm test
或
npm config set proxy=http://127.0.0.1:8087
```

### pip源
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
    index-url = http://pypi.douban.com/simple
    [install]
    trusted-host = pypi.douban.com
    ```


---

## 搜索引擎语法
- 包含关键字:`intitle:关键字`
- 包含多个关键字:`allintitle:关键字 关键字2`
- 搜索特定类型的文件:`关键字 filetype:扩展名` 例如`人类简史 filetype:pdf`
- 搜索特定网站的内容:`关键字 site:网址`
- 排除不想要的结果:`关键字 - 排查条件`,例如搜索 “运动相机”，但只想看 GoPro 品牌以外的产品`运动相机 -GoPro`
- 双引号的用处:例如：`"how to write a code"` 如果没有引号，搜索的大部分结果是以 `write code` 为关键字。包含引号后，会确保将完整的字符串做为期望的检索结果提交给搜索引擎。
