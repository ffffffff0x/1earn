# PDB符号文件

---

**什么是 PDB 文件**

- PDB（Program Data Base），意即程序的基本数据，是 VS 编译链接时生成的文件。DPB 文件主要存储了 VS 调试程序时所需要的基本信息，主要包括源文件名、变量名、函数名、FPO(帧指针)、对应的行号等等。因为存储的是调试信息，所以一般情况下 PDB 文件是在 Debug 模式下才会生成。
- PDB 文件是在我们编译工程的时候产生的，它是和对应的模块 (exe 或 dll) 一起生成出来的。pdb 文件包含了编译后程序指向源代码的位置信息，用于调试的时候定位到源代码，主要是用来方便调试的。

PDB 文件中记录了源文件路径的相关信息，所以在载入 PDB 文件的时候，就可以将相关调试信息与源码对应。这样可以可视化的实时查看调试时的函数调用、变量值等相关信息。模块当中记录的 PDB 文件是绝对路径。所以只要模块在当前电脑上载入，调试器自然地会根据模块当中的路径信息找到相应 PDB 文件并载入。同样 PDB 文件中记录的源文件路径也是绝对路径，所以 PDB 文件只要在当前电脑上载入，调试进入相应模块时，都能够匹配到记录的源文件，然后可视化地查看相应信息。

**PDB 文件的调用过程**

模块 (Module)，EXE 和 DLL 都可以称之为模块，因为它们都有自已独立的 Stack，所以我们在调试程序时，可以在 Call Stack 窗口查看到所有调用的 Module Name。并且可以右键查看相应模块的 ybmol Load Information，即该模块调用的 PDB 文件路径的过程。

每个模块被载入的时候，其相同名字的 PDB 文件同时被载入。所以 Debug 模式下，不仅因为代码没有优化，同时因为要载入 PDB 文件，所以 Debug 模式下的程序执行速度非常慢。

每个模块只会生成一个相同名字的 PDB 文件，并且模块生成的同时，会校验 PDB 文件生成 GUID 记录在模块内。这是因为调试时，调试器强制要求每个模块必须和 PDB 文件保持一致。实验过程中，用之前生成的 PDB 文件替换当前生成的 PDB 文件时，Debug 窗口会显示 No symbols loaded. MSDN 也做了相应的说明：The debugger will load only a PDB for a binary that exactly matches the PDB that was created when the binary was built.

**PDB 文件存储格式**

PDB 的文件格式类似于磁盘的文件系统，每个磁盘会被划分成很多个大小一样的扇区，文件中的数据就存放在不同的扇区中，而且无需保证这些扇区在磁盘上是连续的。PDB 文件用 page 进行划分，类似于扇区，stream 就类似于文件，stream directory 类似于文件目录。

**PDB 文件的内容**

PDB 不是公开的文件格式，但是 Microsoft 提供了 API 来帮助从 PDB 中获取数据。

Native C++ PDB 包含了如下的信息：
* public，private 和 static 函数地址；
* 全局变量的名字和地址；
* 参数和局部变量的名字和在堆栈的偏移量；
* class，structure 和数据的类型定义；
* Frame Pointer Omission 数据，用来在 x86 上的 native 堆栈的遍历；
* 源代码文件的名字和行数；

.NET PDB 只包含了 2 部分信息:
* 源代码文件名字和行数；
* 和局部变量的名字；
* 所有的其他的数据都已经包含在了. NET Metadata 中了；

**PDB 文件的查找策略**

1. 文件被执行或者被载入的地址
2. 就是硬编码在 PE 文件头中的那个地址。
3. 如果配置了符号服务器，第二步以后应该先去符号服务器的缓存目录下找，如果找不到再去符号服务器上去找。找到的话就会下载到缓存目录。
4. VS 中设置的一些符号查询的目录
5. c:\Windows 文件夹。

**PDB 如何工作**

