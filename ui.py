import handlers
from tkinter import *                               
from tkinter import ttk

import os
print(os.getcwd())
root = Tk()
root.title("Калькулятор")
root.geometry("400x440+600+200")
root.config(bg="#FFFFFF")

def click(y):
    label["text"] = y
    print(y)

photo0 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\0.png")
photo1 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\1.png")
photo2 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\2.png")
photo3 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\3.png")
photo4 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\4.png")
photo5 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\5.png")
photo6 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\6.png")
photo7 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\7.png")
photo8 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\8.png")
photo9 = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\9.png")
photo_plus = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\plus.png")
photo_minus = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\minus.png")
photo_umnoj = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\mult.png")
photo_delen = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\division.png")
photo_ravno = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\equally.png")
photo_sbros = PhotoImage(file=r"C:\Users\Арсений\Desktop\533-calc\grafika\clear.png")


label = ttk.Label(background="#FFFFFF", text="MUhahah", font="20")

btn1 = Button(root, image=photo1 ,text=" 1 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit1)
btn2 = Button(root, image=photo2 ,text=" 2 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit2)
btn3 = Button(root, image=photo3 ,text=" 3 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit3)
btn4 = Button(root, image=photo4 ,text=" 4 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit4)
btn5 = Button(root, image=photo5 ,text=" 5 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit5)
btn6 = Button(root, image=photo6 ,text=" 6 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit6)
btn7 = Button(root, image=photo7 ,text=" 7 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit7)
btn8 = Button(root, image=photo8 ,text=" 8 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit8)
btn9 = Button(root, image=photo9 ,text=" 9 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit9)
btn0 = Button(root, image=photo0 ,text=" 0 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleDigit0)
btn_plus = Button(root, image=photo_plus ,text=" + ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleOperatorPlus)
btn_minus = Button(root, image=photo_minus ,text=" - ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleOperatorMinus)
btn_umnoj = Button(root, image=photo_umnoj ,text=" * ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleOperatorMult)
btn_delen = Button(root, image=photo_delen ,text=" / ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleOperatorDivide)
btn_ravno = Button(root, image=photo_ravno ,text=" = ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleOperatorEquals)
btn_sbros = Button(root, image=photo_sbros ,text=" C ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handlers.handleErase)

label.place(x=20, y=0, width=100, height=100)

btn9.place(x=200, y=80, width=100, height=80)
btn8.place(x=100, y=80, width=100, height=80)
btn7.place(x=0, y=80, width=100, height=80)
btn6.place(x=200, y=170, width=100, height=80)
btn5.place(x=100, y=170, width=100, height=80)
btn4.place(x=0, y=170, width=100, height=80)
btn3.place(x=200, y=260, width=100, height=80)
btn2.place(x=100, y=260, width=100, height=80)
btn1.place(x=0, y=260, width=100, height=80)

btn_sbros.place(x=0, y=350, width=100, height=80)
btn0.place(x=100, y=350, width=100, height=80)
btn_ravno.place(x=200, y=350, width=100, height=80)

btn_plus.place(x=300, y=350, width=100, height=80)
btn_minus.place(x=300, y=260, width=100, height=80)
btn_umnoj.place(x=300, y=170, width=100, height=80)
btn_delen.place(x=300, y=80, width=100, height=80)

root.mainloop()