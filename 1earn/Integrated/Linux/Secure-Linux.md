```
  ████████                                              ██       ██
 ██░░░░░░                                              ░██      ░░
░██         █████   █████  ██   ██ ██████  █████       ░██       ██ ███████  ██   ██ ██   ██
░█████████ ██░░░██ ██░░░██░██  ░██░░██░░█ ██░░░██ █████░██      ░██░░██░░░██░██  ░██░░██ ██
░░░░░░░░██░███████░██  ░░ ░██  ░██ ░██ ░ ░███████░░░░░ ░██      ░██ ░██  ░██░██  ░██ ░░███
       ░██░██░░░░ ░██   ██░██  ░██ ░██   ░██░░░░       ░██      ░██ ░██  ░██░██  ░██  ██░██
 ████████ ░░██████░░█████ ░░██████░███   ░░██████      ░████████░██ ███  ░██░░██████ ██ ░░██
░░░░░░░░   ░░░░░░  ░░░░░   ░░░░░░ ░░░     ░░░░░░       ░░░░░░░░ ░░ ░░░   ░░  ░░░░░░ ░░   ░░
```

<p align="center">
    <a href="https://commons.wikimedia.org/wiki/File:William_J._McCloskey_(1859%E2%80%931941),_Wrapped_Oranges,_1889._Oil_on_canvas._Amon_Carter_Museum_of_American_Art.jpg"><img src="../../../assets/img/banner/Secure-Linux.jpg" width="90%"></a>
</p>

<p align="center">
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/Integrated/Linux/open-source.png" width="15%"></a>
    <a href="https://github.com/ellerbrock/open-source-badges/"><img src="../../../assets/img/Integrated/Linux/bash.png" width="15%"></a>
</p>

- `Linux 加固+维护+应急响应参考`
- `文档内容仅限 Linux ,web 服务和中间件的加固内容请看` [加固](../../Security/BlueTeam/加固.md)

---

# 大纲

