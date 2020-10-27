from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.NAME, "password").send_keys("123456")

