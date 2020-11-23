# Proc 类

---

- https://www.kancloud.cn/imxieke/ruby-base/107309

---

# Proc 类是什么

所谓 `Proc`，就是使块对象化的类。`Proc` 与块的关系非常密切,下面，我们来看看如何创建与执行 `Proc` 对象。

- `Proc.new(...)`
- `proc{...}`

    创建 `Proc` 对象的典型方法是通过 `Proc.new` 方法，或者对 `proc` 方法指定块。
    ```ruby
    hello1 = Proc.new do |name|
    puts "Hello, #{name}."
    end
    　
    hello2 = proc do |name|
    puts "Hello, #{name}."
    end
    　
    hello1.call("World")    #=> Hello, World.
    hello2.call("Ruby")     #=> Hello, Ruby.
    ```
    利用 `Proc.new` 方法，或者对 `proc` 方法指定块，都可以创建代表块的 `Proc` 对象。

    通过调用 `Proc.call` 方法执行块。调用 `Proc.call` 方法时的参数会作为块变量，块中最后一个表达式的值则为 `Proc.call` 的返回值。`Proc.call` 还有一个名称叫 `Proc#[]`。
    ```ruby
    # 判断西历的年是否为闰年的处理
    leap = Proc.new do |year|
    year % 4 == 0 && year % 100 != 0 || year % 400 ==0
    end

    p leap.call(2000)    #=> true
    p leap[2013]         #=> false
    p leap[2016]         #=> true
    ```
    将块变量设置为 |* 数组 | 的形式后，就可以像方法参数一样，以数组的形式接收可变数量的参数。
    ```ruby
    double = Proc.new do |*args|
    args.map{|i| i * 2 }    # 所有元素乘两倍
    end
    　
    p double.call(1, 2, 3)    #=> [2, 3, 4]
    p double[2, 3, 4]         #=> [4, 6, 8]
    ```
    除此以外，定义普通方法时可使用的参数形式，如默认参数、关键字参数等，几乎都可以被用于块变量的定义，并被指定给 `Proc.call` 方法。

**lambda**

`Proc.new`、`proc` 等有另外一种写法叫 `lambda`。与 `Proc.new`、`proc` 一样，`lambda` 也可以创建 `Proc` 对象，但通过 `lambda` 创建的 `Proc` 的行为会更接近方法。

第一个不同点是，`lambda` 的参数数量的检查更加严密。对用 `Proc.new` 创建的 `Proc` 对象调用 `call` 方法时，`call` 方法的参数数量与块变量的数量可以不同。但通过 `lambda` 创建 `Proc` 对象时，如果参数数量不正确，程序就会产生错误。
```ruby
prc1 = Proc.new do |a, b, c|
  p [a, b, c]
end
prc1.call(1, 2)    #=> [1, 2, nil]

prc2 = lambda do |a, b, c|
  p [a, b, c]
end
prc2.call(1, 2)    #=> 错误（ArgumentError）
```

第二个不同点是，`lambda` 可以使用 `return` 将值从块中返回。下面的代码中 `power_of` 方法会利用参数 `n` 返回“计算 x 的 n 次幂的 Proc 对象”。请注意，返回值并不是数值，而是进行运算的 `Proc` 对象。调用 `power_of(3)` 后，结果就会得到 call 方法参数值的 3 次幂的 `Proc` 对象。从 `lambda` 中返回值时使用了 `return`，这里的 `return` 会将 `lambda` 中的值返回。
```
def power_of(n)
  lambda do |x|
    return x ** n
  end
end

cube = power_of(3)
p cube.call(5)  #=> 125
```

接下来，我们尝试用 `Proc.new` 方法改写代码。使用 `Proc.new` 方法时，在块中使用 `return` 后，程序就会跳过当前执行块，直接从创建这个块的方法返回。在本例中，即虽然块内的 `return` 应该从 `power_of` 方法返回，但由于程序运行时 `power_of` 方法的上下文会消失，因此程序就会出现错误。
```ruby
def power_of(n)
  Proc.new do |x|
    return x ** n
  end
end

cube = power_of(3)
p cube.call(5)  #=> 错误（LocalJumpError）
```
不是 `lambda` 的普通块中的 `return`，会从正在执行循环的方法返回。下面代码中的 `prefix` 方法会比较参数 `ary` 中的元素是否与 `obj` 相等，相等就返回在此之前的所有元素，不相等则返回空数组。第 6 行中的 `return` 并不会从块返回，而是跳过块，并作为 `prefix` 方法整体的返回值返回。
```ruby
def prefix(ary, obj)
  result = []               # 初始化结果数组
  ary.each do |item|        # 逐个检查元素
    result << item          # 将元素追加到结果数组中
    if item == obj          # 如果元素与条件一致
      return result         # 返回结果数组
    end
  end
  return result             # 所有元素检查完毕的时候
end

prefix([1, 2, 3, 4, 5], 3)  #=> [1, 2, 3]
```

