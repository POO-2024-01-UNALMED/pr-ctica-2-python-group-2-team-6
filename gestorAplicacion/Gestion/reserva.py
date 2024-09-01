from Usuario.cliente import Cliente

class Reserva:
    contador_reservas = 0
    reservas = []

    def __init__(self, clientes=None, fecha=None):
        if clientes is None:
            clientes = []
        if fecha is None:
            fecha = []
        self.clientes = clientes
        self.fecha = fecha
        self.restaurante = None
        self.satisfaccion = False
        self.codigo_reserva = Reserva.contador_reservas
        Reserva.contador_reservas += 1
        Reserva.reservas.append(self)

    def get_codigo_reserva(self):
        return self.codigo_reserva

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_clientes(self):
        return self.clientes

    def set_clientes(self, clientes):
        self.clientes = clientes

    def get_restaurante(self):
        return self.restaurante

    def set_restaurante(self, restaurante):
        self.restaurante = restaurante

    def is_satisfaccion(self):
        return self.satisfaccion

    def set_satisfaccion(self, satisfaccion):
        self.satisfaccion = satisfaccion

    @classmethod
    def get_reservas(cls):
        return cls.reservas

    @classmethod
    def set_reservas(cls, reservas):
        cls.reservas = reservas

    def __str__(self):
        sb = [
            "Información de la reserva:",
            f"\nCiudad: {self.restaurante.get_ciudad().get_nombre()}",
            f"\nZona: {self.restaurante.get_zona().get_nombre()}",
            f"\nRestaurante: {self.restaurante.get_nombre()}",
            f"\nClientes: {self.clientes}",
            f"\nFecha: {self.fecha[2]}/{self.fecha[1]}/{self.fecha[0]}",
            f"\nHora: {self.fecha[3]}:00",
            f"\nMesa: #{self.clientes[0].get_mesa()}",
            f"\nFactura: {self.clientes[0].get_factura()}",
        ]
        return ''.join(sb)