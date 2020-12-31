# Power-SQL

---

# 库

## 创建数据库

我们可以在登陆 MySQL 服务后，使用 creat 命令创建数据库，语法如下:
```sql
create database 数据库名称 [库选项];
```
其中，库选项是用来约束数据库的，为可选项（有默认值），共有两种，分别为：
- 字符集设定：charset/ character set+ 具体字符集，用来表示数据存储的编码格式，常用的字符集包括 GBK 和 UTF8 等。
- 校对集设定：collate+ 具体校对集，表示数据比较的规则，其依赖字符集。

示例：
```sql
create database TBL_ERROR_CODE charset utf8;
```

其中，数据库的名字不能用关键字（已经被占用的字符，例如 `update` 和 `insert` 等）或者保留字（将来可能会用的，例如 `access` 和 `cast` 等）。
如果非要使用数据库的关键字或者保留字作为数据库名称，那么必须用反引号将其括起来，例如：
```sql
create database `update` charset utf8;
```

如果还想使用中文作为数据库的名称，那就得保证数据库能够识别中文（强烈建议不要用中文命名数据库的名称），例如：
```sql
-- 设置中文名称的方法，其中 gbk 为当前数据库的默认字符集
set names gbk;
create database 北京 charset gbk;
```

## 删除数据库

使用普通用户登陆 MySQL 服务器，你可能需要特定的权限来创建或者删除 MySQL 数据库，所以我们这边使用 root 用户登录，root 用户拥有最高权限。

在删除数据库过程中，务必要十分谨慎，因为在执行删除命令后，所有数据将会消失。
```
drop database <数据库名>;
​```

例如删除名为 test 的数据库：
```sql
drop database test;
```

## 查询数据库

查看全部
```sql
show databases;
```

查看部分（模糊查询）
```sql
show databases like 'pattern';
```

其中，pattern 是匹配模式，有两种，分别为：
- %：表示匹配多个字符；
- _：表示匹配单个字符。

此外，在匹配含有下划线 _ 的数据库名称的时候，需要在下划线前面加上反斜线 \_ 进行转义操作。
```sql
show databases like 'TBL%';
```
表示匹配所有 TBL 开头的数据库。

查看数据库的创建语句
```sql
show create database 数据库名称;
```
在这里，查看的结果有可能与咱们书写的 SQL 语句不同，这是因为数据库在执行 SQL 语句之前会优化 SQL，系统保存的是优化后的结果。

## 选择数据库

在你连接到 MySQL 数据库后，可能有多个可以操作的数据库，所以你需要选择你要操作的数据库。
```
use test;
```

执行以上命令后，你就已经成功选择了 test 数据库，在后续的操作中都会在 test 数据库中执行。

注意:所有的数据库名，表名，表字段都是区分大小写的。所以你在使用 SQL 命令时需要输入正确的名称。

## 更新数据库

在这里，需要注意：数据库的名字不可以修改。

```sql
alter database 数据库名称 [库选项];
```

示例：
```
alter database TBL_ERROR_CODE charset gbk;
```

表示修改此数据库的字符集为 gbk.

---

# 表

## 创建表

创建 MySQL 数据表需要以下信息：
- 表名
- 表字段名
- 定义每个表字段

以下为创建 MySQL 数据表的 SQL 通用语法：
```sql
create table [if not exists] + 表名(
    字段名称 数据类型,
    ……
    字段名称 数据类型   /* 最后后一行，不需要加逗号 */
)[表选项];
```
其中，`if not exists` 表示如果表名不存在，就执行创建代码；如果表名存在，则不执行创建代码。

表选项则是用来控制表的表现形式的，共有三种，分别为：
- 字符集设定：charset/ character set+ 具体字符集，用来表示数据存储的编码格式，常用的字符集包括 GBK 和 UTF8 等。
- 校对集设定：collate+ 具体校对集，表示数据比较的规则，其依赖字符集。
- 存储引擎：engine+ 具体存储引擎，默认为 InnoDB，常用的还有 MyISAM.

