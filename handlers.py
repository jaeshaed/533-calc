import cv 

calcStack = []
stringedCalcStack = ""

def _handleDigit(digit):
    if calcStack and calcStack[-1].replace(".", "", 1).isdigit():
        calcStack[-1] += digit
    else:
        calcStack.append(digit)
def handleDigit1():
    _handleDigit('1')
    string = makeToString()
    return string
def handleDigit2():
    _handleDigit('2')
    string = makeToString()
    return string
def handleDigit3():
    _handleDigit('3')
    string = makeToString()
    return string
def handleDigit4():
    _handleDigit('4')
    string = makeToString()
    return string
def handleDigit5():
    _handleDigit('5')
    string = makeToString()
    return string
def handleDigit6():
    _handleDigit('6')
    string = makeToString()
    return string
def handleDigit7():
    _handleDigit('7')
    string = makeToString()
    return string
def handleDigit8():
    _handleDigit('8')
    string = makeToString()
    return string
def handleDigit9():
    _handleDigit('9')
    string = makeToString()
    return string
def handleDigit0():
    _handleDigit('0')
    string = makeToString()
    return string
    
def handleErase():
    calcStack.clear()
    string = makeToString()
    return string
    
def handleOperatorPlus():
    calcStack.append('+')
    string = makeToString()
    return string
def handleOperatorMinus():
    calcStack.append('-')
    string = makeToString()
    return string
def handleOperatorMult():
    calcStack.append('*')
    string = makeToString()
    return string
def handleOperatorDivide():
    calcStack.append('/')
    string = makeToString()
    return string
def handleComma():
    _handleDigit('.')
    string = makeToString()
    return string
def handleOperatorEquals():
    if not calcStack:
        return ''
    while len(calcStack) > 1:
        try:
            calcExpression(calcStack)
        except ValueError as err:
            calcStack.clear()
            return f'ОШИБКА: {err}'
    string = makeToString()
    return string

def calcExpression(expression):
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
        finalResult = cv.add(a, b)
    elif operator == '-':
        finalResult = cv.subtract(a, b)
    elif operator == '*':
        finalResult = cv.multiply(a, b)
    elif operator == '/':
        finalResult = cv.divide(a, b)
        # cv.divide() may return an error as a string
        if not isinstance(finalResult, float):
            raise ValueError(finalResult)
    else:
        raise ValueError(f"unsupported operator: {operator}")

    # drop the fractional part if it was zero (1.0 -> 1)
    if finalResult.is_integer():
        finalResult = int(finalResult)

    expression.insert(0, str(finalResult))
        
        
def makeToString():
    stringedCalcStack = "".join(map(str, calcStack))
    return stringedCalcStack


# handleDigit6()
# handleDigit6()
# handleOperatorMult()
# handleDigit6()
# handleDigit6()
# print(handleOperatorEquals())
