# mysql

---

## my.cnf 配置文件

```bash
port = 3309
socket =  /usr/local/mysql/tmp/mysql.sock

[mysqld]                    # 服务器端配置
!include  /usr/local/mysql/etc/mysqld.cnf   # 包含的配置文件，可以把用户名和密码文件单独存放
port = 3306　　             # 监听端口　　
bind-address = 0.0.0.0　　  # 监听的 ip 地址 (全0是监听所有网口,即对外开放,不建议⚠❗)
server-id = 1　　           # MySQL 服务的 ID
socket = /usr/local/mysql/tmp/mysql.sock    # socket 通信设置
pid-file = /usr/local/mysql/var/mysql.pid   # pid 文件路径
basedir = /usr/local/mysql/                 # MySQL 程序路径
datadir = /usr/local/mysql/data             # 数据目录
tmpdir = /usr/local/mysql/tmp/
# 此目录被 MySQL 用来保存临时文件. 例如, 它被用来处理基于磁盘的大型排序, 和内部排序一样，以及简单的临时表. 如果你不创建非常大的临时文件, 将其放置到 swapfs/tmpfs 文件系统上也许比较好。另一种选择是你也可以将其放置在独立的磁盘上. 你可以使用”;” 来放置多个路径，他们会按照 roud-robin 方法被轮询使用.

slave-load-tmpdir = /usr/local/mysql/tmp/   # 当 slave 执行 load data infile 时使用
```

### skip options 相关选项

```bash
skip-name-resolve
# 禁止 MySQL 对外部连接进行 DNS 解析，使用这一选项可以消除 MySQL 进行 DNS 解析的时间。但需要注意，如果开启该选项，则所有远程主机连接授权都要使用 IP 地址方式，否则 MySQL 将无法正常处理连接请求！

skip-symbolic-links
# 不能使用连接文件，多个客户可能会访问同一个数据库，因此这防止外部客户锁定 MySQL 服务器。 该选项默认开启

skip-external-locking
# 不使用系统锁定，要使用 myisamchk,必须关闭服务器 ,避免 MySQL的外部锁定，减少出错几率增强稳定性。

skip-slave-start
# 启动 mysql,不启动复制

skip-networking
# 开启该选项可以彻底关闭 MySQL 的 TCP/IP 连接方式，如果 WEB 服务器是以远程连接的方式访问 MySQL 数据库服务器则不要开启该选项！否则将无法正常连接！ 如果所有的进程都是在同一台服务器连接到本地的 mysqld, 这样设置将是增强安全的方法

sysdate-is-now = 1
# 把SYSDATE 函数编程为 NOW的别名

skip-grant-tables
# ⚠❗ 在启动mysql时不启动grant-tables，授权表,在忘记管理员密码后有用
```

### 系统资源相关选项

