import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOK, Vamos a registrarte en el sistema")

        nombre = input("¿Cual es tu nombre ?: ")
        apellido = input("¿Cual es tu apellido ?: ")
        email = input("¿Cual es tu email ?: ")
        password = input("¿Cual es tu password ?: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        result = usuario.registrar()
        if result[0] >= 1:
            print(f"\nPerfecto {result[1].nombre} te has registrado con el email {result[1].email}.")
        else:
            print(f"\nNo te has registrado ")

    def login(self):
        print("\nIdentificate en el sistema...")
        try:
            email = input("¿Cual es tu email ?: ")
            password = input("¿Cual es tu password ?: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if login[3] == email:
                print(f"\nBienvenido {login[1]} , te has registrado en el sistema  {login[5]}")
                self.proximas_acciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"\nLogin Incorrecto, intentalo mas tarde")

    def proximas_acciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que acción desea realizar?: ")
        doIt = notas.acciones.Acciones()
        if accion == "crear":
            doIt.crear(usuario)
            self.proximas_acciones(usuario)
        elif accion == "mostrar":
            doIt.mostrar(usuario)
            self.proximas_acciones(usuario)
        elif accion == "eliminar":
            doIt.borrar(usuario)
            self.proximas_acciones(usuario)
        elif accion == "salir":
            print(f"\nOk {usuario[1]}, hasta pronto")
            exit()
