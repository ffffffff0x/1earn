# Plan
`大多数人都高估了他们一天能做的事情，但低估了他们一年能做的事情。`
[TOC]

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

---

## 搜索引擎语法
- 包含关键字:`intitle:关键字`
- 包含多个关键字:`allintitle:关键字 关键字2`
- 搜索特定类型的文件:`关键字 filetype:扩展名` 例如`人类简史 filetype:pdf`
- 搜索特定网站的内容:`关键字 site:网址`
- 排除不想要的结果:`关键字 - 排查条件`,例如搜索 “运动相机”，但只想看 GoPro 品牌以外的产品`运动相机 -GoPro`
- 双引号的用处:例如：`"how to write a code"` 如果没有引号，搜索的大部分结果是以 `write code` 为关键字。包含引号后，会确保将完整的字符串做为期望的检索结果提交给搜索引擎。
