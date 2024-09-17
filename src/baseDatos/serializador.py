import os
import pickle
from gestorAplicacion.Entorno.casilla import Casilla
from gestorAplicacion.Entorno.ciudad import Ciudad
from gestorAplicacion.Entorno.mesa import Mesa
from gestorAplicacion.Entorno.zona import Zona
from gestorAplicacion.Gestion.cargamento import Cargamento
from gestorAplicacion.Gestion.evento import Evento
from gestorAplicacion.Gestion.factura import Factura
from gestorAplicacion.Gestion.ingrediente import Ingrediente
from gestorAplicacion.Gestion.pedido import Pedido
from gestorAplicacion.Gestion.plato import Plato
from gestorAplicacion.Gestion.reserva import Reserva
from gestorAplicacion.Gestion.restaurante import Restaurante
from gestorAplicacion.Usuario.cliente import Cliente
from gestorAplicacion.Usuario.trabajador import Trabajador

class Serializador:

    @staticmethod
    def serializar(lista, nombre):
        try:
            ruta = os.path.join(os.getcwd(), "src/baseDatos/temp", f"{nombre}.txt")
            with open(ruta, 'wb') as file:
                pickle.dump(lista, file)
        except FileNotFoundError as e:
            print(f"El archivo no se encontró: {e}")
        except IOError as e:
            print(f"Error al serializar el objeto: {e}")

    @staticmethod
    def serializar_listas():
        Serializador.serializar(Casilla.get_casillas(), "casillas")
        Serializador.serializar(Ciudad.get_ciudades(), "ciudades")
        Serializador.serializar(Mesa.get_mesas(), "mesas")
        Serializador.serializar(Zona.get_zonas(), "zonas")
        Serializador.serializar(Cargamento.get_cargamentos(), "cargamentos")
        Serializador.serializar(Evento.get_eventos(), "eventos")
        Serializador.serializar(Factura.get_facturas(), "facturas")
        Serializador.serializar(Ingrediente.get_ingredientes(), "ingredientes")
        Serializador.serializar(Pedido.get_pedidos(), "pedidos")
        Serializador.serializar(Plato.get_platos(), "platos")
        Serializador.serializar(Reserva.get_reservas(), "reservas")
        Serializador.serializar(Restaurante.get_restaurantes(), "restaurantes")
        Serializador.serializar(Cliente.get_clientes(), "clientes")
        Serializador.serializar(Trabajador.get_trabajadores(), "trabajadores")
        Serializador.serializar(Trabajador.get_cocineros(), "cocineros")
        Serializador.serializar(Plato.get_gastronomias_francesa(), "Gastronomia Francesa")
        Serializador.serializar(Plato.get_gastronomias_italiana(), "Gastronomia Italiana")
        Serializador.serializar(Plato.get_gastronomias_japonesa(), "Gastronomia Japonesa")
        Serializador.serializar(Plato.get_gastronomias_marroqui(), "Gastronomia Marroquí")
        Serializador.serializar(Plato.get_vinos_champanas_meeting(), "Vinos champañas meetings")
        Serializador.serializar(Plato.get_platos_cumple(), "Platos del cumpleaños")
