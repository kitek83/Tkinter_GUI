import tkinter
class Triangle:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window2 = tkinter.Tk()
        self.window3 = tkinter.Tk()
        self.window4 = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.window,width=200,height=200)
        self.canvas2 = tkinter.Canvas(self.window2,width=400,height=400)
        self.canvas3 = tkinter.Canvas(self.window3,width=200,height=200)
        self.canvas4 = tkinter.Canvas(self.window4,width=200,height=200)

        points = [10,10, 189,10, 100,189, 10,10]
        self.canvas.create_line(points,width=5,fill='blue',dash=(5,3))
        self.canvas.pack()

        self.canvas2.create_rectangle(10,10, 389,389,width=6)
        self.canvas2.pack()

        self.canvas3.create_oval(10,10 ,50,50,fill='green',width=9)
        self.canvas3.create_oval(100,100, 160,180)
        self.canvas3.pack()

        self.canvas4.create_arc(30,30, 190,190, start=180
                                ,extent=35)
        self.canvas4.pack()

        tkinter.mainloop()
my_traingle = Triangle()