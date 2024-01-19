import os, shutil

# crear carpeta
if not os.path.isdir('./mi_carpeta'):
    os.mkdir('./mi_carpeta')
else:
    print("ya existe el archivo")

# elimiar carptea
# os.rmdir('./mi_carpeta')
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"
# shutil.copytree(ruta_original, ruta_nueva)
# os.rmdir('./mi_carpeta_copiada')

print("Contenido de mi carpeta:")
contenido = os.listdir("./")
for elemento in contenido:
    print(f"{contenido.index(elemento) + 1}. -> {elemento}")
