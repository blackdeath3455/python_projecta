from tkinter import*

tk=Tk()
tk.title("borusan asim kocabitik")
tk.geometry("400x250")

lbl=Label(tk,text="Entry")
lbl.pack()

entry=Entry(tk,width=25)
entry.pack()
entry2=Entry(tk,width=25,textvariable=StringVar(),show="*",)
entry2.pack()

tk.mainloop()