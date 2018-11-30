import tkinter
from PIL import Image, ImageTk, ImageSequence

#Class App
class LWIN:
    def __init__(self, parent):
        #self.title("Gif Test!!!")
        self.parent = parent
        #self.overrideredirect(True)
        self.canvas = tkinter.Canvas(parent, width=400, height=100)
        self.canvas.pack()
        #LWIN.lift()
        self.configure.wm_attributes("-disabled", True)
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
app = LWIN(myroot)
myroot.mainloop()