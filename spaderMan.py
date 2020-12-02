import pandas as pd
from selenium import webdriver
import time

# 爬取剧集列表，并输出成为excel表格
chromedriver_path = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)
driver.maximize_window()
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
url = 'https://movie.douban.com/tag/#/?sort=U&range=2,10&tags=%E7%94%B5%E5%BD%B1,2010%E5%B9%B4%E4%BB%A3,' \
      '%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86 '
js = 'window.open("' + url + '")'
driver.execute_script(js)
driver.close()
driver.switch_to.window(driver.window_handles[0])

# 模拟循环
while True:
    try:
        js = "var q=document.documentElement.scrollTop=10000000"
        driver.execute_script(js)
        driver.find_element_by_class_name('more').click()
        time.sleep(2)
    except:
        break

#  输出为excl文件
name = [k.text for k in driver.find_elements_by_class_name('title')]
score = [k.text for k in driver.find_elements_by_class_name('rate')]
url = [k.get_attribute('href') for k in driver.find_elements_by_class_name('item')]
pd.DataFrame({'name': name, 'score': score, 'url': url}).to_excel('电影名称.xlsx')
