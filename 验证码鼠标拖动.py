# 1.导包
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# 2.创建浏览器驱动对象
driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作
driver.get(
    "file:///C:/Users/sandysong/Desktop/pagetest/%E9%AA%8C%E8%AF%81%E7%A0%81/index.html")
# 4.业务操作
# 创建鼠标对象
# 拖拽某个元素到指定位置
mouse = ActionChains(driver)
mouse.drag_and_drop_by_offset(driver.find_element_by_class_name("handler_bg"), 261, 0)
mouse.perform()
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()