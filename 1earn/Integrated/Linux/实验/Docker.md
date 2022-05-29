# Docker

> 笔记大部分内容来自 [docker_practice](https://github.com/yeasy/docker_practice) ,仅做内容排版修改
> 部分内容由 [xidaner](https://github.com/xidaner) 提供,仅做部分内容排版修改

---

**常见报错**
- Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
  ```bash
  systemctl daemon-reload
  service docker restart
  ```

- docker timeout
  ```bash
  echo "nameserver 8.8.8.8" > /etc/resolv.conf
  sudo systemctl daemon-reload
  sudo systemctl restart docker
  ```

- 容器 "Exited (0)" 自动退出
  - 有时镜像内置的执行命令无法正确执行，于是容器就 Exited 了
  - 尝试在 docker run 命令最后加上或删除 /bin/bash 选项

---

## 镜像

**镜像管理**

```bash
docker search [keyword]                           # 搜索镜像
docker image ls                                   # 查看已下载的镜像列表
docker image rm [docker_image_id]                 # 删除本地的 docker 镜像
```

**镜像体积**

docker image ls 标识的所占用空间和在 Docker Hub 上看到的镜像大小不同。

比如，ubuntu:18.04 镜像大小，显示是 63.3MB，但是在 Docker Hub 显示的却是 25.47 MB。这是因为 Docker Hub 中显示的体积是压缩后的体积。在镜像下载和上传过程中镜像是保持着压缩状态的，因此 Docker Hub 所显示的大小是网络传输中更关心的流量大小。而 docker image ls 显示的是镜像下载到本地后，展开的大小，准确说，是展开后的各层所占空间的总和，因为镜像到本地后，查看空间的时候，更关心的是本地磁盘空间占用的大小。

另外,docker image ls 列表中的镜像体积总和并非是所有镜像实际硬盘消耗。由于 Docker 镜像是多层存储结构，并且可以继承、复用，因此不同镜像可能会因为使用相同的基础镜像，从而拥有共同的层。由于 Docker 使用 Union FS，相同的层只需要保存一份即可，因此实际镜像硬盘占用空间很可能要比这个列表镜像大小的总和要小的多。

```bash
docker system df        # 查看镜像、容器、数据卷所占用的空间
```

**虚悬镜像**

镜像列表中，可能存在一个特殊的镜像，这个镜像既没有仓库名，也没有标签，均为 `<none>`。

这种镜像原本是有镜像名和标签的，比如原来为 mongo:3.2，随着官方镜像维护，发布了新版本后，重新 docker pull mongo:3.2 时，mongo:3.2 这个镜像名被转移到了新下载的镜像身上，而旧的镜像上的这个名称则被取消，从而成为了 <none>。除了 docker pull 可能导致这种情况，docker build 也同样可以导致这种现象。由于新旧镜像同名，旧镜像名称被取消，从而出现仓库名、标签均为 <none> 的镜像。这类无标签镜像也被称为 虚悬镜像(dangling image) ，可以用下面的命令专门显示这类镜像：
```bash
docker image ls -f dangling=true
```

一般来说，虚悬镜像已经失去了存在的价值，是可以随意删除的，可以用下面的命令删除。
```bash
docker image prune
```

**中间层镜像**

为了加速镜像构建、重复利用资源，Docker 会利用 中间层镜像。所以在使用一段时间后，可能会看到一些依赖的中间层镜像。默认的 docker image ls 列表中只会显示顶层镜像，如果希望显示包括中间层镜像在内的所有镜像的话，需要加 -a 参数。
```bash
docker image ls -a
```

这样会看到很多无标签的镜像，与之前的虚悬镜像不同，这些无标签的镜像很多都是中间层镜像，是其它镜像所依赖的镜像。这些无标签镜像不应该删除，否则会导致上层镜像因为依赖丢失而出错。实际上，这些镜像也没必要删除，因为之前说过，相同的层只会存一遍，而这些镜像是别的镜像的依赖，因此并不会因为它们被列出来而多存了一份，无论如何你也会需要它们。只要删除那些依赖它们的镜像后，这些依赖的中间层镜像也会被连带删除。

### commit 编辑镜像

```bash
docker run --name web1 -d -p 80:80 nginx
```

这条命令会用 nginx 镜像启动一个容器，命名为 web1，并且映射了 80 端口，这样我们可以用浏览器去访问这个 nginx 服务器。如果是在本机运行的 Docker，那么可以直接访问：http://localhost ，如果是在虚拟机、云服务器上安装的 Docker，则需要将 localhost 换为虚拟机地址或者实际云服务器地址。

直接用浏览器访问的话，我们会看到默认的 Nginx 欢迎页面。

我们修改这个默认的页面，然后进行保存，首先进入容器
```bash
docker exec -it web1 /bin/bash

curl 127.0.0.1
echo '<h1>Just test!</h1>' > /usr/share/nginx/html/index.html
curl 127.0.0.1
exit
```

我们修改了容器的文件，也就是改动了容器的存储层。我们可以通过 docker diff 命令看到具体的改动。
```
docker diff web1
```

当运行一个容器的时候（如果不使用卷的话），任何文件修改都会被记录于容器存储层里。而 Docker 提供了一个 docker commit 命令，可以将容器的存储层保存下来成为镜像。

就是在原有镜像的基础上，再叠加上容器的存储层，并构成新的镜像。以后我们运行这个新镜像的时候，就会拥有原有容器最后的文件变化。

用下面的命令将容器保存为镜像
```bash
docker commit --author "zhangsan" --message "修改了默认网页" web1 nginx:v2
```

现在可以在 docker image ls 中看到这个修改过的镜像：
```bash
docker image ls nginx
```

可以用 docker history 具体查看镜像内的历史记录，如果比较 nginx:latest 的历史记录，我们会发现新增了我们刚刚提交的这一层。
```bash
root@debian-gnu-linux-10:~# docker history 0c245efcceb8
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
0c245efcceb8   50 seconds ago   nginx -g daemon off;                            1.25kB    修改了默认网页
eeb9db34b331   2 months ago     /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
<missing>      2 months ago     /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B
<missing>      2 months ago     /bin/sh -c #(nop)  EXPOSE 80                    0B
<missing>      2 months ago     /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B
<missing>      2 months ago     /bin/sh -c #(nop) COPY file:09a214a3e07c919a…   4.61kB
<missing>      2 months ago     /bin/sh -c #(nop) COPY file:0fd5fca330dcd6a7…   1.04kB
<missing>      2 months ago     /bin/sh -c #(nop) COPY file:0b866ff3fc1ef5b0…   1.96kB
<missing>      2 months ago     /bin/sh -c #(nop) COPY file:65504f71f5855ca0…   1.2kB
...

root@debian-gnu-linux-10:~# docker history eeb9db34b331
IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
eeb9db34b331   2 months ago   /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
<missing>      2 months ago   /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B
<missing>      2 months ago   /bin/sh -c #(nop)  EXPOSE 80                    0B
<missing>      2 months ago   /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B
<missing>      2 months ago   /bin/sh -c #(nop) COPY file:09a214a3e07c919a…   4.61kB
<missing>      2 months ago   /bin/sh -c #(nop) COPY file:0fd5fca330dcd6a7…   1.04kB
<missing>      2 months ago   /bin/sh -c #(nop) COPY file:0b866ff3fc1ef5b0…   1.96kB
<missing>      2 months ago   /bin/sh -c #(nop) COPY file:65504f71f5855ca0…   1.2kB
...
```

新的镜像定制好后，我们可以来运行这个镜像。
```
docker run --name web2 -d -p 81:80 nginx:v2

docker exec -it web2 /bin/bash

curl 127.0.0.1
```

### Dockerfile

镜像的定制实际上就是定制每一层所添加的配置、文件。如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像，那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。这个脚本就是 Dockerfile。

Dockerfile 是一个文本文件，其内包含了一条条的 指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。

还以之前修改 nginx 镜像为例，这次我们使用 Dockerfile 来定制。

在一个空白目录中，建立一个文本文件，并命名为 Dockerfile：
```bash
mkdir mynginx && cd mynginx
vim Dockerfile

FROM nginx
RUN echo '<h1>Just test!</h1>' > /usr/share/nginx/html/index.html
```

**FROM 指定基础镜像**

所谓定制镜像，那一定是以一个镜像为基础，在其上进行定制。就像我们之前运行了一个 nginx 镜像的容器，再进行修改一样，基础镜像是必须指定的。而 FROM 就是指定 基础镜像，因此一个 Dockerfile 中 FROM 是必备的指令，并且必须是第一条指令。

在 dockerhub 上有非常多的高质量的官方镜像，有可以直接拿来使用的服务类的镜像，如 nginx、tomcat、php 等；也有一些方便开发、构建、运行各种语言应用的镜像，如 python、go 等。可以在其中寻找一个最符合我们最终目标的镜像为基础镜像进行定制。

如果没有找到对应服务的镜像，官方镜像中还提供了一些更为基础的操作系统镜像，如 ubuntu、alpine 等，这些操作系统的软件库为我们提供了更广阔的扩展空间。除了选择现有镜像为基础镜像外，Docker 还存在一个特殊的镜像，名为 scratch。这个镜像是虚拟的概念，并不实际存在，它表示一个空白的镜像。

如果你以 scratch 为基础镜像的话，意味着你不以任何镜像为基础，接下来所写的指令将作为镜像第一层开始存在。

不以任何系统为基础，直接将可执行文件复制进镜像的做法并不罕见，对于 Linux 下静态编译的程序来说，并不需要有操作系统提供运行时支持，所需的一切库都已经在可执行文件里了，因此直接 FROM scratch 会让镜像体积更加小巧。使用 Go 语言 开发的应用很多会使用这种方式来制作镜像，这也是为什么有人认为 Go 是特别适合容器微服务架构的语言的原因之一。

**RUN 执行命令**

RUN 指令是用来执行命令行命令的。由于命令行的强大能力，RUN 指令在定制镜像时是最常用的指令之一。其格式有两种：
- shell 格式：RUN <命令>，就像直接在命令行中输入的命令一样。刚才写的 Dockerfile 中的 RUN 指令就是这种格式。
    ```dockerfile
    RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
    ```

- exec 格式：RUN ["可执行文件", "参数1", "参数2"]，这更像是函数调用中的格式。既然 RUN 就像 Shell 脚本一样可以执行命令，那么我们是否就可以像 Shell 脚本一样把每个命令对应一个 RUN 呢？比如这样：
    ```dockerfile
    FROM debian:stretch

    RUN apt-get update
    RUN apt-get install -y gcc libc6-dev make wget
    RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
    RUN mkdir -p /usr/src/redis
    RUN tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1
    RUN make -C /usr/src/redis
    RUN make -C /usr/src/redis install
    ```

    Dockerfile 中每一个指令都会建立一层，RUN 也不例外。每一个 RUN 的行为，就和刚才我们手工建立镜像的过程一样：新建立一层，在其上执行这些命令，执行结束后，commit 这一层的修改，构成新的镜像。

    而上面的这种写法，创建了 7 层镜像。这是完全没有意义的，而且很多运行时不需要的东西，都被装进了镜像里，比如编译环境、更新的软件包等等。结果就是产生非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。 这是很多初学 Docker 的人常犯的一个错误。

    Union FS 是有最大层数限制的，比如 AUFS，曾经是最大不得超过 42 层，现在是不得超过 127 层。

正确的写法应该是这样
```dockerfile
FROM debian:stretch

RUN set -x; buildDeps='gcc libc6-dev make wget' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
    && mkdir -p /usr/src/redis \
    && tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
    && make -C /usr/src/redis \
    && make -C /usr/src/redis install \
    && rm -rf /var/lib/apt/lists/* \
    && rm redis.tar.gz \
    && rm -r /usr/src/redis \
    && apt-get purge -y --auto-remove $buildDeps
```

仅仅使用一个 RUN 指令，并使用 && 将各个所需命令串联起来。将之前的 7 层，简化为了 1 层。在撰写 Dockerfile 的时候，要经常提醒自己，这并不是在写 Shell 脚本，而是在定义每一层该如何构建。

并且，这里为了格式化还进行了换行。Dockerfile 支持 Shell 类的行尾添加 \ 的命令换行方式，以及行首 # 进行注释的格式。良好的格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。

此外，还可以看到这一组命令的最后添加了清理工作的命令，删除了为了编译构建所需要的软件，清理了所有下载、展开的文件，并且还清理了 apt 缓存文件。这是很重要的一步，我们之前说过，镜像是多层存储，每一层的东西并不会在下一层被删除，会一直跟随着镜像。因此镜像构建时，一定要确保每一层只添加真正需要添加的东西，任何无关的东西都应该清理掉。

现在到之前 nginx 的 Dockerfile 文件所在目录执行 docker build
```
root@debian-gnu-linux-10:~/mynginx# docker build -t nginx:v3 .
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM nginx
 ---> eeb9db34b331
Step 2/2 : RUN echo '<h1>Just test!</h1>' > /usr/share/nginx/html/index.html
 ---> Running in b51eb821c115
Removing intermediate container b51eb821c115
 ---> 2109677c2aef
Successfully built 2109677c2aef
Successfully tagged nginx:v3
```

从命令的输出结果中，我们可以清晰的看到镜像的构建过程。在 Step 2 中，如同我们之前所说的那样，RUN 指令启动了一个容器 b51eb821c115 ，执行了所要求的命令，并最后提交了这一层 2109677c2aef ，随后删除了所用到的这个容器 b51eb821c115

在这里我们指定了最终镜像的名称 -t nginx:v3，构建成功后，我们可以像之前运行 nginx:v2 那样来运行这个镜像，其结果会和 nginx:v2 一样。

**镜像构建上下文（Context）**

docker build 命令最后有一个 . 表示当前目录，而 Dockerfile 就在当前目录，因此不少初学者以为这个路径是在指定 Dockerfile 所在路径，这么理解其实是不准确的。如果对应上面的命令格式，你可能会发现，这是在指定上下文路径。那么什么是上下文呢？

Docker 在运行时分为 Docker 引擎（也就是服务端守护进程）和客户端工具。Docker 的引擎提供了一组 REST API，被称为 Docker Remote API，而如 docker 命令这样的客户端工具，则是通过这组 API 与 Docker 引擎交互，从而完成各种功能。因此，虽然表面上我们好像是在本机执行各种 docker 功能，但实际上，一切都是使用的远程调用形式在服务端（Docker 引擎）完成。也因为这种 C/S 设计，让我们操作远程服务器的 Docker 引擎变得轻而易举。

当我们进行镜像构建的时候，并非所有定制都会通过 RUN 指令完成，经常会需要将一些本地文件复制进镜像，比如通过 COPY 指令、ADD 指令等。而 docker build 命令构建镜像，其实并非在本地构建，而是在服务端，也就是 Docker 引擎中构建的。那么在这种客户端/服务端的架构中，如何才能让服务端获得本地文件呢？

这就引入了上下文的概念。当构建的时候，用户会指定构建镜像上下文的路径，docker build 命令得知这个路径后，会将路径下的所有内容打包，然后上传给 Docker 引擎。这样 Docker 引擎收到这个上下文包后，展开就会获得构建镜像所需的一切文件。

如果在 Dockerfile 中这么写：
```dockerfile
COPY ./package.json /app/
```

这并不是要复制执行 docker build 命令所在的目录下的 package.json，也不是复制 Dockerfile 所在目录下的 package.json，而是复制 上下文（context） 目录下的 package.json。

因此，COPY 这类指令中的源文件的路径都是相对路径。这也是初学者经常会问的为什么 `COPY ../package.json /app` 或者 `COPY /opt/xxxx /app` 无法工作的原因，因为这些路径已经超出了上下文的范围，Docker 引擎无法获得这些位置的文件。如果真的需要那些文件，应该将它们复制到上下文目录中去。

现在就可以理解刚才的命令 docker build -t nginx:v3 . 中的这个 .，实际上是在指定上下文的目录，docker build 命令会将该目录下的内容打包交给 Docker 引擎以帮助构建镜像。

理解构建上下文对于镜像构建是很重要的，避免犯一些不应该的错误。比如有些初学者在发现 `COPY /opt/xxxx /app` 不工作后，于是干脆将 Dockerfile 放到了硬盘根目录去构建，结果发现 docker build 执行后，在发送一个几十 GB 的东西，极为缓慢而且很容易构建失败。那是因为这种做法是在让 docker build 打包整个硬盘，这显然是使用错误。

一般来说，应该会将 Dockerfile 置于一个空目录下，或者项目根目录下。如果该目录下没有所需文件，那么应该把所需文件复制一份过来。如果目录下有些东西确实不希望构建时传给 Docker 引擎，那么可以用 `.gitignore` 一样的语法写一个 `.dockerignore`，该文件是用于剔除不需要作为上下文传递给 Docker 引擎的。

那么为什么会有人误以为 . 是指定 Dockerfile 所在目录呢？这是因为在默认情况下，如果不额外指定 Dockerfile 的话，会将上下文目录下的名为 Dockerfile 的文件作为 Dockerfile。

这只是默认行为，实际上 Dockerfile 的文件名并不要求必须为 Dockerfile，而且并不要求必须位于上下文目录中，比如可以用 `-f ../Dockerfile.php` 参数指定某个文件作为 Dockerfile。一般都会默认使用的文件名 Dockerfile，以及会将其置于镜像构建上下文目录中。

**直接用 Git repo 进行构建**

```bash
docker build -t hello-world https://github.com/docker-library/hello-world.git#master:amd64/hello-world
```

**用给定的 tar 压缩包构建**

```bash
docker build http://server/context.tar.gz
```

**从标准输入中读取 Dockerfile 进行构建**

如果标准输入传入的是文本文件，则将其视为 Dockerfile，并开始构建。这种形式由于直接从标准输入中读取 Dockerfile 的内容，它没有上下文，因此不可以像其他方法那样可以将本地文件 COPY 进镜像之类的事情。

```bash
docker build - < Dockerfile
# 或
cat Dockerfile | docker build -
```

**从标准输入中读取上下文压缩包进行构建**

如果发现标准输入的文件格式是 gzip、bzip2 以及 xz 的话，将会使其为上下文压缩包，直接将其展开，将里面视为上下文，并开始构建。

```bash
docker build - < context.tar.gz
```

---

## 导出和导入

**容器导出**

如果要导出本地某个容器，可以使用 docker export 命令。

```bash
docker container ls -a
docker export xxx > ubuntu.tar
```

这样将导出容器快照到本地文件。

```bash
# 当前目录的 Dockerfile 创建镜像
docker build -t <image-name>:<tag> .

# 指定文件构建镜像
docker build -f /path/to/a/Dockerfile -t <image-name>:<tag> .

# 将镜像保存 tar 包
docker save -o image-name.tar <image-name>:<tag>

# 导入 tar 镜像
docker load --input image-name.tar

```

**导入容器快照**

可以使用 docker import 从容器快照文件中再导入为镜像，例如
```bash
cat ubuntu.tar | docker import - test/ubuntu:v1.0
```

此外，也可以通过指定 URL 或者某个目录来导入，例如
```bash
docker import http://example.com/exampleimage.tgz example/imagerepo
```

用户既可以使用 docker load 来导入镜像存储文件到本地镜像库，也可以使用 docker import 来导入一个容器快照到本地镜像库。这两者的区别在于容器快照文件将丢弃所有的历史记录和元数据信息（即仅保存容器当时的快照状态），而镜像存储文件将保存完整记录，体积也要大。此外，从容器快照文件导入时可以重新指定标签等元数据信息。

---

## Docker Hub

- https://hub.docker.com

**登陆**

执行 docker login 命令交互式的输入用户名及密码来完成在命令行界面登录 Docker Hub。
```bash
docker login
```
通过 docker logout 退出登录

**拉取镜像**

可以通过 docker search 命令来查找官方仓库中的镜像，并利用 docker pull 命令来将它下载到本地。

根据是否是官方提供，可将镜像分为两类。

一种是类似 centos 这样的镜像，被称为基础镜像或根镜像。这些基础镜像由 Docker 公司创建、验证、支持、提供。这样的镜像往往使用单个单词作为名字。

还有一种类型，比如 ansible/centos7-ansible 镜像，它是由 Docker Hub 的注册用户创建并维护的，往往带有用户名称前缀。可以通过前缀 username/ 来指定使用某个用户提供的镜像，比如 ansible 用户。

**推送镜像**

用户也可以在登录后通过 docker push 命令来将自己的镜像推送到 Docker Hub。

```bash
# 登录 Docker Hub
docker login

# 容器打包镜像
docker commit -a "作者" -m "备注" 容器ID <image-name>:<tag>

# 将容器打包成规范的镜像
docker commit -m <exiting-Container> <hub-user>/<repo-name>[:<tag>]

# 上传推送镜像到公共仓库
docker push <hub-user>/<repo-name>:<tag>
docker push xxxx/ubuntu:18.04

# 报错 : denied: requested access to the resource is denied
docker tag nginx zhang3/nginx:latest
docker push zhang3/nginx:latest
# tag 修改为 zhang3/xxxxx 就 push 成功。需要注意的是 zhang3 需要是本人的 docker 用户名。
```

---

## docker remote api

> ⚠️ 注意: 监听 0.0.0.0 有安全风险,生产环境下请监听 127.0.0.1

```bash
vim /usr/lib/systemd/system/docker.service

ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock

systemctl daemon-reload
systemctl restart docker
```

---

## 容器网络管理

### 原生网络

Docker 安装完成存在多种原生网络模式 bridge、host、none。

**bridge 模式（桥接模式）**

> -net=bridge(默认)

这是dokcer网络的默认设置，为容器创建独立的网络命名空间，容器具有独立的网卡等所有单独的网络栈，是最常用的使用方式。

在 docker run 启动容器的时候，如果不加 -net 参数，就默认采用这种网络模式。

安装完 docker，系统会自动添加一个供 docker 使用的网桥 docker0，我们创建一个新的容器时，容器通过 DHCP 获取一个与 docker0 同网段的 IP 地址，并默认连接到 docker0 网桥，以此实现容器与宿主机的网络互通。

当执行 docker run 加入 -p 参数是，实际是在 iptables 中加入了对应的 DNAT 端口转发规则。

**host 模式（主机模式）**

> -net=host

host 模式的容器跟宿主机共用一个 namespace，拥有一样的 IP 和路由，因此容器内的服务端口不能跟宿主机相同。

这个模式下创建出来的容器，直接使用容器宿主机的网络命名空间。将不拥有自己独立的Network Namespace，即没有独立的网络环境。它使用宿主机的ip和端口。这种模式主要适用于管理员希望以docker方式管理服务器。

**none 模式（禁用网络模式）**

> -net=none

为容器创建独立网络命名空间，但不为它做任何网络配置，容器中只有lo，用户可以在此基础上，对容器网络做任意定制。这个模式下，dokcer不为容器进行任何网络配置。需要我们自己为容器添加网卡，配置IP。因此，若想使用pipework配置docker容器的ip地址，必须要在none模式下才可以。

**其他容器模式（即container模式，join模式）**

-net=container:NAME_or_ID 与host模式类似，只是容器将与指定的容器共享网络命名空间。这个模式就是指定一个已有的容器，共享该容器的IP和端口。除了网络方面两个容器共享，其他的如文件系统，进程等还是隔离开的。

**用户自定义**

docker 1.9版本以后新增的特性，允许容器使用第三方的网络实现或者创建单独的bridge网络，提供网络隔离能力。

### 外部访问容器

容器中可以运行一些网络应用，要让外部也可以访问这些应用，可以通过 -P 或 -p 参数来指定端口映射。

当使用 -P 标记时，Docker 会随机映射一个端口到内部容器开放的网络端口。

> ⚠️ 注意 -p 标记可以多次使用来绑定多个端口

使用 docker container ls 可以看到,端口映射情况

可以通过 docker logs 命令来查看访问记录
```
docker logs xxx
```

-p 则可以指定要映射的端口，并且，在一个指定端口上只可以绑定一个容器。支持的格式有 ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort。

**映射所有接口地址**

使用 hostPort:containerPort 格式本地的 80 端口映射到容器的 80 端口，可以执行
```bash
docker run -d -p 80:80 nginx:alpine
```

此时默认会绑定本地所有接口上的所有地址。

**映射到指定地址的指定端口**

可以使用 ip:hostPort:containerPort 格式指定映射使用一个特定地址，比如 localhost 地址 127.0.0.1
```bash
docker run -d -p 127.0.0.1:80:80 nginx:alpine
```

**映射到指定地址的任意端口**

使用 ip::containerPort 绑定 localhost 的任意端口到容器的 80 端口，本地主机会自动分配一个端口。
```bash
docker run -d -p 127.0.0.1::80 nginx:alpine
```

还可以使用 udp 标记来指定 udp 端口
```bash
docker run -d -p 127.0.0.1:80:80/udp nginx:alpine
```

**查看映射端口配置**

使用 docker port 来查看当前映射的端口配置，也可以查看到绑定的地址
```bash
docker port xxxx 80
```

### 查看容器的ip地址

```bash
# 进入容器后
cat /etc/hosts
```

```bash
# 在宿主机
docker inspect <container id> | jq .[].NetworkSettings.Networks
# 或
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-ID>
# 或
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
```

### 容器互联

新创建的容器和已经存在的一个容器共享一个 Network Namespace，而不是和宿主机共享。新创建的容器不会创建自己的网卡，配置自己的 IP，而是和一个指定的容器共享 IP、端口范围等。同样，两个容器除了网络方面，其他的如文件系统、进程列表等还是隔离的。两个容器的进程可以通过lo网卡设备通信。

```bash
docker network ls

# 新建虚拟网络
docker network create -d bridge demo-net
# -d 参数指定 Docker 网络类型，有 bridge overlay。其中 overlay 网络类型用于 Swarm mode

# 第二个例子
docker run -itd --name test1 --network demo-net alpine
docker run -itd --name test2 --network demo-net alpine

# 分别进入容器，能够互相ping通
docker exec -it test1 /bin/bash
docker exec -it test2 /bin/bash
```

### 自定义IP

```bash
# 用下面的命令创建docker网桥
docker network create -d bridge -o com.docker.network.bridge.name='demo-net2' --subnet=172.10.200.0/24 --ip-range=172.10.200.0/24 --gateway=172.10.200.1 demo-net2

# 运行容器
docker run -itd --name test0 --network demo-net2 alpine
```

### 容器dns配置

```bash
# vi /etc/docker/daemon.json 设置所有容器的DNS
# 这样容器就可以共享这里的DNS配置，解析域名了。
"dns": [
  "223.5.5.5",
  "8.8.8.8"
]

# 单独指定容器DNS
docker run -it --rm --dns=223.5.5.5 --dns-search=test.com bmc/opensuse15.2:dev
```

如果在容器启动时没有指定 --dns/--dns-search 两个参数，Docker 会默认用主机上的 /etc/resolv.conf 来配置容器。

---

## 案例

### 推荐的镜像

**BusyBox**

BusyBox 是一个集成了一百多个最常用 Linux 命令和工具（如 cat、echo、grep、mount、telnet 等）的精简工具箱，它只需要几 MB 的大小，很方便进行各种快速验证，被誉为“Linux 系统的瑞士军刀”。

BusyBox 可运行于多款 POSIX 环境的操作系统中，如 Linux（包括 Android）、Hurd、FreeBSD 等。

一般是 1～3M 的大小

```bash
docker pull busybox:latest
docker image ls
```

**Alpine**

Alpine 操作系统是一个面向安全的轻型 Linux 发行版。它不同于通常 Linux 发行版，Alpine 采用了 musl libc 和 busybox 以减小系统的体积和运行时资源消耗，但功能上比 busybox 又完善的多，因此得到开源社区越来越多的青睐。在保持瘦身的同时，Alpine 还提供了自己的包管理工具 apk，可以通过 https://pkgs.alpinelinux.org/packages 网站上查询包信息，也可以直接通过 apk 命令直接查询和安装各种软件。

Alpine 由非商业组织维护的，支持广泛场景的 Linux发行版，它特别为资深/重度Linux用户而优化，关注安全，性能和资源效能。Alpine 镜像可以适用于更多常用场景，并且是一个优秀的可以适用于生产的基础系统/环境。

Alpine Docker 镜像也继承了 Alpine Linux 发行版的这些优势。相比于其他 Docker 镜像，它的容量非常小，仅仅只有 5 MB 左右（对比 Ubuntu 系列镜像接近 200 MB），且拥有非常友好的包管理机制。官方镜像来自 docker-alpine 项目。
目前 Docker 官方已开始推荐使用 Alpine 替代之前的 Ubuntu 做为基础镜像环境。这样会带来多个好处。包括镜像下载速度加快，镜像安全性提高，主机之间的切换更方便，占用更少磁盘空间等。

一般是 5～6M 的大小

```bash
docker pull alpine:latest
docker image ls
```

由于镜像很小，下载时间往往很短，读者可以直接使用 docker run 指令直接运行一个 Alpine 容器，并指定运行的 Linux 指令，例如：
```bash
docker run alpine echo '123'
```

如果使用 Alpine 镜像替换 Ubuntu 基础镜像，安装软件包时需要用 apk 包管理器替换 apt 工具，如
```bash
apk add --no-cache <package>
```

Alpine 中软件安装包的名字可能会与其他发行版有所不同，可以在 https://pkgs.alpinelinux.org/packages 网站搜索并确定安装包名称。如果需要的安装包不在主索引内，但是在测试或社区索引中。那么可以按照以下方法使用这些安装包。
```bash
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
apk --update add --no-cache <package>
```

由于在国内访问 apk 仓库较缓慢，建议在使用 apk 之前先替换仓库地址为国内镜像。
```bash
sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories
apk add --no-cache <package>
```

**Debian**

Debian 是由 GPL 和其他自由软件许可协议授权的自由软件组成的操作系统，由 Debian 计划（Debian Project） 组织维护。Debian 计划 是一个独立的、分散的组织，由 3000 人志愿者组成，接受世界多个非盈利组织的资金支持，Software in the Public Interest 提供支持并持有商标作为保护机构。Debian 以其坚守 Unix 和自由软件的精神，以及其给予用户的众多选择而闻名。现时 Debian 包括了超过 25,000 个软件包并支持 12 个计算机系统结构。

Debian 作为一个大的系统组织框架，其下有多种不同操作系统核心的分支计划，主要为采用 Linux 核心的 Debian GNU/Linux 系统，其他还有采用 GNU Hurd 核心的 Debian GNU/Hurd 系统、采用 FreeBSD 核心的 Debian GNU/kFreeBSD 系统，以及采用 NetBSD 核心的 Debian GNU/NetBSD 系统。甚至还有利用 Debian 的系统架构和工具，采用 OpenSolaris 核心构建而成的 Nexenta OS 系统。在这些 Debian 系统中，以采用 Linux 核心的 Debian GNU/Linux 最为著名。

```bash
docker pull debian:latest
docker image ls
docker run -it debian bash
```

**Ubuntu**

Ubuntu 是一个以桌面应用为主的 GNU/Linux 操作系统。Ubuntu 基于 Debian 发行版和 GNOME/Unity 桌面环境，与 Debian 的不同在于它每 6 个月会发布一个新版本，每 2 年推出一个长期支持 （Long Term Support，LTS） 版本，一般支持 3 年时间。

```bash
docker pull ubuntu:18.04
docker image ls
docker run -ti ubuntu:18.04 /bin/bash
```

**CentOS**

CentOS（Community Enterprise Operating System，中文意思是：社区企业操作系统），它是基于 Red Hat Enterprise Linux 源代码编译而成。由于 CentOS 与 Redhat Linux 源于相同的代码基础，所以很多成本敏感且需要高稳定性的公司就使用 CentOS 来替代商业版 Red Hat Enterprise Linux。CentOS 自身不包含闭源软件。

```bash
docker pull centos:7
docker image ls
docker run -it centos:7 bash
```

**fedora**

Fedora 由 Fedora Project 社区开发，红帽公司赞助的 Linux 发行版。它的目标是创建一套新颖、多功能并且自由和开源的操作系统。Fedora 的功能对于用户而言，它是一套功能完备的，可以更新的免费操作系统，而对赞助商 Red Hat 而言，它是许多新技术的测试平台。被认为可用的技术最终会加入到 Red Hat Enterprise Linux 中。

```bash
docker pull fedora:latest
docker image ls
docker run -it fedora bash
```

### PHP

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

---

## Source & Reference

- https://mp.weixin.qq.com/s/8c9AZXrGH4dkDK1JOe9FPg
- https://www.sqlsec.com/2020/11/docker4.html
- https://blog.csdn.net/sannerlittle/article/details/77063800
- https://yeasy.gitbook.io/docker_practice/image/list
- https://yeasy.gitbook.io/docker_practice/network/port_mapping
- https://yeasy.gitbook.io/docker_practice/image/build
- https://yeasy.gitbook.io/docker_practice/image/commit
