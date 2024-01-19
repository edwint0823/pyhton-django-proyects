from tkinter import *

ventana = Tk()
# ventana.geometry("700x470")

texto = Label(ventana, text="Bienvenido")
texto.config(
    fg="white",
    bg="#000000",
    padx=20,
    pady=20,
    font=("Arial", 30)
)
texto.pack(side=TOP)

texto = Label(ventana, text="Soy pepe el grillo")
texto.config(
    justify=RIGHT,
    height=3,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle"
)
texto.pack(side=TOP, fill=X, expand=True)

texto = Label(ventana, text="Hola 1")
texto.config(
    justify=RIGHT,
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle"
)
texto.pack(side=LEFT, fill=X, expand=True)

texto = Label(ventana, text="Hola 2")
texto.config(
    justify=RIGHT,
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle"
)
texto.pack(side=LEFT, fill=X, expand=True)

texto = Label(ventana, text="Hola 3")
texto.config(
    justify=RIGHT,
    height=3,
    bg="pink",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle"
)
texto.pack(side=LEFT, fill=X, expand=True)
ventana.mainloop()
