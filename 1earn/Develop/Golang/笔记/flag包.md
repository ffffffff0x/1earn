# flag 包

---

**Source & Reference**

- [Go语言flag包:命令行参数解析](http://c.biancheng.net/view/5573.html)

---

几个概念:
- 命令行参数(或参数):是指运行程序提供的参数
- 已定义命令行参数:是指程序中通过 flag.Xxx 等这种形式定义了的参数
- 非 flag(non-flag)命令行参数(或保留的命令行参数):先可以简单理解为 flag 包不能解析的参数

```go
package main

import (
    "flag"
    "fmt"
    "os"
)

var (
    h, H bool

    v bool
    q *bool

    D    string
    Conf string
)

func init() {
    flag.BoolVar(&h, "h", false, "帮助信息")
    flag.BoolVar(&h, "H", false, "帮助信息")

    flag.BoolVar(&v, "v", false, "显示版本号")

    //
    flag.StringVar(&D, "D", "deamon", "set descripton ")
    flag.StringVar(&Conf, "Conf", "/dev/conf/cli.conf", "set Conf filename ")

    // 另一种绑定方式
    q = flag.Bool("q", false, "退出程序")

    // 像flag.Xxx函数格式都是一样的，第一个参数表示参数名称，
    // 第二个参数表示默认值，第三个参数表示使用说明和描述.
    // flag.XxxVar这样的函数第一个参数换成了变量地址，
        // 后面的参数和flag.Xxx是一样的.

    // 改变默认的 Usage

    flag.Usage = usage

    flag.Parse()

    var cmd string = flag.Arg(0)

    fmt.Printf("-----------------------\n")
    fmt.Printf("cli non=flags      : %s\n", cmd)

    fmt.Printf("q: %b\n", *q)

    fmt.Printf("descripton:  %s\n", D)
    fmt.Printf("Conf filename : %s\n", Conf)

    fmt.Printf("-----------------------\n")
    fmt.Printf("there are %d non-flag input param\n", flag.NArg())
    for i, param := range flag.Args() {
        fmt.Printf("#%d    :%s\n", i, param)
    }

}

func main() {
    flag.Parse()

    if h || H {
        flag.Usage()
    }
}

func usage() {
    fmt.Fprintf(os.Stderr, `CLI: 8.0
Usage: Cli [-hvq] [-D descripton] [-Conf filename]

`)
    flag.PrintDefaults()
}
```

flag 包实现了命令行参数的解析，大致需要几个步骤:

**flag 参数定义或绑定**

定义 flags 有两种方式:

1. flag.Xxx()，其中 Xxx 可以是 Int、String 等;返回一个相应类型的指针，如:
```go
var ip = flag.Int("flagname", 1234, "help message for flagname")
```

2. flag.XxxVar()，将 flag 绑定到一个变量上，如:
```go
var flagvar int
flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname")
```
另外，还可以创建自定义 flag，只要实现 flag.Value 接口即可(要求 receiver 是指针)，这时候可以通过如下方式定义该 flag:
```go
flag.Var(&flagVal, "name", "help message for flagname")
```
命令行 flag 的语法有如下三种形式:-flag // 只支持 bool 类型 -flag=x -flag x // 只支持非 bool 类型

**flag 参数解析**

在所有的 flag 定义完成之后，可以通过调用 `flag.Parse()` 进行解析.

根据 `Parse()` 中 for 循环终止的条件，当 parseOne 返回 false，nil 时，Parse 解析终止.
```go
s := f.args[0]
if len(s) == 0 || s[0] != '-' || len(s) == 1 {
    return false, nil
}
```

当遇到单独的一个"-"或不是"-"开始时，会停止解析.比如:./cli - -f 或 ./cli -f，这两种情况，-f 都不会被正确解析.像这些参数，我们称之为 non-flag 参数.

parseOne 方法中接下来是处理 -flag=x，然后是 -flag(bool 类型)(这里对 bool 进行了特殊处理)，接着是 -flag x 这种形式，最后，将解析成功的 Flag 实例存入 FlagSet 的 actual map 中.

`Arg(i int)` 和 `Args()`、`NArg()`、`NFlag()` `Arg(i int)` 和 `Args()` 这两个方法就是获取 non-flag 参数的;`NArg()` 获得 non-flag 个数;`NFlag()` 获得 FlagSet 中 actual 长度(即被设置了的参数个数).

flag 解析遇到 non-flag 参数就停止了.所以如果我们将 non-flag 参数放在最前面，flag 什么也不会解析，因为 flag 遇到了这个就停止解析了.

**分支程序**

根据参数值，代码进入分支程序，执行相关功能.上面代码提供了 -h 参数的功能执行.
```go
if h || H {
        flag.Usage()
    }
```

总体而言，从例子上看，flag package 很有用，但是并没有强大到解析一切的程度.如果入参解析非常复杂，flag 可能捉襟见肘.
