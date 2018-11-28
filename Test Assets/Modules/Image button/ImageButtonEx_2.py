from tkinter import *
root=Tk()
b=Button(root,justify = LEFT)
photo=PhotoImage(file="SceneLoop_QuestionBox.png")
b.config(image=photo, text="Hello Scroll",width="380",height="80")
b.pack(side=LEFT)
root.mainloop()
