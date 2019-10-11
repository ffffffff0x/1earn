# VSFTP 配置案例

---

**安装**
- **服务端**

	`yum install vsftpd`

- **客户端**

	`yum install ftp`

---

# 匿名访问

|参数|作用|
| :------------- | :------------- |
|anonymous_enable=YES |	允许匿名访问模式 |
|anon_umask=022 |	匿名用户上传文件的 umask 值|
|anon_upload_enable=YES |	允许匿名用户上传文件|
|anon_mkdir_write_enable=YES |	允许匿名用户创建目录|
|anon_other_write_enable=YES |	允许匿名用户修改目录名称或删除目录|

```vim
vim /etc/vsftpd/vsftpd.conf

1 anonymous_enable=YES
2 anon_umask=022
3 anon_upload_enable=YES
4 anon_mkdir_write_enable=YES
5 anon_other_write_enable=YES
```
```bash
setenforce 0
firewall-cmd --permanent --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

现在就可以在客户端执行 ftp 命令连接到远程的 FTP 服务器了.
在 vsftpd 服务程序的匿名开放认证模式下,其账户统一为 anonymous,密码为空.而且在连接到 FTP 服务器后,默认访问的是 /var/ftp 目录.
我们可以切换到该目录下的 pub 目录中,然后尝试创建一个新的目录文件,以检验是否拥有写入权限：
```bash
[root@linuxprobe ~]# ftp 192.168.10.10
Connected to 192.168.10.10 (192.168.10.10).
220 (vsFTPd 3.0.2)
Name (192.168.10.10:root): anonymous
331 Please specify the password.
Password:此处敲击回车即可
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

ftp> cd pub
250 Directory successfully changed.

ftp> mkdir files
257 "/pub/files" created

ftp> rename files database
350 Ready for RNTO.
250 Rename successful.

ftp> rmdir database
250 Remove directory operation successful.

ftp> exit
221 Goodbye.
```

---

# 本地用户

|参数 |	作用|
| :------------- | :------------- |
|anonymous_enable=NO 	|禁止匿名访问模式|
|local_enable=YES |	允许本地用户模式|
|write_enable=YES |	设置可写权限|
|local_umask=022 |	本地用户模式创建文件的 umask 值|
|userlist_deny=YES 	|启用“禁止用户名单”,名单文件为ftpusers和user_list|
|userlist_enable=YES |	开启用户作用名单文件功能|

```vim
vim /etc/vsftpd/vsftpd.conf

1 anonymous_enable=NO
2 local_enable=YES
3 write_enable=YES
4 local_umask=022
```
```bash
setenforce 0
firewall-cmd --permanent --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```
按理来讲,现在已经完全可以本地用户的身份登录 FTP 服务器了.但是在使用 root 管理员登录后,系统提示如下的错误信息：
```bash
[root@linuxprobe ~]# ftp 192.168.10.10
Connected to 192.168.10.10 (192.168.10.10).
220 (vsFTPd 3.0.2)
Name (192.168.10.10:root): root
530 Permission denied.
Login failed.
ftp>
```
可见,在我们输入 root 管理员的密码之前,就已经被系统拒绝访问了.这是因为 vsftpd 服务程序所在的目录中默认存放着两个名为“用户名单”的文件 (ftpusers和user_list) .只要里面写有某位用户的名字,就不再允许这位用户登录到 FTP 服务器上.
```bash
[root@linuxprobe ~]# cat /etc/vsftpd/user_list

[root@linuxprobe ~]# cat /etc/vsftpd/ftpusers
```
如果你确认在生产环境中使用 root 管理员不会对系统安全产生影响,只需按照上面的提示删除掉 root 用户名即可.我们也可以选择 ftpusers 和 user_list 文件中没有的一个普通用户尝试登录 FTP 服务器
在采用本地用户模式登录 FTP 服务器后,默认访问的是该用户的家目录,也就是说,访问的是 /home/username 目录.而且该目录的默认所有者、所属组都是该用户自己,因此不存在写入权限不足的情况.

---

# 虚拟用户

1. 创建用于进行 FTP 认证的用户数据库文件,其中奇数行为账户名,偶数行为密码.例如,我们分别创建出 zhangsan 和 lisi 两个用户,密码均为 redhat
```bash
cd /etc/vsftpd/
```
```vim
vim login.list

