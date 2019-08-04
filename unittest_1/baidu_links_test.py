import unittest
from selenium import webdriver

class F2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_new(self):
        self.driver.find_element_by_link_text("新闻").click()

    def test_baidu_map(self):
        self.driver.find_element_by_partial_link_text("图").click()

if __name__ == "__main__":
    unittest.main(verbosity=2)

