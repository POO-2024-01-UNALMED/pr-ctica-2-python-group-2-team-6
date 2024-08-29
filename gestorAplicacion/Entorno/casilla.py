class Casilla:
    casillas = []
    tipos = ["MESA", "VENTANA", "PUERTA"]

    def __init__(self, tipo=None, coordX=None, coordY=None):
        if tipo is not None and coordX is not None and coordY is not None:
            self.tipo = Casilla.tipos[tipo]
            self.coordX = coordX
            self.coordY = coordY
        else:
            self.tipo = None
            self.coordX = None
            self.coordY = None

        Casilla.casillas.append(self)

    def get_coordX(self):
        return self.coordX

    def get_coordY(self):
        return self.coordY

    def get_tipo(self):
        return self.tipo

    def __str__(self):
        return f"Casilla{{tipo='{self.tipo}', coordX={self.coordX}, coordY={self.coordY}}}"

    @staticmethod
    def get_casillas():
        return Casilla.casillas