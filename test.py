from tkinter import *

root = Tk()  # creates a blank window

topFrame = Frame(root)
topFrame.pack()
midFrame = Frame(root)
midFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

l1 = Label(topFrame, text="Username")
l1.pack(side=LEFT)
un_in = Entry(topFrame, bd=5)
un_in.pack(side=RIGHT)
l2 = Label(midFrame, text="Password")
l2.pack(side=LEFT)
pw_in = Entry(midFrame, bd=5)
pw_in.pack(side=RIGHT)

btn1 = Button(bottomFrame, text="Login", fg="red")
btn2 = Button(bottomFrame, text="Create Account", fg="blue")
btn1.bind("<Button-1>", print("HELLO"))
btn1.pack()
btn2.pack()

root.mainloop()  # put the window to constantly print
