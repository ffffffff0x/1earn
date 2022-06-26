# Pillow

---

## 安装

```bash
python2 -m pip install Pillow
pip3 install Pillow
```

---

## 加载图片，使用方法open

```py
from PIL import Image
im = Image.open('test.jpg')

im.show()
# show 会调用系统默认的图片浏览器,linux好像不行，windows下正常

print im.format,im.size,im.mode
# im是一个Image对象，属性有format，size，mode。format是格式，size 是一个元组，表示(宽，高)，mode则指的图片的模式。
```

## 图片的读和写

读文件用 `Image.open()`，保存文件用 `Image.save()`，也可以用 save 方法来进行图片的格式转换。使用 os 模块中的 `os.path.splitext()` 方法可以将文件名和扩展名分离开来，下面的代码能够把 jpg 格式的图片转为 png 格式。
```py
infile = 'test.jpg'
f,e = os.path.splitext(infile)
outfile = f + '.png'

try:
    Image.open(infile).save(outfile)
except IOError:
    print "cannot convert",infile
```

## 图片剪切

从一张图片中剪切出一块区域，比如从图片提取矩形，使用 `crop()` 方法。
```py
im = Image.open('test.jpg')
box = (150,150,245,280)
region = im.crop(box)
region.show()
```

## 图片黏贴

图片的黏贴就是将一张图覆盖到另一张图上面。黏贴的方法是 paste()。格式为：paste(要贴的图片，要贴的图片的 4 元坐标组成的区域)。如下面，我们把 test.jpg 这张图片，取区域 (50,50,200,200)，将该区域旋转 180 度后贴到原来的位置。

```py
im = Image.open('test.jpg')
box = (50,50,200,200)
region = im.crop(box)
# 将图片逆序旋转180后，黏贴到原来复制的位置
region = region.transpose(Image.ROTATE_180)
im.paste(region,box)
im.show()
```

## 图像序列

当处理 GIF 这种包含多个帧的图片，称之为序列文件，PIL 会自动打开序列文件的第一帧。而使用 seek 和 tell 方法可以在不同帧移动。tell 是帧数，而 seek 是取当前帧数的图片。

使用while循环：
```py
from PIL import Image
im = Image.open("test.gif")
im.seek(1)
im.show()

try:
    while 1:
        im.seek(im.tell()+1)
        im.show()
except EOFError:
pass
```

如果要使用for循环，可以使用ImageSequence模块的Iterator方法。
```py
from PIL import Image
from PIL import ImageSequence

im = Image.open("test.gif")
for frame in ImageSequence.Iterator(im):
frame.show()
```

## 读取像素和修改像素

```py
from PIL import Image
img = Image.open('test.jpg')
width , height = img.size

for i in range(0,width):
    for j in range(0,height):
        tmp = img.getpixel((i,j))
        img.putpixel((i,j),(0,0,tmp[2]))
img.show()
```

---

## Source & Reference

- [CTF 图像隐写Python脚本处理](https://mp.weixin.qq.com/s/hTtMn53H4PbrK-7x_Ff2_w)
