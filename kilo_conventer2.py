import  tkinter
import tkinter.messagebox

class Conventer:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)

        self.label = tkinter.Label(self.top_frame,text='Enter distance in kilometres:')
        self.entry = tkinter.Entry(self.top_frame, width=15)
        self.label.pack(side='left')
        self.entry.pack(side='left')

        self.convert = tkinter.Button(self.bottom_frame,text='Convert',command=self.conver_t)
        self.quit = tkinter.Button(self.bottom_frame,text='quit',command=self.window.quit)
        self.convert.pack(side='left')
        self.quit.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def conver_t(self):
        kilo = float(self.entry.get())
        mile = format(kilo * 0.6214, '.2f')
        tkinter.messagebox.showinfo('conversion from kilometre to miles:',
                                    str(kilo) + 'km is ' + str(mile) + ' miles')
my_convert = Conventer()