#This program tranlsates words in buttons after clicking the button

import tkinter
class Translator:
    def __init__(self):
        self.windpw = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.windpw)
        self.mid_frame = tkinter.Frame(self.windpw)
        self.bottom_frame = tkinter.Frame(self.windpw)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.trans_var1 = tkinter.StringVar()
        self.trans_var2 = tkinter.StringVar()
        self.trans_var3 = tkinter.StringVar()

        self.top_button = tkinter.Button(self.top_frame,text='sinister',command=self.translate1)
        self.top_label = tkinter.Label(self.top_frame,textvariable=self.trans_var1)
        self.top_button.pack(side='left')
        self.top_label.pack(side='left')

        self.mid_button = tkinter.Button(self.mid_frame,text='dexter',command=self.translate2)
        self.mid_label = tkinter.Label(self.mid_frame,textvariable=self.trans_var2)
        self.mid_button.pack(side='left')
        self.mid_label.pack(side='left')

        self.down_button = tkinter.Button(self.bottom_frame,text='medium',command=self.translate3)
        self.down_label = tkinter.Label(self.bottom_frame,textvariable=self.trans_var3)
        self.down_button.pack(side='left')
        self.down_label.pack(side='left')

        tkinter.mainloop()

    def translate1(self):
        self.translate1 = 'lewy'
        self.trans_var1.set(self.translate1)

    def translate2(self):
        self.translate2 = 'prawy'
        self.trans_var2.set(self.translate2)

    def translate3(self):
        self.translate3 = 'srodkowy'
        self.trans_var3.set(self.translate3)

my_trans = Translator()