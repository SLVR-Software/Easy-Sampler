import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def on_click(event):
    ent2.config(foreground='black')
    if ent2.get() == "Click & type...":
        event.widget.delete(0, tk.END)
    else:
        ent2.config(foreground='black')

myvar = tk.StringVar()
myvar.set("Click & type...")

ent1 = ttk.Entry(root)
ent1.grid()

ent2 = ttk.Entry(root, textvariable=myvar)
ent2.config(foreground='gray')
ent2.bind("<Button-1>", on_click)
ent2.bind("<FocusIn>", on_click)
ent2.grid()

root.mainloop()