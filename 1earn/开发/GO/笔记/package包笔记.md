# package包笔记

---

## Reference
- [Go语言包（package），Golang包（package）](http://c.biancheng.net/golang/package/)

---

# 基本概念

Go 语言是使用包来组织源代码的，并实现命名空间的管理。任何源代码文件必须属于某个包。源码文件的第一行有效代码必须是 package pacakgeName 语句，通过该语句声明自己所在的包。

Go 语言的包借助了目录树的组织形式，一般包的名称就是其源文件所在目录的名称，虽然 Go 没有强制包名必须和其所在的目录名同名，但还是建议包名和所在目录同名，这样结构更清晰。

包可以定义在很深的目录中，包的定义是不包括目录路径的，但是包的引用一般是全路径引用。比如在 $GOPATH/src/a/b/ 下定义一个包 c。在包 c 的源码中只需声明为 package c，而不是声明为 package a/b/c，但是在“import”包 c 时，需要带上路径 import "a/b/c"。包的

包的习惯用法：
- 包名一般是小写的，使用一个简短的命名。
- 包名一般要和所在的目录同名。
- 包一般放到公司的域名目录下，这样能保证包名的唯一性，便于共享代码。比如个人的 GitHub 项目的包一般放到 $GOPATH/src/github.com/userName/projectName 目录下。

**包引用**

标准包的源码位于 $GOROOT/src/ 下面，标准包可以直接引用。自定义的包和第三方包的源码必须放到 $GOPATH/src 目录下才能被引用。

**包引用路径**

包的引用路径有两种写法，一种是全路径，另一种是相对路径。

- 全路径引用

    包的绝对路径就是“$GOROOT/src 或 $GOPATH/src”后面包的源码的全路径，比如下面的包引用：
    ```go
    import "lab/test"
    import "database/sql/driver"
    import "database/sql"
    ```
    test 包是自定义的包，其源码位于$GOPATH/src/lab/test 目录下； sql 和 driver 包的源码分别位于 $GOROOT/src/database/sql 和 $GOROOT/src/database/sql/driver 下。

- 相对路径引用

    相对路径只能用于引用 $GOPATH 下的包，标准包的引用只能使用全路径引用。比如下面两个包：包 a 的路径是 $GOPATH/src/lab/a，包 b 的源码路径为 $GOPATH/src/lab/b，假设 b 引用了 a 包，则可以使用相对路径引用方式。示例如下：
    ```go
    // 相对路径引用
    import "../a"
    // 全路径引用
    import "lab/a"
    ```

**包引用格式**

包引用有四种引用格式，为叙述方便，我们以 fmt 标准库为例进行说明。

1. 标准引用方式如下
    ```go
    import "fmt"
    ```
    此时可以用“fmt.”作为前缀引用包内可导出元素，这是常用的一种方式。

2. 别名引用方式如下
    ```go
    import F "fmt"
    ```
    此时相当于给包 fmt 起了个别名 F，用“F.”代替标准的“fmt.”作为前缀引用 fmt 包内可导出元素。

3. 省略方式如下
    ```go
    import . "fmt"
    ```
    此时相当于把包 fmt 的命名空间直接合并到当前程序的命名空间中，使用 fmt 包内可导出元素可以不用前缀“fmt.”，直接引用。示例如下：
    ```go
    package main
    import . "fmt"
    func main () {
        //不需要加前级 fmt.
        Println( "hello , world!”)
    }
    ```

4. 仅执行包初始化 init 函数

    使用标准格式引用包，但是代码中却没有使用包，编译器会报错。如果包中有 init 初始化函数，则通过 import _ "packageName" 这种方式引用包，仅执行包的初始化函数，即使包没有 init 初始化函数，也不会引发编译器报错。示例如下：
    ```go
    import _ "fmt"
    ```

注意：
- 一个包可以有多个 init 函数，包加载会执行全部的 init 函数，但并不能保证执行顺序，所以不建议在一个包中放入多个 init 函数，将需要初始化的逻辑放到一个 init 函数里面。
- 包不能出现环形引用。比如包 a 引用了包 b，包 b 引用了包 c，如果包 c 又引用了包 a，则编译不能通过。
- 包的重复引用是允许的。比如包 a 引用了包 b 和包 c，包 b 和包 c 都引用了包 d。这种场景相当于重复引用了 d，这种情况是允许的，并且 Go 编译器保证 d 的 init 函数只会执行一次。

**包加载**

在执行 main.main 之前， Go 引导程序会先对整个程序的包进行初始化。整个执行的流程如下图所示。

![image](../../../../assets/img/开发/go/笔记/package包笔记/1.png)

Go 包的初始化有如下特点：
- 包初始化程序从 main 函数引用的包开始，逐级查找包的引用，直到找到没有引用其他包的包，最终生成一个包引用的有向无环图。
- Go 编译器会将有向无环图转换为一棵树，然后从树的叶子节点开始逐层向上对包进行初始化。
- 单个包的初始化过程如上图所示，先初始化常量，然后是全局变量，最后执行包的 init 函数（如果有）。

---

## 封装简介及实现细节

在 Go 语言中封装就是把抽象出来的字段和对字段的操作封装在一起，数据被保护在内部，程序的其它包只能通过被授权的方法，才能对字段进行操作。

封装的好处：
- 隐藏实现细节；
- 可以对数据进行验证，保证数据安全合理。

如何体现封装：
- 对结构体中的属性进行封装；
- 通过方法，包，实现封装。

封装的实现步骤：
- 将结构体、字段的首字母小写；
- 给结构体所在的包提供一个工厂模式的函数，首字母大写，类似一个构造函数；
- 提供一个首字母大写的 Set 方法（类似其它语言的 public），用于对属性判断并赋值；
- 提供一个首字母大写的 Get 方法（类似其它语言的 public），用于获取属性的值。

【示例】对于员工，不能随便查看年龄，工资等隐私，并对输入的年龄进行合理的验证。代码结构如下：

![image](../../../../assets/img/开发/go/笔记/package包笔记/2.png)

person.go 中的代码如下所示：
```go
package model

import "fmt"

type person struct {
    Name string
    age int   //其它包不能直接访问..
    sal float64
}

//写一个工厂模式的函数，相当于构造函数
func NewPerson(name string) *person {
    return &person{
        Name : name,
    }
}

//为了访问age 和 sal 我们编写一对SetXxx的方法和GetXxx的方法
func (p *person) SetAge(age int) {
    if age >0 && age <150 {
        p.age = age
    } else {
        fmt.Println("年龄范围不正确..")
        //给程序员给一个默认值
    }
}
func (p *person) GetAge() int {
    return p.age
}

func (p *person) SetSal(sal float64) {
    if sal >= 3000 && sal <= 30000 {
        p.sal = sal
    } else {
        fmt.Println("薪水范围不正确..")
    }
}

func (p *person) GetSal() float64 {
    return p.sal
}
```

main.go 中的代码如下所示：
```go
package main

import (
    "fmt"
    "../model"
)

func main() {

    p := model.NewPerson("smith")
    p.SetAge(18)
    p.SetSal(5000)
    fmt.Println(p)
    fmt.Println(p.Name, " age =", p.GetAge(), " sal = ", p.GetSal())
}
```

执行效果如下图所示：

![image](../../../../assets/img/开发/go/笔记/package包笔记/3.png)

---

## GOPATH 详解

GOPATH 是 Go 语言中使用的一个环境变量，它使用绝对路径提供项目的工作目录。

工作目录是一个工程开发的相对参考目录，好比当你要在公司编写一套服务器代码，你的工位所包含的桌面、计算机及椅子就是你的工作区。工作区的概念与工作目录的概念也是类似的。如果不使用工作目录的概念，在多人开发时，每个人有一套自己的目录结构，读取配置文件的位置不统一，输出的二进制运行文件也不统一，这样会导致开发的标准不统一，影响开发效率。

GOPATH 适合处理大量 Go语言源码、多个包组合而成的复杂工程。

使用命令行查看 GOPATH 信息
```
go env
GOARCH="amd64"
GOBIN=""
GOEXE=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOOS="linux"
GOPATH="/home/aaa/go"
GORACE=""
GOROOT="/usr/local/go"
GOTOOLDIR="/usr/local/go/pkg/tool/linux_amd64"
GCCGO="gccgo"
CC="gcc"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0"
CXX="g++"
CGO_ENABLED="1"
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
```

命令行说明如下：
- 第 1 行，执行 go env 指令，将输出当前 Go 开发包的环境变量状态。
- 第 2 行，GOARCH 表示目标处理器架构。
- 第 3 行，GOBIN 表示编译器和链接器的安装位置。
- 第 7 行，GOOS 表示目标操作系统。
- 第 8 行，GOPATH 表示当前工作目录。
- 第 10 行，GOROOT 表示 Go 开发包的安装目录。

从命令行输出中，可以看到 GOPATH 设定的路径为：`/home/aaa/go`

在 Go 1.8 版本之前，GOPATH 环境变量默认是空的。从 Go 1.8 版本开始，Go 开发包在安装完成后，将 GOPATH 赋予了一个默认的目录，参见下表。

![image](../../../../assets/img/开发/go/笔记/package包笔记/4.png)

**使用 GOPATH 的工程结构**

在 GOPATH 指定的工作目录下，代码总是会保存在 $GOPATH/src 目录下。在工程经过 go build、go install 或 go get 等指令后，会将产生的二进制可执行文件放在 $GOPATH/bin 目录下，生成的中间缓存文件会被保存在 $GOPATH/pkg 下。

如果需要将整个源码添加到版本管理工具（Version Control System，VCS）中时，只需要添加 $GOPATH/src 目录的源码即可。bin 和 pkg 目录的内容都可以由 src 目录生成。

---

## 常用内置包简介

标准的 Go 语言代码库中包含了大量的包，并且在安装 Go 的时候多数会伴随一起安装。浏览 $GOROOT/src/pkg 目录并且查看那些包会非常有启发。无法对每个包就加以解说，不过下面的这些值得讨论：

1. fmt

    包 fmt 实现了格式化的 I/O 函数，这与 C 的 printf 和 scanf 类似。格式化短语派生于 C 。一些短语（%-序列）这样使用：
    - %v：默认格式的值。当打印结构时，加号（%+v）会增加字段名；
    - %#v：Go 样式的值表达；
    - %T：带有类型的 Go 样式的值表达；

2. io

    这个包提供了原始的 I/O 操作界面。它主要的任务是对 os 包这样的原始的 I/O 进行封装，增加一些其他相关，使其具有抽象功能用在公共的接口上。

3. bufio

    这个包实现了缓冲的 I/O。它封装于 io.Reader 和 io.Writer 对象，创建了另一个对象（Reader 和 Writer）在提供缓冲的同时实现了一些文本 I/O 的功能。

4. sort

    sort 包提供了对数组和用户定义集合的原始的排序功能。

5. strconv

    strconv 包提供了将字符串转换成基本数据类型，或者从基本数据类型转换为字符串的功能。

6. os

    os 包提供了与平台无关的操作系统功能接口。其设计是 Unix 形式的。

7. sync

    sync 包提供了基本的同步原语，例如互斥锁。

8. flag

    flag 包实现了命令行解析。

9. encoding/json

    encoding/json 包实现了编码与解码 RFC 4627 定义的 JSON 对象。

10. html/template

    数据驱动的模板，用于生成文本输出，例如 HTML。

    将模板关联到某个数据结构上进行解析。模板内容指向数据结构的元素（通常结构的字段或者 map 的键）控制解析并且决定某个值会被显示。模板扫描结构以便解析，而“游标” @ 决定了当前位置在结构中的值。

11. net/http

    net/http 实现了 HTTP 请求、响应和 URL 的解析，并且提供了可扩展的 HTTP 服务和基本的 HTTP 客户端。

12. unsafe

    unsafe 包包含了 Go 程序中数据类型上所有不安全的操作。通常无须使用这个。

13. reflect

    reflect 包实现了运行时反射，允许程序通过抽象类型操作对象。通常用于处理静态类型 `interface{}` 的值，并且通过 Typeof 解析出其动态类型信息，通常会返回一个有接口类型 Type 的对象。

14. os/exec

    os/exec 包执行外部命令。

---

## 自定义包

很多例子都是以一个包的形式存在的，也就是 main 包。在 Go语言里，允许我们将同一个包的代码分隔成多个小块来单独保存，只需要将这些文件放在同一个目录即可。

对于更大的应用程序，我们可能更喜欢将它的功能性分隔成逻辑的单元，分别在不同的包里实现。或者将一些应用程序通用的那一部分剖离出来。

Go 语言里并没有限制一个应用程序能导入多少个包或者一个包能被多少个应用程序共享，但是将这些应用程序特定的包放在当前应用程序的子目录下和放在 GOPATH 源码目录下是不大一样的。

我们可以将我们自己的包安装到 Go 语言包目录树下，也就是 GOROOT 下，但是这样没有什么好处而且可能会不太方便，因为有些系统是通过包管理系统来安装 Go 语言的，有些是通过安装包，有些是手动编译的。

**创建自定义的包**

我们创建的自定义的包最好就放在 GOPATH 的 src 目录下（或者 GOPATH src 的某个子目录），如果这个包只属于某个应用程序，可以直接放在应用程序的子目录下，但如果我们希望这个包可以被其他的应用程序共享，那就应该放在 GOPATH 的 src 目录下，每个包单独放在一个目录里，如果两个不同的包放在同一个目录下，会出现名字冲突的编译错误。

作为惯例，包的源代码应放在一个同名的文件夹下面。同一个包可以有任意多个文件，文件的名字也没有任何规定（但后续名必须是 .go），这里我们假设包名就是 .go 的文件名（如果一个包有多个 .go 文件，则其中会有一个 .go 文件的文件名和包名相同）。

stacker 例子由一个主程序（在 stacker.go 文件里）和一个自定义的 stack 包（在文件 stack.go 里）组成，源码目录的层次结构如下：
```go
aGoPath/src/stacker/stacker.go
aGoPath/src/stacker/stack/stack.go
```

GOPATH 环境变量是由多个目录路径组成且路径之间以冒号（Windows 上是分号）分隔开的字符串，这里的 aGoPath 就是 GOPATH 路径集合中的其中一个路径。

我们在 stacker 目录里执行 go build 命令，就会得到一个 stacker 的可执行文件（在 Windows 系统上是 stacker.exe）。但是，如果我们希望生成的可执行文件放到 GOPATH 的 bin 目录里，或者想将 stacker/stack 包共享给其他的应用程序使用，这就必须使用 go install 来完成。

当执行 go install 命令创建 stacker 程序时，会创建两个目录（如果不存在就会创建）：aGoPath/bin 和 aGoPath/pkg/linux_amd64/stacker，前者包含了 stacker 可执行文件，后者包含了 stack 包的静态库文件（至于 linux_amd64 等会根据不同的系统和硬件体系结构而变化，例如在 32 位的 Windows 系统上是 windows_386）。

需要在 stacker 程序中使用 stack 包时，在程序源文件中使用导入语句 import "stacker/stack" 即可，也就是绝对路径（Unix 风格）去除 aGoPath/src 这部分。事实上，只要这个包放在 GOPATH 下，都可以被别的程序或者包导入，GOPATH 下的包没有共享和专用之分。

又比如实现的有序映射是在 omap 包里，它被设计为可由多个程序使用。为了避免包名的冲突，我们在 GOPATH （如果 GOPATH 有多个路径，任意一个路径都可以）路径下创建了一个具有唯一名字（这里用了域名）的目录，结构如下：
```go
aGoPath/src/qtrac.eu/omap/omap.go
```

这样其他的程序，只要它们也在某个 GOPATH 目录下面，都可以通过使用 import "qtrac.eu/omap" 来导入这个包。如果我们还有其他的包需要共享，则将它们放到 aGoPath/src/qtrac.eu 路径下即可。

当使用 go install 安装 omap 包的时候，它创建了 aGoPath/pkg/linux_amd64/qtrac.eu 目录（如果不存在的话），保存了 omap 包的静态库文件，其中 linux_amd64 是根据不同的系统和硬件体系结构而变化的。

如果我们希望在一个包里创建新的包，例如，在 my_package 包下面创建两个新的包 pkg1 和 pkg2，可以这么做：在 aGoPath/src/my_package 建两个子目录，例如 aGoPath/src/my_package/pkg1 和 aGoPath/src/my_package/pkg2，对应的包文件是 aGoPath/src/my_package/pkg1/pkg1.go 和 aGoPath/src/my_package/pkg2/pkg2.go。

之后，假如想导入 pkg2，使用 import my_package/pkg2 即可。Go语言标准库的源码树就是这样的结构。当然，my_package 目录可以有它自己的包，如 aGoPath/src/my_package/my_package.go 文件。

Go 语言中的包导入的搜索路径是首先到 GOROOT（即 `$GOROOT/pkg/${GOOS}_${GOARCH}`，比如 /opt/go/pkg/linux_amd64），然后是 GOPATH 环境变量下的目录。这就意味这可能会有名字冲突。最简单的方法就是确保 GOPATH 里包含的每个路径都是唯一的，例如之前我们以域名来作为 omap 的包的目录。

在 Go 程序里使用标准库里的包和使用 GOPATH 路径下的包是一样的，下面几个小节我们来讨论一些平台特定的代码。

**平台特定的代码**

在某些情况下，我们必须为不同的平台编写一些特定的代码。例如，在类 Unix 的系统上，通常 shell 都支持通配符（也叫 globbing），所以在命令行输入 *.txt，程序就能够从 `os.Args[1:]` 切片里读取到比如 `["README.txt", "INSTALL.txt"]` 这些值。

但是在 Windows 平台上，程序只会接收到我们可以使用 `filepath.Glob()` 函数来实现通配符的功能，但是这只需要在 Windows 平台上使用。

那如何决定什么时候才需要使用 `filepath.Glob()` 函数呢，使用 `if runtime.GOOS == "windows” {...}` 即可，例如 cgrep1/cgrep1.go 程序等等。另一种办法就是使用平台特定的代码来实现，例如，cgrep3 程序有 3 个文件，cgrep.go、util_linux.go、util_windows.go，其中 util_linux.go 定义了这么一个函数：
```go
func commandLineFiles(files []string) []string { return files }
```

很明显，这个函数并没有处理文件名通配，因为在类 Unix 系统上没必要这么做。而 util_windows.go 文件则定义了另一个同名的函数。
```go
func commandLineFiles(files []string) []string {
    args := make([]string, 0, len(files))
    for _, name := range files {
        if matches, err := filepath.Glob(name); err != nil {
            args = append (args, name)    // 无效模式
        } else if matches ! = nil {       // 至少有一个匹配
            args = append(args, matches...)
        }
    }
    return args
}
```

当我们使用 go build 来创建 cgrep3 程序时，在 Linux 机器上 util_linux.go 文件会被编译而 util_windows.go 则被忽略，而在 Windows 平台恰好相反，这样就确保了只有一个 `commandLineFiles()` 函数被实际编译了。

在 Mac OS X 系统和 FreeBSD 系统上，既不会编译 util_linux.go 也不会编译 util_windows.go，所以 go build 会返回失败。但是我们可以创建一个软链接或者直接复制 util_linux.go 到 util_darwin.go 或者 util_freebsd.go，因为这两个平台的 shell 也是支持通配符的，这样就能正常构建 Mac OS X 和 FreeBSD 平台的程序了。

**导入包**

Go 语言允许我们对导入的包使用别名来标识。这个特性是非常方便和有用的，例如，可以在不同的实现之间进行自由的切换。举个例子，假如我们实现了 bio 包的两个版本 bio_v1 和 bio_v2，现在在某个程序里使用了 import bio "bio_v1"，如果需要切换到另一个版本的实现，只需要将 bio_v1 改成 bio_v2 即可，即 import bio "bio_v2"，但是需要注意的是，bio_v1 和 bio_v2 的 API 必须是相同的，或者 bio_v2 是 bio_v1 的超集，这样其余所有的的代码都不需要做任何改动。另外，最好就不要对官方标准库的包使用别名，因为这样可能会导致一些混淆或激怒后来的维护者。

当导入一个包时，它所有的 `init()` 函数就会被执行。有些时候我们并非真的需要使用这些包，仅仅是希望它的 `init()` 函数被执行而已。

举个例子，如果我们需要处理图像，通常会导入 Go 标准库支持的所有相关的包，但是并不会用到这些包的任何函数。下面就是 imagetag1.go 程序的导入语句部分。
```go
import (
    "fmt"
    "image"
    "os"
    "path/filepath"
    "runtime”
    _ "image/gif"
    _ "image/jpeg"
    _ "image/png"
)
```

这里导入了 image/gif、image/jpeg 和 image/png 包，纯粹是为了让它们的 `init()` 函数被执行（这些 `init()` 函数注册了各自的图像格式），所有这些包都以下划线作为别名，所以 Go 语言不会发出导入了某个包但是没有使用的警告。

---

## 导出包内标识符

下面代码中包含一系列未导出标识符，它们的首字母都为小写，这些标识符可以在包内自由使用，但是包外无法访问它们，代码如下：
```go
package mypkg

var myVar = 100

const myConst = "hello"

type myStruct struct {
}
```

将 myStruct 和 myConst 首字母大写，导出这些标识符，修改后代码如下：
```go
package mypkg

var myVar = 100

const MyConst = "hello"

type MyStruct struct {
}
```

此时，MyConst 和 MyStruct 可以被外部访问，而 myVar 由于首字母是小写，因此只能在 mypkg 包内使用，不能被外部包引用。

**导出结构体及接口成员**

在被导出的结构体或接口中，如果它们的字段或方法首字母是大写，外部可以访问这些字段和方法，代码如下：
```go
type MyStruct struct {

    // 包外可以访问的字段
    ExportedField int

    // 仅限包内访问的字段
    privateField int
}

type MyInterface interface {

    // 包外可以访问的方法
    ExportedMethod()

    // 仅限包内访问的方法
    privateMethod()
}
```

在代码中，MyStruct 的 ExportedField 和 MyInterface 的 `ExportedMethod()` 可以被包外访问。

---

# 包管理工具 dep

**什么是 dep？**

dep 和 go，在一定程度上相当于 maven 之于 Java，composer 之于 PHP，dep 是 go 语言官方的一个包管理工具。

相比较 go get 而言，dep 可以直接给引入的第三方包一个专门的目录，并且可以专门制定一个配置文件，控制 go 项目所引入的包，版本以及其他依赖关系。

**安装**

安装 dep 工具的方式有很多种，如果是 mac 电脑的话，只需要如下命令：
```
brew install dep
```
对于 Linux 和类 Unix 系统而言，我们还可以使用如下方式安装 dep：
```
curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
```
或者直接使用源码安装。

而对于 windows 电脑，可能会相对来说麻烦些

Download application: https://go.equinox.io/github.com/golang/dep/cmd/dep

Unzip and move the executable to %ProgramFiles%\ for system-wide use

Run %ProgramFiles%\dep.exe from PowerShell or cmd.

**使用**

dep 一般进场会使用 3 个命令：
- init-用来初始化项目
- status-用来查看当前项目的依赖包的状态
- ensure-用来同步包的配置文件和引入的包

下面我们正式使用 dep 来创建一个项目。首先建立一个项目路径，这里我们将项目路径叫做depProject。然后在项目路径中建立 src 源代码目录。在 src 中建立一个存放 dep 文件和项目主文件的目录，我们暂且可以叫做 depmain，并建立一个 go 文件。

这样我们的目录结构如下：
```
depProject
    |----src
          |----depmain
                  |-----main.go
```

建立好之后，我们在 main.go 中写一个简单的 go 程序：
```go
package main

import (
 "fmt"
)
func main() {
 fmt.Println("hello")
}
```

之后我们在这个目录下运行如下命令：
```
dep init
```

运行完成之后，dep 就会为我们自动生成如下文件和目录：


有点像常规 go 项目的样子了，不过需要注意的是 pkg 中存放的 go 语言引入包的缓存文件，vendor 中存放的是真正的引入的包内容。接下来是两个文件，Gopkg.lock 和 Gopkg.toml。Gopkg.lock 文件是自动生成的，而 Gopkg.toml 文件是我们可以编辑的文件，通过编辑这个文件，并运行 dep 的命令可以达到引入包的目的：

**go dep 不方便的地方**

新项目在自己工作目录下，使用 dep 初始化会报错：

而我并不希望将新项目的目录 my_project/go 加入到 GOPATH 中。

---

# go modules

**初始化**
```
go mod init test/go
go: creating new go.mod: module test/go

ls
go.mod

cat go.mod
module test/go

go 1.13
```

新建一个 gin main 文件 main.go
```go
package main

import "github.com/gin-gonic/gin"

func main() {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run() // listen and serve on 0.0.0.0:8080
}
```

执行 go build, 会看到目录下多了两个文件 go.sum 和 go_tool
```
ls
go.mod  go.sum  go_tool*  main.go
```

go.mod 随之更新
```
cat go.mod
module sunzhongwei.com/go_tool

go 1.13

require github.com/gin-gonic/gin v1.4.0
```

**go.mod 的作用是什么**

从上面的步骤来看，go build 可以自动下载依赖，那还要 go.mod 有什么用？

我觉得类似 composer install 一样，也是第一次更新 go.mod 文件，添加没有的依赖。

之后就会读取 go.mod。
