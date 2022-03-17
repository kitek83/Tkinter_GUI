import tkinter
class Line:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window,width=200,height=200)
        self.canvas.create_line(0,0,199,199)
        self.canvas.create_line(199,0,0,199)
        self.canvas.pack()

        tkinter.mainloop()

my_line = Line()