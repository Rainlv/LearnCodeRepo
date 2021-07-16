from time import sleep

from selenium import webdriver

drive_path = r'E:\Code_Tools\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('''--no-sandbox''')
# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('''--disable-gpu''')
chrome_options.binary_location = r"E:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
drive = webdriver.Chrome(executable_path=drive_path, chrome_options=chrome_options)

drive.get('https://www.baidu.com')
# print(drive.page_source)

# sleep(5)
# drive.close()  # 关闭当前页面
# drive.quit()  # 关闭浏览器
# inputTag = drive.find_element_by_id('kw')   # 找id为kw的元素
# inputTag = drive.find_element_by_class_name('s_ipt')
# inputTag = drive.find_element_by_name('kw')
# inputTag = drive.find_elements_by_name('kw')  # elements表示返回多个符合要求的元素，列表返回
# inputTag = drive.find_element_by_xpath('//input[@id="kw"]') # xpath语法选择元素
inputTag = drive.find_element_by_css_selector('.quickdelete-wrap > input')  # css选择器选择元素
inputTag.send_keys('python')  # 向找到的元素输入python

# sleep(2)
# inputTag.clear() # 清除inputTag输入内容
submitTag = drive.find_element_by_id('su') # 找到百度一下的点击框
submitTag.click() # 点击

# 若只是想解析网页源代码，获取page_source后，用lxml操作，效率高
# 若要输入值等操作，用selenium方法


from time import sleep


# 无界面爬虫初始化
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path = r'E:\Anaconda\chromedriver.exe'
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# # 创建浏览器对象
# driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)