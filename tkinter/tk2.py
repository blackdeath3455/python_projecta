from tkinter import*
tk=Tk()
tk.title("borusan asim kocabiyik")
tk.geometry("400x250")

def buton():
    lbl["text"]="1. butona tikliyoruz"
def buton2():
    lbl["text"]="2. butona tiklandi"
btn= Button(tk,
            text="buton",
            padx="20",pady="5",
            command=buton)
btn.pack()

btn2 = Button(tk,
              text="buton",font="Times 12 bold",
              padx="25",pady="10",
              bg="red",fg="white", cursor="hand2",
              activebackground="black",activeforeground="green",
              command=buton2)
btn2.pack()
lbl=Label(tk)
lbl.pack()
tk.mainloop()