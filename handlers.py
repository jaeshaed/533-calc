import cv 

calcStack = []
stringedCalcStack = ""

def _handle_digit(digit):
    if calcStack and calcStack[-1].replace(".", "", 1).isdigit():
        calcStack[-1] += digit
    else:
        calcStack.append(digit)
def handle_digit1():
    _handle_digit('1')
    string = make_to_string()
    return string
def handle_digit2():
    _handle_digit('2')
    string = make_to_string()
    return string
def handle_digit3():
    _handle_digit('3')
    string = make_to_string()
    return string
def handle_digit4():
    _handle_digit('4')
    string = make_to_string()
    return string
def handle_digit5():
    _handle_digit('5')
    string = make_to_string()
    return string
def handle_digit6():
    _handle_digit('6')
    string = make_to_string()
    return string
def handle_digit7():
    _handle_digit('7')
    string = make_to_string()
    return string
def handle_digit8():
    _handle_digit('8')
    string = make_to_string()
    return string
def handle_digit9():
    _handle_digit('9')
    string = make_to_string()
    return string
def handle_digit0():
    _handle_digit('0')
    string = make_to_string()
    return string
    
def handle_erase():
    calcStack.clear()
    string = make_to_string()
    return string
    
def handle_operator_plus():
    calcStack.append('+')
    string = make_to_string()
    return string
def handle_operator_minus():
    calcStack.append('-')
    string = make_to_string()
    return string
def handle_operator_mult():
    calcStack.append('*')
    string = make_to_string()
    return string
def handle_operator_divide():
    calcStack.append('/')
    string = make_to_string()
    return string
def handle_comma():
    _handle_digit('.')
    string = make_to_string()
    return string
def handle_operator_equals():
    if not calcStack:
        return ''
    while len(calcStack) > 1:
        try:
            calc_expression(calcStack)
        except ValueError as err:
            calcStack.clear()
            return f'ОШИБКА: {err}'
    string = make_to_string()
    return string

def calc_expression(expression):
    if not isinstance(expression, list):
        raise ValueError("must be a list")
    if not expression:
        raise ValueError('empty list')

    # Allow the expression to start with a negative number.
    if expression[0] == '-':
        expression.insert(0, '0')

    try:
        a = float(expression.pop(0))
        operator = expression.pop(0)
        b = float(expression.pop(0))
    except (IndexError, ValueError):
        raise ValueError('некорректное выражение')

    if operator == '+':
        final_result = cv.add(a, b)
    elif operator == '-':
        final_result = cv.subtract(a, b)
    elif operator == '*':
        final_result = cv.multiply(a, b)
    elif operator == '/':
        final_result = cv.divide(a, b)
        # cv.divide() may return an error as a string
        if not isinstance(final_result, float):
            raise ValueError(final_result)
    else:
        raise ValueError(f"unsupported operator: {operator}")

    # drop the fractional part if it was zero (1.0 -> 1)
    if final_result.is_integer():
        final_result = int(final_result)

    expression.insert(0, str(final_result))
        
        
def make_to_string():
    stringed_calc_stack = "".join(map(str, calcStack))
    return stringed_calc_stack


# handleDigit6()
# handleDigit6()
# handleOperatorMult()
# handleDigit6()
# handleDigit6()
# print(handleOperatorEquals())
