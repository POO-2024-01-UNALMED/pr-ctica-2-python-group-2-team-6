from gestorAplicacion.Usuario.cliente import Cliente
from datetime import date

class Evento:
    eventos = []

    def __init__(self, nombre=None, coste=0, platos=None, tipo_evento=None, cliente_evento=None, fecha=None):
        self.nombre = nombre
        self.coste = coste
        self.platos = platos if platos is not None else []
        self.tipo_evento = tipo_evento
        self.cliente_evento = cliente_evento
        self.fecha = fecha
        Evento.eventos.append(self)

    @classmethod
    def get_eventos(cls):
        return cls.eventos

    @classmethod
    def set_eventos(cls, eventos):
        cls.eventos = eventos

    def set_nombre_evento(self, nombre_evento):
        self.nombre = nombre_evento

    def set_coste(self, coste):
        self.coste = coste

    def set_nombre_motivo(self, nombre_motivo):
        self.nombre_motivo = nombre_motivo

    def set_platos(self, platos):
        self.platos = platos

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    def get_platos(self):
        return self.platos

    def adicionar_plato(self, plato):
        self.platos.append(plato)

    def get_nombre(self):
        return self.nombre

    def get_coste(self):
        return self.coste

    def get_tipo_evento(self):
        return self.tipo_evento

    def set_tipo_evento(self, tipo_evento):
        self.tipo_evento = tipo_evento
