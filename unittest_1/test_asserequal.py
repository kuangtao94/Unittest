"""断言详解"""

from unittest_1.it import *

def add(a,b):
    return a - b


class BaiduLink(Init):
    @unittest.skip("该功能已经取消，请忽略该条测试用例的执行")
    def test_baidu_news(self):
        self.driver.find_element_by_link_text("新闻").click()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text("地图").click()

    @unittest.expectedFailure
    def test_001(self):
        """两个数之差进行断言"""
        self.assertEqual(add(3-2),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

