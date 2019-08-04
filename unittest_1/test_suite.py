import unittest

class Baidu_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_baidu_news(self):
        pass

    def test_baidu_map(self):
        pass

if __name__ == '__main__':

    """测试套件suite，1、分别测试Baidu_Test类的方法；2、可直接执行Baidu_Test类"""
    suite = unittest.TestSuite()
    suite.addTest(Baidu_Test())
#    suite.addTest(Baidu_Test("test_baidu_news"))
#   suite.addTest(Baidu_Test("test_baidu_map"))
    unittest.TextTestRunner(verbosity=2).run(suite)


