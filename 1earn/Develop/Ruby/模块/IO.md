# IO

---

- https://www.kancloud.cn/imxieke/ruby-base/107305

---

IO 类的主要作用就是让程序与外部进行数据的输入（input）/ 输出（output）操作。

# 输入 / 输出的种类

**标准输入 / 输出**

程序在启动后会预先分配 3 个 IO 对象。

- 标准输入

    标准输入可以获取从键盘输入的内容。通过预定义常量 `STDIN` 可调用操作标准输入的 IO 对象。另外，用全局变量 `$stdin` 也可以引用标准输入的 IO 对象。不指定接收者的 `gets` 方法等都会默认从标准输入中获取数据。

- 标准输出

    向标准输出写入的数据会显示在屏幕中。通过预定义常量 `STDOUT` 可调用操作标准输出的 IO 对象。另外，用全局变量 `$stdout` 也可以引用标准输出的 IO 对象。不指定接收者的 `puts`、`print`、`printf` 等方法会默认将数据写入到标准输出。

- 标准错误输出

    向标准错误输出写入的数据会显示在屏幕中。通过预定义常量 `STDERR` 可调用操作标准错误输出的 IO 对象。另外，用全局变量 `$stderr` 也可以引用标准错误输出的 IO 对象。

    标准错误输出原本是用于输出错误信息的，但实际上，除输出警告或者错误之外，在希望与程序正常输出的信息做出区别时也可以使用它
    ```ruby
    $stdout.print "Output to $stdout.\n"  # 标准输出
    $stderr.print "Output to $stderr.\n"  # 标准错误输出
    ```
    执行示例
    ```
    > ruby out.rb
    Output to $stdout.
    Output to $stderr.
    ```

    将输出结果重定向到文件时，标准输出的内容会被写入到文件，只有标准错误输出的内容被输出到屏幕中。
    ```
    执行示例
    > ruby out.rb > log.txt
    Output to $stderr.
    ```
    在执行程序时，在命令后加上 `>` 文件名，就可以将程序执行时的输出结果保存到文件中。我们把这个控制台的功能称为“重定向”。通过这个功能，不仅 ruby 命令，程序的输出内容也都可以保存在文件中。

根据需要灵活使用标准输出与标准错误输出，可以使我们很方便地分开获取正常信息与错误信息。

> 备注　ruby 命令的错误信息也会被输出到标准错误输出。

通常标准输入、标准输出、标准错误输出都是与控制台关联的。但是将命令的输出重定向到文件，或者使用管道（pipe）将结果传递给其他程序时则与控制台没有关系。根据实际的使用情况，程序的输入 `/` 输出状态也各异。IO 对象是否与控制台关联，我们可以通过 `tty?` 方法判断。

一个检查标准输入是否为屏幕的例子
```ruby
if $stdin.tty?
  print "Stdin is a TTY.\n"
else
  print "Stdin is not a TTY.\n"
end
```

下面我们用不同的方式调用这个程序，看看有何不同。首先是普通调用。

执行示例
```
> ruby tty.rb
Stdin is a TTY.
```
将命令的输出结果传给管道，或者通过文件输入内容时，程序的结果会不一样。

执行示例
```
> echo | ruby tty.rb
Stdin is not a TTY.
> ruby tty.rb < data.txt
Stdin is not a TTY.
```
> TTY 是 TeleTYpe 的缩写。

**文件输入 / 输出**

通过 `IO` 类的子类 `File` 类可以进行文件的输入 `/` `输出处理。File` 类中封装了文件删除、文件属性变更等文件专用的功能，而一些基本的输入 `/` 输出处理则使用继承自 `IO` 类的方法。

- **io= File.open(file, mode)**
- **io = open(file, mode)**

    通过 `File.open` 方法或 `open` 方法打开文件并获取新的 `IO` 对象。

    模式（mode）会指定以何种目的打开文件。缺省模式为只读模式（`"r"`）。在 Windows 环境下，在各模式后加上 `b`、通过 `"rb"`、`"rb+"` 等这样的形式即可表示二进制模式（后述）。

    模式 | 意义
    -   | -
    r   | 用只读模式打开文件。
    r+  | 用读写模式打开文件。
    w   | 用只写模式打开文件。文件不存在则创建新的文件；文件已存在则清空文件，即将文件大小设置为0。
    w+  | 读写模式，其余同 "w" 。
    a   | 用追加模式打开文件。文件不存在则创建新的文件。
    a+  | 用读取/ 追加模式打开文件。文件不存在则创建新的文件。

