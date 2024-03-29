import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


root = tk.Tk()

btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+')

#can use widget.unbind(event) to unbind an event

btn.focus()
btn.pack(expand=True)

root.mainloop()