class Factura:
    facturas = []
    numero_factura = 0

    def __init__(self, pedido=None, valor=0, metodo_pago=None, pago_preconsumo=False, propina=0, pagada=False, evento=None):
        self.evento = evento
        self.valor = valor
        self.metodo_pago = metodo_pago
        self.pago_preconsumo = pago_preconsumo
        self.pedido = pedido
        self.propina = propina
        self.pagada = pagada
        Factura.numero_factura += 1
        Factura.facturas.append(self)

    @classmethod
    def crear_factura_unificada(cls, facturas):
        valor_total = sum(factura.calcular_valor() for factura in facturas)
        return cls(valor=valor_total, propina=0, pagada=False)

    @classmethod
    def get_facturas(cls):
        return cls.facturas

    def pagar(self):
        self.pagada = True

    def set_metodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago

    def set_pago_preconsumo(self, pago_preconsumo):
        self.pago_preconsumo = pago_preconsumo

    def set_valor(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def get_metodo_pago(self):
        return self.metodo_pago

    def get_pedido(self):
        return self.pedido

    def set_evento(self, evento):
        self.evento = evento

    def get_evento(self):
        return self.evento

    def aumentar_valor(self, valor):
        self.valor += valor

    def calcular_valor(self, ):
        valor = 0
        for plato in self.pedido.platos:
            valor += plato.precio
        if self.pago_preconsumo:
            valor += int(valor * 0.19)
        valor += self.propina
        self.set_valor(valor)
        return valor

    def __str__(self):
        return f"Número factura: {Factura.numero_factura}"