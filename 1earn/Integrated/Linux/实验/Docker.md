# Docker

> 笔记内容由 [xidaner](https://github.com/xidaner) 提供,仅做部分内容排版修改

---

使用docker 搭建`PHP`环境

**PHP**

- PHP 5.2

    |PHP版本|系统版本|	Apache 版本|Web路径|COMMAND|
    |-|-|-|-|-|
    |5.2.17|Ubuntu 16.04.5|2.2.22|	/var/www/html|/init.sh|

    ```bash
    # 拉取镜像
    docker pull seti/php52:latest

    # 运行容器
    docker run -d -p 8080:80 --name PHP5.2 seti/php52:latestW
    ```

- PHP 5.6

    |PHP版本|系统版本|	Apache 版本|Web路径|COMMAND|
    |-|-|-|-|-|
    |5.6.40|Ubuntu 16.04.5|2.4.37|/var/www/app|/sbin/entrypoint.sh|

    ```bash
    # 拉取镜像
    docker pull romeoz/docker-apache-php:5.6

    # 运行容器
    docker run -d -p 8080:80 --name PHP5.6 romeoz/docker-apache-php:5.6
    ```

- PHP 7.3

    |PHP版本|系统版本|	Apache 版本|Web路径|COMMAND|
    |-|-|-|-|-|
    |7.3.10|Ubuntu 18.04.3|2.4.4|/var/www/app|/sbin/entrypoint.sh|

    ```bash
    # 拉取镜像
    docker pull romeoz/docker-apache-php:7.3

    # 运行容器
    docker run -d -p 8080:80 --name PHP7.3 romeoz/docker-apache-php:7.3
    ```

**LAMP**

- PHP 5.6.28 + MariaDB 10.1.19

    |PHP版本|MariaDB版本|系统版本|Apache 版本	|Web路径|	COMMAND|
    |-|-|-|-|-|-|
    |5.6.28	|10.1.19	|Alpine Linux 3.4	|2.4.23|	/var/www/html|	/start.sh|

    MySQL 的用户名和密码信息：

    |用户名|密码|
    |-|-|
    |root|空|

    ```bash
    # 拉取镜像
    docker pull janes/alpine-lamp:latest

    # 运行容器
    docker run -d -p 8080:80 --name LAMP janes/alpine-lamp:latest
    ```

- PHP 5.5.9 + MySQL 5.5.61

    |PHP版本|MySQL版本|系统版本|Apache 版本	|Web路径|	COMMAND|
    |-|-|-|-|-|-|
    |5.5.9	|5.5.61	|Ubuntu 14.04.5		|2.4.7|	/var/www/html|	/start.sh|

    MySQL 的用户名和密码信息：

    |用户名|密码|
    |-|-|
    |root|root|

    ```bash
    # 拉取镜像
    docker pull medicean/vulapps:base_lamp

    # 运行容器
    docker run -d -p 8080:80 --name LAMP medicean/vulapps:base_lamp
    ```

- PHP 7.3.22 + MariaDB 10.4.15

    |PHP版本|MariaDB版本|系统版本|Apache 版本	|Web路径|	COMMAND|
    |-|-|-|-|-|-|
    |7.3.22	|10.4.15	|Alpine Linux 3.11|2.4.46|/var/www/localhost/htdocs|/entry.sh|

    MySQL 的用户名和密码信息：

    |用户名|密码|
    |-|-|
    |root|root|

    ```bash
    # 拉取镜像
    docker pull sqlsec/alpine-lamp

    # 运行容器 记住要指定密码
    docker run -d -p 8080:80 --name LAMP -e MYSQL_ROOT_PASSWORD=root sqlsec/alpine-lamp
    ```
