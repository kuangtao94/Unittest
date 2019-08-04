
import unittest
import HTMLTestRunner

def add(a,b):
    return a+ｂ

class Baidu(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001(self):
        """计算两个数之和"""
        self.assertEqual(add(2,3),5)

if __name__ == '__main__':
    testunit = unittest.TestSuite(unittest.makeSuite(Baidu))
    htmlFile = "recort.html"
    with open(htmlFile,"wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,title="",description=None
        ).run(testunit)

