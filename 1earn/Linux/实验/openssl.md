# 概念
[TOC]
## 什么是x509证书链
x509 证书一般会用到三类文件，key，csr，crt。
Key是私用密钥，openssl格式，通常是rsa算法。
csr是证书请求文件，用于申请证书。在制作csr文件的时候，必须使用自己的私钥来签署申请，还可以设定一个密钥。
crt是CA认证后的证书文件（windows下面的csr，其实是crt），签署人用自己的key给你签署的凭证。


## openssl中有如下后缀名的文件
- .key格式：私有的密钥
- .csr格式：证书签名请求（证书请求文件），含有公钥信息，certificate signing request的缩写
- .crt格式：证书文件，certificate的缩写
- .crl格式：证书吊销列表，Certificate Revocation List的缩写
- .pem格式：用于导出，导入证书时候的证书的格式，有证书开头，结尾的格式


## CA根证书的生成步骤
生成CA私钥（.key）-->生成CA证书请求（.csr）-->自签名得到根证书（.crt）（CA给自已颁发的证书）。
```flow
st=>start: 生成CA私钥（.key）
op=>operation: 生成CA证书请求（.csr）
cond=>condition: 自签名得到根证书（.crt）

st->op->cond
```


生成CA私钥
>cd /etc/pki/CA/private
>openssl genrsa 2048 > cakey.pem 

生成自签证书、用openssl中req这个命令、叫证书请求
>openssl req -new -x509 -key cakey.pem -out /etc/pki/CA/cacert.pem

在CA的目录下创建两个文件：
cd /etc/pki/CA
touch index.txt  #索引问文件
touch serial    #给客户发证编号存放文件
echo 01 > serial

mkdir /etc/httpd/ssl
cd /etc/httpd/ssl
openssl genrsa 1024 > httpd.key 
openssl req -new -key httpd.key > httpd.csr
openssl ca -days 365 -in httpd.csr > httpd.crt 

使用cat /etc/pki/CA/index.txt查看openssl证书数据库文件
cat /etc/pki/CA/index.txt