当你加载一个模块到进程的地址空间的时候，debugger 用 2 种信息来找到相应的 PDB 文件。
- 一种是文件的名字，如果加载 zzz.dll,debugger 则查找 zzz.pdb 文件。
- 在文件名字相同的情况下 debugger 还通过嵌入到 PDB 和 binay 的 GUID 来确保 PDB 和 binay 的真正的匹配。所以即使没有任何的代码修改，昨天的 binay 和今天的 PDB 是不能匹配的。可以使用 dempbin.exe 来查看 binary 的 GUID。

在 VisualStudio 中的 modules 窗口的 symbol file 列可以查看 PDB 的 load 顺序。第一个搜索的路径是 binary 所在的路径，如果不在 binary 所在的路径，则查找 binary 中 hardcode 记录的 build 目录，例如 obj\debug\*.pdb, 如果以上两个路径都没有找到 PDB，则根据 symbol server 的设置，在本地的 symbol server 的 cache 中查找，如果在本地的 symbol server 的 cache 中没有对应的 PDB，则最后才到远程的 symbol server 中查找。通过上面的查找顺序我们可以看出为什么 PDB 查找不会冲突。

对于有时我们需要在别人的机器上 debug 的情况，需要将相应的 PDB 与 binary 一起拷贝，对于加入 GAC 的. NET 的 binary，需要将 PDB 文件拷贝到 C:\Windows\assembly\GAC_MSIL\Example\1.0.0.0__682bc775ff82796a 类似的 binary 所在的目录。另一个变通的方法是定义环境变量 DEVPATH，从而代替使用命令 GACUTIL 将 binary 放入 GAC 中。在定义 DEVPATH 后，只需要将 binary 和 PDB 放到 DEVPATH 的路径，在 DEVPATH 下的 binary 相当于在 GAC 下。使用 DEVPATH，首先需要创建目录且对当前 build 用户有写权限，然后创建环境变量 DEVPATH 且值为刚才创建的目录，然后在 web.config，app.config 或 machine.config 中开启 development 模式，启动对 DEVPATH 的使用
```
<configuration>
   <runtime>
      <developmentMode developerInstallation="true"/>
   </runtime>
</configuration>
```

在你打开了 development 模式后，如果 DEVPATH 没有定义或路径不存在的话会导致程序启动时异常 "Invalid value for registry"。而且如果在 machine.config 中开启 DEVPATH 的使用会影响其他的所有的程序，所以要慎重使用 machine.config。

最后开发人员需要知道的是源代码信息是如何存储在 PDB 文件中的。
- 对于开发人员自己机器上生成的 build，在运行 source indexing tool 后，版本控制工具将代码存储到你设置的代码 cache 中。
- 对于在公用的 build 机器上生成的 build，只是存储了 PDB 文件的全路径，例如在 c:\foo 下的源文件 mycode.cpp，在 pdb 文件中存储的路径为 c:\foo\mycode.cpp。使用虚拟盘来增加 PDB 对绝对路径的依赖，例如可以使用 subst.exe 将源代码路径挂载为 V:，在别人的机器上 debug 的时候也挂载 V：。

**如何查看二进制文件和 PDB 的 GUID**

- 使用 VS 自带的 DUMPBIN 工具可以查看二进制文件所期望的 PDB 的 GUID。基本用法就是 DUMPBIN /HEADER 文件,详情可参考 https://docs.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-160
- https://www.codeproject.com/Articles/37456/How-To-Inspect-the-Content-of-a-Program-Database-P

---

**Source & Reference**
- [Specify symbol (.pdb) and source files in the Visual Studio debugger (C#, C++, Visual Basic, F#)](https://docs.microsoft.com/en-us/visualstudio/debugger/specify-symbol-dot-pdb-and-source-files-in-the-visual-studio-debugger?view=vs-2019)
- [PDB Symbol Files](https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/pdb-symbol-files)
- [PDB文件：每个开发人员都必须知道的](https://www.cnblogs.com/itech/archive/2011/08/15/2136522.html)
- [PDB文件详解](https://blog.csdn.net/feihe0755/article/details/54233714)
- [什么是PDB文件？](https://cloud.tencent.com/developer/ask/30007)
