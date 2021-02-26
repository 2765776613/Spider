from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://qzone.qq.com/')

driver.switch_to.frame('login_frame')
a_tag = driver.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = driver.find_element_by_id('u')
password_tag = driver.find_element_by_id('p')

userName_tag.send_keys('xxxxxx')
sleep(1)
password_tag.send_keys('XXXXXX')
sleep(1)
btn = driver.find_element_by_id('login_button')
btn.click()

sleep(3)
driver.quit()