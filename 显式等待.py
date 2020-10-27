# 1.导包
import time
from selenium import webdriver
# 2.创建浏览器驱动对象
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作
# driver.implicitly_wait(30)
driver.get(
    "file:///C:/Users/sandysong/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 4.业务操作
print(time.strftime("%Y%m%d_%H%M%S"))
element = WebDriverWait(driver, 10, 1).until(
    lambda x: x.find_element_by_css_selector("[placeholder*='延时']"))
element.send_keys("admin")
print(time.strftime("%Y%m%d_%H%M%S"))
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()