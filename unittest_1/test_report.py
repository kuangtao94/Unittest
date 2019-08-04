import unittest
import HTMLTestRunner
import os

class F11(unittest.TestCase):
    def test_001(self):
        self.assertEqual(1,1)

    def test_002(self):
        self.assertEqual(1,1)

class F12(unittest.TestCase):
    def test_f11_001(self):
        self.assertEqual(1,1)

    def test_f11_002(self):
        self.assertEqual(1,1)

    def test_f11_003(self):
        self.assertEqual(1,1)

    @staticmethod
    def suite():
        suites = unittest.TestLoader().discover(
            start_dir = os.path.dirname(__file__),
            pattern = "test_report.py",
            top_level_dir = None
        )
        return suites

if __name__ == '__main__':
    suite = unittest.makeSuite(F11)
    filename = "recort.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(fp,title="",description="")
    runner.run(suite)


#使用HTML生成测试报告
    file = open("report.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = file,
        title = "测试数据",
        description=""
     )
    runner.run(F12())
    file.close()

#使用discover套件可以执行指定文件的脚本！
    suite = unittest.TestLoader().discover(
        start_dir = os.path.dirname(__file__),
        pattern = "test_report.py",
        top_level_dir=None
    )
    unittest.TextTestRunner(verbosity=2).run(suite)

    """执行F11脚本的三种套件方法"""
    suite = unittest.TestLoader().loadTestsFromModule("test_report.py")
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(F11)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestSuite(unittest.makeSuite(F11))
    unittest.TextTestRunner(verbosity=2).run(suite)




