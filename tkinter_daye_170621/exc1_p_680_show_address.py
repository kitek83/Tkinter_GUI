#This program showes the address in the window after clicking the button.
import tkinter
class Address:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.str_var = tkinter.StringVar()
        self.label_add = tkinter.Label(self.top_frame,textvariable=self.str_var)
        self.label_add.pack(side='top')

        self.show_info = tkinter.Button(self.bottom_frame,text='Show address',command=self.show_address)
        self.quit = tkinter.Button(self.bottom_frame,text='Quit',command = self.window.destroy)
        self.show_info.pack(side='left')
        self.quit.pack(side='left')

        tkinter.mainloop()

    def show_address(self):
        self.address = "Finska 17/2 \n 71-792 Szczecin \n Poland"
        self.str_var.set(self.address)




my_address = Address()