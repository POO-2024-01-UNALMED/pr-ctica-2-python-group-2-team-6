class Cargamento:
    cargamentos = []
    UTILIDADES = ["Rosa", "Vela", "Globo Negro", "Globo Blanco", "Globo Dorado", "Globo Rosado", "Globo Azul", "Birrete", "Angel Varon", "Angel Femenino"]

    def __init__(self, proxima_entrega=None, ingredientes=None, frecuencia=0, restaurante=None):
        self.proxima_entrega = proxima_entrega if proxima_entrega is not None else []
        self.ingredientes = ingredientes if ingredientes is not None else []
        self.frecuencia = frecuencia
        self.utilidades = []
        self.restaurante = restaurante
        Cargamento.cargamentos.append(self)

    @classmethod
    def get_cargamentos(cls):
        return cls.cargamentos

    def set_proxima_entrega(self, proxima_entrega):
        self.proxima_entrega = proxima_entrega

    def set_frecuencia(self, frecuencia):
        self.frecuencia = frecuencia

    def get_ingredientes(self):
        return self.ingredientes

    def get_utilidades(self):
        return self.utilidades

    def get_restaurante(self):
        return self.restaurante

    def set_restaurante(self, restaurante):
        self.restaurante = restaurante

    def aumentar_cantidad_ingrediente(self, cantidad_nueva):
        existe = False
        indice_existe = -1
        cantidad = 0
        
        for i, cantidad_actual in enumerate(self.ingredientes):
            if cantidad_actual[0] == cantidad_nueva[0]:
                indice_existe = i
                existe = True
                break

        if existe:
            cantidad = int(self.ingredientes[indice_existe][1])
            cantidad += int(cantidad_nueva[1])
            self.ingredientes[indice_existe][1] = str(cantidad)
        else:
            self.ingredientes.append(cantidad_nueva)