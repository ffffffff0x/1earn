# openssl

---

## 什么是x509证书链

x509 证书一般会用到三类文件，key，csr，crt.

- Key 是私用密钥，openssl 格式，通常是 rsa 算法.
- csr 是证书请求文件，用于申请证书.在制作 csr 文件的时候，必须使用自己的私钥来签署申请，还可以设定一个密钥.
- crt 是 CA 认证后的证书文件(windows 下面的 csr，其实是 crt)，签署人用自己的 key 给你签署的凭证.

---

## openssl 中有如下后缀名的文件

- .key 格式:私有的密钥
- .csr 格式:证书签名请求(证书请求文件)，含有公钥信息，certificate signing request 的缩写
- .crt 格式:证书文件，certificate 的缩写
- .crl 格式:证书吊销列表，Certificate Revocation List 的缩写
- .pem 格式:用于导出，导入证书时候的证书的格式，有证书开头，结尾的格式

---

## 证书各个字段的含义

查看证书的内容
```bash
openssl x509 -in /etc/pki/CA/cacert.pem -noout -text|egrep -i "issuer|subject|serial|dates"
```

- CN : 公用名称 (Common Name)
- O : 单位名称 (Organization Name)
- L : 所在城市
- S : 所在省份
- C : 所在国家
- OU : 显示其他内容
- E : 电子邮件
- G : 多个姓名字段
- Description : 介绍
- Phone : 电话号码
- STREET : 地址
- PostalCode : 邮政编码

---

## CA 根证书的生成步骤

生成 CA 私钥(.key)-->生成 CA 证书请求(.csr)-->自签名得到根证书(.crt)(CA 给自已颁发的证书).
```flow
st=>start: 生成 CA 私钥(.key)
op=>operation: 生成 CA 证书请求(.csr)
cond=>condition: 自签名得到根证书(.crt)

st->op->cond
```

生成 CA 私钥
```
cd /etc/pki/CA/private
openssl genrsa 2048 > cakey.pem
```

生成自签证书、用 openssl 中 req 这个命令
```
openssl req -new -x509 -key cakey.pem -out /etc/pki/CA/cacert.pem
```

在 CA 的目录下创建两个文件:
```bash
cd /etc/pki/CA
touch index.txt # 索引问文件
touch serial    # 给客户发证编号存放文件
echo 01 > serial
```
```bash
mkdir /etc/httpd/ssl
cd /etc/httpd/ssl
openssl genrsa 1024 > httpd.key
openssl req -new -key httpd.key > httpd.csr
openssl ca -days 365 -in httpd.csr > httpd.crt

# 查看 openssl 证书数据库文件
cat /etc/pki/CA/index.txt
```

---

## keytool 自签

```bash
keytool \
 -keystore server.jks  -storepass test123456  -deststoretype pkcs12 \
 -genkeypair -keyalg RSA -validity 395 -keysize 2048  -sigalg SHA256withRSA \
 -dname "CN=*.test.com"

openssl pkcs12 -in server.jks -nodes -nocerts -out ca.key
openssl pkcs12 -in server.jks -nokeys -out ca.crt

openssl x509 -in ca.crt -noout -text
```

---

## Source & Reference

- https://blog.csdn.net/Michaelwubo/article/details/113736166
- https://cloud.tencent.com/developer/article/1411029
- https://www.cnblogs.com/iiiiher/p/8085698.html
- https://ultimatesecurity.pro/post/san-certificate/
