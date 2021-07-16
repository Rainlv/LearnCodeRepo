from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By

drive_path = r'E:\Anaconda\chromedriver.exe'
drive = webdriver.Chrome(executable_path=drive_path)

drive.get('https://www.baidu.com/')
# drive.implicitly_wait(20)  # 等待20s

element = WebDriverWait(drive, 10).until(  # 在id='kw'的元素出现前最多等待10s
    Ec.presence_of_element_located((By.ID, 'kw'))  # locate后的条件放元组 ， EC还有其他条件
)

print(element)
