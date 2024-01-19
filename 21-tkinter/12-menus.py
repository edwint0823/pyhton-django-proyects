from tkinter import *

ventana = Tk()
ventana.geometry("800x300")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo_menu = Menu(mi_menu, tearoff=0)

archivo_menu.add_command(label="Nuevo archivo")
archivo_menu.add_command(label="Nueva ventana")
archivo_menu.add_separator()
archivo_menu.add_command(label="Abrir archivo")
archivo_menu.add_command(label="Abrir carpeta")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

mi_menu.add_cascade(label="Archivo", menu=archivo_menu)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccionar")

ventana.mainloop()
