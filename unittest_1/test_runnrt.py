import unittest
from selenium import webdriver

class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("Http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text("新闻").click()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text("地图").click()

class BaiduSo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("Http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_so(self):
        self.driver.find_element_by_id("kw").send_keys("webdriver")
        self.driver.find_element_by_id("su").click()

if __name__ == '__main__':
    """执行F7中所有的用例，TestLoader加载测试类"""
    suite = unittest.TestLoader().loadTestsFromModule("test_runnrt.py")
    unittest.TextTestRunner(verbosity=2).run(suite)


