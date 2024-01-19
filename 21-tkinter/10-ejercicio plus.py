from tkinter import *
from tkinter import messagebox as MessageBox


class Calculadora:

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def sumar(self):
        self.resultado.set(str(self.c_float(self.numero1.get()) + self.c_float(self.numero2.get())))
        self.mostrar_resultado()

    def restar(self):
        self.resultado.set(str(self.c_float(self.numero1.get()) - self.c_float(self.numero2.get())))
        self.mostrar_resultado()

    def multiplicar(self):
        self.resultado.set(str(self.c_float(self.numero1.get()) * self.c_float(self.numero2.get())))
        self.mostrar_resultado()

    def dividir(self):
        self.resultado.set(str(self.c_float(self.numero1.get()) / self.c_float(self.numero2.get())))
        self.mostrar_resultado()

    def mostrar_resultado(self):
        MessageBox.showinfo("Resultado", f"El resultado es {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

    def c_float(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            self.alertas.showerror("Cha loca, la cago", "No sea mca ponga números, o es alérgico al acido fólico ?")
        return result


ventana = Tk()
ventana.title("Calculara mela")
ventana.geometry("300x300")

calculadora = Calculadora(MessageBox)

marco = Frame(ventana, width=250, height=200)
marco.config(
    padx=15,
    pady=15,
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco).pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()
