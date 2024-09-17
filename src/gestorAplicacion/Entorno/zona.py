import pickle

class Zona:
    zonas = []

    def __init__(self, poblacion=0, nombre=None, ciudad=None):
        self.poblacion = poblacion
        self.nombre = nombre
        self.restaurantes = []
        self.ciudad = ciudad
        Zona.zonas.append(self)

    def get_ciudad(self):
        return self.ciudad

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def get_poblacion(self):
        return self.poblacion

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_restaurantes(self):
        return self.restaurantes

    @classmethod
    def get_zonas(cls):
        return cls.zonas

    def __str__(self):
        return (f"{{Información de la Zona: "
                f"población = {self.poblacion}, "
                f"nombre = '{self.nombre}', "
                f"restaurantes = {self.restaurantes}, "
                f"ciudad = {self.ciudad}}}")