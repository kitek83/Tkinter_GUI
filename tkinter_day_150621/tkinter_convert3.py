import tkinter
class Convert:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.mid_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)

        self.label_km = tkinter.Label(self.top_frame,text='Enter distance in [km]:')
        self.entry = tkinter.Entry(self.top_frame,width=15)
        self.label_km.pack(side='left')
        self.entry.pack(side='left')

        self.decr_label = tkinter.Label(self.mid_frame,text='from [km] to [miles]:')
        self.value = tkinter.StringVar()
        self.mid_label = tkinter.Label(self.mid_frame,textvariable=self.value)
        self.decr_label.pack(side='left')
        self.mid_label.pack(side='left')

        self.convert = tkinter.Button(self.bottom_frame,text='convert',command=self.conver_t)
        self.quit = tkinter.Button(self.bottom_frame,text='quit',command=self.window.destroy)
        self.convert.pack(side='left')
        self.quit.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def conver_t(self):
        km = float(self.entry.get())
        mile = format(km * 0.6214,'.2f')
        self.value.set(mile)
my_convert = Convert()

