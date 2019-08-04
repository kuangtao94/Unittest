print("Hello World")

#单元测试
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import unittest_1
# class Baidu(unittest_1.TestCase):
#     def __init__(self,*args,**kwargs):
#         unittest_1.TestCase.__init__(self,*args,**kwargs)
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("http://www.baidu.com")
#         self.driver.implicitly_wait(30)
#     def test001(self):
#         """验证title是否正确"""
#         self.assertEquals(u"百度一下，你就知道",self.driver.title)
#     def test002(self):
#         """验证url是否正确"""
#         self.assertEquals(u"https:www.baidu.com",self.driver.current_url)
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == "__main__":
#     unittest_1.main(verbosity=2)


#Simple usage:
import unittest_1
class IntegerArithmeticTestCase(unittest_1.TestCase):
    def testAdd(self):## test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
if __name__ == '__main__':
    unittest_1.main()
