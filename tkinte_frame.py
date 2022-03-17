import tkinter
class Gui:
    def __init__(self):
        self.window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)

        self.label1 = tkinter.Label(self.top_frame, text='Kris')
        self.label2 = tkinter.Label(self.top_frame, text='Grzesiek')
        self.label3 = tkinter.Label(self.top_frame, text='Jack')

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame, text='Adrianna')
        self.label5 = tkinter.Label(self.bottom_frame, text='Joanna')
        self.label6 = tkinter.Label(self.bottom_frame, text='Lilianna')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

my_gui = Gui()
