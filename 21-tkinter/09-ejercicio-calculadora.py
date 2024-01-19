from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title("Calculara mela")
ventana.geometry("300x300")


def sumar():
    resultado.set(str(c_float(numero1.get()) + c_float(numero2.get())))
    mostrar_resultado()


def restar():
    resultado.set(str(c_float(numero1.get()) - c_float(numero2.get())))
    mostrar_resultado()


def multiplicar():
    resultado.set(str(c_float(numero1.get()) * c_float(numero2.get())))
    mostrar_resultado()


def dividir():
    resultado.set(str(c_float(numero1.get()) / c_float(numero2.get())))
    mostrar_resultado()


def mostrar_resultado():
    MessageBox.showinfo("Resultado", f"El resultado es {resultado.get()}")
    numero1.set("")
    numero2.set("")


def c_float(numero):
    try:
        result = float(numero)
    except:
        result = 0
        MessageBox.showerror("Cha loca, la cago", "No sea mca ponga números, o es alérgico al acido fólico ?")
    return result


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=250, height=200)
marco.config(
    padx=15,
    pady=15,
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco).pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()
