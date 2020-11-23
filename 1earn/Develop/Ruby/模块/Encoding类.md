# Encoding 类

---

- https://www.kancloud.cn/imxieke/ruby-base/107307

---

# Ruby 的编码与字符串

字符编码是计算机进行字符操作的基础，字符编码有多种，而且即使是在同一个程序中，有时候输入 / 输出的字符编码也有可能不一样。例如程序输入是 `UTF-8` 字符编码，而输出却是 `Shift_JIS` 字符编码等情况。虽然“あ”的 `UTF-8` 的字符编码与 `Shift_JIS` 的字符编码实际上是不同的，但经过适当的转换，也是可以编写这样的程序的。

至于程序如何处理字符编码，不同的编程语言有不同的解决方案。Ruby 的每个字符串对象都包含“字符串数据本身”以及“该数据的字符编码”两个信息。其中，关于字符编码的信息即我们一般所讲的编码。

创建字符串对象一般有两种方法，一种是在脚本中直接以字面量的形式定义，另外一种是从程序的外部（文件、控制台、网络等）获取字符串数据。数据的获取方式决定了它的编码方式。截取字符串的某部分，或者连接多个字符串生成新字符串等的时候，编码会继承原有的字符串的编码。

程序向外部输出字符串时，必须指定适当的编码。

Ruby 会按照以下信息决定字符串对象的编码，或者在输入 / 输出处理时转换编码。

# 脚本编码与魔法注释

Ruby 脚本的编码就是通过在脚本的开头书写魔法注释来指定的。

脚本自身的编码称为脚本编码（script encoding）。脚本中的字符串、正则表达式的字面量会依据脚本编码进行解释。脚本编码为 EUC-JP 时，字符串、正则表达式的字面量也都为 EUC-JP。同样，如果脚本编码为 Shift_JIS，那么字符串、正则表达式的字面量也为 Shift_JIS。

我们把指定脚本编码的注释称为魔法注释（magic comment）。Ruby 在解释脚本前，会先读取魔法注释来决定脚本编码。

魔法注释必须写在脚本的首行（第 1 行以 #! ～ 开头时，则写在第 2 行）。下面是将脚本编码指定为 UTF-8 的例子。
```ruby
# encoding: utf-8
```

> 在 Unix 中，赋予脚本执行权限后，就可以直接执行脚本。这时，可以在文件开头以 `#!` 命令的路径 的形式来指定执行脚本的命令。在本书的例子中，我们经常使用 >ruby 脚本名 这样的形式来表示 在命令行执行脚本的命令为 ruby，但若像“#! /usr/bin/ruby”这样，在文件开头写上 ruby 命令的路径的话，那么就能直接以 `>` 脚本名的形式执行脚本了。

此外，为了可以兼容 Emacs、VIM 等编辑器的编码指定方式，我们也可以像下面这样写。
```ruby
# -*- coding: utf-8 -*-        # 编辑器为Emacs 的时候
# vim:set fileencoding=utf-8:  # 编辑器为VIM 的时候
```
程序代码的编码会严格检查是否与脚本编码一致。因此，有时候直接写上日语的字符串后就会产生错误。

```ruby
# encoding: US-ASCII
a = 'こんにちは'    #=> invalid multibyte char (US-ASCII)
```

由于 US-ASCII 不能表示日语的字符串，因此会产生错误。在 Ruby1.9 中，没有魔法注释时默认脚本编码也为 US-ASCII，因此也会产生这个错误。

为了使日语或中文字符能正常显示，必须指定适当的编码。而在 Ruby2.0 中，由于没有魔法注释时的默认脚本编码为 UTF-8，因此如果代码是以 UTF-8 编码编写的话，那么就无须使用魔法注释了。

