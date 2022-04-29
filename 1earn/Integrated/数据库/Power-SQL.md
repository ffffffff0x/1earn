# Power-SQL

---

## DDL 操作数据库、表

### 数据库操作

#### 创建数据库

我们可以在登录 MySQL 服务后，使用 creat 命令创建数据库，语法如下:
```sql
create database 数据库名称 [库选项];
```
其中，库选项是用来约束数据库的，为可选项（有默认值），共有两种，分别为：
- 字符集设定：charset/ character set+ 具体字符集，用来表示数据存储的编码格式，常用的字符集包括 GBK 和 UTF8 等。
- 校对集设定：collate+ 具体校对集，表示数据比较的规则，其依赖字符集。

示例：
```sql
-- 创建数据库 test
create database test charset utf8;
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

```sql
-- 创建数据库，判断不存在，再创建;
create database if not exists 数据库名称;

-- 创建数据库，并且指定字符集;
create database 数据库名称 character set 字符集名称;

-- 创建数据库db，判断是否存在，并指定字符集为gbk
create database if not exists db character set gbk;
```

#### 删除数据库

使用普通用户登录 MySQL 服务器，你可能需要特定的权限来创建或者删除 MySQL 数据库，所以我们这边使用 root 用户登录，root 用户拥有最高权限。

在删除数据库过程中，务必要十分谨慎，因为在执行删除命令后，所有数据将会消失。
```sql
-- 语法
drop database <数据库名>;

-- 例如删除名为 test 的数据库：
drop database test;

-- 判断数据库是否存在，存在则删除;
drop database if exists 数据库名称;
```

#### 查询数据库

```sql
-- 查看全部
show databases;

-- 查看部分（模糊查询）
show databases like 'pattern';
```

其中，pattern 是匹配模式，有两种，分别为：
- %：表示匹配多个字符;
- _：表示匹配单个字符。

此外，在匹配含有下划线 _ 的数据库名称的时候，需要在下划线前面加上反斜线 \_ 进行转义操作。
```sql
-- 匹配所有 TBL 开头的数据库。
show databases like 'TBL%';

-- 查看数据库的创建语句
show create database 数据库名称;
-- 在这里，查看的结果有可能与咱们书写的 SQL 语句不同，这是因为数据库在执行 SQL 语句之前会优化 SQL，系统保存的是优化后的结果。
```

#### 更新数据库

在这里，需要注意：数据库的名字不可以修改。

```sql
-- 语法
alter database 数据库名称 [库选项];

