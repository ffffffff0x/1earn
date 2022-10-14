# GO

---

**推荐工具/资源书籍**
- [Go - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode.Go)
- [GoLand: A Clever IDE to Go by JetBrains](https://www.jetbrains.com/go/)
- [re4lity/Hacking-With-Golang](https://github.com/re4lity/Hacking-With-Golang) - Golang安全资源合集
- [Quorafind/golang-developer-roadmap-cn](https://github.com/Quorafind/golang-developer-roadmap-cn) - Go 开发者路线图

---

## 常见报错

- **fatal error: can’t find import: fmt**

	说明你的环境变量没有配置正确

---

## IDE

### vscode

- [在VsCode中搭建Go开发环境，手把手教你配置](https://juejin.im/post/5cdd811fe51d45475d5e8e0c)

### Goland 常用快捷键

**文件操作相关**
- `Ctrl + E` 	打开最近浏览过的文件
- `Ctrl + N` 	快速打开某个 struct 结构体所在的文件
- `Ctrl + Shift + N` 	快速打开文件
- `Shift + F6` 	重命名文件夹、文件、方法、变量名等

**代码格式化相关**
- `Ctrl + Alt + L` 	格式化代码
- `Ctrl + 空格` 	代码提示
- `Ctrl + /` 	单行注释
- `Ctrl + Shift + /` 	多行注释
- `Ctrl + B 或 F4` 	快速跳转到结构体或方法的定义位置(需将光标移动到结构体或方法的名称上)
- `Ctrl + "+ 或 -"` 	可以将当前(光标所在位置)的方法进行展开或折叠

**查找和定位相关**
- `Ctrl + R`    替换文本
- `Ctrl + F` 	查找文本
- `Ctrl + Shift + F` 	全局查找
- `Ctrl + G` 	显示当前光标所在行的行号
- `Ctrl + Shift + Alt + N` 	查找类中的方法或变量

**编辑代码相关**
- `Ctrl + J` 	快速生成一个代码片段
- `Shift+Enter` 	向光标的下方插入一行,并将光标移动到该行的开始位置
- `Ctrl + X` 	删除当前光标所在行
- `Ctrl + D` 	复制当前光标所在行
- `Ctrl + Shift + 方向键上或下` 	将光标所在的行进行上下移动(也可以使用 Alt+Shift+方向键上或下)
- `Alt + 回车` 	自动导入需要导入的包
- `Ctrl + Shift + U` 	将选中的内容进行大小写转化
- `Alt + Insert` 	生成测试代码
- `Alt + Up/Down` 	快速移动到上一个或下一个方法
- `Ctrl + Alt + Space` 	类名或接口名提示(代码提示)
- `Ctrl + P` 	提示方法的参数类型(需在方法调用的位置使用,并将光标移动至( )的内部或两侧)

**编辑器相关**
- `Ctrl + Alt + left/right` 	返回至上次浏览的位置
- `Alt + left/right` 	切换代码视图
- `Ctrl + W` 	快速选中代码
- `Alt + F3` 	逐个向下查找选中的代码,并高亮显示
- `Tab` 	代码标签输入完成后,按 Tab,生成代码
- `F2 或 Shift + F2` 	快速定位错误或警告
- `Alt + Shift + C` 	查看最近的操作
- `Alt + 1` 	快速打开或隐藏工程面板

---

## 安装/配置/报错
### 安装

**windows**

默认情况下 `.msi` 文件会安装在 `c:\Go` 目录下.且环境变量自动配置好.`GOPATH` 变量请自己指定

**linux**
```bash
访问 https://golang.org/dl/ 下载最新版本包

tar -C /usr/local -xzf 相应文件.tar.gz

export PATH=$PATH:/usr/local/go/bin
export GOROOT=/usr/local/go
export GOPATH=$HOME/Applications/Go
source $HOME/.profile
source ~/.bash_profile
# $GOPATH 可以包含多个工作目录,取决于你的个人情况.如果你设置了多个工作目录,那么当你在之后使用 go get(远程包安装命令)时远程包将会被安装在第一个目录下.
go version
```

**安装目录清单**

你的 Go 安装目录的文件夹结构应该如下所示:

- api   每个版本的 api 变更差异
- bin   go 源码包编译出的编译器(go)、文档工具(godoc)、格式化工具(gofmt)
- doc   英文版的 Go 文档
- lib   引用的一些库文件
- misc  杂项用途的文件,例如 Android 平台的编译、git 的提交钩子等
- pkg   Windows 平台编译好的中间文件
- src   标准库的源码
- test  测试用例

---

### 配置

**Go 环境变量**

Go 开发环境依赖于一些操作系统环境变量,你最好在安装 Go 之间就已经设置好他们.如果你使用的是 Windows 的话,你完全不用进行手动设置,Go 将被默认安装在目录 `c:/go` 下.这里列举几个最为重要的环境变量:

- $GOROOT 表示 Go 在你的电脑上的安装位置,它的值一般都是 `$HOME/go`,当然,你也可以安装在别的地方.
- $GOARCH 表示目标机器的处理器架构,它的值可以是 386、amd64 或 arm.
- $GOOS 表示目标机器的操作系统,它的值可以是 darwin、freebsd、linux 或 windows.
- $GOBIN 表示编译器和链接器的安装位置,默认是 `$GOROOT/bin`,如果你使用的是 Go 1.0.3 及以后的版本,一般情况下你可以将它的值设置为空,Go 将会使用前面提到的默认值.

目标机器是指你打算运行你的 Go 应用程序的机器.

Go 编译器支持交叉编译,也就是说你可以在一台机器上构建运行在具有不同操作系统和处理器架构上运行的应用程序,也就是说编写源代码的机器可以和目标机器有完全不同的特性(操作系统与处理器架构).

为了区分本地机器和目标机器,你可以使用 $GOHOSTOS 和 $GOHOSTARCH 设置目标机器的参数,这两个变量只有在进行交叉编译的时候才会用到,如果你不进行显示设置,他们的值会和本地机器($GOOS 和 $GOARCH)一样.


> Mac 下编译 Linux 和 Windows 64位可执行程序
```
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
```

> Linux 下编译 Mac 和 Windows 64位可执行程序
```
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
```

> Windows 下编译 Mac 和 Linux 64位可执行程序
```
SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=amd64
go build main.go

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64
go build main.go
```

- $GOPATH 默认采用和 $GOROOT 一样的值,但从 Go 1.1 版本开始,你必须修改为其它路径.它可以包含多个包含 Go 语言源码文件、包文件和可执行文件的路径,而这些路径下又必须分别包含三个规定的目录:src、pkg 和 bin,这三个目录分别用于存放源码文件、包文件和可执行文件.
- $GOARM 专门针对基于 arm 架构的处理器,它的值可以是 5 或 6,默认为 6.
- $GOMAXPROCS 用于设置应用程序可使用的处理器个数与核数.

---

### Test

```bash
mkdir -p $HOME/Applications/Go
cd $HOME/Applications/Go
```
```vim
vim hello.go


package main

import "fmt"

func main() {
	fmt.Printf("hello, world\n")
}
```
```bash
go build
./Go
```

### 报错

**解决 Golang https 请求时，x509: certificate signed by unknown authority 问题**
- http://www.honlyc.com/post/golang-x509-certificate-unknown-authority/

---

## 简介知识
### 工程结构

**工作区**

一般情况下,Go 语言的源码文件必须放在工作区中.但是对于命令源码文件来说,这不是必需的.工作区其实就是一个对应于特定工程的目录,它应包含 3 个子目录:src 目录、pkg 目录和 bin 目录,下面逐一说明.

- src 目录

    用于以代码包的形式组织并保存 Go 源码文件,这里的代码包与 src 下的子目录一一对应.例如,若一个源码文件被声明属于代码包 log,那么它就应当保存在 src/log 目录中.

    当然,也可以把 Go 源码文件直接放在 src 目录下,但这样的 Go 源码文件就只能被声明属于 main 代码包了.除非用于临时测试或演示,一般还是建议把 Go 源码文件放入特定的代码包中.

- pkg 目录

    用于存放通过 go install 命令安装后的代码包的归档文件.前提是代码包中必须包含 Go 库源码文件.归档文件是指那些名称以".a"结尾的文件.该目录与 GOROOT 目录下的 pkg 目录功能类似.区别在于,工作区中的 pkg 目录专门用来存放用户代码的归档文件.

    编译和安装用户代码的过程一般会以代码包为单位进行.比如 log 包被编译安装后,将生成一个名为 log.a 的归档文件,并存放在当前工作区的 pkg 目录下的平台相关目录中.

- bin 目录

    与 pkg 目录类似,在通过 go install 命令完成安装后,保存由 Go 命令源码文件生成的可执行文件.在类 Unix 操作系统下,这个可执行文件一般来说名称与源码文件的主文件名相同.而在 Windows 操作系统下,这个可执行文件的名称则是源码文件主文件名加 .exe 后缀.

**GOPATH**

我们需要将工作区的目录路径添加到环境变量 GOPATH 中.否则,即使处于同一工作区,代码之间也无法通过绝对代码包路径调用.在实际开发环境中,工作区可以只有一个,也可以有多个,这些工作区的目录路径都需要添加到 GOPATH 中.与 GOROOT 一样,我们应该确保 GOPATH 一直有效.

需要注意一下两点:
1. GOPATH 中不要包含 Go 语言的根目录,以便将 Go 语言本身的工作区同用户工作区严格分开.
2. 通过 Go 工具中的代码获取命令 go get,可将指定项目的源码下载到我们在 GOPATH 中设定的第一个工作区中,并在其中完成编译和安装.

**源码文件**

Go 的源码文件有 3 个种类,即命令源码文件、库源码文件和测试源码文件,下面详细说明这 3 类源码文件.

- 命令源码文件

    如果一个源码文件被声明属于 main 代码包,且该文件代码中包含无参数声明和结果声明的 main 函数,则它就是命令源码文件.命令源码文件可通过 go run 命令直接启动运行.

    同一个代码包中的所有源码文件,其所属代码包的名称必须一致.如果命令源码文件和库源码文件处于同一个代码包中,那么在该包中就无法正确执行 go build 和 go install 命令.换句话说,这些源码文件将无法通过常规方法编译和安装.

    因此,命令源码文件通常会单独放在一个代码包中.这是合理且必要的,因为通常一个程序模块或软件的启动入口只有一个.

    同一个代码包中可以有多个命令源码文件,可通过 go run 命令分别运行,但这会使 go build 和 go install 命令无法编译和安装该代码包.所以,我们也不应该把多个命令源码文件放在同一个代码包中.

    当代码包中有且仅有一个命令源码文件时,在文件所在目录中执行 go build 命令,即可在该目录下生成一个与目录同名的可执行文件;而若使用 go install 则可在当前工作区的 bin 目录下生成相应的可执行文件.例如,代码包 gopcp.v2/helper/ds 中只有一个源码文件 showds.go,且它是命令源码文件,则相关操作和结果如下:
    ```bash
    root:~/golang/example.v2/src/gopcp.v2/helper/ds$ Is
    showds.go
    root:~/golang/example.v2/src/gopcp.v2/helper/ds$ go build
    root:~/golang/example.v2/src/gopcp.v2/helper/ds$ Is
    ds showds.go
    root: ~/golang/example.v2/src/gopcp.v2/helper/ds$ go install
    root:~/golang/example.v2/src/gopcp・v2/helper/ds$ Is ../../../../bin
    ds
    ```
    需要特别注意,只有当环境变量 GOPATH 中只包含一个工作区的目录路径时,go install 命令才会把命令源码文件安装到当前工作区的 bin 目录下;否则,像这样执行 go install 命令就会失败.此时必须设置环境变量 GOBIN,该环境变量的值是一个目录的路径,该目录用于存放所有因安装 Go 命令源码文件而生成的可执行文件.

- 库源码文件

    通常,库源码文件声明的包名会与它直接所属的代码包(目录)名一致,且库源码文件中不包含无参数声明和无结果声明的 main 函数.下面来安装(其中包含编译)gopcp.v2/helper/log 包,其中含有若干库源码文件:
    ```bash
    root:~/golang/example.v2/src/gopcp.v2/helper/log$ ls
    base    logger.go    logger_test.go logrus
    root: ~/golang/example.v2/src/gopcp.v2/helper/log$ go install
    root:~/golang/example.v2/src/gopcp.v2/helper/log$ ls    ../../../pkg
    linux_amd64
    root:~/golang/example.v2/src/gopcp.v2/helper/log$ ls    ../../../pkg/linux_amd64/gopcp.v2/helper
    log    log.a
    root:~/golang/example.v2/src/gopcp.v2/helper/log$ ls ../../../../pkg/linux_amd64/gopcp.v2/helper/log
    base.a    field.a    logrus.a
    ```
    这里,我们通过在 gopcp.v2/helper/log 代码包的目录下执行 go install 命令,成功安装了该包并生成了若干归档文件.这些归档文件的存放目录由以下规则产生.

    安装库源码文件时所生成的归档文件会被存放到当前工作区的 pkg 目录中.example.v2 项目的 gopcp.v2/helper/log 包所属工作区的根目录是 ~/golang/example.v2.因此,上面所说的 pkg 目录即 ~/golang/example.v2/pkg.

    根据被编译时的目标计算环境,归档文件会被放在该 pkg 目录下的平台相关目录中.例如,我是在 64 位的 Linux 计算环境下安装的,对应的平台相关目录就是 linux_amd64,那么归档文件一定会被存放到 ~/golang/example.v2/pkg/linux_amd64 目录中的某个地方.

    存放归档文件的目录的相对路径与被安装的代码包的上一级代码包的相对路径一致.第一个相对路径是相对于工作区的 pkg 目录下的平台相关目录而言的,而第二个相对路径是相对于工作区的 src 目录而言的.

    例如,gopcp.v2/helper/log 包的归档文件 log.a 一定会被存放到 ~/golang/example.v2/pkg/linux_amd64/gopcp.v2/helper 这个目录下.而它的子代码包 gopcp.v2/helper/log/base 的归档文件 base.a,则一定会被存放到 ~/golang/example.v2/pkg/linux_amd64/gopcp.v2/helper/log 目录下.

- 测试源码文件

    测试源码文件是一种特殊的库文件,可以通过执行 go test 命令运行当前代码包下的所有测试源码文件.成为测试源码文件的充分条件有两个,如下.
    - 文件名需要以"_test.go"结尾.
    - 文件中需要至少包含一个名称以 Test 开头或 Benchmark 开头,且拥有一个类型为 *testing.T 或 *testing.B 的参数的函数.testing.T 和 testing.B 是两个结构体类型.而 *testing.T 和 *testing.B 则分别为前两者的指针类型.它们分别是功能测试和基准测试所需的.

    当在一个代码包中执行 go test 命令时,该代码包中的所有测试源码文件会被找到并运行.我们依然以 gopcp.v2/helper/log 包为例:
    ```bash
    root:~/golang/example.v2/src/gopcp.v2/helper/log$ go test
    PASS
    ok    gopcp.v2/helper/log    0.008s
    ```
    这里使用 go test 命令在 gopcp.v2/helper/log 包中找到并运行了测试源码文件 logger_test.go,且调用其中所有的测试函数.命令行的回显信息表示我们通过了测试,并且运行测试源码文件中的测试程序共花费了 0.080 S.

    最后插一句,Go 代码的文本文件需要以 UTF-8 编码存储.如果源码文件中出现了非 UTF-8 编码的字符,那么在运行、编译或安装的时候,Go 命令会抛出 illegal UTF-8 sequence 错误.

**代码包**

在 Go 中,代码包是代码编译和安装的基本单元,也是非常直观的代码组织形式.

- 包声明

    在 example.v2 项目的代码包中,多数源码文件名称看似都与包名没什么关系.实际上,在 Go 语言中,代码包中的源码文件可以任意命名.另外,这些任意名称的源码文件都必须以包声明语句作为文件中代码的第一行.比如,gopcp.v2/helper/log/base 包中的所有源码文件都要先声明自己属于某一个代码包:
    ```go
    package "base"
    ```
    其中 package 是 Go 中用于包声明语句的关键字.Go 规定包声明中的包名是代码包路径的最后一个元素.比如,`gopcp.v2/helper/log/base` 包的源码文件包声明中的包名是 base.但是,不论命令源码文件存放在哪个代码包中,它都必须声明属于 main 包.

-  包导入

    代码包 `gopcp.v2/helper/log` 中的 logger.go 需要依赖 base 子包和 logrus 子包,因此需要在源码文件中使用代码包导入语句,如下所示:
    ```go
    import "gopcp.v2/helper/log/base"
    import "gopcp.v2/helper/log/logrus"
    ```
    这需要用到代码包导入路径,即代码包在工作区的 src 目录下的相对路径.

    当导入多个代码包时,可以用圆括号括起它们,且每个代码包名独占一行.在使用被导入代码包中公开的程序实体时,需要使用包路径的最后一个元素加的方式指定代码所在的包.

    因此,上述语句可以写成:
    ```go
    import (
        "gopcp.v2/helper/log/base"
        "gopcp.v2/helper/log/logrus"
    )
    ```
    同一个源码文件中导入的多个代码包的最后一个元素不能重复,否则一旦使用其中的程序实体,就会引起编译错误.但是,如果你只导入不使用,同样会引起编译错误.一个解决方法是为其中一个起个别名,比如:
    ```go
    import (
        "github.com/Sirupsen/logrus"
        mylogrus "gopcp.v2/helper/log/logrus"
    )
    ```
    如果我们想不加前缀而直接使用某个依赖包中的程序实体,就可以用"."来代替别名,如下所示:
    ```go
    import (
        . "gopcp.v2/helper/log/logrus"
    )
    ```
    看到那个"."了吗？之后,在当前源码文件中,我们就可以这样做了:
    ```go
    var logger = NewLogger("gopcp") // NewLogger 是 gopcp.v2/helper/log/logrus 包中的函数
    ```
    这里强调一下,Go 中的变量、常量、函数和类型声明可统称为程序实体,而它们的名称统称为标识符.标识符可以是 Unicode 字符集中任意能表示自然语言文字的字符、数字以及下划线 (_).标识符不能以数字或下划线开头.

    实际上,标识符的首字符的大小写控制着对应程序实体的访问权限.如果标识符的首字符是大写形式,那么它所对应的程序实体就可以被本代码包之外的代码访问到,也称为可导出的或公开的;否则,对应的程序实体就只能被本包内的代码访问,也称为不可导岀的或包级私有的.要想成为可导出的程序实体,还需要额外满足以下两个条件.

    - 程序实体必须是非局部的.局部的程序实体是指:它被定义在了函数或结构体的内部.
    - 代码包所属目录必须包含在 GOPATH 中定义的工作区目录中.

    代码包导入还有另外一种情况:如果只想初始化某个代码包,而不需要在当前源码文件中使用那个代码包中的任何程序实体,就可以用"_"来代替别名:
    ```go
    import (
        _ "github.com/Simpsen/logrus"
    )
    ```
    这种情况下,我们只是触发了这个代码包中的初始化操作(如果有的话).符号"_"就像一个垃圾桶,它在代码中使用很广泛,在后续的学习中还可以看到它的身影.

-  包初始化

    在Go语言中,可以有专门的函数负责代码包初始化,称为代码包初始化函数.这个函数需要无任何参数声明和结果声明,且名称必须为 init,如下所示:
    ```go
    func init() {
        fmt.Println("Initialize...")
    }
    ```
    Go 会在程序真正执行前对整个程序的依赖进行分析,并初始化相关的代码包.也就是说,所有的代码包初始化函数都会在 main 函数(命令源码文件中的入口函数)执行前执行完毕,而且只会执行一次.另外,对于每一个代码包来说,其中的所有全局变量的初始化,都会在代码包的初始化函数执行前完成.这避免了在代码包初始化函数对某个变量进行赋值之后,又被该变量声明中赋予的值覆盖掉的问题.

    下面的代码展示了全局赋值语句、代码包初始化函数以及主函数的执行顺序.其中,双斜杠及其右边的内容为代码注释,Go 编译器在编译的时候会将其忽略.
    ```go
    package main //命令源码文件必须在这里声明自己属于main包
    import ( //导入标准库代码包fmt和runtime
        "fmt"
        "runtime"
    )
    func init() { //代码包初始化函数
        fmt.Printf("Map: %v\n", m)  // 格式化的打印
        //通过调用runtime包的代码获取当前机器的操作系统和计算架构.
        //而后通过fmt包的Sprintf方法进行格式化字符串生成并赋值给变量info
        info = fmt.Sprintf("OS: %s, Arch: %s", runtime.GOOS, runtime.GOARCH)
    }
    //非局部变量,map类型,且已初始化
    var m = map[int]string{1: "A", 2: "B", 3: "C"}
    //非局部变量,string类型,未被初始化
    var info string
    func main() {         //命令源码文件必须有的入口函数,也称主函数
        fmt.Println(info) // 打印变量 info
    }
    ```

    运行这个文件:
    ```
    D:\code>go run main.go
    Map: map[1:A 2:B 3:C]
    OS: windows, Arch: amd64
    ```
    关于每行代码的用途,在源码文件中我已经作了基本的解释.这里只解释这个小程序的输出.

    第一行是对变量 m 的值格式化后的结果.可以看到,在函数 init 的第一条语句执行时,变量 m 已经被初始化并赋值了.这验证了:当前代码包中所有全局变量的初始化会在代码包初始化函数执行前完成.

    第二行是对变量 info 的值格式化后的结果.变量 info 被定义时并没有显式赋值,因此它被赋予类型 string 的零值——""(空字符串).之后,变量 info 在代码包初始化函数 init 中被赋值,并在入口函数 main 中输出.这验证了:所有的代码包初始化函数都会在 main 函数执行前执行完毕.

    同一个代码包中可以存在多个代码包初始化函数,甚至代码包内的每一个源码文件都可以定义多个代码包初始化函数.Go 不会保证同一个代码包中多个代码包初始化函数的执行顺序.此外,被导入的代码包的初始化函数总是会先执行.在上例中,fmt 和 runtime 包中的 init 函数(如果有的话)会先执行,然后当前文件中的 init 函数才会执行.

---

## 一些项目

**图形化**
- [fyne](https://github.com/fyne-io/fyne) - web框架

**网络操作**
- [caucy/batch_ping](https://github.com/caucy/batch_ping) - 多主机 ping
- [hdm/nextnet](https://github.com/hdm/nextnet) - 专门扫描 137 端口存活主机

**系统信息**
- [gopsutil](https://github.com/shirou/gopsutil)
- [wmi](https://github.com/StackExchange/wmi)

**web**
- [gin](https://github.com/gin-gonic/gin)

**Crypto**
- [tjfoc/gmsm: GM SM2/3/4 library based on Golang (基于Go语言的国密SM2/SM3/SM4算法库)](https://github.com/tjfoc/gmsm)

**通知**
- [notify](https://github.com/nikoksr/notify)

**telegram bot**
- [telebot](https://github.com/tucnak/telebot)
- [telegram-bot-api](https://github.com/go-telegram-bot-api/telegram-bot-api)

**配置**
- [go-ini/ini](https://github.com/go-ini/ini) - 在Go中提供了ini文件的读写功能

**花里胡哨**
- [gookit/color](https://github.com/gookit/color) - 给终端输出加颜色
- https://github.com/fatih/color - Color package for Go (golang)

**格式化**
- [tidwall/gjson](https://github.com/tidwall/gjson) - Get JSON values quickly - JSON parser for Go

**反虚拟机**
- https://github.com/p3tr0v/chacal

**语言**
- [mozillazg/go-pinyin](https://github.com/mozillazg/go-pinyin) - 汉字转拼音
