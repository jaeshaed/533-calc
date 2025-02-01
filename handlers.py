import cv 

calcStack = []
stringedCalcStack = ""

def handleDigit1():
    calcStack.append(1)
    string = makeToString()
    return string
def handleDigit2():
    calcStack.append(2)
    
    return stringedCalcStack
def handleDigit3():
    calcStack.append(3)
    string = makeToString()
    return string
def handleDigit4():
    calcStack.append(4)
    string = makeToString()
    return string
def handleDigit5():
    calcStack.append(5)
    string = makeToString()
    return string
def handleDigit6():
    calcStack.append(6)
    string = makeToString()
    return string
def handleDigit7():
    calcStack.append(7)
    string = makeToString()
    return string
def handleDigit8():
    calcStack.append(8)
    string = makeToString()
    return string
def handleDigit9():
    calcStack.append(9)
    string = makeToString()
    return string
def handleDigit0():
    calcStack.append(0)
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
def handleOperatorEquals():
    result = calcExpression(calcStack)
    calcStack.clear
    calcStack.append(result)
    string = makeToString()
    return string

def calcExpression(expression):
    if not isinstance(expression, list):
        raise ValueError("must be a list")
    
    numbers = []
    operators = []
    
    # separate numbers and operators
    for item in expression:
        if isinstance(item, (int, float)):
            numbers.append(item)
        elif isinstance(item, str) and item in '+-*/':
            operators.append(item)
          
    result = numbers[0]
    for i, operator in enumerate(operators):
        nextNumber = numbers[i+1]
        if operator == '+':
            finalResult = cv.add(result, nextNumber)
        elif operator == '-':
            finalResult = cv.subtract(result, nextNumber)
        elif operator == '*':
            finalResult = cv.multiply(result, nextNumber)
        elif operator == '/':
            finalResult = cv.divide(result, nextNumber)
         
    return finalResult
        
        
def makeToString():
    stringedCalcStack = "".join(map(str, calcStack))
    return stringedCalcStack


handleDigit6()

handleDigit6()

handleOperatorMult()
handleDigit6()
print(handleDigit3())
