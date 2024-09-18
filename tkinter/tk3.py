from tkinter import*
from tkinter import messagebox

tk=Tk()
tk.title("borusan asim kocabiyik")
tk.geometry("400x250")

def show():
    messagebox.showinfo("baslik","info")
    messagebox.showerror("baslik","hata")
    messagebox.showwarning("baslik","uyari")

def ask():
    messagebox.askyesno("baslik","askyesno")
    messagebox.askokcancel("baslik","ask ok cancel")
    messagebox.askquestion("baslik","askquestion")
    messagebox.askretrycancel("baslik","askretru")
    messagebox.askyesnocancel("baslik","askyesno cancel")

l1=Label(tk,text="messagebox",font="Verdana 12 bold")
l1.pack()
b1=Button(tk,text="show",command=show,cursor="hand2")
b1.pack()
b2=Button(tk,text="ask",command=ask,cursor="hand2")
b2.pack()

tk.mainloop()
    