以下例子中我们将在已经指定的数据库中创建数据表 test_tbl：
```sql
CREATE TABLE IF NOT EXISTS `test_tbl`(
   `test_id` INT UNSIGNED AUTO_INCREMENT,
   `test_title` VARCHAR(100) NOT NULL,
   `test_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `test_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
- 如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为 NULL ，就会报错。
- AUTO_INCREMENT 定义列为自增的属性，一般用于主键，数值会自动加1。
- PRIMARY KEY关键字用于定义列为主键。 你可以使用多列来定义主键，列间以逗号分隔。
- ENGINE 设置存储引擎，CHARSET 设置编码。

由于任何表都归属于某个数据库，因此在创建表的时候，都必须先指定具体的数据库。在这里，指定数据库的方式有两种，分别为：
第 1 种：显式的指定表所属的数据库，示例
```sql
create table if not exists test.student(
    name varchar(10),
    age int,            /* 整型不需要指定具体的长度 */
    grade varchar(10)   /* 最后后一行，不需要加逗号 */
)charset utf8;
```

第 2 种：隐式的指定表所属的数据库，示例
```sql
use test;               /* use + 数据库名称，表示切换到指定的数据库，这句命令其实不加分号也可以，但不建议这么做 */
create table if not exists student(
    name varchar(10),
    age int,            /* 整型不需要指定具体的长度 */
    grade varchar(10)   /* 最后后一行，不需要加逗号 */
)charset utf8;
```

创建 MySql 的表时，表名和字段名外面的符号 ` 不是单引号，而是英文输入法状态下的反单引号，也就是键盘左上角 esc 按键下面的那一个 ~ 按键，坑惨了。

反引号是为了区分 MySql 关键字与普通字符而引入的符号，一般的，表名与字段名都使用反引号。

## 删除表

MySQL 中删除数据表是非常容易操作的， 但是你再进行删除表操作时要非常小心，因为执行删除命令后所有数据都会消失。

**删除表的几种情况**
- drop table table_name : 删除表全部数据和表结构，立刻释放磁盘空间，不管是 Innodb 和 MyISAM;

    实例，删除学生表：
    ```sql
    drop table student;
    ```

- truncate table table_name : 删除表全部数据，保留表结构，立刻释放磁盘空间 ，不管是 Innodb 和 MyISAM;

    实例，删除学生表：
    ```sql
    truncate table student;
    ```

- delete from table_name : 删除表全部数据，表结构不变，对于 MyISAM 会立刻释放磁盘空间，InnoDB 不会释放磁盘空间;

    实例，删除学生表：
    ```sql
    delete from student;
    ```

- delete from table_name where xxx : 带条件的删除，表结构不变，不管是 innodb 还是 MyISAM 都不会释放磁盘空间;

    实例，删除学生表中姓名为 "张三" 的数据：
    ```sql
    delete from student where T_name = "张三";
    ```

- delete 操作以后，使用 optimize table table_name 会立刻释放磁盘空间，不管是 innodb 还是 myisam;

    实例，删除学生表中姓名为 "张三" 的数据：
    ```sql
    delete from student where T_name = "张三";
    ```
    实例，释放学生表的表空间：
    ```sql
    optimize table student;
    ```
    delete from 表以后虽然未释放磁盘空间，但是下次插入数据的时候，仍然可以使用这部分空间。

总结
- 当你不再需要该表时， 用 drop;
- 当你仍要保留该表，但要删除所有记录时， 用 truncate;
- 当你要删除部分记录时， 用 delete。

## 查询表

查看全部
```sql
show tables;
```

查看部分（模糊查询）
```sql
show tables like 'pattern';
```
其中，pattern 是匹配模式，有两种，分别为：
- %：表示匹配多个字符；
- _：表示匹配单个字符。

此外，在匹配含有下划线 _ 的表名的时候，需要在下划线前面加上反斜线 `\_` 进行转义操作。
```sql
show tables like '%t';
```
表示匹配所有以 t 结尾的表。

查看表的创建语句
```sql
show create table 表名;
```
在这里，咱们也可以用 `\g` 和 `\G` 代替上述语句中的;分号，其中 `\g` 等价于分号，`\G` 则在等价于分号的同时，将查的表结构旋转 90 度，变成纵向结构。

查看表中的字段信息
```sql
show columns from 表名;
```

## 更新表

修改表名
```sql
rename table 旧表名 to 新表名;
```

修改表选项
```sql
alter table 表名 表选项[=] 值;
```

