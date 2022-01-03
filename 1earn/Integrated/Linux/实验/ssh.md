# ssh

---

## 配置文件

sshd 配置文件是 : /etc/ssh/sshd_config

```bash
Port 22                 # 设置 ssh 监听的端口号，默认 22 端口

ListenAddress 0.0.0.0   # 指定监听的地址，默认监听所有；
Protocol 2,1            # 指定支持的 SSH 协议的版本号。'1'和'2'表示仅仅支持 SSH-1 和 SSH-2 协议。"2,1" 表示同时支持 SSH-1 和 SSH-2 协议。

HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_dsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key
HostKey /etc/ssh/ssh_host_ed25519_key
# HostKey 是主机私钥文件的存放位置;
# SSH-1 默认是 /etc/ssh/ssh_host_key 。
# SSH-2 默认是 /etc/ssh/ssh_host_rsa_key 和 /etc/ssh/ssh_host_dsa_key 。一台主机可以拥有多个不同的私钥。"rsa1" 仅用于 SSH-1，"dsa" 和 "rsa" 仅用于 SSH-2。

UsePrivilegeSeparation yes      # 是否通过创建非特权子进程处理接入请求的方法来进行权限分离。默认值是"yes"。 认证成功后，将以该认证用户的身份创另一个子进程。这样做的目的是为了防止通过有缺陷的子进程提升权限，从而使系统更加安全。

KeyRegenerationInterval 3600    # 在 SSH-1 协议下，短命的服务器密钥将以此指令设置的时间为周期 (秒)，不断重新生成；这个机制可以尽量减小密钥丢失或者黑客攻击造成的损失。设为 0 表示永不重新生成为 3600(秒)。

ServerKeyBits 1024              # 指定服务器密钥的位数
SyslogFacility AUTH             # 指定将日志消息通过哪个日志子系统 (facility) 发送。有效值是：DAEMON, USER, AUTH(默认), LOCAL0, LOCAL1, LOCAL2, LOCAL3,LOCAL4, LOCAL5,LOCAL6, LOCAL7

LogLevel INFO                   # 指定日志等级(详细程度)。可用值如下: QUIET, FATAL, ERROR, INFO(默认), VERBOSE, DEBUG, DEBUG1, DEBUG2, DEBUG3
# DEBUG 与 DEBUG1 等价；
# DEBUG2 和 DEBUG3 则分别指定了更详细、更罗嗦的日志输出。比 DEBUG 更详细的日志可能会泄漏用户的敏感信息，因此反对使用。

LoginGraceTime 120              # 限制用户必须在指定的时限 (单位秒) 内认证成功，0 表示无限制。默认值是 120 秒; 如果用户不能成功登录，在用户切断连接之前服务器需要等待 120 秒。

PermitRootLogin yes
# 是否允许 root 登录。可用值如下："yes"(默认) 表示允许。
#"no" 表示禁止。
# "without-password" 表示禁止使用密码认证登录。
# "forced-commands-only" 表示只有在指定了 command 选项的情况下才允许使用公钥认证登录，同时其它认证方法全部被禁止。这个值常用于做远程备份之类的事情。

StrictModes yes                 # 指定是否要求 sshd(8) 在接受连接请求前对用户主目录和相关的配置文件 进行宿主和权限检查。强烈建议使用默认值"yes"来预防可能出现的低级错误。

RSAAuthentication yes           # 是否允许使用纯 RSA 公钥认证。仅用于 SSH-1。默认值是 "yes"。

PubkeyAuthentication yes        # 是否允许公钥认证。仅可以用于 SSH-2。默认值为 "yes"。

IgnoreRhosts yes                # 是否取消使用 ~/.ssh/.rhosts 来做为认证。推荐设为 yes。

RhostsRSAAuthentication no      # 这个选项是专门给 version 1 用的，使用 rhosts 档案在 /etc/hosts.equiv 配合 RSA 演算方式来进行认证！推荐 no。

HostbasedAuthentication no      # 这个与上面的项目类似，不过是给 version 2 使用的

IgnoreUserKnownHosts no         # 是否在 RhostsRSAAuthentication 或 HostbasedAuthentication 过程中忽略用户的 ~/.ssh/known_hosts 文件。默认值是 "no"。为了提高安全性，可以设为 "yes"。

PermitEmptyPasswords no         # 是否允许密码为空的用户远程登录。默认为 "no"。

ChallengeResponseAuthentication no  # 是否允许质疑 - 应答 (challenge-response) 认证。默认值是 "yes"，所有 login.conf 中允许的认证方式都被支持。

PasswordAuthentication yes      # 是否允许使用基于密码的认证。默认为 "yes"。

KerberosAuthentication no       # 是否要求用户为 PasswordAuthentication 提供的密码必须通 过 Kerberos KDC 认证，也就是是否使用 Kerberos 认证。使用 Kerberos 认证，服务器需要一个可以校验 KDC identity 的 Kerberos servtab 。默认值是 "no"。

KerberosGetAFSToken no          # 如果使用了 AFS 并且该用户有一个 Kerberos 5 TGT，那么开启该指令后, 将会在访问用户的家目录前尝试获取一个 AFS  token 。默认为 "no"。

KerberosOrLocalPasswd yes       # 如果 Kerberos 密码认证失败，那么该密码还将要通过其它的认证机制(比如 /etc/passwd)。默认值为"yes"。

KerberosTicketCleanup yes       # 是否在用户退出登录后自动销毁用户的 ticket 。默认 "yes"。

GSSAPIAuthentication no         # 是否允许使用基于 GSSAPI 的用户认证。默认值为 "no"。仅用 于 SSH-2。

GSSAPICleanupCredentials yes    # 是否在用户退出登录后自动销毁用户凭证缓存。默认值是 "yes"。仅用于 SSH-2。

X11Forwarding no                # 是否允许进行 X11 转发。默认值是 "no"，设为 "yes" 表示允许。如果允许 X11 转发并且 sshd 代理的显示区被配置为在含有通配符的地址 (X11UseLocalhost) 上监听。那么将可能有额外的信息被泄漏。由于使用 X11 转发的可能带来的风险，此指令默认值为 "no"。需要注意的是，禁止 X11 转发并不能禁止用户转发 X11 通信，因为用户可以安装他们自己的转发器。如果启用了 UseLogin ，那么 X11 转发将被自动禁止。

X11DisplayOffset 10             # 指定 X11 转发的第一个可用的显示区 (display) 数字。默认值是 10 。这个可以用于防止 sshd 占用了真实的 X11 服务器显示区，从而发生混淆。

PrintMotd no                    # 登入后是否显示出一些信息呢？例如上次登入的时间、地点等等，预设是 yes ，但是，如果为了安全，可以考虑改为 no ！

PrintLastLog yes                # 指定是否显示最后一位用户的登录时间。默认值是 "yes"

TCPKeepAlive yes                # 指定系统是否向客户端发送 TCP keepalive 消息。默认值是 "yes"。这种消息可以检测到死连接、连接不当关闭、客户端崩溃等异常。可以设为 "no" 关闭这个特性。

UseLogin no                     # 是否在交互式会话的登录过程中使用 login。默认值是 "no"。如果开启此指令，那么 X11Forwarding 将会被禁止，因为 login 不知道如何处理 xauth cookies 。需要注意的是，login 是禁止用于远程执行命令的。如果指定了 UsePrivilegeSeparation ，那么它将在认证完成后被禁用。

MaxStartups 10                  # 最大允许保持多少个未认证的连接。默认值是 10 。到达限制后，将不再接受新连接，除非先前的连接认证成功或超出 LoginGraceTime 的限制。

MaxAuthTries 6                  # 指定每个连接最大允许的认证次数。默认值是 6 。如果失败认证的次数超过这个数值的一半，连接将被强制断开，且会生成额外的失败日志消息。

UseDNS no                       # 指定是否应该对远程主机名进行反向解析，以检查此主机名是否与其 IP 地址真实对应。

Banner /etc/issue.net           # 将这个指令指定的文件中的内容在用户进行认证前显示给远程用户。这个特性仅能用于 SSH-2，默认什么内容也不显示。"none" 表示禁用这个特性。

Subsystem sftp /usr/lib/openssh/sftp-server     # 配置一个外部子系统 (例如，一个文件传输守护进程)。仅用于 SSH-2 协议。值是一个子系统的名字和对应的命令行 (含选项和参数)。

UsePAM yes                      # 是否使用 PAM 模块认证
```

---

## Source & Reference

- https://blog.51cto.com/xujpxm/1717862
- https://www.agwa.name/blog/post/ssh_signatures
