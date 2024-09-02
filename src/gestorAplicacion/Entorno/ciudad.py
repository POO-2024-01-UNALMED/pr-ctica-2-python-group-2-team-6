from zona import Zona
class Ciudad(Zona):
    ciudades = []

    def __init__(self, nombre=None):
        super().__init__(nombre=nombre)
        self.zonas_ciudad = []
        Ciudad.ciudades.append(self)

    def get_zonas_ciudad(self):
        return self.zonas_ciudad

    @classmethod
    def get_ciudades(cls):
        return cls.ciudades

    def actualizar_poblacion(self):
        self.poblacion = sum(zona.get_poblacion() for zona in self.zonas_ciudad)

    def __str__(self):
        return (f"{{Información de la Ciudad: "
                f"población = {self.poblacion}, "
                f"nombre = '{self.nombre}'}}")

    def agregar_zona(self, zona):
        self.zonas_ciudad.append(zona)