```bash
back_log = 50
# 接受队列，对于没建立 tcp 连接的请求队列放入缓存中，队列大小为 back_log，受限制与 OS 参数，试图设定 back_log 高于你的操作系统的限制将是无效的。默认值为 50。对于 Linux 系统推荐设置为小于 512 的整数。如果系统在一个短时间内有很多连接，则需要增大该参数的值

max_connections = 1000
# 指定 MySQL 允许的最大连接进程数。如果在访问数据库时经常出现 "Too Many Connections" 的错误提 示，则需要增大该参数值。

max_connect_errors = 10000
# 如果某个用户发起的连接 error 超过该数值，则该用户的下次连接将被阻塞，直到管理员执行 flush hosts ; 命令或者服务重启， 防止黑客 ， 非法的密码以及其他在链接时的错误会增加此值

open_files_limit = 10240
#MySQL 打开的文件描述符限制，默认最小 1024; 当 open_files_limit 没有被配置的时候，比较 max_connections*5 和 ulimit-n 的值，哪个大用哪个，当 open_file_limit 被配置的时候，比较 open_files_limit 和 max_connections*5 的值，哪个大用哪个。

connect-timeout = 10
# 连接超时之前的最大秒数, 在 Linux 平台上，该超时也用作等待服务器首次回应的时间

wait-timeout = 28800
# 等待关闭连接的时间

interactive-timeout = 28800
# 关闭连接之前，允许 interactive_timeout（取代了 wait_timeout）秒的不活动时间。客户端的会话 wait_timeout 变量被设为会话 interactive_timeout 变量的值。如果前端程序采用短连接，建议缩短这 2 个值, 如果前端程序采用长连接，可直接注释掉这两个选项，默认配置(8 小时)

slave-net-timeout = 600
# 从服务器也能够处理网络连接中断。但是，只有从服务器超过 slave_net_timeout 秒没有从主服务器收到数据才通知网络中断

net_read_timeout = 30
# 从服务器读取信息的超时

net_write_timeout = 60
# 从服务器写入信息的超时

net_retry_count = 10
# 如果某个通信端口的读操作中断了，在放弃前重试多次

net_buffer_length = 16384
# 包消息缓冲区初始化为 net_buffer_length 字节，但需要时可以增长到 max_allowed_packet 字节

max_allowed_packet = 64M
# 服务所能处理的请求包的最大大小以及服务所能处理的最大的请求大小(当与大的 BLOB 字段一起工作时相当必要)， 每个连接独立的大小. 大小动态增加。 设置最大包, 限制 server 接受的数据包大小，避免超长 SQL 的执行有问题 默认值为 16M，当 MySQL 客户端或 mysqld
服务器收到大于 max_allowed_packet 字节的信息包时，将发出 “信息包过大” 错误，并关闭连接。对于某些客户端，如果通信信息包过大，在执行查询期间，可能会遇到 “丢失与 MySQL 服务器的连接” 错误。默认值 16M。

table_cache = 512
# 所有线程所打开表的数量. 增加此值就增加了 mysqld 所需要的文件描述符的数量这样你需要确认在 [mysqld_safe] 中 “open-files-limit” 变量设置打开文件数量允许至少 4096

thread_stack = 192K
# 线程使用的堆大小. 此容量的内存在每次连接时被预留. MySQL 本身常不会需要超过 64K 的内存如果你使用你自己的需要大量堆的 UDF 函数或者你的操作系统对于某些操作需要更多的堆, 你也许需要将其设置的更高一点. 默认设置足以满足大多数应用

thread_cache_size = 20
# 在 cache 中保留多少线程用于重用. 当一个客户端断开连接后, 如果 cache 中的线程还少于 thread_cache_size, 则客户端线程被放入 cache 中. 这可以在你需要大量新连接的时候极大的减少线程创建的开销,服务器线程缓存这个值表示可以重新利用保存在缓存中线程的数量, 当断开连接时如果缓存中还有空间, 那么客户端的线程将被放到缓存中, 如果线程重新被请求，那么请求将从缓存中读取, 如果缓存中是空的或者是新的请求，那么这个线程将被重新创建, 如果有很多新的线程，增加这个值可以改善系统性能. 通过比较 Connections 和 Threads_created 状态的变量，可以看到这个变量的作用

thread_concurrency = 8
# 此允许应用程序给予线程系统一个提示在同一时间给予渴望被运行的线程的数量. 该参数取值为服务器逻辑 CPU 数量 ×2，在本例中，服务器有 2 颗物理 CPU，而每颗物理 CPU 又支持 H.T 超线程，所以实际取值为 4 × 2 ＝ 8. 设置 thread_concurrency 的值的正确与否,
# 对 mysql 的性能影响很大, 在多个 cpu(或多核)的情况下，错误设置了 thread_concurrency 的值, 会导致 mysql 不能充分利用多 cpu(或多核), 出现同一时刻只能一个 cpu(或核)在工作的情况。 thread_concurrency 应设为 CPU 核数的 2 倍. 比如有一个双核的 CPU,那么 thread_concurrency 的应该为 4; 2 个双核的 cpu,thread_concurrency 的值应为 8, 属重点优化参数
```

### qcache settings 相关选项

