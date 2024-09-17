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

class Deserializador:

    @staticmethod
    def deserializar(lista, nombre):
        try:
            path = os.path.join(os.getcwd(), "src/baseDatos/temp", f"{nombre}.txt")
            with open(path, 'rb') as file:
                lista.extend(pickle.load(file))
        except FileNotFoundError as e:
            print(f"Archivo no encontrado: {e}")
        except IOError as e:
            print(f"Error de IO: {e}")
        except pickle.UnpicklingError as e:
            print(f"Error deserializando objeto: {e}")

    @staticmethod
    def deserializar_listas():
        Deserializador.deserializar(Casilla.get_casillas(), "casillas")
        Deserializador.deserializar(Ciudad.get_ciudades(), "ciudades")
        Deserializador.deserializar(Mesa.get_mesas(), "mesas")
        Deserializador.deserializar(Zona.get_zonas(), "zonas")
        Deserializador.deserializar(Cargamento.get_cargamentos(), "cargamentos")
        Deserializador.deserializar(Evento.get_eventos(), "eventos")
        Deserializador.deserializar(Factura.get_facturas(), "facturas")
        Deserializador.deserializar(Ingrediente.get_ingredientes(), "ingredientes")
        Deserializador.deserializar(Pedido.get_pedidos(), "pedidos")
        Deserializador.deserializar(Plato.get_platos(), "platos")
        Deserializador.deserializar(Reserva.get_reservas(), "reservas")
        Deserializador.deserializar(Restaurante.get_restaurantes(), "restaurantes")
        Deserializador.deserializar(Cliente.get_clientes(), "clientes")
        Deserializador.deserializar(Trabajador.get_trabajadores(), "trabajadores")
        Deserializador.deserializar(Trabajador.get_cocineros(), "cocineros")
        Deserializador.deserializar(Plato.get_gastronomias_francesa(), "Gastronomia Francesa")
        Deserializador.deserializar(Plato.get_gastronomias_italiana(), "Gastronomia Italiana")
        Deserializador.deserializar(Plato.get_gastronomias_japonesa(), "Gastronomia Japonesa")
        Deserializador.deserializar(Plato.get_gastronomias_marroqui(), "Gastronomia Marroquí")
        Deserializador.deserializar(Plato.get_vinos_champanas_meeting(), "Vinos champañas meetings")
        Deserializador.deserializar(Plato.get_platos_cumple(), "Platos del cumpleaños")
