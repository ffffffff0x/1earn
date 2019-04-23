**搭建**
这篇百度文库的文档写的相当详细具体,我觉得没有必要重复写一遍,https://wenku.baidu.com/view/4646e1b4866fb84ae45c8dd3.html ,虽然是基于2008R2,版本有点老,但是还是推荐
`ps.我以前怎么就没发现百度文库这么牛逼呢？`

**群集节点的删除**
一般情况下,Windows群集可以在群集管理器中,使用功能菜单的"退出节点"来删除一个群集节点,但有时这个功能是不可用的,这种情况下,如果要从群集中删除一个叫SecondNode的节点,使用的命令是：
`cluster node SecondNode /force`

这个命令执行之后,群集管理器中"退出节点"的功能就可以继续使用了。然后就可以删除故障群集功能,重新启动,然后可以再次配置！

未测试的删除方法,建议先使用上面的命令,不行再用这个
```bash
在2008R2 的powershell
输入：  import-module    failovercluster
clear-node
```

**无法退出节点时**
在正常删除Cluster 节点之后,再添加节点时,报"节点已经加入群集",无法加入,注册表信息删除后可正常移除Cluster服务,删除注册表中这两个后重新启动就可以了
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\ClusDisk`
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\ClusSvc`


