import tkinter
import tkinter.messagebox
class Radio:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame =tkinter.Frame(self.window)
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)  #?check this set

        self.rb1 = tkinter.Radiobutton(self.top_frame,text='option1',variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text='option2',variable=self.radio_var,value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text='option3',variable=self.radio_var,value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame,text='Ok',command=self.get_option)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.window.destroy)
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        tkinter.mainloop()

    def get_option(self):
        tkinter.messagebox.showinfo('Choice:','You selected option ' + str(self.radio_var.get()))





my_radio = Radio()