新增字段
```sql
alter table 表名 add [column] 字段名 数据类型 [列属性][位置];
```
其中，位置表示此字段存储的位置，分为 first（第一个位置）和 after + 字段名（指定的字段后，默认为最后一个位置）.
```sql
alter table student
add column id int first;
```

修改字段
```sql
alter table 表名 modify 字段名 数据类型 [列属性][位置];
```
其中，位置表示此字段存储的位置，分为 first（第一个位置）和 after + 字段名（指定的字段后，默认为最后一个位置）.
```sql
alter table student
modify name char(10) after id;
```

重命名字段
```sql
alter table 表名 change 旧字段名 新字段名 数据类型 [列属性][位置];
```
其中，位置表示此字段存储的位置，分为 first（第一个位置）和 after + 字段名（指定的字段后，默认为最后一个位置）.
```sql
alter table student
change grade class varchar(10);
```

删除字段
```sql
alter table 表名 drop 字段名;
alter table student
drop age;
```
注意：如果表中已经存在数据，那么删除该字段会清空该字段的所有数据，而且不可逆，慎用。

## 复制表

如果我们需要完全的复制 MySQL 的数据表，包括表的结构，索引，默认值等。 如果仅仅使用 CREATE TABLE ... SELECT 命令，是无法实现的。
```sql
CREATE TABLE targetTable LIKE sourceTable;
INSERT INTO targetTable SELECT * FROM sourceTable;
​
可以拷贝一个表中其中的一些字段:
CREATE TABLE newadmin AS
(
    SELECT username, password FROM admin
)
​
可以将新建的表的字段改名:
CREATE TABLE newadmin AS
(  
    SELECT id, username AS uname, password AS pass FROM admin
)
​
可以拷贝一部分数据:
CREATE TABLE newadmin AS
(
    SELECT * FROM admin WHERE LEFT(username,1) = 's'
)
​
可以在创建表的同时定义表中的字段信息:
CREATE TABLE newadmin
(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY
)
AS
(
    SELECT * FROM admin
)  
```
或
```sql
create table 新表 select * from 旧表
```

**整体方法**

步骤一: 获取数据表的完整结构。

```sql
mysql> SHOW CREATE TABLE test_tbl \G;
*************************** 1. row ***************************
       Table: test_tbl
Create Table: CREATE TABLE `test_tbl` (
  `test_id` int(11) NOT NULL auto_increment,
  `test_title` varchar(100) NOT NULL default '',
  `test_author` varchar(40) NOT NULL default '',
  `submission_date` date default NULL,
  PRIMARY KEY  (`test_id`),
  UNIQUE KEY `AUTHOR_INDEX` (`test_author`)
) ENGINE=InnoDB
1 row in set (0.00 sec)
```

步骤二

修改 SQL 语句的数据表名，并执行 SQL 语句。

```sql
mysql> CREATE TABLE `clone_tbl` (
  -> `test_id` int(11) NOT NULL auto_increment,
  -> `test_title` varchar(100) NOT NULL default '',
  -> `test_author` varchar(40) NOT NULL default '',
  -> `submission_date` date default NULL,
  -> PRIMARY KEY  (`test_id`),
  -> UNIQUE KEY `AUTHOR_INDEX` (`test_author`)
-> ) ENGINE=InnoDB;
Query OK, 0 rows affected (1.80 sec)
```

步骤三

执行完第二步骤后，你将在数据库中创建新的克隆表 clone_tbl。 如果你想拷贝数据表的数据你可以使用 INSERT INTO... SELECT 语句来实现。

```sql
mysql> INSERT INTO clone_tbl (test_id,
    ->                        test_title,
    ->                        test_author,
    ->                        submission_date)
    -> SELECT test_id,test_title,
    ->        test_author,submission_date
    -> FROM test_tbl;
Query OK, 3 rows affected (0.07 sec)
Records: 3  Duplicates: 0  Warnings: 0
```

## 临时表

MySQL 临时表在我们需要保存一些临时数据时是非常有用的。临时表只在当前连接可见，当关闭连接时，Mysql 会自动删除表并释放所有空间。

MySQL 临时表只在当前连接可见，如果你使用 PHP 脚本来创建 MySQL 临时表，那每当 PHP 脚本执行完成后，该临时表也会自动销毁。如果你使用了其他 MySQL 客户端程序连接 MySQL 数据库服务器来创建临时表，那么只有在关闭客户端程序时才会销毁临时表，当然你也可以手动销毁。

