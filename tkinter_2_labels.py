import tkinter
class Gui:
    def __init__(self):
        self.window = tkinter.Tk()

        self.label1 = tkinter.Label(self.window,text = 'Hello Kris again!')
        self.label2 = tkinter.Label(self.window,text = 'This is 2nd label.')

        self.label1.pack()
        self.label2.pack()
        tkinter.mainloop()
my_gui =Gui()