from tkinter import*

tk=Tk()
tk.title("borusan asim kocabiyik")
tk.geometry("400x250")

#grid

g1=Label(tk,text="grid label 1")
g1.grid(row=0,column=0,pady=5,padx=5)
g2=Button(tk,text="grid button 1")
g2.grid(row=0,column=1,pady=5,padx=5)
g3=Label(tk,text="grid label 2")
g3.grid(row=1,column=0)
g4=Button(tk,text="grid buton 2")
g4.grid(row=1,column=1)

#place

p1=Label(tk,text="place label")
p1.place(x=170,y=140)
p1=Button(tk,text="place button")
p1.place(x=165,y=165)


tk.mainloop()
