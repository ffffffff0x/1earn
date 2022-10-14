# time 包

---

**Source & Reference**

- [Go语言time包:时间和日期](http://c.biancheng.net/view/5392.html)

---

time 包为我们提供了一个数据类型 time.Time(作为值使用)以及显示和测量时间和日期的功能函数.

当前时间可以使用 `time.Now()` 获取，或者使用 `t.Day()`、`t.Minute()` 等等来获取时间的一部分;甚至可以自定义时间格式化字符串，例如:`fmt.Printf("%02d.%02d.%4d\n", t.Day(), t.Month(), t.Year())` 将会输出 21.07.2011.

Duration 类型表示两个连续时刻所相差的纳秒数，类型为 int64.Location 类型映射某个时区的时间，UTC 表示通用协调世界时间.

包中的一个预定义函数 func (t Time) Format(layout string) string 可以根据一个格式化字符串来将一个时间 t 转换为相应格式的字符串，可以使用一些预定义的格式，如:time.ANSIC 或 time.RFC822.

一般的格式化设计是通过对于一个标准时间的格式化描述来展现的，这听起来很奇怪，但看下面这个例子就会一目了然:
```go
fmt.Println(t.Format("02 Jan 2006 15:04"))
```

输出:
```
16 Oct 2019 16:31
```

---

```go
package main
import (
    "fmt"
    "time"
)
var week time.Duration
func main() {
    t := time.Now()
    fmt.Println(t)  // 2019-10-16 16:32:19.6001046 +0800 CST m=+0.009992501

    fmt.Printf("%02d.%02d.%4d\n", t.Day(), t.Month(), t.Year())
    // 16.10.2019

    t = time.Now().UTC()
    fmt.Println(t)          // 2019-10-16 08:32:58.7242797 +0000 UTC

    fmt.Println(time.Now()) // 2019-10-16 16:33:27.3045405 +0800 CST m=+0.080952501

    // calculating times:
    week = 60 * 60 * 24 * 7 * 1e9 // must be in nanosec
    week_from_now := t.Add(week)
    fmt.Println(week_from_now)    // 2019-10-23 08:33:53.6846208 +0000 UTC

    // formatting times:
    fmt.Println(t.Format(time.RFC822)) // 16 Oct 19 08:34 UTC

    fmt.Println(t.Format(time.ANSIC))  // Wed Oct 16 08:34:26 2019

    fmt.Println(t.Format("02 Jan 2006 15:04")) // 16 Oct 2019 08:34

    s := t.Format("20060102")
    fmt.Println(t, "=>", s)
    // 2019-10-16 08:34:26.5230908 +0000 UTC => 20191016
}
```

如果需要在应用程序在经过一定时间或周期执行某项任务(事件处理的特例)，则可以使用 time.After 或者 time.Ticker.另外，time.Sleep(Duration d)可以实现对某个进程(实质上是 goroutine)时长为 d 的暂停.
