# uncover

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**项目地址**
- [projectdiscovery/uncover](https://github.com/projectdiscovery/uncover)

---

## 安装

**通过 go 安装**
```bash
go install -v github.com/projectdiscovery/uncover/cmd/uncover@latest
```

**通过 f8x 安装**
```bash
curl -o f8x https://f8x.io/ && mv --force f8x /usr/local/bin/f8x && chmod +x /usr/local/bin/f8x
f8x -k
```

---

## 配置

第一次运行,会在 `$HOME/.config/uncover/provider-config.yaml` 创建个空文件

需要自行修改 api 密钥

```yaml
shodan: [xxxxxxxxxxxxxxxxxxxx]
censys: [xxxxxxxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxxxxx]
fofa: [xxxxxxxxxx@qq.com:xxxxxxxxxxxxxxxxxxxx]
quake: [xxxxxxxxxxxxxxxxxxxx]
hunter: [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
zoomeye: [xxxxxxxxxxxxxxxxxxxx@qq.com:xxxxxxxxxxxxxxxxxxxx]
```

---

## 使用

**同时对多个搜索引擎进行查询**

搜索 `jira`
```
echo jira | uncover -e shodan,censys,fofa,quake,hunter,zoomeye
```

**对多个搜索引擎进行多个查询**

```
uncover -shodan 'http.component:"Atlassian Jira"' -censys 'services.software.product=`Jira`' -fofa 'app="ATLASSIAN-JIRA"' -quake 'Jira' -hunter 'Jira' -zoomeye 'app:"Atlassian JIRA"'
```

**对多个搜索语句进行查询**

```
cat dorks.txt

ssl:"Uber Technologies, Inc."
title:"Grafana"
```

```
uncover -q dorks.txt
```