zhangsan
redhat
lisi
redhat
```
> 但是,明文信息既不安全,也不符合让 vsftpd 服务程序直接加载的格式,因此需要使用db_load 命令用哈希 (hash) 算法将原始的明文信息文件转换成数据库文件,并且降低数据库文件的权限 (避免其他人看到数据库文件的内容) ,然后再把原始的明文信息文件删除.

```bash
db_load -T -t hash -f login.list login.db
rm -f login.list
```

2. 创建 vsftpd 服务程序用于存储文件的根目录以及虚拟用户映射的系统本地用户.FTP 服务用于存储文件的根目录指的是,当虚拟用户登录后所访问的默认位置

> 由于 Linux 系统中的每一个文件都有所有者、所属组属性,例如使用虚拟账户“张三”新建了一个文件,但是系统中找不到账户“张三”,就会导致这个文件的权限出现错误.为此,需要再创建一个可以映射到虚拟用户的系统本地用户.简单来说,就是让虚拟用户默认登录到与之有映射关系的这个系统本地用户的家目录中,虚拟用户创建的文件的属性也都归属于这个系统本地用户,从而避免 Linux 系统无法处理虚拟用户所创建文件的属性权限.

> 为了方便管理 FTP 服务器上的数据,可以把这个系统本地用户的家目录设置为 /var 目录 (该目录用来存放经常发生改变的数据) .并且为了安全起见,我们将这个系统本地用户设置为不允许登录 FTP 服务器,这不会影响虚拟用户登录,而且还可以避免黑客通过这个系统本地用户进行登录.

```bash
useradd -d /home/ftp -s /sbin/nologin virtual
chmod -Rf 755 /home/ftp
```

3. 建立用于支持虚拟用户的 PAM 文件.
新建一个用于虚拟用户认证的 PAM 文件 vsftpd.vu,其中 PAM 文件内的“db=”参数为使用 db_load 命令生成的账户密码数据库文件的路径,但不用写数据库文件的后缀：
```vim
vim /etc/pam.d/vsftpd.vu

auth       required     pam_userdb.so db=/etc/vsftpd/login
account    required     pam_userdb.so db=/etc/vsftpd/login
```
在 vsftpd 服务程序的主配置文件中通过 pam_service_name 参数将 PAM 认证文件的名称修改为 vsftpd.vu,

例如,在 vsftpd 服务程序的主配置文件中默认就带有参数 pam_service_name=vsftpd,表示登录 FTP 服务器时是根据 /etc/pam.d/vsftpd 文件进行安全认证的.现在我们要做的就是把 vsftpd 主配置文件中原有的 PAM 认证文件 vsftpd 修改为新建的 vsftpd.vu 文件即可.
```vim
vim /etc/vsftpd/vsftpd.conf

1 anonymous_enable=NO
2 local_enable=YES
3 guest_enable=YES
4 guest_username=virtual
5 pam_service_name=vsftpd.vu
6 allow_writeable_chroot=YES
```

|参数 |	作用|
| :------------- | :------------- |
|anonymous_enable=NO 	|禁止匿名开放模式|
|local_enable=YES |	允许本地用户模式|
|guest_enable=YES |	开启虚拟用户模式|
|guest_username=virtual |	指定虚拟用户账户|
|pam_service_name=vsftpd.vu |	指定 PAM 文件|
|allow_writeable_chroot=YES |	允许对禁锢的 FTP 根目录执行写入操作,而且不拒绝用户的登录请求|

为虚拟用户设置不同的权限.虽然账户 zhangsan 和 lisi 都是用于 vsftpd 服务程序认证的虚拟账户,但是我们依然想对这两人进行区别对待.比如,允许张三上传、创建、修改、查看、删除文件,只允许李四查看文件.这可以通过 vsftpd 服务程序来实现.只需新建一个目录,在里面分别创建两个以 zhangsan 和 lisi 命名的文件,其中在名为 zhangsan 的文件中写入允许的相关权限
```vim
mkdir /etc/vsftpd/user_conf/
cd /etc/vsftpd/user_conf/
touch lisi
```
```vim
vim zhangsan

anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
```

然后再次修改 vsftpd 主配置文件,通过添加 user_config_dir 参数来定义这两个虚拟用户不同权限的配置文件所存放的路径.为了让修改后的参数立即生效,需要重启 vsftpd 服务程序并将该服务添加到开机启动项中：
```vim
vim /etc/vsftpd/vsftpd.conf

