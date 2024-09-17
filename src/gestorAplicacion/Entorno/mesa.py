from gestorAplicacion.Entorno.casilla import Casilla
from gestorAplicacion.Gestion.restaurante import Restaurante
from gestorAplicacion.Gestion.pedido import Pedido
from gestorAplicacion.Usuario.trabajador import Trabajador
from gestorAplicacion.Usuario.cliente import Cliente
from gestorAplicacion.Gestion.factura import Factura
import pickle

class Mesa(Casilla):
    mesas = []
    contador_mesa = 1

    def __init__(self, tipo=None, coord_x=None, coord_y=None, VIP=False, num_asientos=4):
        super().__init__(tipo, coord_x, coord_y)
        self.num_asientos = num_asientos
        self.VIP = VIP
        self.num_mesa = Mesa.contador_mesa
        Mesa.contador_mesa += 1
        self.fechas_disponibles = []
        self.facturas = []
        self.clientes = []
        self.ultima_fecha_reserva = None
        self.restaurante = None
        self.coordenada = [coord_x, coord_y] if coord_x is not None and coord_y is not None else []
        self.distancia_puerta = 9999
        self.distancia_ventana = 9999
        self.valor_total = 0
        self.pedido = None
        self.mesero = None
        Mesa.mesas.append(self)

    @classmethod
    def get_mesas(cls):
        return cls.mesas

    def is_vip(self):
        return self.VIP

    def get_num_mesa(self):
        return self.num_mesa

    def set_restaurante(self, restaurante):
        self.restaurante = restaurante

    def get_restaurante(self):
        return self.restaurante

    def get_clientes(self):
        return self.clientes

    def set_clientes(self, clientes):
        self.clientes = clientes

    def get_facturas(self):
        return self.facturas

    def set_valor_total(self, valor_total):
        self.valor_total = valor_total

    def get_valor_total(self):
        return self.valor_total

    def get_distancia_puerta(self):
        return self.distancia_puerta

    def set_distancia_puerta(self, distancia_puerta):
        self.distancia_puerta = distancia_puerta

    def get_distancia_ventana(self):
        return self.distancia_ventana

    def set_distancia_ventana(self, distancia_ventana):
        self.distancia_ventana = distancia_ventana

    def get_fechas_disponibles(self):
        return self.fechas_disponibles

    def set_fechas_disponibles(self, fechas_disponibles):
        self.fechas_disponibles = fechas_disponibles

    def get_ultima_fecha_reserva(self):
        return self.ultima_fecha_reserva

    def set_ultima_fecha_reserva(self, ultima_fecha_reserva):
        self.ultima_fecha_reserva = ultima_fecha_reserva

    def set_mesero(self, mesero):
        self.mesero = mesero
