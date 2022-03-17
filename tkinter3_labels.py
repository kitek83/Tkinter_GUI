import tkinter
class MyGui:
    def __init__(self):
        self.window = tkinter.Tk()
        self.label1 = tkinter.Label(self.window, text = 'Hello my King!')
        self.label2 = tkinter.Label(self.window, text = 'You will be excellent programmer!')

        self.label1.pack(side='top'
                              '')
        self.label2.pack(side='left')
        tkinter.mainloop()
my_gui = MyGui()