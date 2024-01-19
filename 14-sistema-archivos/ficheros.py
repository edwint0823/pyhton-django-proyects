from io import open
import pathlib
import shutil

ruta = str(pathlib.Path().absolute()) + "/archivo_texto.txt"
archivo = open(ruta, "a+")

# escrubir
archivo.write("Hola soy un texto \n")
archivo.close()

# abir archivo
archivo_lectura = open(ruta, "r")

# leer contenido
# contenido = archivo_lectura.read()
# print(contenido)
# for elemento in contenido:
#     print(elemento)

# leer contenido y guardar lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)

for frase in lista:
    print(f"- {frase.upper()}")

# crud de archivos
# copiar
ruta_original = str(pathlib.Path().absolute()) + "/archivo_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/archivo_texto2.txt"
ruta_alternativa = "../01-holamundo/archivo_texto_copiado.txt"
ruta_alt_absoluta = str(pathlib.Path().absolute()) + "/../01-holamundo/archivo_texto_copiado.txt"
# shutil.copyfile(ruta_original, ruta_alternativa)


# mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/archivo_movido_NUEVO.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/archivo_texto2.txt"

shutil.move(ruta_original, ruta_nueva)

"""
# Eliminar
"""
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/archivo_movido_NUEVO.txt"
os.remove(ruta_nueva)
"""
# comprobar
import os.path

ruta_comprobar = os.path.abspath("./") + '/archivo_texto2.txt'
# print(os.path.abspath("./"))
if os.path.isfile(ruta_comprobar):
    print('existe')
else:
    print('no existe')