实例
```sql
-- 以下展示了使用 MySQL 临时表的简单实例，以下的 SQL 代码可以适用于 PHP 脚本的 mysql_query() 函数。

mysql> CREATE TEMPORARY TABLE SalesSummary (
    -> product_name VARCHAR(50) NOT NULL
    -> , total_sales DECIMAL(12,2) NOT NULL DEFAULT 0.00
    -> , avg_unit_price DECIMAL(7,2) NOT NULL DEFAULT 0.00
    -> , total_units_sold INT UNSIGNED NOT NULL DEFAULT 0
);
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO SalesSummary
    -> (product_name, total_sales, avg_unit_price, total_units_sold)
    -> VALUES
    -> ('cucumber', 100.25, 90, 2);

mysql> SELECT * FROM SalesSummary;
+--------------+-------------+----------------+------------------+
| product_name | total_sales | avg_unit_price | total_units_sold |
+--------------+-------------+----------------+------------------+
| cucumber     |      100.25 |          90.00 |                2 |
+--------------+-------------+----------------+------------------+
1 row in set (0.00 sec)
```

## 索引

MySQL 索引的建立对于 MySQL 的高效运行是很重要的，索引可以大大提高 MySQL 的检索速度。

打个比方，如果合理的设计且使用索引的 MySQL 是一辆兰博基尼的话，那么没有设计和使用索引的 MySQL 就是一个人力三轮车。

例如，如果想要查阅一本书中与某个特定主题相关的所有页面，你会先去查询索引（索引按照字母表顺序列出了所有主题），然后从索引中找到一页或者多页与该主题相关的页面。

索引分单列索引和组合索引。
- 单列索引，即一个索引只包含单个列，一个表可以有多个单列索引，但这不是组合索引。
- 组合索引，即一个索引包含多个列。

上面都在说使用索引的好处，但过多的使用索引将会造成滥用。因此索引也会有它的缺点：虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行 INSERT、UPDATE和DELETE。因为更新表时，MySQL 不仅要保存数据，还要保存一下索引文件。

索引能够提高 SELECT 查询和 WHERE 子句的速度，但是却降低了包含 UPDATE 语句或 INSERT 语句的数据输入过程的速度。索引的创建与删除不会对表中的数据产生影响。

建立索引会占用磁盘空间的索引文件。实际上，索引也是一张表，该表保存了主键与索引字段，并指向实体表的记录。在不读取整个表的情况下，索引使数据库应用程序可以更快地查找数据。

**普通索引**
- 创建索引

    这是最基本的索引，它没有任何限制。它有以下几种创建方式：
    ```sql
    CREATE INDEX indexName
    ON mytable(username(length));
    ```
    如果是 CHAR，VARCHAR 类型，length 可以小于字段实际长度；如果是 BLOB 和 TEXT 类型，必须指定 length。

- 修改表结构(添加索引)
    ```sql
    ALTER table tableName
    ADD INDEX indexName(columnName)
    ```

- 创建表的时候直接指定
    ```sql
    CREATE TABLE mytable(  
    ID INT NOT NULL,  
    username VARCHAR(16) NOT NULL,
    INDEX [indexName] (username(length))  
    );
    ``` 

- 删除索引的语法
    ```sql
    DROP INDEX [indexName] ON mytable;
    ```

**唯一索引**

它与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一。它有以下几种创建方式：

- 创建索引
    ```sql
    CREATE UNIQUE INDEX indexName
    ON mytable(username(length))
    ```

- 修改表结构
    ```sql
    ALTER table mytable
    ADD UNIQUE [indexName] (username(length))
    ```

- 创建表的时候直接指定
    ```sql
    CREATE TABLE mytable(  
    ID INT NOT NULL,  
    username VARCHAR(16) NOT NULL,  
    UNIQUE [indexName] (username(length))  
    );
    ```

**实例**

