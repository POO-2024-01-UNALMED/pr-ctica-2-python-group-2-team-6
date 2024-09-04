from enum import Enum
from gestorAplicacion.Usuario.persona import Persona

class Tipo(Enum):
    COCINERO = 1
    MESERO = 2

class Trabajador(Persona):
    cocineros = []
    trabajadores = []

    def __init__(self, nombre=None, cedula=None, especialidad=None, salario=0):
        self.nombre = nombre
        self.cedula = cedula
        self.especialidad = especialidad
        self.salario = salario
        self.calificacion = 0.0
        self.reseñas = []
        self.restaurante = None
        self.tipo = None
        self.mesa = None
        self.ganancias_extra = 0

        if self.tipo == Tipo.COCINERO:
            Trabajador.cocineros.append(self)
        Trabajador.trabajadores.append(self)
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Salario: {self.salario}")

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula

    def aumentar_ganancias_extra(self, valor):
        self.ganancias_extra += valor

    def get_tipo(self):
        return self.tipo

    def get_especialidad(self):
        return self.especialidad

    @classmethod
    def get_cocineros(cls):
        return cls.cocineros

    @classmethod
    def set_cocineros(cls, cocineros):
        cls.cocineros = cocineros

    def get_mesa(self):
        return self.mesa

    def set_mesa(self, mesa):
        self.mesa = mesa

    def pago_extra_servicio(self, eventos, especialidad):
        for evento in eventos:
            if evento.get_nombre() == self.get_especialidad():
                self.salario += 40000

    def cocinar(self, pedido):
        platos_cocinados = []
        for plato in pedido.get_platos():
            for ingrediente_cantidad in plato.get_cantidad_ingredientes():  # ["NombreIngrediente", "2"]
                for ingrediente in pedido.get_restaurante().get_bodega_ingredientes():
                    en_bodega_antes = int(ingrediente[1])
                    cantidad_requerida = int(ingrediente_cantidad[1])
                    if cantidad_requerida <= en_bodega_antes:
                        en_bodega_ahora = en_bodega_antes - cantidad_requerida
                        ingrediente[1] = str(en_bodega_ahora)
                        platos_cocinados.append(plato)
        return platos_cocinados