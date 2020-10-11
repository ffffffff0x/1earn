# Hashcat

<p align="center">
    <img src="../../../assets/img/logo/Hashcat.jpg" width="20%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**简介**

Hashcat 自称是世界上最快的密码恢复工具。它在2015年之前拥有专有代码库，但现在作为免费软件发布。适用于 Linux，OS X 和 Windows 的版本可以使用基于 CPU 或基于 GPU 的变体。支持 hashcat 的散列算法有 Microsoft LM hash，MD4，MD5，SHA 系列，Unix 加密格式，MySQL 和 Cisco PIX 等。

**官网**
- https://hashcat.net/hashcat/

**文章 & Reference**
- [Hashcat的使用手册总结](https://xz.aliyun.com/t/4008)

**工具**
- [nccgroup/hashcrack](https://github.com/nccgroup/hashcrack) - 解包一些散列类型，选择合理的选项并调用 hashcat,hashcat 辅助工具
- [brannondorsey/naive-hashcat](https://github.com/brannondorsey/naive-hashcat) - 包括各种字典，组合，基于规则的攻击和掩码（暴力）攻击。hashcat 傻瓜版?
- [wavestone-cdt/wavecrack](https://github.com/wavestone-cdt/wavecrack) - web 版的 hashcat

**安装**
```bash
mkdir /pentest && cd $_
wget https://hashcat.net/files/hashcat-6.1.1.7z
7z x hashcat-6.1.1.7z && rm -rf hashcat-6.1.1.7z
cd hashcat-6.1.1 && chmod +x hashcat.bin && cp hashcat.bin hashcat
ln -s /pentest/hashcat-6.1.1/hashcat /usr/sbin/hashcat
```

---

# 常见 Hash id 对照表

- https://hashcat.net/wiki/doku.php?id=example_hashes
```bash
hashcat --help

- [ Hash modes ] -

      # | Name                                             | Category
  ======+==================================================+======================================
    900 | MD4                                              | Raw Hash
      0 | MD5                                              | Raw Hash
   5100 | Half MD5                                         | Raw Hash
    100 | SHA1                                             | Raw Hash
   1300 | SHA2-224                                         | Raw Hash
   1400 | SHA2-256                                         | Raw Hash
  10800 | SHA2-384                                         | Raw Hash
   1700 | SHA2-512                                         | Raw Hash
  17300 | SHA3-224                                         | Raw Hash
  17400 | SHA3-256                                         | Raw Hash
  17500 | SHA3-384                                         | Raw Hash
  17600 | SHA3-512                                         | Raw Hash
  17700 | Keccak-224                                       | Raw Hash
  17800 | Keccak-256                                       | Raw Hash
  17900 | Keccak-384                                       | Raw Hash
  18000 | Keccak-512                                       | Raw Hash
    600 | BLAKE2b-512                                      | Raw Hash
  10100 | SipHash                                          | Raw Hash
   6000 | RIPEMD-160                                       | Raw Hash
   6100 | Whirlpool                                        | Raw Hash
   6900 | GOST R 34.11-94                                  | Raw Hash
  11700 | GOST R 34.11-2012 (Streebog) 256-bit, big-endian | Raw Hash
  11800 | GOST R 34.11-2012 (Streebog) 512-bit, big-endian | Raw Hash
     10 | md5($pass.$salt)                                 | Raw Hash, Salted and/or Iterated
     20 | md5($salt.$pass)                                 | Raw Hash, Salted and/or Iterated
     30 | md5(utf16le($pass).$salt)                        | Raw Hash, Salted and/or Iterated
     40 | md5($salt.utf16le($pass))                        | Raw Hash, Salted and/or Iterated
   3800 | md5($salt.$pass.$salt)                           | Raw Hash, Salted and/or Iterated
   3710 | md5($salt.md5($pass))                            | Raw Hash, Salted and/or Iterated
   4010 | md5($salt.md5($salt.$pass))                      | Raw Hash, Salted and/or Iterated
   4110 | md5($salt.md5($pass.$salt))                      | Raw Hash, Salted and/or Iterated
   2600 | md5(md5($pass))                                  | Raw Hash, Salted and/or Iterated
   3910 | md5(md5($pass).md5($salt))                       | Raw Hash, Salted and/or Iterated
   4300 | md5(strtoupper(md5($pass)))                      | Raw Hash, Salted and/or Iterated
   4400 | md5(sha1($pass))                                 | Raw Hash, Salted and/or Iterated
    110 | sha1($pass.$salt)                                | Raw Hash, Salted and/or Iterated
    120 | sha1($salt.$pass)                                | Raw Hash, Salted and/or Iterated
    130 | sha1(utf16le($pass).$salt)                       | Raw Hash, Salted and/or Iterated

以下略
```

---

# 例子

## 查看爆破案例

```bash
hashcat --example-hashes | less
```

---

## 爆破drupal7的密码hash

```bash

echo "\$S\$DvQI6Y600iNeXRIeEMF94Y6FvN8nujJcEDTCP9nS5.i38jnEKuDR" > source.txt
echo "\$S\$DWGrxef6.D0cwB5Ts.GlnLw15chRRWH2s1R3QBwC0EkvBQ/9TCGg" >> source.txt

hashcat -m 7900 -a 0 source.txt pass01.txt

-m 指定要破解的 hash 类型，如果不指定类型，则默认是 MD5
-a 指定要使用的破解模式，其值参考后面对参数。“-a 0”字典攻击，“-a 1” 组合攻击；“-a 3”掩码攻击。
source.txt 你要爆破的 hash 列表
pass01.txt 你的密码表
```

![](../../../assets/img/Security/实验/靶机/VulnHub/DC/DC1/9.png)

---

## 爆破wifi握手包

```bash
hashcat -m 2500 wireless.hccapx pass.txt --force

MODE: 2500
TYPE: WPA/WPA2 PMK
```

---

## 爆破NTLM-hash

```bash
hashcat -m 1000 hash.txt pass1.txt

MODE: 1000
TYPE: NTLM
b4b9b02e6f09a9bd760f388b67351e2b
```

---

## 爆破net-NTLMv2

```bash
hashcat -m 5600 hash.txt pass1.txt

MODE: 5600
TYPE: NetNTLMv2
admin::N46iSNekpT:08ca45b7d7ea58ee:88dcbe4446168966a153a0064958dac6:5c7830315c7830310000000000000b45c67103d07d7b95acd12ffa11230e0000000052920b85f78d013c31cdb3b92f5d765c783030
```

---

## 爆破pdf文件

获取文件 hash
```bash
cd /usr/share/john/
./pdf2john.pl xxx.pdf
```

接下来就是一个一个的试,看是哪种加密算法,比如 word 自带的加密用的就是 10500
```bash
hashcat.exe -m 10400 hash.txt pass1.txt
hashcat.exe -m 10410 hash.txt pass1.txt
hashcat.exe -m 10420 hash.txt pass1.txt
hashcat.exe -m 10500 hash.txt pass1.txt
hashcat.exe -m 10600 hash.txt pass1.txt
hashcat.exe -m 10700 hash.txt pass1.txt

MODE: 10400
TYPE: PDF 1.1 - 1.3 (Acrobat 2 - 4)
$pdf$1*2*40*-1*0*16*51726437280452826511473255744374*32*9b09be05c226214fa1178342673d86f273602b95104f2384b6c9b709b2cbc058*32*0000000000000000000000000000000000000000000000000000000000000000

MODE: 10410
TYPE: PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1
$pdf$1*2*40*-1*0*16*01221086741440841668371056103222*32*27c3fecef6d46a78eb61b8b4dbc690f5f8a2912bbb9afc842c12d79481568b74*32*0000000000000000000000000000000000000000000000000000000000000000

MODE: 10420
TYPE: PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2
$pdf$1*2*40*-1*0*16*01221086741440841668371056103222*32*27c3fecef6d46a78eb61b8b4dbc690f5f8a2912bbb9afc842c12d79481568b74*32*0000000000000000000000000000000000000000000000000000000000000000:6a8aedccb7

MODE: 10500
TYPE: PDF 1.4 - 1.6 (Acrobat 5 - 8)
$pdf$2*3*128*-1028*1*16*da42ee15d4b3e08fe5b9ecea0e02ad0f*32*c9b59d72c7c670c42eeb4fca1d2ca15000000000000000000000000000000000*32*c4ff3e868dc87604626c2b8c259297a14d58c6309c70b00afdfb1fbba10ee571

MODE: 10600
TYPE: PDF 1.7 Level 3 (Acrobat 9)
$pdf$5*5*256*-1028*1*16*20583814402184226866485332754315*127*f95d927a94829db8e2fbfbc9726ebe0a391b22a084ccc2882eb107a74f7884812058381440218422686648533275431500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*127*00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000

MODE: 10700
TYPE: PDF 1.7 Level 8 (Acrobat 10 - 11)
$pdf$5*6*256*-1028*1*16*21240790753544575679622633641532*127*2d1ecff66ea354d3d34325a6503da57e03c199c21b13dd842f8d515826054d8d2124079075354457567962263364153200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*127*00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000*32*0000000000000000000000000000000000000000000000000000000000000000
```

---

## 爆破shadow文件

hash.txt 只保留加密的密码字段 : `$id$salt$encrypted`
```bash
hashcat -m 500 hash.txt pass1.txt
hashcat -m 1500 hash.txt pass1.txt
hashcat -m 1800 hash.txt pass1.txt

MODE: 500
TYPE: md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5) 2
$1$28772684$iEwNOgGugqO9.bIz5sk8k/

MODE: 1500
TYPE: descrypt, DES (Unix), Traditional DES
48c/R8JAv757A

MODE: 1800
TYPE: sha512crypt $6$, SHA512 (Unix)
$6$52450745$k5ka2p8bFuSmoVT1tzOyyuaREkkKBcCNqoDKzYiJL9RaE8yMnPgh2XzzF0NDrUhgrcLwg78xs1w5pJiypEdFX/
```

---

## 爆破压缩包

用 zip2john 获取文件的 hash 值
```bash
zip2john.exe 1.zip > hash.txt
rar2john.exe 1.rar > hash.txt

sudo apt install libcompress-raw-lzma-perl -y
wget https://raw.githubusercontent.com/philsmd/7z2hashcat/master/7z2hashcat.pl
perl 7z2hashcat.pl file.7z > hash.txt
```

```bash
# 7z(住:hashcat 貌似只能跑加密了文件名的 7z 压缩包，未加密文件名的 7z 压缩包需要用 john 跑)
hashcat -m 11600 --force hash.txt pass1.txt

MODE: 11600
TYPE: 7-Zip
$7z$0$19$0$salt$8$f6196259a7326e3f0000000000000000$185065650$112$98$f3bc2a88062c419a25acd40c0c2d75421cf23263f69c51b13f9b1aada41a8a09f9adeae45d67c60b56aad338f20c0dcc5eb811c7a61128ee0746f922cdb9c59096869f341c7a9cb1ac7bb7d771f546b82cf4e6f11a5ecd4b61751e4d8de66dd6e2dfb5b7d1022d2211e2d66ea1703f96
# 如果在 windows 下的话,记得修改编码为 ANSI

# rar
hashcat -m 12500 --force hash.txt pass1.txt
hashcat -m 13000 --force hash.txt pass1.txt

MODE: 12500
TYPE: RAR3-hp
$RAR3$*0*45109af8ab5f297a*adbf6c5385d7a40373e8f77d7b89d317

MODE: 13000
TYPE: RAR5
$rar5$16$74575567518807622265582327032280$15$f8b4064de34ac02ecabfe9abdf93ed6a$8$9843834ed0f7c754

# zip
hashcat -m 13600 --force hash.txt pass1.txt
hashcat -m 17200 --force hash.txt pass1.txt
hashcat -m 17210 --force hash.txt pass1.txt
hashcat -m 17220 --force hash.txt pass1.txt
hashcat -m 17225 --force hash.txt pass1.txt
hashcat -m 17230 --force hash.txt pass1.txt
hashcat -m 23001 --force hash.txt pass1.txt
hashcat -m 23002 --force hash.txt pass1.txt
hashcat -m 23003 --force hash.txt pass1.txt

MODE: 13600
TYPE: WinZip
$zip2$*0*3*0*e3222d3b65b5a2785b192d31e39ff9de*1320*e*19648c3e063c82a9ad3ef08ed833*3135c79ecb86cd6f48fc*$/zip2$

MODE: 17200
TYPE: PKZIP (Compressed)
$pkzip2$1*1*2*0*e3*1c5*eda7a8de*0*28*8*e3*eda7*5096*a9fc1f4e951c8fb3031a6f903e5f4e3211c8fdc4671547bf77f6f682afbfcc7475d83898985621a7af9bccd1349d1976500a68c48f630b7f22d7a0955524d768e34868880461335417ddd149c65a917c0eb0a4bf7224e24a1e04cf4ace5eef52205f4452e66ded937db9545f843a68b1e84a2e933cc05fb36d3db90e6c5faf1bee2249fdd06a7307849902a8bb24ec7e8a0886a4544ca47979a9dfeefe034bdfc5bd593904cfe9a5309dd199d337d3183f307c2cb39622549a5b9b8b485b7949a4803f63f67ca427a0640ad3793a519b2476c52198488e3e2e04cac202d624fb7d13c2*$/pkzip2$

MODE: 17210
TYPE: PKZIP (Uncompressed)
$pkzip2$1*1*2*0*1d1*1c5*eda7a8de*0*28*0*1d1*eda7*5096*1dea673da43d9fc7e2be1a1f4f664269fceb6cb88723a97408ae1fe07f774d31d1442ea8485081e63f919851ca0b7588d5e3442317fff19fe547a4ef97492ed75417c427eea3c4e146e16c100a2f8b6abd7e5988dc967e5a0e51f641401605d673630ea52ebb04da4b388489901656532c9aa474ca090dbac7cf8a21428d57b42a71da5f3d83fed927361e5d385ca8e480a6d42dea5b4bf497d3a24e79fc7be37c8d1721238cbe9e1ea3ae1eb91fc02aabdf33070d718d5105b70b3d7f3d2c28b3edd822e89a5abc0c8fee117c7fbfbfd4b4c8e130977b75cb0b1da080bfe1c0859e6483c42f459c8069d45a76220e046e6c2a2417392fd87e4aa4a2559eaab3baf78a77a1b94d8c8af16a977b4bb45e3da211838ad044f209428dba82666bf3d54d4eed82c64a9b3444a44746b9e398d0516a2596d84243b4a1d7e87d9843f38e45b6be67fd980107f3ad7b8453d87300e6c51ac9f5e3f6c3b702654440c543b1d808b62f7a313a83b31a6faaeedc2620de7057cd0df80f70346fe2d4dccc318f0b5ed128bcf0643e63d754bb05f53afb2b0fa90b34b538b2ad3648209dff587df4fa18698e4fa6d858ad44aa55d2bba3b08dfdedd3e28b8b7caf394d5d9d95e452c2ab1c836b9d74538c2f0d24b9b577*$/pkzip2$

MODE: 17220
TYPE: PKZIP (Compressed Multi-File)
$pkzip2$3*1*1*0*8*24*a425*8827*d1730095cd829e245df04ebba6c52c0573d49d3bbeab6cb385b7fa8a28dcccd3098bfdd7*1*0*8*24*2a74*882a*51281ac874a60baedc375ca645888d29780e20d4076edd1e7154a99bde982152a736311f*2*0*e3*1c5*eda7a8de*0*29*8*e3*eda7*5096*1455781b59707f5151139e018bdcfeebfc89bc37e372883a7ec0670a5eafc622feb338f9b021b6601a674094898a91beac70e41e675f77702834ca6156111a1bf7361bc9f3715d77dfcdd626634c68354c6f2e5e0a7b1e1ce84a44e632d0f6e36019feeab92fb7eac9dda8df436e287aafece95d042059a1b27d533c5eab62c1c559af220dc432f2eb1a38a70f29e8f3cb5a207704274d1e305d7402180fd47e026522792f5113c52a116d5bb25b67074ffd6f4926b221555234aabddc69775335d592d5c7d22462b75de1259e8342a9ba71cb06223d13c7f51f13be2ad76352c3b8ed*$/pkzip2$

MODE: 17225
TYPE: PKZIP (Mixed Multi-File)
$pkzip2$3*1*1*0*0*24*3e2c*3ef8*0619e9d17ff3f994065b99b1fa8aef41c056edf9fa4540919c109742dcb32f797fc90ce0*1*0*8*24*431a*3f26*18e2461c0dbad89bd9cc763067a020c89b5e16195b1ac5fa7fb13bd246d000b6833a2988*2*0*23*17*1e3c1a16*2e4*2f*0*23*1e3c*3f2d*54ea4dbc711026561485bbd191bf300ae24fa0997f3779b688cdad323985f8d3bb8b0c*$/pkzip2$

MODE: 17230
TYPE: PKZIP (Compressed Multi-File Checksum-Only)
$pkzip2$8*1*1*0*8*24*a425*8827*3bd479d541019c2f32395046b8fbca7e1dca218b9b5414975be49942c3536298e9cc939e*1*0*8*24*2a74*882a*537af57c30fd9fd4b3eefa9ce55b6bff3bbfada237a7c1dace8ebf3bb0de107426211da3*1*0*8*24*2a74*882a*5f406b4858d3489fd4a6a6788798ac9b924b5d0ca8b8e5a6371739c9edcfd28c82f75316*1*0*8*24*2a74*882a*1843aca546b2ea68bd844d1e99d4f74d86417248eb48dd5e956270e42a331c18ea13f5ed*1*0*8*24*2a74*882a*aca3d16543bbfb2e5d2659f63802e0fa5b33e0a1f8ae47334019b4f0b6045d3d8eda3af1*1*0*8*24*2a74*882a*fbe0efc9e10ae1fc9b169bd060470bf3e39f09f8d83bebecd5216de02b81e35fe7e7b2f2*1*0*8*24*2a74*882a*537886dbabffbb7cac77deb01dc84760894524e6966183b4478a4ef56f0c657375a235a1*1*0*8*24*eda7*5096*40eb30ef1ddd9b77b894ed46abf199b480f1e5614fde510855f92ae7b8026a11f80e4d5f*$/pkzip2$

MODE: 23001
TYPE: SecureZIP AES-128
$zip3$*0*1*128*0*b4630625c92b6e7848f6fd86*df2f62611b3d02d2c7e05a48dad57c7d93b0bac1362261ab533807afb69db856676aa6e350320130b5cbf27c55a48c0f75739654ac312f1cf5c37149557fc88a92c7e3dde8d23edd2b839036e88092a708b7e818bf1b6de92f0efb5cce184cceb11db6b3ca0527d0bdf1f1137ee6660d9890928cd80542ac1f439515519147c14d965b5ba107c6227f971e3e115170bf*0*0*0*file.txt

MODE: 23002
TYPE: SecureZIP AES-192
$zip3$*0*1*192*0*53ff2de8c280778e1e0ab997*603eb37dbab9ea109e2c405e37d8cae1ec89e1e0d0b9ce5bf55d1b571c343b6a3df35fe381c30249cb0738a9b956ba8e52dfc5552894296300446a771032776c811ff8a71d9bb3c4d6c37016c027e41fea2d157d5b0ce17804b1d7c1606b7c1121d37851bd705e001f2cd755bbf305966d129a17c1d48ff8e87cfa41f479090cd456527db7d1d43f9020ad8e73f851a5*0*0*0*file.txt

MODE: 23003
TYPE: SecureZIP AES-256
$zip3$*0*1*256*0*39bff47df6152a0214d7a967*65ff418ffb3b1198cccdef0327c03750f328d6dd5287e00e4c467f33b92a6ef40a74bb11b5afad61a6c3c9b279d8bd7961e96af7b470c36fc186fd3cfe059107021c9dea0cf206692f727eeca71f18f5b0b6ee1f702b648bba01aa21c7b7f3f0f7d547838aad46868155a04214f22feef7b31d7a15e1abe6dba5e569c62ee640783bb4a54054c2c69e93ece9f1a2af9d*0*0*0*file.txt
```

---

## 爆破office

```bash
python /usr/share/john/office2john.py xxx.docx
```

```bash
hashcat -m 9600 hash.txt pass1.txt

MODE: 9400
TYPE: MS Office 2010
$office$*2007*20*128*16*411a51284e0d0200b131a8949aaaa5cc*117d532441c63968bee7647d9b7df7d6*df1d601ccf905b375575108f42ef838fb88e1cde

MODE: 9500
TYPE: MS Office 2010
$office$*2010*100000*128*16*77233201017277788267221014757262*b2d0ca4854ba19cf95a2647d5eee906c*e30cbbb189575cafb6f142a90c2622fa9e78d293c5b0c001517b3f5b82993557

MODE: 9600
TYPE: MS Office 2013
$office$*2013*100000*256*16*7dd611d7eb4c899f74816d1dec817b3b*948dc0b2c2c6c32f14b5995a543ad037*0b7ee0e48e935f937192a59de48a7d561ef2691d5c8a3ba87ec2d04402a94895
```