-- 修改test数据库的字符集为 gbk.
alter database test charset gbk;
```

#### 选择数据库

在你连接到 MySQL 数据库后，可能有多个可以操作的数据库，所以你需要选择你要操作的数据库。
```sql
-- 使用 test 数据库
use test;
```

执行以上命令后，你就已经成功选择了 test 数据库，在后续的操作中都会在 test 数据库中执行。

注意:所有的数据库名，表名，表字段都是区分大小写的。所以你在使用 SQL 命令时需要输入正确的名称。

```sql
-- 查询正在使用的数据库;
select database();
```

#### 数据库的备份和还原

备份：
```bash
mysqldump -u用户名 -p密码 要备份的数据库名称 > 保存路径;
```

还原：
- 登录数据库：-u用户名称 -p密码;
- 创建数据库：create database 数据库名称;
- 使用数据库：use 数据库名称;
- 执行文件：source 文件路径;

#### 权限的管理

**查询权限**
```sql
-- 语法
show grants for '用户名'@'主机名';
show grants for 'list'@'localhost';
```

**授予权限**
```sql
-- 语法
grant 权限列表 on 数据库.表名 to '用户名'@'主机名';
```

**一次授予所有权限**
```sql
grant all on * . * to '用户名'@'主机名';
```

**撤销权限**
```sql
revoke 权限列表 on 数据库名.表名 from '用户名'@'主机名';
```

---

### 表操作

#### 创建表

创建 MySQL 数据表需要以下信息：
- 表名
- 表字段名
- 定义每个表字段

以下为创建 MySQL 数据表的 SQL 通用语法：
```sql
create table [if not exists] + 表名(
    字段名称 数据类型,
    ……
    字段名称 数据类型   /* 最后后一行，不需要加逗号 */
)[表选项];
```

其中，`if not exists` 表示如果表名不存在，就执行创建代码;如果表名存在，则不执行创建代码。

表选项则是用来控制表的表现形式的，共有三种，分别为：
- 字符集设定：charset/ character set+ 具体字符集，用来表示数据存储的编码格式，常用的字符集包括 GBK 和 UTF8 等。
- 校对集设定：collate+ 具体校对集，表示数据比较的规则，其依赖字符集。
- 存储引擎：engine+ 具体存储引擎，默认为 InnoDB，常用的还有 MyISAM.

```sql
-- 在已经指定的数据库中创建数据表 test_tbl：
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
    age int,            /* 整型不需要指定具体的长度 */
    grade varchar(10)   /* 最后后一行，不需要加逗号 */
)charset utf8;
```

第 2 种：隐式的指定表所属的数据库，示例
```sql
use test;               /* use + 数据库名称，表示切换到指定的数据库，这句命令其实不加分号也可以，但不建议这么做 */
create table if not exists student(
    name varchar(10),
    age int,            /* 整型不需要指定具体的长度 */
    grade varchar(10)   /* 最后后一行，不需要加逗号 */
)charset utf8;
```

创建 MySql 的表时，表名和字段名外面的符号 ` 不是单引号，而是英文输入法状态下的反单引号，也就是键盘左上角 esc 按键下面的那一个 ~ 按键

反引号是为了区分 MySql 关键字与普通字符而引入的符号，一般的，表名与字段名都使用反引号。

#### 删除表

MySQL 中删除数据表是非常容易操作的， 但是你再进行删除表操作时要非常小心，因为执行删除命令后所有数据都会消失。

```sql
-- drop table table_name : 删除表全部数据和表结构，立刻释放磁盘空间，不管是 Innodb 和 MyISAM;
drop table student;

-- 判断表是否存在，若存在则删除;
drop table if exists 表名称;

-- truncate table table_name : 删除表全部数据，保留表结构，立刻释放磁盘空间 ，不管是 Innodb 和 MyISAM;
truncate table student;

-- delete from table_name : 删除表全部数据，表结构不变，对于 MyISAM 会立刻释放磁盘空间，InnoDB 不会释放磁盘空间;
delete from student;

-- delete from table_name where xxx : 带条件的删除，表结构不变，不管是 innodb 还是 MyISAM 都不会释放磁盘空间;
delete from student where T_name = "张三";  -- 实例，删除学生表中姓名为 "张三" 的数据：

-- delete 操作以后，使用 optimize table table_name 会立刻释放磁盘空间，不管是 innodb 还是 myisam;
delete from student where T_name = "张三";  -- 实例，删除学生表中姓名为 "张三" 的数据：

-- 实例，释放学生表的表空间：
optimize table student;
```

delete from 表以后虽然未释放磁盘空间，但是下次插入数据的时候，仍然可以使用这部分空间。

总结
- 当你不再需要该表时， 用 drop;
- 当你仍要保留该表，但要删除所有记录时， 用 truncate;
- 当你要删除部分记录时， 用 delete。

#### 查询表

```sql
-- 查看全部
show tables;

-- 查看部分（模糊查询）
show tables like 'pattern';
```

其中，pattern 是匹配模式，有两种，分别为：
- %：表示匹配多个字符;
- _：表示匹配单个字符。

此外，在匹配含有下划线 _ 的表名的时候，需要在下划线前面加上反斜线 `\_` 进行转义操作。
```sql
-- 表示匹配所有以 t 结尾的表。
show tables like '%t';

-- 查看表的创建语句
show create table 表名;
```
在这里，咱们也可以用 `\g` 和 `\G` 代替上述语句中的;分号，其中 `\g` 等价于分号，`\G` 则在等价于分号的同时，将查的表结构旋转 90 度，变成纵向结构。

