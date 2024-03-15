from tkinter import *

tk=Tk()

canvas=Canvas(tk, width=500, height=500, bg="orange")

canvas.pack()

#canvas.create_rectangle(10,10,50,50)

#canvas.create_rectangle(20,20,300,100)

canvas.create_rectangle(20,20,100,300)


mainloop()