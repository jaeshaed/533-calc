import unittest
import handlers

class TestMethods(unittest.TestCase):

    def tearDown(self):
        handlers.handleErase()

    def test_calcAddition(self):
        # 5 + 5 = 10
        supposedResult = '10'
        handlers.handleDigit5()
        handlers.handleOperatorPlus()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)
        
    def test_calcMinus(self):
        # 5 - 5 = 0
        supposedResult = '0'
        handlers.handleDigit5()
        handlers.handleOperatorMinus()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)
        
    def test_calcDivide(self):
        # 5 / 5 = 1
        supposedResult = '1'
        handlers.handleDigit5()
        handlers.handleOperatorDivide()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)
        
    def test_calcMultiply(self):
        # 5 * 5 = 25
        supposedResult = '25'
        handlers.handleDigit5()
        handlers.handleOperatorMult()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)

    def test_handleOperatorEquals_on_empty_stack(self):
        # = ?
        supposedResult = ''
        handlers.handleErase()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_multidigit_number_addition(self):
        # 63 + 81 = 144
        supposedResult = '144'
        handlers.handleDigit6()
        handlers.handleDigit3()
        handlers.handleOperatorPlus()
        handlers.handleDigit8()
        handlers.handleDigit1()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_multidigit_number_subtraction(self):
        # 21 - 385 = -364
        supposedResult = '-364'
        handlers.handleDigit2()
        handlers.handleDigit1()
        handlers.handleOperatorMinus()
        handlers.handleDigit3()
        handlers.handleDigit8()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_multidigit_number_multiplication(self):
        # 4 * 10 = 40
        supposedResult = '40'
        handlers.handleDigit4()
        handlers.handleOperatorMult()
        handlers.handleDigit1()
        handlers.handleDigit0()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_multidigit_number_division(self):
        # 57 / 4 = 14.25
        supposedResult = '14.25'
        handlers.handleDigit5()
        handlers.handleDigit7()
        handlers.handleOperatorDivide()
        handlers.handleDigit4()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_negative_numbers(self):
        # -5 + 2 = -3
        supposedResult = '-3'
        handlers.handleOperatorMinus()
        handlers.handleDigit5()
        handlers.handleOperatorPlus()
        handlers.handleDigit2()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_malformed_input_1(self):
        # /* = ?
        supposedResult = 'ОШИБКА: некорректное выражение'
        handlers.handleOperatorDivide()
        handlers.handleOperatorMult()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_malformed_input_2(self):
        # 5 + = ?
        supposedResult = 'ОШИБКА: некорректное выражение'
        handlers.handleDigit5()
        handlers.handleOperatorPlus()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_divizion_by_zero(self):
        # 5 / 0 = ?
        supposedResult = 'ОШИБКА: деление на ноль'
        handlers.handleDigit5()
        handlers.handleOperatorDivide()
        handlers.handleDigit0()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_calccomma_addition(self):
        # 5.5 + 5.5 = 11
        supposedResult = '11'
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        handlers.handleOperatorPlus()
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()
        
        self.assertEqual(result, supposedResult)

    def test_calccomma_minus(self):
        # 5.5 - 5.5 = 0
        supposedResult = '0'
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        handlers.handleOperatorMinus()
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_calccomma_multiply(self):
        # 5.5 * 5.5 = 30.25
        supposedResult = '30.25'
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        handlers.handleOperatorMult()
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_calccomma_dicide(self):
        #5.5 / 5.5 = 1
        supposedResult = '1'
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        handlers.handleOperatorDivide()
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleDigit5()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_malformed_input3(self):
        # 5..3 + ..2 = ?
        supposedResult = 'ОШИБКА: некорректное выражение'
        handlers.handleDigit5()
        handlers.handleComma()
        handlers.handleComma()
        handlers.handleOperatorPlus()
        handlers.handleComma()
        handlers.handleComma()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

    def test_malformed_input4(self):
        # .08 + 32. = ?
        supposedResult = 'ОШИБКА: некорректное выражение'
        handlers.handleComma()
        handlers.handleDigit0()
        handlers.handleDigit8()
        handlers.handleOperatorPlus()
        handlers.handleDigit3()
        handlers.handleDigit2()
        handlers.handleComma()
        result = handlers.handleOperatorEquals()

        self.assertEqual(result, supposedResult)

if __name__ == "__main__":
    unittest.main()
