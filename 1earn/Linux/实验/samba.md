# smb🏓
配置 smb 服务，共享目录为 /smbshare，
共享名必须为 smbshare，
只有本网段内的所有主机可以访问，
smbshare 必须是可以浏览的，
用户 smb1 必须能够读取共享中的内容，
（用户名需要自己创建，密码为 smb123456）；

>yum -y install samba 

```vim	
vim /etc/samba/smb.conf
[smbshare]
	path = /smbshare
	public = yes
	writeable=yes
	hosts allow = 192.168.xx.
	hosts deny = all
```

验证配置文件有没有错误
>	testparm

添加用户,设置密码
>	useradd smb1
>	smbpasswd ‐a smb1(密码：smb123456)

将用户添加到 samba 服务器中，并设置密码
>	pdbedit ‐a smb1(密码：smb123456)

查看 samba 数据库用户
>	pdbedit ‐L

创建共享目录，设置所有者和所属组
>	mkdir /smbshare
>	chown smb1:smb1 /smbshare

关闭 selinux（需要重启）
```vim
vim /etc/selinux/config
SELINUX=disabled

firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload

systemctl restart smb
```

---

**18-I**
配置samba服务
A
- 修改工作组为WORKGROUP
- 注释[homes]和[printers]相关的所有内容
- 共享名为webdata
- webdata可以浏览且webdata可写
- 共享目录为/data/web_data，且apache用户对该目录有读写执行权限，用setfacl命令配置目录权限。
- 只有192.168.1XX.33的主机可以访问。（XX现场提供）
- 添加一个apache用户（密码自定义）对外提供Samba服务。

>yum -y install samba 

```vim
vim /etc/samba/smb.conf
[global]
	workgroup = WORKGROUP

[webdata]
	path = /data/web_data
	public = yes
	writable=yes
	hosts allow = 192.168.1xx.33/32
	hosts deny = all
```

```bash
testparm
useradd -s /sbin/nologin apache
smbpasswd ‐a apache(密码：smb123456)
pdbedit ‐a apache(密码：smb123456)
pdbedit ‐L

mkdir /data/web_data
cd /data/web_data/
setfacl -m u:apache:rwx .
getfacl /deta/web_data/
```

```vim
setenforce 0

firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload

systemctl start smb
```


B
- 配置smb，使用apache用户挂载serverA共享的目录至/data/web_data目录下，作为http服务网站根目录使用。

```bash
yum -y install samba 

mkdir /data/web_data
mount -t cifs -o username=apache,password='ruijie' //192.168.xx+1.xx/webdata 
/data/web_data
```

---

**18 J0**
A
配置smb服务
- 修改工作组为WORKGROUP；
- 注释[homes]和[printers]的内容；
- 共享目录为/data/web_data；
- 共享名必须为webdata；
- 只有192.168.XX+1.0/24网段内的所有主机可以访问；
- webdata必须是可以浏览的；
- webdata必须是可写的；
- 创建文件的权限为0770；
- 仅允许用户apache访问且apache是该共享的管理者（用户名需要自己创建，密码为ruijie）。

>yum -y install samba 

```vim
vim /etc/samba/smb.conf
[global]
	workgroup = WORKGROUP

[webdata]
	path = /data/web_data
	public = yes
	writable=yes
	hosts allow = 192.168.xx+1.
	hosts deny = all
	create mask = 0770
```

```bash
testparm
useradd apache
smbpasswd ‐a apache(密码：ruijie)
pdbedit ‐a apache(密码：ruijie)
pdbedit ‐L

mkdir /data/web_data
cd /data/web_data/

```

```vim
setenforce 0
firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload
systemctl start smb
```


B
- 配置smb，使用apache用户挂载云主机A共享的目录至/data/web_data目录下。

```bash
yum -y install samba 

mkdir /data/web_data
mount -t cifs -o username=apache,password='ruijie' //192.168.xx+1.xx/webdata 
/data/web_data
```