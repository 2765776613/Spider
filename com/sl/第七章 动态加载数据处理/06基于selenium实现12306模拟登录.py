from selenium import webdriver
from time import sleep
from chaojiying import Chaojiying_Client
from PIL import Image
from selenium.webdriver import ActionChains
# 实现规避检测
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=option)
driver.get('https://kyfw.12306.cn/otn/resources/login.html')

driver.maximize_window()  # 防止后面的location有偏差
sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
sleep(2)

# 将当前页面截图并保存
driver.save_screenshot('all.png')

# 确定验证码图片对应的左上角和右下角坐标（裁剪的区域就可以确定）
code_img_ele = driver.find_element_by_class_name('imgCode')
location = code_img_ele.location  # 返回验证码图片左上角坐标 x,y
# print(location)
size = code_img_ele.size  # 返回验证码标签对应的长和宽
# print(size)
k = 1.5  # 根据自己电脑的显示设置中的缩放比例
coordinates = (
    int(location['x']) * k, int(location['y']) * k,
    int(location['x'] + size['width']) * k,
    int(location['y'] + size['height']) * k
)

i = Image.open('./all.png')
# 根据指定区域进行图片裁剪
frame = i.crop(coordinates)
frame.save('./code.png')

# 将验证码图片提交给超级鹰进行识别
chaojiying = Chaojiying_Client('codesl', 'sunlei123', '913203')
im = open('code.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']
print(result)

all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
# 遍历列表，使用动作链对每一个列表元素对应的x，y指定的位置进行点击操作
for l in all_list:
    x = l[0]
    y = l[1]
    print("点击~~")
    ActionChains(driver).move_to_element_with_offset(code_img_ele, x / k, y / k).click().perform()
    sleep(0.5)

driver.find_element_by_id('J-userName').send_keys('15972945075')
sleep(2)
driver.find_element_by_id('J-password').send_keys('sunlei1314')
sleep(2)
driver.find_element_by_id('J-login').click()

sleep(3)
span = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
# 动作链
action = ActionChains(driver)
# # 点击长按指定的标签
# action.click_and_hold(span)
# # perform()立即执行动作链操作
# # 修改源码：selenium/webdriver/common/actions/pointer_input
# # DEFAULT_MOVE_DURATION = 50
# action.move_by_offset(int(span.size['width']), 0).perform()
action.drag_and_drop_by_offset(span, int(span.size['width']), 0).perform()
action.release()

sleep(2)
driver.quit()
