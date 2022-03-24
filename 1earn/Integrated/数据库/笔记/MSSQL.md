# MSSQL

---

## 角色

角色是为了方便权限管理而设置的一种管理单位，可使一组登录账户或数据库用户在数据库服务器或数据库对象上具有相同的权限。

按权限作用范围可分为固定服务器角色与固定数据库角色，其作用范围分别为整个数据库服务器与单个数据库。

数据库角色除了固定角色外，还有一种角色是用户定义的数据库角色，可以创建、修改或删除。

**固定服务器角色**

必须使登录账户成为某个固定服务器角色的成员，才能使它们具有操作数据库服务器的权限。

- sysadmin 执行 SQL Server 中的任何动作
- serveradmin 配置服务器设置
- setupadmin 安装复制和管理扩展过程
- securityadmin 管理登录和创建数据库等
- processadmin 管理 SQL Server 进程
- dbcreator 创建和修改数据库
- diskadmin 管理磁盘文件
- bulkadmin 有权执行 BULK INSERT 语句

**固定数据库角色**

固定数据库角色在数据库层上进行定义，作用范围仅限于每个单独的数据库中，相互没有影响。

- db_owner 执行数据库中技术所有动作
- db_accessadmin 添加、删除用户
- db_datareader 查看所有数据库中用户表内数据
- db_datawriter 添加、修改或删除所有数据库中用户表内数据
- db_ddladmin 执行所有 DDL 操作
- db_securityadmin 管理数据库中与安全权限有关所有动作
- db_backoperator 备份数据库
- db_denydatareader 不能看到数据库中任何数据
- db_denydatawriter 不能改变数据库中任何数据

---

## 身份验证方式

SQL Server 两种身份验证方式
- Windows 身份验证 : 用户只要通过操作系统的登录验证，就可以连接到 SQL Server 服务器。
- SQLServer 身份验证 : 即使用户通过了操作系统的登录验证，也必须输入有效的 SQL Server 专用登录名与密码。

---

## 补丁

SQL Server 补丁相关概念
- RTM： 表示 Release to Manufacturing ，这是产品的原始发布版本，当从光盘或 MSDN 下载的默认版本。
- Hotfix：需要修复的某个问题，每年 SQL Server 会出现许多 bug 或漏洞，这些问题的修复则被定义为 Hotfix。
- Cumulative Update（CU）：累计更新包，由 Hotfix 组成。CU 每 8 个星期发布一次，每个最新的 CU 版本都包含之前的 CU 中的 Hotfix。
- Service Package（SP）： SP 是集成 Hotfix 最多的包，这些 Hotfix 是经过官方完整测试过的。