```sql
-- 查看表中的字段信息
show columns from 表名;

-- 查询表的结构
desc 表名;
```

#### 更新表

```sql
-- 修改表名
rename table 旧表名 to 新表名;

-- 修改表选项
alter table 表名 表选项[=] 值;

-- 修改表的字符集
alter table 表名 character set 字符集名称;

-- 新增字段
alter table 表名 add [column] 列名 数据类型 [列属性][位置];

-- 其中，位置表示此字段存储的位置，分为 first（第一个位置）和 after + 列名（指定的字段后，默认为最后一个位置）.
alter table student add column id int first;

-- 只修改列的数据类型;
alter table 表名 modify 列名 数据类型 [列属性][位置];

-- 其中，位置表示此字段存储的位置，分为 first（第一个位置）和 after + 列名（指定的字段后，默认为最后一个位置）.
alter table student modify name char(10) after id;

-- 即修改列名，也修改该列的数据类型
alter table 表名 change 旧列名 新的列名 新的数据类型 [列属性][位置];

-- 其中，位置表示此字段存储的位置，分为 first（第一个位置）和 after + 列名（指定的字段后，默认为最后一个位置）.
alter table student change grade class varchar(10);

-- 删除字段
alter table 表名 drop 列名;

alter table student drop age;
-- 注意：如果表中已经存在数据，那么删除该字段会清空该字段的所有数据，而且不可逆，慎用。
```

#### 复制表

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
  PRIMARY KEY  (`test_id`),
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
  -> PRIMARY KEY  (`test_id`),
  -> UNIQUE KEY `AUTHOR_INDEX` (`test_author`)
-> ) ENGINE=InnoDB;
Query OK, 0 rows affected (1.80 sec)
```

步骤三

执行完第二步骤后，你将在数据库中创建新的克隆表 clone_tbl。 如果你想拷贝数据表的数据你可以使用 INSERT INTO... SELECT 语句来实现。

```sql
mysql> INSERT INTO clone_tbl (test_id,
    ->                        test_title,
    ->                        test_author,
    ->                        submission_date)
    -> SELECT test_id,test_title,
    ->        test_author,submission_date
    -> FROM test_tbl;
Query OK, 3 rows affected (0.07 sec)
Records: 3  Duplicates: 0  Warnings: 0
```

#### 临时表

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

#### 索引

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
    如果是 CHAR，VARCHAR 类型，length 可以小于字段实际长度;如果是 BLOB 和 TEXT 类型，必须指定 length。

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

## DML 增删改表中的数据

### 插入数据

第 1 种：给全表字段插入数据，不需要指定字段列表，但要求数据的值出现的顺序必须与表中的字段出现的顺序一致，并且凡是非数值数据，都需要用引号（建议使用单引号）括起来。
```sql
insert into 表名
values(值列表)[,(值列表)];

-- 示例:
insert into test
valus('charies',18,'3.1');
```
如果数据是字符型，必须使用单引号或者双引号，如："value"。

第 2 种：给部分字段插入数据，需要选定字段列表，字段列表中字段出现的顺序与表中字段的顺序无关，但值列表中字段值的顺序必须与字段列表中的顺序保持一致。
```sql
insert into 表名(字段列表)
values(值列表)[,(值列表)];

-- 示例:
insert into test(age,name)
valus(18,'guo');
```

### 删除数据

```sql
-- 删除满足条件的信息
DELETE FROM table_name [WHERE Clause]
-- 如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。可以在 WHERE 子句中指定任何条件.

-- 删除 id 为 3 的行
delete from students where id=3;
```
```sql
-- 删除所有年龄小于 21 岁的数据
delete from students where age<20;

