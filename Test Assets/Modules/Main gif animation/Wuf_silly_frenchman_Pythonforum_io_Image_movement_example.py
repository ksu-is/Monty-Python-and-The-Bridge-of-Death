#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from functools import partial
 
try:
    # Tkinter for Python 2.xx
    import Tkinter as tk
except ImportError:
    # Tkinter for Python 3.xx
    import tkinter as tk
 
APP_TITLE = "Move Image (png)"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200
 
 
class Application(tk.Frame):
 
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
         
        self.master.bind('<KeyPress>', self.move_Knight)
         
        self.canvas = tk.Canvas(self, bg='steelblue', highlightthickness=0)
        self.canvas.pack()
         
        self.knight1_speed = 2
         
        self.image = tk.PhotoImage(file='my_image.png')
        self.canvas.create_image(10, 10, anchor='nw', image=self.image,
            tags='my_image') 
 
    def move_Knight(self, event):
        print(event.keysym)
        if event.keysym == "Up":
            self.canvas.move('my_image', 0, -self.knight1_speed)
        elif event.keysym == "Down":
            self.canvas.move('my_image', 0, self.knight1_speed)
        elif event.keysym == "Left":
            self.canvas.move('my_image', -self.knight1_speed, 0)
        elif event.keysym == "Right":
            self.canvas.move('my_image', self.knight1_speed, 0)
                        
def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
     
    app = Application(app_win).pack(fill='both', expand=True)
     
    app_win.mainloop()
  
  
if __name__ == '__main__':
    main()