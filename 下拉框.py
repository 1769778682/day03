# 1.导包
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
# 2.创建浏览器驱动对象


driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作
driver.get(
    "file:///C:/Users/sandysong/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 4.业务操作
# driver.find_element_by_css_selector("[value='gz']").click()
# time.sleep(2)
# driver.find_element_by_css_selector("[value='sh']").click()
# time.sleep(2)
# driver.find_element_by_css_selector("[value='bj']").click()
# 用下标选择
select = Select(driver.find_element_by_id("selectA"))
select.select_by_index(2)
time.sleep(2)
# 用
select.select_by_value("sh")
time.sleep(2)
# 用
select.select_by_visible_text("北京")
# 5.3秒后关闭浏览器窗口
time.sleep(3)
# driver.quit()