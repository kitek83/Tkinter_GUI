import tkinter
class Average:
    def __init__(self):
        self.window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.window)
        self.frame2 = tkinter.Frame(self.window)
        self.frame3 = tkinter.Frame(self.window)
        self.frame4 = tkinter.Frame(self.window)
        self.frame5 = tkinter.Frame(self.window)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.label1 = tkinter.Label(self.frame1,text='Enter result from the exam nr1:')
        self.label2 = tkinter.Label(self.frame2,text='Enter the result from the exam nr2:')
        self.label3 = tkinter.Label(self.frame3,text='Enter the result from the exam nr3:')
        self.label4 = tkinter.Label(self.frame4,text='Average:')

        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        self.label4.pack(side='left')

        self.entry1 = tkinter.Entry(self.frame1, width=15)
        self.entry2 = tkinter.Entry(self.frame2, width=15)
        self.entry3 = tkinter.Entry(self.frame3,width=15)

        self.entry1.pack(side='right')
        self.entry2.pack(side='left')
        self.entry3.pack(side='left')

        self.value = tkinter.StringVar()
        self.label5 = tkinter.Label(self.frame4,textvariable=self.value)
        self.label5.pack(side='left')

        self.average = tkinter.Button(self.frame5,text='Average',command=self.get_average)
        self.quit = tkinter.Button(self.frame5,text='Quit',command=self.window.destroy)
        self.average.pack(side='left')
        self.quit.pack(side='left')

        tkinter.mainloop()
    def get_average(self):
        result1 = float(self.entry1.get())
        result2 = float(self.entry2.get())
        result3 = float(self.entry3.get())

        average = format((result1+result2+result3)/3 ,'.2f')
        self.value.set(average)
my_average = Average()


































