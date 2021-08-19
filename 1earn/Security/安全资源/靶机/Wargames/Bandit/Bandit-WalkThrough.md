# Bandit-WalkThrough

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

https://overthewire.org/wargames/bandit/

## Level 0 访问

ssh 连接

主机：bandit.labs.overthewire.org

端口：2220

bandit0/bandit0

不知道为啥 xshell 直接连不上去,用 linux ssh 连接上去了
```bash
ssh -p 2220 bandit0@bandit.labs.overthewire.org
```

---

## Level 0 → Level 1

连接上后,查看readme
```bash
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

---

## Level 1 → Level 2

通过上一关读出的密码连接 2220 端口的 bandit1 用户

```
ssh -p 2220 bandit1@bandit.labs.overthewire.org
```

查看当前目录
```bash
bandit1@bandit:~$ ls -la
total 24
-rw-r-----  1 bandit2 bandit1   33 May  7  2020 -
drwxr-xr-x  2 root    root    4096 May  7  2020 .
drwxr-xr-x 41 root    root    4096 May  7  2020 ..
-rw-r--r--  1 root    root     220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root    3526 May 15  2017 .bashrc
-rw-r--r--  1 root    root     675 May 15  2017 .profile
```

查看 这个 `-` 文件,直接看不行,要加个路径

```bash
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

---

## Level 2 → Level 3

通过上一关读出的密码连接 2220 端口的 bandit2 用户

```
ssh -p 2220 bandit2@bandit.labs.overthewire.org
```

查看当前目录
```bash
bandit2@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root    root    4096 May  7  2020 .
drwxr-xr-x 41 root    root    4096 May  7  2020 ..
-rw-r--r--  1 root    root     220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root    3526 May 15  2017 .bashrc
-rw-r--r--  1 root    root     675 May 15  2017 .profile
-rw-r-----  1 bandit3 bandit2   33 May  7  2020 spaces in this filename
```

这个文件名带空格,其实也好解决引号括起来就行了
```bash
bandit2@bandit:~$ cat 'spaces in this filename'
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

---

## Level 3 → Level 4

通过上一关读出的密码连接 2220 端口的 bandit3 用户

```bash
ssh -p 2220 bandit3@bandit.labs.overthewire.org
```

查看当前目录
```bash
bandit3@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root 4096 May  7  2020 .
drwxr-xr-x 41 root root 4096 May  7  2020 ..
-rw-r--r--  1 root root  220 May 15  2017 .bash_logout
-rw-r--r--  1 root root 3526 May 15  2017 .bashrc
drwxr-xr-x  2 root root 4096 May  7  2020 inhere
-rw-r--r--  1 root root  675 May 15  2017 .profile

# 发现一个目录,进入查看
bandit3@bandit:~$ cd inhere/

# 用 -la 查看隐藏文件
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 May  7  2020 .
drwxr-xr-x 3 root    root    4096 May  7  2020 ..
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden
```

带 . 号的文件,默认直接 ls 是看不到的

```bash
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

---

## Level 4 → Level 5

通过上一关读出的密码连接 2220 端口的 bandit4 用户

```bash
ssh -p 2220 bandit4@bandit.labs.overthewire.org
```

查看当前目录
```bash
bandit4@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root 4096 May  7  2020 .
drwxr-xr-x 41 root root 4096 May  7  2020 ..
-rw-r--r--  1 root root  220 May 15  2017 .bash_logout
-rw-r--r--  1 root root 3526 May 15  2017 .bashrc
drwxr-xr-x  2 root root 4096 May  7  2020 inhere
-rw-r--r--  1 root root  675 May 15  2017 .profile

bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls -la
total 48
drwxr-xr-x 2 root    root    4096 May  7  2020 .
drwxr-xr-x 3 root    root    4096 May  7  2020 ..
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file00
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file01
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file02
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file03
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file04
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file05
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file06
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file07
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file08
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file09
```

题目说是可读类型,用 file 命令查看文件类型

