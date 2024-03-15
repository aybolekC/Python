import tkinter as tk
import turtle

root=tk.Tk()

turtle.color("red")
turtle.shape("turtle")


#turtle.forward(100)
#turtle.left(120)

#turtle.forward(100)
#turtle.left(120)


#code is rewritten with for loop to draw a triangle
for i in range(3):
    turtle.forward(100)
    turtle.left(120)


root.mainloop