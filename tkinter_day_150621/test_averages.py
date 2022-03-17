import tkinter
class Average:
    def __init__(self):
        self.window = tkinter.Tk()

        self.frame_1 = tkinter.Frame(self.window)
        self.frame_2 = tkinter.Frame(self.window)
        self.frame_3 = tkinter.Frame(self.window)
        self.frame_4 = tkinter.Frame(self.window)
        self.frame_5 = tkinter.Frame(self.window)

        self.label1 = tkinter.Label(self.frame_1,text='Enter the result from the exam nr1:')
        self.label2 = tkinter.Label(self.frame_2, text='Enter the result from the exam nr2:')
        self.label3 = tkinter.Label(self.frame_3, text='Enter the result from the exam nr3:')
        self.label4 = tkinter.Label(self.frame_4, text='Average:')

        self.entry1 = tkinter.Entry(self.frame_1,width=15)
        self.entry2 = tkinter.Entry(self.frame_2, width=15)
        self.entry3 = tkinter.Entry(self.frame_3,width=15)

        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        self.label4.pack(side='left')

        self.entry1.pack(side='left')
        self.entry2.pack(side='left')
        self.entry3.pack(side='left')

        self.value = tkinter.StringVar()
        self.result = tkinter.Label(self.frame_4,textvariable=self.value)
        self.result.pack(side='left')

        self.calc = tkinter.Button(self.frame_5,text='calculate',command=self.calc_average)
        self.quit = tkinter.Button(self.frame_5,text='quit',command=self.window.destroy)
        self.calc.pack(side='left')
        self.quit.pack(side='left')

        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        tkinter.mainloop()

    def calc_average(self):
        self.result1 = float(self.entry1.get())
        self.result2 = float(self.entry2.get())
        self.result3 = float(self.entry3.get())

        self.average = (self.result1 + self.result2 + self.result3) / 3
        self.value.set(self.average)
my_average = Average()






























