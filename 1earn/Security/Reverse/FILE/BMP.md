# BMP

---

bmp 文件头 BM

---

# 图片结构头及宽高计算

首先需要了解到的文件头和 bitmapinfoheader 字段有：

- bfType        2 一定为19778，其转化为十六进制为0x4d42，对应的字符串为BM
- bfSize        4 文件大小
- bfReserved1   2 一般为0
- bfReserved2   2 一般为0
- bfOffBits     4 从文件开始处到像素数据的偏移，也就是这两个结构体大小之和
- biSize        4 此结构体的大小
- biWidth       4 图像的宽
- biHeight      4 图像的高
- biPlanes      2 图像的帧数，一般为1
- biBitCount    2 一像素所占的位数，一般是24
- biCompression 4 一般为0
- biSizeImage   4 像素数据所占大小，即结构体中文件大小减去偏移(bfSize-bfOffBits)

其中存在关系为：biSizeImage=bfSize-bfOffBits =biWidth*biHeight*biBitCount/8

换句话来说就是 height=biSizeImage/biWidth/(biBitCount/8)

---

**Source & Reference**
- [misc-stegaBasic](https://www.jianshu.com/p/fe7a5fff2a95)
