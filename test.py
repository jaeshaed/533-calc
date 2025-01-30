import unittest
import handlers

class TestMethods(unittest.TestCase):
    def test_calcAddition(self):
        supposedResult = 10
        handlers.handleDigit5()
        handlers.handleOperatorPlus()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        calc = handlers.calcExpression(result)
        
        self.assertEqual(calc, supposedResult)
        

if __name__ == "__main__":
    unittest.main()