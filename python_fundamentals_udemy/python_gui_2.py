import tkinter

window=tkinter.Tk()
window.title("My GUI")


#create a label
tkinter.Label(window,text="Enter text: ").grid(row=0, column=0)

#create a text entry box
entry=tkinter.Entry(window, width=20, bg="pink")
entry.grid(row=1,column=0)

#create a checkbox
tkinter.Checkbutton(window,text="Checkbutton 1").grid(row=3, column=0)
tkinter.Checkbutton(window,text="Checkbutton 2").grid(row=4, column=0)

#create a scale bar
tkinter.Scale(window, from_=0, to=100,orient=tkinter.HORIZONTAL).grid(row=4,column=1)

#canvas
#a space for drawing
tkinter.Canvas(window,bg="red", width=150, height=100).grid(row=6, column=2)


window.mainloop()