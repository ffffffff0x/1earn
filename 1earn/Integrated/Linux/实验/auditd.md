# auditd

---

## auditd.conf

```bash
# 目录或这个目录中的日志文件。
log_file =/var/log/audit/audit.log

# 日志所属组
log_group = root

# 审计应采用多少优先级推进守护进程。必须是非负数。0表示没有变化。
priority_boost = 4

# 多长时间向日志文件中写一次数据。值可以是 NONE、INCREMENTAL、DATA 和 SYNC 之一。如果设置为 NONE，则不需要做特殊努力来将数据 刷新到日志文件中。

# 如果设置为 INCREMENTAL，则用 freq 选项的值确定多长时间发生一次向磁盘的刷新。
# 如果设置为 DATA，则审计数据和日志文件一直是同步的。
# 如果设置为 SYNC，则每次写到日志文件时，数据和元数据是同步的。
flush = INCREMENTAL
# 如果 flush 设置为 INCREMETNAL，审计守护进程在写到日志文件中前从内核中接收的记录数

# max_log_file_action 设置为 ROTATE 时要保存的日志文件数目。必须是 0~99 之间的数。如果设置为小于 2，则不会循环日志。如果递 增了日志文件的数目，就可能有必要递增/etc/audit/audit.rules中的内核
freq = 20

# backlog 设置值，以便留出日志循环的时间。如果没有设置 num_logs 值，它就默认为 0，意味着从来不循环日志文件。
num_logs = 5

# 控制调度程序与审计守护进程之间的通信类型。有效值为 lossy 和 lossless。
# 如果设置为 lossy，若审计守护进程与调度程序之间的缓冲区已满 (缓冲区为 128 千字节)，则发送给调度程序的引入事件会被丢弃。然而，只要 log_format 没有设置为 nolog，事件就仍然会写到磁盘中。
# 如果设 置为 lossless，则在向调度程序发送事件之前和将日志写到磁盘之前，调度程序会等待缓冲区有足够的空间。
disp_qos = lossy

# 当启动这个守护进程时，由审计守护进程自动启动程序。所有守护进程都传递给这个程序。可以用它来进一步定制报表或者以与您的自定义分析程序兼容的不同格式产生它们。自定义程序的示例代码可以在 / usr/share/doc/audit- /skeleton.c 中找到。由于调度程序用根用户特权运行，因此使用这个选项时要极其小心。这个选项不是必需的。
dispatcher = /sbin/audispd

# 此选项控制计算机节点名如何插入到审计事件流中。它有如下的选择：none,  hostname, fqd, numeric, and user
# None 意味着没有计算机名被插入到审计事件中。
# hostname 通过 gethostname 系统调用返回的名称。
# fqd 意味着它 = 以主机名和解决它与 DNS 的完全合格的域名
# numeric 类似于 fqd 除解决本机的 IP 地址，为了使用这个选项，你可能想要测试’hostname -i’ 或 ’domainname-i’返回一个数字地址, 另外，此选项不如果 DHCP 的使用是因为你可以有不同的地址，在同一台机器上的时间推荐。
# user 是从名称选项中定义的字符串。默认值是没有
name_format = NONE

# 以兆字节表示的最大日志文件容量。当达到这个容量时，会执行 max_log_file _action 指定的动作
max_log_file = 6

# 当达到 max_log_file 的日志文件大小时采取的动作。值必须是 IGNORE、SYSLOG、SUSPEND、ROTATE 和 KEEP_LOGS 之 一。
# 如果设置为 IGNORE，则在日志文件达到 max_log_file 后不采取动作。
# 如果设置为 SYSLOG，则当达到文件容量时会向系统日志 / var /log/messages 中写入一条警告。
# 如果设置为 SUSPEND，则当达到文件容量后不会向日志文件写入审计消息。
# 如果设置为 ROTATE，则当达 到指定文件容量后会循环日志文件，但是只会保存一定数目的老文件，这个数目由 num_logs 参数指定。老文件的文件名将为 audit.log.N，其中 N 是一个数字。这个数字越大，则文件越老。
# 如果设置为 KEEP_LOGS，则会循环日志文件，但是会忽略 num_logs 参数，因此不会删除日志文件
max_log_file_action = ROTATE

# 以兆字节表示的磁盘空间数量。当达到这个水平时，会采取 space_left_action 参数中的动作
space_left = 75

# 当磁盘空间量达到 space_left 中的值时，采取这个动作。有效值为 IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE 和 HALT。
# 如果设置为 IGNORE，则不采取动作。
# 如果设置为 SYSLOG，则向系统日志 / var/log/messages 写一条警告消息。
# 如果设置为 EMAIL，则从 action_mail_acct 向这个地址发送一封电子邮件，并向 / var/log/messages 中写一条警告消息。
# 如果设置为 SUSPEND，则不再向审计日志文件中写警告消息。
# 如果设置为 SINGLE，则系统将在单用户模式下。如果设置为 SALT，则系统会关闭。
space_left_action = SYSLOG

# 负责维护审计守护进程和日志的管理员的电子邮件地址。如果地址没有主机名，则假定主机名为本地地址，比如 root。
# 必须安装 sendmail 并配置为向指定电子邮件地址发送电子邮件。
action_mail_acct = root

# 以兆字节表示的磁盘空间数量。用这个选项设置比 space_left_action 更多的主动性动作，以防万一 space_left_action 没有让管理员释放任何磁盘空间。这个值应小于 space_left_action。如果达到这个水平，则会采取 admin_space_left_ action 所指定的动作。
admin_space_left = 50

# 当自由磁盘空间量达到 admin_space_left 指定的值时，则采取动作。有效值为 IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE 和 HALT。
# 与这些值关联的动作与 space_left_action 中的相同。
admin_space_left_action = SUSPEND

# 如果含有这个审计文件的分区已满，则采取这个动作。可能值为 IGNORE、SYSLOG、SUSPEND、SINGLE 和 HALT。与这些值关联的动作
# 与 space_left_action 中的相同。
disk_full_action = SUSPEND

# 如果在写审计日志或循环日志文件时检测到错误时采取的动作。值必须是 IGNORE、SYSLOG、SUSPEND、SINGLE 和 HALT 之一。
# 与这些值关的动作与 space_left_action 中的相同
disk_error_action = SUSPEND

# 这是在范围 1、65535，一个数字值，如果指定，原因 auditd 听在从远程系统审计记录相应的 TCP 端口。审计程序可能与 tcp_wrappers。
# 你可能想控制在 hosts.allow 入口访问和否认文件。
##tcp_listen_port =

# 这是一个数字值，这表明有多少等待（要求但 UNAC 接受）的连接是允许的。默认值是 5。设置过小的可能导致连接被拒绝，
# 如果太多主机开始在完全相同的时间，如电源故障后。
tcp_listen_queue = 5

# 这是一个数字值，该值表示一个地址允许有多少个并发连接。默认为 1，最大为 1024。设置过大可能会允许拒绝服务攻击的日志服务器。
# 还要注意的是，内核内部有一个最大的，最终将防止这种即使 auditd 允许它通过配置。在大多数情况下，默认应该是足够除非写一个自定义的恢复脚本运行提出未发送事件。在这种情况下，您将增加的数量只有足够大，让它在过。
tcp_max_per_addr = 1

##tcp_client_ports = 1024-65535
tcp_client_max_idle = 0

# 如果设置为 “yes”，Kerberos 5 将用于认证和加密。默认是 “no”。
enable_krb5 = no

# This is the principal for this server. 默认是 "auditd"。 考虑到这个默认值，服务器将寻找存储在 / etc/audit/audit.key 中的类似 auditd/hostname@EXAMPLE.COM 的密钥来验证自己，其中 hostname 是服务器主机的规范名称，由 DNS 查询其 IP 地址返回。
krb5_principal = auditd

# Location of the key for this client's principal. 注意，该密钥文件必须由root拥有，模式为0400。默认是/etc/audit/audit.key。
##krb5_key_file = /etc/audit/audit.key
```

---

## Source & Reference

- https://man7.org/linux/man-pages/man5/auditd.conf.5.html
- https://blog.csdn.net/u012085379/article/details/50973245