```bash
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat file07
cat: file07: No such file or directory
bandit4@bandit:~/inhere$ cat ./file07
cat: ./file07: No such file or directory
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

---

## Level 5 → Level 6

通过上一关读出的密码连接 2220 端口的 bandit5 用户

```bash
ssh -p 2220 bandit5@bandit.labs.overthewire.org
```

查看当前目录
```bash
bandit5@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root    4096 May  7  2020 .
drwxr-xr-x 41 root root    4096 May  7  2020 ..
-rw-r--r--  1 root root     220 May 15  2017 .bash_logout
-rw-r--r--  1 root root    3526 May 15  2017 .bashrc
drwxr-x--- 22 root bandit5 4096 May  7  2020 inhere
-rw-r--r--  1 root root     675 May 15  2017 .profile
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls -la
total 88
drwxr-x--- 22 root bandit5 4096 May  7  2020 .
drwxr-xr-x  3 root root    4096 May  7  2020 ..
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere00
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere01
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere02
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere03
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere04
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere05
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere06
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere07
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere08
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere09
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere10
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere11
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere12
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere13
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere14
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere15
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere16
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere17
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere18
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere19
```

题目说文件大小是 1033 bytes in size

直接用 find 查找即可
```bash
bandit5@bandit:~/inhere$ find ./ -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

---

## Level 6 → Level 7

通过上一关读出的密码连接 2220 端口的 bandit6 用户

```bash
ssh -p 2220 bandit6@bandit.labs.overthewire.org
```

题目里说文件的格式如下
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

一样用find找,不过这里注意将错误输出给 /dev/null
```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

---

## Level 7 → Level 8

通过上一关读出的密码连接 2220 端口的 bandit7 用户

```bash
ssh -p 2220 bandit7@bandit.labs.overthewire.org
```

The password for the next level is stored in the file data.txt next to the word millionth

找 data.txt 并匹配 millionth
```bash
bandit7@bandit:~$ ls -la
total 4108
drwxr-xr-x  2 root    root       4096 May  7  2020 .
drwxr-xr-x 41 root    root       4096 May  7  2020 ..
-rw-r--r--  1 root    root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root       3526 May 15  2017 .bashrc
-rw-r-----  1 bandit8 bandit7 4184396 May  7  2020 data.txt
-rw-r--r--  1 root    root        675 May 15  2017 .profile
bandit7@bandit:~$ cat data.txt |grep millionth
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

---

## Level 8 → Level 9

通过上一关读出的密码连接 2220 端口的 bandit8 用户

```bash
ssh -p 2220 bandit8@bandit.labs.overthewire.org
```

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

这里要找文本中只出现一次的行

可以用 uniq 实现
```bash
bandit8@bandit:~$ ls -la
total 56
drwxr-xr-x  2 root    root     4096 May  7  2020 .
drwxr-xr-x 41 root    root     4096 May  7  2020 ..
-rw-r--r--  1 root    root      220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root     3526 May 15  2017 .bashrc
-rw-r-----  1 bandit9 bandit8 33033 May  7  2020 data.txt
-rw-r--r--  1 root    root      675 May 15  2017 .profile

bandit8@bandit:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

---

## Level 9 → Level 10

通过上一关读出的密码连接 2220 端口的 bandit9 用户

```bash
ssh -p 2220 bandit9@bandit.labs.overthewire.org
```

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

打开是一堆乱码,尝试用 string 读字符串

```
bandit9@bandit:~$ ls -la
total 40
drwxr-xr-x  2 root     root     4096 May  7  2020 .
drwxr-xr-x 41 root     root     4096 May  7  2020 ..
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc
-rw-r-----  1 bandit10 bandit9 19379 May  7  2020 data.txt
-rw-r--r--  1 root     root      675 May 15  2017 .profile

