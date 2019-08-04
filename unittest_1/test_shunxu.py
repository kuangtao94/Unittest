import unittest
from selenium import webdriver

class F4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("Http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

        """百度首页链接测试"""

    def test_baidu_del(self):
        """首页链接测试：验证新闻的链接"""
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.back()

#先执行_add ,再执行_del

    def test_baidu_add(self):
        """首页链接测试：验证地图的链接"""
        self.driver.find_element_by_link_text("地图").click()
        self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)