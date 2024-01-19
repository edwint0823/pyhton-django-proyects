from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola estoy insertando una imagen").pack(anchor=W)

imagen = Image.open('./imagenes/fondo.png')
render = ImageTk.PhotoImage(imagen)

lb_imagen = Label(ventana, image=render)
lb_imagen.config(width=400, height=400)
lb_imagen.pack()
ventana.mainloop()
