# Ghidra

> 文章作者 [the-fog](https://github.com/the-fog)

<p align="center">
    <img src="../../../assets/img/logo/Ghidra.png" width="25%">
</p>

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 简介

Ghidra 是由美国国家安全局（NSA）研究部门开发的软件逆向工程（SRE）套件，用于支持网络安全任务。包括一套功能齐全的高端软件分析工具，使用户能够在各种平台(Windows、Mac OS和Linux)分析编译后的代码。功能包括反汇编，汇编，反编译，绘图和脚本，以及数百个其他功能。和 IDA 一样，Ghidra支持各种处理器指令集和可执行格式，用户还可以使用公开的API开发自己的Ghidra插件和脚本。不同的是，IDA是收费的，而Ghidra是免费开源的。

---

# 环境配置

Ghidra 的压缩包可以在[官网](https://ghidra-sre.org/)上下载到，截至目前最新版本为9.2，官方推荐使用的JDK版本为11+。配置好JAVA环境后，解压压缩包即可。如电脑上有多个JAVA环境，可以在 Ghidra 文件夹下的 support/launch.properties 文件中修改 JAVA_HOME_OVERRIDE 的值。

在Windows上运行 ghidraRun.bat，在 Linux/unix/macOS(OS X) 上运行 ghidraRun 启动。Ghidra 操作指南位于解压文件夹下的 docs/CheatSheet.html。

Ghidra 启动示意图：

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/1.png)

---

# 基础介绍

IDA 只要把要分析的文件拖进去即可，而 Ghidra 则不同，Ghidra 是基于项目(Project)设计的，个人感觉这一点应该是为了方便团队协作而设计的。要开始使用 Ghidra 需先创建一个项目，点击 File->New Project->Non-Shared Project->next->选择项目文件夹并填写项目名称->Finish。

如图，我创建了一个名为 test 的项目

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/2.png)

这个时候，就可以把要分析的文件拖进去了，也可以通过File->Import File->导入想要分析的文件，点击OK即可。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/3.png)

Ghidra 在加载完成后，会显示该文件的基础信息，如架构、大小、MD5值等

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/4.png)

然后就可以用Ghidra 自带的 CodeBrowser 打开目标文件了，在目标文件名上右击->Open with -> CodeBrowser

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/5.png)

一般第一次打开某个文件，Ghidra 都会提醒我们是否要分析，选择  yes，然后会出现分析选项，我们这里不做任何更改，直接 Analyze 即可

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/6.png)

然后，Ghidra 会花较长的时间分析，受你的CPU性能以及分析文件的大小影响。由于 Ghidra 是 JAVA 编写的，在效率上会低于 C/C++ 编写的 IDA。

接下来，我将依次对下方各个窗口进行简单的介绍。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/7.png)


## Listing

也就是中间那块最大的窗口，我们一般把这样的窗口叫做反汇编窗口，主要用来展示地址、opcode、汇编语句等。通过鼠标滚轮或者右边的滑动条来控制上下移动。

右侧的各种颜色的点标志各个段所在地址，比如CODE、DATA、idata等，点击即可跳转到相应的段

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/8.png)

将鼠标移动到函数名或者偏移地址上会显示出详细信息

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/9.png)

可以使用快捷键G，来跳转到想要去的地址

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/10.png)

## Program Tree

这个位于左上角的窗口，主要显示了程序头部以及各个段。我们可以在相应的文件夹上右击->Create Folder/Create Fragment，来创建文件夹或者分段。这个功能在用来分析大型项目的时候，效果比较显著。同样的，在文件夹上右击还能够进行排序(Sort)功能，提供了 by Address、by Name两种功能可供选择。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/11.png)

我们可以通过选中 Listing 窗口中的代码块拖动到该窗口中来创建分段。也可以在不想要的时候，将相应的分段或者文件夹删除。需要注意的是，只有当删除的分段/文件夹包含于其他分段/文件夹中或者删除的分段/文件夹为空时，才能成功删除。

## Symbol Tree

符号树窗口位于左侧的中间位置，主要显示导入表(Imports)、导出表(Exports)、函数(Function)、标签(Labels)、类(Classes)以及命名空间(Namespaces)。

可以在 Imports 文件夹上右击->Create Library 来创建库。在想要的关联的Imports文件夹中的库上右键->Set External Program->选择想关联的外部程序来设置相应的外部关联程序。在一个父类/命名空间上右击->Create Class/Namespaces，可以创建类/命名空间。所有在Namespace 中的命名空间，都在全局命名空间中。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/12.png)


## Data Type Manager