bandit9@bandit:~$ strings data.txt
Z/,_
WW"&8
2Qk)
xWa_
x?Xn
//M$
;yzEt!
WpU~e
`Rn,I
VSXdK
WB|{
GhG$
========== the*2i"4
DUJmU
ux.j
=:G e
8.jD
)'0K
9DLW
f0"q
zf~Z
 flf
a{KG
lj}ZRO
662Z
.Y `04
wUhy
X38UL
v"*-
AxEf
aeTh
OeOS
e}\"
[72V]>e
N+{G6Q
7XK5
B}T<d
SQr.
{8xG\
|b;{
Y4xsm
-xnfv
6@Bj
-|38
,F3&A
iQ>Zc
 r8C
|wJ*"
gtg~o6c
&>\     7
xk9~
.,N?
n~C!l
LCbD
wqND
tmC>
'<o-
OxYF
68}j
Q~a`%
========== password
#|-l
G}`:
o]zb
JbnhB
:j9)
t7qM
9-q?9z
gh'Kz
uWO)
dxG9
e})nQ
~}K{
acer
?.}@
"*a%si*
<I=zsGi
&15h
!G[\
uOZ\K
BYD1
D2?
Z)========== is
x[U*
m/;7
r%z$c
C !n
&/Lhh[}~s
b$J})Q
z3p)
fRk4Ck
Jq{`
fVHi
Y<_M
88)%
E>aS
*S{"
k<02
i;C\\N
t;afX
:mJ\
){.h
ZcO3
>K`t;X
'p6:
/g'x
l6C4
@17J
V?**
141>Y
YZ+y
K#VV
|6Uj
ckd^r
zDshn:X
A=|t&E
n8os
O\0     f       >
]v#8
2X[eO{
TjIR\+
qeY|
I[aJtZH:
LkfWdO5`
pC:*
X^+5
Aiwj~
        0^8]W
4k1S
BbYR
:hk9
ZpE5
mWW#+\
s/#m`
*Ybc
vNHkt
tVQq
S_JtG1
CQ:[`
63KS+
Rw_0
)'p5
y.f+3
G?'P
olV_
0X Gx
6\Ni
X$)4!
B-"q
p1bz
P%W"
W`yI
ve&I
Zdb=
M]W>g
9!ipo
x3tl%E
{)Xiw-
Mef?Mo
Tr]Zo
;x47
/Uil>
c^ LAh=3G
QR%q
C&&b
fXzzO(Ub
.y#2
LsyH
R       w&
,V*.m
g.o]]|W
]A2xd}M
il,m
.;].F
}<@M
N:)c
sssyJ
:T      Y
_^XF)ZB.g
;9'~
\Jg`
S/gA
g<%x
xzY<
blsN
~U^y
x@nQ
*SF=s
}1:LF
]vur
Emlld
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
_Gmz
\Uli,
A5RK
S'$0
<4t",
4cXO
cj13c:?
&Yra
zEwa
b2+x
z`tlR
o|8M]
.p4Hv
)z<p
S=A.H&^
#hu#
"C}Jy
0R@R_
~KW?
b#Nzx$b
RlG#t]Z}
e790
JzV1O
XEgp
2Q d
z#j\
1Qit
a'b~
bxBB\u$
8Zpc    $FOxF[
ANYwPCpk
Xk]E
bh}s
P'uP
\-A:
sCtY
Z/1x+
ej8z
P"`\XZ
1KOA
```

---

## Level 10 → Level 11

通过上一关读出的密码连接 2220 端口的 bandit10 用户

```bash
ssh -p 2220 bandit10@bandit.labs.overthewire.org
```

The password for the next level is stored in the file data.txt, which contains base64 encoded data

找 base64 数据,解法和上面一样,直接 strings

```bash
bandit10@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 May  7  2020 .
drwxr-xr-x 41 root     root     4096 May  7  2020 ..
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc
-rw-r-----  1 bandit11 bandit10   69 May  7  2020 data.txt
-rw-r--r--  1 root     root      675 May 15  2017 .profile
bandit10@bandit:~$ strings data.txt
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
```

```bash
bandit10@bandit:~$ echo "VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==" | base64 -d -w 0
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

---

## Level 11 → Level 12

通过上一关读出的密码连接 2220 端口的 bandit11 用户

```bash
ssh -p 2220 bandit11@bandit.labs.overthewire.org
```

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

rot13 没啥难度

```
bandit11@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 May  7  2020 .
drwxr-xr-x 41 root     root     4096 May  7  2020 ..
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc
-rw-r-----  1 bandit12 bandit11   49 May  7  2020 data.txt
-rw-r--r--  1 root     root      675 May 15  2017 .profile
bandit11@bandit:~$ strings data.txt
Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
```

使用 tr 可以直接转换

```
bandit11@bandit:~$ cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

---

## Level 12 → Level 13

通过上一关读出的密码连接 2220 端口的 bandit12 用户

```bash
ssh -p 2220 bandit12@bandit.labs.overthewire.org
```

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

先在tmp创建一个目录然后把根目录下的文件复制过去
```bash
bandit12@bandit:~$ mkdir /tmp/f0x
bandit12@bandit:~$ cp data.txt /tmp/f0x
bandit12@bandit:~$ cd /tmp/f0x
bandit12@bandit:/tmp/f0x$ ls -la
total 1996
drwxr-sr-x 2 bandit12 root    4096 Aug 11 10:42 .
drwxrws-wt 1 root     root 2031616 Aug 11 10:42 ..
-rw-r----- 1 bandit12 root    2582 Aug 11 10:42 data.txt
```

用 xxd 命令处理十六进制转储文件
```bash
xxd -r data.txt > data.bin
```

然后就是不停的改后缀,解压
```bash
file data.bin
mv data.bin data.gz
gzip -d data.gz
ls -la

