# CobaltStrike

<p align="center">
    <img src="../../../assets/img/logo/cobaltstrike.png" width="30%"></a>
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**官网**
- https://www.cobaltstrike.com/

**教程**
- [aleenzz/Cobalt_Strike_wiki](https://github.com/aleenzz/Cobalt_Strike_wiki)
- [Cobalt Strike 4.0 手册翻译](https://blog.ateam.qianxin.com/post/cobalt-strike-40-shou-ce-fan-yi-2019-nian-12-yue-2-ri-geng-xin-ban-ben/)

**文章 & Reference**
- [cobalt strike 快速上手 [ 一 ] - FreeBuf专栏·攻防之路](https://www.freebuf.com/column/149236.html)
- [教你修改cobalt strike的50050端口 - 3HACK](https://www.3hack.com/note/96.html)
- [ryanohoro/csbruter: Cobalt Strike team server password brute force tool](https://github.com/ryanohoro/csbruter)

**工具/插件**
- [rmikehodges/cs-ssl-gen](https://github.com/rmikehodges/cs-ssl-gen) sslgen 将安装一个 letsencrypt 证书并从中创建一个 Cobalt Strike 密钥库.
- [uknowsec/SharpToolsAggressor](https://github.com/uknowsec/SharpToolsAggressor) - 内网渗透中常用的c#程序整合成cs脚本,直接内存加载.
- [DeEpinGh0st/Erebus](https://github.com/DeEpinGh0st/Erebus) CobaltStrike 后渗透测试插件
- [QAX-A-Team/EventLogMaster](https://github.com/QAX-A-Team/EventLogMaster) - RDP日志取证&清除插件
- [outflanknl/Spray-AD](https://github.com/outflanknl/Spray-AD) - Cobalt Strike工具，用于审核 AD 用户帐户中的弱密码

**爆破 cobaltstrike teamserver**
```bash
git clone https://github.com/ryanohoro/csbruter
cd csbruter
cat wordlist.txt | python3 csbruter.py xxx.xxx.xxx.xxx
```

**使用**
- 服务端

    `./teamserver <你的IP> <你的密码>`

- 客户端

    `java -Dfile.encoding=UTF-8 -javaagent:CobaltStrikeCN.jar -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -jar cobaltstrike.jar`

    或

    `javaw -Dfile.encoding=UTF-8 -javaagent:CobaltStrikeCN.jar -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -jar cobaltstrike.jar`
