# Postgresql

---

**简介**

PostgreSQL是一种先进的对象-关系数据库管理系统（ORDBMS），它不仅支持关系数据库的各种功能，而且还具备类、继承等对象数据库的特征。

**cli连接**
```bash
psql postgres://账户:密码@地址:5432/数据库名称

# 例如
psql postgres://postgres:Abcd1234@127.0.0.1:5432/test
```

**cli下**
```bash
# 查看已经存在的数据库
\l

# 进入数据库
\c + 数据库名

# 查看表格
\d
```

**报错 : FATAL: no pg_hba.conf entry for host *** user “postgres“, database “postgres“, SSL**

修改 pg_hba.conf
```
host    all             all              0.0.0.0/0              md5
```

**配置监听**

配置 postgresql.conf
```
listen_addresses = '*'
```

## 账户

**更改密码**
```sql
-- 更改 postgres 密码为 Abcd1234
ALTER USER postgres WITH PASSWORD 'Abcd1234';
```

## 导入导出

**导出单表数据**
```
pg_dump -h 127.0.0.1 -U admin -p 5432 -W db -t t1 -inserts > bak.sql
```

**导出多个表数据**
```
pg_dump -h 127.0.0.1 -U admin -p 5432 -W db -t t1 -t t2 -inserts > bak.sql
```

**导出整个数据库**
```
pg_dump -h 127.0.0.1 -U admin -p 5432 -W db -inserts > bak.sql
```

**只导出表结构，不导出数据**
```
pg_dump -h 127.0.0.1 -U admin -p 5432 -W db -s > bak.sql
```

**只导出数据，不导出表结构**
```
pg_dump -h 127.0.0.1 -U admin -p 5432 -W db -inserts -a > bak.sql
```

**postgresql 导入数据源**
```
pg_restore -h 127.0.0.1 -p 5432 -U postgres -W -d test -v "test.dump"
```

---

## Source & Reference

- [PostgreSQL 数据库导入导出](https://blog.51cto.com/niuben/4877093)
- https://qa.1r1g.com/sf/ask/890467721/
- https://blog.csdn.net/qq_50119033/article/details/120922628
