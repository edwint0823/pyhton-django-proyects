from tkinter import *

ventana = Tk()
ventana.geometry("800x300")


def mostrar_profesion():
    texto = ""
    if web.get():
        texto += " Desarrollo web"
    if movil.get():
        if web.get():
            texto += " y Desarrollo móvil "
        else:
            texto += " Desarrollo móvil "

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )


encabezado = Label(ventana, text="Formulario 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)
Label(ventana, text="¿ A que te dedicas").grid(row=1, column=0)

web = IntVar()
movil = IntVar()
Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrar_profesion
).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrar_profesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)


def marcar():
    marcado.config(text=opcion.get())


opcion = StringVar()
opcion.set(None)
Label(ventana, text="Cual es tu genero?").grid(row=5, column=0)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6, column=0)
Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7, column=0)

marcado = Label(ventana)
marcado.grid(row=8)


# opcion menu
def seleccionar():
    seleccionado.config(text=seleccion.get())
    return ""


seleccion = StringVar()
seleccion.set("Opcion 1")

Label(ventana, text="Selecciona una opción").grid(row=5, column=1)

select = OptionMenu(ventana, seleccion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)
seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()
