class Coche:
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_velocidad(self):
        return self.velocidad


coche = Coche()
coche.set_color("Amarillo")
coche.set_modelo("Murciélago")

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print(coche.get_color())
print(coche.get_velocidad())
print(coche.get_modelo())

# crear mas objetos
coche2 = Coche()
coche2.set_color("Naranja")
coche2.set_modelo("Gallardo")
coche2.acelerar()

print("COCHE 2")
print(coche2.get_color())
print(coche2.get_modelo())
