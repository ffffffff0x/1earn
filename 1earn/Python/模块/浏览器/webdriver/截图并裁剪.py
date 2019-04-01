import time

from PIL import Image
from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\ppox\\Desktop\\chromedriver.exe")
driver.get("https://www.baidu.com")
time.sleep(1)

driver.get_screenshot_as_file("C:\\Users\\ppox\\Desktop\\fuck.png")  #截屏
imgFrame = Image.open('C:\\Users\\ppox\\Desktop\\fuck.png')      #保存

size = (100,200,400,500)   #设置尺寸
imgFrame = imgFrame.crop(size)  # 裁剪
imgFrame.save(r'C:\\Users\\ppox\\Desktop\\fuck2.png')   #保存


