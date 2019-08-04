"""套件分离测试"""
import unittest
from unittest_1.it import Init

class BaiduLink(Init):

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()

    # 静态方法，直接调用suite方法
    @staticmethod
    def suite():
        suite = unittest.TestSuite(unittest.makeSuite(BaiduLink))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduLink.suite())






