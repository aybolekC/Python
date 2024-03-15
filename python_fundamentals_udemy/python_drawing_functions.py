import tkinter as tk
import turtle

root=tk.Tk()

def rectangle(horizontal, vertical, color):
    turtle.pendown()
    turtle.pensize(2)

    turtle.color(color)
    turtle.begin_fill()

    for i in range(1,3):
        turtle.forward(horizontal)
        turtle.right(90)
        turtle.forward(vertical)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.speed("slow")

rectangle(50,15,'purple')


root.mainloop