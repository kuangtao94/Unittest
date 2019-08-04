# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class BlogTitle(unittest.TestCase):

    def setUp(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.driver.get("https://www.cnblogs.com/Teachertao/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_blog_01(self):
        u"""验证元素title完全等于 Teacher涛 - 博客园"""
        # time.sleep(3)
        result = EC.title_is(u'Teacher涛 - 博客园')(self.driver)
        # print(result())
        self.assertTrue(result)

    def test_blog_02(self):
        u"""验证元素判断title包含Teacher"""
        # time.sleep(3)
        title = EC.title_contains("Teacher")(self.driver)
        # print(title())
        self.assertTrue(title)


if __name__ == "__main__":
    unittest.main(verbosity=2)

