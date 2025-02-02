def add (x,y):
    """Складываем два числа
    
    аргументы:
        x(int): первое число
        y(int): второе число
    Возврат:
        int: сложение x и y
    """
    return x + y

def subtract(x,y):
    """Вычитание двух чисел

    аргументы:
        x(int): первое число
        y(int): второе число
    возврат:
        int: вычитание x и y"""
    return x-y

def multiply(x,y):
    """Умножение двух чисел

       аргументы:
           x(int): первое число
           y(int): второе число
       возврат:
           int: умножение x и y"""
    return x * y


def divide(x,y):
    """Деление двух чисел

       аргументы:
           x(int): первое число
           y(int): второе число
       возврат:
           int: деление x и y"""
    if y != 0:
        return x / y
    else:
        return "деление на ноль"