本例会创建一个简单的索引，名为 "PersonIndex"，在 Person 表的 LastName 列：
```sql
CREATE INDEX PersonIndex
ON Person (LastName)
```
如果你希望以降序索引某个列中的值，你可以在列名称之后添加保留字 DESC：
```sql
CREATE INDEX PersonIndex
ON Person (LastName DESC)
```
假如你希望索引不止一个列，你可以在括号中列出这些列的名称，用逗号隔开：
```sql
CREATE INDEX PersonIndex
ON Person (LastName, FirstName)
```
此种索引叫聚簇索引

**使用ALTER 命令添加和删除索引**

有四种方式来添加数据表的索引：
- ALTER TABLE tbl_name ADD PRIMARY KEY (column_list): 该语句添加一个主键，这意味着索引值必须是唯一的，且不能为NULL。
- ALTER TABLE tbl_name ADD UNIQUE index_name (column_list): 这条语句创建索引的值必须是唯一的（除了NULL外，NULL可能会出现多次）。
- ALTER TABLE tbl_name ADD INDEX index_name (column_list): 添加普通索引，索引值可出现多次。
- ALTER TABLE tbl_name ADD FULLTEXT index_name (column_list):该语句指定了索引为 FULLTEXT ，用于全文索引。

以下实例为在表中添加索引。
```sql
ALTER TABLE testalter_tbl ADD INDEX (c);
```
你还可以在 ALTER 命令中使用 DROP 子句来删除索引。尝试以下实例删除索引:
```sql
ALTER TABLE testalter_tbl DROP INDEX c;
```

**显示索引信息**

你可以使用 SHOW INDEX 命令来列出表中的相关的索引信息。可以通过添加 \G 来格式化输出信息。
```sql
SHOW INDEX FROM table_name; \G
```

---

# 数据

## 插入数据

第 1 种：给全表字段插入数据，不需要指定字段列表，但要求数据的值出现的顺序必须与表中的字段出现的顺序一致，并且凡是非数值数据，都需要用引号（建议使用单引号）括起来。 
```sql
insert into 表名
values(值列表)[,(值列表)];
```

示例:
```sql
insert into test
valus('charies',18,'3.1');
```
如果数据是字符型，必须使用单引号或者双引号，如："value"。

第 2 种：给部分字段插入数据，需要选定字段列表，字段列表中字段出现的顺序与表中字段的顺序无关，但值列表中字段值的顺序必须与字段列表中的顺序保持一致。
```sql
insert into 表名(字段列表)
values(值列表)[,(值列表)];
```

示例:
```sql
insert into test(age,name)
valus(18,'guo');
```

## 删除数据

```sql
DELETE FROM table_name [WHERE Clause]
```
如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。可以在 WHERE 子句中指定任何条件.

示例:
```sql
-- 删除 id 为 3 的行
delete from students where id=3;
```
```sql
-- 删除所有年龄小于 21 岁的数据
delete from students where age<20;
```
```sql
-- 删除表中的所有数据
delete from students;
```

## 查询数据

以下为在 MySQL 数据库中查询数据通用的 SELECT 语法,SELECT 命令可以读取一条或者多条记录。
```sql
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```

查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用 WHERE 语句来设定查询条件。
- 使用星号（*）来代替其他字段，SELECT 语句会返回表的所有字段数据
- 使用 WHERE 语句来包含任何条件。
- 使用 LIMIT 属性来设定返回的记录数。
- 通过 OFFSET 指定 SELECT 语句开始查询的数据偏移量。默认情况下偏移量为 0。

## 修改数据

如果我们需要修改或更新 MySQL 中的数据，我们可以使用 SQL UPDATE 命令来操作。
```sql
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

示例:
```sql
update test
set age = 20
where name = 'guo';
```
在这里，建议尽量加上 where 条件，否则的话，操作的就是全表数据。

此外，判断更新操作是否成功，并不是看 SQL 语句是否执行成功，而是看是否有记录受到影响，即 affected 的数量大于 1 时，才是真正的更新成功。

```sql
-- 将 id 为 5 的手机号改为默认的
update students
set tel=default
where id=5;
```
```sql
-- 将所有人的年龄增加 1
update students
set age=age+1;
```
```sql
-- 将手机号为 13288097888 的姓名改为 "小明", 年龄改为 19: 
update students
set name="小明", age=19
where tel="13288097888";
```

## 序列

MySQL 序列是一组整数：1, 2, 3, ...，由于一张数据表只能有一个字段自增主键， 如果你想实现其他字段也实现自动增加，就可以使用MySQL序列来实现。

**使用 AUTO_INCREMENT**
```sql
-- 以下实例中创建了数据表 insect， insect 中 id 无需指定值可实现自动增长。

