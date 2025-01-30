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
    return x * y


def divide(x,y):
    if y != 0:
        return x / y
    else:
        return"ошибка: деление на ноль"   
