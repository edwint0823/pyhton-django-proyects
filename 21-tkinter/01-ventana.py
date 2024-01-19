from tkinter import *
import os.path


class Programa:
    def __init__(self):
        self.title = "Una ventana loco"
        self.icon = "./imagenes/logo.ico"
        self.icon_alt = "./21-tkinter/imagenes/logo.ico"
        self.size = "700x470"
        self.resizable = False

    def cargar(self):
        # crear ventana
        ventana = Tk()
        self.ventana = ventana
        # titulo
        ventana.title(self.title)
        # icono ventana
        ruta_icono = os.path.abspath(self.icon)
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)
        # mostrar texto
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        ventana.iconbitmap(ruta_icono)
        # tamaño
        ventana.geometry(self.size)

        # bloquear tamaño
        ventana.resizable(self.resizable, self.resizable)

    def add_texto(self, palabra):
        texto = Label(self.ventana, text=palabra)
        texto.pack()

    def mostrar(self):
        # arrancar y mostrar ventana hasta que se cierr
        self.ventana.mainloop()


# instanciar
programa = Programa()
programa.cargar()
programa.add_texto("El pepe")
programa.mostrar()
