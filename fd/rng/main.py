import tkinter as tk
from random import randrange

root = tk.Tk()
root.title("RandGUI")
root.geometry("300x50")

label = tk.Label(root, text=f"{randrange(0, 100)}")
btn = tk.Button(root, text="Generate Random Number", bg="yellow",
                command=lambda: label.config(text=f"{randrange(0, 100)}"))
label.pack()
btn.pack()

root.mainloop()
