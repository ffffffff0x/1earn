# Mac-Plan

---

## 快捷键

- 锁屏 : Control + Command + Q
- 截图 : Shift + Command + 5
- 刷新 : Command + R
- 行首 : Command + 左键
- 行末 : Command + 右键
- 输入Emoji 表情和颜文字 : Control + Command + space

---

## 代理

```bash
# 请根据自己的代理软件进行调整!!!!
export https_proxy=http://127.0.0.1:7890;export http_proxy=http://127.0.0.1:7890;export all_proxy=socks5://127.0.0.1:7890
```

---

## 权限

由于 macOS 默认情况下只允许运行可信任签名的应用，如果 macOS 阻止运行该软件，请打开 macOS 终端，在新建的终端 Shell 中输入：
```bash
sudo spctl --master-disable
```

由于调用了sudo权限，你可能需要输入密码，会输出如下提示：
```
Password:
```
此时你需要输入密码，在 Shell 中输入的密码是不可见的，输入完毕后请按回车键。

---

针对 "已损坏" 的解决办法

苹果系统有一个 GateKeeper 保护机制。

从互联网上下载来的文件，会被自动打上 com.apple.quarantine 标志，我们可以理解为 "免疫隔离"。

系统根据这个附加属性对这个文件作出限制。

随着版本不同，MacOS 对 com.apple.quarantine 的限制越来越严格，在较新 的 MacOS 中，会直接提示 "映像损坏" 或 "应用损坏" 这类很激进的策略。

我们可以通过手动移除该选项来解决此问题。
```
sudo xattr -r -d com.apple.quarantine /Applications/xxxxxxxx.app
```

---

解锁文件夹
```
chflags -R nouchg *
```

---

## 优化

**减少程序坞的响应时间**

```bash
# 设置启动坞动画时间设置为 0.5 秒
defaults write com.apple.dock autohide-time-modifier -float 0.5 && killall Dock

# 设置启动坞响应时间最短
defaults write com.apple.dock autohide-delay -int 0 && killall Dock

# 恢复启动坞默认动画时间
defaults delete com.apple.dock autohide-time-modifier && killall Dock

# 恢复默认启动坞响应时间
defaults delete com.apple.Dock autohide-delay && killall Dock

```

**左右光标移动速度**

系统偏好设置 -> 键盘 -> 键盘
- 按键重复：对应的是移动速度；
- 重复前延迟：对应的是移动前的反应时间。

---

## 软件

**Rosetta 2**

```
softwareupdate --install-rosetta
```

**chrome**

- https://www.google.com/chrome/

**clash**

- https://github.com/Fndroid/clash_for_windows_pkg/releases

**homebrew**

- https://brew.sh/index_zh-cn
- https://gitee.com/cunkai/HomebrewCN

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/f0x/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

然后使用 `brew install xxx` 就可以安装应用了,也可以使用 `brew uninstall xxx` 卸载软件

**nodejs**
```bash
brew install nodejs

# 按需给权限,可以不用这条
sudo chmod -R 777 /usr/local/lib/node_modules/
```

**git**

```bash
brew install git
```

**ffmpeg**
```bash
brew install ffmpeg
```

**motrix**

- https://github.com/agalwood/Motrix

```bash
brew update && brew install --cask motrix
```

**腾讯柠檬清理**

- https://lemon.qq.com/

**snipaste**

- https://zh.snipaste.com/

**tabby**

- https://github.com/Eugeny/tabby

**wgestures2**

- https://www.yingdev.com/projects/wgestures2#

**vlc**

- https://www.videolan.org/index.zh.html

**edge**

- https://www.microsoft.com/en-us/edge

**Alfred**

- https://www.alfredapp.com/

**code-server**

- https://github.com/coder/code-server

```bash
brew install code-server
brew services start code-server
# Now visit http://127.0.0.1:8080. Your password is in ~/.config/code-server/config.yaml
```

**python**

默认自带 python2 和 python3

**java**

- https://oracle.com/java/technologies/downloads/#java8-mac
- https://www.azul.com/downloads/?os=macos&architecture=arm-64-bit

