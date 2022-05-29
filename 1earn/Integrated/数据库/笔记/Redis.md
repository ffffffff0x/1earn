# Redis

---

## 什么是 Redis

Redis 是一个 key-value 存储系统。和 Memcached 类似，它支持存储的 value 类型相对更多，包括 string(字符串)、list(链表)、set(集合)、zset(sorted set -- 有序集合) 和 hash（哈希类型）。这些数据类型都支持 push/pop、add/remove 及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在此基础上，redis 支持各种不同方式的排序。与 memcached 一样，为了保证效率，数据都是缓存在内存中。区别的是 redis 会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了 master-slave(主从) 同步。

Redis 的出现，很大程度补偿了 memcached 这类 key/value 存储的不足，在部分场合可以对关系数据库起到很好的补充作用。

Redis 与其他 key - value 缓存产品有以下三个特点：
- Redis 支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。
- Redis 不仅仅支持简单的 key-value 类型的数据，同时还提供 list，set，zset，hash 等数据结构的存储。
- Redis 支持数据的备份，即 master-slave 模式的数据备份。

---

## 安装

**使用包管理器或者编译安装**

- [Redis安装](../../Linux/Power-Linux.md#redis)

**通过 docker 搭建环境**

```bash
wget -O f8x-dev https://f8x.io/dev
bash f8x-dev -redis
```

---

## Redis 配置

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf 。可以通过 CONFIG 命令查看或设置配置项

```
port 6379                   //指定 Redis 监听端口，默认端口为 6379
bind 127.0.0.1              //绑定的主机地址
timeout 300                 //当客户端闲置多长秒后关闭连接，如果指定为 0 ，表示关闭该功能
databases 16                //设置数据库的数量，默认数据库为0，可以使用 SELECT 命令在连接上指定数据库id
save <seconds> <changes>    //指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合
dbfilename dump.rdb         //指定本地数据库文件名，默认值为 dump.rdb
dir ./                      //指定本地数据库存放目录
```

Redis CONFIG 查看配置命令格式如下:
```
CONFIG GET CONFIG_SETTING_NAME
```

使用 `*` 号获取所有配置项
```
CONFIG GET *
```

**编辑配置**

可以通过修改 redis.conf 文件或使用 `CONFIG set` 命令来修改配置

```
CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE
```

---

## 基本语法

### 运行

```bash
redis-server /etc/redis.conf
```

一般情况下外面的主机是连接不了 redis 的，因为 redis 遵循 bind 指令，这将强制 Redis 只监听 IPV4 环回接口 (意味着 Redis 将能够只接收来自同一台计算机的连接运行)

可以修改 redis 配置文件 /etc/redis.conf 中添加本地地址来解决，修改完之后重新启动 redis 服务，可以发现可以连接了
```
bind 127.0.0.1 192.168.1.1
```

**常见报错**

`Redis Can't handle RDB format version 9`
- 在整个文件系统中搜索 dump.rdb：

    ```
    find / -name *.rdb
    ```

    删除 dump.rdb 文件

### 连接

```
redis-cli -h 127.0.0.1
redis-cli -h 127.0.0.1 -p 6379 -a password

ping
```

### SET 命令

Redis SET 命令用于设置给定 key 的值。如果 key 已经存储其他值， SET 就覆写旧值，且无视类型。

```
redis 127.0.0.1:6379> SET KEY_NAME VALUE
```

### GET 命令

Redis Get 命令用于获取指定 key 的值。如果 key 不存在，返回 nil

```
redis 127.0.0.1:6379> GET KEY_NAME
```

### Flushall 命令

Redis Flushall 命令用于清空整个 Redis 服务器的数据(删除所有数据库的所有 key )。
```
redis 127.0.0.1:6379> FLUSHALL
```

### Redis 数据备份与恢复

SAVE 命令用于创建当前数据库的备份，将执行一个同步保存操作，将当前 Redis 实例的所有数据快照(snapshot)以默认 RDB 文件的形式保存到硬盘  (此命令将在 redis 安装目录下创建一个 dump.rdb文件)
```
redis 127.0.0.1:6379> SAVE
```

恢复数据，只需要将备份文件(dump.rdb) 移动到 redis 安装目录并启动服务即可。获取 redis 目录可用 CONFIG 命令
```
CONFIG GET dir
```

### Redis 安全配置

配置文件中的参数 `requirepass` 是配置 redis 访问密码的参数,可以通过以下命令查看是否进行了密码设置
```
CONFIG get requirepass
```

默认情况下 requirepass 参数为空，这就意味着可以无需通过密码验证就可以连接到 redis 服务

然后可以通过以下命令来修改参数，设置密码之后，客户端连接 redis 服务就需要密码验证，否则无法执行命令 (但是命令行修改了密码之后，配置文件的 requirepass 字段后面的密码是不会随之修改的)
```
CONFIG set requirepass "123123"
CONFIG get requirepass
```

AUTH 命令可用于检测给定的密码是否与配置文件中的密码相符 (密码匹配正确时返回OK，否则返回一个错误)
```
AUTH PASSWORD
```
