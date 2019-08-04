import unittest
class Fass(unittest.TestCase):
    def setup(self):
        print("已经准备好了")

    def tearown(self):
        print("已处理")

    def test001(self):
        print("test")

    def test002(self):
        print("Teacher")

if __name__ == '__main__':
    unittest.main(verbosity=2)