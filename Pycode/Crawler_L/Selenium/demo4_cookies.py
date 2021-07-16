from selenium import webdriver

drive_path = r'E:\Anaconda\chromedriver.exe'
driver = webdriver.Chrome(executable_path=drive_path)
driver.get('https://www.baidu.com/')

# for cookie in driver.get_cookies():
#     print(cookie)

print(driver.get_cookie('PSTM')) # 获取name为PSTM的cookie信息
driver.delete_cookie('PSTM') # 删除PSTM的cookie
driver.delete_all_cookies() # 删除driver产生的所有cookie
