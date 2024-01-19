nombre = "Edwin"
print(nombre)
print(type(nombre))

# Detectar tipado
comprobar = isinstance(nombre, str)

if comprobar:
    print("El nombre es string")
else:
    print("El nombre no es string")

# limpiar espacio
frase = "              mi nombre               "
print(frase.strip())

# Eliminar variable
year = 2023
print(year)
del year

# cobrobar variable vacia
texto = '   ff'
if len(texto) <= 0:
    print(f"la variable esta vaciá")
else:
    print(f"la variable tiene {len(texto)} caracteres")
# encontrar caracteres
frase = 'The life is beautiful'
print(frase.find("life"))

# reeemplazar palabras
nueva_frase = frase.replace("life", "motorbike")
print(nueva_frase)

# mayusculas y minusculas
print(nombre.upper())
print(nombre.lower())
