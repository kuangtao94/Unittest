from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 静默模式
# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.cnblogs.com/Teachertao")
print(driver.title)