但有时仅使用魔法注释是不够的。例如，使用特殊字符 `\u` 创建字符串后，即使脚本编码不是 UTF-8，其生成的字符串也一定是 UTF-8。
```ruby
# encoding: EUC-JP
a = "\u3042\u3044"
puts a          #=> "あい"
p a.encoding    #=> #<Encoding:UTF-8>
```
因此，必须使用 `encode!` 方法明确进行编码转换。
```ruby
# encoding: EUC-JP
a = "\u3042\u3044"
a.encode!("EUC-JP")
p a.encoding    #=> #<Encoding:EUC-JP>
```
这样，变量 `a` 的字符串的编码也就变为 EUC-JP 了。

# Encoding 类

我们可以用 `String.encoding` 方法来调查字符串的编码。`String.encoding` 方法返回 `Encoding` 对象。
```ruby
p "こんにちは".encoding #=> #<Encoding:UTF-8>
```
本例中的“こんにちは”字符串对象的编码为 UTF-8。

> 日语 Windows 环境中的字符编码一般为 Windows-31J。这是 Windows 专用的扩展自 Shift_JIS 的编码，例如，Shift_JIS 中原本并没有①。Windows-31J 还有一个别名叫 CP932（Microsoft code page932 的意思），在互联网上就字符编码讨论时，有时候会用到这个名称。

在脚本中使用不同的编码时，需要进行必要的转换。我们可以用 `String.encode` 方法转换字符串对象的编码。
```ruby
str = "こんにちは"
p str.encoding     #=> #<Encoding:UTF-8>
str2 = str.encode("EUC-JP")
p str2.encoding    #=> #<Encoding:EUC-JP>
```
在本例中，我们尝试把 UTF-8 字符串对象转换为新的 EUC-JP 字符串对象。

在操作字符串时，Ruby 会自动进行检查。例如，如果要连接不同编码的字符串则会产生错误。
```ruby
# encoding: utf-8

str1 = "こんにちは"
p str1.encoding    #=> #<Encoding:UTF-8>
str2 = "あいうえお".encode("EUC-JP")
p str2.encoding    #=> #<Encoding:EUC-JP>
str3 = str1 + str2 #=> incompatible character encodings: UTF-8
                   #=> and EUC-JP(Encoding::CompatibilityError)
```
为了防止错误，在连接字符串前，必须使用 `encode` 方法等把两者转换为相同的编码。

还有，在进行字符串比较时，如果编码不一样，即使表面的值相同，程序也会将其判断为不同的字符串。
```ruby
# encoding: utf-8
p "あ" == "あ".encode("Shift_JIS")    #=> false
```
另外，在本例中，用 `String.encode` 指定编码时，除了可以使用编码名的字符串外，还可以直接使用 `Encoding` 对象来指定。

**Encoding 类的方法**

接下来，我们将会介绍 `Encoding` 类的方法。

- `Encoding.compatible?(str1, str2)`

    检查两个字符串的兼容性。这里所说的兼容性是指两个字符串是否可以连接。可兼容则返回字符串连接后的编码，不可兼容则返回 `nil`。
    ```ruby
    p Encoding.compatible?("AB".encode("EUC-JP"),
                        "あ".encode("UTF-8"))    #=> #<Encoding:UTF-8>
    p Encoding.compatible?("あ".encode("EUC-JP"),
                        "あ".encode("UTF-8"))    #=> nil
    ```
    AB 这个字符串的编码无论是 EUC-JP 还是 UTF-8 都是一样的，因此，将其转换为 EUC-JP 后也可以与 UTF-8 字符串连接；而あ这个字符串则无法连接，因此返回 `nil`。

- `Encoding.default_external`

    返回默认的外部编码，这个值会影响 `IO` 类的外部编码。

- `Encoding.default_internal`

    返回默认的内部编码，这个值会影响 `IO` 类的内部编码。

- `Encoding.find(name)`

    返回编码名 `name` 对应的 `Encoding` 对象。预定义的编码名由不含空格的英文字母、数字与符号构成。查找编码的时候不区分 `name` 的大小写。
    ```ruby
    p Encoding.find("Shift_JIS")   # => #<Encoding:Shift_JIS>
    p Encoding.find("shift_JIS")   # => #<Encoding:Shift_JIS>
    ```

    特殊的编码名
    名称	    | 意义
    - | -
    locale	    | 根据本地信息决定的编码
    external	| 默认的外部编码
    internal	| 默认的内部编码
    filesystem	| 文件系统的编码