user_config_dir=/etc/vsftpd/user_conf
```

```bash
setenforce 0
firewall-cmd --permanent --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

# 案例
## 案例 1

- 使用虚拟用户认证方式,创建用户 virtftp,该用户的家目录为 /data/ftp_data,shell 为 /sbin/nologin,并将虚拟用户映射至 virtftp 用户；
- 允许属主对 /data/ftp_data 有写权限；
- 关闭 PASV 模式的安全检查；
- 设置客户端最大连接数为 100,每个 IP 允许 3 个连接数；
- ftpuser 虚拟用户可以下载与上传文件；
- ftpadmin 虚拟用户可以下载与上传文件以及删除重命名操作,上传文件的 umask 为 022.
- 配置文件要求:
	- 以下文件除了 vsftpd.conf 文件其余文件均需要自行创建
	- /etc/vsftpd/vsftpd.conf(ftp 配置文件)/etc/pam.d/vsftpd.vu, (pam 配置文件) 
	- /etc/vsftpd/vlogin.db, (用户数据库) 
	- /etc/vsftpd/ftp_user (该目录下 ftp 用户权限配置目录) 
	- ftpuser,ftpadmin 用户权限相关配置文件均在 /etc/vsftpd/ftp_user 目录下.

**安装服务,配置虚拟用户认证**
```bash
yum install vsftpd
```
```vim
cd /etc/vsftp
vim vlogin.list

ftpuser
123456
ftpadmin
123456
```
```bash
db_load -T -t hash -f vlogin.list vlogin.db

cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.vu
```
```vim
vim /etc/pam.d/vsftpd.vu

auth       required     pam_userdb.so db=/etc/vsftpd/vlogin
account    required     pam_userdb.so db=/etc/vsftpd/vlogin
```

**修改配置文件**
```vim
vim /etc/vsftpd/vsftpd.conf

pam_service_name=vsftpd.vu
guest_enable=YES
guest_username=virtftp
user_config_dir=/etc/vsftpd/ftp_user
allow_writeable_chroot=YES

pasv_promiscuous=YES
max_clients=100
max_per_ip=3
```

**创建家目录为 /data/ftp_data,shell为/sbin/nologin 的 virtftp 用户；**
```bash
useradd -d /data/ftp_data -s /sbin/nologin virtftp
chmod -Rf 755 /data/ftp_data
cd /data/ftp_data
touch testfile
```

**配置权限文件**
```bash
mkdir /etc/vsftpd/ftp_user
cd /etc/vsftpd/ftp_user
```
```vim
vim ftpuser

anon_upload_enable=YES
```
```vim
vim ftpadmin

anon_upload_enable=YES
anon_mkdir_wirte_enable=YES
anon_other_wirte_enable=YES
anon_umask=022
```

**起服务**
```bash
setenforce 0
firewall-cmd --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

## 案例 2

- 创建用户 tom,密码为 aaabbb.
- 为 WEB 网站创建 FTP 站点,具体要求如下：
- FTP 普通用户主目录：/data/web_data
- FTP 访问权限：通过扩展 acl 方式允许用户 tom 读取和写入
- FTP 访问路径为：ftp://tom:aaabbb@公网IP/
- 为产品资料下载创建 FTP 站点,具体要求如下：
- FTP 匿名用户主目录：/data/instructions
- FTP 访问权限：允许匿名用户读取
- FTP 访问路径为：ftp://公网IP/

**修改配置文件**
```vim
vim /etc/vsftpd/vsftpd.conf

local_root=/data/web_data
anon_root=/data/instructions
anon_upload_enable=NO
```

**创建用户与 acl；**
```bash
useradd tom
passwd tom
cd /data/web_data
chmod -Rf 755 /data/web_data
setfacl -R -m u:tom:rwx .
touch success
```

**起服务**
```bash
setenforce 0
firewall-cmd --zone=public --add-service=ftp
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

## 案例 3

