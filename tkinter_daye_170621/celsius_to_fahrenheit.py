#This program conver Celsius degrees to Fahrenheit degrees.
import tkinter
class Temperature:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.mid_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.top_label = tkinter.Label(self.top_frame,text='Enter temperature in [C]:')
        self.top_entry = tkinter.Entry(self.top_frame,width=15)
        self.top_label.pack(side='left')
        self.top_entry.pack(side='left')

        self.mid_label = tkinter.Label(self.mid_frame,text='Celsius degrees to Fahrenheit degrees:')
        self.temp_var = tkinter.StringVar()
        self.label3 = tkinter.Label(self.mid_frame,textvariable=self.temp_var)
        self.mid_label.pack(side='left')
        self.label3.pack(side='left')

        self.conv_button = tkinter.Button(self.bottom_frame,text='Convert',command=self.convert)
        self.quit = tkinter.Button(self.bottom_frame,text='Quit',command=self.window.destroy)
        self.conv_button.pack(side='left')
        self.quit.pack(side='left')

        tkinter.mainloop()

    def convert(self):
        self.celc = float(self.top_entry.get())
        self.far = format(((9/5*self.celc)+32),'.2f')
        self.temp_var.set(self.far)


my_temp = Temperature()