**javafx**
- https://openjfx.io/
- https://openjfx.cn/dl/

```
export PATH_TO_FX=/Library/Java/JavaVirtualMachines/jdk-17.0.2.jdk/javafx-sdk-17.0.2/lib
```

**php**

先查询有哪些 php 的版本，M1 目前只支持部分版本
```bash
brew search php
```

这里我安装 php7.3,参考 stackoverflow 的回答 https://stackoverflow.com/questions/70417377/error-php7-3-has-been-disabled-because-it-is-a-versioned-formula
```bash
brew tap shivammathur/php
brew install shivammathur/php/php@7.3
```

安装完毕后应该就可以在 `/opt/homebrew/etc/php/7.3/` 目录下看到 php 了

运行以下命令加入到环境变量中
```
echo 'export PATH="/opt/homebrew/opt/php@7.3/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="/opt/homebrew/opt/php@7.3/sbin:$PATH"' >> ~/.zshrc
```

`brew info php` 可以查看我们安装的 php 信息

**jenv**

- https://github.com/jenv/jenv

```bash
brew install jenv

echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(jenv init -)"' >> ~/.zshrc

jenv add /Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home
jenv add /Library/Java/JavaVirtualMachines/jdk-11.0.14.jdk/Contents/Home
jenv add /Library/Java/JavaVirtualMachines/jdk-17.0.2.jdk/Contents/Home
jenv versions
jenv global 1.8
jenv local 1.8
```

**miniforge**

- https://github.com/conda-forge/miniforge

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
mv Miniforge3-MacOSX-arm64.sh ~/
cd
bash Miniforge3-MacOSX-arm64.sh
```

**CotEditor**

- https://github.com/coteditor/CotEditor

**nginx**

```
brew install nginx
brew info nginx
```

管理 nginx 运行状态
```bash
# 开启
nginx

# 关闭
nginx -s stop
/opt/homebrew/opt/nginx/bin/nginx -s stop
```

默认 www 目录
```
/opt/homebrew/var/www
```

配置文件所在目录
```
/opt/homebrew/etc/nginx/
```

---

## 一些依赖

**libpq.5.dylib**

搜索发现这个应该是 postgresql 相关功能依赖的文件

一种方法是直接安装 postgresql,不过我测试了没成功
```bash
brew install postgresql
```

我在本地用 fzf 搜索发现 System/Volumes/Data/opt/homebrew/lib/libpq.5.dylib 路径有这个文件,那么复制一个好了,建立个软连接也行
```bash
mkdir -p /usr/local/lib/
sudo cp /System/Volumes/Data/opt/homebrew/lib/libpq.5.dylib /usr/local/lib/libpq.5.dylib
```

参考
- https://github.com/PostgresApp/PostgresApp/issues/83
- https://blog.csdn.net/yutianyue126/article/details/106911948

**libssl.1.1.dylib**

```
brew install openssl@1.1
sudo cp /opt/homebrew/opt/openssl@1.1/lib/libssl.1.1.dylib /usr/local/lib/libssl.1.1.dylib
```

参考
- https://www.v2ex.com/t/666738
- https://pavcreations.com/dyld-library-not-loaded-libssl-1-1-dylib-fix-on-macos/
- https://stackoverflow.com/questions/59006602/dyld-library-not-loaded-usr-local-opt-openssl-lib-libssl-1-0-0-dylib

**libcrypto.1.1.dylib**

```
brew install openssl@1.1
sudo cp /opt/homebrew/opt/openssl@1.1/lib/libcrypto.1.1.dylib /usr/local/lib/libcrypto.1.1.dylib
```

---

## 环境变量

和 linux 是一样的,比如装 maven ,下载解压放到 Library 下,添加环境变量
```
export maven_HOME=/Library/apache-maven-3.8.4
export PATH=$PATH:$maven_HOME/bin
```

可以长期修改
```diff
vim ~/.zshrc

++ export maven_HOME=/Library/apache-maven-3.8.4
++ export PATH=$PATH:$maven_HOME/bin

source ~/.zshrc
mvn -v
```
