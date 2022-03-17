#This program calculate the price of the list services agter marking corresponding service.
import tkinter
class Workshop:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.mid_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.cb1_intr = tkinter.IntVar()
        self.cb2_intr = tkinter.IntVar()
        self.cb3_intr = tkinter.IntVar()
        self.cb4_intr = tkinter.IntVar()
        self.cb5_intr = tkinter.IntVar()
        self.cb6_intr = tkinter.IntVar()
        self.cb7_intr = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.top_frame,text='oil change - 30 zl',variable=self.cb1_intr)
        self.cb2 = tkinter.Checkbutton(self.top_frame,text='lubrication - 20 zl',variable=self.cb2_intr)
        self.cb3 = tkinter.Checkbutton(self.top_frame,text='radiator check - 40 zl',variable=self.cb3_intr)
        self.cb4 = tkinter.Checkbutton(self.top_frame,text='checking the gearbox - 100 zl',variable=self.cb4_intr)
        self.cb5 = tkinter.Checkbutton(self.top_frame,text='vehicle inspection - 35 zl',variable=self.cb5_intr)
        self.cb6 = tkinter.Checkbutton(self.top_frame,text='muffler replacement - 200 zl',variable=self.cb6_intr)
        self.cb7 = tkinter.Checkbutton(self.top_frame,text='wheel balancing - 20 zl',variable=self.cb7_intr)

        self.cb1.pack(side='top')
        self.cb2.pack(side='top')
        self.cb3.pack(side='top')
        self.cb5.pack(side='top')
        self.cb5.pack(side='top')
        self.cb6.pack(side='top')
        self.cb7.pack(side='top')

        self.label1 = tkinter.Label(self.mid_frame,text='Total cost:')
        self.l_string = tkinter.StringVar()
        self.label2 = tkinter.Label(self.mid_frame,textvariable=self.l_string)
        self.label3 = tkinter.Label(self.mid_frame,text='zl')
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame,text='calculate cost',command=self.calculate_costs)
        self.quit = tkinter.Button(self.bottom_frame,text='Quit',command=self.window.destroy)
        self.calc_button.pack(side='left')
        self.quit.pack(side='left')

        tkinter.mainloop()
    def calculate_costs(self):
        total = 0
        if self.cb1_intr.get() == 1:
            total += 30
        if self.cb2_intr.get() == 1:
            total += 20
        if self.cb3_intr.get() == 1:
            total += 40
        if self.cb4_intr.get() == 1:
            total += 100
        if self.cb5_intr.get() == 1:
            total += 35
        if self.cb6_intr.get() == 1:
            total += 200
        if self.cb7_intr.get() == 1:
            total += 20

        self.l_string.set(total)
































my_workshop = Workshop()