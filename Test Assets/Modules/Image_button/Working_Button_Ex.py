from tkinter import *
from tkinter.font import Font

root=Tk()
b=Button(root)
text1='Sir Lancealot of Camelot'
BFont = Font(family='Gothic', size='18', weight='bold')
photo=PhotoImage(file="SLQB.png")
b.config(image=photo, text=text1,font=BFont, compound=CENTER)
b.pack()
root.mainloop()