# Speed-SQL

---

**数据库分类**

数据库通常分为:层次式数据库、网络式数据库、关系式数据库三种。

而不同的数据库是按不同的数据结构来联系和组织的。而在当今的互联网中，最常见的数据库模型主要是两种，即关系型数据库和非关系型数据库。

**关系型数据库**

当前在成熟应用且服务与各种系统的主力数据库还是关系型数据库。

![image](../../../assets/img/运维/数据库/Speed-SQL/1.png)

代表：Oracle、SQL Server、MySQL

**非关系型数据库**

随着时代的进步与发展的需要，非关系型数据库应运而生。

代表：Redis、Mongodb

NoSQL 数据库在存储速度与灵活性方面有优势，也常用于缓存。

---

# MySQL

**概要**

MySQL 是一个关系型数据库管理系统，由瑞典 MySQL AB 公司开发，目前属于 Oracle 旗下产品。MySQL 是一种关系数据库管理系统，关系数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内。MySQL 软件采用了双授权政策，分为社区版和商业版。

**存储引擎**

MySQL 数据库根据应用的需要准备了不同的引擎，不同的引擎侧重点不一样，区别如下：

- MyISAM MySQL 5.0 之前的默认数据库引擎，最为常用。拥有较高的插入，查询速度，但不支持事务
- InnoDB 事务型数据库的首选引擎，支持 ACID 事务，支持行级锁定, MySQL 5.5 起成为默认数据库引擎
- BDB 事务型数据库的另一种选择，支持 Commit 和 Rollback 等其他事务特性
- Memory 所有数据置于内存的存储引擎，拥有极高的插入，更新和查询效率。但是会占用和数据量成正比的内存空间。并且其内容会在 MySQL 重新启动时丢失
- Merge 将一定数量的 MyISAM 表联合而成一个整体，在超大规模数据存储时很有用
- Archive 非常适合存储大量的独立的，作为历史记录的数据。因为它们不经常被读取。Archive 拥有高效的插入速度，但其对查询的支持相对较差
- Federated 将不同的 MySQL 服务器联合起来，逻辑上组成一个完整的数据库。非常适合分布式应用
- Cluster/NDB 高冗余的存储引擎，用多台数据机器联合提供服务以提高整体性能和安全性。适合数据量大，安全和性能要求高的应用
- CSV 逻辑上由逗号分割数据的存储引擎。它会在数据库子目录里为每个数据表创建一个 .csv 文件。这是一种普通文本文件，每个数据行占用一个文本行。CSV 存储引擎不支持索引。
- BlackHole 黑洞引擎，写入的任何数据都会消失，一般用于记录 binlog 做复制的中继
- EXAMPLE 存储引擎是一个不做任何事情的存根引擎。它的目的是作为 MySQL 源代码中的一个例子，用来演示如何开始编写一个新存储引擎。同样，它的主要兴趣是对开发者。EXAMPLE 存储引擎不支持编索引。

另外，MySQL 的存储引擎接口定义良好。有兴趣的开发者可以通过阅读文档编写自己的存储引擎。

**列的类型**

数字类型
- 整数: tinyint、smallint、mediumint、int、bigint
- 浮点数: float、double、real、decimal
- 日期和时间: date、time、datetime、timestamp、year

字符串类型
- 字符串: char、varchar
- 文本: tinytext、text、mediumtext、longtext

二进制(可用来存储图片、音乐等)
- tinyblob、blob、mediumblob、longblob

---

# 常用 SQL 语句

**SQL 查询重复出现次数最多的记录,按出现频率排序**
```sql
SELECT keyword, count( * ) AS count
FROM article_keyword
GROUP BY keyword
ORDER BY count DESC
LIMIT 20
```

**查询不重复的记录**
```sql
select distinct * from tableName
```

**查询不重复的记录转入其他表**

- 新表
    ```sql
    create table tab2 as select distinct * from tab1
    ```

- 存在的表
    ```sql
    insert into tab2 select distinct * from tab1
    ```

**查询A表有但B表没有**
```sql
select a.name,b.name
from tab1 a left join tab2 b
on a.name = b.name
where b.name is null
```

---

**Source & Reference**
- [MySQL数据库](https://www.cnblogs.com/tester-l/p/8191750.html)
