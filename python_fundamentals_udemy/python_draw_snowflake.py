import tkinter as tk
import turtle

root=tk.Tk()

turtle.speed("slow")
turtle.pencolor("white")
turtle.pensize(10)

turtle.Screen().bgcolor("red")

# this function will draw V shape horizontally
# cursor will move right 30 degrees and will draw 60 pixel line forward and backward
#then cursor will point to 60 degrees left and will draw 60 pixel line forward and backward
#then cursor will move 30 degrees right and will be waiting ready in the middle of the v shape
def snow():
    turtle.right(30)
    turtle.forward(60)
    turtle.backward(60)
    turtle.left(60)

    turtle.forward(60)
    turtle.backward(60)
    turtle.right(30)

#snow()

# this function will build an arm of the snowflake
# every iteration cursor will move 30 pixels ahead and call snow() function to draw v shape
# once v shape is drawen due the iteration again cursor will move 30 pixels ahead
# since iteration is 4 times (4X30 pixels = 120)
# once arm is done building cursor will move 120 pixels backwards
def snowArm():
    for i in range(0,4):
        turtle.forward(30)
        snow()
    turtle.backward(120)


#below function will iterate snowArm function number of times dpending from the move right action degree
# total 360 degree should be the fullfilled--- and if we move cursor each time 45 degrees, then we need to iterate 8 times to match it with 360
# if we move cursor in 60 degrees then we need to iterate 6 times to meet 360 degrees

def snowflake():
    for i in range(0,8):
        snowArm()
        turtle.right(45)


#snow()
#snowArm()
snowflake()

root.mainloop