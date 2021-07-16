from selenium import webdriver

drive_path = r'E:\Anaconda\chromedriver.exe'
drive = webdriver.Chrome(executable_path=drive_path)
drive.get('https://www.baidu.com')

submitTag = drive.find_element_by_id('su')
print(submitTag.get_attribute("value")) # 获得submitTag的value属性

drive.save_screenshot('baidu.png') # 获取网页截图
