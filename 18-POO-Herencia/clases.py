class Persona:

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_altura(self):
        return self.altura

    def get_edad(self):
        return self.edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_altura(self, altura):
        self.altura = altura

    def set_edad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"


class Informatico(Persona):

    def __init__(self):
        self.lenguajes = "HTML, Python, JavaScript, PHP"
        self.experiencia = 5

    def get_lenguajes(self):
        return self.lenguajes

    def get_experiencia(self):
        return self.experiencia

    def aprender(self, lenguajes):
        self.lenguajes += f", {lenguajes}"
        return self.lenguajes

    def programar(self):
        return "Estoy Programando"

    def reparar_pc(self):
        return "He reparado tu ordenador"


class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.auditarRedes = "experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"
