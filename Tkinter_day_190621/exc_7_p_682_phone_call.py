import tkinter
import tkinter.messagebox
class Call:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.mid_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.radio_intr = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Phone call(06:00-17:59) - 7gr/min',
                                       variable=self.radio_intr,value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text='Phone call(18:00-23:59) - 12gr/min',
                                       variable=self.radio_intr,value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text='Phone call(24:00-05:59) - 5gr/min',
                                       variable=self.radio_intr,value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.label1 = tkinter.Label(self.mid_frame,text='Enter duration of you phone call [min]:')
        self.entry1 = tkinter.Entry(self.mid_frame,width=15)
        self.label1.pack(side='left')
        self.entry1.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame,text='Calculate price',command=self.get_price)
        self.quit = tkinter.Button(self.bottom_frame,text='quit',command=self.window.destroy)
        self.calc_button.pack(side='left')
        self.quit.pack(side='left')

        tkinter.mainloop()

    def get_price(self):
        self.minutes = float(self.entry1.get())
        if self.radio_intr.get() == 1:
            self.price = 7 * self.minutes
        if self.radio_intr.get() == 2:
            self.price = 12 * self.minutes
        if self.radio_intr.get() == 3:
            self.price = 5 * self.minutes

        tkinter.messagebox.showinfo('Price for the phone call:','phone call price: '+ str(self.price) + 'gr')



my_call = Call()