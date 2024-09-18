from tkinter import*

tk=Tk()
tk.title("borusan asim kocabiyik bilisim")
tk.geometry("400x250")
Label(tk,text="verdana",font="Verdena 12",bg="red",fg="white",).pack()
Label(tk,text="verdana Bold",font="Verdena 12 bold",).pack()
Label(tk,text="verdana Italic",font="Verdena 12 italic",).pack()
Label(tk,text="verdana Roman",font="Verdena 12 roman",).pack()

Label(tk,text="Helvetica",font="Helvetica 12",bg="red",fg="white").pack()
Label(tk,text="Helvetica Bold",font="Helvetica 12 bold",).pack()
Label(tk,text="Helvetica Italic",font="Helvetica 12 italic",).pack()
Label(tk,text="Helvetica Roman",font="Helvetica 12 roman",).pack()

Label(tk,text="Times",font="Verdena 12",).pack()
Label(tk,text="Times Bold",font="Verdena 12 bold").pack()
Label(tk,text="Times Italic",font="Verdena 12 italic",).pack()
Label(tk,text="Times Roman",font="Verdena 12 roman",).pack()
tk.mainloop()