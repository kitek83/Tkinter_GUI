import tkinter
class MyGui:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window2 = tkinter.Tk()

        self.label = tkinter.Label(self.window, text = 'Welcome the world!')
        self.label2 = tkinter.Label(self.window2, text = "Hello Kris")

        self.label.pack()
        self.label2.pack()
        tkinter.mainloop()
my_gui = MyGui()