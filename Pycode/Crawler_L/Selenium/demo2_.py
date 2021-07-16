from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select  # 操作select标签必要导入

drive_path = r'E:\Anaconda\chromedriver.exe'

drive = webdriver.Chrome(executable_path=drive_path)

# 操作checkbox标签(豆瓣不行)
# drive.get('https://www.douban.com/')
# rememberTag = drive.find_element_by_name('remember')
# rememberTag.click()  # 模拟鼠标单击操作


# 操作select标签
# drive.get('xxx')  # 没找到网站，展示一下代码框架
# selectTag = Select(drive.find_element_by_name('这是一个select标签')) # 找到一个select标签
# selectTag.select_by_index(1)    # 顺序，0开始（大概
# selectTag.select_by_value('xxx') # 源码中的value
# selectTag.select_by_visible_text('') # 源码中的text()