数据类型管理器窗口位于左下角，用来展示各种数据类型。可以让用户定位、组织数据类型，也能够将数据类型应用于程序。Ghidra的一个长期目标，就是让用户能够搭建数据类型的库，并在不同的程序、项目甚至用户之间分享使用。

Ghidra 支持三类数据类型: Built-in、user defined、derived

|类型|描述|
|:----|:----|
|Built-in|直接由Java实现并被用于基本的标准类型，比如byte、word、string等等，不能被改变或重命名|
|user defined|有四个用户定义(user defined)的数据类型，分别是Structures、Unions、Enums和Typedefs，可以被创建、修改及重命名|
|derived|两种派生的数据类型: Pointers(指针)和Arrays(数组)，可以被创建与删除，但是名字由其基本类型决定|

以当前这个测试项目为例，Ghidra 在分析完后，会自动生成 BuiltInTypes列表，同时还会根据程序的架构等生成相应的数据类型列表。比如这里是 windows_vs12_32

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/13.png)

## Decompile

反编译窗口，位于右侧。在Listing窗口中浏览到函数时，反编译窗口会显示将其反编译成C/C++语言后的结果，功能上类似于IDA的F5。

可以通过右上角的导出按钮，把相应的函数导出成C文件。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/14.png)

## Console

控制台窗口，位于最下方，用来显示各种脚本的输出等。脚本管理器位于 Window->Script Manager ，里面有很多 Ghidra  自带的脚本。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/15.png)

其中大多数为 .java 的脚本，还有部分为 .py 的脚本。选择一个脚本，点击运行，Ghidra  便会加载该脚本，并将输出显示在控制台窗口中(如果有的话)。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/16.png)

下面结合一个具体实例，来演示下 Ghidra 的使用。

# CTF实例

我这里选择的是[BugKuCTF平台](https://ctf.bugku.com/challenges)的逆向题的[RE_Cirno](https://ctf.bugku.com/files/3c8bece7183bf76637d12d214d0809ec/RE_Cirno.jpg)题目。这个题目的附件是个 .jpg文件，使用010打开该文件，会发现下方有个未知填充块。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/17.png)

熟悉文件头的人都知道，PK..是压缩包的文件头，如果不熟悉的话，也可以用 binwalk 分离出来。

```plain
binwalk -Me RE_Cirno.jpg
```
解压，得到 re.exe。在命令行中运行re.exe,得到如下提示。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/18.png)

把 re.exe 拖到 Ghidra  中打开，进行分析。由于有按任意键继续，猜测使用了system("pause")函数。在上方的Search->For Strings->中查找pause

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/19.png)

通过点击右边的交叉引用，找到关键函数

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/20.png)

Windows->Function Graph 可以看到该函数地图形化显示

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/21.png)

在右侧的反编译窗口，将关键的代码段拷贝下来

```plain
  uint local_70;
  uint local_6c;
  int local_68;
  int local_64 [24]; 
  local_64[0] = 0x73;
  local_64[1] = 0x5e;
  local_64[2] = 0x61;
  local_64[3] = 0x72;
  local_64[4] = 0x67;
  local_64[5] = 0x2f;
  local_64[6] = 0x6b;
  local_64[7] = 0x72;
  local_64[8] = 0x41;
  local_64[9] = 0x30;
  local_64[10] = 0x31;
  local_64[11] = 0x69;
  local_64[12] = 0x75;
  local_64[13] = 0x76;
  local_64[14] = 0x65;
  local_64[15] = 0x30;
  local_64[16] = 0x71;
  local_64[17] = 0x5f;
  local_64[18] = 99;
  local_64[19] = 0x2f;
  local_64[20] = 0x5c;
  local_64[21] = 0x74;
  local_64[22] = 0x5d;
  local_64[23] = 0x66;
  local_68 = 0;
  while (local_68 < 0x18) {
    local_70 = local_64[local_68] + 9U ^ 9;
    local_68 = local_68 + 1;
    local_6c = local_70;
  }
```

只需简单修改下，即可编译运行。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/22.png)

得到字符串

```plain
uncry1}rC03{wvg0sae1ltof
```
根据上面的提示反方向围住，将该字符串颠倒下
```plain
fotl1eas0gvw{30Cr}1yrcnu
```

然后解栅栏密码，得到flag

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/23.png)

之所以拿这道题目举例，是因为同样的程序在ida 7.0的 反编译如下：

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/24.png)

可以注意到是没有异或符号的，而在反汇编中，我们可以清楚地看到存在异或操作。暂不清楚，新版本IDA是否修复该bug。

![](https://gitee.com/asdasdasd123123/pic/raw/master/img/42/25.png)
