import unittest
import handlers

class TestMethods(unittest.TestCase):

    def tearDown(self):
        handlers.handleErase()

    def test_calcAddition(self):
        supposedResult = '10'
        handlers.handleDigit5()
        handlers.handleOperatorPlus()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)
        
    def test_calcMinus(self):
        supposedResult = '0'
        handlers.handleDigit5()
        handlers.handleOperatorMinus()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)
        
    def test_calcDivide(self):
        supposedResult = '1'
        handlers.handleDigit5()
        handlers.handleOperatorDivide()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)
        
    def test_calcMultiply(self):
        supposedResult = '25'
        handlers.handleDigit5()
        handlers.handleOperatorMult()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)
        

if __name__ == "__main__":
    unittest.main()
