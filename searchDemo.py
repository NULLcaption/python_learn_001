# Python模拟鼠标点击事件，完成搜索功能
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 创建浏览器驱动对象
chromedriver_path = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)
driver.get('https://www.baidu.com/')
# 显式等待，设置timeout
wait = WebDriverWait(driver, 10)
# 判断输入框是否加载
input = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#kw')))
# 判断搜索按钮是否加载
submit = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.s_btn')))
# 输入搜索词，点击搜索按钮
input.send_keys('香飘飘')
submit.click()
# 延时10秒关闭
time.sleep(10)
# 关闭浏览器驱动
driver.close()
