def muestra_nombre():
    print("Juan")
    print("Francisco")
    print("Victor")
    print("Edwin")
    print("pepe")
    print("Jef")


muestra_nombre()


def muestra_nombre_input(nombre):
    print(f"SU nombre es {nombre}")


# numero = input("Ingresa el numero ")


# muestra_nombre_input(numero)

def tabla(numero):
    print(f"Tabla de multiplicar {numero}")
    for contador in range(1, 11):
        operacion = int(numero) * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")


# tabla(numero)

# otro ejemplo parametros opcionales
def getEmpleado(nombre, dni=None):
    print("EMPLEADO")
    print(f"Nombre : {nombre}")
    if dni is not None:
        print(f"Dni : {dni}")


# getEmpleado("Pepe")


# ejemplo de oparaciones matematicas
def calculadora(numero1, numero2, basicas=False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    if basicas:
        cadena += f"Suma : {suma}"
        cadena += "\n"
        cadena += f"Resta : {resta}"
        cadena += "\n"
    else:
        cadena += f"Multiplicación : {multi}"
        cadena += "\n"
        cadena += f"División : {division}"
        cadena += "\n"
    return cadena


print(calculadora(5, 5, True))


# Ejemplo de funciones anidadas

def getNombre(nombre):
    return f"El nombre es : {nombre}"


def getApellido(apellido):
    return f"El apellido es : {apellido}"


def devuelveTodo(nombre, apellido):
    return f"{getNombre(nombre)} {getApellido(apellido)}"


print(devuelveTodo("Edwin ", "Ariza"))

# funciones lambda (anonimas)

tell_me_year = lambda year: f"El año es {year}"

print(tell_me_year(2020))
