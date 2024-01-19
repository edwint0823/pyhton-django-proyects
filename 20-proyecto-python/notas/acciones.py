import notas.nota as modelo


class Acciones:
    def crear(self, usuario):
        print(f"Ok {usuario[1]} vamos a crear una nueva nota...")

        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Introduce la descripción de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"La nota {nota.titulo} se guardo correctamente")
        else:
            print(f"No se ha guardado la nota, lo siento {usuario[1]} ")

    def mostrar(self, usuario):
        print(f"Vale {usuario[1]} estas son las notas que existen")

        nota = modelo.Nota(usuario[0])

        notas = nota.listar()
        for elemento in notas:
            print("-----------------------------------------------")
            print('\nTitulo: ', elemento[2])
            print('Descripción: ', elemento[3])
            print("-----------------------------------------------")

    def borrar(self, usuario):
        print(f"Vale {usuario[1]} Vamos a borrar nota")
        titulo = input("Introduce el titulo de la nota :")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"hemos borrado la nota: {nota.titulo}")
        else:
            print(f"No se ha borrado la nota")