-- 删除表中的所有数据
delete from students;
```

### 修改数据

```sql
-- 如果我们需要修改或更新 MySQL 中的数据，我们可以使用 SQL UPDATE 命令来操作。
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]

-- 示例:
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

-- 将所有人的年龄增加 1
update students
set age=age+1;

-- 将手机号为 13288097888 的姓名改为 "小明", 年龄改为 19:
update students
set name="小明", age=19
where tel="13288097888";
```

## DQL 查询表中的记录

### 查询数据

```sql
-- SELECT 命令可以读取一条或者多条记录。
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]

select​ 字段列表
from​ 表名列表
where​ 条件列表
group​ 分组字段
having​ 分组之后的条件
order by​ 排序
limit​ 分页限定
```

查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用 WHERE 语句来设定查询条件。
- 使用星号（*）来代替其他字段，SELECT 语句会返回表的所有字段数据
- 使用 WHERE 语句来包含任何条件。
- 使用 LIMIT 属性来设定返回的记录数。
- 通过 OFFSET 指定 SELECT 语句开始查询的数据偏移量。默认情况下偏移量为 0。

#### 基础查询

```sql
-- 多个字段的查询
select 字段1，字段2，…… from 表名;

-- 去除重复
select distinct 字段名 from 表名;

-- 条件查询
where 子句后面跟条件
运算符
大于、小于、>=、<=、=、<>(不等于)
between...and
in(集合)
like：模糊查询
占位符
_：可以代替任意一个字符;
%：可以代替任意多个字符;
and 或 &&
or 或 ||
not 或 ！

-- 查询年龄大于等于20
select * from stu where age >= 20;

-- 查询年龄不等于20
select * from stu where age <> 20;
select * from stu where age != 20;

-- 查询年龄大于等于20，小于等于30的;
select * from stu where age between 20 and 30;
select * from stu where age >= 20 && age <= 30;

-- 查询年龄22岁、19岁、25岁;
select * from stu where age = 22 or age = 19 or age = 25;
select * from stu where age in (22, 19, 25);

-- 查询英语成绩为null;
select * from stu where English is null;
-- 注意事项：不能写=null;

-- 查询英语成绩不为null;
select * from stu where English is not null;
-- 注意事项：不能写!=null;

-- 查询姓张的人：
select * from stu where name like '张%';

-- 查询名字里面第二个字是三的人;
select * from stu where name like '_三%';

-- 查询名字是三个字的人
select * from stu where name like '_ _ _';

-- 查询名字里面包含张的人
select * from stu where name like '%张%';
```

#### 排序查询

```sql
-- 语法
order by 子句;

-- 按照数学成绩升序排序;
select * from stu order by math;
select * from stu order by math ASC;

-- 按照数学成绩升序排名，如果数学成绩一样，则按照英语成绩升序排名;
select * from stu order by math ASC，English ASC;
```

排序方式：
- ASC：升序（默认就是升序）;
- DESC：降序

注意：如果有多个排序条件，则当前边的条件值一样时，才会判断第二条件;

#### 聚合查询

```sql
-- count：计算个数;一般选择非空的列：主键

select count(ifnull(id,0)) from stu;

-- count(*)：不建议使用;
-- max：计算最大值;

select max(english) from stu;

-- min：计算最小值;

select min(english) from stu;

-- sum：计算和;

select sum(english) from stu;

-- avg：计算平均值;

