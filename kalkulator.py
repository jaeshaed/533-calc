import cv
chislo1 = int(input('Введите первое число: '))
chislo2 = int(input('Введите второе число: '))
znak = input("Введите +, -, *, /")
if znak == "+":
    print("Ответ", cv.add(chislo1,chislo2))
if znak == "-":
    print("Ответ", cv.subtract(chislo1,chislo2))
if znak == "*":
    print("Ответ", cv.multiply(chislo1,chislo2))
if znak == "/":
    print("Ответ", cv.divide(chislo1,chislo2))
