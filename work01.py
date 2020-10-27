# 导包
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://localhost/")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("13812345678")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_name("sbtbutton").click()
time.sleep(2)
ele = driver.find_elements_by_css_selector(".mu-afte span")
# em = driver.find_element_by_css_selector(".mu-num")
# mu = driver.find_element_by_css_selector(".mu-unit")
print(type(ele))
for i in range(len(ele)):
    ele = driver.find_elements_by_css_selector(".mu-afte span")[i].text
    em = driver.find_elements_by_css_selector(".mu-num")[i].text
    mu = driver.find_elements_by_css_selector(".mu-unit")[i].text
    print("{}{}{}".format(ele, em, mu))
driver.find_element_by_link_text("首页").click()
time.sleep(2)
driver.find_element_by_id("q").send_keys("小米")
time.sleep(2)
driver.find_element_by_css_selector(".ecsc-search-button").click()
time.sleep(2)
driver.find_element_by_link_text("加入购物车").click()
time.sleep(2)
driver.find_element_by_id("join_cart").click()
time.sleep(1)
driver.refresh()
mouse = ActionChains(driver)
mouse.move_to_element(driver.find_element_by_css_selector(".share-shopcar-index"))
mouse.perform()
try:
    print(f"购物车商品数量：{driver.find_element_by_id('total_qty').text}")
    print(f"购物车商品总价：{driver.find_element_by_id('total_pay').text}")
except Exception as e:
    print(f"没有物品时：{driver.find_element_by_css_selector('.c-i').text}")

time.sleep(3)
driver.quit()
