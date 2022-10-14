# GoReleaser

- https://github.com/goreleaser/goreleaser

---

自动化打包工具

---

**安装**

- https://github.com/goreleaser/goreleaser/releases

---

**使用**

在目标目录执行 goreleaser init ，将会生成一个 `.goreleaser.yml` 配置文件

修改配置,例如
```yml
# This is an example .goreleaser.yml file with some sane defaults.
# Make sure to check the documentation at http://goreleaser.com
before:
  hooks:
    # You may remove this if you don't use go modules.
    #- go mod tidy
    # you may remove this if you don't need go generate
    #- go generate ./...
builds:
  - env:
      - CGO_ENABLED=0
    id: "anewproject"
    binary: "anew"
    goos:
      - linux
      - windows
      - darwin
    goarch:
      - amd64
archives:
  - replacements:
      darwin: Darwin
      linux: Linux
      windows: Windows
      386: i386
      amd64: x86_64
checksum:
  name_template: 'checksums.txt'
snapshot:
  name_template: "v1.0.0-snapshot"
changelog:
  sort: asc
  filters:
    exclude:
      - '^docs:'
      - '^test:'
```

**打包**

```
goreleaser --snapshot --skip-publish --rm-dist
```

这里可能会提示

```
⨯ release failed after 2.94s error=failed to build for darwin_amd64: go: cannot find main module, but found .git/config in C:\xxx
```

直接
```
go mod init hello
```
再运行一遍就可以了

如果提示一下报错
```
couldn't guess project_name, please add it to your config
```

添加一行就行
```yaml
project_name: myproject
```

**main.go 不在根目录的情况**

```yaml
# .goreleaser.yaml
builds:
- main: ./path/to/your/main/pkg/
```
