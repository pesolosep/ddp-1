
from tkinter import *


class CalcGUI:
    def __init__(self, master):
        self.master = master
        master.title("CalcGUI")
        master.geometry("270x140")

        self.e1_var = IntVar()
        self.e1 = Entry(self.master, textvariable=self.e1_var)
        self.e1.grid(row=0, column=0, rowspan=4)  # __(2)__

        self.e2_var = IntVar()
        self.e2 = Entry(self.master, textvariable=self.e2_var)
        self.e2.grid(row=0, column=2, rowspan=4)

        self.b1 = Button(self.master, text="+", command=self.add)
        self.b1.grid(row=0, column=1)
        self.b2 = Button(self.master, text="-", command=self.sub)
        self.b2.grid(row=1, column=1)
        self.b3 = Button(self.master, text="*", command=self.mult)
        self.b3.grid(row=2, column=1)
        self.b4 = Button(self.master, text="/", command=self.div)
        self.b4.grid(row=3, column=1)

        self.l1 = Label(self.master, text="Result:0")
        self.l1.grid(row=4, column=0, columnspan=3)

    def add(self):
        res = self.e1_var.get()+self.e2_var.get()
        self.l1["text"] = f"Result:{res}"

    def sub(self):
        res = self.e1_var.get()-self.e2_var.get()
        self.l1["text"] = f"Result:{res}"

    def mult(self):
        res = self.e1_var.get()*self.e2_var.get()
        self.l1["text"] = f"Result:{res}"

    def div(self):
        res = self.e1_var.get()//self.e2_var.get()
        self.l1["text"] = f"Result:{res}"


root = Tk()
r = CalcGUI(root)
root.mainloop()
