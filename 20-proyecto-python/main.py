from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

doIt = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    doIt.registro()

elif accion == "login":
    doIt.login()
