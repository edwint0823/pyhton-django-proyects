from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=70,
)


def mostrar_alerta():
    # MessageBox.showinfo("Alerta", "Hola puto")
    # MessageBox.showwarning("Alerta", "Hola puto")
    MessageBox.showerror("Alerta", "Hola puto")


Button(ventana, text="Mostrar alerta", command=mostrar_alerta).pack()


def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Quiere salir puto ?")
    if resultado == "yes":
        MessageBox.showinfo("Adios ", f"nos vemos {nombre}")
        ventana.destroy()


Button(ventana, text="Salir", command=lambda: salir("Edwin")).pack()
ventana.mainloop()
