import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEquals(calc.add(10,5), 15)
    def test_subtract(self):
        self.assertEquals(calc.subtract(10,5), 5)
    def test_mul(self):
        self.assertEquals(calc.mul(10,5), 50)
    def test_divide(self):
        self.assertEquals(calc.divide(10,5), 2)

if __name__ == '__main__':
    unittest.main()
