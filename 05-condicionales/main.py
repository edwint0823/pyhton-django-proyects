""""

"""
# Ejemplo 1
color = input("Cual es el color que estoy pensando ")

if color == "rojo":
    print("Es rojo loco")
else:
    print("No es rojo loco")

# Ejemplo 2

# Ejemplo 3
edad = input("Cual es su edad ")
ciudad = input("Donde vive ")

if int(edad) >= 18:
    print("Es mayor de edad")
    if ciudad == "Bucaros":
        print("Es de bucaros")
    elif ciudad == "Europa":
        print("No es de bucaros")
else:
    print("ta chiquito pelao")

# Ejmplo 4

edad_minima = 18
edad_maxima = 65
edad_oficial = int(edad)
if edad_oficial >= 18 or edad_oficial <= 65:
    print("Esta en edad de chamba")
else:
    print("No esta en edad de chamba")

pais = ciudad
# Ejmplo 5
if not (pais == "Mexico" or pais == "Colombia" or pais == "Costa rica" or pais == "España"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")
