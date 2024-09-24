from tkinter import *
import random
from PIL import ImageTk,Image
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage
def buton():
    sayi1=random.randint(1,6)
    sayi2=random.randint(1,6)
    lbl["text"] = sayi1
    lbl1["text"] = sayi2
    img["file"]=f"Desktop/{sayi1}.png"
    img1["file"]=f"Desktop/{sayi2}.png"
    

root = Tk()

btn= Button(root,
            text="buton",
            padx="20",pady="5",
            command=buton)
btn.pack()
lbl = Label(root)
lbl.pack()
lbl1 = Label(root)
lbl1.pack()

canvas = Canvas(root, width = 600, height = 200)
canvas.pack(fill=BOTH, expand=True)
img = PhotoImage(file="Desktop/6.png",)
img=img.subsample(2,2)
canvas.create_image(1,1, anchor=NW, image=img)

canvas1 = Canvas(root, width = 600, height = 200)
canvas1.pack(fill=BOTH, expand=YES)
img1 = PhotoImage(file="Desktop/6.png")

canvas1.create_image(1,1, anchor=NW, image=img1)


mainloop()