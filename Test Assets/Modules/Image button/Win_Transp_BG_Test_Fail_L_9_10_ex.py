import tkinter as tk # Python 3
root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
root.image = tk.PhotoImage(file='SceneLoop_QuestionBox.png')
label = tk.Label(root, image=root.image, bg='#F1D592')
root.overrideredirect(True)
root.geometry("+380+80")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "#F1D592")
label.pack()
label.mainloop()