#imported modules
import tkinter as tk

# Establishing Fonts
LARGE_FONT = ('Courier, 12')
Small_FONT = ('Verdana, 8')


class mpbodapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
#        (self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
#        return super().__init__(screenName=screenName, baseName=baseName, className=className, useTk=useTk, sync=sync, use=use)
#        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()
    
# for this program command notation have letters capitalized!
def C1(param):
    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ='Start Page',font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Start!",
                            command=lambda: C1('not on point'))
        button1.pack()

app = mpbodapp()
app.mainloop()
