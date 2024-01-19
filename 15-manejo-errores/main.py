"""
try:
    nombre = input('Ingrese su nombre: ')

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print('Ha ocurrido un error')
else:
    print("Ha funcionado correctamente")
finally:
    print('Finalizado')
"""

"""

try:
    numero = int(input('Numero para elevarlo al cuadrado '))
    print("El cuadrado es " + str(numero * numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros")
# except ValueError:
#     print("Introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un error", type(e).__name__)
"""
try:
    nombre = input('Ingrese el nombre ')
    edad = int(input('Ingrese la edad '))

    if edad < 5 or edad > 110:
        raise ValueError('El edad es invalido')
    elif len(nombre) <= 1:
        raise ValueError('El nombre es invalido')
    else:
        print(f'Bienvenido {nombre}')
except ValueError:
    print('Introduce los datos correctamente')
