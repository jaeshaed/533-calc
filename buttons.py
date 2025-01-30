calcStack = []

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
