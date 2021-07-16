from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains

drive_path = r'E:\Code\Envs\Crawler-env\chromedriver.exe'
driver = webdriver.Chrome(executable_path=drive_path)
driver.get('https://www.baidu.com/')


inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')

# 创建行为链
actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag,'python')
actions.move_to_element(submitTag)
actions.click(submitTag)
# 运行行为链
actions.perform()