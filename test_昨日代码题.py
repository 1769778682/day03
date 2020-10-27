# 1.导包
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# 2.创建浏览器驱动对象
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# 3.打开测试地址
driver.get('http://localhost/')
# 4.业务操作
"""--------登陆----------"""
driver.find_element_by_css_selector(".red").click()
driver.find_element_by_id('username').send_keys('15800000001')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('verify_code').send_keys('8888')
driver.find_element_by_name('sbtbutton').click()
WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_xpath("//*[text()='安全退出']"))

"""--------获取会员相关信息--------"""
for i in range(len(driver.find_elements_by_css_selector(".mu-afte span"))):
    mu_title = driver.find_elements_by_css_selector(".mu-afte span")[i].text
    mu_num = driver.find_elements_by_css_selector(".mu-num")[i].text
    mu_unit = driver.find_elements_by_css_selector(".mu-unit")[i].text
    print("{} {} {}".format(mu_title, mu_num, mu_unit))

"""---------搜索商品并加入购物车-------"""
driver.find_element_by_id('q').send_keys('小米')
driver.find_element_by_class_name("search_usercenter_btn").click()
driver.find_element_by_css_selector("[onclick*='+104)']").click()
driver.find_element_by_id("join_cart").click()
time.sleep(5)
driver.refresh()

"""---------获取购物车内的信息------"""
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_css_selector(".share-shopcar-index"))
action.perform()
try:
    total_qty = driver.find_element_by_id("total_qty").text
    total_pay = driver.find_element_by_id("total_pay").text
    print("购物车商品数量=={} 总价=={}".format(total_qty, total_pay))
except Exception as e:
    print(driver.find_element_by_css_selector(".ma").text)

# 5.关闭浏览器
time.sleep(5)
driver.quit()
