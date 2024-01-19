peliculas = ["batman", "Spiderman"]
cantantes = list(('can', 'apa', 'r'))
years = list(range(2023, 2050))
print(type(peliculas))
print(type(cantantes))

nombre_extra = "fast & furious"
peliculas[0] = nombre_extra
# indices
print(peliculas[0])
print(cantantes[1:3])
print(cantantes[2:])

# Añadir
cantantes.append("kase O")
print(cantantes[2:])
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Ingrese un nombre de la pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")

# listas multidimensionales

contactos = [
    [
        "Antinio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        "Pepe",
        "pepe@pepe.com"
    ]
]

print(contactos[2][0])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) != 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"email: {elemento}")
    print("\n")
