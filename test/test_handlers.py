import unittest
import handlers

class TestMethods(unittest.TestCase):

    def tearDown(self):
        handlers.handle_erase()

    def test_calcAddition(self):
        # 5 + 5 = 10
        supposed_result = '10'
        handlers.handle_digit5()
        handlers.handle_operator_plus()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()
        
        self.assertEqual(result, supposed_result)
        
    def test_calcMinus(self):
        # 5 - 5 = 0
        supposed_result = '0'
        handlers.handle_digit5()
        handlers.handle_operator_minus()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()
        
        self.assertEqual(result, supposed_result)
        
    def test_calcDivide(self):
        # 5 / 5 = 1
        supposed_result = '1'
        handlers.handle_digit5()
        handlers.handle_operator_divide()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()
        
        self.assertEqual(result, supposed_result)
        
    def test_calcMultiply(self):
        # 5 * 5 = 25
        supposed_result = '25'
        handlers.handle_digit5()
        handlers.handle_operator_mult()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()
        
        self.assertEqual(result, supposed_result)

    def test_handleOperatorEquals_on_empty_stack(self):
        # = ?
        supposed_result = ''
        handlers.handle_erase()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_multidigit_number_addition(self):
        # 63 + 81 = 144
        supposed_result = '144'
        handlers.handle_digit6()
        handlers.handle_digit3()
        handlers.handle_operator_plus()
        handlers.handle_digit8()
        handlers.handle_digit1()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_multidigit_number_subtraction(self):
        # 21 - 385 = -364
        supposed_result = '-364'
        handlers.handle_digit2()
        handlers.handle_digit1()
        handlers.handle_operator_minus()
        handlers.handle_digit3()
        handlers.handle_digit8()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_multidigit_number_multiplication(self):
        # 4 * 10 = 40
        supposed_result = '40'
        handlers.handle_digit4()
        handlers.handle_operator_mult()
        handlers.handle_digit1()
        handlers.handle_digit0()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_multidigit_number_division(self):
        # 57 / 4 = 14.25
        supposed_result = '14.25'
        handlers.handle_digit5()
        handlers.handle_digit7()
        handlers.handle_operator_divide()
        handlers.handle_digit4()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_negative_numbers(self):
        # -5 + 2 = -3
        supposed_result = '-3'
        handlers.handle_operator_minus()
        handlers.handle_digit5()
        handlers.handle_operator_plus()
        handlers.handle_digit2()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_malformed_input_1(self):
        # /* = ?
        supposed_result = 'ОШИБКА: некорректное выражение'
        handlers.handle_operator_divide()
        handlers.handle_operator_mult()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_malformed_input_2(self):
        # 5 + = ?
        supposed_result = 'ОШИБКА: некорректное выражение'
        handlers.handle_digit5()
        handlers.handle_operator_plus()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_divizion_by_zero(self):
        # 5 / 0 = ?
        supposed_result = 'ОШИБКА: деление на ноль'
        handlers.handle_digit5()
        handlers.handle_operator_divide()
        handlers.handle_digit0()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_calccomma_addition(self):
        # 5.5 + 5.5 = 11
        supposed_result = '11'
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        handlers.handle_operator_plus()
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()
        
        self.assertEqual(result, supposed_result)

    def test_calccomma_minus(self):
        # 5.5 - 5.5 = 0
        supposed_result = '0'
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        handlers.handle_operator_minus()
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_calccomma_multiply(self):
        # 5.5 * 5.5 = 30.25
        supposed_result = '30.25'
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        handlers.handle_operator_mult()
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_calccomma_dicide(self):
        #5.5 / 5.5 = 1
        supposed_result = '1'
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        handlers.handle_operator_divide()
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_digit5()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_malformed_input3(self):
        # 5..3 + ..2 = ?
        supposed_result = 'ОШИБКА: некорректное выражение'
        handlers.handle_digit5()
        handlers.handle_comma()
        handlers.handle_comma()
        handlers.handle_operator_plus()
        handlers.handle_comma()
        handlers.handle_comma()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

    def test_malformed_input4(self):
        # .08 + 32. = ?
        supposed_result = 'ОШИБКА: некорректное выражение'
        handlers.handle_comma()
        handlers.handle_digit0()
        handlers.handle_digit8()
        handlers.handle_operator_plus()
        handlers.handle_digit3()
        handlers.handle_digit2()
        handlers.handle_comma()
        result = handlers.handle_operator_equals()

        self.assertEqual(result, supposed_result)

if __name__ == "__main__":
    unittest.main()
