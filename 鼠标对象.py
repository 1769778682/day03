# 1.导包
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# 2.创建浏览器驱动对象
driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作
driver.get(
    "file:///C:/Users/sandysong/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 4.业务操作
driver.find_element_by_id("userA").send_keys("admin")
mouse = ActionChains(driver)
# 鼠标双击
mouse.double_click(driver.find_element_by_id("userA"))
mouse.perform()
time.sleep(2)
# 鼠标右键
mouse.context_click(driver.find_element_by_id("userA"))
mouse.perform()
time.sleep(2)
mouse.double_click(driver.find_element_by_id("userA"))
mouse.perform()
# 鼠标悬停
mouse.move_to_element(driver.find_element_by_tag_name("button"))
mouse.perform()
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()
