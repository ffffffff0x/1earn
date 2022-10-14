# Suricata

<p align="center">
    <img src="../../../assets/img/logo/Suricata.png" width="22%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**官网**
- https://suricata-ids.org/

**项目地址**
- https://github.com/OISF/suricata

**简介**

Suricata 是由 OISF（开发信息安全基金会）开发，它也是基于签名，但是集成了创新的技术。该引擎嵌入了一个 HTTP 规范化器和分析器（HTP 库），可提供非常先进的 HTTP 流处理，从而能够在 OSI 模型的第七层（应用层）上解析流量。

Suircata 是一款支持 IDS 和 IPS 的多线程入侵检测系统，与传统 Snort 相比，Suircata 的多线程和模块化设计上使其在效率和性能上超过了原有 Snort，它将 CPU 密集型的深度包检测工作并行地分配给多个并发任务来完成。这样的并行检测可以充分利用多核硬件的优势来提升入侵检测系统的吞吐量，在数据包的深度检测上效果优越。并且 Suircata 可以兼容现有的 Snort 规则签名，还增加了对 ipv6 的支持，已经逐渐成为传统 Snort 入侵检测系统的代替方案。

**相关文章**
- [Suricata工控规则研究](https://www.freebuf.com/articles/ics-articles/237420.html)
- [Suricata IDS 入门 — 规则详解](https://www.secpulse.com/archives/71603.html)
- [使用Suricata和ELK进行流量检测](https://zhuanlan.zhihu.com/p/64742715)
- [Suricata规则介绍、以及使用suricata-update做规则管理](https://zhuanlan.zhihu.com/p/36340468)
- [suricata下的挖矿行为检测](https://www.freebuf.com/articles/network/195171.html)
- [Suricata + Lua实现本地情报对接](https://www.freebuf.com/sectool/218951.html)

**架构**

Suricata 有三种运行模式，分别为 single，workers，autofp。官方推荐性能最佳的运行模式为 workers 模式。
- single 模式：只有一个包处理线程，一般在开发模式下使用。
- workers 模式：多个包处理线程，每个线程包含完整的处理逻辑。
- autofp 模式：有多个包捕获线程，多个包处理线程。一般适用于 nfqueue 场景，从多个 queue 中消费流量来处理。

报文检测系统通常包含四大部分，报文获取、报文解码、报文检测、日志记录；Suricata 不同的功能安装模块划分，一个模块的输出是另一个模块的输入。

---

## 安装部署

**Ubuntu 下安装**
```bash
add-apt-repository ppa:oisf/suricata-stable
apt update
apt install -y suricata jq
apt install -y suricata-update
```

### 基础使用
```bash
suricata-update # 更新规则
suricata -T     # 测试运行

suricata -i ens33 -c /etc/suricata/suricata.yaml -vvv       # 启动运行
# 注: 这里 -vvv 参数建议加上. 如果你的Lua脚本有一些问题, 如果加上了这个参数, 就可以通过 suricata.log 日志看出。

suricata -r <path>  -c /etc/suricata/suricata.yaml -vvv     # 在PCAP脱机模式（重放模式）下运行，从PCAP文件读取文件。如果<path>指定了一个目录，则该目录中的所有文件将按修改时间的顺序进行处理，以保持文件之间的流状态。
```

### 配置文件

`/etc/suricata/` 目录下有 4 个配置文件和一个文件夹, 作用分别是:
- classification.config : 定义了各种流量攻击类型和优先级，类似拒绝服务攻击和 web 应用攻击等
- reference.config : 记录一些安全网站，漏洞平台的网址，或者是自己可以自定义的 url，是参考的意思，用来联系外部的恶意攻击检测网站中关于此类攻击的页面。
- suricata.yaml : Suricata 默认的配置文件，以硬编码的形式写在源代码中, 里面定义了几乎关于 Suricata 的所有运行内容，包括运行模式、抓包的数量和大小、签名和规则的属性和日志告警输出等等。
    - 先设置 `HOME_NET` 与 `EXTERNAL_NET`，推荐 `HOME_NET` 填写内网网段，`EXTERNAL_NET` 设置为 `any`
    - 如果 `HOME_NET` 设置了 `any`，`EXTERNAL_NET` 设置 `!$HOME_NET` 的话会报错，如果 `HOME_NET` 设置了内网地址，`EXTERNAL_NET` 设置为 `!$HOME_NET` 的话，有些内网之间的告警就无法匹配到
- threshold.config : threshold（阈值）关键字可用于控制规则的警报频率，可用于在规则生成警报之前为其设置最小阈值.
- rules : 规则目录, 存放不同种类的规则，规则用来判定流量攻击类型，并定义攻击类型和告警种类，可以存放自带的规则，也可以自己按规则语法编写

---

## 规则详解

suricata 完全兼容 snort 规则
```
alert modbus any any -> any any (msg:"SURICATA Modbus Request flood detected"; flow:to_server;app-layer-event:modbus.flooded; classtype:protocol-command-decode; sid:2250009; rev:2;)

- alert：                                           默认顺序为：pass，drop，reject，alert，跳过、丢弃、拒绝、警告四种类型的动作
- Modbus：                                          注明协议种类，UDP/ICMP 等
- Any：                                             源地址 / 目的地址（IP）
- Any：                                             源端口 / 目的端口
- ->：                                              方向，单向流量；<> 双向流量
- Any：                                             源地址 / 目的地址（IP）
- Any：                                             源端口 / 目的端口
- msg:”SURICATA Modbus Request flood detected”：    关键字 msg 提供对触发警报的有关签名 / 规则相关文本提示信息
- flow:to_server：                                  客户端到服务器
- app-layer-event:modbus.flooded：                  具体攻击内容
- classtype:protocol-command-decode：               提供有关规则和警报分类的信息，由 classification.config 文件定义。
- sid:2250009：                                     用于唯一性规则标识，sid 不能重复
- rev:2：                                           规则版本号，每次修改规则 rev 则递增 1
```

> 以下内容来自文章 <sup>[[Suricata IDS 入门 — 规则详解](https://www.secpulse.com/archives/71603.html)]</sup>

完整规则
```
alert  tcp $EXTERNAL_NET $FILE_DATA_PORTS -> $HOME_NET any (msg:"INDICATOR-SHELLCODE  heapspray characters detected - ASCII     "; flow:to_client,established; file_data; content:"0d0d0d0d";  fast_pattern:only; metadata:service ftp-data, service http,service imap, service  pop3;  reference:url,sf-freedom.blogspot.com/2006/07/heap-spraying-internet-exploiter.html;  classty    pe:attempted-user; sid:33339;  rev:1;)
```

- `alert  tcp $EXTERNAL_NET $FILE_DATA_PORTS -> $HOME_NET any`
- ` 规则行为 协议 源 ip 源端口 流量方向 目标 ip 目标端口   红色代表规则头 `
    - 规则行为，根据优先级排列：
        - `pass`        如果匹配到规则后，suricata 会停止扫描数据包，并跳到所有规则的末尾
        - `drop`        ips 模式使用，如果匹配到之后则立即阻断数据包不会发送任何信息
        - `reject`      对数据包主动拒绝，接受者与发送中都会收到一个拒绝包
        - `alert`       记录所有匹配的规则并记录与匹配规则相关的数据包
    - 协议：在规则中指定匹配那些协议，suricata 支持的协议要比 snort 多一些
        - TCP、UDP、ICMP、IP（同时用与 TCP 与 UDP）、http、ftp、smb、dns
    - 源 ip，目标 ip：
        - 支持单个 ip，cidr，ip 组，[96.30.87.36,96.32.45.57]，所有主机 any，以及规则文件中配置的 ip 变量 `$HOME_NET`（受保护的 ip 段）与 `$EXTERNAL_NET`（其他所有 ip）：
    - 源端口 / 目标端口：
        - 支持设置单个端口 80，端口组 [80,8080], 端口范围[1024:65535] 以及 any 任意端口, 还可以在配置文件中添加端口组，通过 `!` 号来进行排除
    - 流量方向：
        - `->`          单向流量，从源 ip 到目标 ip 的单项流量
        - `<>`          双向流量，2 个 ip 往返之间的流量
- 规则体 : `(msg:"INDICATOR-SHELLCODE  heapspray characters detected - ASCII"; flow:to_client,established; file_data; content:"0d0d0d0d";  fast_pattern:only; metadata:service ftp-data, service http,service imap, service  pop3;  reference:url,sf-freedom.blogspot.com/2006/07/heap-spraying-internet-exploiter.html;  classtype:attempted-user; sid:33339; rev:1;)`
    - MSG：规则名称，规则中的第一个字段
        - ids 告警上显示的信息，INDICATOR-SHELLCODE  heapspray  characters detected - ASCII
    - 源 ip、目标 ip 检测：
        - sameip 会将流量中源 ip 和目标 ip 相同的显示出来
        - `alert  ip any any -> any any (msg:"GPL SCAN same SRC/DST"; sameip;  reference:bugtraq,2666; reference:cve,1999-0016;  reference:url,www.cert.org/advisories/CA-1997-28.html; classtype:bad-unknown;  sid:2100527; rev:9; metadata:created_at 2010_09_23, updated_at 2010_09_23;)`
    - flow 流匹配：
        - flow 是特定时间内具有相同数据的数据包（5 元组信息）同属于一个流，suricata 会将这些流量保存在内存中。
        - flowbits set , name       设置条件
        - flowbits isset, name      选择条件
        - 一旦设置 flowbits 之后，第一条规则没有命中那么第二条规则即使命中了也不会显示出来，例如一些攻击行为的响应信息，现在请求中设置条件，然后在响应中选择条件
        - to_client/from_server     服务器到客户端
        - to_server/from_client     客户端到服务器
        - established               匹配已经建立连接的（tcp 则是经过 3 次握手之后，udp 则是有双向流量）
        - no_established            匹配不属于建立连接的
        - only_stream               匹配由流引擎重新组装的数据包
        - no_stream                 不匹配流引擎重新组装的数据包
    - 阀值 threshold：
        - threshold:  `type <threshold|limit|both>, track <by_src|by_dst>, count <N>,  seconds <T>`
        - threshold     最小阀值  也就是说只有匹配到至少多少次数才进行告警
        - limit         限制告警次数，例如最少 5 分钟内告警一次
        - 调节阀值主要是通过 2 种方法，一种是通过规则内的 threshold 关键字来调节，下图中类型是 limit 也就是限制告警次数，track  by_s rc 代表来源 ip，seconds 60 每个 60 秒告警一次 count 1
        - 另外一种则是通过配置文件 /etc/suricata/threshold.config 来进行控制，更加推荐这种方法，写在规则内部每次更新后都会替换掉。
        - `event_filter gen_id 1（组 id）, sig_id  1101111（规则 id）, type limit ,track by_src, count 1 ,  seconds 60`
        - suppress 则是告警排除，排除指定 ip 产生的规则告警
    - 内容匹配 content：检测数据包中是否存在此内容，例如检测流量中是否存在 0d0d0d0d
        - 如果有多个匹配项可以使用 `content:"evilliveshere";   content:"here";` 这种写法，注意如果没有用内容修饰的话，ids 不会按照先后顺序去匹配的，只会在内容中匹配是否包含这 2 个值，必须用内容修饰来调整先后顺序，用 distance 0 来让第二个匹配项在第一个匹配项匹配位置之后匹配，并且如果有多个 content 他们的关系是 and 关系必须都匹配到才告警 。
        - 使用感叹号 `!` 对匹配项的否定：`content:!"evilliveshere"`;
        - 将字符串的十六进制用管道符（|）进行包围：content:"|FF D8|"; 字符串与十六进制混合使用：content:"FF |SMB|25 05 00 00 80";
        - 匹配内容区分大小写，保留字符（; \ "|）须进行转义或十六进制转码
        - 内容修饰，能够更加精准匹配
        - 不区分大小写 nocase：
            - content:"root";nocase;                修饰符直接在；号后面添加
        - 偏移位置 offset：
            - content:"xss";offset 100;             代表了从数据包开始位置 0 往后偏移 100 位字节后进行匹配
        - 结束位置 depth：
            - content:"xss";offset 100;depth 200;   代表了匹配数据包结束的位置，如果没有 offset 则是从开始位置计算，有 offset 则是从 offset 开始，此次则是从 100 字节开始匹配到 200 字节内的内容。
        - 在 xx 范围外 distance ：
            - 本次匹配必须在上一次匹配结束位置到 distance 设置的偏移位置区间之外，例如 content:"msg1";content:"msg2";distance 25; 如果 msg1 在第 100 行找到，那么就会在 100+25 后匹配 msg2
        - 在 xx 范围内 within：
            - 本次匹配必须在上一次匹配结束位置之内，如果上次结束是 100，within 15；那么第二次匹配必须在 100 到 115 之内开始匹配, 如果 within 与 distance 同时出现 content:"evilliveshere";  content:"here";  distance:1;within:7; 则匹配 here 在 evilliveshere 位置结束 1-7 内匹配
        -  Payload 大小 dsize：
            - dsize: >64                        用来匹配 payload 大小，可以用来检测异常包大小
        - pcre 正则  pcre：
            - content:"xss"; pcre:"xss\w"       先匹配 content 内容后才进行匹配 pcre 正则，这样的话减少系统开销
        - http 修饰符：
            - 更多详细内容查看：http://suricata.readthedocs.io/en/suricata-4.0.4/rules/http-keywords.html
            - `alert  tcp any any -> any 80(msg:"Evil Doamin www.appliednsm.com";  "content:"GET";httpmethod;   content:"www.appliednsm.com";http_uri; sid:5445555; rev:1;)`
            - http_client_body          HTTP 客户端请求的主体内容
            - http_cookie               HTTP 头字段的 “Cookie” 内容
            - http_header               HTTP 请求或响应头的任何内容
            - http_method               客户端使用的 HTTP 方法（GET，POST 等）
            - http_uri                  HTTP 客户端请求的 URI 内容
            - http_stat_code            服务器响应的 HTTP 状态字段内容
            - http_stat_message         服务器响应的 HTTP 状态消息内容
            - http_encode               在 HTTP 传输过程中所使用的编码类型
            - url_len                   url 长度
        - 快速匹配模式：
            - fast_pattern;             如果 suricata 规则中有多个匹配项目，快速匹配的目的是设置优先级最高的匹配项，如果设置了快速匹配模式没有命中则跳过这条规则
    - 元数据 Metadata：
        - suricata 会忽略元数据背后的语句，用于添加备注
    - 组 gid：
        - [1:2000000] 告警前面的 1 代表组 id
    - 优先级 priority：
        - 手动设置规则优先级别，范围 1-255，1 最高，一般都是 1-4，suricata 会首先检查优先级较高的规则
    - 引用 reference：
        - 连接外部信息来源，补充描述，reference:url,sf-freedom.blogspot.com/2006/07/heap-spraying-internet-exploiter.html
    - 类别 classtype：
        - 根据规则检测到的活动类型为规则分类，classtype:attempted-user
    - 特征标示符 sid：
        - 用于唯一性规则标识，sid 不能重复，0-10000000 VRT 保留，20000000-29999999 Emerging 保留，30000000+：公用
    - 修订 rev：
        - 规则版本号，每次修改规则 rev 则递增 1

### 规则修改

suricata 主要是 et/open 规则，这是系统自带的规则，目前开源免费的就是 et/open、pt 规则、sslbl 规则，其余的需要授权码才能更新

```bash
suricata-update list-sources    # 列出当前的规则源
suricata-update update-sources  # 更新规则源
suricata-update                 # 更新规则

suricata-update enable-source ptresearch/attackdetection    # 启用ptresearch/attackdetection的规则集
suricata-update disable-source et/pro                       # 关闭某个规则源
suricata-update remove-source et/pro                        # 删除某个规则源
```
例如要禁用某一个规则，直接新建 `/etc/suricata/disable.conf` 文件，然后在里面填入 sid，正则表达式，规则组名, 配置好 `disable.conf` 后，使用如下命令更新规则：
```bash
suricata-update --disable-conf /etc/suricata/disable.conf
```

使用 Suricata-update 更新规则时，默认是将所有规则合并在一个规则文件中：`/var/lib/suricata/rules/suricata.rules`,Suricata-update 有个 --no-merge 参数，使用这个参数更新规则，规则不会进行合并，是以独立的文件存在于文件夹下。但是在管理规则的时候很不方便，必须要自己管理 Suricata 引入的规则。

指定一个文件让 suricata-update 合并输出会更简单。在 suricata.yaml 中修改 default-rule-path 和 rule-files。
