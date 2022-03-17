import tkinter
import tkinter.messagebox
class Gui:
    def __init__(self):
        self.window = tkinter.Tk()

        self.button = tkinter.Button(self.window,text='click me',command=self.show_info)
        self.button.pack()
        tkinter.mainloop()

    def show_info(self):
        tkinter.messagebox.showinfo('answer:', 'Thank You for the clicking me!')

my_gui = Gui()