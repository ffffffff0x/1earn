# nfs🏸

1. 在Centos上配置nfs服务以只读的形式方式共享目录／public（目录需要自己创建）。
```bash
yum ‐y install nfs‐utils
vim /etc/exports
	/public 192.168.xxx.xxx(ro)

mkdir /public

vi /etc/selinux/config
	SELINUX=disabled

firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload

service rpcbind start
service nfs start
```


客户端挂载 nfs；
1. 访问使用 nfsuser1 进行访问（用户需要自己创建）；
2. 在 Centos 上挂载来自 Centos 的 nfs 共享,将共享目录挂载到 /mnt/nfsfiles,启动时自动挂载。
```bash
yum ‐y install nfs‐utils
mkdir /mnt/nfsfiles

useradd nfsuser1
passwd nfsuser1
```

验证共享是否成功
>showmount ‐e 192.168.xxx.xxx

挂载共享目录
```vim
vim /etc/fstab
	192.168.xxx.xxx:/public /mnt/nfsfiles/	nfs defaults 0 0
```

>su ‐l nfsuser1

**验证**
服务器
```bash
[root@localhost ~]# cd /public/
[root@localhost public]# echo "hello" > hello.txt
```
客户端
```bash
[nfsuser1@localhost ~]$ cd /mnt/nfsfiles/
[nfsuser1@localhost nfsfiles]$ cat hello.txt
```

---

1. 将云主机 1 配置为 nfs 服务器，把 /var/www/html 作为共享目录，
```bash
yum ‐y install nfs‐utils
vim /etc/exports
	/var/www/html 192.168.xxx.xxx(rw)

firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload

service rpcbind start
service nfs start
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

2. 将云主机 2 配置为 nfs 客户端，并在其上查看共享目录，并挂载到本地目录/test
```bash
mount.nfs 192.168.xxx.xxx:/var/www/html /test
```

3. 同时将 /test 文件夹内容拷贝到云主机2下的 /home/www，并创建一个归档备份
```bash
cp /test /home/www
```

4. 将云主机2的 /home/www 目录打包备份至 /home 目录下文件名为 www.tar.bz2，备份周期为每天凌晨2点开始。
```bash
cd /
yum install -y bzip2

vim back.sh		#编写备份脚本文件
	tar jcvf /home/www.tar.bz2 /home/www

chmod -x back.sh	#编辑脚本文件为可执行文件

crontab -e	#编写定时任务crontab脚本
0 2 * * * /back.sh
#每天的02点00分自动执行脚本文件

#跟踪执行结果
tail -f /var/log/cron  #跟踪查询定时任务是否执行
cat /var/spool/cron/root #查询root下有那些定时任务
```

---


1. 启动 nfs 服务和设置开机启动；
```bash
firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload

service rpcbind start
service nfs start
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

2. 将以上挂载的云硬盘格式化为 ext4 格式并挂载到 /mnt 目录上；
```bash
fdisk ‐l		查看磁盘情况
fdisk /dev/sdb	创建系统分区
	n
	p
	1
	后面都是默认，直接回车

	w	写入分区表

mkfs.ext4 /dev/sdb1
mkdir /mnt/sdb1
mount /dev/sdd1 /mnt/sdb1
```

3. 在云主机2上发布共享 /public 目录（需自行创建）和 /mnt 目录，/mnt 目录允许所有用户访问，但不能写入，/public 目录允许 192.168.11.0/24 网段的用户读写。
```bash
yum ‐y install nfs‐utils

vim /etc/exports
	/mnt *(ro)
	/public 192.168.11.*(rw)

mkdir /public

firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload

service rpcbind start
service nfs start
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

---

**18 E0**
A
配置NFS服务，以读写访问方式将/data/web_data目录仅共享给192.168.XX+1.0/24网段的所有用户，且不挤压root用户的权限。

```bash
yum ‐y install nfs‐utils

vim /etc/exports
	/data/web_data 192.168.XX+1.*(rw,no_root_squash)

mkdir -p /data/web_data

firewall-cmd --zone=public --add-service=rpc-bind	--permanent
firewall-cmd --zone=public --add-service=mountd --permanent
firewall-cmd --zone=public --add-port=2049/tcp --permanent
firewall-cmd --zone=public --add-port=2049/udp --permanent
firewall-cmd --reload

service rpcbind start
service nfs start
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```


B
配置NFS服务，将云主机A共享的目录挂载至/data/web_data目录下。
```bash
yum ‐y install nfs‐utils

firewall-cmd --zone=public --add-service=nfs --permanent
firewall-cmd --reload

service rpcbind start
service nfs start
systemctl enable rpcbind.service
systemctl enable nfs-server.service
```

验证共享是否成功
>showmount ‐e 192.168.xxx.xxx

```
mkdir -p /data/web_data
mount.nfs 192.168.xxx.xxx:/data/web_data /data/web_data
```