- **io.close**

    使用 `close` 方法关闭已打开的文件。

    1 个程序中同时打开文件的数量是有限制的，因此使用完的文件应该尽快关闭。如果打开多个文件而不进行关闭操作，程序就很可能会在使用 `open` 方法时突然产生异常。

    `File.open` 方法如果使用块，则文件会在使用完毕后自动关闭。这种情况下，`IO` 对象会被作为块变量传递给块。块执行完毕后，块变量引用的 `IO` 对象也会自动关闭。这种写法会使输入 `/` 输出的操作范围更加清晰。
    ```ruby
    File.open("foo.txt") do |io|
    while line = io.gets
        ┊
    end
    end
    ```

- **io.close?**

    用 `close?` 方法可以检查 `IO` 对象是否关闭了。
    ```ruby
    io = File.open("foo.txt")
    io.close
    p io.closed?    #=> true
    ```

- **File.read(file)**

    使用类方法 `read` 可以一次性读取文件 `file` 的内容。
    ```ruby
    data = File.read("foo.txt")
    ```
    > 在 Windows 中不能使用 `File.read` 方法读取像图像数据等二进制数据。`File.read` 方法使用文本模式打开文件时，会对换行符等进行转换，因此无法得到正确的结果。

# 基本的输入 / 输出操作

输入 / 输出操作的数据为字符串，也就是所谓的 `String` 对象。执行输入操作后，会从头到尾按顺序读取数据，执行输出操作后，则会按写入顺序不断追加数据。

**输入操作**

- **io.gets(rs)**
- **io.each(rs)**
- **io.each_line(rs)**
- **io.readlines(rs)**

    从 `IO` 类的对象 `io` 中读取一行数据。用参数 `rs` 的字符串分行。省略 `rs` 时则用预定义变量 `$/`（默认值为 `"\n"`）。

    这些方法返回的字符串中包含行末尾的换行符。用 `chmop!` 方法可以很方便地删除字符串末尾的换行符。

    输入完毕后再尝试获取数据时，`gets` 方法会返回 `nil`。另外，我们还可以使用 `eof?` 方法检查输入是否已经完毕。
    ```ruby
    while line = io.gets
    line.chomp!
        ┊        # 对line 进行的操作
    end
    p io.eof?     #=> true
    ```

    `while` 条件表达式中同时进行了变量赋值与条件判断的操作。将 `gets` 方法的返回值复制给 `line`，并将该值作为 `while` 语句的条件来判断。上面是 `gets` 方法的经典用法，大家应该尽快掌握这种写法。

    用 `each_line` 方法也可以实现同样的效果。
    ```ruby
    io.each_line do |line|
    line.chomp!
        ┊        # 对line 进行的操作
    end
    ```

    另外，用 `readlines` 方法可以一次性地读取所有数据，并返回将每行数据作为元素封装的数组。
    ```ruby
    ary = io.readlines
    ary.each_line do |line|
    line.chomp!
        ┊        # 对line 进行的操作
    end
    ```

    > gets 方法与 puts 方法，分别是“get string”、“put string”的意思。

- **io.lineno**
- **io.lineno=(number)**

    使用 `gets` 方法、`each_line` 方法逐行读取数据时，会自动记录读取的行数。这个行数可以通过 `lineno` 方法取得。此外，通过 `lineno=` 方法也可以改变这个值，但值的改变并不会对文件指针（后述）有影响。

    在下面的例子中，逐行读取标准输入的数据，并在行首添加行编号。
    ```ruby
    $stdin.each_line do |line|
    printf("%3d %s", $stdin.lineno, line)
    end
    ```

- **io.each_char**

    逐个字符地读取 `io` 中的数据并执行块。将得到的字符（`String` 对象）作为块变量传递。

- **io.getc**

    只读取 `io` 中的一个字符。根据文件编码的不同，有时一个字符会由多个字节组成，但这个方法只会读取一个字符，然后返回其字符串对象。数据全部读取完后再读取时会返回 `nil`。
    ```ruby
    while ch = io.getc
    ┊       # 对line 进行的操作
    end
    ```

- **io.ungetc(ch)**

    将参数 `ch` 指定的字符退回到 `io` 的输入缓冲中。
    ```ruby
    # hello.txt 中的内容为“Hello, Ruby.\n”
    File.open("hello.txt") do |io|
    p io.getc  #=> "H"
    io.ungetc(72)
    p io.gets  #=> "Hello, Ruby.\n"
    end
    ```
    指定一个字符大小的字符串对象。对可退回的字符数没有限制。

