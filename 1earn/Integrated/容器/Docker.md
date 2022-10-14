# Docker

<p align="center">
    <img src="../../../assets/img/banner/Docker.png">
</p>

---

**官网**
- https://www.docker.com

**Docker是啥**

Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从 Apache2.0 协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

**版本区别**

最早的时候 docker 就是一个开源项目，主要由 docker 公司维护.

- 2017年年初，docker 公司将原先的 docker 项目改名为 moby，并创建了 docker-ce 和 docker-ee.
- docker-ce 是社区版本，适用于刚刚开始 docker 和开发基于 docker 研发的应用开发者或者小型团队.
- docker-ee 是企业版，适用于企业级开发，同样也适用于开发、分发和运行商务级别的应用的 IT 团队.
- docker-io, docker-engin 是以前早期的版本.

**扩展项目**
- [Compose](https://github.com/docker/compose) - 一个部署多个容器的简单但是非常必要的工具.
    - [Docker-Compose安装使用](../../Linux/Power-Linux.md#docker-compose)
- [Portainer](https://www.portainer.io/) - Docker 一款可视化管理用具，部署简单，推荐。
    - [Docker-Portainer安装使用](../../Linux/Power-Linux.md#docker-portainer)
- [instantbox](https://github.com/instantbox/instantbox) - 脚本实现的一个 docker 虚拟化平台,快速获得开箱即用的热乎乎的虚拟机😁
- [silenceshell/docker_mirror](https://github.com/silenceshell/docker_mirror) - 查找最快的 docker 镜像
- [jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker) - 快速管理 docker

**学习教程**
- [Docker — 从入门到实践](https://yeasy.gitbook.io/docker_practice/)

---

## Docker 原理

Docker 是目前最具代表性的容器平台之一，它模糊了传统的 IaaS 和 PaaS 的边界，具有持续部署与测试、跨云平台支持等优点。在基于 Kubernetes 等容器编排工具实现的容器云环境中，通过对跨主机集群资源的调度，容器云可提供资源共享与隔离、容器编排与部署、应用支撑等功能。

Docker 容器技术以宿主机中的容器为管理单元，但各容器共用宿主机内核资源，分别通过 Linux 系统的 Namespaces 和 CGroups 机制实现资源的隔离与限制。

**相关文章**
- [Docker原理第二话--Namespace](https://blog.csdn.net/m0_37552052/article/details/78344607)
- [Docker原理第三话--CGroups](https://blog.csdn.net/m0_37552052/article/details/78480266)

**Namespaces**

为了保证容器进程之间的资源隔离，避免相互影响和干扰，Linux 内核的 Namespaces（命名空间）机制提供了 UTS、User、Mount、Network、PID、IPC 等命名空间实现了主机名、用户权限、文件系统、网络、进程号、进程间通信等六项资源隔离功能。通过调用 clone() 函数并传入相应的系统调用参数创建容器进程，可实现对应资源内容的隔离，如表所示。

| 命名空间 	  |  系统调用参数 	   |   隔离内容 	                   |  Linux内核版本 |
| - | - | - | - |
| UTS         | CLONE_NEWUTS       | 主机名和域名                    |   2.6.19 |
| IPC         | CLONE_NEWIPC       | 信号量、信息队列和共享内	       |   2.6.19 |
| PID         | CLONE_NEWPID       | 进程编号            	         |  2.6.24 |
| Network     | CLONE_NEWNET       | 网络设备、网络栈、端口等           |  2.6.29 |
| Mount       | CLONE_NEWNS        | 挂载点（文件系统）                |  2.4.19 |
| User        | CLONE_NEWUSER      | 用户和用户组                     |  3.8 |

对于某个进程而言，可通过查看 `/proc/[PID]/ns` 文件，获取该进程下的命名空间隔离情况。其中，每一项命名空间都拥有一个编号对其进行唯一标识，如果宿主机中两个进程指向的命名空间编号相同，则表示他们同在一个命名空间之下。

![](../../../assets/img/Integrated/容器/docker/1.png)

**CGroups**

CGroups（Control Groups，控制组）机制最早于 2006 年由 Google 提出，目前是 Linux 内核的一种机制，可以实现对任务组（进程组或线程组）使用的物理资源（CPU、内存、I/O等）进行限制和记录，通过多种度量标准为各个容器相对公平地分配资源，以防止资源滥用的情况。

在实际应用中，CGroups 会为每个执行任务创建一个钩子，在任务执行的过程中涉及到资源分配使用时，就会触发钩子上的函数并对相应的资源进行检测，从而对资源进行限制和优先级分配。

CGroups 提供了资源限制（Resource Limitation）、优先级分配（Prioritization）、资源统计（Accounting）、任务控制（Control）四个功能，包含 blkio、cpu、cpuacct、cpuset、devices、freezer、memory、perf_event、net_cls、net_prio、ns、hugetl b等子系统，每种子系统独立地控制一种资源，可分别实现块设备输入/输出限制、CPU 使用控制、生成 CPU 资源使用情况报告、内存使用量限制等功能。几个主要子系统的具体功能如表所示。

| 子系统 	| 功能 |
| - | - |
| blkio       | 为块设备（如磁盘、固态硬盘等物理驱动设备）设定输入/输出限制 |
| cpu         | 通过调度程序控制任务对CPU的使用 |
| cpuacct     | 生成任务对CPU资源使用情况的报告 |
| cpuset      | 为任务分配独立的CPU和内存 |
| devices     | 开启或关闭任务对设备的访问 |
| freezer     | 挂起或恢复任务 |
| memory      | 设定任务对内存的使用量限制，生成任务对内存资源使用情况的报告 |

---

## 安装与使用

- [Docker安装使用](../Linux/Power-Linux.md#docker)

---

## 容器网络管理

- [Docker](../Linux/实验/Docker.md#容器网络管理)

---

## 安全

安全部分内容来自 <sup>[[Docker容器安全性分析](https://www.freebuf.com/articles/system/221319.html)]</sup><sup>

**相关文章**
- [Docker容器安全性分析](https://www.freebuf.com/articles/system/221319.html)
- [Docker安全第一话--镜像安全](https://blog.csdn.net/m0_37552052/article/details/78907296)

---

### 容器虚拟化安全

在传统虚拟化技术架构中，Hypervisor 虚拟机监视器是虚拟机资源的管理与调度模块。而在容器架构中，由于不含有 Hypervisor 层，因此需要依靠操作系统内核层面的相关机制对容器进行安全的资源管理。

**容器资源隔离与限制**

在资源隔离方面，与采用虚拟化技术实现操作系统内核级隔离不同，Docker 通过 Linux 内核的 Namespace 机制实现容器与宿主机之间、容器与容器之间资源的相对独立。通过为各运行容器创建自己的命名空间，保证了容器中进程的运行不会影响到其他容器或宿主机中的进程。

在资源限制方面，Docker 通过 CGroups 实现宿主机中不同容器的资源限制与审计，包括对 CPU、内存、I/O 等物理资源进行均衡化配置，防止单个容器耗尽所有资源造成其他容器或宿主机的拒绝服务，保证所有容器的正常运行。

但是，CGroups 未实现对磁盘存储资源的限制。若宿主机中的某个容器耗尽了宿主机的所有存储空间，那么宿主机中的其他容器无法再进行数据写入。Docker 提供的 --storage-opt=[] 磁盘限额仅支持 Device Mapper 文件系统，而 Linux 系统本身采用的磁盘限额机制是基于用户和文件系统的 quota 技术，难以针对 Docker 容器实现基于进程或目录的磁盘限额。因此，可考虑采用以下方法实现容器的磁盘存储限制：
- 为每个容器创建单独用户，限制每个用户的磁盘使用量；
- 选择 XFS 等支持针对目录进行磁盘使用量限制的文件系统；
- 为每个容器创建单独的虚拟文件系统，具体步骤为创建固定大小的磁盘文件，并从该磁盘文件创建虚拟文件系统，然后将该虚拟文件系统挂载到指定的容器目录。

此外，在默认情况下，容器可以使用主机上的所有内存。可以使用内存限制机制来防止一个容器消耗所有主机资源的拒绝服务攻击，具体可使用使用 -m 或 -memory 参数运行容器。

命令示例
```bash
docker run [运行参数] -memory [内存大小] [容器镜像名或ID] [命令]）
```

**容器能力限制**

Linux 内核能力表示进程所拥有的系统调用权限，决定了程序的系统调用能力。

容器的默认能力包括 CHOWN、DAC_OVERRIDE、FSETID、SETGID、SETUID、SETFCAP、NET_RAW、MKNOD、SYS_REBOOT、SYS_CHROOT、KILL、NET_BIND_SERVICE、AUDIT_WRITE 等等，具体功能如表所示。

| 容器默认能力 	    |  作用
| CHOWN	| 允许任意更改文件 UID 以及 GID |
| DAC_OVERRIDE	    | 允许忽略文件的读、写、执行访问权限检查 |
| FSETID	        | 允许文件修改后保留 setuid/setgid 标志位 |
| SETGID	        | 允许改变进程组 ID |
| SETUID	        | 允许改变进程用户 ID |
| SETFCAP	        | 允许向其他进程转移或删除能力 |
| NET_RAW	        | 允许创建 RAW 和 PACKET 套接字 |
| MKNOD	| 允许使用 mknod 创建指定文件 |
| SYS_REBOOT	    | 允许使用 reboot 或者 kexec_load |
| SYS_CHROOT	    | 允许使用 chroot |
| KILL	| 允许发送信号 |
| NET_BIND_SERVICE  | 允许绑定常用端口号（端口号小于 1024） |
| AUDIT_WRITE	    | 允许审计日志写入 |

如果对容器能力不加以适当限制，可能会存在以下安全隐患：
- 内部因素：在运行 Docker 容器时，如果采用默认的内核功能配置可能会产生容器的隔离问题。
- 外部因素：不必要的内核功能可能导致攻击者通过容器实现对宿主机内核的攻击。

因此，不当的容器能力配置可能会扩大攻击面，增加容器与宿主机面临的安全风险，在执行 docker run 命令运行 Docker 容器时可根据实际需求通过 --cap-add 或 --cap-drop 配置接口对容器的能力进行增删。

命令示例
```bash
docker run --cap-drop ALL --cap-add SYS_TIME ntpd /bin/sh）
```

**强制访问控制**

强制访问控制（Mandatory Access Control, MAC）是指每一个主体（包括用户和程序）和客体都拥有固定的安全标记，主体能否对客体进行相关操作，取决于主体和客体所拥有安全标记的关系。在 Docker 容器应用环境下，可通过强制访问控制机制限制容器的访问资源。Linux 内核的强制访问控制机制包括 SELinux、AppArmor 等。

- SELinux 机制

    SELinux（Security-Enhanced Linux）是 Linux 内核的强制访问控制实现，由美国国家安全局（NSA）发起，用以限制进程的资源访问，即进程仅能访问其任务所需的文件资源。因此，可通过 SELinux 对 Docker 容器的资源访问进行控制。

    在启动 Docker daemon 守护进程时，可通过将 --selinux-enabled 参数设为 true，从而在 Docker 容器中使用SELinux。SELinux 可以使经典的 shocker.c 程序失效，使其无法逃逸出 Docker 容器实现对宿主机资源的访问。

    命令示例
    ```bash
    docker daemon --selinux-enabled = true
    ```

- AppArmor 机制

    与 SELinux 类似，AppArmor（Application Armor，应用程序防护）也是 Linux 的一种强制访问控制机制，其作用是对可执行程序进行目录和文件读写、网络端口访问和读写等权限的控制。

    在 Docker daemon 启动后会在 /etc/apparmor.d/docker 自动创建 AppArmor 的默认配置文件 docker-default，可通过在该默认配置文件中新增访问控制规则的方式对容器进行权限控制，同时可在启动容器时通过 --security-opt 指定其他配置文件。例如，在配置文件中加入一行 deny /etc/hosts rwklx 限制对 /etc/hosts 的获取，同样可使 shocker.c 容器逃逸攻击失效。

    命令示例
    ```bash
    docker run --rm -ti --cap-add=all --security-opt apparmor:docker-default shocker bash
    ```

**Seccomp 机制**

Seccomp（Secure Computing Mode）是 Linux 内核提供的安全特性，可实现应用程序的沙盒机制构建，以白名单或黑名单的方式限制进程能够进行的系统调用范围。

在 Docker 中，可通过为每个容器编写 json 格式的 seccomp profile 实现对容器中进程系统调用的限制。在 seccomp profile 中，可定义以下行为对进程的系统调用做出响应：
```
SCMP_ACT_KILL：当进程进行对应的系统调用时，内核发出 SIGSYS 信号终止该进程，该进程不会接受到这个信号；
SCMP_ACT_TRAP：当进程进行对应的系统调用时，该进程会接收到 SIGSYS 信号，并改变自身行为；
SCMP_ACT_ERRNO：当进程进行对应的系统调用时，系统调用失败，进程会接收到 errno 返回值；
SCMP_ACT_TRACE：当进程进行对应的系统调用时，进程会被跟踪；
SCMP_ACT_ALLOW：允许进程进行对应的系统调用行为。
```

默认情况下，在 Docker 容器的启动过程中会使用默认的 seccomp profile，可使用 security-opt seccomp 选项使用特定的 seccomp profile。

命令示例
```
docker run --rm -it --security-opt seccomp:/path/to/seccomp/profile.json hello-world
```

---

### 容器安全管理

#### 镜像仓库安全

- 内容信任机制

    Docker 的内容信任（Content Trust）机制可保护镜像在镜像仓库与用户之间传输过程中的完整性。目前，Docker 的内容信任机制默认关闭，需要手动开启。内容信任机制启用后，镜像发布者可对镜像进行签名，而镜像使用者可以对镜像签名进行验证。

    具体而言，镜像构建者在通过 docker build 命令运行 Dockerfile 文件前，需要通过手动或脚本方式将 DOCKER_CONTENT_TRUST 环境变量置为1进行启用。在内容信任机制开启后，push、build、create、pull、run 等命令均与内容信任机制绑定，只有通过内容信任验证的镜像才可成功运行这些操作。例如，Dockerfile 中如果包含未签名的基础镜像，将无法成功通过 docker build 进行镜像构建。

    命令示例
    ```
    export DOCKER_CONTENT_TRUST = 1
    ```

- Notary 项目

    Notary 是一个从 Docker 中剥离的独立开源项目，提供数据收集的安全性。Notary 用于发布内容的安全管理，可对发布的内容进行数字签名，并允许用户验证内容的完整性和来源。Notary 的目标是保证服务器与客户端之间使用可信连接进行交互，用于解决互联网内容发布的安全性，并未局限于容器应用。

    在 Docker 容器场景中，Notary 可支持 Docker 内容信任机制。因此，可使用 Notary 构建镜像仓库服务器，实现对容器镜像的签名，对镜像源认证、镜像完整性等安全需求提供更好的支持。

#### 镜像安全扫描

为了保证容器运行的安全性，在从公共镜像仓库获取镜像时需要对镜像进行安全检查，防止存在安全隐患甚至恶意漏洞的镜像运行，从源头端预防安全事故的发生。镜像漏洞扫描工具是一类常用的镜像安全检查辅助工具，可检测出容器镜像中含有的 CVE 漏洞。

针对 Docker 镜像的漏洞扫描，目前已经有许多相关工具与解决方案，包括 Docker Security Scanning、Clair、Anchore、Trivy、Aqua 等等。

**Docker Security Scanning 服务**

Docker Security Scanning 是 Docker 官方推出的不开源镜像漏洞扫描服务，用于检测 Docker Cloud 服务中私有仓库和 Docker Hub 官方仓库中的镜像是否安全。

Docker Security Scanning 包括扫描触发、扫描器、数据库、附加元件框架以及 CVE 漏洞数据库比对等服务。当仓库中有镜像发生更新时，会自动启动漏洞扫描；当 CVE 漏洞数据库发生更新时，也会实时更新镜像漏洞扫描结果。

**Clair 工具**

- https://github.com/quay/clair

Clair 是一款开源的 Docker 镜像漏洞扫描工具。与 Docker Security Scanning 类似，Clair 通过对 Docker 镜像进行静态分析并与公共漏洞数据库关联，得到相应的漏洞分析结果。Clair 主要包括以下模块：
```
Fetcher（获取器）：从公共的 CVE 漏洞源收集漏洞数据；
Detector（检测器）：对镜像的每一个 Layer 进行扫描，提取镜像特征；
Notifier+WebHook（通知钩子）- 当新的漏洞被发现时或者已经存在的漏洞发生改变时通知用户/机器
Databases（数据库）：PostSQL 数据库存储容器中的各个层和 CVE 漏洞；
Worker（主进程） - 每个Post Layer都会启动一个worker进行Layer Detect
```

clair 使用时的辅助工具
- https://github.com/jgsqware/clairctl

**Anchore**

- https://github.com/anchore/anchore-engine

Anchore侧重于对镜像的审计，其有强大的对镜像的解析能力
```
anchore analyze --image test
```

**Trivy 工具**

Trivy 是一个简单而全面的开源容器漏洞扫描程序。Trivy 可检测操作系统软件包（Alpine、RHEL、CentOS等）和应用程序依赖项（Bundler、Composer、npm、yarn等）的漏洞。此外，Trivy 具有较高的易用性，只需安装二进制文件并指定扫描容器的镜像名称即可执行扫描。Trivy 提供了丰富的功能接口，相比于其他容器镜像漏洞扫描工具更适合自动化操作，可更好地满足持续集成的需求。

命令示例
```bash
trivy [镜像名]
```

**veinmind-tools**

- https://github.com/chaitin/veinmind-tools

veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器安全工具集

1. 确保机器上正确安装 docker
    ```bash
    docker info
    ```
2. 安装 veinmind-runner 镜像
    ```bash
    docker pull veinmind/veinmind-runner:latest
    ```
3. 下载 veinmind-runner 平行容器启动脚本
    ```bash
    wget -q https://download.veinmind.tech/scripts/veinmind-runner-parallel-container-run.sh -O run.sh && chmod +x run.sh
    ```
4. 快速扫描本地镜像
    ```bash
    ./run.sh scan-host
    ```

#### 容器逆向分析

分析镜像,提取出镜像的构建过程和镜像构建过程中引用的文件。

- [LanikSJ/dfimage](https://github.com/LanikSJ/dfimage) - Reverse-engineer a Dockerfile from a Docker image.
    ```bash
    alias dfimage="docker run -v /var/run/docker.sock:/var/run/docker.sock --rm alpine/dfimage"
    dfimage [镜像名]
    ```

- [wagoodman/dive](https://github.com/wagoodman/dive) - A tool for exploring each layer in a docker image
    ```bash
    docker pull wagoodman/dive
    docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock wagoodman/dive:latest [镜像名]
    ```

#### 容器运行时监控

为了在系统运维层面保证容器运行的安全性，实现安全风险的即时告警与应急响应，需要对 Docker 容器运行时的各项性能指标进行实时监控。

针对 Docker 容器监控的工具与解决方案包括 docker stats、cAdvisor、Scout、DataDog、Sensu 等等，其中最常见的是 Docker 原生的 docker stats 命令和 Google 的 cAdvisor 开源工具。

**docker stats 命令**

docker stats 是 Docker 自带的容器资源使用统计命令，可用于对宿主机上的 Docker 容器的资源使用情况进行手动监控，具体内容包括容器的基本信息、容器的 CPU 使用率、内存使用率、内存使用量与限制、块设备 I/O 使用量、网络 I/O 使用量、进程数等信息。用户可根据自身需求设置 --format 参数控制 docker stats 命令输出的内容格式。

命令示例
```bash
docker stats [容器名]
```

**cAdvisor 工具**

由于 docker stats 只是简单的容器资源查看命令，其可视化程度不高，同时不支持监控数据的存储。cAdvisor 是由 Google 开源的容器监控工具，优化了docker stats 在可视化展示与数据存储方面的缺陷。

cAdvisor 在宿主机上以容器方式运行，通过挂载在本地卷，可对同一台宿主机上运行的所有容器进行实时监控和性能数据采集，具体包括 CPU 使用情况、内存使用情况、网络吞吐量、文件系统使用情况等信息，并提供本地基础查询界面和 API 接口，方便与其他第三方工具进行搭配使用。cAdvisor 默认将数据缓存在内存中，同时也提供不同的持久化存储后端支持，可将监控数据保存 Google BigQuery、InfluxD B或 Redis 等数据库中。

cAdvisor 基于 Go 语言开发，利用 CGroups 获取容器的资源使用信息，目前已被集成在 Kubernetes 中的 Kubelet 组件里作为默认启动项。

命令示例
```bash
docker run -v /var/run:/var/run:rw -v/sys:/sys:ro -v/var/lib/docker:/var/lib/docker:ro -p8080:8080 -d --name cadvisor google/cadvisor
```

**falco**

- https://github.com/falcosecurity/falco

Falco是一款开源的行为监视器，旨在检测应用程序中的异常活动。 Falco由一系列规则组成，这些规则基于应用程序执行的系统调用来识别可疑行为。 Falco可以应用于容器环境、虚拟化环境、Linux物理主机环境

- 相关文章
    - [Docker安全第二话--安全监控](https://blog.csdn.net/m0_37552052/article/details/78909631)

#### 容器安全审计

- Docker 守护进程审计

    在安全审计方面，对于运行 Docker 容器的宿主机而言，除需对主机 Linux 文件系统等进行审计外，还需对 Docker 守护进程的活动进行审计。由于系统默认不会对 Docker 守护进程进行审计，需要通过主动添加审计规则或修改规则文件进行。

    命令示例
    ```bash
    auditctl -w /usr/bin/docker -k docker
    或
    修改 /etc/audit/audit.rules 文件
    ```

- Docker 相关文件目录审计

    除 Docker 守护进程之外，还需对与 Docker 的运行相关的文件和目录进行审计，同样需要通过命令行添加审计规则或修改规则配置文件，具体文件和目录如表所示。

    | 需要审计的文件或目录 	| 备注 |
    | - | - |
    | /var/lib/docker	            | 包含有关容器的所有信息 |
    | /etc/docker	                | 包含 Docker 守护进程和客户端 TLS 通信的密钥和证书 |
    | docker.service	            | Docker 守护进程运行参数配置文件 |
    | docker.socket	                | 守护进程运行 socket |
    | /etc/default/docker	        | 支持 Docker 守护进程各种参数 |
    | /etc/default/daemon.json	    | 支持 Docker 守护进程各种参数 |
    | /usr/bin/docker-containerd	| Docker 可用 containerd 生成容器 |
    | /usr/bin/docker-runc	        | Docker 可用 runC 生成容器 |

    Docker 公司与美国互联网安全中心（CIS）联合制定了 Docker 最佳安全实践 CIS Docker Benchmark，目前最新版本为 1.2.0。为了帮助 Docker 用户对其部署的容器环境进行安全检查，Docker 官方提供了 Docker Bench for Security 安全配置检查脚本工具 docker-bench-security，其检查依据便是 CIS 制定的 Docker 最佳安全实践。

---

### 容器网络安全

**容器间流量限制**

由于 Docker 容器默认的网桥模式不会对网络流量进行控制和限制，为了防止潜在的网络 DoS 攻击风险，需要根据实际需求对网络流量进行相应的配置。

- 完全禁止容器间通信

    在特定的应用场景中，如果宿主机中的所有容器无需在三层或四层进行网络通信交互，可通过将 Docker daemon 的 --icc 参数设为 false 以禁止容器与容器间的通信。

    命令示例
    ```
    dockerd --icc = false
    ```

- 容器间流量控制

    在存在多租户的容器云环境中，可能存在单个容器占用大量宿主机物理网卡抢占其他容器带宽的情况。为了保证容器之间的正常通信，同时避免异常流量造成网络 DoS 攻击等后果，需要对容器之间的通信流量进行一定的限制。

    由于 Docker 通过创建虚拟网卡对（eth0 和 veth*）将容器与虚拟网桥 docker0 连接，而容器之间的通信需要经由虚拟网卡对 eth0 和 veth* 通过网桥连接，因此，可采用 Linux 的流量控制模块 traffic controller 对容器网络进行流量限制。

    traffic controller的原理是建立数据包队列并制定发送规则，实现流量限制与调度的功能。为了在一定程度上减轻容器间的 DoS 攻击的危害，可将 traffic controller 的 dev 设置为宿主机中与各容器连接的 veth* 虚拟网卡，以此进行宿主机上容器间流量限制。

**网桥模式下的网络访问控制**

在默认的网桥连接模式中，连接在同一个网桥的两个容器可以进行直接相互访问。因此，为了实现网络访问控制，可按需配置网络访问控制机制和策略。

- 为容器创建不同的桥接网络

    为了实现容器间的网络隔离，可将容器放在不同的桥接网络中。当在 Docker 中使用 docker network create 命令创建新的桥接网络时，会在 iptables 中的 DOCKER-ISOLATION 新增 DROP 丢弃规则，阻断与其他网络之间的通信流量，实现容器网络之间隔离的目的。

    命令示例
    ```
    docker network create --subnet 102.102.0.0/24 test
    ```

- 基于白名单策略的网络访问控制

    为了保证容器间的网络安全，可默认禁止容器间的通信，然后按需设置网络访问控制规则。

    具体而言，在同一虚拟网络内，不同 Docker 容器之间的网络访问可通过 iptables 进行控制。在将 Docker daemon 的 --icc 参数设为 false后，iptables 的 FORWARD 链策略为默认全部丢弃。此时，可采用白名单策略实现网络访问控制，即根据实际需要在 iptables 中添加访问控制策略，以最小化策略减小攻击面。

**集群模式下的网络访问控制**

与通过 OpenStack 建立的虚拟化集群通过 VLAN 对不同租户进行子网隔离不同，基于 Overlay 网络的容器集群在同一主机内相同子网中的不同容器之间默认可以直接访问。

如需控制宿主机外部到内部容器应用的访问，可通过在宿主机 iptables 中的 DOCKER-INGRESS 链手动添加 ACL 访问控制规则以控制宿主机的 eth0 到容器的访问，或者在宿主机外部部署防火墙等方法实现。

然而，在大型的容器云环境中，由于存在频繁的微服务动态变化更新，通过手动的方式配置 iptables 或更新防火墙是不现实的。因此，可通过微分段（Micro-Segmentation）实现面向容器云环境中的容器防火墙。微分段是一种细粒度的网络分段隔离机制，与传统的以网络地址为基本单位的网络分段机制不同，微分段可以以单个容器、同网段容器、容器应用为粒度实现分段隔离，并通过容器防火墙对实现微分段间的网络访问控制。

### 更多内容

- [Docker 安全](../../Security/RedTeam/软件服务安全/实验/Docker.md)
