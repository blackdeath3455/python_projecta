from tkinter import*
from PIL import ImageTk,Image

tk=Tk()
tk.title("borusan asim kocaiyik")
tk.geometry("500x500")

resim=ImageTk.PhotoImage(Image.open("Desktop/cat.jpg"))
Label(tk,image=resim).pack()

#yeniden boyutlandirma
image=Image.open("Desktop/cat.jpg")

#resize widht height
resize_image=image.resize((110,160))

img=ImageTk.PhotoImage(resize_image)
Label(tk,image=img).pack()

tk.mainloop()
