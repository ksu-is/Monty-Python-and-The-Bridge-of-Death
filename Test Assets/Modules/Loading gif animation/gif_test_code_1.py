import tkinter
from PIL import Image, ImageTk, ImageSequence
import time

#Class App
class Swin(tkinter.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=800, height=800)
        self.canvas.pack()



class Lwin(tkinter.Frame):
    def __init__(self, parent):
        self.parent = parent
        #self.overrideredirect(True)
        self.canvas = tkinter.Canvas(parent, width=400, height=100)
        self.canvas.pack()
        #Lwin.lift()
        #self.wm_attributes("-disabled", True)
        self.sequence = [ImageTk.PhotoImage(img)
                             for img in ImageSequence.Iterator(
                                 Image.open('Test Assets/Modules/Loading gif animation/Fake_LB_MPBOD_GIF_RAW.gif'))]
        self.image = self.canvas.create_image(200,50, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(33, lambda: self.animate((counter+1) % (len(self.sequence))))
        #self.parent.after(10000, self.parent.destroy())

# run it ...
myroot = tkinter.Tk()
app = Lwin(myroot)
#app = Swin(myroot)
myroot.mainloop()