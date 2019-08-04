"""套件公用测试类可进行分离"""

import unittest
from selenium import webdriver

class Init(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("Http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()