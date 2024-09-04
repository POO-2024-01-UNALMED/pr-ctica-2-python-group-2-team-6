# from Entorno.casilla import Casilla
# from Entorno.ciudad import Ciudad
# from Entorno.mesa import Mesa
# from Entorno.zona import Zona
# from Usuario.cliente import Cliente
# from Usuario.trabajador import Trabajador

from utilidad import *

class Restaurante:
    # Atributos de clase
    restaurantes = []
    restaurantes_creados = 0

    def __init__(self, capacidad=0, nombre="", historial_reservas=None, ciudad=None, zona=None, zona_vip=False):
        self.intentos_reserva = []
        self.clientes = []
        self.menu = []
        self.mesas = []
        self.disposicion = []
        self.casillas = []
        self.fechas_disponibles = []
        self.historial_reservas = historial_reservas if historial_reservas is not None else []
        self.parqueadero = [False] * 10
        self.ciudad = ciudad
        self.zona = zona
        self.zona_vip = zona_vip
        self.calificacion = 0.0
        self.coord_x = 0
        self.coord_y = 0
        self.bodega_ingredientes = []
        self.bodega_items = []
        self.reseñas = []
        self.platos_recomendados = []
        self.platos_descuento = []
        self.nombre = nombre
        self.capacidad = capacidad
        self.trabajadores = []
        self.cargamento = None
        self.ganancias = 0
        Restaurante.restaurantes_creados += 1
        Restaurante.restaurantes.append(self)

    # Métodos de clase
    @classmethod
    def get_restaurantes(cls):
        return cls.restaurantes

    # Métodos de instancia
    def get_ganancias(self):
        return self.ganancias

    def set_ganancias(self, ganancias):
        self.ganancias = ganancias

    def get_trabajadores(self):
        return self.trabajadores

    def set_trabajadores(self, trabajadores):
        self.trabajadores = trabajadores

    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def get_clientes(self):
        return self.clientes

    def set_clientes(self, clientes):
        self.clientes = clientes

    def get_fechas_disponibles(self):
        return self.fechas_disponibles

    def set_fechas_disponibles(self, fechas_disponibles):
        self.fechas_disponibles = fechas_disponibles

    def get_historial_reservas(self):
        return self.historial_reservas

    def get_cargamento(self):
        return self.cargamento

    def set_cargamento(self, cargamento):
        self.cargamento = cargamento

    def is_zona_vip(self):
        return self.zona_vip

    def set_zona_vip(self, zona_vip):
        self.zona_vip = zona_vip

    def get_zona(self):
        return self.zona

    def set_zona(self, zona):
        self.zona = zona

    def get_ciudad(self):
        return self.ciudad

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def get_calificacion(self):
        return self.calificacion

    def set_calificacion(self, calificacion):
        self.calificacion = calificacion

    def get_disposicion(self):
        return self.disposicion

    def set_disposicion(self, disposicion):
        self.disposicion = disposicion

    def get_coord_x(self):
        return self.coord_x

    def get_coord_y(self):
        return self.coord_y

    def get_mesas(self):
        return self.mesas

    def get_casillas(self):
        return self.casillas

    def get_menu(self):
        return self.menu

    def set_menu(self, menu):
        self.menu = menu

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def añadir_reseña(self, reseña):
        self.reseñas.append(reseña)

    def agregar_plato_recomendado(self, plato):
        self.platos_recomendados.append(plato)

    def eliminar_plato_recomendado(self, plato):
        self.platos_recomendados.remove(plato)

    def agregar_plato_descuento(self, plato):
        self.platos_descuento.append(plato)

    def eliminar_plato_descuento(self, plato):
        self.platos_descuento.remove(plato)

    def get_platos_recomendados(self):
        return self.platos_recomendados

    def get_platos_descuento(self):
        return self.platos_descuento

    def eliminar_plato(self, plato):
        self.menu.remove(plato)

    def agregar_plato(self, plato):
        self.menu.append(plato)

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def get_parqueadero(self):
        return self.parqueadero

    def get_intentos_reserva(self):
        return self.intentos_reserva

    def añadir_intentos_reserva(self, intento_reserva):
        self.intentos_reserva.append(intento_reserva)

    def get_bodega_ingredientes(self):
        return self.bodega_ingredientes

    def get_bodega_items(self):
        return self.bodega_items

    def actualizar_fechas_disponibles(self):
        total_fechas_disponibles_mesas = []
        for mesa in self.get_mesas():
            total_fechas_disponibles_mesas = intersectar_listas(total_fechas_disponibles_mesas, mesa.get_fechas_disponibles())

        nuevo_array = []
        anio_actual = total_fechas_disponibles_mesas[0][0]
        mes_actual = total_fechas_disponibles_mesas[0][1]
        lista_actual = [anio_actual, mes_actual]

        for fila in total_fechas_disponibles_mesas:
            anio, mes, dia = fila

            if anio != anio_actual or mes != mes_actual:
                nuevo_array.append(lista_actual)
                lista_actual = [anio, mes]
                anio_actual = anio
                mes_actual = mes

            lista_actual.append(dia)

        nuevo_array.append(lista_actual)
        self.set_fechas_disponibles(nuevo_array)

    def __str__(self):
        return (f"{{Información del Restaurante: ciudad={self.ciudad.get_nombre()}, zona={self.zona.get_nombre()}, "
                f"zonaVIP={self.zona_vip}, calificacion={self.calificacion}, mesas={self.mesas}, menu={self.menu}}}")

    def restar_de_bodega_ingrediente(self, indice, cantidad):
        if indice != -1:
            cantidad_pasada = int(self.bodega_ingredientes[indice][1])
            nombre = self.bodega_ingredientes[indice][0]
            self.bodega_ingredientes[indice] = [nombre, str(cantidad_pasada - cantidad)]

    def restar_de_bodega(self, indice, cantidad):
        if indice != -1:
            cantidad_pasada = int(self.bodega_items[indice][1])
            nombre = self.bodega_items[indice][0]
            self.bodega_items[indice] = [nombre, str(cantidad_pasada - cantidad)]