import unittest

class F6(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001(self):
        pass

    def test_002(self):
        pass

if __name__ == '__main__':
    """使用套件 Makesuite 可以执行F6类的所有执行用例"""
    suite = unittest.TestSuite(unittest.makeSuite(F6))
    unittest.TextTestRunner(verbosity=2).run()