- **io.getbyte**

    只读取 `io` 中的一个字节，返回得到的字节转换为 `ASCII` 码后的整数对象。数据全部读取完后再读取时会返回 `nil`。

- **io.ungetbyte(byte)**

    将参数 `byte` 指定的一个字节退回到输入缓冲中。参数为整数时，将该整数除以 256 后的余数作为 ASCII 码字符返回一个字节；参数为字符串时，只返回字符串的第一个字节。

- **io.read(size)**

    读取参数 `size` 指定的大小的数据。不指定大小时，则一次性读取全部数据并返回。
    ```ruby
    # hello.txt 中的内容为"Hello, Ruby.\n"
    File.open("hello.txt") do |io|
    p io.read(5)  #=> "Hello"
    p io.read     #=> ",Ruby.\n"
    end
    ```

**输出操作**

- **io.puts(str0, str1, …)**

    对字符串末尾添加换行符后输出。指定多个参数时，会分别添加换行符。如果参数为 `Sting` 类以外的对象，则会调用 `to_s` 方法，将其转换为字符串后再输出。
    ```ruby
    $stdout.puts "foo", "bar", "baz"
    ```
    执行示例
    ```
    > ruby stdout_put.rb
    foo
    bar
    baz
    ```

- **io.putc(ch)**

    输出参数 `ch` 指定的字符编码所对应的字符。参数为字符串时输出首字符。
    ```ruby
    $stdout.putc(82)  # 82 是R 的ASCII 码
    $stdout.putc("Ruby")
    $stdout.putc("\n")
    ```
    执行示例
    ```
    > ruby stdout_putc.rb
    RR
    ```

- **io.print(str0, str1, …)**

    输出参数指定的字符串。参数可指定多个字符串。参数为 `String` 以外的对象时会自动将其转换为字符串。

- **io.printf(fmt, arg0, arg1, …)**

    按照指定的格式输出字符串。格式 `fmt` 的用法与 `printf` 方法一样

- **io.write(str)**

    输出参数 `str` 指定的字符串。参数为 `String` 以外的对象时会自动将其转换为字符串。方法返回值为输出的字节数。
    ```ruby
    size = $stdout.write("Hello.\n")    #=> Hello.
    p size                              #=> 6
    ```

- **io<<str**

    输出参数 `str` 指定的字符串。`<<` 会返回接收者本身，因此可以像下面这样写：
    ```ruby
    io << "foo" << "bar" << "baz"
    ```

# 文件指针

一般情况下，我们会以行为单位处理文本数据。由于只有当读取到换行符时才能知道行的长度，因此，如要读取第 100 行的数据，就意味着要将这 100 行的数据全部读取。另外，如果我们修改了数据，行的长度也会随之变更，这样一来，文件中后面的数据就都要做出修改。

为了提高读取效率，可以将文件分成固定长度的文件块，来直接访问某个位置的数据（虽然据此可以访问任意位置的数据，但却不能处理超过指定长度的数据）。

我们用文件指针（file pointer）或者当前文件偏移量（current file offset）来表示 `IO` 对象指向的文件的位置。每当读写文件时，文件指针都会自动移动，而我们也可以使文件指针指向任意位置来读写数据。

- **io.pos**
- **io.pos=(position)**

    通过 `pos` 方法可以获得文件指针现在的位置。改变文件指针的位置用 `pos=` 方法。
    ```ruby
    # hello.txt 中的内容为"Hello, Ruby.\n"
    　
    File.open("hello.txt") do |io|
    p io.read(5)    #=> "Hello"
    p io.pos        #=> 5
    io.pos = 0
    p io.gets       #=> "Hello, Ruby.\n"
    end
    ```

- **io.seek(offset, whence)**

    移动文件指针的方法。参数 `offset` 为用于指定位置的整数，参数 `whence` 用于指定 `offset` 如何移动

    whence	| 意义
    - | -
    IO::SEEK_SET	| 将文件指针移动到 offset 指定的位置
    IO::SEEK_CUR	| 将 offset 视为相对于当前位置的偏移位置来移动文件指针
    IO::SEEK_END	| 将 offset 指定为相对于文件末尾的偏移位置

