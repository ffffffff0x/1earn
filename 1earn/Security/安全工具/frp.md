# frp

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**简介**

frp 是一个专注于内网穿透的高性能的反向代理应用，支持 TCP、UDP、HTTP、HTTPS 等多种协议。可以将内网服务以安全、便捷的方式通过具有公网 IP 节点的中转暴露到公网。

**项目地址**
- https://github.com/fatedier/frp

---

## 安装

linux 配置方式见如下链接🔗
- [frp安装配置](../../../../Integrated/Linux/Power-Linux.md#frp)

---

## 配置案例

- https://gofrp.org/docs/examples/
- [配置frp内网穿透](https://www.feios.me/build-frp-server/)

**frp 实验 : 通过 SSH 访问内网机器**

- 公网 IP 的机器上(1.1.1.1)

    部署 frps，修改 frps.ini 文件，这里使用了最简化的配置，设置了 frp 服务器用户接收客户端连接的端口：
    ```ini
    [common]
    bind_port = 7000
    ```

    启动 frps

- 内网机器上(172.16.1.1)

    部署 frpc，修改 frpc.ini 文件
    ```ini
    [common]
    server_addr = 1.1.1.1
    server_port = 7000

    [ssh]
    type = tcp
    local_ip = 127.0.0.1
    local_port = 22
    remote_port = 6000
    ```
    local_ip 和 local_port 配置为本地需要暴露到公网的服务地址和端口。remote_port 表示在 frp 服务端监听的端口，访问此端口的流量将会被转发到本地服务对应的端口。

    启动 frpc

- 外部访问

    此时通过 SSH 访问内网机器 172.16.1.1，假设用户名为 test：
    ```
    ssh -oPort=6000 test@1.1.1.1
    ```

    frp 会将请求 1.1.1.1:6000 的流量转发到内网机器 172.16.1.1 的 22 端口

**frp 实验 : 通过 RDP 访问内网机器(STCP)**

- 公网 IP 的机器上(1.1.1.1)

    部署 frps，修改 frps.ini 文件
    ```ini
    [common]
    bind_port = 24880
    authentication_method = token
    token = token
    tls_only = true
    ```

    启动 frps
    ```
    ./frps -c frps.ini
    ```

- 内网机器上(172.16.1.1)

    部署 frpc，修改 frpc.ini 文件
    ```ini
    [common]
    server_addr = 1.1.1.1
    server_port = 24880
    authentication_method = token
    token = token
    tls_enable = true

    [frp]
    type = stcp
    sk = token
    local_ip = 127.0.0.1
    local_port = 3389
    # true 启用加密
    use_encryption = false
    # true 启用压缩
    use_compression = true
    ```

    启动 frpc
    ```
    ./frpc.exe -c frpc.ini
    ```

- 主力机器(192.168.1.1)

    部署 frpc，修改 frpc.ini 文件
    ```ini
    [common]
    server_addr = 1.1.1.1
    server_port = 24880
    authentication_method = token
    token = token
    tls_enable = true

    [frp_visitor]
    type = stcp
    # stcp 的访问者
    role = visitor
    # 要访问的 stcp 代理的名字
    server_name = frp
    # 只有 sk 一致的用户才能访问到此服务
    sk = token
    # 绑定本地端口用于访问 远程桌面 服务
    bind_addr = 127.0.0.1
    bind_port = 6000
    use_encryption = false
    use_compression = false
    ```

    启动 frpc
    ```
    ./frpc.exe -c frpc.ini
    ```

    rdp 127.0.0.1:6000

**frp 实验 : 映射本地 http 服务到公网 vps 上,并且绑 host www.test123.com**

- 公网 IP 的机器上(1.1.1.1)

    部署 frps，修改 frps.ini 文件
    ```ini
    [common]
    bind_port = 8080
    authentication_method = token
    token = token
    vhost_http_port = 80
    ```

    启动 frps
    ```
    ./frps -c frps.ini
    ```

- 内网机器上(172.16.1.1)

    部署 frpc，修改 frpc.ini 文件
    ```ini
    [common]
    server_addr = 1.1.1.1
    server_port = 8080
    token=token

    [web]
    type = http
    local_port = 80
    custom_domains = www.test123.com
    ```

    启动 frpc
    ```
    ./frpc.exe -c frpc.ini
    ```

- 测试

    ```
    curl http://1.1.1.1 -H "Host:www.test123.com"
    ```
