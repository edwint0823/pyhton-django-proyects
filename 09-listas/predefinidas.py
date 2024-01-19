cantantes = ['can', 'apa', 'r']
numeros = [1, 3, 5, 4, 9, 50, 20]

# ordenar
numeros.sort()
print(numeros)

# añádir
cantantes.append("kase o")
cantantes.insert(0, "santa fe klan")
print(cantantes)

# eliminar
cantantes.pop(1)
cantantes.remove("r")
print(cantantes)

numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('r' in cantantes)

# contar numeros elementos
print(len(cantantes))

# cuantas vecxes aparece un elemento
numeros.append(5)
print(numeros.count(5))

# Unir lista
cantantes.extend(numeros)
print(cantantes)
