import unittest
from selenium import webdriver

class BaiduSo(unittest.TestCase):
    def setUp(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("Https://www.baidu.com/")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_so_enabled(self):
        """百度首页：百度首页输入框可编辑"""
        so = self.driver.find_element_by_id("kw")
        """断言"""
        self.assertTrue(so.is_enabled())

    def test_baidu_so(self):
        """百度首页：测试百度有搜索功能"""
        self.driver.find_element_by_id("kw").send_keys("selenium")
     #   so = send_key("selenium")
        self.driver.find_element_by_id("su").click()
        """断言"""
  #      self.assertEqual(self.driver.find_element_by_id("kw").text, "selenium")

if __name__ == '__main__':
    unittest.main(verbosity=2)