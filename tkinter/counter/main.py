from tkinter import *


class Counter:
    def __init__(self):
        self.count = 0
        self.master = Tk()
        self.master.title("Counter")
        self.master.geometry("800x700")
        self.add_btn = Button(self.master, text="Add")

    def reset(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
