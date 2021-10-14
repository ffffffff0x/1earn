# nuclei

---

**项目地址**
- [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)

**模板库**
- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) - 由社区维护的 POC 库

**文章**
- [安利一款还不错的开源工具—Nuclei](https://mp.weixin.qq.com/s/C_-FRZMqF4ifzlx-ij4iIQ)
- [projectdiscovery之nuclei源码阅读](https://mp.weixin.qq.com/s/zedeOp8ywOohqogCOWTpbA)
- [Automate Cache Poisoning Vulnerability - Nuclei](https://blog.melbadry9.xyz/fuzzing/nuclei-cache-poisoning)
- [Exploiting Race conditions with Nuclei](https://blog.projectdiscovery.io/exploiting-race-conditons/)
- [Writing Network Templates with Nuclei](https://blog.projectdiscovery.io/writing-network-templates-with-nuclei/)

---

# 安装及维护

**安装**
- 二进制文件安装
    1. 从 Releases 页面下载已经构建好的二进制文件压缩包
    ```bash
    tar -xzvf nuclei-linux-amd64.tar.gz
    mv nuclei /usr/local/bin/
    nuclei -version
    ```

- 源码安装
    ```bash
    GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei
    ```

- 编译安装
    ```bash
    git clone https://github.com/projectdiscovery/nuclei.git; cd nuclei/v2/cmd/nuclei/; go build; mv nuclei /usr/local/bin/; nuclei -version
    ```

- 基于 docker
    ```bash
    docker pull projectdiscovery/nuclei
    docker run -it projectdiscovery/nuclei
    ```

**模板库更新**

该命令会从 https://github.com/projectdiscovery/nuclei-templates 模板库中下载最新版本
```
nuclei -update-templates
```

**命令参数**

| 命令                   | 描述                             | 例子                                            |
| ---------------------- | -------------------------------- | ----------------------------------------------- |
| bulk-size              | 每个模板最大并行的主机数(默认25) | nuclei -bulk-size 25                            |
| burp-collaborator-biid | 使用burp-collaborator插件        | nuclei -burp-collaborator-biid XXXX             |
| c                      | 并行的最大模板数量(默认10)       | nuclei -c 10                                    |
| l                      | 对URL列表进行测试                | nuclei -l urls.txt                              |
| target                 | 对目标进行测试                   | nuclei -target hxxps://example.com              |
| t                      | 要检测的模板种类                 | nuclei -t git-core.yaml -t cves/                |
| no-color               | 输出不显示颜色                   | nuclei -no-color                                |
| no-meta                | 不显示匹配的元数据               | nuclei -no-meta                                 |
| json                   | 输出为json格式                   | nuclei -json                                    |
| include-rr             | json输出格式中包含请求和响应数据 | nuclei -json -include-rr                        |
| o                      | 输出为文件                       | nuclei -o output.txt                            |
| project                | 避免发送相同的请求               | nuclei -project                                 |
| stats                  | 使用进度条                       | nuclei -stats                                   |
| silent                 | 只输出测试成功的结果             | nuclei -silent                                  |
| retries                | 失败后的重试次数                 | nuclei -retries 1                               |
| timeout                | 超时时间(默认为5秒)              | nuclei -timeout 5                               |
| trace-log              | 输出日志到log文件                | nuclei -trace-log logs                          |
| rate-limit             | 每秒最大请求数(默认150)          | nuclei -rate-limit 150                          |
| severity               | 根据严重性选择模板               | nuclei  -severity critical,high                 |
| stop-at-first-match    | 第一次匹配不要处理HTTP请求       | nuclei -stop-at-frst-match                      |
| exclude                | 排除的模板或文件夹               | nuclei -exclude panels -exclude tokens          |
| debug                  | 调试请求或者响应                 | nuclei -debug                                   |
| update-templates       | 下载或者升级模板                 | nuclei -update-templates                        |
| update-directory       | 选择储存模板的目录(可选)         | nuclei -update-directory templates              |
| tl                     | 列出可用的模板                   | nuclei -tl                                      |
| templates-version      | 显示已安装的模板版本             | nuclei -templates-version                       |
| v                      | 显示发送请求的详细信息           | nuclei -v                                       |
| version                | 显示nuclei的版本号               | nuclei -version                                 |
| proxy-url              | 输入代理地址                     | nuclei -proxy-url hxxp://127.0.0.1:8080         |
| proxy-socks-url        | 输入socks代理地址                | nuclei -proxy-socks-url socks5://127.0.0.1:8080 |
| H                      | 自定义请求头                     | nuclei -H "x-bug-bounty:hacker"                 |

---

# 使用

**运行单个模板**

对 urls.txt 中所有的主机运行 git-core.yaml 并返回结果到 results.txt

这将对 `urls.txt` 中所有的主机运行 `git-core.yaml` 并返回结果到 `results.txt`

```bash
nuclei -l urls.txt -t files/git-core.yaml -o results.txt
```

你可以轻松的通过管道使用标准的输入 (STDIN) 传递 URL 列表。

```bash
cat urls.txt | nuclei -t files/git-core.yaml -o results.txt
```

Nuclei 可以接受如下列表的 URL 作为输入，例如以下 URL：

```
https://test.some-site.com
http://vuls-testing.com
https://test.com
```

**运行多个模板**

这将会对 `urls.txt` 中所有的 URL 运行 `cves` 和 `files` 模板检查，并返回输出到 `results.txt`

```bash
nuclei -l urls.txt -t cves/ -t files/ -o results.txt
```

**组合运行**

```bash
subfinder -d hackerone.com -silent | httpx -silent | nuclei -t cves/ -o results.txt
```

**docker 调用**

对 `urls.txt` 中的 URL 通过 docker 中的 nuclei 进行检测，并将结果输出到本机的 `results.txt` 文件：
```
cat urls.txt | docker run -v /path/to/nuclei-templates:/app/nuclei-templates -v /path/to/nuclei/config:/app/.nuclei-config.json -i projectdiscovery/nuclei -t /app/nuclei-templates/files/git-config.yaml > results.txt
```

> 记得更改本机的模板路径

---

# 使用优化

**速率限制**

Nuclei 有多种控制速率的方法，包括并行执行多个模板、并行检查多个主机，以及使 nuclei 限制全局的请求速率，下面就是示例。

- `-c` 参数 - 限制并行的模板数
- `-bulk-size` 参数 - 限制并行的主机数
- `-rate-limit` 参数 - 全局速率限制

如果你想快速扫描或者控制扫描，请使用这些标志并输入限制数，`速率限制` 只保证控制传出的请求，与其他参数无关。

**排除模板**

[Nuclei模板](https://github.com/projectdiscovery/nuclei-templates) 包含多种检查，其中有许多对攻击有用的检查，但并不是都有用的。如果您只希望扫描少数特定的模板或目录，则可以使用如下的参数筛选模板，或将某些模板排除。

- **排除模板运行**

    我们不建议同时运行所有的 nuclei 模板，如果要排除模板，可以使用 `exclude` 参数来排除特定的目录或模板。

    ```bash
    nuclei -l urls.txt -t nuclei-templates -exclude panels/ -exclude technologies -exclude files/wp-xmlrpc.yaml
    ```

    注意：如上述示例中显示的那样，目录和特定模板都将不会扫描

- **基于严重性运行模板**

    您可以根据模板的严重性运行模板，扫描时可以选择单个严重性或多个严重性。

    ```bash
    nuclei -l urls.txt -t cves/ -severity critical,medium
    ```

    上面的例子将运行 `cves` 目录下所有 ` 严重 ` 和 ` 中等 ` 的模板。

    ```bash
    nuclei -l urls.txt -t panels/ -t technologies -severity info
    ```

    上面的例子将运行 `panels` 和 `technologies` 目录下严重性标记为 `info` 的模板

- **使用 `.nuclei-ignore` 文件排除模板**

    自从 nuclei 的 [v2.1.1 版本](https://github.com/projectdiscovery/nuclei/releases/tag/v2.1.1) 以来，我们添加了对 `.nuclei-ignore` 文件的支持，该文件与 `update-templates` 参数一起使用，在 **.nuclei-ignore** 文件中，您可以定义要从 nuclei 扫描中排除的所有模板目录或者模板路径，要开始使用此功能，请确保使用 `nuclei-update-templates` 参数安装 nuclei 模板，现在可以根据 `.nuclei-ignore` 的文件来添加、更新、删除模板文件。

    ```
    nano ~/nuclei-templates/.nuclei-ignore
    ```

    默认的 nuclei 忽略列表可以访问 [这里](https://github.com/projectdiscovery/nuclei-templates/blob/master/.nuclei-ignore) ，如果不想排除任何内容，只需要删除 `.nuclei-ignore` 文件。