```bash
query_cache_limit = 2M
# 不缓存查询大于该值的结果. 只有小于此设定值的结果才会被缓冲,  此设置用来保护查询缓冲, 防止一个极大的结果集将其他所有的查询结果都覆盖.

query_cache_min_res_unit = 2K
# 查询缓存分配的最小块大小. 默认是 4KB，设置值大对大数据查询有好处，但如果你的查询都是小数据查询，就容易造成内存碎片和浪费
# 查询缓存碎片率 = Qcache_free_blocks / Qcache_total_blocks * 100%
# 如果查询缓存碎片率超过 20%，可以用 FLUSH QUERY CACHE 整理缓存碎片，或者试试减小 query_cache_min_res_unit，如果你的查询都是小数据量的话。
# 查询缓存利用率 = (query_cache_size – Qcache_free_memory) / query_cache_size *100%
# 查询缓存利用率在 25% 以下的话说明 query_cache_size 设置的过大，可适当减小; 查询缓存利用率在 80% 以上而且 Qcache_lowmem_prunes > 50 的话说明 query_cache_size 可能有点小，要不就是碎片太多。
# 查询缓存命中率 = (Qcache_hits – Qcache_inserts) / Qcache_hits * 100%

query_cache_size = 64M
# 指定 MySQL 查询缓冲区的大小。可以通过在 MySQL 控制台执行以下命令观察：
# 代码:
# > SHOW VARIABLES LIKE '%query_cache%';
# > SHOW STATUS LIKE 'Qcache%'; 如果 Qcache_lowmem_prunes 的值非常大，则表明经常出现缓冲不够的情况；
# 如果 Qcache_hits 的值非常大，则表明查询缓冲使用非常频繁，如果该值较小反而会影响效率，那么可以考虑不用查询缓冲； Qcache_free_blocks，如果该值非常大，则表明缓冲区中碎片很多。
# memlock # 如果你的系统支持 memlock() 函数, 你也许希望打开此选项用以让运行中的 mysql 在在内存高度紧张的时候, 数据在内存中保持锁定并且防止可能被 swapping out, 此选项对于性能有益
```

### default settings 相关选项

```bash
default_table_type = InnoDB
# 当创建新表时作为默认使用的表类型, 如果在创建表示没有特别执行表类型, 将会使用此值

default-time-zone = system
# 服务器时区

character-set-server = utf8
#server 级别字符集

default-storage-engine = InnoDB
# 默认存储引擎
```

### tmp && heap settings 相关选项

```bash
tmp_table_size = 512M
# 临时表的最大大小，如果超过该值，则结果放到磁盘中, 此限制是针对单个表的, 而不是总和.

max_heap_table_size = 512M
# 独立的内存表所允许的最大容量. 此选项为了防止意外创建一个超大的内存表导致永尽所有的内存资源.
```

### log settings 相关选项

