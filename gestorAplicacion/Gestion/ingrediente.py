class Ingrediente:
    ingredientes = []

    def __init__(self, nombre=None, precio=None):
        self.nombre = nombre
        self.precio = precio
        Ingrediente.ingredientes.append(self)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    @classmethod
    def get_ingredientes(cls):
        return cls.ingredientes

    @classmethod
    def set_ingredientes(cls, ingredientes):
        cls.ingredientes = ingredientes

    def __str__(self):
        return f"Ingrediente{{nombre='{self.nombre}', precio={self.precio}}}"