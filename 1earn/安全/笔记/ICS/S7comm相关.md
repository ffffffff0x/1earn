# S7comm 相关

---

## 免责声明

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 错误类型

## 头结构的错误类型

S7comm 头结构中常见的错误类型，如下表：
| Hex  | Value                       | 描述           |
| ---- | --------------------------- | -------------- |
| 0x00 | No error                    | 没有错误       |
| 0x81 | Application relationship    | 应用关系       |
| 0x82 | Object definition           | 对象定义       |
| 0x83 | No resources available      | 没有可用资源   |
| 0x84 | Error on service processing | 服务处理中错误 |
| 0x85 | Error on supplies           | 请求错误       |
| 0x87 | Access error                | 访问错误       |

## 参数中的错误码（Error code in parameter part）

常见的 S7Comm 参数中的错误码，如下表：
| Hex    | Value                                          | 描述           |
| ------ | ---------------------------------------------- | -------------- |
| 0x0000 | No error                                       | 无错误         |
| 0x0110 | Invalid block number                           | 无效的块编号   |
| 0x0111 | Invalid request length                         | 无效的请求长度 |
| 0x0112 | Invalid parameter                              | 无效参数       |
| 0x0113 | Invalid block type                             | 无效的块类型   |
| 0x0114 | Block not found                                | 块没有发现     |
| 0x0115 | Block already exists                           | 块已经存在     |
| 0x0116 | Block is write-protected                       | 块被写保护     |
| 0x0117 | The block/operating system update is too large | 块太大         |
| 0x0118 | Invalid block number                           | 无效的块编号   |
| 0x0119 | Incorrect password entered                     | 输入错误的密码 |
| 0x011A | PG resource error                              | PG 资源错误     |
| 0x011B | PLC resource error                             | PLC 资源错误    |
| 0x011C | Protocol error                                 | 协议错误       |

---

# 功能码

## JOB和ACK_DATA的功能码

当 PDU 类型是 JOB 和 ACK_DATA 时，常见的功能码，如下表：
| Hex  | Value               | 值           |
| ---- | ------------------- | ------------ |
| 0x00 | CPU services        | CPU服务      |
| 0xf0 | Setup communication | 建立通信     |
| 0x04 | Read Var            | 读取值       |
| 0x05 | Write Var           | 写入值       |
| 0x1a | Request download    | 请求下载     |
| 0x1b | Download block      | 下载块       |
| 0x1c | Download ended      | 下载结束     |
| 0x1d | Start upload        | 开始上传     |
| 0x1e | Upload              | 上传         |
| 0x1f | End upload          | 上传结束     |
| 0x28 | PI-Service          | 程序调用服务 |
| 0x29 | PLC Stop            | 关闭 PLC      |

## UserData的功能组

UserData 中常见的功能组，如下表：
| 值  | 功能组                                |
| --- | ------------------------------------- |
| 0x0 | 转换工作模式（Mode-transition）       |
| 0x1 | 工程师命令调试（Programmer commands） |
| 0x2 | 循环读取（Cyclic data）               |
| 0x3 | 块功能（Block functions）             |
| 0x4 | CPU 功能（CPU functions）              |
| 0x5 | 安全功能（Security）                  |
| 0x6 | PBC BSEND/BRECV                       |
| 0x7 | 时间功能（Time functions）            |
| 0xf | NC 编程（NC programming）              |

---

# 区域（Area names）

PLC 中常见的区域类型，如下表：
| Hex  | Value                        | 值                   |
| ---- | ---------------------------- | -------------------- |
| 0x03 | System info of 200 family    | 200 系列系统信息      |
| 0x05 | System flags of 200 family   | 200 系列系统标志      |
| 0x06 | Analog inputs of 200 family  | 200 系列模拟量输入    |
| 0x07 | Analog outputs of 200 family | 200 系列模拟量输出    |
| 0x80 | Direct peripheral access (P) | 直接访问外设         |
| 0x81 | Inputs (I)                   | 输入（I）            |
| 0x82 | Outputs (Q)                  | 输出（Q）            |
| 0x83 | Flags (M)                    | 内部标志（M）        |
| 0x84 | Data blocks (DB)             | 数据块（DB）         |
| 0x85 | Instance data blocks (DI)    | 背景数据块（DI）     |
| 0x86 | Local data (L)               | 局部变量（L）        |
| 0x87 | Unknown yet (V)              | 全局变量（V）        |
| 0x1c | S7 counters (C)              | S7 计数器（C）        |
| 0x1d | S7 timers (T)                | S7 定时器（T）        |
| 0x1e | IEC counters (200 family)    | IEC 计数器（200系列） |
| 0x1f | IEC timers (200 family)      | IEC 定时器（200系列） |

---

# 数据传输大小（Transport Sizes ）

## Item数据的传输大小（Transport sizes in item data）

下表是 Item 数据的传输大小：
| Hex | 值            | 描述                 |
| --- | ------------- | -------------------- |
| 1   | BIT           | 位（1位）            |
| 2   | BYTE          | 字节（8位）          |
| 3   | CHAR          | 字符（8位）          |
| 4   | WORD          | 字（16位）           |
| 5   | INT           | 整数（16位）         |
| 6   | DWORD         | 双字（32位）         |
| 7   | DINT          | 有符号的整数（32位） |
| 8   | REAL          | 浮点数（32位）       |
| 10  | TOD           | Time of day（32位）  |
| 11  | TIME          | IEC 时间（32位）      |
| 12  | S5TIME        | SIMATIC 时间（16位）  |
| 15  | DATE_AND_TIME | 日期和时间           |
| 28  | COUNTER       | 计数器               |
| 29  | TIMER         | 定时器               |
| 30  | IEC TIMER     | IEC 定时器            |
| 31  | IEC COUNTER   | IEC 计数器            |
| 32  | HS COUNTER    | HS 计数器             |

