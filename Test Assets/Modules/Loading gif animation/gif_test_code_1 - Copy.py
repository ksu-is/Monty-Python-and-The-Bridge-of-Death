import tkinter
from PIL import Image, ImageTk, ImageSequence

#Class App
def __init__(self, parent):
    root.title("Gif Test!!!")
    root.parent = parent
    root.overrideredirect(True)
    root.canvas = tkinter.Canvas(parent, width=400, height=100)
    root.canvas.pack()
    root.lift()
    root.configure.wm_attributes("-disabled", True)
    root.sequence = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                            Image.open('Test Assets/Modules/Loading gif animation/Fake_LB_MPBOD_GIF_RAW.gif'))]
    root.image = root.canvas.create_image(200,50, image=self.sequence[0])
    root.animate(1)
def animate(self, counter):
    root.canvas.itemconfig(self.image, image=self.sequence[counter])
    root.parent.after(33, lambda: self.animate((counter+1) % (len(self.sequence))))

# run it ...
root = tkinter.Tk()
#app = LWIN(root)
root.mainloop()