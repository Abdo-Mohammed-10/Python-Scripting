from tkinter import *
from tkinter import ttk
root=Tk()
frame=Frame(root)

labeltext=StringVar()
label=Label(frame,textvariable=labeltext)
labeltext.set("this is a label")

button=Button(frame,text="click me")

label.pack()
button.pack()
frame.pack()

root.mainloop()
# created by
# Abdulrahman Mohammmed