import tkinter
import tkinter.messagebox
class Checkbox:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.cb1_var = tkinter.IntVar()
        self.cb2_var = tkinter.IntVar()
        self.cb3_var = tkinter.IntVar()

        self.cb1_var.set(0)
        self.cb2_var.set(0)
        self.cb3_var.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame,text='option1',variable=self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.top_frame,text='option2',variable=self.cb2_var)
        self.cb3 = tkinter.Checkbutton(self.top_frame,text='option3',variable=self.cb3_var)
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame,text='Ok',command=self.get_option)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.window.destroy)
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        tkinter.mainloop()
    def get_option(self):
        self.message = 'You selected option: '
        if self.cb1_var.get() == 1:
            self.message = self.message + '1\n'
        if self.cb2_var.get() == 1:
            self.message = self.message + '2\n'
        if self.cb3_var.get() == 1:
            self.message = self.message + '3\n'

        tkinter.messagebox.showinfo('Your choice:',self.message + '\n' + self.message)



























my_checkbox = Checkbox()