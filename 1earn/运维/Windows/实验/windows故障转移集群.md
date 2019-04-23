



**群集节点的删除**
一般情况下，Windows群集可以在群集管理器中，使用功能菜单的“退出节点”来删除一个群集节点，但有时这个功能是不可用的，这种情况下，如果要从群集中删除一个叫SecondNode的节点，使用的命令是：
`cluster node SecondNode /force`

这个命令执行之后，群集管理器中“退出节点”的功能就可以继续使用了。然后就可以删除故障群集功能，重新启动，然后可以再次配置！

待测试
```
在2008R2 的powershell
输入：  import-module    failovercluster
clear-node
```

**无法退出节点时**
在正常删除Cluster 节点之后，再添加节点时，报“节点已经加入群集”，无法加入，注册表信息删除后可正常移除Cluster服务,删除注册表中这两个后重新启动就可以了
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\ClusDisk`
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\ClusSvc`


