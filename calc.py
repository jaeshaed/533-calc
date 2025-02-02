import handlers
from tkinter import *                               
from tkinter import ttk

import os

root = Tk()
root.title("Калькулятор")
root.geometry("400x440+600+200")
root.config(bg="#FFFFFF")

def click(y):
    label["text"] = y
    print(y)

photo0 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/0.png"))
photo1 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/1.png"))
photo2 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/2.png"))
photo3 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/3.png"))
photo4 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/4.png"))
photo5 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/5.png"))
photo6 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/6.png"))
photo7 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/7.png"))
photo8 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/8.png"))
photo9 = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/9.png"))
photo_plus = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/plus.png"))
photo_minus = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/minus.png"))
photo_umnoj = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/mult.png"))
photo_delen = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/division.png"))
photo_ravno = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/equally.png"))
photo_sbros = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/clear.png"))


label = ttk.Label(background="#FFFFFF", text="", font="20")

def Handler1():
    label.config(text=handlers.handleDigit1())

def Handler2():
    label.config(text=handlers.handleDigit2())

def Handler3():
    label.config(text=handlers.handleDigit3())

def Handler4():
    label.config(text=handlers.handleDigit4())

def Handler5():
    label.config(text=handlers.handleDigit5())

def Handler6():
    label.config(text=handlers.handleDigit6())

def Handler7():
    label.config(text=handlers.handleDigit7())

def Handler8():
    label.config(text=handlers.handleDigit8())

def Handler9():
    label.config(text=handlers.handleDigit9())

def Handler0():
    label.config(text=handlers.handleDigit0())

def HandlerPlus():
    label.config(text=handlers.handleOperatorPlus())

def HandlerMinus():
    label.config(text=handlers.handleOperatorMinus())

def HandlerUmnoj():
    label.config(text=handlers.handleOperatorMult())

def HandlerRavno():
    label.config(text=handlers.handleOperatorEquals())

def HandlerDelen():
    label.config(text=handlers.handleOperatorDivide())
    
def HandlerClear():
    label.config(text=handlers.handleErase())


btn1 = Button(root, image=photo1 ,text=" 1 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler1)
btn2 = Button(root, image=photo2 ,text=" 2 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler2)
btn3 = Button(root, image=photo3 ,text=" 3 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler3)
btn4 = Button(root, image=photo4 ,text=" 4 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler4)
btn5 = Button(root, image=photo5 ,text=" 5 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler5)
btn6 = Button(root, image=photo6 ,text=" 6 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler6)
btn7 = Button(root, image=photo7 ,text=" 7 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler7)
btn8 = Button(root, image=photo8 ,text=" 8 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler8)
btn9 = Button(root, image=photo9 ,text=" 9 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler9)
btn0 = Button(root, image=photo0 ,text=" 0 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=Handler0)
btn_plus = Button(root, image=photo_plus ,text=" + ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=HandlerPlus)
btn_minus = Button(root, image=photo_minus ,text=" - ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=HandlerMinus)
btn_umnoj = Button(root, image=photo_umnoj ,text=" * ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=HandlerUmnoj)
btn_delen = Button(root, image=photo_delen ,text=" / ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=HandlerDelen)
btn_ravno = Button(root, image=photo_ravno ,text=" = ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=HandlerRavno)
btn_sbros = Button(root, image=photo_sbros ,text=" C ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=HandlerClear)

label.place(x=20, y=0, width=300, height=100)

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
