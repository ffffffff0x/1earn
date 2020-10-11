# MySQL 函数

---

# 常见系统函数

- version() -- MySQL版本
- user() -- 数据库用户名
- database() -- 数据库名
- @@datadir -- 数据库路径
- @@basedir -- 安装路径
- @@version_compile_os -- 操作系统版本

---

# 常见连接函数

在 select 数据时，我们往往需要将数据进行连接后进行回显。很多的时候想将多个数据或者多行数据进行输出的时候，需要使用字符串连接函数。

**concat(str1,str2,...)**

没有分隔符地连接字符串

**concat_ws(separator,str1,str2,...)**

含有分隔符地连接字符串

**group_concat(str1,str2,...)**

连接一个组的所有字符串，并以逗号分隔每一条数据

https://www.cnblogs.com/lcamry/p/5715634.html

---

# 截取字符串常用函数

**mid()**

此函数为截取字符串一部分。

```sql
MID(column_name,start[,length])
-- column_name  : 必需。要提取字符的字段。
-- start        : 必需。规定开始位置（起始值是 1）。
-- length       : 可选。要返回的字符数。如果省略，则 MID() 函数返回剩余文本。
```

例如 : str="123456" mid(str,2,1) 结果为2

**substr()**

Substr() 和 substring() 函数实现的功能是一样的，均为截取字符串。

```sql
string substring(string, start, length)
string substr(string, start, length)
-- 参数描述同 mid() 函数，第一个参数为要处理的字符串，start 为开始位置，length 为截取的长度。
```

**Left()**

得到字符串左部指定个数的字符

```sql
Left ( string, n )
-- string 为要截取的字符串，n 为长度。
```

**ord()**

返回第一个字符的 ASCII 码

例如 : ORD(MID(DATABASE(),1,1))>114 意为检测 database() 的第一位 ASCII 码是否大于 114，也就是 'r'

---

# 导入导出函数

**load_file()**

读取文件并返回该文件的内容作为一个字符串。

例如 : select 1,1,1,load_file(char(99,58,47,98,111,111,116,46,105,110,105))

---

**Source & Reference**
- [Sql注入截取字符串常用函数](https://www.cnblogs.com/lcamry/p/5504374.html)
