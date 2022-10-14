# OS 包

---

**Source & Reference**

- [Go语言os包用法简述](http://c.biancheng.net/view/5572.html)

---

os 标准包，是一个比较重要的包，顾名思义，主要是在服务器上进行系统的基本操作，如文件操作，目录操作，执行命令，信号与中断，进程，系统状态等等.在 os 包下，有 exec，signal，user 三个子包.

**启动外部命令和程序**

写命令行程序时需要对命令参数进行解析，这时我们可以使用 os 库.os 库可以通过变量 Args 来获取命令参数，os.Args 返回一个字符串数组，其中第一个参数就是执行文件本身.
```go
package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println(os.Args)
}
```

编译执行后执行
```
$ ./cmd -user="root"
[./cmd -user=root]
```

这种方式对于简单的参数格式还能使用，一旦面对复杂的参数格式，比较费时费劲，所以这时我们会选择 flag 库.

在 os 包中，相关函数名字和作用有较重的 Unix 风，比如:
```go
func Chdir(dir string) error //chdir 将当前工作目录更改为 dir 目录
func Getwd() (dir string, err error) //获取当前目录
func Chmod(name string, mode FileMode) error //更改文件的权限
func Chown(name string, uid, gid int) error //更改文件拥有者 owner
func Chtimes(name string, atime time.Time, mtime time.Time) error func Clearenv() //清除所有环境变量(慎用)
func Environ() []string //返回所有环境变量
func Exit(code int) //系统退出，并返回 code，其中 0 表示执行成功并退出，非 0 表示错误并退出
```

在 os 包中，有关文件的处理也有很多方法，如:
```go
func Create(name string) (file File, err error) // Create 采用模式 0666 创建一个名为 name 的文件，如果文件已存在会截断它(为空文件)
func Open(name string) (file File, err error) // Open 打开一个文件用于读取.
func (f File) Stat() (fi FileInfo, err error) // Stat 返回描述文件 f 的 FileInfo 类型值
func (f File) Readdir(n int) (fi []FileInfo, err error) // Readdir 读取目录 f 的内容，返回一个有 n 个成员的 []FileInfo
func (f File) Read(b []byte) (n int, err error) // Read 方法从 f 中读取最多 len(b) 字节数据并写入 b
func (f File) WriteString(s string) (ret int, err error) // 向文件中写入字符串
func (f File) Sync() (err error) // Sync 递交文件的当前内容进行稳定的存储.
func (f File) Close() error // Close 关闭文件 f
```

在 os 包中有一个 StartProcess 函数可以调用或启动外部系统命令和二进制可执行文件;它的第一个参数是要运行的进程，第二个参数用来传递选项或参数，第三个参数是含有系统环境基本信息的结构体.

这个函数返回被启动进程的 `id(pid)`，或者启动失败返回错误.
```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // 1) os.StartProcess //
    /*********************/
    /* Linux: */
    env := os.Environ()
    procAttr := &os.ProcAttr{
        Env: env,
        Files: []*os.File{
            os.Stdin,
            os.Stdout,
            os.Stderr,
        },
    }
    // 1st example: list files
    Pid, err := os.StartProcess("/bin/ls", []string{"ls", "-l"}, procAttr)
    if err != nil {
        fmt.Printf("Error %v starting process!", err) //
        os.Exit(1)
    }
    fmt.Printf("The process id is %v", pid)
}
```

**os/signal 信号处理**

一个运行良好的程序在退出(正常退出或者强制退出，如 ctrl+c，kill 等)时是可以执行一段清理代码，将收尾工作做完后再真正退出.一般采用系统 Signal 来通知系统退出，如 kill pid.在程序中针对一些系统信号设置了处理函数，当收到信号后，会执行相关清理程序或通知各个子进程做自清理.

Go 语言的系统信号处理主要涉及 os 包、os.signal 包以及 syscall 包.其中最主要的函数是 signal 包中的 Notify 函数:
```go
func Notify(c chan<- os.Signal, sig …os.Signal)
```

该函数会将进程收到的系统 Signal 转发给 channel c.如果没有传入 sig 参数，那么 Notify 会将系统收到的所有信号转发给 channel c.

Notify 会根据传入的 os.Signal，监听对应 Signal 信号，`Notify()` 方法会将接收到对应 os.Signal 往一个 channel c 中发送.

下面代码以 syscall.SIGUSR2 信息为例，说明了具体实现:
```go
package main

import (
    "fmt"
    "os"
    "os/signal"
    "syscall"
    "time"
)

func main() {
    go signalListen()
    for {
        time.Sleep(10 * time.Second)
    }
}

func signalListen() {
    c := make(chan os.Signal)
    signal.Notify(c, syscall.SIGUSR2)
    for {
        s := <-c
        //收到信号后的处理，这里只是输出信号内容，可以做一些更有意思的事
        fmt.Println("get signal:", s)
    }
}
```
