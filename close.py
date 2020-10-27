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
driver.maximize_window()
time.sleep(2)
# 点击百度
driver.find_element(By.PARTIAL_LINK_TEXT, "访问").click()
time.sleep(2)
# 回退
# driver.back()
# time.sleep(2)
# # 前进
# driver.forward()
# time.sleep(2)
# 打印标题
print(driver.title)
time.sleep(2)
# 打印地址
print(driver.current_url)
time.sleep(2)
# 刷新浏览器
driver.refresh()
time.sleep(2)
driver.close()
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()