- **io.rewind**

    将文件指针返回到文件的开头。`lineno` 方法返回的行编号为 0。
    ```ruby
    # hello.txt 中的内容为"Hello, Ruby.\n"
    File.open("hello.txt")do |io|
    p io.gets    #=> "Hello,Ruby.\n"
    io.rewind
    p io.gets    #=> "Hello, Ruby.\n"
    end
    ```

- **io.truncate(size)**

    按照参数 `size` 指定的大小截断文件。
    ```ruby
    io.truncate(0)         # 将文件大小置为0
    io.truncate(io.pos)    # 删除当前文件指针以后的数据
    ```

# 二进制模式与文本模式

不同平台下的换行符也不同。

虽然各个平台的换行符不一样，但为了保证程序的兼容性，会将字符串中的 `"\n"` 转换为当前 OS 的换行符并输出。此外，在读取的时候也会将实际的换行符转换为 `"\n"`。

下图是 Windows 中转换换行符的情形

![image](../../../../assets/img/Develop/Ruby/模块/IO/1.png)

**Windows 环境中字符 "\n" 的转换**

当需要确定文件大小进行输入 `/` 输出处理时，或者直接使用从其他平台拷贝的文件时，如果进行换行符转换，就有可能会引发问题。

为了解决上述那样的问题，Ruby 中还提供了不进行换行符转换的方法。换行符处理的前提是以行为单位做输入 / 输出处理，需要转换时称为文本模式，反之不需要转换时则称为二进制模式。

- **io.binmode**

    新的 `IO` 对象默认是文本模式，使用 `binmode` 方法可将其变更为二进制模式。
    ```ruby
    File.open("foo.txt", "w") do |io|
    io.binmode
    io.write "Hello, world.\n"
    end
    ```
    这样就可以既不用转换换行符，又能得到与文件中一模一样的数据。

    > 转换为二进制模式的 IO 对象无法再次转换为文本模式。

# 缓冲

即使对 `IO` 对象输出数据，结果也并不一定马上就会反映在控制台或者文件中。在使用 `write`、`print` 等方法操作 `IO` 对象时，程序内部会开辟出一定的空间来保存临时生成的数据副本。这部分空间就称为缓冲（buffer）。缓冲里累积一定量的数据后，就会做实际的输出处理，然后清空缓冲。

![image](../../../../assets/img/Develop/Ruby/模块/IO/2.png)

像这样，使用临时缓冲进行数据处理称为缓冲处理（buffering）。

在向控制台输出的两种方式（标准输出与标准错误输出）中，标准错误输出完全不采用缓冲处理。因此，当两种方式混合使用时，程序实际输出的顺序可能会与程序代码中记录的顺序不一样。
```ruby
$stdout.print "out1 "
$stderr.print "err1 "
$stdout.print "out2 "
$stdout.print "out3 "
$stderr.print "err2\n"
$stdout.print "out4\n"
```
执行示例
```
> ruby test_buffering1.rb
err1 err2
out1 out2 out3 out4
```

标准错误输出的主要目的是输出如警告、错误等信息，因此执行结果必须马上反映出来。再次强调，建议在显示程序中正常信息以外的信息时使用标准错误输出。

虽然缓冲处理可以提高输出效率，但有时候我们会希望执行结果可以马上反映出来，这时我们就可以用下面的方法来同步数据的操作与输出。

- **io.flush**

    强制输出缓冲中的数据。在基础上追加 `$stdout.flush` 的调用。
    ```ruby
    $stdout.print "out1 "; $stdout.flush
    $stderr.print "err1 "
    $stdout.print "out2 "; $stdout.flush
    $stdout.print "out3 "; $stdout.flush
    $stderr.print "err2\n"
    $stdout.print "out4\n"
    ```
    执行示例
    ```
    > ruby test_buffering2.rb
    out1 err1 out2 out3 err2
    out4
    ```

- **io.sync**
- **io.sync=(state)**

    通过 `io.sync = true`，程序写入缓冲时 `flush` 方法就会被自动调用。
    ```ruby
    $stdout.sync = true  # 同步输出处理
    $stdout.print "out1 "
    $stderr.print "err1 "
    $stdout.print "out2 "
    $stdout.print "out3 "
    $stderr.print "err2\n"
    $stdout.print "out4\n"
    ```
    即使不逐次调用 flush 方法，也可以像下面那样按顺序输出：
    ```
    > ruby test_buffering3.rb
    out1 err1 out2 out3 err2
    out4
    ```

# 与命令进行交互

