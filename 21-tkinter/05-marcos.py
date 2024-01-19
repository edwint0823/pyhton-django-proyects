from tkinter import *

ventana = Tk()

ventana.title("Marcos")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=True)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="grey",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Hola pepe")
texto.config(
    bg="grey",
    fg="white",
    font=("Arial", 20, "bold"),
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=True)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="light blue",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=NW)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="light green",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

ventana.mainloop()
