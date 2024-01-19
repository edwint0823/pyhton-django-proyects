def mostrar(lista):
    result = ""
    for elemento in lista:
        result += str(elemento)
        result += "\n"
    return result


numeros = [2, 5, 4, 2, 6, 4, 7, 8, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7]

print(mostrar(numeros))
numeros.sort()
print(mostrar(numeros))
print(len(numeros))
try:
    busqueda = int(input("Que elemento desea buscar? "))
    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Que elemento desea buscar?"))
    else:
        print(f"Has introducido el {busqueda}")
        
    search = numeros.index(busqueda)
    print(search)
except:
    print("El elemento a buscar no existe")
finally:
    print("Has finalizado")
