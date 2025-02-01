import cv 

calcStack = []

def HandleDigits(digit):
    calcStack.append(digit)
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
