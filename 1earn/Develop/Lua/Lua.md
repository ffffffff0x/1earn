# Lua

---

**官网**

- http://www.lua.org/

**教程**

- https://www.runoob.com/lua/lua-tutorial.html

---

## 环境安装

**Linux 系统上安装**
```
curl -R -O http://www.lua.org/ftp/lua-5.4.3.tar.gz
tar zxf lua-5.4.3.tar.gz
cd lua-5.4.3
make linux test
make install
```

其他版本如果报错需要装
```bash
# centos
yum install readline-devel

# debian
apt-get install libreadline-dev
```

或
```
f8x -lua
```

**测试**
```
vim test.lua

print("Hello World!")
```

```bash
lua test.lua
```

**Window 系统上安装 Lua**

- https://github.com/rjpcomputing/luaforwindows
- http://luadist.org/

---

## 使用

lua 和 python 一样，都提供了交互式编程模式，和脚本式编程模式

直接输入 lua 即可进入交互式编程模式

将 Lua 程序代码保存到一个以 lua 结尾的文件，并执行，该模式称为脚本式编程
