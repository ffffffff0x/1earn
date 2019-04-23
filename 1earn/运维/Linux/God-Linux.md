# God-Linux🎭
[TOC]

---

## bash
``` bash
!$：上一个命令的最后一个参数。例如：上一条命令（vim test.txt），cat !$ = cat test.txt
cat !$

cat !$代替方案
cat [组合键："esc"+"."]

一个命令创建项目的目录结构
mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}

筛选出命令中错误的输出，方便找到问题
yum list 1 > /dev/null

查看自己的外网地址
curl ifconfig.me

fork炸弹
:(){:|:&};:
```


## VIM
``` bash
无 root 权限，保存编辑的文件
:w !sudo tee %
```

`每个人都能学会雕塑：米开朗基罗这样的人反倒需要学习如何不去雕塑。伟大的程序员也是如此`
