from tkinter import *
root = Tk()
canvas = Canvas(root, width = 1980, height = 1080)
canvas.pack()
img = PhotoImage(file="Desktop/rainbow-png-7020.png")
canvas.create_image(20,20, anchor=NW, image=img)
mainloop()