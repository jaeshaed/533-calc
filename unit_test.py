import unittest
import cv

class TestCalcMethods(unittest.TestCase):

    def test_add (self): 
        x = 4
        y = 5
        result = cv.add(x,y)
        self.assertEqual(result, 9)

    def test_sub (self):
        x = 4
        y = 5
        result = cv.subtract(x,y)
        self.assertEqual(result, -1)
    
    def test_mult (self):
        x = 4
        y = 5
        result = cv.multiply(x,y)
        self.assertEqual(result, 20)
    
    def test_div (self):
        x = 4
        y = 4
        result = cv.divide(x,y)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()