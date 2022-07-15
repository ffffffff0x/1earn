# RedGuard

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/wikiZ/RedGuard

---

## 介绍

RedGuard，是一款 C2 设施前置流量控制技术的衍生作品，有着更加轻量的设计、高效的流量交互、以及使用 go 语言开发具有的可靠兼容性。它所解决的核心问题也是在面对日益复杂的红蓝攻防演练行动中，给予攻击队更加优秀的 C2 基础设施隐匿方案，赋予 C2 设施的交互流量以流量控制功能，拦截那些 “恶意” 的分析流量，更好的完成整个攻击任务。

RedGuard 可以帮助你快速自建域前置.

---

## 安装

**本地编译安装**
```bash
git clone https://github.com/wikiZ/RedGuard.git
cd RedGuard
# You can also use upx to compress the compiled file size
go build -ldflags "-s -w"
# Give the tool executable permission and perform initialization operations
chmod +x ./RedGuard&&./RedGuard
```

**通过f8x安装**
```bash
wget -O f8x https://f8x.io/
bash f8x -rg
```

---

## 使用

**运行**
```
./RedGuard
```

**后台运行**
```
nohup ./RedGuard &
```

**配置文件**
```
~/.RedGuard_CobaltStrike.ini
```

---

## 配置举例

```ini
{"360.net":"http://127.0.0.1:8080","360.com":"https://127.0.0.1:4433"}
```

代表 host 头 `360.net` 会转发给 `http://127.0.0.1:8080`, host 头 `360.com` 会转发给 `https://127.0.0.1:4433`

在未授权情况下，得到的响应信息也是重定向的站点返回信息。

---

## 自定义 CA

将自己的证书重命名为 ca.crt 和 ca.key 覆盖在 cert-rsa/ 目录，启动 rg 即可

---

## 自建域前置

前面3台 RedGuard ,后面1台 cs
```
RedGuard1 ⎺⎺⎺⎱
RedGuard2 ⎼⎼⎼⎼cs
RedGuard3 ⎽⎽⎽⎰
```

cs 配置 3台 rg 的地址，header 头改为 rg 配置的即可
