from selenium import webdriver
from time import sleep
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions

'''
在使用的时候直接复制粘贴即可，无需去记
'''

# 实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 如何实现让selenium规避被检测到的风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(chrome_options=chrome_options, options=option)

# 无可视化页面（无头浏览器） PhantomJs是无头浏览器
driver.get('https://www.baidu.com')

print(driver.page_source)

sleep(2)
driver.quit()