`break` 被用于控制迭代器的行为。这个命令会向接收块的方法的调用者返回结果值。如下所示，`break []` 会马上终止 `Array.collect` 方法，并将空数组作为 `collent` 方法的整体的返回值返回。
```ruby
[:a, :b, :c].collect do |item|
  break []
end
```

> 用 `Proc.new` 方法或者 `proc` 方法创建的 `Proc` 对象的情况下，由于这些方法都接收块，在调用 `Proc.call` 方法的时候并没有适当的返回对象，因此就会发生错误。而 `lambda` 的情况下则与 `return` 一样，将值返回给 `Proc.call` 方法。另一方面，由于 `next` 方法的作用在于中断 1 次块的执行，因此无论如何创建 `Proc` 对象，都可以将值返回给 `call` 方法。

`lambda` 有另外一种写法——“`->( 块变量 ){ 处理 }`”。块变量在 `{ ～ }` 之前，看上去有点像函数。使用 `->` 的时候，我们一般会使用 `{ ～ }` 而不是 `do ～ end`。
```ruby
square = ->(n){ return n ** 2}
p square[5]    #=> 25
```

**通过 Proc 参数接收块**

在调用带块的方法时，通过 `Proc` 参数的形式指定块后，该块就会作为 `Proc` 对象被方法接收。下面代码在 `total2` 方法中，调用 `total2` 方法时指定的块，可以作为 `Proc` 对象从变量 `block` 中获取。
```ruby
def total2(from, to, &block)
  result = 0               # 合计值
  from.upto(to) do |num|   # 处理从 from 到 to 的值
    if block               #   如果有块的话
      result +=            #     累加经过块处理的值
   block.call(num)
    else                   #   如果没有块的话
      result += num        #     直接累加
    end
  end
  return result            # 返回方法的结果
end

p total2(1, 10)                   # 从 1 到 10 的和 => 55
p total2(1, 10){|num| num ** 2 }  # 从 1 到 10 的 2 次冥的和 => 385
```

**to_proc 方法**

有些对象有 `to_proc` 方法。在方法中指定块时，如果以 & 对象的形式传递参数，对象 `.to_proc` 就会被自动调用，进而生成 `Proc` 对象。

其中，`Symbol.to_proc` 方法是比较典型的，并且经常被用到。例如，对符号 `:to_i` 使用 `Symbol.to_proc` 方法，就会生成下面那样的 `Proc` 对象。
```ruby
Proc.new{|arg| arg.to_i }
```
这个对象在什么时候使用呢？例如，把数组的所有元素转换为数值类型时，一般的做法如下：

执行示例
```ruby
>> %w(42 39 56).map{|i| i.to_i }
=> [42, 39, 56]
```

上述代码还可以像下面这样写：

执行示例
```ruby
>> %w(42 39 56).map(&:to_i)
=> [42, 39, 56]
```
按照类名排序的程序，也可以写成：

执行示例
```ruby
>> [Integer, String, Array, Hash, File, IO].sort_by(&:name)
=> [Array, File, Hash, IO, Integer, String]
```
熟悉这样的写法可能需要一定的时间，但这种写法不仅干净利索，而且意图明确。

# Proc 的特征

虽然 `Proc` 对象可以作为匿名函数或方法使用，但它并不只是单纯的对象化。
```ruby
def counter
  c = 0         # 初始化计数器
  Proc.new do   # 每调用 1 次 call 方法，计数器加1
    c += 1      # 返回加 1 后的 Proc 对象
  end
end

# 创建计数器 c1 并计数
c1 = counter
p c1.call       #=> 1
p c1.call       #=> 2
p c1.call       #=> 3

# 创建计数器 c2 并计数
c2 = counter    # 创建计数器c2
p c2.call       #=> 1
p c2.call       #=> 2

# 再次用 c1 计数
p c1.call       #=> 4
```

第 1 行到第 6 行为 `counter` 方法的定义。该方法首先把作为计数器的本地变量 `c` 初始化为 0。然后每调用 1 次 `Proc.call` 方法，就将计数器加 1，并返回该 `Proc` 对象。在第 9 行中，调用 `counter` 方法，将 `Proc` 对象赋值给 `c1`。可以看到，`c1` 调用 `call` 方法后，`proc` 对象引用的本地变量 `c` 开始计数了。在第 15 行中，以同样的方法创建新的计数器，之后计数器被重置。在最后的第 20 行中，再次调用最初创建的 `c1` 的 `call` 方法，计数器开始接着之前的结果计数。

通过这个例子我们可以看出，变量 `c1` 与变量 `c2` 引用的 `Proc` 对象，是分别保存、处理调用 `counter` 方法时初始化的本地变量的。与此同时，`Proc` 对象也会将处理内容、本地变量的作用域等定义块时的状态一起保存。

