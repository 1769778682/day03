# 1.导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 2.创建浏览器驱动对象
driver = webdriver.Chrome()
# 3.打开测试网址打开注册A.html页面，完成以下操作
driver.get(
    "file:///C:/Users/sandysong/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 4.业务操作
# 1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys("admin")
time.sleep(2)
# 2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
driver.find_element(By.CSS_SELECTOR, "[placeholder='请输入密码']").send_keys('123456')
time.sleep(2)
# 3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000
driver.find_element(By.CSS_SELECTOR, ".telA").send_keys("18600000000")
time.sleep(2)
# 4).使用CSS定位方式中元素选择器定位注册按钮，并点击
driver.find_element(By.CSS_SELECTOR, "button").click()

# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()
