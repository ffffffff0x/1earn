# [Burp Suite](https://portswigger.net/)

## Target


## Proxy


## Intruder 爆破模块

**Target**

目标设定

**Positions**

确定要爆破的参数，爆破类型

![image](../../../../img/渗透/工具/burp/1.png)
- 狙击手模式（Sniper）——它使用一组 Payload 集合，依次替换 Payload 位置上（一次攻击只能使用一个 Payload 位置）被 § 标志的文本（而没有被 § 标志的文本将不受影响），对服务器端进行请求，通常用于测试请求参数是否存在漏洞。

- 攻城锤模式（Battering ram）——它使用单一的 Payload 集合，依次替换 Payload 位置上被 § 标志的文本（而没有被 § 标志的文本将不受影响），对服务器端进行请求，与狙击手模式的区别在于，如果有多个参数且都为 Payload 位置标志时，使用的 Payload 值是相同的，而狙击手模式只能使用一个 Payload 位置标志。

- 草叉模式（Pitchfork ）——它可以使用多组 Payload 集合，在每一个不同的 Payload 标志位置上（最多20个），遍历所有的 Payload。举例来说，如果有两个 Payload 标志位置，第一个 Payload 值为 A 和 B，第二个 Payload 值为 C 和 D，则发起攻击时，将共发起两次攻击，第一次使用的 Payload 分别为 A 和 C，第二次使用的 Payload 分别为 B 和 D。

- 集束炸弹模式（Cluster bomb） 它可以使用多组 Payload 集合，在每一个不同的 Payload 标志位置上（最多 20 个），依次遍历所有的 Payload。它与草叉模式的主要区别在于，执行的 Payload 数据 Payload 组的乘积。举例来说，如果有两个 Payload 标志位置，第一个 Payload 值为 A 和 B，第二个 Payload 值为 C 和 D，则发起攻击时，将共发起四次攻击，第一次使用的 Payload 分别为 A 和 C，第二次使用的 Payload 分别为 A 和 D，第三次使用的 Payload 分别为 B 和 C，第四次使用的 Payload 分别为 B 和 D。

**Payloads**

Payload Processing 配置加密规则,优先级由上往下,自动给字典编码

Payload Encoding 配置字典进行 URL 编码

**Options**


















## Extender 插件模块

下载、管理burp的插件

官方插件商店 https://portswigger.net/bappstore

大部分插件运行需要 [Jython](https://www.jython.org/downloads.html)、[JRuby](https://www.jruby.org/download) 环境












