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
print("用户名输入框的大小：", driver.find_element_by_id("userA").size)
print("页面上第一个超链接的文本内容：", driver.find_element_by_link_text("百度").text)
print("页面上第一个超链接的地址：", driver.find_element_by_link_text("百度").get_attribute("href"))
print('页面标签是不可见状态：', driver.find_element_by_name("sp1").is_displayed())
print('页面中取消按钮是不可用状态：', driver.find_element_by_id("cancelA").is_enabled())
print("页面中'旅游'对应的复选框为勾选Ture：", driver.find_element_by_id("lyA").is_selected())
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()