虽然 Ruby 是几乎什么都能实现的强大的语言，但是也会有与其他命令进行数据交换的时候。例如，读取使用 GUN zip 压缩的数据的时候，使用 gunzip 命令会很方便。在 Ruby 中，使用 `IO.popen` 方法可以与其他命令进行数据处理。

- **IO.popen(command, mode)**

    参数 `mode` 的使用方法与 `File.open` 方法是一样的，参数缺省时默认为 `"r"` 模式。

    用 `IO.popen` 方法生成的 `IO` 对象的输入 / 输出，会关联启动后的命令 command 的标准输入 / 输出。也就是说，`IO` 对象的输出会作为命令的输入，命令的输出则会作为 `IO` 对象的输入。

    利用 `gunzip` 命令解压处理扩展名为 `.gz` 的文件（`-c` 为将解压后的结果写入到标准输出时的选项）。
    ```ruby
    pattern = Regexp.new(ARGV[0])
    filename = ARGV[1]
    if /.gz$/ =~ filename
    file = IO.popen("gunzip -c #{filename}")
    else
    file = File.open(filename)
    end
    file.each_line do |text|
    if pattern =~ text
        print text
    end
    end
    ```

- **open("|command", mode)**

    将带有管道符号的命令传给 `open` 方法的效果与使用 `IO.popen` 方法是一样的。
    ```ruby
    filename = ARGV[0]
    open("|gunzip -c #{filename}") do |io|
    io.each_line do |line|
        print line
    end
    end
    ```

# open-uri 库

除了控制台、文件以外，进程间通信时使用的管道（pipe）、网络间通信时使用的套接字（socket）也都可以作为 `IO` 对象使用。

通过 `require` 引用 `open-uri` 库后，我们就可以像打开普通的文件一样打开 HTTP、FTP 的 URL。使用 `open-uri` 库的功能时，不要使用 `File.open` 方法，只使用 `open` 方法即可。
```ruby
require "open-uri"

# 通过HTTP 读取数据
open("http://www.ruby-lang.org") do |io|
  puts io.read  # 将Ruby 的官方网页输出到控制台
end

# 通过FTP 读取数据
url = "ftp://www.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p0.tar.gz"
open(url) do |io|
  open("ruby-2.0.0-p0.tar.gz", "w") do |f|  # 打开本地文件
    f.write(io.read)
  end
end
```

通过 HTTP 协议时，服务器会根据客户端的状态改变应答的内容，比如返回中文或英语的网页等。为了实现这个功能，请求时就需要向服务器发送元信息（meta information）。

例如，HTTP 头部信息 Accept-Language 就表示优先接收中文网页。指定 HTTP 头部信息时，会将其以散列的形式传递给 open 方法的第 2 个参数。
```ruby
require "open-uri"

options = {
  "Accept-Language" => "zh-cn, en;q=0.5",
}
open("http://www.ruby-lang.org", options){|io|
  puts io.read
}
```

# stringio 库

在测试程序时，虽然我们会希望知道向文件或控制台输出了什么，但程序实际执行的结果却往往很难知道。为此，我们可以通过向模拟 `IO` 对象的对象进行输出来确认执行结果。

`StringIO` 就是用于模拟 `IO` 对象的对象。通过 `require` 引用 `stringio` 库后，就可以使用 `StringIO` 对象了。
```ruby
require "stringio"

io = StringIO.new
io.puts("A")
io.puts("B")
io.puts("C")
io.rewind
p io.read  #=> "A\nB\nC\n"
```

实际上，向 `StringIO` 对象进行的输出并不会被输出到任何地方，而是会被保存在对象中，之后就可以使用 `read` 方法等来读取该输出。

`StringIO` 对象还有另外一种用法，那就是将字符串数据当作 `IO` 数据处理。将大数据保存在文件中，并将小数据直接传输给别的处理时，通过使用 `StringIO` 对象，程序就可以不区分对待 `IO` 对象和字符串了。实际上，之前介绍的用 `open-uri` 库打开 `URI` 时，也是有时候返回 IO 对象，有时候返回 `StringIO` 对象。不过一般情况下，我们不需要在意这两者的区别。通过将数据字符串传递给 `StringIO.new` 方法的参数，就可以由字符串创建 `StringIO` 对象。
```ruby
require "stringio"

io = StringIO.new("A\nB\nC\n")
p io.gets  #=> "A\n"
p io.gets  #=> "B\n"
p io.gets  #=> "C\n"
```
