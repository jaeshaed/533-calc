import cv 

calcStack = []

def handleDigit1():
    calcStack.append(1)
    return makeToString
def handleDigit2():
    calcStack.append(2)
    return makeToString
def handleDigit3():
    calcStack.append(3)
    return makeToString
def handleDigit4():
    calcStack.append(4)
    return makeToString
def handleDigit5():
    calcStack.append(5)
    return makeToString
def handleDigit6():
    calcStack.append(6)
    return makeToString
def handleDigit7():
    calcStack.append(7)
    return makeToString
def handleDigit8():
    calcStack.append(8)
    return makeToString
def handleDigit9():
    calcStack.append(9)
    return makeToString
def handleDigit0():
    calcStack.append(0)
    return makeToString
    
def handleOperatorPlus():
    calcStack.append('+')
    return makeToString
def handleOperatorMinus():
    calcStack.append('-')
    return makeToString
def handleOperatorMult():
    calcStack.append('*')
    return makeToString
def handleOperatorDivide():
    calcStack.append('/')
    return makeToString
def handleOperatorEquals():
    result = calcExpression(calcStack)
    return result

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
    joined = "".join(map(str, calcStack))