## 数据的传输大小（Transport sizes in data）

下表是数据部分中的值得传输大小：
| Hex | 值              | 描述                                   |
| --- | --------------- | -------------------------------------- |
| 0   | NULL            |                                        |
| 3   | BIT             | bit access, len is in bits             |
| 4   | BYTE/WORD/DWORD | byte/word/dword access, len is in bits |
| 5   | INTEGER         | integer access, len is in bits         |
| 6   | DINTEGER        | integer access, len is in bytes        |
| 7   | REAL            | real access, len is in bytes           |
| 9   | OCTET           | STRING 	octet string, len is in bytes  |

---

# 变量的结构标识（Syntax Ids of variable specification）

下表是常见的变量的结构标识：
| Hex  | 值             | 描述                                          |
| ---- | -------------- | --------------------------------------------- |
| 0x10 | S7ANY          | Address data S7-Any pointer-like DB1.DBX10.2  |
| 0x13 | PBC-R_ID       | R_ID for PBC                                  |
| 0x15 | ALARM_LOCKFREE | Alarm lock/free dataset                       |
| 0x16 | ALARM_IND      | Alarm indication dataset                      |
| 0x19 | ALARM_ACK      | Alarm acknowledge message dataset             |
| 0x1a | ALARM_QUERYREQ | Alarm query request dataset                   |
| 0x1c | NOTIFY_IND     | Notify indication dataset                     |
| 0xa2 | DRIVEESANY     | seen on Drive ES Starter with routing over S7 |
| 0xb2 | 1200SYM        | Symbolic address mode of S7-1200              |
| 0xb0 | DBREAD         | Kind of DB block read, seen only at an S7-400 |
| 0x82 | NCK            | Sinumerik NCK HMI access                      |

---

# 返回码（Return Code）

响应报文中 Data 部分的常见返回码，如下表：
| Hex  | 值                               | 描述                                  |
| ---- | -------------------------------- | ------------------------------------- |
| 0x00 | Reserved                         | 未定义，预留                          |
| 0x01 | Hardware error                   | 硬件错误                              |
| 0x03 | Accessing the object not allowed | 对象不允许访问                        |
| 0x05 | Invalid address                  | 无效地址，所需的地址超出此 PLC 的极限 |
| 0x06 | Data type not supported          | 数据类型不支持                        |
| 0x07 | Data type inconsistent           | 日期类型不一致                        |
| 0x0a | Object does not exist            | 对象不存在                            |
| 0xff | Success                          | 成功                                  |

---

# 块（Block）

在西门子设备中有8种不同类型的功能块：
| Hex    | 类型                                  | 描述                                                                                                   |
| ------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 0x3038 | OB，ASCII 为'08'，组织块               | OB 决定用户程序的结构                                                                                   |
| 0x3039 | CMod，ASCII 为'09'                     |                                                                                                        |
| 0x3041 | DB，ASCII 为'0A'，数据块               | DB 是用于存储用户数据的数据区域，除了指定给一个功能块的数据，还可以定义可以被任何块使用的共享数据      |
| 0x3042 | SDB，ASCII 为'0B'，系统和数据块        | 由编程软件自动生成主要存放 PLC 的硬件组态等信息，用户无法直接打开和更改                                  |
| 0x3043 | FC，ASCII 为'0C'，功能                 | FB、FC 本质都是一样的，都相当于子程序，可以被其他程序调用（也可以调用其他子程序），FC 使用的是共享数据块 |
| 0x3044 | SFC，ASCII 为'0D'，系统功能            | SFB 和 SFC 集成在 S7 CPU 中可以让你访问一些重要的系统功能                                                   |
| 0x3045 | FB，ASCII 为'0E'，功能块，带背景数据块 | FB、FC 本质都是一样的，都相当于子程序，可以被其他程序调用（也可以调用其他子程序），FB 使用的是背景数据块 |
| 0x3046 | SFB，ASCII 为'0F'，系统功能块          | SFB 和 SFC 集成在 S7 CPU 中可以让你访问一些重要的系统功能                                                   |

OB、FB、SFB、FC 和 SFC 都包含部分程序，因此也称作逻辑块。每种块类型所允许的块的数量以及块的长度视 CPU 而定。

---

# 程序调用服务名（PI service names）

下表是程序调用服务名称及其相关参数：
| 服务名    | 描述                                                                 |
| --------- | -------------------------------------------------------------------- |
| _INSE     | PI-Service _INSE (Activates a PLC module)                            |
| _DELE     | PI-Service _DELE (Removes module from the PLC's passive file system) |
| P_PROGRAM | PI-Service P_PROGRAM (PLC Start / Stop)                              |
| _MODU     | PI-Service _MODU (PLC Copy Ram to Rom)                               |
| _GARB     | PI-Service _GARB (Compress PLC memory)                               |

---

# 拓展协议的参数类型

下表是扩展数据中参数类型：
| 值  | 类型                  |
| --- | --------------------- |
| 0x0 | 推送（Push）          |
| 0x4 | 请求（Request）       |
| 0x8 | 响应（Response）      |
| 0x3 | NC 推送（NC Push）     |
| 0x7 | NC 请求（NC Request）  |
| 0xb | NC 响应（NC Response） |
