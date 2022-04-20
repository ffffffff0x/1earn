# containerd

> 项目地址 : https://github.com/containerd/containerd

---

## 安装

如果你安装了docker,你的主机里就会有 containerd

所以这里略

## 使用

```bash
containerd -h

ctr -h
```

**pull image**
```bash
ctr images pull docker.io/library/golang:latest
ctr images ls -q    # -q for only the name
```

**delect image**
```bash
ctr images rm docker.io/library/redis:alpine
```

**从 Dockerfile 导入 containerd**
```bash
docker save -o hello-world.tar hello-world      # 将 image 保存为 .tar 文件
# docker save -o tar-filename.tar image-name

ctr images import hello-world.tar               # 导入
```

**创建容器**
```bash
ctr container create docker.io/library/golang:latest hello-1
```

**启动容器**
```bash
ctr task start hello-1
```

开启后默认进入容器,输入 whoami 查看

**删除容器**
```bash
ctr container rm hello-1
```
