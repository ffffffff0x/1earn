
```sql
select group_concat(table_name) from information_schema.tables where table_schema=database()
```

查看 xxx 的字段
```sql
select group_concat(column_name) from information_schema.columns where table_name='xxx'
```

读取字段的内容
```sql
select flag from fl4g
```
