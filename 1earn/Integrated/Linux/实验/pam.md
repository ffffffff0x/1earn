# PAM

---

## 关于PAM

PAM 基础知识见 [认证](../笔记/认证.md#pam)

**安装 PAM**

CentOS、Fedora、EulerOS 系统默认安装了 PAM 并默认启动。
```bash
apt-get install libpam-cracklib
```

**判断程序是否使用了 PAM**

```
ldd /usr/bin/passwd | grep libpam
```

**PAM 身份验证配置文件**

`/etc/pam.d/` 目录包含应用程序的 PAM 配置文件。例如，login 程序将其程序/服务名称定义为 login，与之对应的 PAM 配置文件为 `/etc/pam.d/login`。

**PAM 配置文件语法格式**

每个PAM配置文件都包含一组指令，用于定义模块以及控制标志和参数。每条指令都有一个简单的语法，用于标识模块的目的（接口）和模块的配置设置，语法格式如下：
```
module_interface      control_flag      module_name  module_arguments
```

**PAM 模块接口(模块管理组)**

PAM为认证任务提供四种类型可用的模块接口，它们分别提供不同的认证服务：
* auth      - 认证模块接口，如验证用户身份、检查密码是否可以通过，并设置用户凭据
* account   - 账户模块接口，检查指定账户是否满足当前验证条件，如用户是否有权访问所请求的服务，检查账户是否到期
* password  - 密码模块接口，用于更改用户密码，以及强制使用强密码配置
* session   - 会话模块接口，用于管理和配置用户会话。会话在用户成功认证之后启动生效

**PAM 控制标志**

所有的 PAM 模块被调用时都会返回成功或者失败的结果，每个 PAM 模块中由多个对应的控制标志决定结果是否通过或失败。每一个控制标志对应一个处理结果，PAM 库将这些通过/失败的结果整合为一个整体的通过/失败结果，然后将结果返回给应用程序。模块可以按特定的顺序堆叠。控制标志是实现用户在对某一个特定的应用程序或服务身份验证的具体实现细节。该控制标志是 PAM 配置文件中的第二个字段，PAM 控制标志如下：

* required      - 模块结果必须成功才能继续认证，如果在此处测试失败，则继续测试引用在该模块接口的下一个模块，直到所有的模块测试完成，才将结果通知给用户。
* requisite     - 模块结果必须成功才能继续认证，如果在此处测试失败，则会立即将失败结果通知给用户。
* sufficient    - 模块结果如果测试失败，将被忽略。如果 sufficient 模块测试成功，并且之前的 required 模块没有发生故障，PAM 会向应用程序返回通过的结果，不会再调用堆栈中其他模块。
* optional      - 该模块返回的通过 / 失败结果被忽略。当没有其他模块被引用时，标记为 optional 模块并且成功验证时该模块才是必须的。该模块被调用来执行一些操作，并不影响模块堆栈的结果。
* include       - 与其他控制标志不同，include 与模块结果的处理方式无关。该标志用于直接引用其他 PAM 模块的配置参数

---

## PAM模式使用说明

### pam_access.so

pam_access.so 模块主要的功能和作用是根据主机名（包括普通主机名或者 FQDN）、IP 地址和用户实现全面的访问控制。pam_access.so 模块的具体工作行为根据配置文件 `/etc/security/access.conf` 来决定。该配置文件的主体包含了三个字段——权限、用户和访问发起方。格式上是一个用 "" 隔开的表。
* 第一个字段：权限（permission），使用 "+" 表示授予权限，用 "-" 表示禁止权限。
* 第二个字段：用户（user），定义了用户、组以及用 "@" 表示的在不同主机上的同名用户和同一主机上不同名用户。
* 第三个字段：访问发起方（origins），定义了发起访问的主机名称、域名称、终端名称。

而且 `/etc/security/access.conf` 文件提供了很多范例供修改时参考，并且都给出了具体的说明，例如：
```bash
#禁止非root用户通过tty1访问相关服务
#-:ALL EXCEPT root:tty1

#禁止除了wheel、shutdown以及sync之外的所有用户访问相关服务
#-:ALL EXCEPT wheel shutdown sync:LOCAL

#禁止wheel用户通过.win.tue.nl之外的其它它终端访问相关服务
#-:wheel:ALL EXCEPT LOCAL .win.tue.nl

# 禁止下面的用户从任何主机登录。其它用户可以从任意地方访问相关服务
#-:wsbscaro wsbsecr wsbspac wsbsym wscosor wstaiwde:ALL

# root用户允许通过cron来使用tty1到tty6终端访问相关服务
#+ : root : cron crond :0 tty1 tty2 tty3 tty4 tty5 tty6

# 用户root允许从下面的地址访问相关服务
#+ : root : 192.168.200.1 192.168.200.4 192.168.200.9
#+ : root : 127.0.0.1

# 用户root可以从192.168.201.网段访问相关服务
#+ : root : 192.168.201.

# 用户root可以从.foo.bar.org中任何主机访问相关服务
#+ : root : .foo.bar.org

# 用户root不允许从任何主机访问相关服务
#- : root : ALL

# 用户@nis_group和foo可以从任何主机访问相关服务
#+ : @nis_group foo : ALL

# 用户john只能从127.0.0.0/24来对本机相关服务进行访问
#+ : john : 127.0.0.0/24

# 用户john可以通过ipv4和ipv6的地址对本机相关服务进行访问
#+ : john : ::ffff:127.0.0.0/127

# 用户john可以通过ipv6的地址访问本机相关服务
#+ : john : 2001:4ca0:0:101::1

# 用户john可以通过ipv6的主机IP地址来访问本机
#+ : john : 2001:4ca0:0:101:0:0:0:1

# 用户john可以通过ipv6的IP地址和掩码来访问相关服务
#+ : john : 2001:4ca0:0:101::/64

# 开放所有用户对本机所有相关服务的访问
#- : ALL : ALL
```

**示例 : 如果要在网络内架设一个 FTP 服务器，而且在该 FTP 服务器上需要强制地指定某个用户只能通过某个 IP 地址登录**

```diff
vim /etc/pam.d/vsftpd

#%PAM-1.0
session    optional     pam_keyinit.so    force revoke
auth       required pam_listfile.so item=user sense=deny file=/etc/vsftpd/ftpusers onerr=succeed
auth       required pam_shells.so
auth       include  password-auth
account    include  password-auth
++ account    required     pam_access.so                 // 添加这一行内容
session    required     pam_loginuid.so
session    include  password-auth
```

修改 `/etc/security/access.conf` 配置文件, 在文件底部添加下面的两行
```diff
vim /etc/security/access.conf

++ - : kevin : ALL EXCEPT 192.168.10.101
++ - : grace : ALL EXCEPT 192.168.10.101
```

kevin 和 grace 用户不能从 192.168.10.101 之外的任何客户端访问 FTP 服务器；

修改 `/etc/vsftpd/vsftpd.conf` 文件，禁用匿名登录
```diff
++ Anonymous_enable = NO
```

重启 vsftpd 服务

针对这种需求而且不想使用防火墙以及应用程序自带的认证机制的时候，通过 pam_access.so 可以实现所需的效果

### pam_listfile.so

pam_listfile.so 模块的功能和 pam_access.so 模块类似，目标也是实现基于用户/组，主机名/IP，终端的访问控制。不过它实现的方式和 pam_access.so 会稍微有些不同，因为它没有专门的默认配置文件。访问控制是靠 pam 配置文件中的控制选项和一个自定义的配置文件来实现的。而且除了针对上述访问源的控制之外，还能够控制到 ruser，rhost，所属用户组和登录 shell。所以有些用户认为它的功能似乎比 pam_access.so 更加灵活和强大一些。

使用 pam_listfile.so 模块配置的格式分为五个部分：分别是 item、onerr、sense、file 以及 apply。 其中：
* item=[tty|user|rhost|ruser|group|shell]：定义了对哪些列出的目标或者条件采用规则，显然，这里可以指定多种不同的条件。
* onerr=succeed|fail：定义了当出现错误（比如无法打开配置文件）时的缺省返回值。
* sense=allow|deny：定义了当在配置文件中找到符合条件的项目时的控制方式。如果没有找到符合条件的项目，则一般验证都会通过。
* file=filename：用于指定配置文件的全路径名称。
* apply=user|@group：定义规则适用的用户类型（用户或者组）。

**示例 : 不允许 bobo 账号通过 ssh 方式登录**

针对这种需求只需要更改 `/etc/pam.d/sshd` 文件，并在该文件中添加一行（一定要添加到第一行）
```diff
vim /etc/pam.d/sshd

++ auth required pam_listfile.so  item=user sense=deny file=/etc/pam.d/denyusers onerr=succeed
```

建立文件/etc/pam.d/denyusers，并在文件中写入用户信息
```
echo "bobo" > /etc/pam.d/denyusers
```

表示用户以 ssh 登录必须要通过 pam_listfile.so 模块进行认证，认证的对象类型是用户，采用的动作是禁止，禁止的目标是 `/etc/pam.d/denyuser` 文件中所定义的用户。

这样在该条目添加到该文件之后，使用 bobo 账号从其它主机远程 ssh 访问服务器会出现密码错误的提示，但是使用 root 或者其它用户则访问能够成功！

再次强调，要注意 pam 模块使用的顺序，刚才的规则一定要添加到 `/etc/pam.d/sshd` 文件的 auth 的第一行之前，否则不会生效

**示例 : 仅仅允许 kevin 用户可以通过 ssh 远程登录。**

在 `/etc/pam.d/sshd` 文件中添加一条（务必添加到文件的第一行！）：
```diff
vim /etc/pam.d/sshd

++ auth required pam_listfile.so item=user sense=allow file=/etc/sshdusers onerr=succeed
```
```
echo "kevin" >/etc/sshdusers
```

注：此处如果 root 也使用 ssh 远程连接，也会受到 pam_listfile.so 限制的。

### pam_limits.so

pam_limits.so 模块的主要功能是限制用户会话过程中对各种系统资源的使用情况。缺省情况下该模块的配置文件是 `/etc/security/limits.conf` 。而该配置文件的基本格式实际上是由 4 个字段组成的表，其中具体限制的内容包括：
```
Domain            type            item                                     value
用户名 / 组名       软 / 硬限制     core——core 文件大小 (KB)                    具体值
　　                              data——最大数据大小 (KB)
　　                              fsize——最大文件大小 (KB)
　　                              memlock——最大可用内存空间 (KB)
　　                              nofile——最大可以打开的文件数量
　　                              rss——最大可驻留空间 (KB)
　　                              stack——最大堆栈空间 (KB)
　　                              cpu——最大 CPU 使用时间（MIN）
　　                              nproc——最大运行进程数
　　                              as——地址空间限制
　　                              maxlogins——用户可以登录到系统最多次数
　　                              locks——最大锁定文件数目
```

需要注意的是，如果没有任何限制可以使用 "-" 号，并且针对用户限制的优先级一般要比针对组限制的优先级更高。

使用 pam_limits.so 模块的最常见的场景是在运行 Oracle 数据库的 RHEL 服务器中，因为一般 Oracle 数据库在安装之前，按照其官方文档的说明需要先对某些用户（Oracle）使用系统资源的情况进行限制。所以我们总是能够在 Oracle 数据库服务器的 `/etc/security/limits.conf` 文件中看到类似这样的配置：
```
vim /etc/security/limits.conf
.......
oracle           soft    nproc   2047
oracle           hard    nproc   16384
oracle           soft    nofile  1024
oracle           hard    nofile  65536
```

结合上面的配置文件说明，可知 Oracle 数据库需要对 Oracle 用户使用资源的情况进行一些限制，包括： oracle 用户最大能开启的进程数不超过 16384，最大能打开的文件数不超过 65536。

顺便提一下，针对 nofile，这个只是基于用户层面的限制和调整方法。基于系统层面的限制和调整方法是修改 / etc/sysctl.conf 文件，直接改 fs.file-max 参数，调整之后 sysctl –p 生效。

**示例 : 限制用户 bobo 登录到 SSH 服务器时的最大连接数（防止同一个用户开启过多的登录进程）**

/etc/pam.d/system-auth 中，默认就会通过 pam_limits.so 限制用户最多使用多少系统资源
```
cat /etc/pam.d/system-auth|grep limits.so
session     required      pam_limits.so
```

因此只需要在 `/etc/security/limits.conf` 文件中增加一行对 bobo 用户产生的连接数进行限定：
```diff
vim /etc/security/limits.conf

++ bobo             hard    maxlogins       2
```

### pam_rootok.so

一般情况下，pam_rootok.so 模块的主要作用是使 uid 为 0 的用户，即 root 用户能够直接通过认证而不用输入密码。pam_rootok.so 模块的一个典型应用是插入到一些应用程序的认证配置文件中，当 root 用户执行这些命令的时候可以不用输入口令而直接通过认证。比如说 "su" 命令，为什么当以 root 用户执行 "su" 切换到普通用户身份的时候是不需要输入任何口令而可以直接切换过去？

查看一下 `/etc/pam.d/su` 文件的内容
```
cat /etc/pam.d/su

auth        sufficient  pam_rootok.so
```

而如果将该行配置注释掉的情况下，就会发现即便以 root 用户切换普通用户的时候仍然要求输入口令。

另外一种方法，只需要将上述的 "sufficient" 改成 "required" 即可。因为这样，pam_rootok.so 模块的验证通过就成为了必要条件之一。

pam_rootok.so 模块的另外一个应用是在 chfn 命令中。Chfn 命令用于改变 `/etc/passwd` 中的用户的说明字段。当以 root 身份执行 chfn 命令修改用户信息的时候是不用输入密码的。但是以普通用户身份执行 chfn 则需要输入密码之后才能改变自己的用户说明。这实际上也是因为在 `/etc/pam.d/chfn` 配置文件中的第一行调用了 pam_rootok.so 的结果。

不过这里即便将该配置中的第一行注释掉，root 用户通过 chfn 修改自己信息的时候仍然不需要使用密码。所以恐怕效果不是很明显。究其原因主要是很多 PAM 模块对 root 用户是不会产生限制的。

可以在 `/etc/pam.d/su` 文件里设置禁止用户使用 su 命令
```bash
vim /etc/pam.d/su
auth sufficient pam_rootok.so
#auth required pam_wheel.so use_uid
```

以上两行是默认状态（即开启第一行，注释第二行），这种状态下是允许所有用户间使用 su 命令进行切换的！（或者两行都注释也是运行所有用户都能使用 su 命令，但 root 下使用 su 切换到其他普通用户需要输入密码；如果第一行不注释，则 root 使用 su 切换普通用户就不需要输入密码）

如果开启第二行，表示只有 root 用户和 wheel 组内的用户才可以使用 su 命令。

如果注释第一行，开启第二行，表示只有 wheel 组内的用户才能使用 su 命令，root 用户也被禁用 su 命令。

### pam_userdb.so

pam_userdb.so 模块的主要作用是通过一个轻量级的 Berkeley 数据库来保存用户和口令信息。这样用户认证将通过该数据库进行，而不是传统的 `/etc/passwd` 和 `/etc/shadow` 或者其它的一些基于 LDAP 或者 NIS 等类型的网络认证。所以存在于 Berkeley 数据库中的用户也称为虚拟用户。

pam_userdb.so 模块的一个典型用途就是结合 vsftpd 配置基于虚拟用户访问的 FTP 服务器。

相对于本地用户以及匿名用户来说，虚拟用户只是相对于 FTP 服务器而言才有用的用户，这些用户被严格地限定在 pam_userdb 数据库当中。所以虚拟用户只能访问 FTP 服务器所提供的资源，因而可以大大提高系统安全性。另外相对于匿名用户而言，虚拟用户必须通过用户名和密码才能够访问 FTP 的资源。这样也提高了对 FTP 用户下载的可管理性。

基于虚拟用户实现的 vsftpd 的原理基本上是这样一个过程：先定义一些专门针对 FTP 的虚拟用户，然后将用户信息加入到系统自带的数据库中（但不是 passwd）从而生成一个访问 FTP 的虚拟用户列表，这里使用的数据库是 db4 也就是 Berkeley DB。然后可以通过使用 pam_userdb.so 模块来调用该数据库存储用户信息以及实现 FTP 用户认证。当然同时也可以在系统中通过对配置文件的定义和划分来实现对不同虚拟用户不同类型的访问控制。

### pam_cracklib.so

pam_cracklib.so 是一个常用并且非常重要的 PAM 模块。该模块主要的作用是对用户密码的强健性进行检测。即检查和限制用户自定义密码的长度、复杂度和历史等。如不满足上述强度的密码将拒绝用户使用。pam_cracklib.so 比较重要和难于理解的是它的一些参数和计数方法，其常用参数包括：
```
debug：    将调试信息写入日志；
type=xxx： 当添加 / 修改密码时，系统给出的缺省提示符是 "New UNIX password:" 以及 "Retype UNIX password:"，而使用该参数可以自定义输入密码的提示符，比如指定 type=your own word；
retry=N：  定义登录 / 修改密码失败时，可以重试的次数；
Difok=N：  定义新密码中必须至少有几个字符要与旧密码不同。但是如果新密码中有 1/2 以上的字符与旧密码不同时，该新密码将被接受；
minlen=N： 定义用户密码的最小长度；
dcredit=N：定义用户密码中必须至少包含多少个数字；
ucredit=N：定义用户密码中必须至少包含多少个大写字母；
lcredit=N：定义用户密码中必须至少包含多少个小些字母；
ocredit=N：定义用户密码中必须至少包含多少个特殊字符（除数字、字母之外）；

注意
当 N>0 时，N 代表新密码中最多可以有 N 个指定的字符
当 N<0 时，N 代表新密码中最少可以有 N 个指定的字符
```

### pam_pwhistroy.so

pam_pwhistory.so 模块也是一个常用模块，一般辅助 pam_cracklib.so，pam_tally.so 以及 pam_unix.so 等模块来加强用户使用密码的安全度。不过 pam_pwhistory.so 模块起的是另一类的作用，即专门为用户建立一个密码历史档案，防止用户在一定时间内使用已经用过的密码。

`/etc/pam.d/system-auth` 下的配置针对的是普通用户，在 root 用户下是无效的

当需要限定用户在 90 天之内不能重复使用以前曾经使用过的 10 个密码，那么具体操作方法是去修改 `/etc/pam.d/system-auth` 文件，在 password 接口处增加：
```
password  required  pam_cracklib.so  retry=3  password  required  pam_pwhistory.so enforce_for_root remember=10
```

此时用户使用过的密码将会记录到 `/etc/security/opasswd` 文件中。但是 pam_pwhistory.so 并没有什么选项可以限定密码在多少天之内无法被重复使用，
所以上述的 90 天是无法配置的。一个简单的解决方法就是当 90 天左右的时候，手动清空一次 opasswd 文件即可。

当然，如果要实现同样的功能除了 pam_pwhistory.so 模块之外还有其它的办法。比较常用的是 pam_unix.so 模块。

具体方法是修改 `/etc/pam.d/system-auth` 文件，给 pam_unix.so 模块里加上 remember=10 这个选项，修改之后的配置文件为：
```diff
vim /etc/pam.d/system-auth

++ password required pam_unix.so md5 remember=10 use_authtok
```

不过此时 `/etc/security/opasswd` 文件因为记录了 N 个使用过的密码，所以安全性就十分关键了，所以要确保该文件只能被 root 用户读取和编辑：

---

## PAM身份验证安全配置实例

### 用户设置的密码不能与过去3次内的密码重复

修改 `/etc/pam.d/system-auth`, 增加 pam_unix.so 的参数，如下：
```
vim /etc/pam.d/system-auth
......
password    sufficient    pam_unix.so md5 shadow nullok try_first_pass use_authtok remember=3
```

### 用户设置的密码必须至少包含5个数字和3个特殊符号

修改 `/etc/pam.d/system-auth`，在 password 使用 pam_cracklib.so 设置的最后附加 dcredit=-5 ocredit=-3
```
vim /etc/pam.d/system-auth
......
password    requisite     pam_cracklib.so try_first_pass retry=3 dcredit=-5 ocredit=-3
```

### 限制kevin用户最多同时登陆4个

这需要 pam_limits.so 模块。由于 `/etc/pam.d/system-auth` 中，默认就会通过 pam_limits.so 限制用户最多使用多少系统资源.
```
cat /etc/pam.d/system-auth|grep limits.so
session     required      pam_limits.so
```

因此只需要在 `/etc/security/limits.conf` 中加入以下内容:
```
vim /etc/security/limits.conf
......
kevin        hard       maxlogins       4
```

### 强制使用强密码 (用户密码安全配置)

PAM 配置文件：`/etc/pam.d/system-auth-ac`

模块名称: pam_cracklib(仅适用于 password 模块接口)

模块参数:
* minlen=12             密码字符长度不少于 12 位 (默认为 9)
* lcredit=-1            至少包含 1 个小写字母
* ucredit=-1            至少包含 1 个大写字母
* dcredit=-1            至少包含 1 个数字
* ocredit=-1            至少包含 1 个特殊字符
* retry=3               配置密码时，提示 3 次用户密码错误输入
* difok=6               配置密码时，新密码中至少 6 个字符与旧密码不同 (默认为 5)

其他常用参数：
* reject_username       新密码中不能包含与用户名称相同的字段
* maxrepeat=N           拒绝包含超过 N 个连续字符的密码，默认值为 0 表示此检查已禁用
* maxsequence=N         拒绝包含大于 N 的单调字符序列的密码，例如’1234’或’fedcb’，默认情况下即使没有这个参数配置，一般大多数这样的密码都不会通过，除非序列只是密码的一小部分
* maxclassrepeat=N      拒绝包含相同类别的 N 个以上连续字符的密码。默认值为 0 表示此检查已禁用。
* use_authtok           强制使用先前的密码，不提示用户输入新密码 (不允许用户修改密码)

模块名称：pam_unix (适用于 account，auth， password 和 session 模块接口)

模块参数：
* remember=N            保存每个用户使用过的 N 个密码，强制密码不能跟历史密码重复

其他常见参数：
* sha512                当用户下一次更改密码时，使用 SHA256 算法进行加密
* md5                   当用户更改密码时，使用 MD5 算法对其进行加密。
* try_first_pass        在提示用户输入密码之前，模块首先尝试先前的密码，以测试是否满足该模块的需求。
* use_first_pass        该模块强制使用先前的密码 (不允许用户修改密码)，如果密码为空或者密码不对，用户将被拒绝访问
* shadow                用户保护密码
* nullok                默认不允许空密码访问服务
* use_authtok           强制使用先前的密码，不提示用户输入新密码 (不允许用户修改密码)

在 RHEL/CentOS 下的配置，passwd 程序的 PAM 配置文件涉及主配置文件 `/etc/pam.d/passwd` 和 `/etc/pam.d/system-auth-ac`（也可以是 `/etc/pam.d/password-auth-ac`），其中 `/etc/pam.d/passwd` 配置文件默认只包含了 `/etc/pam.d/system-auth-ac` 配置文件，因此对于以上 PAM 身份验证密码模块配置，只修改/配置该文件即可。

在 Ubuntu 中，配置文件包括：`/etc/pam.d/common-password`、`/etc/pam.d/common-account`、`/etc/pam.d/common-auth`、`/etc/pam.d/common-session`

设置 口令最小长度不小于8，至少包含大写字母、小写字母、数字和特殊字符中的三种。
```bash
# CentOS、Fedora、EulerOS操作系统
password requisite pam_cracklib.so try_first_pass retry=3 minlen=9 dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 type=

# Debian、Ubuntu操作系统
vim /etc/pam.d/common-password

password requisite pam_cracklib.so retry=3 minlen=9 dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 difok=3
```

### 用户 SSH 登录失败尝试次数超出限制后锁定账户 (帐户锁定/解锁和时间设置)

为了进一步提高安全性，可以指定超过失败登录尝试次数后锁定用户。用户账户可以被解锁（可以由 root 用户主动解锁），或者在设定的时间后自动解锁。

如在三次失败的登录尝试后锁定用户十分钟。需要在 `/etc/pam.d/password-auth-ac`(或者在 `/etc/pam.d/sshd`) 文件添加以下参数：

```
auth        required      pam_tally2.so deny=3 unlock_time=600 onerr=succeed file=/var/log/tallylog
```

在 Ubuntu、SuSE Linux 中，需要修改 `/etc/pam.d/common-auth` 配置文件

另外，使用 PAM 还可以限制在 console 控制台上登录，需要修改 `/etc/pam.d/system-auth` 配置文件 (或者 `/etc/pam.d/login`)，添加如上 auth 配置字段即可。

一旦用户失败登录尝试次数达到 3 次，该帐户立刻被锁定，除非 root 用户解锁。root 用户下使用如下命令解锁用户：
```
pam_tally2 -u username -r --reset
```

查看用户登录失败信息
```
pam_tally2 -u username
```

如果要在 3 次失败登录尝试后永久锁定用户，那么需要删除 unlock_time 字段，除非 root 用户解锁该账户，否则将永久锁定。

### pam_tally/pam_tally2 模块参数

全局选项
* onerr=[succeed|fail]
* file=/path/to/log     失败登录日志文件，默认为 `/var/log/tallylog`
* audit                 如果登录的用户没有找到，则将用户名信息记录到系统日志中
* silent                不打印相关的信息
* no_log_info           不通过 syslog 记录日志信息

AUTH 选项
* deny=n                失败登录次数超过 n 次后拒绝访问
* lock_time=n           失败登录后锁定的时间（秒数）
* unlock_time=n         超出失败登录次数限制后，解锁的时间
* no_lock_time          不在日志文件 `/var/log/faillog` 中记录. fail_locktime 字段
* magic_root            root 用户 (uid=0) 调用该模块时，计数器不会递增
* even_deny_root        root 用户失败登录次数超过 deny=n 次后拒绝访问
* root_unlock_time=n    与 even_deny_root 相对应的选项，如果配置该选项，则 root 用户在登录失败次数超出限制后被锁定指定时间

### 允许普通用户使用 sudo 而不是 su (限制普通用户登录到 root 用户)

Linux 系统上默认存在一个 wheel 组，用于限制普通用户通过 su 登录到 root 用户，只有属于 wheel 组的用户成员才能使用 su。但是在默认情况下，系统并没有启用这个功能，我们可以通过 PAM 启用它，或者修改为指定的组 / 用户使用 su，当然指定为什么组可以按照要求而定。该配置通过 pam_wheel 模块指定。

首先启用 whell 组，使得只属于 wheel 组的用户可以使用 su 命令, 需要在 `/etc/pam.d/su` 配置文件添加以下配置：
```
auth            required        pam_wheel.so use_uid
```

需要注意应该将这一行参数添加在 `/etc/pam.d/su` 文件的首部，否则 PAM 模块可能会跳过该项检查。配置完之后，我们就可以将需要用 su 权限的用户添加到 wheel 组中，如下：
```
usermod -a -G wheel username
```

其次，如果你不想使用 wheel 组，而是使用其他的组代替，比如指定组名为 myadmingroup 的组拥有 su 的权限，需要这么做：
```
auth            required        pam_wheel.so use_uid group=myadmingroup
```

最后配置指定用户拥有 sudo 权限，要知道我们的目的是尽量少使用 root 身份的权限，sudo 可以让用户仅仅在需要调用 root 用户权限的情况下调用。我们可以指定特定的组/用户使用 sudo(不需要 root 密码) 调用 root 权限。visudo 打开配置文件：
```
hmm    ALL=(ALL)     NOPASSWD: ALL   #允许hmm用户通过sudo执行任何命令(不需要输入密码)

%wheel  ALL=(ALL)    ALL             #允许wheel组成员使用sudo执行任何命令(需要输入密码)
```

**禁止直接使用 root 用户通过 SSH 登录**

在 `/etc/pam.d/password-auth-ac` 或者 `/etc/pam.d/sshd` 配置文件中添加以下配置（该配置禁止 SSH 的口令认证，但仍然可以使用 SSH 密钥登录）

```
auth        required      pam_securetty.so
```

此外还可以配置 `/etc/securetty` 文件禁止 root 用户通过所有 tty 终端登录系统
```bash
cp /etc/securetty /etc/securetty.saved
echo "" >/etc/securetty
```

### 限制 root 只能从 kevin.com 这台计算机使用 ssh 远程登陆

由于 ssh 服务器的程序文件使用 sshd, 而 sshd 刚好支持 PAM，验证如下：
```
ldd /usr/sbin/sshd | grep libpam.so
    libpam.so.0 => /lib64/libpam.so.0 (0x00007f36f254d000)
```

修改 `/etc/pam.d/sshd`, 加入第二行，如下：
```diff
vim /etc/pam.d/sshd
auth       include      system-auth
++ account    required     pam_access.so accessfile=/etc/deny_sshd
account    required     pam_nologin.so
```

创建 `/etc/deny_sshd` 文件
```diff
vim /etc/deny_sshd

++ -:root:ALL EXCEPT kevin.com
```

---

## Source & Reference

- https://developer.aliyun.com/article/560279
- https://www.cnblogs.com/kevingrace/p/8671964.html
