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
        
    def test_calcMinus(self):
        supposedResult = 0
        handlers.handleDigit5()
        handlers.handleOperatorMinus()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        calc = handlers.calcExpression(result)
        
        self.assertEqual(calc, supposedResult)
        
    def test_calcDivide(self):
        supposedResult = 1
        handlers.handleDigit5()
        handlers.handleOperatorDivide()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        calc = handlers.calcExpression(result)
        
        self.assertEqual(calc, supposedResult)
        
    def test_calcMultiply(self):
        supposedResult = 25
        handlers.handleDigit5()
        handlers.handleOperatorMult()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        calc = handlers.calcExpression(result)
        
        self.assertEqual(calc, supposedResult)
        

if __name__ == "__main__":
    unittest.main()