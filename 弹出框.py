# 1.导包
import time
from selenium import webdriver
# 2.创建浏览器驱动对象

driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作

driver.get(
    "file:///C:/Users/sandysong/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 4.业务操作
driver.find_element_by_id("alerta").click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()
driver.find_element_by_id("userA").send_keys("admin")
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()