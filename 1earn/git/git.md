# 基本操作
```git
git config --global user.name "username"
git config --global user.email user@aaa.com
git init    #初始化仓库
git config --list   #检查配置信息
```

---

# 远程操作
多人协作的工作模式通常是这样：
首先，可以试图用 `git push origin branch-name` 推送自己的修改；
如果推送失败，则因为远程分支比你的本地更新，需要先用 `git pull` 试图合并；
如果合并有冲突，则解决冲突，并在本地提交；
没有冲突或者解决掉冲突后，再用 `git push origin branch-name` 推送就能成功！
如果 `git pull` 提示 `“no tracking information”`，则说明本地分支和远程分支的链接关系没有创建，用命令 `git branch --set-upstream branch-name origin/branch-name`

## git clone
`git clone <版本库的网址> <本地目录名>`

## git remote
```git
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
```git
git fetch <远程主机名>  #将某个远程主机的更新，全部取回本地

it branch 命令的 -r 选项，可以用来查看远程分支，-a 选项查看所有分支。
git branch -r

git branch -a
```

上面命令表示，本地主机的当前分支是 master，远程分支是 origin/master。
取回远程主机的更新以后，可以在它的基础上，使用 `git checkout` 命令创建一个新的分支。
```git
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
```git
git pull <远程主机名> <远程分支名>:<本地分支名> #取回远程主机某个分支的更新，再与本地的指定分支合并。
git pull origin next:master #取回 origin 主机的 next 分支，与本地的 master 分支合并
```

## git push
```git
git push <远程主机名> <本地分支名>:<远程分支名> #将本地分支的更新，推送到远程主机
git push origin master  #本地的 master 分支推送到 origin 主机的 master 分支。如果后者不存在，则会被新建。

如果远程主机的版本比本地版本更新，推送时 Git 会报错，要求先在本地做 git pull 合并差异，然后再推送到远程主机。这时，如果你一定要推送，可以使用 --force 选项。
git push --force origin 
上面命令使用 --force选项，结果导致远程主机上更新的版本被覆盖。除非你很确定要这样做，否则应该尽量避免使用 --force 选项。
```



