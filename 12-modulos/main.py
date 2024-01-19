# import mimodulo

# print(mimodulo.holaMundo("Edwin"))

from mimodulo import holaMundo

# from mimodulo import *

print(holaMundo("Edwin"))

# modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.weekday())

fecha_personalizada = fecha_completa.strftime("%d/%m/%y, %H:%M:%S")

print(fecha_personalizada)
print(datetime.datetime.now().time())
# modulo matematicas
import math

print(f"Raiz cuadrada de 10 {math.sqrt(10)}")
print(f"numero {math.pi}")

print(f"redondear {math.ceil(math.pi)}")
print(f"redondear {math.floor(math.pi)}")

# modulo ramdom

import random

print(random.randint(15, 67))
