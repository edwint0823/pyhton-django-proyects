contador = 0
resultado = 0
for contador in range(0, 5):
    resultado += contador
    print(f"Va el {str(contador)}")

print(f"resultado {str(resultado)}")

# Ejemplo

numero_usuario = int(input('Numero para multiplicar '))
if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla del {numero_usuario}")

for numero_tabla in range(1, 11):
    if numero_usuario * numero_tabla == 56:
        print("Esta prohibido mostrar")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
# cuando el for termina de manera normal no aplica para los breaks
else:
    print("Tabla finalizada")
