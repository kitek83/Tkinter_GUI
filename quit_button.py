import tkinter
import tkinter.messagebox
class Gui:
    def __init__(self):

        self.window = tkinter.Tk()
        self.button = tkinter.Button(self.window,text='click me!',command=self.show_info)
        self.button2 = tkinter.Button(self.window,text='finish',command=self.window.quit)

        self.button.pack()
        self.button2.pack()
        tkinter.mainloop()

    def show_info(self):
        tkinter.messagebox.showinfo('Answer:', 'Thank you for clicking.')

  
my_gui = Gui()