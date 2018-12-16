import tkinter
from PIL import Image, ImageTk, ImageSequence


#Class App
class Swin(tkinter.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=800, height=800)
        self.canvas.pack()


#creating the window, or frame, as a class. A method that is supposed to help with multi-window applications
class Lwin(tkinter.Frame):
    def __init__(self, parent):
        self.parent = parent
        myroot.overrideredirect(True)
        self.canvas = tkinter.Canvas(parent, width=400, height=100)
        self.canvas.pack()
        myroot.wm_attributes("-topmost", True)
        myroot.wm_attributes("-disabled", True)
        myroot.wm_attributes("-transparentcolor", "#87ceeb")
        self.sequence = [ImageTk.PhotoImage(img)
                             for img in ImageSequence.Iterator(
                                 Image.open('Test Assets/Modules/Loading gif animation/Fake_LB_MPBOD_GIF_RAW.gif'))]
        self.image = self.canvas.create_image(200,50, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(33, lambda: self.animate((counter+1) % (len(self.sequence))))
        

# run it ...
myroot = tkinter.Tk()
app = Lwin(myroot)
myroot.mainloop()