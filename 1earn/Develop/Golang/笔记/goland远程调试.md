# goland 远程调试

---

本地的gopath和远端机器不需要一致，go版本也不需要一致

---

## 远端机器

**go**

需要安装 go 环境,可以用 f8x 装
```bash
wget -O f8x https://f8x.io/ && mv --force f8x /usr/local/bin/f8x && chmod +x /usr/local/bin/f8x
f8x -go
```

**dlv**

装一个delve

```bash
export GO111MODULE=on && export GOPROXY=https://goproxy.io
go install -v github.com/go-delve/delve/cmd/dlv@latest
which dlv
ln -s /root/go/bin/dlv /usr/local/bin/dlv
dlv
```

---

## 本地

检测下 goland 是否自带 `FTP/SFTP/WebDAV Connectivity` 插件

**添加远程服务器信息**

点击tools->deployment->configuration

添加一个 sftp

添加远程服务器,添加映射

**测试上传**

tools->deployment->upload to

**开始调试**

右上角的配置,选择go remote

配置远程服务器信息，端口使用默认

会给出远端需要运行的命令
```bash
dlv debug --headless --listen=:2345 --api-version=2
```

远端运行后,即可正常调试
