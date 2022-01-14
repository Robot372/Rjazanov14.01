from tkinter import *

win=Tk()
win.title("Okno")
win.geometry("400x400")
c=IntVar()
c.set(1)
c=Canvas(win, width=1000, height=1000, bg="white")
# Ovaal
c.create_oval(300, 350, 100, 100, outline="#f11", fill="#1f1", width=2)
c.create_oval(250, 250, 180, 180, outline="red", fill="red", width=2)
c.create_oval(120, 120, 170, 170, outline="red", fill="red", width=2)

def lisa_osa(osa:str)
    global c,var_pea,var_nina,var_suu
    pea=var_pea.get()
    nina=var_nina.get()
    suu=var_suu.get()
    if pea=="pea" and nina=="tühi" and suu=="tühi"




c.pack()
win.mainloop()

def lisa_nina():
    if var_nina.get()=="nina":
        lbl.configure(text="Lisame nina canva peale")
    elif var_nina.get()=="tühi":
        lbl.configure(text="On vaja nina kustutada ära")
def lisa_suu():
    if var_suu.get()=="suu":
        vastus.configure(text="Lisame suu canva peale")
    else:
        vastus.configure(text="On vaja suu kustutada ära")
