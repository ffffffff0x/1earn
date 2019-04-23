# Git 使用指南
[TOC]

---

# 原理
![image](https://i.loli.net/2019/04/03/5ca4175e156b4.jpg)
- **工作区（Working Directory）**
    就是你在电脑里能看到的目录，比如我的 gitcode 文件夹就是一个工作区。

- **版本库（Repository）**
    工作区有一个隐藏目录.git，这个不算工作区，而是 Git 的版本库。
    Git 的版本库里存了很多东西，其中最重要的就是称为 stage（或者叫 index）的暂存区，还有 Git 为我们自动创建的第一个分支 master，以及指向master 的一个指针叫 HEAD 。

    把文件往 Git 版本库里添加的时候，是分两步执行的：
    第一步是用 git add 把文件添加进去，实际上就是把文件修改添加到暂存区；
    第二步是用 git commit 提交更改，实际上就是把暂存区的所有内容提交到当前分支。

    因为我们创建 Git 版本库时，Git 自动为我们创建了唯一一个 master 分支，所以，现在，git commit 就是往 master 分支上提交更改。
    你可以简单理解为，需要提交的文件修改通通放到暂存区，然后，一次性提交暂存区的所有修改。

---

# 基本操作
```bash
git config --global user.name "username"
git config --global user.email user@aaa.com
# 如果使用了 –global 选项，那么该命令只需要运行一次，因为之后无论你在该系统上做任何事情，Git 都会使用那些信息。当你想针对特定项目使用不同的用户名称与邮件地址时，可以在那个项目目录下运行没有 –global 选项的命令来配置。

git config --global http.proxy  #查看当前代理设置
git config --global http.proxy 'socks5://127.0.0.1:1080'    #设置当前代理
git config --global https.proxy 'socks5://127.0.0.1:1080'   #设置当前代理
git config --global --unset https.proxy #删除 proxy


git init    #初始化仓库
git config --list   #检查配置信息

git status  #查看状态
git diff    #查看已暂存和未暂存的修改
git diff --cached   #查看暂存区和本地仓库之间的差异

git log     #查看提交历史
git reflog  #显示当前分支的最近几次提交


git commit -m "Input your commit message"   #提交更新
git commit -a -m "Commit message"   #跳过使用暂存区
git rm <finame> 
git mv file_from file_to


已修改，未暂存
#如果我们只是在编辑器里修改了文件，但还没有执行 git add .，这时候我们的文件还在工作区，并没有进入暂存区，我们可以用
git checkout -- test.txt  #git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以 “一键还原”。
git reset HEAD file    #把暂存区的修改撤销掉（unstage），重新放回工作区

已暂存，未提交
#你已经执行了 git add .，但还没有执行 git commit -m "comment"。这时候你意识到了错误，想要撤销，你可以执行：
git reset
git checkout .

已提交，未推送
#你的手太快，你既执行了 git add .，又执行了 git commit，这时候你的代码已经进入了你的本地仓库，然而你后悔了，怎么办？不要着急，还有办法。
git reset --hard origin/master
#还是这个 git reset --hard 命令，只不过这次多了一个参数 origin/master，正如我们上面讲过的，origin/master 代表远程仓库，既然你已经污染了你的本地仓库，那么就从远程仓库把代码取回来吧。

已推送
#很不幸，你的手实在是太快了，你既 git add 了，又 git commit 了，并且还 git push 了，这时你的代码已经进入远程仓库。如果你想恢复的话，还好，由于你的本地仓库和远程仓库是等价的，你只需要先恢复本地仓库，再强制 push 到远程仓库就好了：
git reset --hard HEAD^
git push -f
```

## 分支管理
![image](https://i.loli.net/2019/04/03/5ca41e96e528e.png)
```bash
git branch  #查看分支
git branch -r #查看远程分支
git branch -a #查看所有分支
git branch <name>   #创建分支
git checkout <name> #切换分支
git checkout -b <name>  #创建 + 切换分支
git merge <name>    #合并某分支到当前分支
git branch -d <name>    #删除分支

git stash   #储藏分支
git stash list
git stash pop   #恢复的同时把 stash 内容也删了
```

## 标签管理
```bash
#注意，标签不是按时间顺序列出，而是按字母排序的。可以用 git show <tagname> 查看标签信息

git tag <name> 用于新建一个标签，默认为 HEAD，也可以指定一个 commit id；
git tag -a <tagname> -m "blablabla..." 可以指定标签信息；
git tag -s <tagname> -m "blablabla..." 可以用 PGP 签名标签；
git tag 可以查看所有标签。
git push origin <tagname> 可以推送一个本地标签；
git push origin --tags 可以推送全部未推送过的本地标签；
git tag -d <tagname> 可以删除一个本地标签；
git push origin :refs/tags/<tagname> 可以删除一个远程标签。
```

## 忽略文件
一个名为 .gitignore 的文件，列出要忽略的文件模式。
配置语法：
```bash
以斜杠“/”开头表示目录；
以星号“*”通配多个字符；
以问号“?”通配单个字符
以方括号“[]”包含单个字符的匹配列表；
以叹号“!”表示不忽略(跟踪)匹配到的文件或目录；

/*
!.gitignore
!/fw/bin/
!/fw/sf/
说明：忽略全部内容，但是不忽略 .gitignore 文件、根目录下的 /fw/bin/ 和 /fw/sf/ 目录；
```
此外，git 对于 .ignore 配置文件是按行从上到下进行规则匹配的，意味着如果前面的规则匹配的范围更大，则后面的规则将不会生效；

## 别名
```bash
以下2条都是对 git lg 的 alias
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --"

git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"
```
---

# 远程操作
![image](https://i.loli.net/2019/04/02/5ca36a2b1f811.png)
多人协作的工作模式通常是这样：
首先，可以试图用 `git push origin branch-name` 推送自己的修改；
如果推送失败，则因为远程分支比你的本地更新，需要先用 `git pull` 试图合并；
如果合并有冲突，则解决冲突，并在本地提交；
没有冲突或者解决掉冲突后，再用 `git push origin branch-name` 推送就能成功！
如果 `git pull` 提示 `“no tracking information”`，则说明本地分支和远程分支的链接关系没有创建，用命令 `git branch --set-upstream branch-name origin/branch-name`

## git clone
`git clone <版本库的网址> <本地目录名>`

## git remote
```bash
git remote #命令列出所有远程主机

git remote -v #参看远程主机的网址
origin  git@github.com:jquery/jquery.git (fetch)
origin  git@github.com:jquery/jquery.git (push)

git remote add <主机名> <网址>    #用于添加远程主机
git remote rm <主机名>  #用于删除远程主机
git remote rename <原主机名> <新主机名> #用于远程主机的改名
```

## git fetch
git fetch 会使你与另一仓库同步，提取你本地所没有的数据，为你在同步时的该远端的每一分支提供书签。 这些分支被叫做 “远端分支”，除了 Git 不允许你检出（切换到该分支）之外，跟本地分支没区别 —— 你可以将它们合并到当前分支，与其他分支作比较差异，查看那些分支的历史日志，等等。同步之后你就可以在本地操作这些。
```bash
git fetch <远程主机名>  #将某个远程主机的更新，全部取回本地

it branch 命令的 -r 选项，可以用来查看远程分支，-a 选项查看所有分支。
git branch -r

git branch -a
```

上面命令表示，本地主机的当前分支是 master，远程分支是 origin/master。
取回远程主机的更新以后，可以在它的基础上，使用 `git checkout` 命令创建一个新的分支。
```bash
git checkout -b newBrach origin/master
上面命令表示，在 origin/master 的基础上，创建一个新分支。

此外，也可以使用 git merge 命令或者 git rebase 命令，在本地分支上合并远程分支。
git merge origin/master
或者
git rebase origin/master
上面命令表示在当前分支上，合并 origin/master。
```

## git pull
基本上，该命令就是在 `git fetch` 之后紧接着 `git merge` 远端分支到你所在的任意分支。
```bash
git pull <远程主机名> <远程分支名>:<本地分支名> #取回远程主机某个分支的更新，再与本地的指定分支合并。
git pull origin next:master #取回 origin 主机的 next 分支，与本地的 master 分支合并
```

## git push
```bash
git push <远程主机名> <本地分支名>:<远程分支名> #将本地分支的更新，推送到远程主机
git push origin master  #本地的 master 分支推送到 origin 主机的 master 分支。如果后者不存在，则会被新建。

如果远程主机的版本比本地版本更新，推送时 Git 会报错，要求先在本地做 git pull 合并差异，然后再推送到远程主机。这时，如果你一定要推送，可以使用 --force 选项。
git push --force origin 
上面命令使用 --force选项，结果导致远程主机上更新的版本被覆盖。除非你很确定要这样做，否则应该尽量避免使用 --force 选项。
```

## github
- **github开启二次验证后后，git push验证权限失败**
    github开启二次验证后，提交时密码用个人设置里的Personal Access Token，不是账号密码

- **Git Push 避免用户名和密码方法**
    在windows中添加一个用户变量，变量名:HOME,变量值：%USERPROFILE%
    
    ![image](https://i.imgur.com/TWEi10z.jpg)

    进入%HOME%目录，新建一个名为"_netrc"的文件，文件中内容格式如下：
    ```bash
    machine github.com
    login your-usernmae
    password your-password
    ```
    
---

# Reference
- [Git Push 避免用户名和密码方法](https://www.cnblogs.com/ballwql/p/3462104.html)
- [Git初始配置和基本使用](https://blog.csdn.net/daily886/article/details/80140720)
- [Git远程操作详解 - 阮一峰的网络日志](www.ruanyifeng.com/blog/2014/06/git_remote.html)
- [Git教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
- [Git 的 .gitignore 配置](https://www.cnblogs.com/haiq/archive/2012/12/26/2833746.html)
- [让Git的输出更友好: 多种颜色和自定义log格式](https://blog.csdn.net/lts_cxl/article/details/17282725)
- [Git 的 4 个阶段的撤销更改](http://blog.jobbole.com/113097/)
