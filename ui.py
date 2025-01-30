from tkinter import *                               
from tkinter import ttk

root = Tk()
root.title("Калькулятор")
root.geometry("400x440")
root.config(bg="#FFFFFF")

# def click(y):
#     label["text"] = y
#     print(y)

photo0 = PhotoImage(file=r"C:\Users\Арсений\Desktop\0.png")

label = ttk.Label(background="#FFFFFF")

btn1 = Button(root, text=" 1 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn2 = Button(root, text=" 2 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn3 = Button(root, text=" 3 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn4 = Button(root, text=" 4 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn5 = Button(root, text=" 5 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn6 = Button(root, text=" 6 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn7 = Button(root, text=" 7 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn8 = Button(root, text=" 8 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn9 = Button(root, text=" 9 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn0 = Button(root, text=" 0 ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn_plus = Button(root, text=" + ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn_minus = Button(root, text=" - ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn_umnoj = Button(root, text=" * ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn_delen = Button(root, text=" / ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn_ravno = Button(root, text=" = ", cursor="hand2", borderwidth=0, background="#FFFFFF")
btn_sbros = Button(root, text=" C ", cursor="hand2", borderwidth=0, background="#FFFFFF")

label.place(x=0, y=0, width=100, height=80)

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