from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Formularios tkinter")

# texto encabezado
encabezado = Label(ventana, text="formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    width=50,
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W, padx=5, pady=5)
# label campo
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Campo texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state=NORMAL)
# label campo
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Campo texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state=NORMAL)

# Campo texto desc (text area)
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=NW, padx=5, pady=5)

campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, sticky=W, padx=5, pady=5)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

# boton
Label(ventana).grid(row=4, column=1)
boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
    padx=5,
    pady=5,
    bg="green",
    fg="white",
    bd=0
)

ventana.mainloop()
