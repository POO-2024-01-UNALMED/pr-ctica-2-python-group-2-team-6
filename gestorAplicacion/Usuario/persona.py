import abc

class Persona(abc.ABC):
    def __init__(self, nombre=None, cedula=None):
        self._nombre = nombre
        self._cedula = cedula

    @abc.abstractmethod
    def mostrar_informacion(self):
        pass

    def despedida(self):
        return f"Hasta luego {self._nombre}.\nEsperamos que regreses pronto."

    def getNombre(self):
        return self._nombre

    def setNombre(self, valor):
        self._nombre = valor
    
    def getCedula(self):
        return self._cedula

    def setCedula(self, valor):
        self._cedula = valor