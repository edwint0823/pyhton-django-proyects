class Coche:
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    def get_soy_privado(self):
        return self.__soy_privado
    
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_caballaje(self):
        return self.caballaje

    def get_plazas(self):
        return self.plazas

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_velocidad(self):
        return self.velocidad

    def get_info(self):
        info = ' ----- Info de coche -----'
        info += f'\nColor: {self.get_color()}'
        info += f'\nMarca: {self.get_marca()}'
        info += f'\nModelo: {self.get_modelo()}'
        info += f'\nvelocidad: {self.get_velocidad()}'
        info += f'\nCaballaje: {self.get_caballaje()}'
        info += f'\nPlazas: {self.get_plazas()}'
        return info
