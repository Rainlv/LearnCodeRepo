from selenium import webdriver

drive_path = r'E:\Anaconda\chromedriver.exe'
drive = webdriver.Chrome(executable_path=drive_path)
drive.get('https://www.baidu.com/')

drive.execute_script("window.open('https://www.douban.com/')")  # 打开新标签页
# 浏览器切到douban网页
print(drive.current_url)  # 打印当前网址, 代码层面页面还在baidu

print(drive.window_handles)  # 标签页列表
drive.switch_to.window((drive.window_handles[1]))  # 将drive切换到第二个标签页，列表下标从0开始
print(drive.current_url)