* [文件](#文件)
    * [可疑文件](#可疑文件)
    * [文件恢复](#文件恢复)
* [系统](#系统)
    * [密码重置](#密码重置)
    * [会话](#会话)
    * [开机启动](#开机启动)
    * [账号](#账号)
    * [SELinux](#selinux)
    * [进程](#进程)
    * [系统完整性](#系统完整性)
    * [日志](#日志)
* [Net](#Net)
    * [端口](#端口)
    * [Firewall](#firewall)
    * [禁ping](#禁ping)
    * [SSH](#ssh)
    * [文件共享](文件共享)
* [加固](#加固)

---

# 文件
## 可疑文件

### 最近文件

```bash
find / -ctime -2                # 查找72小时内新增的文件
find ./ -mtime 0 -name "*.jsp"  # 查找24小时内被修改的 JSP 文件
find / *.jsp -perm 4777         # 查找777的权限的文件
```

### 临时文件

```bash
ls -a /tmp                      # 查看临时目录
```

### 配置文件

```bash
strings /usr/sbin/sshd | egrep '[1-9]{1,3}.[1-9]{1,3}.'    # 分析 sshd 文件，是否包括IP信息
```

---

## 文件恢复

`一点建议 : 业务系统,rm 删除后,没有立即关机,运行的系统会持续覆盖误删数据.所以对于重要数据,误删后请立即关机`

**[foremost](http://foremost.sourceforge.net/)**
```bash
apt-get install -y foremost
rm -f /dev/sdb1/photo1.png

foremost -t png -i /dev/sdb1
# 恢复完成后会在当前目录建立一个 output 目录,在 output 目录下会建立 png 子目录下会包括所有可以恢复的 png 格式的文件.
# 需要说明的是 png 子目录下会包括的 png 格式的文件名称已经改变,另外 output 目录下的 audit.txt 文件是恢复文件列表.
```

**[extundelete](http://extundelete.sourceforge.net/)**
```bash
apt-get install -y extundelete
mkdir -p /backupdate/deldate
mkfs.ext4 /dev/sdd1
mount /dev/sdd1 /backupdate
cd /backupdate/deldate
touch del1.txt
echo " test 1" > del1.txt
md5sum del1.txt             # 获取文件校验码
66fb6627dbaa37721048e4549db3224d  del1.txt
rm -fr /backupdate/*
umount /backupdate          # 卸载文件系统或者挂载为只读

extundelete /dev/sdd1 --inode 2                                 #查询恢复数据信息,注意这里的 --inode 2 这里会扫描分区 :
extundelete /dev/sdd1 --restore-file del1.txt                   # 如果恢复一个目录
extundelete /dev/sdd1 --restore-directory /backupdate/deldate   # 恢复所有文件
extundelete /dev/sdd1 --restore-all                             # 获取恢复文件校验码,对比检测是否恢复成功
md5sum RECOVERED_FILES/ del1.txt
66fb6627dbaa37721048e4549db3224d  RECOVERED_FILES/del1.txt
```

**[ext3grep](https://code.google.com/archive/p/ext3grep/downloads)**

如果被误删的文件在根分区,那么你最好重启计算机,进入单用户模式,以只读的方式挂载根分区,然后再进行恢复.

进入单用户模式后,根分区还是以读写方式 mount 的,用下面的命令,把挂载方式由读写(rw)改为只读(ro):  `mount -o ro,remount / `

如果被删除的文件不是根分区,也可以用 unmount 的方式将该分区卸载.假设文件在分区 /dev/sda3中,该分区挂载到 /home,那么我们用下面的命令来卸载: `umount /dev/sda3 `

当然,在卸载前要保证没有程序在访问该分区,否则卸载会失败.所以,一般推荐进入单用户模式来恢复文件.

*安装*

访问 https://code.google.com/archive/p/ext3grep/downloads 下载源代码,这里以 ext3grep-0.10.2.tar.gz 为例
```bash
yum install -y e2fsprogs
yum install -y e2fsprogs-devel
tar zxf ext3grep-0.10.2.tar.gz
cd ./ext3grep-0.10.2
./configure
make
make install
```

如果 make 出错,修改 src/ext3.h
```C
// ext3grep -- An ext3 file system investigation and undelete tool
//
//! @file ext3.h Declaration of ext3 types and macros.
//
// Copyright (C) 2008, by
//
// Carlo Wood, Run on IRC <carlo@alinoe.com>
// RSA-1024 0x624ACAD5 1997-01-26                    Sign & Encrypt
// Fingerprint16 = 32 EC A7 B6 AC DB 65 A6  F6 F6 55 DD 1C DC FF 61
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#ifndef EXT3_H
#define EXT3_H
#ifdef _LINUX_EXT2_FS_H
#error please include this file before any other includes of ext2fs/ext2_fs.h
#endif
#define s_clusters_per_group s_frags_per_group

// Use the header files from e2progs (http://e2fsprogs.sourceforge.net)
// We can use these headers and then everything named ext2 or ext3.
#include <ext2fs/ext2_fs.h>			// Definitions of ext2, ext3 and ext4.

// All of the following is backwards compatible, so we can use the EXT2 versions.
#define EXT3_BLOCK_SIZE		EXT2_BLOCK_SIZE
#define EXT3_FRAG_SIZE		EXT2_FRAG_SIZE
#define EXT3_BLOCKS_PER_GROUP	EXT2_BLOCKS_PER_GROUP
#define EXT3_INODES_PER_GROUP	EXT2_INODES_PER_GROUP
#define EXT3_FIRST_INO		EXT2_FIRST_INO
#define EXT3_INODE_SIZE		EXT2_INODE_SIZE
#define EXT3_BLOCK_SIZE_BITS	EXT2_BLOCK_SIZE_BITS
#define EXT3_DESC_PER_BLOCK	EXT2_DESC_PER_BLOCK
#define EXT3_DIR_ROUND		EXT2_DIR_ROUND
#define EXT3_DIR_REC_LEN	EXT2_DIR_REC_LEN
#define EXT3_FT_DIR		EXT2_FT_DIR
#define EXT3_FT_UNKNOWN		EXT2_FT_UNKNOWN
#define EXT3_FT_MAX		EXT2_FT_MAX
#define EXT3_MAX_BLOCK_SIZE	EXT2_MAX_BLOCK_SIZE
#define EXT3_NDIR_BLOCKS	EXT2_NDIR_BLOCKS
#define EXT3_IND_BLOCK		EXT2_IND_BLOCK
#define EXT3_DIND_BLOCK		EXT2_DIND_BLOCK
#define EXT3_TIND_BLOCK		EXT2_TIND_BLOCK
#define EXT3_VALID_FS		EXT2_VALID_FS
#define EXT3_ERROR_FS		EXT2_ERROR_FS
#define EXT3_FT_REG_FILE	EXT2_FT_REG_FILE
#define EXT3_FT_CHRDEV		EXT2_FT_CHRDEV
#define EXT3_FT_BLKDEV		EXT2_FT_BLKDEV
#define EXT3_FT_FIFO		EXT2_FT_FIFO
#define EXT3_FT_SOCK		EXT2_FT_SOCK
#define EXT3_FT_SYMLINK		EXT2_FT_SYMLINK
#define EXT3_N_BLOCKS		EXT2_N_BLOCKS
#define EXT3_DIR_PAD		EXT2_DIR_PAD
#define EXT3_ROOT_INO		EXT2_ROOT_INO
#define EXT3_I_SIZE		EXT2_I_SIZE
#define EXT3_FEATURE_COMPAT_DIR_PREALLOC	EXT2_FEATURE_COMPAT_DIR_PREALLOC
#define EXT3_FEATURE_COMPAT_IMAGIC_INODES	EXT2_FEATURE_COMPAT_IMAGIC_INODES
#define EXT3_FEATURE_COMPAT_EXT_ATTR		EXT2_FEATURE_COMPAT_EXT_ATTR
#define EXT3_FEATURE_COMPAT_RESIZE_INODE	EXT2_FEATURE_COMPAT_RESIZE_INODE
#define EXT3_FEATURE_COMPAT_DIR_INDEX		EXT2_FEATURE_COMPAT_DIR_INDEX
#define EXT3_FEATURE_INCOMPAT_COMPRESSION	EXT2_FEATURE_INCOMPAT_COMPRESSION
#define EXT3_FEATURE_INCOMPAT_FILETYPE		EXT2_FEATURE_INCOMPAT_FILETYPE
#define EXT3_FEATURE_INCOMPAT_META_BG		EXT2_FEATURE_INCOMPAT_META_BG
#define EXT3_FEATURE_RO_COMPAT_SPARSE_SUPER	EXT2_FEATURE_RO_COMPAT_SPARSE_SUPER
#define EXT3_FEATURE_RO_COMPAT_LARGE_FILE	EXT2_FEATURE_RO_COMPAT_LARGE_FILE
#define EXT3_FEATURE_RO_COMPAT_BTREE_DIR	0x0004
typedef ext2_super_block ext3_super_block;
typedef ext2_group_desc ext3_group_desc;
typedef ext2_inode ext3_inode;
typedef ext2_dir_entry_2 ext3_dir_entry_2;

// Get declaration of journal_superblock_t
#include <ext2fs/ext2fs.h>
// This header is a copy from e2fsprogs-1.40.7 except that the type
// of 'journal_revoke_header_t::r_count' was changed from int to __s32.
#include "kernel-jbd.h"

#ifndef USE_PCH
#include <stdint.h>
#endif

extern uint32_t inode_count_;

// This (POD) struct protects it's members so we
// can do access control for debugging purposes.

struct Inode : protected ext3_inode {
  public:
    __u16 mode(void) const { return i_mode; }
    __u16 uid_low(void) const { return i_uid_low; }
    off_t size(void) const { return EXT3_I_SIZE(this); }
    __u32 atime(void) const { return i_atime; }
    __u32 ctime(void) const { return i_ctime; }
    __u32 mtime(void) const { return i_mtime; }
    __u32 dtime(void) const { return i_dtime; }
    __u16 gid_low(void) const { return i_gid_low; }
    __u16 links_count(void) const { return i_links_count; }
    __u32 blocks(void) const { return i_blocks; }
    __u32 flags(void) const { return i_flags; }
    __u32 const* block(void) const { return i_block; }
    __u32 generation(void) const { return i_generation; }
    __u32 file_acl(void) const { return i_file_acl; }
    __u32 dir_acl(void) const { return i_dir_acl; }
    __u32 faddr(void) const { return i_faddr; }
    __u16 uid_high(void) const { return i_uid_high; }
    __u16 gid_high(void) const { return i_gid_high; }

    #ifndef i_reseved2
    #define i_reserved2 osd2.hurd2.h_i_author
#endif
    __u32 reserved2(void) const { return i_reserved2; }
    void set_reserved2(__u32 val) { i_reserved2 = val; }

    // Returns true if this inode is part of an ORPHAN list.
    // In that case, dtime is overloaded to point to the next orphan and contains an inode number.
    bool is_orphan(void) const
    {
       // This relies on the fact that time_t is larger than the number of inodes.
       // Assuming we might deal with files as old as five years, then this would
       // go wrong for partitions larger than ~ 8 TB (assuming a block size of 4096
       // and twice as many blocks as inodes).
       return i_links_count == 0 && i_atime && i_dtime < i_atime && i_dtime <= inode_count_;
    }

    // This returns true if dtime() is expected to contain a date.
    bool has_valid_dtime(void) const
    {
      return i_dtime && !is_orphan();
    }

    // This returns true if the inode appears to contain data refering to a previously
    // deleted file, directory or symlink but does not contain the block list anymore.
    // That means it will return false for orphan-ed inodes, although they are basically
    // (partially) deleted.
    bool is_deleted(void) const
    {
      return i_links_count == 0 && i_mode && (i_block[0] == 0 ||
                                              !((i_mode & 0xf000) == 0x4000 || (i_mode & 0xf000) == 0x8000));
    }
};

#endif // EXT3_H
```

*使用*

在开始恢复前,选择一个目录来存放被恢复的文件.ext3grep 程序会在当前目录下创建一个名为 RESTORED_FILES 的目录来存放被恢复的文件.因此在运行 ext3grep 命令前,先要切换到一个你可读写的目录中.

因为进入了单用户模式,并且将根分区设成了只读,那么只能把恢复出来的文件放在U盘中了.因此,先 cd /mnt 进入U盘目录.如果你有幸记得你误删除的文件名及其路径的话,就可以直接用下面的命令进行恢复了:
```bash
ext3grep /dev/your-device --restore-file path/to/your/file/filename
# 需要注意的是,上面的文件路径,是在该分区上文件路径.假设我们要恢复 /dev/sda3 分区上文件,这个分区原来的安装点是 /home,现在想恢复文件 /home//vi/tips.xml,那么输入的命令应该是:

ext3grep /dev/sda3 --restore-file /vi/tips.xml

# 如果你忘记了文件名,或者你误删除的是一个目录而你无法记全该目录中的文件,你可以先用下面的命令查询一下文件名:
ext3grep /dev/sda3 --dump-names | tee filename.txt

上面的命令把 ext3grep 命令的输出记录到文件 filename.txt 中,你可以慢慢查看,或者使用 grep 命令过滤出你需要的信息.

当你知道了目录/文件的信息后,就可以用上面说的命令进行恢复了.

# 这款软件不能按目录恢复文件,只能执行恢复全部命令:
ext3grep /dev/sda3 --restore-all
```

*binlog*

开启 Binlog,让 ext3grep 从 Binlog 中恢复,对数据库场景有用.

---

# 系统
## 密码重置

### centos7

1. 在启动菜单选择启动内核,按 e 编辑,找到 rhgb quiet 一行,把 `rhgb quiet` 替换为 `init=/bin/bash` (临时生效)
2. 按 `CTRL+X` 进入单用户模式
3. 挂载根文件系统: `mount -o remount,rw /`
4. 使用 `passwd` 命令直接设置 root 密码: `passwd root` 输入两次新密码.
5. 最后,执行如下命令更新 SELinux: `touch /.autorelabel`
6. 进入正常模式: `exec /sbin/init`  现在可以使用新设置的 root 密码登录了.

### Ubuntu14

- 方案一
    1. 重启电脑长按 shift 键直到进入进入 GRUB 引导模式，选择第二行 Ubuntu 高级选项, 选中直接回车
    2. 按 e 进入（recovery mode） 编译kernel进行启动参数
    3. 倒数第四行，删除 `recovery nomodeset` ,添加 `quiet splash rw init=/bin/bash` 。然后按 F10, 启动。
    4. 运行后系统直接进入 root mode，输入：`passwd`

- 方案二
    1. 重启电脑长按 shift 键直到进入进入 GRUB 引导模式，选择第二行 Ubuntu 高级选项, 选中直接回车
    2. 选择一个括号里是 recovery mode 的系统发行编号，回车进入
    3. 选择 root 项，回车
    4. 最下方输入 root 密码，回车，便会切换到 root 用户；此时需要输入此条命令 `mount -o remount,rw /` 回车，再用 `passwd 用户名` 便可以修改密码了；
    5. 继续输入 `exit` 返回，选中 `resume`，回车，此时会跳出一个确认界面，再回车即可

---

## 会话

### 查

```bash
who     # 查看当前登录用户
w       # 查看登录用户行为
last    # 查看登录用户历史
```

### 防

```bash
pkill -u linfengfeiye   # 直接剔除用户
ps -ef| grep pts/0      # 得到用户登录相应的进程号 pid 后执行
kill -9 pid             # 安全剔除用户
```

### 修改账户超时值,设置自动注销时间

```
vim /etc/profile

TMOUT=600
```

### 命令记录

```bash
histroy                 # 查看 root 的历史命令
```
进入 `/home` 各帐号目录下的 `.bash_history` 查看普通帐号的历史命令

**history优化**
```bash
# 保存1万条命令
sed -i 's/^HISTSIZE=1000/HISTSIZE=10000/g' /etc/profile

# 记录IP，在 /etc/profile 的文件尾部添加如下行数配置信息
USER_IP=`who -u am i 2>/dev/null | awk '{print $NF}' | sed -e 's/[()]//g'`
if [ "$USER_IP" = "" ]
then
USER_IP=`hostname`
fi
export HISTTIMEFORMAT="%F %T $USER_IP `whoami` "
shopt -s histappend
export PROMPT_COMMAND="history -a"

# 让配置生效
source /etc/profile
```

---

## 开机启动

### 查看开机启动服务

```bash
chkconfig                   # 查看开机启动服务命令
chkconfig --list | grep "3:启用\|3:开\|3:on\|5:启用\|5:开\|5:on"

ls /etc/init.d              # 查看开机启动配置文件命令
cat /etc/rc.local           # 查看 rc 启动文件
ls /etc/rc.d/rc[0~6].d

runlevel                    # 查看运行级别命令
```

### 查看计划任务

```bash
crontab -l                  # 计划任务列表
ls -alh /var/spool/cron     # 默认编写的 crontab 文件会保存在 /var/spool/cron/用户名 下
ls -al /etc/ | grep cron
ls -al /etc/cron*
cat /etc/cron*
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny
cat /etc/crontab
cat /etc/anacrontab
cat /var/spool/cron/crontabs/root
```

---

## 账号

### 异常查找
```bash
awk -F: '{if($3==0||$4==0)print $1}' /etc/passwd            # 查看 UID\GID 为0的帐号
awk -F: '{if($7!="/usr/sbin/nologin"&&$7!="/sbin/nologin")print $1}' /etc/passwd # 查看能够登录的帐号
awk '/\$1|\$6/{print $1}' /etc/shadow                       # 查询可以远程登录的帐号信息
lastlog                                                     # 系统中所有用户最近一次登录信息
lastb                                                       # 显示用户错误的登录列表
users                                                       # 打印当前登录的用户，每个用户名对应一个登录会话。如果一个用户不止一个登录会话，其用户名显示相同次数
```

### 异常设置

**/etc/passwd**
- 若用户 ID=0,则表示该用户拥有超级用户的权限
- 检查是否有多个 ID=0
- 禁用或删除多余的账号

**/etc/login.defs**
```bash
PASS_MAX_DAYS   90              # 用户的密码最长使用天数
PASS_MIN_DAYS   0               # 两次修改密码的最小时间间隔
PASS_MIN_LEN    7               # 密码的最小长度
PASS_WARN_AGE   9               # 密码过期前多少天开始提示
```

### 当查到异常用户时,需要立即禁用
```bash
usermod -L user     # 禁用帐号，帐号无法登录，/etc/shadow第二栏为!开头
userdel user        # 删除user用户
userdel -r admin    # 将删除user用户，并且将/home目录下的admin目录一并删除
```

### 安全配置

**设置账户锁定登录失败锁定次数、锁定时间**
```bash
vim /etc/pam.d/system-auth

auth required pam_tally.so onerr=fail deny=6 unlock_time=300  # 设置为密码连续输错6次,锁定时间300秒
auth required pam_tally.so deny=2 unlock_time=60 even_day_root root_unlock_time=60
```

### 安全审计

```bash
ps -ef | grep auditd            # 查看是否开启系统安全审计功能
more /etc/audit/audit.rules     # 查看审计的规则文件
    - w 文件 -p 权限(r读 w写 x执行 a修改文件属性) -k 关键字
    - w /etc/passwd -p wa -k passwd_changes             # 对重要文件的操作行为进行监控
    - a -系列动作 -S 系统调用名称 -F 字段-值 -k 关键字
    - a exit,always -S mount -S umount                  # 对系统调用进行监控
more /etc/audit/auditd.conf     # 查看安全事件配置

ausearch -i | less              # 查看审计日志
more /var/log/audit/audit.log   # 查看审计日志
```

**audit**

linux audit 子系统是一个用于收集记录系统、内核、用户进程发生的行为事件的一种安全审计系统。该系统可以可靠地收集有关上任何与安全相关（或与安全无关）事件的信息，它可以帮助跟踪在系统上执行过的一些操作。

audit 和 syslog 有本质区别。syslog 记录的信息有限，主要目的是软件调试，对于用户的操作行为（如某用户修改删除了某文件）却无法通过这些日志文件来查看。而 audit 的目的则不同，它是 linux 安全体系的重要组成部分，是一种 “被动” 的防御体系。

```bash
yum install audit*.* -y         # 安装 audit
service auditd start            # 启动 audit
service auditd status           # 查看 audit 状态

# 开启了 autid 服务后，所有的审计日志会记录在 /var/log/audit/audit.log 文件中。
```

audit 安装后会生成 2 个配置文件:
* /etc/audit/auditd.conf
* /etc/audit/audit.rules

具体配置信息请查看 [文件](./笔记/文件.md#etc)

audit 常用命令
```bash
ausearch    # 查询 audit log 工具
aureport    # 输出 audit 系统报告

auditctl -l # 查看 audit 规则
aureport --user
aureport --file
aureport --summary

# 配置记录命令rm命令执行
auditctl -w /bin/rm -p x -k removefile
```

---

## SELinux

**关闭 SELinux**
- 需要重启
	```vim
	vim /etc/selinux/config

	SELINUX=disabled
	```

- 不需要重启

	`setenforce 0`

---

## 进程

### 进程定位

```bash
ps -aux         # 列出所有进程以及相关信息命令
ps -ef
service --status-all | grep running
top             # 总览系统全面信息命令
pidof name      # 定位程序的 pid
pidof -x name   # 定位脚本的 pid
lsof -g gid     # 寻找恶意文件关联的 lib 文件
```

### 进程限制

```bash
ulimit -u 20    # 临时性允许用户最多创建 20 个进程,预防类似 fork 炸弹
```

```vim
vim /etc/security/limits.conf
    user1 - nproc 20  # 退出后重新登录,就会发现最大进程数已经更改为 20 了
```

### 负载

**文章**
- [Linux系统清除缓存](https://www.cnblogs.com/jiu0821/p/9854704.html)

**查询负载、进程监控**

```bash
ps aux | grep Z                                         # 列出进程表中所有僵尸进程
ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3|head   # 获取占用CPU资源最多的10个进程
ps aux|head -1;ps aux|grep -v PID|sort -rn -k +4|head   # 获取占用内存资源最多的10个进程
```

**清理缓存**

```bash
sync    # sync 命令做同步,以确保文件系统的完整性,将所有未写的系统缓冲区写到磁盘中,包含已修改的 i-node、已延迟的块 I/O 和读写映射文件.否则在释放缓存的过程中,可能会丢失未保存的文件.
echo 1 > /proc/sys/vm/drop_caches   # 清理 pagecache(页面缓存)
echo 2 > /proc/sys/vm/drop_caches   # 清理 dentries(目录缓存)和inodes
echo 3 > /proc/sys/vm/drop_caches   # 清理 pagecache、dentries 和 inodes
sync
```

---

## 系统完整性

通过 rpm 自带的 -Va 来校验检查所有的 rpm 软件包，查看哪些命令是否被替换了
```bash
rpm -Va
# 如果一切均校验正常将不会产生任何输出，如果有不一致的地方，就会显示出来，输出格式是8位长字符串，每个字符都用以表示文件与RPM数据库中一种属性的比较结果 ，如果是. (点) 则表示测试通过。

验证内容中的8个信息的具体内容如下：
- S         文件大小是否改变
- M         文件的类型或文件的权限（rwx）是否被改变
- 5         文件MD5校验是否改变（可以看成文件内容是否改变）
- D         设备中，从代码是否改变
- L         文件路径是否改变
- U         文件的属主（所有者）是否改变
- G         文件的属组是否改变
- T         文件的修改时间是否改变
```

**还原替换命令**
```bash
rpm  -qf /bin/ls  # 查询 ls 命令属于哪个软件包
mv  /bin/ls /tmp  # 先把 ls 转移到 tmp 目录下，造成 ls 命令丢失的假象
rpm2cpio /mnt/cdrom/Packages/coreutils-8.4-19.el6.i686.rpm | cpio -idv ./bin/ls # 提取 rpm 包中 ls 命令到当前目录的/bin/ls下
cp /root/bin/ls  /bin/ # 把 ls 命令复制到 /bin/ 目录,修复文件丢失
```

---

## 日志

**系统日志**
- 内容见 [日志](./笔记/日志.md)

对于日志文件的保护
```bash
chattr +a xxx
chattr +a -R xxx # 递归式增加a权限
# a选项为append (追加) only ,即给日志文件加上a权限后,将只可以追加,不可以删除和修改之前的内容。
```

**web日志**
- 内容见 [取证](../../Security/BlueTeam/取证.md#中间件服务器程序日志) 中间件服务器程序日志部分

**数据库日志**
- 内容见 [取证](../../Security/BlueTeam/取证.md#数据库取证) 数据库取证部分

---

# Net
## 端口

**查**
```bash
getent services     # 查看所有服务的默认端口名称和端口号

lsof -i -P          # 显示进程使用端口使用情况
lsof -i:22          # 只查 22 端口

ss -tnlp
ss -tnlp | grep ssh
ss -tnlp | grep ":22"

netstat -tnlp
netstat -tnlp | grep ssh

nmap -sV -p 22 localhost
```

更多内容查看 [网络](./笔记/信息.md#网络)

**防**
- [EtherDream/anti-portscan: 使用 iptables 防止端口扫描](https://github.com/EtherDream/anti-portscan)
    ```bash
    git clone https://github.com/EtherDream/anti-portscan
    cd anti-portscan
    vim install.sh # 修改需要打开的端口
    sh install.sh
    ```

---

## Firewall

**查**
```bash
firewall-cmd --list-services    # 查看防火墙设置
firewall-cmd --state                    # 显示防火墙状态
firewall-cmd --get-zones                # 列出当前有几个 zone
firewall-cmd --get-active-zones         # 取得当前活动的 zones
firewall-cmd --get-default-zone         # 取得默认的 zone
firewall-cmd --get-service              # 取得当前支持 service
firewall-cmd --get-service --permanent  # 检查下一次重载后将激活的服务

firewall-cmd --zone=public --list-ports # 列出 zone public 端口
firewall-cmd --zone=public --list-all   # 列出 zone public 当前设置

cat /etc/hosts.deny                     # tcp_Wrappers 防火墙的配置文件,详情见 文件.md
cat /etc/hosts.allow                    # tcp_Wrappers 防火墙的配置文件,详情见 文件.md
```

**防**
```bash
firewall-cmd --permanent --zone=public --remove-service=ssh
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=internal --add-source=1.1.1.1
firewall-cmd --reload           # 重启防火墙服务
```

在上面的配置中,如果有人尝试从 1.1.1.1 去 ssh,这个请求将会成功,因为这个源区域(internal)被首先应用,并且它允许 ssh 访问.

如果有人尝试从其它的地址,如 2.2.2.2,去访问 ssh,它不是这个源区域的,因为和这个源区域不匹配.因此,这个请求被直接转到接口区域(public),它没有显式处理 ssh,因为,public 的目标是 default,这个请求被传递到默认动作,它将被拒绝.

如果 1.1.1.1 尝试进行 http 访问会怎样？源区域(internal)不允许它,但是,目标是 default,因此,请求将传递到接口区域(public),它被允许访问.

现在,让我们假设有人从 3.3.3.3 拖你的网站.要限制从那个 IP 的访问,简单地增加它到预定义的 drop 区域,正如其名,它将丢弃所有的连接:
```bash
firewall-cmd --permanent --zone=drop --add-source=3.3.3.3
firewall-cmd --reload
```
下一次 3.3.3.3 尝试去访问你的网站,firewalld 将转发请求到源区域(drop).因为目标是 DROP,请求将被拒绝,并且它不会被转发到接口区域(public).

`注:配置了 firewalld 服务后一定要去检查下规则,因为他不会阻掉正在进行的连接,只能阻掉配置命令后进行的连接,所以你不知道你的ssh会话会不会一断就再也连不上了,血的教训🤣`

---

## iptable

**查询表中的规则**

```bash
iptables -t raw -L      # 列出所有 raw 表中的所有规则
iptables -t mangle -L   # 列出 mangle 表中所有规则
iptables -t nat -L      # 列出 nat 表中所有规则
iptables -t filter -L   # 列出 filter 表中所有规则
```

**查看不同的链中的规则**

```bash
iptables -L INPUT       # 只看 filter 表中（默认 - t 是 filter 表）input 链的规则
iptables -vL INPUT      # 只看 filter 表中（默认 - t 是 filter 表）input 链的规则详情
iptables -nvL INPUT     # 只看 filter 表中（默认 - t 是 filter 表）input 链的规则详情，同时不对 IP 地址进行名称反解析，直接显示 IP
iptables --line-number -nvL INPUT  # 只看 filter 表中（默认 - t 是 filter 表）input 链的规则详情，同时不对 IP 地址进行名称反解析，直接显示 IP，每行加行标
```

---

## nftables

**查看规则汇总**

```bash
nft list tables [<family>]
nft list table [<family>] <name> [-n] [-a]
nft list tables  # 列出所有表
nft list table family table # 列出指定表中的所有链和规则
nft list table inet filter # 要列出inet簇中f
nft list chain family table chain  # 列出一个链中的所有规则
nft list chain inet filter output  # 要列出inet中filter表的output链中的所有规则
```

**nft表管理**

```bash
nft add table family table  # 创建一个新的表
nft list tables  # 列出所有表
nft list table family table # 列出指定表中的所有链和规则
nft list table inet filter # 要列出inet簇中filter表中的所有规则
nft delete table family table  # 删除一个表
nft flush table family table # 要清空一个表中的所有规则
```

**nft链管理**

```bash
nft add chain family table chain   # 将名为chain的常规链添加到名为table的表中
nft add chain inet filter tcpchain   # 例如，将名为tcpchain的常规链添加到inet簇中名为filter的表中
nft add chain family table chain { type type hook hook priority priority \; }   # 添加基本链，需要指定钩子和优先级值
nft list chain family table chain  # 列出一个链中的所有规则
nft list chain inet filter output  # 要列出inet中filter表的output链中的所有规则
nft chain family table chain { [ type type hook hook device device priority priority \; policy <policy> \; ] }  # 要编辑一个链，只需按名称调用并定义要更改的规则
nft chain inet filter input { policy drop \; }   # 将默认表中的input链策略从accept更改为drop
nft delete chain family table chain # 删除一个链,要删除的链不能包含任何规则或者跳转目标。
nft flush chain family table chain # 清空一个链的规则
```

**添加规则**

```bash
nft add rule family table chain handle handle statement  # 将一条规则添加到链中
nft insert rule family table chain handle handle statement # 将规则插入到指定位置,如果未指定handle，则规则插入到链的开头。
```

**删除规则**

```bash
# 下面命令确定一个规则的句柄，然后删除。--number参数用于查看数字输出，如未解析的IP地址。
nft --handle --numeric list chain inet filter input
nft delete rule inet fltrTable input handle 10

# 可以用nft flush table命令清空表中的所有的链。可以用nft flush chain或者nft delete rule命令清空单个链。
# 第一个命令清空foo表中的所有链。第二个命令清空ip foo表中的bar链。第三个命令删除ip6 foo表bar两种的所有规则。
nft flush table foo
nft flush chain foo bar
nft delete rule ip6 foo bar
```

**自动重载**

```bash
清空当前规则集：

# echo "flush ruleset" > /tmp/nftables
导出当前规则集：

# nft list ruleset >> /tmp/nftables
可以直接修改/tmp/nftables文件，使更改生效则运行：

# nft -f /tmp/nftables
```

---

## 禁ping

**临时性,重启后失效**
```bash
echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_all     # 允许 ping
echo 1 >/proc/sys/net/ipv4/icmp_echo_ignore_all     # 禁止 ping
```

**长期性**
```bash
vim /etc/rc.d/rc.local

echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all
```

或

```bash
vim /etc/sysctl.conf

net.ipv4.icmp_echo_ignore_all=1
```

`sysctl -p` 使新配置生效

---

## SSH

**文章**
- [Multiple Ways to Secure SSH Port](http://www.hackingarticles.in/multiple-ways-to-secure-ssh-port/)

**查**
- **查询可以远程登录的帐号信息**
    ```bash
    awk '/\$1|\$6/{print $1}' /etc/shadow
    ```

- **查看尝试暴力破解机器密码的人**
    ```bash
    # Debian 系的发行版
    grep "Failed password for root" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | more

    # Red Hat 系的发行版
    grep "Failed password for root" /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr | more
    ```

- **查看暴力猜用户名的人**
    ```bash
    # Debian 系的发行版
    grep "Failed password for invalid user" /var/log/auth.log | awk '{print $13}' | sort | uniq -c | sort -nr | more

    # Red Hat 系的发行版
    grep "Failed password for invalid user" /var/log/secure | awk '{print $13}' | sort | uniq -c | sort -nr | more
    grep "Failed password" /var/log/secure | awk {'print $9'} | sort | uniq -c | sort -nr
    grep -o "Failed password" /var/log/secure|uniq -c
    ```

- **IP 信息**
    ```bash
    # Debian 系的发行版
    grep "Failed password for root" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | more

    # Red Hat 系的发行版
    grep "Failed password for root" /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr | more
    ```

- **登录成功**
    ```bash
    # Debian 系的发行版
    grep "Accepted " /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | more

    # Red Hat 系的发行版
    grep 'Accepted' /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr
    grep "Accepted " /var/log/secure | awk '{print $1,$2,$3,$9,$11}'
    grep "Accepted " /var/log/secure* | awk '{print $1,$2,$3,$9,$11}'
    ```

- **私钥**
    ```bash
    ll -al /etc/ssh/
    ll -al /root/.ssh/
    ```

**防**
- **ping 钥匙**
    - [使用 ping 钥匙临时开启 SSH:22 端口,实现远程安全 SSH 登录管理就这么简单](https://www.cnblogs.com/martinzhang/p/5348769.html)

    ```bash
    # 规则1 只接受Data为1078字节的ping包,并将源IP记录到自定义名为sshKeyList的列表中
    iptables -A INPUT -p icmp -m icmp --icmp-type 8 -m length --length 1078 -m recent --name sshKeyList --set -j ACCEPT

    # 规则2 若30秒内发送次数达到6次(及更高),当发起SSH:22新连接请求时拒绝
    iptables -A INPUT -p tcp -m tcp --dport 22 --syn -m recent --name sshKeyList --rcheck --seconds 30 --hitcount 6 -j DROP

    # 规则3 若30秒内发送次数达到5次,当发起SSH:22新连接请求时放行
    iptables -A INPUT -p tcp -m tcp --dport 22 --syn -m recent --name sshKeyList --rcheck --seconds 30 --hitcount 5 -j ACCEPT

    # 规则4 对于已建立的连接放行
    iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT

    # 规则5 老规矩:最后的拒绝
    iptables -A INPUT -j DROP
    ```

- **更改默认端口**

    修改 `/etc/ssh/sshd_config` 文件,将其中的 Port 22 改为指定的端口

    `!!! 警告,记得防火墙要先放行端口,不然你的远程主机就连不上了🤣!!!`
    ```
    service ssh restart
    ```

- **配置使用 RSA 私钥登录**

    1. 先生成你的客户端的密钥,包括一个私钥和公钥
        ```bash
        ssh-keygen -t rsa
        ```

    2. 把公钥拷贝到服务器上,注意,生成私钥的时候,文件名是可以自定义的,且可以再加一层密码,所以建议文件名取自己能识别出哪台机器的名字.
        ```bash
        cd /root/.ssh
        scp id_rsa.pub root@XX.XX.XX.XX:~/
        ```

    3. 然后在服务器上,你的用户目录下,新建 `.ssh` 文件夹,并将该文件夹的权限设为 700
        ```bash
        cd
        mkdir .ssh
        chmod 700 .ssh
        ```

    4. 新建一个 authorized_keys,这是默认允许的 key 存储的文件.如果已经存在,则只需要将上传的 id_rsa.pub 文件内容追加进去即可,如果不存在则新建并改权限为 400 即可. 然后编辑 ssh 的配置文件
        ```bash
        mv id_rsa.pub .ssh
        cd .ssh
        cat id_rsa.pub >> authorized_keys
        chmod 600 authorized_keys
        ```
        ```bash
        vim /etc/ssh/sshd_config

        RSAAuthentication yes                           # RSA 认证
        PubkeyAuthentication yes                        # 开启公钥验证
        AuthorizedKeysFile /root/.ssh/authorized_keys   # 验证文件路径
        PasswordAuthentication no                       # 禁止密码登录
        ```

        `service sshd restart` 重启 sshd 服务

    5. 测试使用私钥登录
        ```bash
        ssh root@x.x.x.x -i id_rsa
        ```

- **禁止 root 用户登录**

    可以建一个用户来专门管理,而非直接使用 root 用户,修改 /etc/ssh/sshd_config
    ```vim
    vim /etc/ssh/sshd_config

    PermitRootLogin no
    ```

- **使用 Fail2ban**
    - [fail2ban](https://github.com/fail2ban/fail2ban) ,详细搭建步骤请移步 [Power-Linux](./Power-Linux.md##Fail2ban)

- **SSH 陷阱**
    - [skeeto/endlessh](https://github.com/skeeto/endlessh) - 蓝队 SSH 陷阱

---

## 文件共享

**NFS服务**

配置文件
```
/etc/exports
```

**TFTP服务**

配置文件
```
/etc/default/tftpd-hpa

/etc/xinetd.d/tftp
```

**samba服务**

配置文件
```
/etc/samba/smb.conf
```

---

# 加固

## 查后门

**相关文章**
- [linux常见backdoor及排查技术](https://xz.aliyun.com/t/4090)

**添加 root 权限后门用户**

检查 `/etc/passwd` 文件是否有异常

**vim 后门**

检测对应 vim 进程号虚拟目录的 map 文件是否有 python 字眼.

查看连接情况 `netstat -antlp`

例如发现 vim pid 为 12
```
file /proc/12/exe
more /proc/12/cmdline
more /proc/12/maps | grep python
```

**strace 记录**

通过排查 shell 的配置文件或者 `alias` 命令即可发现,例如 `~/.bashrc` 和 `~/.bash_profile` 文件查看是否有恶意的 alias 问题.

**定时任务和开机启动项**

 一般通过 `crontab -l` 命令即可检测到定时任务后门.不同的 linux 发行版可能查看开机启动项的文件不大相同,Debian 系 linux 系统一般是通过查看 `/etc/init.d` 目录有无最近修改和异常的开机启动项.而 Redhat 系的 linux 系统一般是查看 `/etc/rc.d/init.d` 或者 `/etc/systemd/system` 等目录.

**预加载型动态链接库后门 ld.so.preload**

通过 `strace` 命令去跟踪预加载的文件是否为 `/etc/ld.so.preload` ,以及文件中是否有异常的动态链接库.以及检查是否设置 LD_PRELOAD 环境变量等.注意:在进行应急响应的时候有可能系统命令被替换或者关键系统函数被劫持(例如通过预加载型动态链接库后门),导致系统命令执行不正常,这个时候可以下载 busybox.下载编译好的对应平台版本的 busybox,或者下载源码进行编译通过U盘拷贝到系统上,因为 busybox 是静态编译的,不依赖于系统的动态链接库,busybox 的使用类似如下 busybox ls,busybox ps -a.

**内核级 rootkit**

可以通过 unhide 等工具进行排查,更多内容见 [应急](../../Security/BlueTeam/应急.md#rootkit)

**深信服 Web 后门扫描**

http://edr.sangfor.com.cn/backdoor_detection.html

---

## 杀毒

**[ClamavNet](https://www.clamav.net/downloads)**

---

## 配置 pam.d 策略

- [pam](./实验/pam.md)
- [认证](./笔记/认证.md#pam)
