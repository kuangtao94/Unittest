from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
class BolgHome(unittest.TestCase):
    u'''博客首页'''
    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument("headless")
        cls.driver = webdriver.Chrome(chrome_options=cls.option)
        url = "https://www.cnblogs.com/Teachertao/"
        cls.driver.get(url)
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        u'''验证元素存在：博客园'''
        locator = ("id", "blog_nav_sitehome")
        text = u"博客园"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_02(self):
        u'''验证元素存在：首页'''
        locator = ("id", "blog_nav_myhome")
        text = u"首页"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_03(self):
        u'''验证元素存在：发新随笔'''
        locator = ("id","blog_nav_newpost")
        text = u"发新随笔"
        result = EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
