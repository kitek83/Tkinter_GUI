#This program calculates distance[km] you can travel on 1L of fuel.
import tkinter
class Fuel:
    def __init__(self):
        self.window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.window)
        self.frame2 = tkinter.Frame(self.window)
        self.frame3 = tkinter.Frame(self.window)
        self.frame4 = tkinter.Frame(self.window)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        self.label1 = tkinter.Label(self.frame1,text='Enter full fuel tank capacity:')
        self.entry1 = tkinter.Entry(self.frame1,width=15)
        self.label1.pack(side='left')
        self.entry1.pack(side='left')

        self.label2 = tkinter.Label(self.frame2,text='Enter number of km, the car travel with full fuel tank:')
        self.entry2 = tkinter.Entry(self.frame2,width=15)
        self.label2.pack(side='left')
        self.entry2.pack(side='left')

        self.label3 = tkinter.Label(self.frame3, text='Distance[km] you can travel on 1L of fuel:')
        self.fuel_var = tkinter.StringVar()
        self.label4 = tkinter.Label(self.frame3,textvariable=self.fuel_var)
        self.label3.pack(side='left')
        self.label4.pack(side='left')

        self.button_calc = tkinter.Button(self.frame4,text='calculate distance',command=self.fuel_cons)
        self.quit = tkinter.Button(self.frame4,text='Quit',command=self.window.destroy)
        self.button_calc.pack(side='left')
        self.quit.pack(side='left')

        tkinter.mainloop()

    def fuel_cons(self):
        self.km = float(self.entry2.get())
        self.fuel_cap = float(self.entry1.get())
        self.km_to_travel = format((self.km / self.fuel_cap),'.2f')

        self.fuel_var.set(self.km_to_travel)

my_fuel = Fuel()