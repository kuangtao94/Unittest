from unittest_1.it import *
import unittest
class BaiduLink(Init):
    def test_baidu_shouye(self):
        """百度业务，测试百度的title是否正确"""
        self.assertEqual(self.driver.title,"百度一下，你就知道")
       # self.assertEqual(self.driver.title,"百度一下，你就知道".encode("gdk"))

    def test_baidu_title(self):
        if self.driver.title == "百度一下，你就知道":
            print("pass")
        else:
            print("Fail")

    def test_baidu_title(self):
        try:
            self.assertEqual(self.driver.title,"百度一下，你就知道")
        except Exception as e:
            print("Fail info:{0}".format(e.args))

    def test_baidu_login(self):
        """断言so 是否为真，返回的为 bool 型"""
        so= self.driver.find_element_by_id("kw")
        self.assertTrue(so.is_enabled())

    def test_baidu_title(self):
        """断言百度是否再title里面"""
        self.assertIn("百度",self.driver.title)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(BaiduLink)
    unittest.TextTestRunner(verbosity=2).run(suite)