CREATE TABLE insect
    (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    name VARCHAR(30) NOT NULL, # type of insect
    date DATE NOT NULL, # date collected
    origin VARCHAR(30) NOT NULL # where collected
);

INSERT INTO insect (id,name,date,origin) VALUES
    (NULL,'housefly','2001-09-10','kitchen'),
    (NULL,'millipede','2001-09-10','driveway'),
    (NULL,'grasshopper','2001-09-10','front yard');

SELECT * FROM insect ORDER BY id;
+----+-------------+------------+------------+
| id | name        | date       | origin     |
+----+-------------+------------+------------+
|  1 | housefly    | 2001-09-10 | kitchen    |
|  2 | millipede   | 2001-09-10 | driveway   |
|  3 | grasshopper | 2001-09-10 | front yard |
+----+-------------+------------+------------+
```

**重置序列**

如果你删除了数据表中的多条记录，并希望对剩下数据的 AUTO_INCREMENT 列进行重新排列，那么你可以通过删除自增的列，然后重新添加来实现。 不过该操作要非常小心，如果在删除的同时又有新记录添加，有可能会出现数据混乱。操作如下所示：
```sql
ALTER TABLE insect
DROP id;
​
ALTER TABLE insect
ADD id INT UNSIGNED NOT NULL AUTO_INCREMENT FIRST,
ADD PRIMARY KEY (id);
```

**设置序列的开始值**

一般情况下序列的开始值为 1，但如果你需要指定一个开始值 100，那我们可以通过以下语句来实现：
```sql
mysql> CREATE TABLE insect
    -> (
    -> id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    -> PRIMARY KEY (id),
    -> name VARCHAR(30) NOT NULL,
    -> date DATE NOT NULL,
    -> origin VARCHAR(30) NOT NULL
)engine=innodb auto_increment=100 charset=utf8;
```

或者你也可以在表创建成功后，通过以下语句来实现：
```sql
ALTER TABLE t AUTO_INCREMENT = 100;
```

---

# 子句

## Like 子句

以下是 SQL SELECT 语句使用 LIKE 子句从数据表中读取数据的通用语法:
```sql
SELECT field1, field2,...fieldN
FROM table_name
WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
```

- 你可以在 WHERE 子句中指定任何条件.
- 你可以在 WHERE 子句中使用LIKE子句.
- 你可以使用LIKE子句代替等号 =.
- LIKE 通常与 % 一同使用,类似于一个元字符的搜索.
- 你可以使用 AND 或者 OR 指定一个或多个条件.
- 你可以在 DELETE 或 UPDATE 命令中使用 WHERE...LIKE 子句来指定条件.

like 匹配/模糊匹配,会与 `%` 和 `_` 结合使用.
```
'%a'     //以a结尾的数据
'a%'     //以a开头的数据
'%a%'    //含有a的数据
'_a_'    //三位且中间字母是a的
'_a'     //两位且结尾字母是a的
'a_'     //两位且开头字母是a的
```

查询以 java 字段开头的信息.
```sql
SELECT * FROM position WHERE name LIKE 'java%';
```

查询包含 java 字段的信息.
```sql
SELECT * FROM position WHERE name LIKE '%java%';
```

查询以 java 字段结尾的信息.
```sql
SELECT * FROM position WHERE name LIKE '%java';
```

- `%` : 表示任意 0 个或多个字符.可匹配任意类型和长度的字符,有些情况下若是中文,请使用两个百分号(%%)表示.
- `_` : 表示任意单个字符.匹配单个任意字符,它常用来限制表达式的字符长度语句.
- `[]` : 表示括号内所列字符中的一个(类似正则表达式).指定一个字符、字符串或范围,要求所匹配对象为它们中的任一个.
- `[^]` : 表示不在括号所列之内的单个字符.其取值和 `[]` 相同,但它要求所匹配对象为指定字符以外的任一个字符.
- 查询内容包含通配符时,由于通配符的缘故,导致我们查询特殊字符 "`%`"、"`_`"、"`[`" 的语句无法正常实现,而把特殊字符用 "`[ ]`" 括起便可正常查询.
