# LuaJIT

---

**官网**

- http://luajit.org/

---

## 环境安装

**Linux 系统上安装**
```bash
git clone https://luajit.org/git/luajit.git
cd luajit
make
make install
export LUAJIT_LIB=/usr/local/lib
```

或
```
f8x -lua
```

**测试**

```
luajit

>print("hello The world")
```

---

## 编译

使用 -b 选项,后缀随便定义,和 luac 一样,只有自己可以运行
```
luajit -b test.lua test.jit
```
