from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.taobao.com/')

# 标签定位
search_input = driver.find_element_by_id('q')
# 标签交互
search_input.send_keys('机器学习实战')

# 执行一组js程序
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

# 点击搜索按钮
btn = driver.find_element_by_class_name('btn-search')
btn.click()

driver.get('https://www.baidu.com')
sleep(2)

# 回退
driver.back()
sleep(2)
# 前进
driver.forward()

sleep(3)
driver.quit()