select avg((ifnull(english,0)) from stu;
```

#### 分组查询

```sql
-- 语法
group by 子句;

-- 按照性别分组，分别查询男生和女生的平均成绩
select sex，avg(ifnull(english,0)) from stu group by sex;

-- 按照性别分组，分别查询男生和女生的平均成绩
select sex, avg(ifnull(english,0))，count(ifnull(id,0)) from stu group by sex;

-- 按照性别分组，分别查询男生和女生的平均成绩，以及人数。要求：分数低于70分的人不参与分组;
select sex, avg(ifnull(english,0))，count(ifnull(id,0)) from stu where english > 70 group by sex;

-- 按照性别分组，分别查询男生和女生的平均成绩，以及人数。要求：分数低于70分的人不参与分组,且分组之后，该组人数要大于2;
select sex, avg(ifnull(english,0))，count(ifnull(id,0)) from stu where english > 70 group by sex having count(ifnull(id,0)) > 2;
select sex, avg(ifnull(english,0))，count(ifnull(id,0)) as 人数 from stu where english > 70 group by sex having 人数 > 2;
```

where 和 having 的区别：
- where 在分组之前进行限定，如果不满足条件，则不参与分组。having 在分组之后进行限定，如果不满足结果，则不会被查询出来;
- where 后面不能跟聚合函数，having 可以跟聚合函数的判断;

#### 分页查询

```sql
-- 语法
limit 开始索引，每页查询的条数;

-- 每页显示3条
select * from stu limit 0,3;
```

#### 模糊查询

```sql
-- LIKE 子句
SELECT field1, field2,...fieldN
FROM table_name
WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
```

- 你可以在 WHERE 子句中指定任何条件.
- 你可以在 WHERE 子句中使用 LIKE 子句.
- 你可以使用 LIKE 子句代替等号 =.
- LIKE 通常与 % 一同使用, 类似于一个元字符的搜索.
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

```sql
-- 查询以 java 字段开头的信息.
SELECT * FROM position WHERE name LIKE 'java%';

-- 查询包含 java 字段的信息.
SELECT * FROM position WHERE name LIKE '%java%';

-- 查询以 java 字段结尾的信息.
SELECT * FROM position WHERE name LIKE '%java';
```

- `%` : 表示任意 0 个或多个字符.可匹配任意类型和长度的字符,有些情况下若是中文,请使用两个百分号(%%)表示.
- `_` : 表示任意单个字符.匹配单个任意字符,它常用来限制表达式的字符长度语句.
- `[]` : 表示括号内所列字符中的一个(类似正则表达式).指定一个字符、字符串或范围,要求所匹配对象为它们中的任一个.
- `[^]` : 表示不在括号所列之内的单个字符.其取值和 `[]` 相同,但它要求所匹配对象为指定字符以外的任一个字符.
- 查询内容包含通配符时,由于通配符的缘故,导致我们查询特殊字符 "`%`"、"`_`"、"`[`" 的语句无法正常实现,而把特殊字符用 "`[ ]`" 括起便可正常查询.

### 多表查询

#### 笛卡尔积

有两个集合A、B，取这两个集合的所有组成情况。

要完成多表查询，需要消除无用的数据。

#### 内连接

**隐式连接**

使用where条件消除无用数据;
```sql
-- 查询所有员工信息和对应的部门信息;
select * from emp, dept where emp.dept_id = dept.id;

-- 查询员工表的姓名，性别、部门表的名称;
select emp.name, emp.sex, dept.name from emp, dept where emp.dept_id = dept.id;

-- 简化
  select
  	t1.name,
      t1.sex,
      t2.name
  from
  	emp t1,
      dept t2
  where
  	t1.dept_id = t2.id;
```

**显示内连接**

```sql
-- 语法
select 字段列表 from 表名1 inner join 表名2 on 条件;

-- 查询所有员工信息和对应的部门信息;
select * from emp inner join dept on emp.dept_id = dept.id;
-- -- inner可以省略，并且这个也可以像上面那样起别名;
```

#### 外连接

**左外连接**
```sql
-- 语法
select 字段列表 from 表1 left outer join 表2 on 条件; -- 注意：outer可以省略不写

-- 查询的范围：查询的是左表所有的信息，以及其与右表的交集部分;
select t1.*, t2.name  from  emp t1 left join dept  t2 on t1.dept = t2.id;
```

**右外连接**
```sql
-- 语法
select 字段列表 from 表1 right outer join 表2 on 条件; -- 注意：outer可以省略不写

-- 查询的范围：查询的是右表所有的信息，以及其与左表的交集部分;
select t1.* t2.name from emp t1 right join dept t2 on t1.dept = t2.id;
```

#### 子查询

概念：查询中嵌套查询，称嵌套查询为子查询。

```sql
-- 查询工资最高的员工信息;

-- 传统写法
-- 首先查询最高工资是多少
select max(工资) from emp; -- 假设查询出来最高工资是9000;
-- 然后将查询出来的信息作为条件在进行查询;
select * from emp where  emp.工资 = 9000;

-- 子查询方式
select * from emp where emp.工资 = (select max(工资) from emp);
```

**子查询的不同情况**

子查询的结果是单行单列的;
```sql
-- 子查询可以作为条件，使用条件运算符去判断;

-- 查询工资小于平均工资的员工信息;
select * from emp where emp.工资 < (select avg(ifnull(工资, 0)) from emp);
```

子查询的结果是多行单列的;
```sql
-- 子查询可以作为条件，使用条件运算符去判断;

-- 查询市场部、销售部所有的员工信息;
select * from emp where emp.dept_id in (select dept_id  from dept where  name in ("市场部", "销售部"));
```

子查询的结果是多行多列的;
```sql
-- 子查询可以作为一张虚拟的表参与查询;

-- 查询员工入职日期是2011-11-11日之后的员工信息和部门信息;
select * from dept t1, (select * from emp where emp.date > "12-11-11") t2 where t1.id = t2.dept_id;
-- 普通查询
select * from emp t1, dept t2 where t1.id = t2.dept_id and t1.date > "2011-11-11";
```

---

## DCL 管理用户、授权

### 管理用户

**添加用户**
```sql
-- 语法：create user '用户名'@'主机名' identified by '密码';
create user 'test' @ 'localhost' identified by '123';
```

**删除用户**
```sql
-- 语法：drop user '用户名' @ '主机名';
drop user 'test' @ 'localhost';
```

**修改用户密码**

```sql
-- 方法一：
update user set password = password('新密码') where user = '用户名';

-- 方法二：
set password for '用户名'@'主机名' = password('新密码');
```

**查询用户**
```sql
-- 切换到 mysql 数据库
use mysql;

-- 切换到 mysql 数据库
select * from user;
```

---

## 约束

**描述**

对表中的数据进行限定，保证数据的正确性、有效性、完整性。

### 非空约束

关键字：not null

作用：某一列的值不能为null;
```sql
-- 创建表时添加约束;
create table stu(
    name varchar(4) not null
);

-- 表创建好后，添加非空约束;
create table stu(
  	name varchar(4)
);

alter table stu modify name varchar(4) not null;

-- 删除约束
alter table stu modify name varchar(4);     -- 将姓名的非空约束删除
```

### 唯一约束

关键字：unique;

作用：某一列的值不能重复;
```sql
-- 创建表时添加唯一约束

create table stu(
  	phone_number varchar(11) unique
);

-- 表创建好后，添加唯一约束;
alter table stu modify phone_number varchar(11)  unique;

-- 删除唯一约束
alter table stu drop index phone_number;
```

注意: 唯一约束可以有 null 值，但是只能有一条记录为 null。通俗来讲，也就是说 null 值也不能重复出现;

### 主键约束

关键字：primary key;

作用：非空且唯一;

```sql
-- 创建表时添加主键约束;
create table stu(
  	id int primary key
);

-- 表创建好后添加主键约束;
alter table stu modify id int primary key;

-- 删除主键
alter table stu drop primary key;
```

注意事项：
- 一张表只能有一个字段为主键;
- 但是可以设置为多个字段为主键，也即联合主键;
- 主键就是表中记录的唯一标识;

### 自动增长

关键字：auto_increment;

作用：如果某一列是数值型的，可以完成值的自动增长。

```sql
-- 在创建表时添加自动增长;
create table stu (
  	id int auto_increment
);

-- 表创建好后添加自动增长
alter table stu modify id int auto_increment;

-- 删除自动增长
alter table stu modify id int;
-- 这样不会删除掉主键约束
```

这个值的增长，是按照上一条的数据进行增长。如果上一条数据是5，那么下一条就是6。

一般情况下，自动增长和主键一起使用;

### 外键约束

关键字：foreign key;

作用: 可定义表间以及表内必需的关系

```sql
-- 在创建表时添加外键约束
create table emp(
  	dep_id int
      constraint  起一个新的名称  foreign  key  (外键名称) references 主表名称(主表列名称);
);

  --主表
  CREATE TABLE department(
  	id INT PRIMARY KEY AUTO_INCREMENT,
  	dep_name VARCHAR(30),
  	dep_location VARCHAR(30)
  );

  CREATE TABLE employee(
  	id INT PRIMARY KEY AUTO_INCREMENT,
  	NAME VARCHAR(30),
  	age INT,
  	dep_id INT,--外键名称
  	CONSTRAINT emp_dep_fk FOREIGN KEY (dep_id) REFERENCES department(id)
  );

-- 创建表后添加外键;
alter table employee add CONSTRAINT emp_dep_fk FOREIGN KEY (dep_id) REFERENCES department(id);

-- 删除外键;
alter table employee  drop foreign key emp_dep_fk;

-- 级联操作

-- 添加外键，设置级联更新;
alter table employee add CONSTRAINT emp_dep_fk FOREIGN KEY (dep_id) REFERENCES department(id) on update  cascade;

-- 添加外键，设置级联更新，设置级联删除;
alter table employee add CONSTRAINT emp_dep_fk FOREIGN KEY (dep_id) REFERENCES department(id) on update  cascade on delete cascade;
```

---

## 数据库的设计

### 多表之间的关系

**一对一**

场景 : 人和身份证

分析：一个人只有一个身份证，一个身份证只能对应一个人。

实现方式：在任意一方设置唯一约束的外键指向另一方的主键;

**一对多（多对一）**

场景 : 部门和员工

分析：一个部门有多个员工，一个员工只能对应一个部门;

实现方式：在多的一方建立外键，指向一的一方的主键。

**多对多**

场景 : 学生和课程：

分析：一个学生可以选择很多门课，一个课程也可以被很多学生选择;

实现方式：多对多需要借助第三张中间表。

---

## 事物

如果一个包含多个步骤的业务操作，被事物管理，那么这些操作要么同时成功，要么同时失败;

**事物的四大特征**

- 原子性：是不可分割的最小操作单位，要么同时成功，要么同时失败;
- 持久性：当事务提交或回滚后，数据库会持久化的保存数据;
- 隔离性：多个事物之间，相互隔离;
- 一致性：事务操作前后，数据总量不变;

**事务的隔离级别**

多个事物之间隔离的、相互独立的。但是如果多个事务操作同一批数据，则会引发一些问题，设置不同的隔离级别就可以解决这些问题。

存在的问题：
- 脏读：一个事务，读取到另一个事务中没有提交的数据;
- 不可重复度(虚读)：在一个事务中，两次读取到的数据不一样;
- 幻读：一个事务操作(DML)数据表中的所有记录，另一个事务添加了一条数据，则第一个事物查询不到自己的修改。

隔离级别：
- read uncommitted : 读未提交
    - 产生的问题：脏读、不可重复读、幻读;
- read committed : 读已提交
    - 产生的问题：不可重复读、幻读;
- repeatable : 可重复读（Oracle 默认）
    - 产生的问题：幻读;
- serializable : 串行化
    - 产生的问题：可以解决所有的问题;

注意：隔离级别从小到大安全性越来越高，但是效率越来越低;

查询数据隔离级别的语句：
```sql
select @@tx_isolation;
```

数据库隔离等级的设置语句：
```sql
set global transation isolation level 级别字符串;
```