- `Encoding.list`
- `Encoding.name_list`

    返回 Ruby 支持的编码一览表。`list` 方法返回的是 `Encoding` 对象一览表，`Encoding.name_list` 返回的是表示编码名的字符串一览表，两者的结果都以数组形式返回。
    ```ruby
    p Encoding.list
        #=> [#<Encoding:ASCII-8BIT>, #<Encoding:UTF-8>, ...
    p Encoding.name_list
        #=> ["ASCII-8BIT", "UTF-8", "US-ASCII", "Big5", ...
    ```

- `enc.name`

    返回 `Encoding` 对象 `enc` 的编码名。
    ```ruby
    p Encoding.find("shift_jis").name    #=> "Shift_JIS"
    ```

- `enc.names`

    像 EUC-JP、eucJP 这样，有些编码有多个名称。这个方法会返回包含 `Encoding` 对象的名称一览表的数组。只要是这个方法中的编码名称，都可以在通过 `Encoding.find` 方法检索时使用。
    ```ruby
    enc = Encoding.find("Shift_JIS")
    p enc.names    #=> ["Shift_JIS", "SJIS"]
    ```

**ASCII-8BIT 与字节串**

ASCII-8BIT 是一个特殊的编码，被用于表示二进制数据以及字节串。因此有时候我们也称这个编码为 BINARY。

此外，把字符串对象用字节串形式保存的时候也会用到这个编码。例如，使用 `Array.pack` 方法将二进制数据生成为字符串时，或者使用 `Marsha1.dump` 方法将对象序列化后的数据生成为字符串时，都会使用该编码。

下面是用 `Array.pack` 方法，把 IP 地址的 4 个数值转换为 4 个字节的字节串。
```ruby
str = [127, 0, 0, 1].pack("C4")
p str                #=> "\x7F\x00\x00\x01"
p str.encoding       # => #<Encoding:ASCII-8BIT>
```
`pack` 方法的参数为字节串化时使用的模式，C4 表示 4 个 8 位的不带符号的整数。执行结果为 4 个字节的字节串，编码为 ASCII-8BIT。

此外，在使用 `open-uri` 库等工具通过网络获取文件时，有时候并不知道字符编码是什么。这时候的编码也默认使用 ASCII-8BIT。
```ruby
# encoding: utf-8
require 'open-uri'
str = open("http://www.example.jp/").read
p str.encoding    #=> #<Encoding:ASCII-8BIT>
```

即使是编码为 ASCII-8BIT 的字符串，实际上也还是正常的字符串，只要知道字符编码，就可以使用 `force_encoding` 方法。这个方法并不会改变字符串的值（二进制数据），而只是改变编码信息。
```ruby
# encoding: utf-8
require 'open-uri'
str = open("http://www.example.jp/").read
str.force_encoding("Windows-31J")
p str.encoding    #=> #<Encoding:Windows-31J>
```
这样一来，我们就可以把 ASCII-8BIT 的字符串当作 Windows-31J 字符串来处理了。

使用 `force_encoding` 方法时，即使指定了不正确的编码，也不会马上产生错误，而是在对该字符串进行操作的时候才会产生错误。检查编码是否正确，可以用 `valid_encoding?` 方法，不正确时则返回 `false`。
```ruby
str = "こんにちは"
str.force_encoding("US-ASCII")    #=> 不会产生错误
str.valid_encoding?               #=> false
str + "みなさん"                  #=> Encoding::CompatibilityError
```

# 正则表达式与编码

与字符串同样，正则表达式也有编码信息。

