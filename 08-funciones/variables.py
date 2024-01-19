# variables globales
frase = "El pepe"


def hola_mundo():
    # variable local
    frase = "Hola pepe"
    print(frase)

    global texto
    texto = "Un texto global dentro de una funcion"


print(hola_mundo())
print(texto)
