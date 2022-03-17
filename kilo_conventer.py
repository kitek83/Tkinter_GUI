import tkinter
import tkinter.messagebox
class Converter:
    def __init__(self):
        self.window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.window)
        self.botton_frame = tkinter.Frame(self.window)

        self.label = tkinter.Label(self.top_frame,text='Enter distance in kilometres:')
        self.entry = tkinter.Entry(self.top_frame,width=25)

        self.label.pack(side='left')
        self.entry.pack(side='left')

        self.conv_button = tkinter.Button(self.botton_frame,text='Convert',command=self.convert)
        self.fin_button = tkinter.Button(self.botton_frame,text='Quit',command=self.window.quit)
        self.conv_button.pack(side='left')
        self.fin_button.pack(side='left')

        self.top_frame.pack()
        self.botton_frame.pack()
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.entry.get())
        mile = format(kilo * 0.6214,'.2f')

        tkinter.messagebox.showinfo('miles to kilometres converter:',
                                str(kilo) + ' kilometres is ' + str(mile) + ' miles')

my_convert = Converter()