正则表达式的编码即其匹配字符串的编码。例如，用 EUC-JP 的正则表达式对象去匹配 UTF-8 字符串时就会产生错误，反之亦然。
```ruby
# encoding: EUC-JP
a = "\u3042\u3044"
p /あ/ =~ a    #=> incompatible encoding regexp match
               #=> (EUC-JP regexp with UTF-8 string)
               #=> (Encoding::CompatibilityError)
```
通常情况下，正则表达式字面量的编码与代码的编码是一样的。指定其他编码的时候，可使用 `Regexp` 类的 `new` 方法。在这个方法中，表示模式第 1 个参数的字符串编码，就是该正则表达式的编码。
```ruby
str = "模式".encode("EUC-JP")
re = Regexp.new(str)
p re.encoding    # => #<Encoding:EUC-JP>
```

# IO 类与编码

使用 `IO` 类进行输入 / 输出操作时编码也非常重要。接下来，我们就向大家介绍一下 `IO` 与编码的相关内容。

**外部编码与内部编码**

每个 `IO` 对象都包含有外部编码与内部编码两种编码信息。外部编码指的是作为输入 / 输出对象的文件、控制台等的编码，内部编码指的是 Ruby 脚本中的编码。`IO` 对象的编码的相关方法如表所示。

方法名	                | 意义
- | -
IO#external_encoding	| 返回 IO 的外部编码
IO#internal_encoding	| 返回 IO 的内部编码
IO#set_encoding	        | 设定 IO 的编码

没有明确指定编码时，`IO` 对象的外部编码与内部编码各自使用其默认值 `Encoding.default_external`、`Encoding.default_internal`。默认情况下，外部编码会基于各个系统的本地信息设定，内部编码不设定。Windows 环境下的编码信息如下所示。
```ruby
p Encoding.default_external    #=> #<Encoding:Windows-31J>
p Encoding.default_internal    #=> nil
File.open("foo.txt") do |f|
  p f.external_encoding        #=> #<Encoding:Windows-31J>
  p f.internal_encoding        #=> nil
end
```

**编码的设定**

在刚才的例子中我们打开了文本文件（foo.txt），但 `IO` 对象（File 对象）的编码与文件的实际内容其实是没关系的。因为编码原本就只是用来说明如何处理字符的信息，因此对文本文件以外的文件并没有多大作用。

`IO.seek` 方法与 `IO.read（size）`方法，都不受编码影响，对任何数据都可以进行读写操作。`IO.read（size）`方法读取的字符串的编码为表示二进制数据的 ASCII-8BIT。

设定 `IO` 对象的编码信息，可以通过使用 `IO.set_encoding` 方法，或者在 `File.open` 方法的参数中指定编码来进行。

- `io.set_encoding(encoding)`

    `IO.set_encoding` 方法以 " 外部编码名 : 内部编码名 " 的形式指定字符串 `encoding`。把外部编码设置为 Shift_JIS，内部编码设置为 UTF-8 的时候，可以像下面那样设定。
    ```ruby
    $stdin.set_encoding("Shift_JIS:UTF-8")
    p $stdin.external_encoding    #=> #<Encoding:Shift_JIS>
    p $stdin.internal_encoding    #=> #<Encoding:UTF-8>
    ```

- `File.open(file, "mode:encoding")`

    为了在打开文件 file 时通过 `File.open` 方法指定编码 `encoding`，可以在第二个参数中指定 mode 的后面用冒号（:）分割，并按顺序指定外部编码以及内部编码（内部编码可省略）。
    ```ruby
    # 指定外部编码为UTF-8
    File.open("foo.txt", "w:UTF-8")
    　
    # 指定外部编码为Shift_JIS
    # 指定内部编码为UTF-8
    File.open("foo.txt", "r:Shift_JIS:UTF-8")
    ```

**编码的作用**