```bash
log-bin = mysql-bin
# 打开二进制日志功能. 在复制 (replication) 配置中, 作为 MASTER 主服务器必须打开此项. 如果你需要从你最后的备份中做基于时间点的恢复, 你也同样需要二进制日志. 这些路径相对于 datadir

log_slave_updates = 1
# 表示 slave 将复制事件写进自己的二进制日志

log-bin-index = mysql-bin.index
# 二进制的索引文件名

relay-log = relay-log
# 定义 relay_log 的位置和名称，如果值为空，则默认位置在数据文件的目录，文件名为 host_name-relay-bin.nnnnnn（By default, relay log file names have the form host_name-relay-bin.nnnnnn in the data directory）；

relay_log_index = relay-log.index
#relay-log 的索引文件名

log-warnings = 1
# 将警告打印输出到错误 log 文件. 如果你对于 MySQL 有任何问题，你应该打开警告 log 并且仔细审查错误日志, 查出可能的原因.

log-error =  /usr/local/mysql/log/mysql.err
# 错误日志路径

log_output = FILE
# 参数 log_output 指定了慢查询输出的格式，默认为 FILE，你可以将它设为 TABLE，然后就可以查询 mysql 架构下的 slow_log 表了

log_slow_queries
# 指定是否开启慢查询日志(该参数要被 slow_query_log 取代，做兼容性保留)

slow_query_log = 1
# 指定是否开启慢查询日志. 慢查询是指消耗了比 “long_query_time” 定义的更多时间的查询. 如果 log_long_format 被打开, 那些没有使用索引的查询也会被记录. 如果你经常增加新查询到已有的系统内的话. 一般来说这是一个好主意,

long-query-time = 1
# 设定慢查询的阀值，超出次设定值的 SQL 即被记录到慢查询日志，缺省值为 10s. 所有的使用了比这个时间 (以秒为单位) 更多的查询会被认为是慢速查询. 不要在这里使用”1″, 否则会导致所有的查询, 甚至非常快的查询页被记录下来(由于 MySQL 目前时间的精确度只能达到秒的级别).

log_long_format
# 在慢速日志中记录更多的信息. 一般此项最好打开，打开此项会记录使得那些没有使用索引的查询也被作为到慢速查询附加到慢速日志里

slow_query_log_file =  /usr/local/mysql/log/slow.log
# 指定慢日志文件存放位置，可以为空，系统会给一个缺省的文件 host_name-slow.log

log-queries-not-using-indexes
# 如果运行的 SQL 语句没有使用索引，则 mysql 数据库同样会将这条 SQL 语句记录到慢查询日志文件中。

min_examined_row_limit=1000　　　　
# 记录那些由于查找了多余 1000 次而引发的慢查询

long-slow-admin-statements　　　　
# 记录那些慢的 optimize table，analyze table 和 alter table 语句

log-slow-slave-statements
# 记录由 Slave 所产生的慢查询

general_log = 1
# 将所有到达 MySQL Server 的 SQL 语句记录下来, 默认关闭

general_log_file =  /usr/local/mysql/log/mysql.log
#general_log 路径

max_binlog_size = 1G
# 如果二进制日志写入的内容超出给定值，日志就会发生滚动。你不能将该变量设置为大于 1GB 或小于 4096 字节。 默认值是 1GB。如果你正使用大的事务，二进制日志还会超过 max_binlog_size

max_relay_log_size = 1G
# 标记 relaylog 允许的最大值，如果该值为 0，则默认值为 max_binlog_size(1G)；如果不为 0，则 max_relay_log_size 则为最大的 relay_log 文件大小；

relay-log-purge = 1
# 是否自动清空不再需要中继日志时。默认值为 1(启用)

expire_logs_days = 30
# 超过 30 天的 binlog 删除

binlog_cache_size = 1M
# 在一个事务中 binlog 为了记录 SQL 状态所持有的 cache 大小, 如果你经常使用大的, 多声明的事务, 你可以增加此值来获取更大的性能. 所有从事务来的状态都将被缓冲在 binlog 缓冲中然后在提交后一次性写入到 binlog 中, 如果事务比此值大, 会使用磁盘上的临时文件来替代. 此缓冲在每个连接的事务第一次更新状态时被创建. session 级别

replicate-wild-ignore-table = mysql.%
# 复制时忽略数据库及表

slave_skip_errors=all
# 定义复制过程中从服务器可以自动跳过的错误号，当复制过程中遇到定义的错误号，就可以自动跳过，直接执行后面的 SQL 语句。
#slave_skip_errors 选项有四个可用值，分别为：off，all，ErorCode，ddl_exist_errors。
# 默认情况下该参数值是 off，我们可以列出具体的 error code，也可以选择 all，mysql5.6 及 MySQL Cluster NDB 7.3 以及后续版本增加了参数 ddl_exist_errors，该参数包含一系列 error code（1007,1008,1050,1051,1054,1060,1061,1068,1094,1146）
# 一些 error code 代表的错误如下：
# 1007：数据库已存在，创建数据库失败
# 1008：数据库不存在，删除数据库失败
# 1050：数据表已存在，创建数据表失败
# 1051：数据表不存在，删除数据表失败
# 1054：字段不存在，或程序文件跟数据库有冲突
# 1060：字段重复，导致无法插入
# 1061：重复键名
# 1068：定义了多个主键
# 1094：位置线程 ID
# 1146：数据表缺失，请恢复数据库
# 1053：复制过程中主服务器宕机
# 1062：主键冲突 Duplicate entry '%s' for key %d
```

