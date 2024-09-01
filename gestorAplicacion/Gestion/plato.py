class Plato:
    platos = []
    platos_cumple = []
    vinos_champanas_meeting = []
    platos_varios = []
    gastronomias_japonesa = []
    gastronomias_italiana = []
    gastronomias_marroqui = []
    gastronomias_francesa = []
    platos_gastronomias = []

    def __init__(self, nombre="", precio=0, tipo="", ingredientes=None, cantidad_ingredientes=None,
                 calificacion=0.0, recomendado=False, cantidad_calificaciones=0, veces_pedido=0,
                 pedidos_recomendados=0, porciones=0, cantidad_de_plato=0):
        if ingredientes is None:
            ingredientes = []
        if cantidad_ingredientes is None:
            cantidad_ingredientes = []
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.ingredientes = ingredientes
        self.cantidad_ingredientes = cantidad_ingredientes
        self.calificacion = calificacion
        self.recomendado = recomendado
        self.cantidad_calificaciones = cantidad_calificaciones
        self.veces_pedido = veces_pedido
        self.pedidos_recomendados = pedidos_recomendados
        self.porciones = porciones
        self.cantidad_de_plato = cantidad_de_plato
        Plato.platos.append(self)

    @staticmethod
    def get_ingredientes():
        return self.ingredientes

    @staticmethod
    def set_ingredientes(ingredientes):
        self.ingredientes = ingredientes

    @classmethod
    def get_gastronomias_francesa(cls):
        return cls.gastronomias_francesa

    @classmethod
    def set_gastronomias_francesa(cls, gastronomias_francesa):
        cls.gastronomias_francesa = gastronomias_francesa

    @classmethod
    def get_gastronomias_marroqui(cls):
        return cls.gastronomias_marroqui

    @classmethod
    def set_gastronomias_marroqui(cls, gastronomias_marroqui):
        cls.gastronomias_marroqui = gastronomias_marroqui

    @classmethod
    def get_gastronomias_italiana(cls):
        return cls.gastronomias_italiana

    @classmethod
    def set_gastronomias_italiana(cls, gastronomias_italiana):
        cls.gastronomias_italiana = gastronomias_italiana

    @classmethod
    def get_gastronomias_japonesa(cls):
        return cls.gastronomias_japonesa

    @classmethod
    def set_gastronomias_japonesa(cls, gastronomias_japonesa):
        cls.gastronomias_japonesa = gastronomias_japonesa

    @classmethod
    def get_platos_varios(cls):
        return cls.platos_varios

    @classmethod
    def set_platos_varios(cls, platos_varios):
        cls.platos_varios = platos_varios

    @classmethod
    def get_vinos_champanas_meeting(cls):
        return cls.vinos_champanas_meeting

    @classmethod
    def set_vinos_champanas_meeting(cls, vinos_champanas_meeting):
        cls.vinos_champanas_meeting = vinos_champanas_meeting

    @classmethod
    def get_platos_cumple(cls):
        return cls.platos_cumple

    @classmethod
    def set_platos_cumple(cls, platos_cumple):
        cls.platos_cumple = platos_cumple

    @classmethod
    def get_platos_gastronomias(cls):
        return cls.platos_gastronomias

    @classmethod
    def set_platos_gastronomias(cls, platos_gastronomias):
        cls.platos_gastronomias = platos_gastronomias

    @classmethod
    def get_platos(cls):
        return cls.platos

    @classmethod
    def set_platos(cls, platos):
        cls.platos = platos

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_cantidad_ingredientes(self):
        return self.cantidad_ingredientes

    def get_calificacion(self):
        return self.calificacion

    def set_calificacion(self, calificacion):
        self.calificacion = (self.calificacion + calificacion) / (self.cantidad_calificaciones + 1)
        self.cantidad_calificaciones += 1

    def set_recomendado(self, recomendado):
        self.recomendado = recomendado

    def get_cantidad_calificaciones(self):
        return self.cantidad_calificaciones

    def get_veces_pedido(self):
        return self.veces_pedido

    def set_veces_pedido(self, veces_pedido):
        self.veces_pedido = veces_pedido

    def aumentar_veces_pedido(self):
        self.veces_pedido += 1

    def get_pedidos_recomendados(self):
        return self.pedidos_recomendados

    def get_porciones(self):
        return self.porciones

    def get_cantidad_de_plato(self):
        return self.cantidad_de_plato

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Plato{{nombre='{self.nombre}', precio={self.precio}, ingredientes={self.ingredientes}}}"

    def descontar_plato(self, cantidad_de_plato_pedido):
        if cantidad_de_plato_pedido <= self.get_cantidad_de_plato():
            self.cantidad_de_plato -= cantidad_de_plato_pedido
        else:
            self.cantidad_de_plato = 0