file data

mv data data.bz2
bzip2 -dv data.bz2
ls -la

file data
mv data data.gz
gzip -d data.gz
ls -la

file data
mv data data.tar
tar -xvf data.tar
ls -la

file data5.bin
mv data5.bin data5.tar
tar -xvf data5.tar
ls -la

file data6.bin
mv data6.bin data6.bz2
bzip2 -dv data6.bz2
ls -la

file data6
mv data6 data6.tar
tar -xvf data6.tar
ls -la

file data8.bin
mv data8.bin data8.gz
gzip -d data8.gz
ls -la

file data8

bandit12@bandit:/tmp/f0x$ cat data8
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

---

## Level 13 → Level 14

通过上一关读出的密码连接 2220 端口的 bandit13 用户

```bash
ssh -p 2220 bandit13@bandit.labs.overthewire.org
```

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

这里提供私钥,尝试直接使用私钥登录
```
ssh -i sshkey.private bandit14@localhost

bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

---

## Level 14 → Level 15

通过上一关读出的密码连接 2220 端口的 bandit14 用户

```bash
ssh -p 2220 bandit14@bandit.labs.overthewire.org
```

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

```
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

---

## Level 15 → Level 16

通过上一关读出的密码连接 2220 端口的 bandit15 用户

```bash
ssh -p 2220 bandit15@bandit.labs.overthewire.org
```

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

这里我们可以通过 openssl 自带的连接工具去连接 30001

