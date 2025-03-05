import handlers
from tkinter import *
from tkinter import ttk
import tkinter as tk

import os

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x530+600+200")
root.config(bg="#FFFFFF")

def key_pressed(event):
    if event.keysym == "0":
        handler0()
    if event.keysym == "1":
        handler1()
    if event.keysym == "2":
        handler2()
    if event.keysym == "3":
        handler3()
    if event.keysym == "4":
        handler4()
    if event.keysym == "5":
        handler5()
    if event.keysym == "6":
        handler6()
    if event.keysym == "7":
        handler7()
    if event.keysym == "8":
        handler8()
    if event.keysym == "9":
        handler9()
    if event.keysym == "minus":
        handler_minus()
    if event.keysym == "plus":
        handler_plus()
    if event.keysym == "asterisk":
        handler_umnoj()
    if event.keysym == "slash":
        handler_delen()
    if event.keysym == "Return" or event.keysym == "equal":
        handler_ravno()
    if event.keysym == "comma" or event.keysym == "period":
        handler_comma()
    if event.keysym == "Escape":
        root.destroy()
    if event.keysym == "BackSpace":
        handler_clear()

root.bind("<KeyPress>", key_pressed)

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
photo_comma = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/comma.png"))
photo_clear = PhotoImage(file=os.path.join(os.path.dirname(__file__), "grafika/clear.png"))

label = ttk.Label(background="#FFFFFF", text="", font="20")

def handler1():
    label.config(text=handlers.handle_digit1().replace(".", ","))

def handler2():
    label.config(text=handlers.handle_digit2().replace(".", ","))

def handler3():
    label.config(text=handlers.handle_digit3().replace(".", ","))

def handler4():
    label.config(text=handlers.handle_digit4().replace(".", ","))

def handler5():
    label.config(text=handlers.handle_digit5().replace(".", ","))

def handler6():
    label.config(text=handlers.handle_digit6().replace(".", ","))

def handler7():
    label.config(text=handlers.handle_digit7().replace(".", ","))

def handler8():
    label.config(text=handlers.handle_digit8().replace(".", ","))

def handler9():
    label.config(text=handlers.handle_digit9().replace(".", ","))

def handler0():
    label.config(text=handlers.handle_digit0().replace(".", ","))

def handler_plus():
    label.config(text=handlers.handle_operator_plus().replace(".", ","))

def handler_minus():
    label.config(text=handlers.handle_operator_minus().replace(".", ","))

def handler_umnoj():
    label.config(text=handlers.handle_operator_mult().replace(".", ","))

def handler_ravno():
    label.config(text=handlers.handle_operator_equals().replace(".", ","))

def handler_delen():
    label.config(text=handlers.handle_operator_divide().replace(".", ","))

def handler_comma():
    label.config(text=handlers.handle_comma().replace(".", ","))

def handler_clear():
    label.config(text=handlers.handle_erase().replace(".", ","))


btn1 = Button(root, image=photo1 ,text=" 1 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler1)
btn2 = Button(root, image=photo2 ,text=" 2 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler2)
btn3 = Button(root, image=photo3 ,text=" 3 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler3)
btn4 = Button(root, image=photo4 ,text=" 4 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler4)
btn5 = Button(root, image=photo5 ,text=" 5 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler5)
btn6 = Button(root, image=photo6 ,text=" 6 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler6)
btn7 = Button(root, image=photo7 ,text=" 7 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler7)
btn8 = Button(root, image=photo8 ,text=" 8 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler8)
btn9 = Button(root, image=photo9 ,text=" 9 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler9)
btn0 = Button(root, image=photo0 ,text=" 0 ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler0)
btn_plus = Button(root, image=photo_plus ,text=" + ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler_plus)
btn_minus = Button(root, image=photo_minus ,text=" - ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler_minus)
btn_umnoj = Button(root, image=photo_umnoj ,text=" * ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler_umnoj)
btn_delen = Button(root, image=photo_delen ,text=" / ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler_delen)
btn_ravno = Button(root, image=photo_ravno ,text=" = ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler_ravno)
btn_comma = Button(root, image=photo_comma ,text=" , ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler_comma)
btn_clear = Button(root, image=photo_clear ,text=" C ", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=handler_clear)

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

btn_comma.place(x=0, y=350, width=100, height=80)
btn0.place(x=100, y=350, width=100, height=80)
btn_ravno.place(x=200, y=350, width=100, height=80)

btn_clear.place(x=100, y=440, width=200, height=80)

btn_plus.place(x=300, y=350, width=100, height=80)
btn_minus.place(x=300, y=260, width=100, height=80)
btn_umnoj.place(x=300, y=170, width=100, height=80)
btn_delen.place(x=300, y=80, width=100, height=80)

root.focus_set()
root.mainloop()