### MyISAM 相关选项

```bash
key_buffer_size = 256M
# 指定用于索引的缓冲区大小，增加它可得到更好的索引处理性能。如果是以 InnoDB 引擎为主的 DB，专用于 MyISAM 引擎的 key_buffer_size 可以设置较小，8MB 已足够  如果是以 MyISAM 引擎为主，可设置较大，但不能超过 4G. 在这里，强烈建议不使用 MyISAM 引擎，默认都是用 InnoDB 引擎. 注意：该参数值设置的过大反而会是服务器整体效率降低！

sort_buffer_size = 2M
# 查询排序时所能使用的缓冲区大小。排序缓冲被用来处理类似 ORDER BY 以及 GROUP BY 队列所引起的排序. 一个用来替代的基于磁盘的合并分类会被使用. 查看 “Sort_merge_passes” 状态变量. 在排序发生时由每个线程分配 注意：该参数对应的分配内存是每连接独占！如果有 100 个连接，那么实际分配的总共排序缓冲区大小为 100 × 6 ＝600MB, 所以, 对于内存在 4GB 左右的服务器推荐设置为 6-8M。

read_buffer_size = 2M
# 读查询操作所能使用的缓冲区大小。和 sort_buffer_size 一样，该参数对应的分配内存也是每连接独享！用来做 MyISAM 表全表扫描的缓冲大小. 当全表扫描需要时, 在对应线程中分配.

join_buffer_size = 8M
# 联合查询操作所能使用的缓冲区大小，和 sort_buffer_size 一样，该参数对应的分配内存也是每连接独享! 此缓冲被使用来优化全联合 (full JOINs 不带索引的联合). 类似的联合在极大多数情况下有非常糟糕的性能表现, 但是将此值设大能够减轻性能影响. 通过 “Select_full_join” 状态变量查看全联合的数量， 当全联合发生时, 在每个线程中分配。

read_rnd_buffer_size = 8M
#MyISAM 以索引扫描 (Random Scan) 方式扫描数据的 buffer 大小

bulk_insert_buffer_size = 64M
#MyISAM 使用特殊的类似树的 cache 来使得突发插入(这些插入是, INSERT … SELECT, INSERT … VALUES (…), (…), …, 以及 LOAD DATAINFILE) 更快. 此变量限制每个进程中缓冲树的字节数. 设置为 0 会关闭此优化. 为了最优化不要将此值设置大于 “key_buffer_size”. 当突发插入被检测到时此缓冲将被分配 MyISAM 用在块插入优化中的树缓冲区的大小。注释：这是一个 per thread 的限制 （ bulk 大量）. 此缓冲当 MySQL 需要在 REPAIR, OPTIMIZE, ALTER 以及 LOAD DATA INFILE 到一个空表中引起重建索引时被分配. 这在每个线程中被分配. 所以在设置大值时需要小心.

myisam_sort_buffer_size = 64M
#MyISAM 设置恢复表之时使用的缓冲区的尺寸, 当在 REPAIR TABLE 或用 CREATE INDEX 创建索引或 ALTER TABLE 过程中排序 MyISAM 索引分配的缓冲区

myisam_max_sort_file_size = 10G
#mysql 重建索引时允许使用的临时文件最大大小

myisam_repair_threads = 1
# 如果该值大于 1，在 Repair by sorting 过程中并行创建 MyISAM 表索引(每个索引在自己的线程内). 如果一个表拥有超过一个索引, MyISAM 可以通过并行排序使用超过一个线程去修复他们. 这对于拥有多个 CPU 以及大量内存情况的用户, 是一个很好的选择.

myisam_recover = 64K
# 允许的 GROUP_CONCAT()函数结果的最大长度

transaction_isolation = REPEATABLE-READ
# 设定默认的事务隔离级别. 可用的级别如下: READ-UNCOMMITTED, READ-COMMITTED, REPEATABLE-READ,SERIALIZABLE
# 1.READ UNCOMMITTED - 读未提交 2.READ COMMITTE - 读已提交 3.REPEATABLE READ - 可重复读 4.SERIALIZABLE - 串行
```