像 `Proc` 对象这样，将处理内容、变量等环境同时进行保存的对象，在编程语言中称为闭包（closure）。使用闭包后，程序就可以将处理内容和数据作为对象来操作。这和在类中描述处理本身、在实例中保存数据本质上是一样的，只是从写程序的角度来看，使用类的话当然也就意味着可以使用更多的功能。

就像刚才的计数器的例子那样，`Proc` 对象可被用来对少量代码实现的功能做对象化处理。另外，由于 Ruby 中大量使用了块，因此在有一定规模的程序开发中，我们就难免会使用到 `Proc` 对象。特别是像调用和传递带块的方法时的方法、通过闭包保存数据等功能，我们都需要透彻理解才行。

# Proc 类的实例方法

- `prc.call(args, ...)`
- `prc[args, ...]`
- `prc.yield(args, ...)`
- `prc.(args, ...)`
- `prc === arg`

    上述方法都执行 `Proc` 对象 prc。
    ```ruby
    prc = Proc.new{|a, b| a + b}
    p prc.call(1, 2)    #=> 3
    p prc[3, 4]         #=> 7
    p prc.yield(5, 6)   #=> 11
    p prc.(7, 8)        #=> 15
    p prc === [9, 10]   #=> 19
    ```

    由于受到语法的限制，通过 `===` 指定的参数只能为 1 个。大家一定要牢记这个方法会在 `Proc` 对象作为 `case` 语句的条件时使用。因此，在创建这样的 `Proc` 对象时，比较恰当的做法是，只接收一个参数，并返回 `true` 或者 `false`。

    下面的例子实现的是，从 1 到 100 的整数中，当值为 3 的倍数时输出 `Fizz`，5 的倍数时输出 `Buzz`，15 的倍数时输出 `Fizz Buzz`，除此以外的情况下则输出该值本身。
    ```ruby
    fizz = proc{|n| n % 3 == 0 }
    buzz = proc{|n| n % 5 == 0 }
    fizzbuzz = proc{|n| n % 3 == 0 && n % 5 == 0}
    (1..100).each do |i|
    case i
    when fizzbuzz then puts "Fizz Buzz"
    when fizz then puts "Fizz"
    when buzz then puts "Buzz"
    else puts i
    end
    end
    ```

- `prc.arity`

    返回作为 `call` 方法的参数的块变量的个数。以 `|*args|` 的形式指定块变量时，返回 -1。
    ```ruby
    prc0 = Proc.new{ nil }
    prc1 = Proc.new{|a| a }
    prc2 = Proc.new{|a, b| a + b }
    prc3 = Proc.new{|a, b, c| a + b +c }
    prcn = Proc.new{|*args| args }
    　
    p prc0.arity    #=> 0
    p prc1.arity    #=> 1
    p prc2.arity    #=> 2
    p prc3.arity    #=> 3
    p prcn.arity    #=> -1
    ```

- `prc.parameters`

    返回关于块变量的详细信息。返回值为 [ 种类 , 变量名 ] 形式的数组的列表。

    符号	    | 意义
    - | -
    `:opt`	    | 可省略的变量
    `:req`	    | 必需的变量
    `:rest`	    | 以 *args 形式表示的变量
    `:key`	    | 关键字参数形式的变量
    `:keyrest`	| 以 **args 形式表示的变量
    `:block`	    | 块

    ```ruby
    prc0 = proc{ nil }
    prc1 = proc{|a| a }
    prc2 = lambda{|a, b| [a, b] }
    prc3 = lambda{|a, b=1, *c| [a, b, c] }
    prc4 = lambda{|a, &block| [a, block] }
    prc5 = lambda{|a: 1, **b| [a, b] }
    　
    p prc0.parameters    #=> []
    p prc1.parameters    #=> [[:opt, :a]]
    p prc2.parameters    #=> [[:req, :a], [:req, :b]]
    p prc3.parameters    #=> [[:req, :a], [:opt, :b], [:rest, :c]]
    p prc4.parameters    #=> [[:req, :a], [:block, :block]]
    p prc5.parameters    #=> [[:key, :a], [:keyrest, :b]]
    ```

- `prc.lambda?`

    判断 prc 是否为通过 `lambda` 定义的方法。
    ```ruby
    prc1 = Proc.new{|a, b| a + b}
    p prc1.lambda?  #=> false
    　
    prc2 = lambda{|a, b| a + b}
    p prc2.lambda?  #=> true
    ```

- `prc.source_location`

    返回定义 prc 的程序代码的位置。返回值为 [ 代码文件名 , 行编号 ] 形式的数组。prc 由扩展库等生成，当 Ruby 脚本不存在时返回 `nil`。
    ```
    prc0 = Proc.new{ nil }
    prc1 = Proc.new{|a| a }

    p prc0.source_location
    p prc1.source_location
    ```
    执行示例
    ```
    > ruby proc_source_location.rb
    ["proc_source_location.rb", 1]
    ["proc_source_location.rb", 2]
    ```