```
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEHxhZ+zANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjEwODA1MjEyMjEzWhcNMjIwODA1MjEyMjEzWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALqNmx6R
csRsPgzRcRsq5oQ4BC9AT/Yu473WbK4SRjHOWwuA4Oqk9w8SLKYZ39FrDEnXSZJw
xqKPR0AH72+l7Itv7X1H07VbeMTQoJVm6NsJm3cuyyxjRwfaIOUFsRtQQyvQlmw7
3CgTbd3wEk1CD+6jlksJj801Vd0uvZh1VVERAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBADjhbe3bTnDWsS4xt8FFg7PJIqNAxF6QjP+7xzJ4yMvWtPP6tVXo
F7SNI52juwH0nFDyM9KOrM/AknWqCYF+yfz6bLD7MaKZ+Kg3DiLaoVJOrVg6Y02+
0vq1rLsqGko5wamCFamx7X9CtFsV0WQjZdA53Na/VwehtlFpf/p20VAi
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: E61E96BBB8E9703082F8D68DDF5EA59E3C78B826F1E4FE78D68E2225D84A21E9
    Session-ID-ctx:
    Master-Key: 743D322D7FE0B6AD921D2902197725CCB8A16447BDF671802DE29DC16D6911839D3BF4814D687410D83264FE59A0F3C7
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 3a a9 fe 3b 12 a1 ed 2b-8d a6 cf aa 23 c9 12 88   :..;...+....#...
    0010 - 62 41 a0 b0 74 0b 0e a1-4d 81 06 29 0e cb d2 85   bA..t...M..)....
    0020 - b3 fc 0e 24 70 5a 56 c0-51 f6 2a 4c c4 60 f4 55   ...$pZV.Q.*L.`.U
    0030 - ef fc da a4 2f 13 05 37-30 16 4c 8d 02 53 99 9f   ..../..70.L..S..
    0040 - f0 33 57 73 5a 1f 3f 5e-3c ad 99 ba 67 a4 d9 94   .3WsZ.?^<...g...
    0050 - bb b2 76 3f 35 06 04 0a-a6 9f 29 5e 39 b0 cf e9   ..v?5.....)^9...
    0060 - 40 d9 bb bc b8 7b cc 89-ae ee b7 35 98 f1 b4 f4   @....{.....5....
    0070 - 90 d6 04 00 02 4b b2 7f-18 b1 43 d8 a6 e9 c1 f8   .....K....C.....
    0080 - dd e3 72 7e eb 7a 92 c5-4b a8 1b 9b b2 a0 9b 7c   ..r~.z..K......|
    0090 - ff a5 df e6 a6 9e b6 44-2e f4 51 13 32 30 7b fd   .......D..Q.20{.

    Start Time: 1628674034
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```

---

## Level 16 → Level 17

通过上一关读出的密码连接 2220 端口的 bandit16 用户

```bash
ssh -p 2220 bandit16@bandit.labs.overthewire.org
```

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

扫描本地端口
```
bandit16@bandit:~$ nmap localhost -p 31000-32000

Starting Nmap 7.40 ( https://nmap.org ) at 2021-08-11 11:28 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00023s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
```

一个一个试
```
bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEatsK7TANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjEwODA1MjEyMzAxWhcNMjIwODA1MjEyMzAxWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALbshxNY
mdJ/7RpASCHk+XULoBymcRoKY9tPU25zhhPmrFAyv0HNXG/GqPjOxI4MHG627HOf
b00a/ikeDUTVdCiDXhungyUx6W07H3uiHHbfNLs1QGl2GPdBVA+z5DZcNsWJ1QB5
888HEzp8YNWyeHnP+5gy5LqlX5hUkF1eu6C1AgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBABVCD/dhWpgN9KC5Eb6hd9ToreRhof44OQaHalJtsayPBBMTK3Lp
KC88rNVJW+cX0z+eUe6en0RIvU56dLNT+zm9cbDvCV1cumz4++nauWes/11eA5aG
2NNgKQHYvT+bOfo3lhOQNwtzpO4MX1sGMjO4dlS4AmxTdjz0UVUPLamk
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 8B08245CF0D19480F27B32F33CE12DA7897B47FC11CD1B7CF50D3E2CFE8BEACD
    Session-ID-ctx:
    Master-Key: 45C6DBE36EE36759C82C8EBEEE1F5ED8E91ED47F75300F8FB2EEE52F08AA83369EC4005C8D309EDE6EFC93D3FD873229
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 30 d5 a9 3d 7d a2 f1 16-f5 b3 32 79 c1 92 42 1a   0..=}.....2y..B.
    0010 - b9 38 3f 88 bd d7 8c 60-53 2a 9a 29 a6 21 9a cd   .8?....`S*.).!..
    0020 - a5 06 77 d5 54 e8 9b d3-6d c1 b3 5a 4a e1 13 f9   ..w.T...m..ZJ...
    0030 - e0 77 a9 85 8b 11 0b 50-86 bd e0 10 4d 3a 32 2b   .w.....P....M:2+
    0040 - 98 ac f0 19 1d 98 30 2f-0c e2 54 19 5e 10 f3 ab   ......0/..T.^...
    0050 - f7 9d ae 3e 34 fd 64 7a-41 3d 99 e7 1a 9e 2c 15   ...>4.dzA=....,.
    0060 - 0f 45 57 c4 fc 0a 48 86-df a6 44 76 41 39 84 cc   .EW...H...DvA9..
    0070 - 1a cf f3 d4 d1 ae a9 67-fa b4 b0 7a a3 19 6f a3   .......g...z..o.
    0080 - 6a 49 69 cc 33 ff 00 a2-8e 51 b2 06 18 a7 5e 2b   jIi.3....Q....^+
    0090 - a3 9e 73 c1 ff 51 de 61-44 50 4c 3c 82 3a 2b 1a   ..s..Q.aDPL<.:+.

    Start Time: 1628674192
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
```

返回给我一个私钥文件,尝试另存

当前路径下没有权限,/tmp下也没权限

不如自己创建一个目录
```bash
rm -rf /tmp/f1x
mkdir /tmp/f1x
cd /tmp/f1x
```

```
tee /tmp/f1x/key <<-'EOF'
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
EOF
```

```
chmod 700 /tmp/f1x/key
ssh -i /tmp/f1x/key bandit17@localhost
```

---

## Level 17 → Level 18

这里在上一关的基础上继续做题

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

这里需要比较2个文件的不同行

```
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

---

## Level 18 → Level 19

通过上一关读出的密码连接 2220 端口的 bandit18 用户

```bash
ssh -p 2220 bandit18@bandit.labs.overthewire.org
```

The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

一旦连接之后会自动断开

这里要在登录的时候执行命令
```
Connection to bandit.labs.overthewire.org closed.
root@localhost:~# ssh -p 2220 bandit18@bandit.labs.overthewire.org cat readme
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

---

## Level 19 → Level 20

通过上一关读出的密码连接 2220 端口的 bandit19 用户

```bash
ssh -p 2220 bandit19@bandit.labs.overthewire.org
```

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

```
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```
