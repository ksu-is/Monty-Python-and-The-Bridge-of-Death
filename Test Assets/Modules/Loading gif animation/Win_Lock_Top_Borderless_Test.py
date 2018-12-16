import tkinter as tk # Python 3
root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
root.image = tk.PhotoImage(file='Test Assets/Modules/Loading gif animation/Fake_LB_MPBOD_GIF_RAW.gif')
label = tk.Label(root, image=root.image, bg='#87ceeb')
root.overrideredirect(True)
root.geometry("+400+100")
root.lift()
#root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "#87ceeb")
label.pack()
label.mainloop()