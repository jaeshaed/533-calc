import cv 

calcStack = []

def handleDigit1():
    calcStack.append(1)
def handleDigit2():
    calcStack.append(2)
def handleDigit3():
    calcStack.append(3)
def handleDigit4():
    calcStack.append(4)
def handleDigit5():
    calcStack.append(5)
def handleDigit6():
    calcStack.append(6)
def handleDigit7():
    calcStack.append(7)
def handleDigit8():
    calcStack.append(8)
def handleDigit9():
    calcStack.append(9)
def handleDigit0():
    calcStack.append(0)
    
def handleErase():
    calcStack.clear()

def HandleDigits(digit):
    calcStack.append(digit)
    
def handleOperatorPlus():
    calcStack.append('+')
def handleOperatorMinus():
    calcStack.append('-')
def handleOperatorMult():
    calcStack.append('*')
def handleOperatorDivide():
    calcStack.append('/')
def handleOperatorEquals():
    return calcStack

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
            
    # print(numbers)
    # print(operators)
    
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
            
    # print(result)
    # print(nextNumber)
    
    return finalResult
        