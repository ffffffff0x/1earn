# GO安全

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

## 代码混淆

- [burrowers/garble](https://github.com/burrowers/garble)
- [unixpickle/gobfuscate](https://github.com/unixpickle/gobfuscate)

---

## 特征清除

**相关文章**
- [如何消除Go的编译特征](https://mp.weixin.qq.com/s/Z0SpYJBikdwA_foPkxnWFQ)

**相关工具**
- [boy-hack/go-strip](https://github.com/boy-hack/go-strip) - 清除 Go 编译时自带的信息
    ```bash
    # 打印出读取的信息
    go-strip -f binary.exe
    # 消除Go的编译信息
    go-strip -f binary.exe -a -output new.exe
    ```

**禁用符号表和调试信息**

虽然 Go 是编译成二进制后运行的，但其默认编译机制（Release With Debug Info）会泄漏一些信息。
默认情况下， Go 程序在运行出错时，会输出如上报错信息（在哪个线程，哪个文件，哪个函数，哪行出的错）。

这两个信息可以在编译时进行禁用：
```
go build -ldflags "-s -w” <package>
```

**隐藏环境变量**

报错信息中目录信息的来源是编译器运行时所处环境的环境变量。

编译时，Go 会从 $GOPATH 寻找我们的代码，从 $GOROOT 提取标准库。在打包时将 $GOPATH 改写为 $GOROOT_FINAL 并作为调试信息的一部分写入目标文件。

要隐藏真实的 $GOPATH ，需要在另外一个目录里对真实的 $GOPATH 创建一个软链接，编译器在寻找时就会把软链接的目录名写到最终文件里，从而达到隐藏目的。
```bash
ACTUAL_GOPATH = "~/Project"
export GOPATH = '/tmp'
export GOROOT_FINAL = $GOPATH
[ ! -d $GOPATH ] && ln -s "$ACTUAL_GOPATH" "$GOPATH"
[[ ! $PATH =~ $GOPATH ]] && export PATH=$PATH:$GOPATH/bin
```

## Go代码审计

- [Go代码审计](./Go安全/Go代码审计.md)
