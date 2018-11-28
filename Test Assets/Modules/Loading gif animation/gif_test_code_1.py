import tkinter
from PIL import Image, ImageTk, ImageSequence

root = tkinter.Tk()
app = App(root)

#Class App
class App:
    def __init__(self,parent):
        self.title("Gif Test!!!")
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=660, height=430)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                             for img in ImageSequence.Iterator(
                                 Image.open('davey1_1.gif'))]
        self.image = self.canvas.create_image(660,430, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(33, lambda: self.animate((counter+1) % (len(self.sequence)))

# run it ...
root.mainloop()
