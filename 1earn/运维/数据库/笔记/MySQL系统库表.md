### MySQL 系统库表

---

**information_schema**

MySQL自带的系统数据库，当中大部分是我们需要了结的信息，比如字符集，权限相关，数据库实体对象信息，外检约束，分区，压缩表，表信息，索引信息，参数，优化，锁和事物等等。所以可以利用这个数据库来进行注入。

```sql
--存储mysql数据库下面的所有表名信息的表
information_schema.tables
    --数据库名 : table_schema
    --表名 : Table_name

-- 存储mysql数据库下面的所有列名信息的表
information_schema.columns
    -- 表名 : table_name
```




