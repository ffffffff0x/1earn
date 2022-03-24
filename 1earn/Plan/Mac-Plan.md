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

解锁
```
chflags -R nouchg *
```

---

## 优化

**减少程序坞的响应时间**

```
# 设置启动坞动画时间设置为 0.5 秒
defaults write com.apple.dock autohide-time-modifier -float 0.5 && killall Dock

# 设置启动坞响应时间最短
defaults write com.apple.dock autohide-delay -int 0 && killall Dock
```

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

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/f0x/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**git**

```bash
brew install git
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

**javafx**

- https://openjfx.cn/dl/
