# ZIP明文攻击

---

**相关工具**
- archpr(Advanced Archive Password Recovery)
- [keyunluo/pkcrack](https://github.com/keyunluo/pkcrack)
- [kimci86/bkcrack](https://github.com/kimci86/bkcrack)
    ```bash
    wget https://github.com/kimci86/bkcrack/releases/download/v1.3.1/bkcrack-1.3.1-Linux.tar.gz
    tar -zxvf bkcrack-1.3.1-Linux.tar.gz
    cp bkcrack-1.3.1-Linux/bkcrack /usr/sbin/bkcrack
    bkcrack -h
    ```

---

## ZIP 的加密算法

ZIP 的加密算法大致分为两种 ZipCrypto 和 AES-256, 各自又分 Deflate 和 Store。

- ZipCrypto Deflate
- ZipCrypto Store
- AES-256 Deflate
- AES-256 Store

ZipCrypto 算是传统的 zip 加密方式。

只有使用 ZipCrypto Deflate /Store 才可以使用 ZIP 已知明文攻击进行破解。

AES256-Deflate/AES256-Store 加密的文件不适用于明文攻击。

---

## ZIP 明文攻击的条件

至少已知明文的 12 个字节及偏移，其中至少 8 字节需要连续。

明文对应的文件加密方式为 ZipCrypto Store

---

## 比较特殊的明文攻击案例

在知道目标文件部分连续明文的情况下，去爆破密钥

例如 flag.txt
```
flag{4d6ba874-881d-4c04-b7c3-5e974b81e86a
```

加密成 flag.zip 加密时注意使用 Deflate 压缩方法,ZipCrypto 加密算法

给出部分连续明文
```
flag{4d6ba874-881d-4c0
```

采用 bkcrack 进行爆破
```bash
echo "flag{4d6ba874-881d-4c0" > plain1.txt
bkcrack -C flag.zip -c flag.txt -p plain1.txt

# 爆破得到zip的密钥如下
1b10db88 4b87405b 0a41939c
```

利用密钥进行解密
```
bkcrack -C flag.zip -c flag.txt -k 1b10db88 4b87405b 0a41939c -d flag1.txt

cat flag1.txt
```

如果是已知部分且不连续可以采用 -o 偏移量参数组合使用
```bash
bkcrack -C flag.zip -c flag.txt -p plain1.txt -o 1 -x 29 37346636

# -c 提取的密文部分
# -p 提取的明文部分
# -x 压缩包内目标文件的偏移地址  部分已知明文值
# -C 加密压缩包
# -o offset  -p参数指定的明文在压缩包内目标文件的偏移量
```

---

## Source & Reference
- [ZIP明文攻击获得加密压缩包内文件](https://jingyan.baidu.com/article/0f5fb0990bba086d8334eaf6.html)
- [zip加密的明文攻击](https://blog.csdn.net/hustcw98/article/details/82392993)
- [ZIP已知明文攻击深入利用](https://www.freebuf.com/articles/network/255145.html)
