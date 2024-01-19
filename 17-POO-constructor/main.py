from coche import Coche

carro = Coche('Amarillo', "Kia", "Picanto", 80, 100, 4)
carro1 = Coche('Verde', "Renolt", "9", 90, 101, 5)
carro2 = Coche('Rojo', "Audi", "R8", 150, 500, 2)
carro3 = Coche('Negro', "Chevrolet", "Spark", 70, 90, 3)

print(carro.get_color())
print(carro.get_info())
print(carro1.get_info())
print(carro2.get_info())
print(carro3.get_info())

# Detectar tipado

if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto correcto")

# Visibilidad
print(carro.soy_publico)
print(carro.get_soy_privado())