- 拒绝匿名访问,只允许本地系统用户登录；
- 使用被动模式,设置主机B公网 IP 为被动模式数据传输地址
- 所有用户主目录为 /data/ftp_data 宿主为 virtual 用户；
- 将用户使用文件的方式记录账号以及密码；
- ftpuser1 用户只能下载不能上传以及删除文件重命名操作；
- ftpuser2 可以下载与上传文件以及删除重命名操作；
- ftpadmin 可以下载与上传文件以及删除重命名操作,上传文件的 umask 为 022；
- 配置文件要求:
	- 以下文件除了 vsftpd.conf 文件其余文件均需要自行创建：
	- /etc/vsftpd/vsftpd.conf(ftp配置文件)/etc/pam.d/vsftpd.vu, (pam 配置文件) 
	- /etc/vsftpd/vlogin.db, (用户数据库) 
	- /etc/vsftpd/user_conf (该目录下 ftp 用户权限配置目录) 
	- ftpuser1,ftpuser2,ftpadmin 用户权限相关配置文件均在 /etc/vsftpd/user_conf 目录下.

**安装服务,配置虚拟用户认证**
```bash
yum install vsftpd
cd /etc/vsftp
```
```vim
vim vlogin.list

ftpuser1
123456
ftpuser2
123456
ftpadmin
123456
```
```bash
db_load -T -t hash -f vlogin.list vlogin.db

cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.vu
```
```vim
vim /etc/pam.d/vsftpd.vu

auth       required     pam_userdb.so db=/etc/vsftpd/vlogin
account    required     pam_userdb.so db=/etc/vsftpd/vlogin
```

**修改配置文件**
```vim
vim /etc/vsftpd/vsftpd.conf

anonymous_enable=NO

pam_service_name=vsftpd.vu

guest_enable=YES
guest_username=virtual
user_config_dir=/etc/vsftpd/ftp_user
allow_writeable_chroot=YES

pasv_enable=YES         # 启用 pasv 模式
pasv_min_port=30000     # pasv 端口起始号
pasv_max_port=40000     # pasv 端口结束号

xferlog_enable=YES         # 启用上传和下载的日志功能,默认开启.
xferlog_file=/var/log/xferlog         # vsftpd 的日志存放位置
```

**创建家目录为 /data/ftp_data 的 virtual 用户；**
```bash
useradd -d /data/ftp_data -s /sbin/nologin virtual
chmod -Rf 755 /data/ftp_data
cd /home/ftp/
touch testfile
grep virtftp /etc/passwd
```

**配置权限文件**
```bash
mkdir /etc/vsftpd/ftp_user
cd /etc/vsftpd/ftpuser1
```
```vim
vim ftpuser

vim ftpuser2

anon_upload_enable=YES
anon_mkdir_wirte_enable=YES
anon_other_wirte_enable=YES

vim ftpadmin

anon_upload_enable=YES
anon_mkdir_wirte_enable=YES
anon_other_wirte_enable=YES
anon_umask=022
```

**起服务**
```bash
setenforce 0
firewall-cmd --zone=public --add-port=30000-40000/tcp --permanent
firewall-cmd --zone=public --add-port=30000-40000/udp --permanent
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```

---

## 案例 4

- 创建用户 tom,密码为 aaabbb；
- 禁止匿名用户登录；
- 使用被动模式,设置主机B公网 IP 为被动模式数据传输地址；
- 为 mariadb 数据库创建 FTP 站点,具体要求如下：
- FTP 普通用户主目录：/data/mariadb_data；
- FTP 访问权限：通过扩展 acl 方式设置用户 tom 拥有读、写、执行权限；
- FTP 访问路径为：ftp://tom:aaabbb@公网IP/.

**修改配置文件**
```vim
vim /etc/vsftpd/vsftpd.conf

anonymous_enable=NO
local_root=/data/mariadb_data

pasv_enable=YES         # 启用 pasv 模式
pasv_min_port=30000     # pasv 端口起始号
pasv_max_port=40000     # pasv 端口结束号
```

**创建用户与 acl；**
```bash
useradd tom
passwd tom
cd /data/mariadb_data
chmod -Rf 755 /data/mariadb_data
setfacl -R -m u:tom:rwx .
touch success
```

**起服务**
```bash
setenforce 0
firewall-cmd --zone=public --add-port=30000-40000/tcp --permanent
firewall-cmd --zone=public --add-port=30000-40000/udp --permanent
firewall-cmd --reload
systemctl restart vsftpd
systemctl enable vsftpd
```
