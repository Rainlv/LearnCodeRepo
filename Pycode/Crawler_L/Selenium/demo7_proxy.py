from selenium import webdriver

drive_path = r'E:\Anaconda\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://112.111.217.217:9999")

drive = webdriver.Chrome(executable_path=drive_path,chrome_options=options)
drive.get('http://45.32.164.128/ip.php')


