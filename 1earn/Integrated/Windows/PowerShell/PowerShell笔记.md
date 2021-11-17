# PowerShell 笔记

---

**什么是 PowerShell**

Windows PowerShell 是一种命令行外壳程序和脚本环境,使命令行用户和脚本编写者可以利用 .NET Framework 的强大功能.

Windows PowerShell 需要用于管理 .NET 对象的语言.该语言需要为使用 cmdlet 提供一致的环境.该语言需要支持复杂的任务,而不会使简单的任务变得更复杂. 该语言需要与在 .NET 编程中使用的高级语言(如C#)一致.

---

**学习资源**
- [specterops/at-ps](https://github.com/specterops/at-ps)

---

**常见报错**
- **无法加载文件 `******.ps1`,因为在此系统中禁止执行脚本.有关详细信息,请参阅 "get-help about_signing"**
    ```powershell
    set-ExecutionPolicy RemoteSigned
    ```

- **使用 powershell 运行脚本报错:进行数字签名.无法在当前系统上运行该脚本.有关运行脚本和设置执行策略的详细信息**
    ```powershell
    powershell "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -force |Out-null"
    ```

---

# 安装Powershell

https://docs.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows

## 支持的 Windows 版本

* ✅ 指示仍支持 OS 或 PowerShell 版本
* ❌ 指示不支持 OS 或 PowerShell 版本
* 💢 指示该 OS 版本不再支持 PowerShell 版本

| Windows版本	                         | 7.0 (LTS)  | 7.1（最新版）	| 7.2 (LTS-preview) |
| - | - | - | - |
| Windows Server 2016,2019,2022         | ✅         | ✅            | ✅ |
| Windows Server 2012 R2                | ✅         | ✅            | ✅ |
| Windows Server Core(2012 R2)          | ✅         | ✅            | ✅ |
| Windows Server Nano(1809)             | ✅         | ✅            | ✅ |
| Windows Server 2012                   | 💢         | ❌            | ❌ |
| Windows Server 2008 R2                | 💢         | ❌            | ❌ |
| Windows 11                            | ✅         | ✅            | ✅ |
| Windows 10 1607                       | ✅         | ✅            | ✅ |
| Windows 8.1	                        | ✅         | ✅            | ❌ |

以下处理器体系结构在 Windows 上支持 PowerShell。

| Windows版本	    | 7.0 (LTS)	    | 7.1（最新版）	    | 7.2 (LTS-preview) |
| - | - | - | - |
| Nano Server 1803	            | x64、Arm32	| X64	            | X64 |
| Windows Server 2012 R2        | x64、x86	    | x64、x86	        | x64、x86 |
| Windows Server Core 2012 R2	| x64、x86	    | x64、x86	        | x64、x86 |
| Windows 10 or 11              | x64、x86	    | x64、x86、Arm64	| x64、x86、Arm64 |
| Windows 8.1                   | x64、x86	    | x64、x86	        | x64、x86 |

---

# 使用

**PS1文件**

一个 PowerShell 脚本其实就是一个简单的文本文件， 这个文件包含了一系列 PowerShell 命令，每个命令显示为独立的一行，对于被视为 PowerShell 脚本的文本文件，它的文件名需要加上 .PS1 的扩展名。

**PowerShell的执行策略**

为防止恶意脚本的执行，PowerShell有一个执行策略，默认情况下，这个执行策略被设置为受限。

我们可以使用：Get-ExecutionPolicy 命令查看PowerShell当前的执行策略。它有4个策略。
* Restricted：脚本不能运行(默认设置)
* RemoteSigned：本地创建的脚本可以运行，但是从网上下载的脚本不能运行(拥有数字证书签名的除外)
* AllSigned：仅当脚本由受信任的发布者签名时才能运行；
* Unrestricted：允许所有的脚本执行

```
Set-ExecutionPolicy 策略名(如：Unrestricted)
```

---

# 常用命令

> 本部分内容由 [xidaner](https://github.com/xidaner) 提供,在此只做排版修改

## 基础入门

像文件系统那样操作 Windows Registry
```powershell
cd e:
```

在文件里递回地搜索某个字符串
```powershell
dir -r | select string "searchforthis"
```
　　
使用内存找到X个进程
```powershell
ps | sort -p ws | select -last x
```

循环(停止,然后重启)一个服务,如 DHCP
```powershell
Restart-Service DHCP
```

在文件夹里列出所有条目
```powershell
Get-ChildItem - Force
```

递归一系列的目录或文件夹
```powershell
Get-ChildItem -Force c:\directory -Recurse
```

在目录里移除所有文件而不需要单个移除
```powershell
Remove-Item C:\tobedeleted -Recurse
```

重启当前计算机
```powershell
(Get-WmiObject -Class Win32_OperatingSystem -ComputerName .).Win32Shutdown(2)
```

---

## 收集信息

查看当前Powershell版本
```powershell
$PSVersionTable
```

获取计算机组成或模型信息
```powershell
Get-WmiObject -Class Win32_ComputerSystem
```

获取当前计算机的 BIOS 信息
```powershell
Get-WmiObject -Class Win32_BIOS -ComputerName .
```

检查设备驱动程序版本
```powershell
Get-WmiObject Win32_PnPSignedDriver| select DeviceName, Manufacturer, DriverVersion
```

列出所安装的修复程序(如QFE或Windows Update文件)
```powershell
Get-WmiObject -Class Win32_QuickFixEngineering -ComputerName .
```

获取当前登录计算机的用户的用户名
```powershell
Get-WmiObject -Class Win32_ComputerSystem -Property UserName -ComputerName .
```

获取当前计算机所安装的应用的名字
```powershell
Get-WmiObject -Class Win32_Product -ComputerName . | Format-Wide -Column 1
```

获取分配给当前计算机的 IP 地址
```powershell
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName . | Format-Table -Property IPAddress
```

获取当前机器详细的 IP 配置报道
```powershell
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName . | Select-Object -Property [a-z]* -ExcludeProperty IPX*,WINS*
```

找到当前计算机上使用 DHCP 启用的网络卡
```powershell
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter "DHCPEnabled=true" -ComputerName .
```

在当前计算机上的所有网络适配器上启用 DHCP
```powershell
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=true -ComputerName . | ForEach-Object -Process {$_.EnableDHCP()}
```

---

## 软件管理

在远程计算机上安装 MSI 包
```powershell
(Get-WMIObject -ComputerName TARGETMACHINE -List | Where-Object -FilterScript {$_.Name -eq "Win32_Product"}).Install(\\MACHINEWHEREMSIRESIDES\path\package.msi)
```

使用基于 MSI 的应用升级包升级所安装的应用
```powershell
(Get-WmiObject -Class Win32_Product -ComputerName . -Filter "Name='name_of_app_to_be_upgraded'").Upgrade(\\MACHINEWHEREMSIRESIDES\path\upgrade_package.msi)
```

从当前计算机移除 MSI 包
```powershell
(Get-WmiObject -Class Win32_Product -Filter "Name='product_to_remove'" -ComputerName . ).Uninstall()
```

---

## 机器管理

一分钟后远程关闭另一台机器
```powershell
Start-Sleep 60; Restart-Computer -Force -ComputerName TARGETMACHINE
```

添加打印机
```powershell
(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection(\\printerserver\hplaser3)
```

移除打印机
```powershell
(New-Object -ComObject WScript.Network).RemovePrinterConnection("\\printerserver\hplaser3 ")
```

进入 PowerShell 会话
```powershell
invoke-command -computername machine1, machine2 -filepath c:\Script\script.ps1
```

---

## 远程桌面

`以下操作,PS 命令窗口,必须都以管理员身份执行.`

1. 机器 A 和 B,分别开启 PowerShell 远程管理服务

    A = 192.168.3.32
    ```
    PS >> Enable-PSRemoting
    ```
    然后按照提示,选项选 Y,执行开启远程管理.

    B = 192.168.3.37
    ```
    PS >> Enable-PSRemoting
    ```
    然后按照提示,选项选 Y,执行开启远程管理.

2. 机器 A 和 B,分别信任需要远程管理的机器 IP 或名称

    A=192.168.3.32
    ```
    PS >> Set-Item WSMan:\localhost\Client\TrustedHosts -Value IP 地址
    ```
    然后按照提示,选项选 Y,表示允许远程发送命令

    B = 192.168.3.37
    PS >>
    ```
    Set-Item WSMan:\localhost\Client\TrustedHosts -Value IP 地址
    ```
    然后按照提示,选项选 Y,表示允许远程发送命令

3. 在机器 A 上面,远程登录和执行命令到机器 B

    A = 192.168.3.32
    ```
    PS >> Enter-PSSession -ComputerName IP地址
    ```
