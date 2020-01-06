# samba 配置案例

---

## 案例 1
- 配置 smb 服务，共享目录为 /smbshare，
- 共享名必须为 smbshare，
- 只有本网段内的所有主机可以访问，
- smbshare 必须是可以浏览的，
- 用户 smb1 必须能够读取共享中的内容(用户名需要自己创建，密码为 smb123456);

```
yum -y install samba
```

```vim
vim /etc/samba/smb.conf

[smbshare]
	path = /smbshare
	public = yes
	writeable=yes
	hosts allow = 192.168.xx.
	hosts deny = all
```

验证配置文件有没有错误 `testparm`

添加用户,设置密码
```bash
useradd smb1
smbpasswd -a smb1(密码:smb123456)
```

将用户添加到 samba 服务器中，并设置密码
```bash
pdbedit -a smb1(密码:smb123456)
```

查看 samba 数据库用户
```bash
pdbedit -L
```

创建共享目录，设置所有者和所属组
```bash
mkdir /smbshare
chown smb1:smb1 /smbshare
```

关闭 selinux(需要重启)
```vim
vim /etc/selinux/config

SELINUX=disabled
```
```bash
firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload

systemctl restart smb
```

---

## 案例 2
**服务端**
- 修改工作组为 WORKGROUP
- 注释 [homes] 和 [printers] 相关的所有内容
- 共享名为 webdata
- webdata 可以浏览且 webdata 可写
- 共享目录为 /data/web_data，且 apache 用户对该目录有读写执行权限，用 setfacl 命令配置目录权限.
- 只有 192.168.1XX.33 的主机可以访问.
- 添加一个 apache 用户(密码自定义)对外提供 Samba 服务.

```bash
yum -y install samba
```
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
smbpasswd -a apache(密码:smb123456)
pdbedit -a apache(密码:smb123456)
pdbedit -L

mkdir /data/web_data
cd /data/web_data/
setfacl -m u:apache:rwx .
getfacl /deta/web_data/
```

```bash
setenforce 0

firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload

systemctl start smb
```


**客户端**
- 配置 smb，使用 apache 用户挂载 serverA 共享的目录至 /data/web_data 目录下，作为 http 服务网站根目录使用.

```bash
yum -y install samba

mkdir /data/web_data
mount -t cifs -o username=apache,password='123' //192.168.xx+1.xx/webdata
/data/web_data
```

---

## 案例 3

**服务端**
- 修改工作组为 WORKGROUP;
- 注释 [homes] 和 [printers] 的内容;
- 共享目录为 /data/web_data;
- 共享名必须为 webdata;
- 只有 192.168.XX+1.0/24 网段内的所有主机可以访问;
- webdata 必须是可以浏览的;
- webdata 必须是可写的;
- 创建文件的权限为 0770;
- 仅允许用户 apache 访问且 apache 是该共享的管理者(用户名需要自己创建，密码为 123).

```bash
yum -y install samba
```
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
smbpasswd -a apache(密码:123)
pdbedit -a apache(密码:123)
pdbedit -L

mkdir /data/web_data
cd /data/web_data/

```

```bash
setenforce 0
firewall-cmd --zone=public --add-service=samba --permanent
firewall-cmd --reload
systemctl start smb
```

**客户端**
- 配置 smb，使用 apache 用户挂载主机A共享的目录至 /data/web_data 目录下.

```bash
yum -y install samba

mkdir /data/web_data
mount -t cifs -o username=apache,password='123' //192.168.xx+1.xx/webdata
/data/web_data
```