### INNODB 相关选项

```bash
skip-innodb
# 如果你的 MySQL 服务包含 InnoDB 支持但是并不打算使用的话, 使用此选项会节省内存以及磁盘空间, 并且加速某些部分

innodb_file_per_table = 1
# InnoDB 为独立表空间模式，每个数据库的每个表都会生成一个数据空间
# 独立表空间优点：
# 1．每个表都有自已独立的表空间。
# 2．每个表的数据和索引都会存在自已的表空间中。
# 3．可以实现单表在不同的数据库中移动。
# 4．空间可以回收（除 drop table 操作处，表空不能自已回收）
# 缺点：
# 1. 单表增加过大，如超过 100G
# 结论：
# 共享表空间在 Insert 操作上少有优势。其它都没独立表空间表现好。当启用独立表空间时，请合理调整：innodb_open_files

innodb_status_file = 1
# 启用 InnoDB 的 status file，便于管理员查看以及监控等

innodb_open_files = 2048
# 限制 Innodb 能打开的表的数据，如果库里的表特别多的情况，请增加这个。这个值默认是 300

innodb_additional_mem_pool_size = 100M
# 设置 InnoDB 存储引擎用来存放数据字典信息以及一些内部数据结构的内存空间大小，所以当我们一个 MySQL Instance 中的数据库对象非常多的时候，是需要适当调整该参数的大小以确保所有数据都能存放在内存中提高访问效率的。

innodb_buffer_pool_size = 2G
# 包括数据页、索引页、插入缓存、锁信息、自适应哈希所以、数据字典信息. InnoDB 使用一个缓冲池来保存索引和原始数据, 不像 MyISAM. 这里你设置越大, 你在存取表里面数据时所需要的磁盘 I/O 越少. 在一个独立使用的数据库服务器上, 你可以设置这个变量到服务器物理内存大小的 80%, 不要设置过大, 否则, 由于物理内存的竞争可能导致操作系统的换页颠簸. 注意在 32 位系统上你每个进程可能被限制在 2-3.5G 用户层面内存限制, 所以不要设置的太高.

innodb_write_io_threads = 4
innodb_read_io_threads = 4
# innodb 使用后台线程处理数据页上的读写 I/O(输入输出)请求, 根据你的 CPU 核数来更改, 默认是 4
# 注: 这两个参数不支持动态改变, 需要把该参数加入到 my.cnf 里，修改完后重启 MySQL 服务, 允许值的范围从 1-64

innodb_data_home_dir =  /usr/local/mysql/var/
# 设置此选项如果你希望 InnoDB 表空间文件被保存在其他分区. 默认保存在 MySQL 的 datadir 中.

innodb_data_file_path = ibdata1:500M;ibdata2:2210M:autoextend
#InnoDB 将数据保存在一个或者多个数据文件中成为表空间. 如果你只有单个逻辑驱动保存你的数据, 一个单个的自增文件就足够好了. 其他情况下. 每个设备一个文件一般都是个好的选择. 你也可以配置 InnoDB 来使用裸盘分区 – 请参考手册来获取更多相关内容

innodb_file_io_threads = 4
# 用来同步 IO 操作的 IO 线程的数量. 此值在 Unix 下被硬编码为 4, 但是在 Windows 磁盘 I/O 可能在一个大数值下表现的更好.

innodb_thread_concurrency = 16
# 在 InnoDb 核心内的允许线程数量, InnoDB 试着在 InnoDB 内保持操作系统线程的数量少于或等于这个参数给出的限制, 最优值依赖于应用程序, 硬件以及操作系统的调度方式. 过高的值可能导致线程的互斥颠簸. 默认设置为 0, 表示不限制并发数，这里推荐设置为 0，更好去发挥 CPU 多核处理能力，提高并发量

innodb_flush_log_at_trx_commit = 1
# 如果设置为 1 ,InnoDB 会在每次提交后刷新 (fsync) 事务日志到磁盘上, 这提供了完整的 ACID 行为. 如果你愿意对事务安全折衷, 并且你正在运行一个小的食物, 你可以设置此值到 0 或者 2 来减少由事务日志引起的磁盘 I/O
# 0 代表日志只大约每秒写入日志文件并且日志文件刷新到磁盘.
# 2 代表日志写入日志文件在每次提交后, 但是日志文件只有大约每秒才会刷新到磁盘上.

innodb_log_buffer_size = 8M
# 用来缓冲日志数据的缓冲区的大小. 当此值快满时, InnoDB 将必须刷新数据到磁盘上. 由于基本上每秒都会刷新一次, 所以没有必要将此值设置的太大(甚至对于长事务而言)

innodb_log_file_size = 500M
# 事物日志大小. 在日志组中每个日志文件的大小，你应该设置日志文件总合大小到你缓冲池大小的 5%~100%，来避免在日志文件覆写上不必要的缓冲池刷新行为. 不论如何, 请注意一个大的日志文件大小会增加恢复进程所需要的时间.

innodb_log_files_in_group = 2
# 在日志组中的文件总数. 通常来说 2~3 是比较好的.

innodb_log_group_home_dir =  /usr/local/mysql/var/
# InnoDB 的日志文件所在位置. 默认是 MySQL 的 datadir. 你可以将其指定到一个独立的硬盘上或者一个 RAID1 卷上来提高其性能 innodb_max_dirty_pages_pct = 90 #innodb 主线程刷新缓存池中的数据，使脏数据比例小于 90%, 这是一个软限制, 不被保证绝对执行.

innodb_lock_wait_timeout = 50
#InnoDB 事务在被回滚之前可以等待一个锁定的超时秒数。InnoDB 在它自己的 锁定表中自动检测事务死锁并且回滚事务。 InnoDB 用 LOCK TABLES 语句注意到锁定设置。默认值是 50 秒

innodb_flush_method = O_DSYNC
# InnoDB 用来刷新日志的方法. 表空间总是使用双重写入刷新方法. 默认值是 “fdatasync”, 另一个是 “O_DSYNC”.

innodb_force_recovery=1
# 如果你发现 InnoDB 表空间损坏, 设置此值为一个非零值可能帮助你导出你的表. 从 1 开始并且增加此值知道你能够成功的导出表.

innodb_fast_shutdown
# 加速 InnoDB 的关闭. 这会阻止 InnoDB 在关闭时做全清除以及插入缓冲合并. 这可能极大增加关机时间, 但是取而代之的是 InnoDB 可能在下次启动时做这些操作.
```

### 其他 相关选项

```bash
[mysqldump]
quick
# 支持较大数据库的转储，在导出非常巨大的表时需要此项。增加该变量的值十分安全，这是因为仅当需要时才会分配额外内存。例如，仅当你发出长查询或 mysqld 必须返回大的结果行时 mysqld 才会分配更多内存。该变量之所以取较小默认值是一种预防措施，以捕获客户端和服务器之间的错误信息包，并确保不会因偶然使用大的信息包而导致内存溢出。 如果你正是用大的 BLOB 值，而且未为 mysqld 授予为处理查询而访问足够内存的权限，也会遇到与大信息包有关的奇怪问题。如果怀疑出现了该情况，请尝试在 mysqld_safe 脚本开始增加 ulimit -d 256000，并重启 mysqld。

[mysql]
auto-rehash
# 允许通过 TAB 键提示

default-character-set = utf8
# 数据库字符集

connect-timeout = 3
[mysqld_safe]

open-files-limit = 8192
# 增加每个进程的可打开文件数量. 确认你已经将全系统限制设定的足够高! 打开大量表需要将此值设大
```

---

## Source & Reference

- https://blog.csdn.net/bbwangj/article/details/83752142
