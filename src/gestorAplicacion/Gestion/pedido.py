from gestorAplicacion.Usuario.cliente import Cliente
from gestorAplicacion.Usuario.trabajador import Trabajador

class Pedido:
    pedidos = []

    def __init__(self, cliente=None, restaurante=None, mesero=None):
        self.platos = []
        self.cliente = cliente
        self.restaurante = restaurante
        self.mesero = mesero
        Pedido.pedidos.append(self)

    def agregar_plato(self, plato):
        if isinstance(plato, list):
            for p in plato:
                self.platos.append(p)
        else:
            self.platos.append(plato)

    def get_platos(self):
        return self.platos

    def set_platos(self, platos):
        self.platos = platos

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    @classmethod
    def get_pedidos(cls):
        return cls.pedidos

    def get_restaurante(self):
        return self.restaurante

    def set_restaurante(self, restaurante):
        self.restaurante = restaurante

    def get_mesero(self):
        return self.mesero

    def set_mesero(self, mesero):
        self.mesero = mesero

    def __str__(self):
        sb = "productos\n"
        for p in self.platos:
            sb += f"{p.get_nombre()}   $ {p.get_precio()}\n"
        return sb