- 输出时编码的作用

    外部编码影响 `IO` 的写入（输出）。在输出的时候，会基于每个字符串的原有编码和 `IO` 对象的外部编码进行编码的转换（因此输出用的 `IO` 对象不需要指定内部编码）。

    如果没有设置外部编码，或者字符串的编码与外部编码一致，则不会进行编码的转换。在需要进行转换的时候，如果输出的字符串的编码不正确（比如实际上是日语字符串，但编码却是中文），或者是无法互相转换的编码组合（例如用于日语与中文的编码），这时程序就会抛出异常。

    ![image](../../../../assets/img/Develop/Ruby/模块/Encoding/1.jpg)

- 输入时编码的作用

    `IO` 的读取（输入）会稍微复杂一点。首先，如果外部编码没有设置，则会使用 `Encoding.default_external` 的值作为外部编码。

    设定了外部编码，但内部编码没设定的时候，则会将读取的字符串的编码设置为 `IO` 对象的外部编码。这种情况下并不会进行编码的转换，而是将文件、控制台输入的数据原封不动地保存为 `String` 对象。

    最后，外部编码和内部编码都设定的时候，则会执行由外部编码转换为内部编码的处理。输入与输出的情况一样，在编码转换的过程中如果数据格式或者编码组合不正确，程序都会抛出异常。

    大家或许会感觉有点复杂，其实只要使用的环境与实际使用的数据的编码一致，我们就不需要考虑编码的转换。另外一方面，如果执行环境与数据的编码不一致，那么我们就需要在程序里有意识地处理编码问题。

    ![image](../../../../assets/img/Develop/Ruby/模块/Encoding/2.jpg)

**UTF8-MAC 编码**

在 Mac OS X 中，文件名中如果使用了浊点或者半浊点字符，有时候就会产生一些奇怪的现象。

例如，创建文件 `ルビー.txt` 并执行下面的程序，可以发现，预计执行结果应该为 `found.`，但实际结果却是 `not found.`。
```ruby
# encoding: utf-8
Dir.glob("*.txt") do |filename|
  if filename == "ルビー.txt"
    puts "found."; exit
  end
end
puts "not found."
```

执行示例
```
> touch ルビー.txt
> ruby utf8mac.rb
not found.
```

另一方面，执行以下脚本，这次会输出 `found.`。
```ruby
# encoding: utf-8
Dir.glob("*.txt") do |filename|
  if filename.encode("UTF8-MAC") == "ルビー.txt".encode("UTF8-MAC")
    puts "found."; exit
  end
end
puts "not found."
```
执行示例
```
> touch ルビー.txt
> ruby utf8mac_fix.rb
found.
```

这是由于 Mac OS X 中的文件系统使用的编码不是 UTF-8，而是一种名为 UTF8-MAC（或者叫 UTF-8-MAC）的编码的缘故。

那么，UTF8-MAC 是什么样的编码呢。我们通过下面的例子来看一下。
```ruby
# encoding: utf-8
str = "ビ"
puts "size: #{str.size}"
p str.each_byte.map{|b| b.to_s(16)}
puts "size: #{str.encode("UTF8-MAC").size}"
p str.encode("UTF8-MAC").each_byte.map{|b| b.to_s(16)}
```
执行示例
```
> ruby utf8mac_str.rb
size: 1
["e3", "83", "93"]
size: 2
["e3", "83", "92", "e3", "82", "99"]
```

本例表示的是在 UTF-8 和 UTF8-MAC 这两种编码方式的情况下，分别以 16 进制的形式输出字符串 " ビ " 的长度以及各个字节的值。从结果中我们可以看出，UTF-8 时的值为“`ec,83,93`”，UTF8-MAC 时则是“`e3,83,92,e3,82,99`”。而转换为 UTF8-MAC 后，字符串的长度也变为了两个字符。

在 UTF8-MAC 中，字符ビ（Unicode 中为 U+30D3）会分解为字符匕（U+30D2）与浊点字符（U+3099）两个字符。用 UTF-8 表示则为 `8392E3` 与 `8299E3` 两个字节串，因此就得到了之前的结果。

像这样，如果把 Mac OS X 的文件系统当作是普通的 UTF-8 看待，往往就会有意料之外的事情发生。在操作日语文件、目录时务必注意这个问题 。
