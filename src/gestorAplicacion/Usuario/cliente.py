from gestorAplicacion.Usuario.persona import Persona
from enum import Enum

class Afiliacion(Enum):
    NINGUNA = 1
    ESTRELLITA = 2
    ESTRELLA = 3
    SUPERESTRELLOTA = 4

class Cliente(Persona):
    clientes = []

    def __init__(self, nombre=None, cedula=None, afiliacion=Afiliacion.NINGUNA, placa_vehiculo="Ninguna", factura=None):
        self.nombre = nombre
        self.cedula = cedula
        self.afiliacion = afiliacion
        self.placa_vehiculo = placa_vehiculo
        self.pedido = None
        self.factura = factura
        self.mesa = None
        self.restaurante = None
        self.puntos_acumulados = 0
        self.platos_favoritos = []
        self.reserva = None
        Cliente.clientes.append(self)

    @classmethod
    def get_clientes(cls):
        return cls.clientes
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Afiliación: {self.afiliacion}")
        print(f"Placa del vehículo: {self.placa_vehiculo}")

    @staticmethod
    def despedida(persona):
        persona.despedida()

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula

    @classmethod
    def get_clientes(cls):
        return cls.clientes

    def set_factura(self, factura):
        self.factura = factura

    def get_pedido(self):
        return self.pedido

    def set_pedido(self, pedido):
        self.pedido = pedido

    def get_factura(self):
        return self.factura

    def set_mesa(self, mesa):
        self.mesa = mesa

    def get_mesa(self):
        return self.mesa

    def set_restaurante(self, restaurante):
        self.restaurante = restaurante

    def get_restaurante(self):
        return self.restaurante

    def set_afiliacion(self, afiliacion):
        self.afiliacion = afiliacion

    def get_afiliacion(self):
        return self.afiliacion

    def set_puntos_acumulados(self, puntos_acumulados):
        self.puntos_acumulados = puntos_acumulados

    def get_puntos_acumulados(self):
        return self.puntos_acumulados

    def set_placa_vehiculo(self, placa_vehiculo):
        self.placa_vehiculo = placa_vehiculo

    def get_placa_vehiculo(self):
        return self.placa_vehiculo

    def get_reserva(self):
        return self.reserva

    def set_reserva(self, reserva):
        self.reserva = reserva

    def agregar_plato_favorito(self, plato):
        self.platos_favoritos.append(plato)

    def get_platos_favoritos(self):
        return self.platos_favoritos

    def reset_datos_reserva(self):
        self.restaurante = None
        self.mesa = None
        self.factura = None
        self.reserva = None

    def __str__(self):
        return f"Datos del cliente:\nNombre: {self.nombre}\nCédula: {self.cedula}"

    def es_afiliado(self):
        return self.get_afiliacion() != Afiliacion.NINGUNA