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

---

## 审计

审计（Audit）用于追踪和记录SQL Server实例，或者单个数据库中发生的事件（Event），审计运作的机制是通过捕获事件（Event），把事件包含的信息写入到事件日志（Event Log）或审计文件（Audit File）中，为review提供最真实详细的数据。

审计主要包含服务器审计对象（Server Audit，简称审计对象）、服务器级别的审计规范（Server Audit Specification）、数据库级别的审计规范（Database Audit Specification）和目标（Target）。
- 审计对象是在服务器级别上创建的对象，必须启用，用于指定审计数据的存储方式和存储路径，并提供工具查看审计数据。
- 服务器级别的审计规范用于记录服务器级别的事件（Event），
- 数据库级别的审计规范用于记录数据库级别的事件，
- Target是指用于存储Audit数据的媒介，可以是File、Windows Security Event Log 或 Windows Application Event Log，常用的Target是File。
SQL Server使用 Extended Events来帮助创建审计，也就是说，审计是在扩展事件的基础上设计的功能，专门用于审核数据库的安全。为了启用审计，首先需要创建一个SQL Server 实例级的审计对象，然后创建从属于它的“服务器审计规范”或“数据库审计规范”，审计输出的结果数据可以存储到审计文件（File）、安全日志（Security Log）和应用程序日志（Application Log）中。

---

## Source & Reference

- [理解SQL Server中的权限体系(上)----主体](https://www.cnblogs.com/CareySon/archive/2012/04/10/mssql-security-principal.html)
- [理解SQL Server中的权限体系(下)----安全对象和权限](https://www.cnblogs.com/CareySon/archive/2012/04/12/SQL-Security-SecurableAndPermission.html)
- [SQL Server 审计 第一篇：介绍（Audit）](https://www.cnblogs.com/ljhdo/p/14085487.html)
- [SQL Server 审计 第二篇： 创建审计](https://www.cnblogs.com/ljhdo/p/5721668.html)
- [SQL Server 审计 第三篇：查看审计数据](https://www.cnblogs.com/ljhdo/p/13232283.html)
