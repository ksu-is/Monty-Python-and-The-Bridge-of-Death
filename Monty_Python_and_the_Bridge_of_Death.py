#imported modules
import tkinter as tk

# Establishing Fonts
LARGE_FONT = ('Courier, 12')
Small_FONT = ('Verdana, 8')

def show_frame(self, cont):
    Frame = self.frames[cont]
    Frame.tkraise()

# Establishing Class for the Program
class MainApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            container = tk.Frame(self)
            container.pack(side='top', fill='both', expand = True)

            container.grid_rowconfigure(800, weight=1)
            container.grid_columnconfigure(800, weight=1)

            self.frames = {}

            frame = MainApp(container, self)

            self.frames[F] = frame

            frame.grid(row=800, column=800, sticky='nsew')

            self.show_frame(MainApp)

# Establishing the Classes for the different frames, or screens.

class GameWin(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            container = tk.Frame(self)
            container.pack(side='top', fill='both', expand = True)

            container.grid_rowconfigure(800, weight=1)
            container.grid_columnconfigure(800, weight=1)

            self.frames = {}

            frame = GameWin(container, self)

            self.frames[F] = frame
            
            self.show_frame(GameWin)

class LoadWin(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            container = tk.Frame(self)
            container.pack(side='top', fill='both', expand = True)

            container.grid_rowconfigure(100, weight=1)
            container.grid_columnconfigure(400, weight=1)

            self.frames = {}

            frame = LoadWin(container, self)

            self.frames[F] = frame
            
            self.show_frame(LoadWin)

class MainWin(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            container = tk.Frame(self)
            container.pack(side='top', fill='both', expand = True)

            container.grid_rowconfigure(800, weight=1)
            container.grid_columnconfigure(800, weight=1)

            self.frames = {}

            frame = MainWin(container, self)

            self.frames[F] = frame
            
            self.show_frame(MainWin)
