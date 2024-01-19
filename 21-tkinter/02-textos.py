from tkinter import *

ventana = Tk()
ventana.geometry("700x470")

texto = Label(ventana, text="Bienvenido")
texto.config(
    fg="white",
    bg="#000000",
    padx=20,
    pady=20,
    font=("Arial", 30)
)
texto.pack()

texto = Label(ventana, text="Soy pepe el grillo")
texto.config(
    justify=RIGHT,
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle"
)
texto.pack(anchor=W)


def pruebas(nombres, apellidos, pais):
    return f"Hola {nombres} {apellidos}, veo que eres de {pais}"


texto = Label(ventana, text=pruebas(pais="Puerto Rico", nombres="Pedro", apellidos="Perez"))
texto.config(
    justify=RIGHT,
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle"
)
texto.pack(anchor=CENTER)
ventana.mainloop()
