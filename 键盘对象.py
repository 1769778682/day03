# 1.导包
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 2.创建浏览器驱动对象


driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作
driver.get(
    "file:///C:/Users/sandysong/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 4.业务操作
# 需求：打开注册A页面，完成以下操作
driver.find_element_by_id("userA").send_keys("admin1")
time.sleep(2)
# 1). 输入用户名：admin1，暂停2秒，删除1
driver.find_element_by_id("userA").send_keys(Keys.BACK_SPACE)
# 2). 全选用户名：admin，暂停2秒
driver.find_element_by_id("userA").send_keys(Keys.CONTROL, "a")
time.sleep(2)
# 3). 复制用户名：admin，暂停2秒
driver.find_element_by_id("userA").send_keys(Keys.CONTROL, "c")
time.sleep(2)
# 4). 粘贴到密码框
driver.find_element_by_id("passwordA").send_keys(Keys.CONTROL, "v")

# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()
