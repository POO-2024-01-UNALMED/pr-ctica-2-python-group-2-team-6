from utilidad import Utilidad

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
from gestorAplicacion.Usuario.persona import Persona
from gestorAplicacion.Usuario.trabajador import Trabajador
import datetime
from datetime import datetime
import random
# from utilidad import Utilidad

# from gestorAplicacion.Entorno.casilla import Casilla
# from gestorAplicacion.Entorno.ciudad import Ciudad
# from gestorAplicacion.Entorno.mesa import Mesa
# from gestorAplicacion.Entorno.zona import Zona
# from gestorAplicacion.Gestion.cargamento import Cargamento
# from gestorAplicacion.Gestion.evento import Evento
# from gestorAplicacion.Gestion.factura import Factura
# from gestorAplicacion.Gestion.ingrediente import Ingrediente
# from gestorAplicacion.Gestion.pedido import Pedido
# from gestorAplicacion.Gestion.plato import Plato
# from gestorAplicacion.Gestion.reserva import Reserva
# from gestorAplicacion.Gestion.restaurante import Restaurante
# from gestorAplicacion.Usuario.cliente import Cliente
# from gestorAplicacion.Usuario.persona import Persona
# from gestorAplicacion.Usuario.trabajador import Trabajador
# import datetime
# from datetime import datetime
# import random

#Funcionalidad 1
#Interacción 1
def reservarMesa():
    encendido1 = True
    while encendido1:
        print("""
                ¿Desea reservar una mesa?
                1. Sí.
                2. No.
                Escriba un número para elegir su opción.""")
        eleccion1 = Utilidad.readInt()

        if eleccion1 == 1:
            # Utilidad.limpiar_pantalla()
            print("Ciudades:")
            Utilidad.listado_ciudades()
            print("Escriba un número para elegir la ciudad.\nEn caso de no encontrar la ciudad requerida escriba 0.")
            eleccion2 = Utilidad.readInt()

            if eleccion2 > len(Ciudad.get_ciudades()) or eleccion2 < 0:
                print(f"Ingrese un número válido [1 - {len(Ciudad.get_ciudades())}].")
            else:
                # Utilidad.limpiar_pantalla()
                if eleccion2 != 0:
                    ciudad = Ciudad.get_ciudades()[eleccion2 - 1]
                    if not ciudad.get_restaurantes():
                        print("Esta ciudad no tiene restaurantes.")
                        reservarMesa()
                    else:
                        encendido2 = True
                        while encendido2:
                            # Utilidad.limpiar_pantalla()
                            print(f"Zonas de {ciudad.get_nombre()}:")
                            zonas_con_restaurante = Utilidad.listado_zonas_con_restaurante_ciudad(ciudad)
                            print("Escriba un número para elegir la zona.")
                            eleccion3 = Utilidad.readInt()

                            if eleccion3 > len(zonas_con_restaurante) or eleccion3 < 1:
                                print(f"Ingrese un número válido [1 - {len(zonas_con_restaurante)}].")
                            else:
                                # Utilidad.limpiar_pantalla()
                                zona = zonas_con_restaurante[eleccion3 - 1]
                                encendido3 = True
                                while encendido3:
                                    # Utilidad.limpiar_pantalla()
                                    print(f"Restaurantes de {zona.get_nombre()}:")
                                    Utilidad.listado_restaurantes_zona(zona)
                                    print("Escriba un número para elegir el restaurante.")
                                    eleccion4 = Utilidad.readInt()

                                    if eleccion4 > len(zona.get_restaurantes()) or eleccion4 < 1:
                                        print(f"Ingrese un número válido [1 - {len(zona.get_restaurantes())}].")
                                    else:
                                        cliente = seleccionMesa(zona.get_restaurantes()[eleccion4 - 1])
                                        restaurante = extras_reserva(cliente)
                                        pago_anticipado(restaurante)
                                        encendido3 = False
                                encendido2 = False
                else:
                    print("Lo sentimos, pero estas son las únicas ciudades donde tenemos restaurantes de nuestra cadena.")
                    print("""
                            ¿Desea elegir otra ciudad?
                            1. Sí.
                            2. No.
                            Escriba un número para elegir su opción.""")
                    eleccion4 = Utilidad.readInt()
                    if eleccion4 == 1:
                        reservarMesa()
                    else:
                        pass
                        # menu_principal()
                encendido1 = False
        elif eleccion1 == 2:
            # Utilidad.limpiar_pantalla()
            # menu_principal()
            encendido1 = False
        else:
            # Utilidad.limpiar_pantalla()
            print("Ingrese un número válido [1 - 2].")

def seleccionMesa(restaurante):
    clientes = []
    print("Ingrese el nombre del cliente:")
    nombre = input().capitalize()
    print("Ingrese la cédula del cliente:")
    cedula = Utilidad.readInt()
    print("Ingrese la placa del vehículo del cliente (en caso de no tener escribir 0):")
    placa_vehiculo = input()
    cliente = Cliente(nombre, cedula, placa_vehiculo, Factura())

    if Utilidad.existe_cliente(cliente):
        cliente = Utilidad.cliente_cedula(cliente)
    else:
        restaurante.get_clientes().append(cliente)
    
    clientes.append(cliente)

    print("Ingrese la cantidad de acompañantes del cliente:")
    print("Ingrese la cantidad de acompañantes. No debe ser mayor a 6.\nEn caso de ingresar un número mayor a 6, este será ignorado y se establecerá en 6.")
    num_acompanantes = Utilidad.readInt()
    
    if num_acompanantes > 0:
        num_acompanantes = min(num_acompanantes, 6)
        for i in range(num_acompanantes):
            print(f"Ingrese el nombre del acompañante #{i + 1}:")
            nombre_acompanante = input()
            print(f"Ingrese la cédula del acompañante #{i + 1}:")
            cedula_acompanante = Utilidad.readInt()
            acompanante = Cliente(nombre_acompanante, cedula_acompanante)
            if Utilidad.existe_cliente(acompanante):
                acompanante = Utilidad.cliente_cedula(acompanante)
            else:
                restaurante.get_clientes().append(acompanante)
            clientes.append(acompanante)

    for cliente1 in clientes:
        cliente1.set_restaurante(restaurante)

    tipo_mesa = False
    print("¿Qué tipo de mesa quiere usar?\n1. Estándar.\n2. VIP.")
    eleccion1 = Utilidad.readInt()
    
    if eleccion1 == 1:
        if not any(mesa.is_vip() == tipo_mesa for mesa in restaurante.get_mesas()):
            print("Lo sentimos, pero no hay mesas estándar, la mesa tendrá que ser VIP.")
            tipo_mesa = True
    elif eleccion1 == 2:
        tipo_mesa = True
        if not any(mesa.is_vip() == tipo_mesa for mesa in restaurante.get_mesas()):
            print("Lo sentimos, pero no hay mesas VIP, la mesa tendrá que ser estándar.")
            tipo_mesa = False
    else:
        print("Debido a que ingresó un dato erróneo se le asignó una mesa estándar.")

    mesas_elegidas = []
    print("Tiene preferencia por estar cerca de:\n1. Puerta.\n2. Ventana.\n3. Ninguna.")
    eleccion2 = Utilidad.readInt()

    if eleccion2 in [1, 2]:
        mesas_elegidas = Utilidad.calcular_distancia(restaurante, eleccion2, tipo_mesa)
    elif eleccion2 == 3:
        for mesa in restaurante.get_mesas():
            mesa.set_distancia_puerta(0)
            mesa.set_distancia_ventana(0)
    else:
        print("Debido a que ingresó un dato erróneo se asume que no tiene ninguna preferencia.")

    encendido1 = True
    while encendido1:
        fecha_elegida = seleccionFecha(restaurante, tipo_mesa, mesas_elegidas)
        Utilidad.limpiar_pantalla()
        print(f"Mesas disponibles para el día {fecha_elegida[2]}/{fecha_elegida[1]}/{fecha_elegida[0]}:")

        mesas_disponibles = []
        for mesa in restaurante.get_mesas():
            for fecha in mesa.get_fechas_disponibles():
                if (fecha[0] == fecha_elegida[0] and fecha[1] == fecha_elegida[1] and
                        fecha[2] == fecha_elegida[2] and mesa.is_vip() == tipo_mesa and len(fecha) > 3):
                    print(f"Mesa #{mesa.get_num_mesa()}")

        if mesas_elegidas:
            print("Según sus preferencias se le recomienda elegir las mesas con el número:")
            for num_mesa in mesas_elegidas:
                print(f"#{num_mesa}")

        print("¿Alguna de las mesas disponibles le es conveniente?\n1. Sí.\n2. No.")
        eleccion4 = Utilidad.readInt()

        if eleccion4 == 1:
            print("Ingrese el número de la mesa de su preferencia.")
            num_mesa = Utilidad.readInt()
            mesa_elegida = next((mesa for mesa in restaurante.get_mesas() if mesa.get_num_mesa() == num_mesa), None)

            if not mesa_elegida:
                print("Ingresó un número inválido. Se le asignará una mesa aleatoria.")
                mesa_elegida = next(mesa for mesa in restaurante.get_mesas() if mesa.get_num_mesa() == mesas_elegidas[0])

            Utilidad.limpiar_pantalla()
            indice_fecha_elegida = next(i for i, fecha in enumerate(mesa_elegida.get_fechas_disponibles())
                                        if fecha[1] == fecha_elegida[1] and fecha[2] == fecha_elegida[2])

            mesa_elegida.set_ultima_fecha_reserva(indice_fecha_elegida)

            print("Horarios disponibles para la mesa seleccionada:")
            for i in range(3, len(mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida])):
                print(f"{i-2}. {mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida][i]}:00.")

            print("¿Alguno de los horarios disponibles le es conveniente?\n1. Sí.\n2. No.")
            eleccion5 = Utilidad.readInt()

            if eleccion5 == 1:
                encendido2 = True
                while encendido2:
                    print(f"Ingrese el horario de su preferencia. [1 - {len(mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida]) - 3}].")
                    hora_elegida = Utilidad.readInt()

                    if hora_elegida < 1 or hora_elegida > len(mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida]) - 3:
                        print(f"Ingrese un número válido [1 - {len(mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida]) - 3}].")
                    else:
                        fecha_elegida.append(mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida][hora_elegida + 2])
                        reserva = Reserva(clientes, fecha_elegida)
                        reserva.set_restaurante(restaurante)
                        mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida].pop(hora_elegida + 2)
                        restaurante.get_historial_reservas().append(reserva)

                        for cliente1 in clientes:
                            cliente1.set_reserva(reserva)
                            cliente1.set_mesa(mesa_elegida)
                            cliente1.set_factura(Factura(Pedido()))

                        print(f"Mesa Elegida: {mesa_elegida.get_fechas_disponibles()}")
                        print(restaurante.get_historial_reservas())
                        print("Su reserva ha sido exitosa")
                        encendido1 = False
                        encendido2 = False
            else:
                print("¿Desea elegir una fecha diferente?\n1. Sí.\n2. No.")
                seguir1 = Utilidad.readInt()
                if seguir1 != 1:
                    encendido1 = False
        else:
            print("¿Desea elegir una fecha diferente?\n1. Sí.\n2. No.")
            seguir2 = Utilidad.readInt()
            if seguir2 != 1:
                encendido1 = False

    print(restaurante)
    return cliente

def seleccionFecha(restaurante, tipo_mesa, mesas_elegidas):
    elecciones = []
    anios = []
    meses = []

    for fechas_mes in restaurante.get_fechas_disponibles():
        if fechas_mes[0] not in anios:
            anios.append(fechas_mes[0])

    print("Años disponibles:")
    for i, anio in enumerate(anios):
        print(f"{i + 1}. {anio}.")

    print(f"Escriba un número para elegir su opción [1 - {len(anios)}].")
    eleccion1 = Utilidad.readInt()

    encendido2 = True
    while encendido2:
        print("Meses disponibles:")
        i = 1
        for fechas_mes in restaurante.get_fechas_disponibles():
            if anios[eleccion1 - 1] == fechas_mes[0]:
                print(f"{i}. {fechas_mes[1]}.")
                meses.append(fechas_mes[1])
                i += 1

        print(f"Escriba un número para elegir su opción [1 - {i - 1}].")
        eleccion2 = Utilidad.readInt()

        if 1 <= eleccion2 <= len(meses):
            encendido2 = False
        else:
            print("Ingrese un número válido")

    encendido3 = True
    indice_mes = 0
    while encendido3:
        print("Días disponibles:")
        for i, fechas in enumerate(restaurante.get_fechas_disponibles()):
            if meses[eleccion2 - 1] == fechas[1]:
                indice_mes = i
                break

        for i in range(2, len(restaurante.get_fechas_disponibles()[indice_mes])):
            print(f"{i - 1}. {restaurante.get_fechas_disponibles()[indice_mes][i]}.")

        print(f"Escriba un número para elegir su opción [1 - {len(restaurante.get_fechas_disponibles()[indice_mes]) - 2}].")
        eleccion3 = Utilidad.readInt()

        if 1 <= eleccion3 <= len(restaurante.get_fechas_disponibles()[indice_mes]) - 2:
            encendido3 = False
        else:
            print("Ingrese un número válido")

    elecciones.extend([anios[eleccion1 - 1], meses[eleccion2 - 1], restaurante.get_fechas_disponibles()[indice_mes][eleccion3 + 1]])
    print(elecciones)
    return elecciones

def extras_reserva(cliente):
    restaurante = cliente.get_restaurante()
    print("Desde la cadena de restaurantes ofrecemos los servicios de reserva de parqueadero y decoraciones para la mesa. Elija un servicio en caso de necesitarlo:")
    print("1. Reserva de Parqueadero.\n2. Decoraciones para la mesa.\n3. No desea ningún servicio extra.")
    eleccion = Utilidad.read_int()

    if eleccion == 1:
        print("Reserva de Parqueadero")
        placa = ""
        cargo_extra1 = 0
        if cliente.get_afiliacion() == Cliente.Afiliacion.NINGUNA:
            print("El servicio tiene un coste de $10.000. ¿Desea reservar el parqueadero?\n1. Sí.\n2. No.")
            eleccion2 = Utilidad.read_int()
            if eleccion2 == 1:
                cargo_extra1 = 10000
                indice_celda = restaurante.get_parqueadero().index(False)
                print(f"Su celda de parqueo es la número: #{indice_celda + 1}")
                if cliente.get_placa_vehiculo() == "Ninguna":
                    print("Ingrese la placa del vehículo:")
                    placa = Utilidad.read_string()
                    cliente.set_placa_vehiculo(placa)
                else:
                    placa = cliente.get_placa_vehiculo()
                print(f"Parqueadero reservado con éxito para el vehículo con placa: {placa}.")
            else:
                extras_reserva(cliente)
        else:
            if cliente.get_placa_vehiculo() == "Ninguna":
                print("Ingrese la placa del vehículo:")
                placa = Utilidad.read_string()
                cliente.set_placa_vehiculo(placa)
            else:
                placa = cliente.get_placa_vehiculo()
            for i in range(len(restaurante.get_parqueadero())):
                if not restaurante.get_parqueadero()[i]:
                    print(f"Parqueadero reservado con éxito para el vehículo con placa: {placa}.")
                    break
            print("Parqueadero reservado con éxito.")
        cliente.get_factura().aumentar_valor(cargo_extra1)

    elif eleccion == 2:
        print("Decoraciones para la mesa")
        if cliente.get_afiliacion() != Cliente.Afiliacion.NINGUNA:
            print("Obtuvo un 15% de descuento en las decoraciones para mesa. El costo es de $42.500")
        else:
            print("El costo de las decoraciones es de $50.000")
        print("¿Desea decorar la mesa?\n1. Sí.\n2. No.")
        eleccion3 = Utilidad.read_int()
        if eleccion3 == 1:
            encendido1 = False
            while not encendido1:
                cargo_extra2 = 0
                print("Disponemos de los siguientes paquetes de decoración:\n1. Cena romántica (30000$).\n2. Graduación (1200$ + 5000$ por cada comensal).\n3. Descubrimiento (1200$ + 6000$ por cada comensal).")
                eleccion4 = Utilidad.read_int()
                if eleccion4 == 1:
                    restaurante.restar_de_bodega(Utilidad.indice_bodega_items("rosa", restaurante), 1)
                    restaurante.restar_de_bodega(Utilidad.indice_bodega_items("vela", restaurante), 3)
                    restaurante.restar_de_bodega_ingrediente(Utilidad.indice_bodega_ingredientes("vino blanco", restaurante), 1)
                    cargo_extra2 = 30000
                elif eleccion4 == 2:
                    restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo negro", restaurante), 3)
                    restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo dorado", restaurante), 3)
                    restaurante.restar_de_bodega(Utilidad.indice_bodega_items("birrete", restaurante), cliente.get_mesa().get_clientes().size())
                    cargo_birretes = 5000 * cliente.get_mesa().get_clientes().size()
                    cargo_extra2 = 1200 + cargo_birretes
                elif eleccion4 == 3:
                    print("Seleccione el género del bebé:\n1. Niño.\n2. Niña.")
                    eleccion5 = Utilidad.read_int()
                    if eleccion5 == 1:
                        restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo azul", restaurante), 3)
                        restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo blanco", restaurante), 3)
                        restaurante.restar_de_bodega(Utilidad.indice_bodega_items("angel varon", restaurante), cliente.get_mesa().get_clientes().size())
                    else:
                        restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo rosado", restaurante), 3)
                        restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo blanco", restaurante), 3)
                        restaurante.restar_de_bodega(Utilidad.indice_bodega_items("angel femenino", restaurante), cliente.get_mesa().get_clientes().size())
                    cargo_angeles = 6000 * cliente.get_mesa().get_clientes().size()
                    cargo_extra2 = 1200 + cargo_angeles
                else:
                    print("Ingrese un dato válido [1 - 3]")
                    encendido1 = True

                cliente.get_factura().aumentar_valor(cargo_extra2)
                print(cliente.get_factura())
        else:
            extras_reserva(cliente)

    elif eleccion == 3:
        print("No desea ningún servicio extra.")

    else:
        print("Ingrese un número válido.")
        extras_reserva(cliente)

    return restaurante


def pago_anticipado(restaurante):
    reserva = restaurante.get_historial_reservas()[-1]
    clientes = reserva.get_clientes()
    factura = clientes[0].get_factura()

    print("¿Desea pagar ya mismo su reserva?\n1. Sí.\n2. No.")
    eleccion1 = Utilidad.read_int()

    if eleccion1 == 1:
        if clientes[0].get_afiliacion() == Cliente.Afiliacion.NINGUNA:
            print("¿Desea afiliarse al restaurante? Hacerlo le daría un descuento extra por ser un nuevo socio\n1. Sí.\n2. No.")
            eleccion2 = Utilidad.read_int()
            if eleccion2 == 1:
                factura.aumentar_valor(13500)  # Aplicar 10% de descuento al valor de la reserva.
                pagar_reserva(restaurante, reserva, clientes, factura)
            else:
                factura.aumentar_valor(15000)
                pagar_reserva(restaurante, reserva, clientes, factura)
        else:
            factura.set_valor(14300)  # Aplicar 5% de descuento al valor de la reserva.
            pagar_reserva(restaurante, reserva, clientes, factura)
        clientes[0].get_factura().set_pago_preconsumo(True)

    else:
        factura.aumentar_valor(15000)
        print("Al realizar el pago postconsumo se solicitará una propina porcentual obligatoria.")
        print("¿Teniendo esto en cuenta, desea continuar sin realizar el pago?\n1. Sí.\n2. No.")
        eleccion6 = Utilidad.read_int()
        if eleccion6 == 1:
            confirmar_reserva(restaurante, reserva, clientes)
        else:
            pago_anticipado(restaurante)


def pagar_reserva(restaurante, reserva, clientes, factura):
    if confirmar_reserva(restaurante, reserva, clientes):
        escoger_metodo_pago(clientes[0])
        encendido1 = True
        while encendido1:
            factura.calcular_valor()
            print(f"¿Desea confirmar la transacción con un valor de: {factura.get_valor()}?")
            print("1. Sí.\n2. No.\nEscriba un número para elegir su opción.")
            eleccion3 = Utilidad.read_int()
            if eleccion3 == 1:
                print("Transacción confirmada.")
                clientes[0].get_factura().set_valor(0)
                encendido1 = False
            else:
                encendido1 = False
                print("Ingrese un valor válido [1 - 2].")

def confirmar_reserva(restaurante, reserva, clientes):
    confirmada = False
    fecha_intento = datetime.now()
    restaurante.get_intentos_reserva().append([fecha_intento.get_year(), fecha_intento.get_month_value(), fecha_intento.get_day_of_month()])
    
    print("Resumen de su reserva:")
    print(reserva)
    print("¿Desea confirmar su reserva?\n1. Sí.\n2. No.")
    eleccion1 = Utilidad.read_int()

    if eleccion1 == 1:
        confirmada = True
        print("Reserva confirmada.")
        print(f"Su código de reserva es: {reserva.get_codigo_reserva()}")
    else:
        print("Reserva cancelada.")
        mesa_reserva = clientes[0].get_mesa()
        fecha_reserva = mesa_reserva.get_fechas_disponibles()[mesa_reserva.get_ultima_fecha_reserva()]
        fecha_reserva.append(reserva.get_fecha()[3])
        mesa_reserva.set_clientes(None)
        mesa_reserva.set_ultima_fecha_reserva(0)
        for cliente in clientes:
            cliente.reset_datos_reserva()
        restaurante.get_historial_reservas().remove(reserva)

    return confirmada

##Funcionalidad 2 

##Cuerpo de la funcionalidad

def ordenar_comida():
    encendido1 = True
    while encendido1:
        print("""
            ¿Desea ordenar comida?
            1. Sí.
            2. No.
            Escriba un número para elegir su opción.""")
        
        eleccion1 = Utilidad.readInt()
        if eleccion1 == 1:
            # Utilidad.limpiar_pantalla()
            print("Ciudades:")
            Utilidad.listado_ciudades()
            print("Escriba un número para elegir la ciudad.\nEn caso de no encontrar la ciudad requerida escriba 0.")
            eleccion2 = Utilidad.readInt()
            
            if eleccion2 > len(Ciudad.get_ciudades()) or eleccion2 < 0:
                print(f"Ingrese un número válido [1 - {len(Ciudad.get_ciudades())}].")
            else:
                # Utilidad.limpiar_pantalla()
                if eleccion2 != 0:  # Si se encuentra la ciudad
                    ciudad = Ciudad.get_ciudades()[eleccion2 - 1]
                    if not ciudad.get_restaurantes():  # Si la ciudad no tiene restaurantes
                        print("Esta ciudad no tiene restaurantes.")
                        ordenar_comida()
                    else:  # Si la ciudad tiene zonas
                        encendido2 = True
                        while encendido2:
                            # Utilidad.limpiar_pantalla()
                            print(f"Zonas de {ciudad.get_nombre()}:")
                            zonas_con_restaurante = Utilidad.listado_zonas_con_restaurante_ciudad(ciudad)
                            print("Escriba un número para elegir la zona.")
                            eleccion3 = Utilidad.readInt()
                            
                            if eleccion3 > len(zonas_con_restaurante) or eleccion3 < 1:  # Si no se encuentra la zona
                                print(f"Ingrese un número válido [1 - {len(zonas_con_restaurante)}].")
                            else:  # Si se encuentra la zona
                                # Utilidad.limpiar_pantalla()
                                zona = zonas_con_restaurante[eleccion3 - 1]
                                encendido3 = True
                                while encendido3:
                                    # Utilidad.limpiar_pantalla()
                                    print(f"Restaurantes de {zona.get_nombre()}:")
                                    Utilidad.listado_restaurantes_zona(zona)
                                    print("Escriba un número para elegir el restaurante.")
                                    eleccion4 = Utilidad.readInt()
                                    
                                    if eleccion4 > len(zona.get_restaurantes()) or eleccion4 < 1:  # Si no se encuentra el restaurante
                                        print(f"Ingrese un número válido [1 - {len(zona.get_restaurantes())}].")
                                    else:  # Si se encuentra el restaurante
                                        # Interacción #1
                                        clientes = establecer_cliente(zona.get_restaurantes()[eleccion4 - 1])
                                        pedidos = hacer_comida(clientes)
                                        asignar_factura(pedidos)
                                        encendido3 = False
                                encendido2 = False
                else:  # Si no se encuentra la ciudad
                    print("Lo sentimos, pero estas son las únicas ciudades donde tenemos restaurantes de nuestra cadena.")
                    print("""
                        ¿Desea elegir otra ciudad?
                        1. Sí.
                        2. No.
                        Escriba un número para elegir su opción.""")
                    eleccion4 = Utilidad.readInt()
                    
                    if eleccion4 == 1:
                        ordenar_comida()
                    else:
                        # menu_principal()
                        pass
                encendido1 = False
        elif eleccion1 == 2:
            # Utilidad.limpiar_pantalla()
            # menu_principal()
            encendido1 = False
        else:
            # Utilidad.limpiar_pantalla()
            print("Ingrese un número válido [1 - 2].")

##Interacción 1

def establecer_cliente(restaurante):
    clientes = []
    print("Ingrese el número de cédula de la persona que desea ordenar:")
    cedula = Utilidad.readInt()
    cliente = Cliente(cedula)

    existe_cliente = Utilidad.existe_cliente(cliente)

    if existe_cliente:
        nuevo_cliente = Utilidad.cliente_cedula(cliente)
        print(nuevo_cliente)
        if nuevo_cliente == cliente:  # Si el cliente no tiene reserva
            print(f"El cliente con cédula {cedula} no está registrado en el restaurante indicado.")
            print("Para continuar tendrá que brindarnos algunos datos adicionales.")
            print("Ingrese el nombre del cliente:")
            nombre = input().capitalize()
            cliente.set_nombre(nombre)
            clientes.append(cliente)
            restaurante.get_clientes().append(cliente)
            cliente.set_restaurante(restaurante)
            mesa = Mesa()
            for mesa_restaurante in restaurante.get_mesas():
                if not mesa_restaurante.get_clientes():
                    cliente.set_mesa(mesa_restaurante)
                    mesa_restaurante.set_clientes([cliente])
                    mesa = mesa_restaurante
            clientes = mesa.get_clientes()

        else:  # Si el cliente tiene reserva
            encendido1 = True
            mesa = Mesa()
            while encendido1:
                print("Ingrese el código de reserva:")
                codigo_reserva = Utilidad.readInt()
                for reserva in restaurante.get_historial_reservas():
                    if reserva.get_codigo_reserva() == codigo_reserva:
                        nuevo_cliente.set_reserva(reserva)
                        clientes.append(nuevo_cliente)
                        mesa = nuevo_cliente.get_mesa()
                        mesa.set_clientes(clientes)
                        print(f"Por favor diríjase a la mesa {mesa.get_num_mesa()}.")
                        encendido1 = False
                        break
                if not encendido1:
                    continue
                else:
                    print("El código de reserva ingresado no es válido.")
                    print("Por favor, ingrese un código de reserva válido.")
    
            clientes = mesa.get_clientes()

    else:
        mesa = Mesa()
        print(f"El cliente con cédula {cedula} no está registrado en ningún restaurante.")
        print("Para continuar tendrá que brindarnos algunos datos adicionales.")
        print("Ingrese el nombre del cliente:")
        nombre = input().capitalize()
        cliente.set_nombre(nombre)
        clientes.append(cliente)
        Cliente.get_clientes().append(cliente)
        restaurante.get_clientes().append(cliente)
        cliente.set_restaurante(restaurante)
        for mesa_restaurante in restaurante.get_mesas():
            if not mesa_restaurante.get_clientes():
                cliente.set_mesa(mesa_restaurante)
                mesa_restaurante.set_clientes([cliente])
                mesa = mesa_restaurante
    
        clientes = mesa.get_clientes()

    print(len(clientes))
    return clientes

##Interacción 2

def hacer_comida(clientes):
    # Utilidad.limpiar_pantalla()

    trabajadores = clientes[0].get_restaurante().get_trabajadores()

    # Buscar Trabajador especialidad Cocinero, especialidad Mesero
    cocinero = None
    mesero = None

    for trabajador in trabajadores:
        if trabajador.get_tipo() == Trabajador.Tipo.COCINERO:
            cocinero = trabajador
        if trabajador.get_tipo() == Trabajador.Tipo.MESERO:
            mesero = trabajador

    mesero.set_mesa(clientes[0].get_mesa())
    clientes[0].get_mesa().set_mesero(mesero)

    pedido_dummy = Pedido()

    pedidos = hacer_pedido(mesero.get_mesa().get_clientes(), pedido_dummy)

    for pedido in pedidos:
        pedido.set_mesero(mesero)
        pedido.set_restaurante(clientes[0].get_restaurante())

        platos_cocinados = cocinero.cocinar(pedido)

        if len(platos_cocinados) != len(pedido.get_platos()):
            print("Algun(os) plato(s) del pedido no ha(n) podido ser cocinado(s) debido a la falta de ingredientes")
            print("Se le descontará de la factura.")
            pedido.set_platos(platos_cocinados)

    return pedidos

def platos_menu(tipo, cliente):
    platos = []
    pedido = Pedido()
    if tipo == "Entrada":
        print("Entradas Disponibles\n")
        for plato in cliente.get_restaurante().get_menu():
            if plato.get_tipo() == "Entrada":
                platos.append(plato)
    elif tipo == "Plato fuerte":
        print("Platos fuertes Disponibles\n")
        for plato in cliente.get_restaurante().get_menu():
            if plato.get_tipo() == "Plato Fuerte":
                platos.append(plato)
    elif tipo == "Bebida":
        print("Bebidas Disponibles\n")
        for plato in cliente.get_restaurante().get_menu():
            if plato.get_tipo() == "Bebida":
                platos.append(plato)
    elif tipo == "Postre":
        print("Postres Disponibles\n")
        for plato in cliente.get_restaurante().get_menu():
            if plato.get_tipo() == "Postre":
                platos.append(plato)
    elif tipo == "Infantil":
        print("Menú infantil\n")
        for plato in cliente.get_restaurante().get_menu():
            if plato.get_tipo() == "Infantil":
                platos.append(plato)
    elif tipo == "Ninguno":
        print("Menú General\n")
        for plato in cliente.get_restaurante().get_menu():
            platos.append(plato)

    for plato in cliente.get_platos_favoritos():
        if plato in cliente.get_restaurante().get_menu():
            platos.append(plato)

    if not platos:
        print("No contamos con platos de este tipo por el momento.")
    else:
        for idx, plato in enumerate(platos):
            print(f"{idx + 1}. {plato}")

        num_plato = Utilidad.readInt()
        cantidad = Utilidad.readInt()

        for _ in range(cantidad):
            plato_pedido = platos[num_plato - 1]
            plato_pedido.aumentar_veces_pedido()
            pedido.agregar_plato(plato_pedido)
            print(f"Su Pedido hasta ahora\n{pedido}\n")

    return pedido

def hacer_pedido(clientes, pedido):
    pedidos = []
    for cliente in clientes:
        pedido_cliente = Pedido()
        encendido2 = True
        while encendido2:
            print("Seleccione una opción:\n1. Entradas.\n2. Platos Fuertes.\n3. Bebidas.\n4. Postres.\n5. Menú Infantil.\n6. Todos.\n7. Terminar.")

            opcion = Utilidad.readInt()
            encendido2 = True
            if opcion == 1:
                # Utilidad.limpiar_pantalla()
                pedido = platos_menu("Entrada", cliente)
                if pedido.get_platos():
                    pedido_cliente.get_platos().extend(pedido.get_platos())
            elif opcion == 2:
                # Utilidad.limpiar_pantalla()
                pedido = platos_menu("Plato fuerte", cliente)
                if pedido.get_platos():
                    pedido_cliente.get_platos().extend(pedido.get_platos())
            elif opcion == 3:
                # Utilidad.limpiar_pantalla()
                pedido = platos_menu("Bebida", cliente)
                if pedido.get_platos():
                    pedido_cliente.get_platos().extend(pedido.get_platos())
            elif opcion == 4:
                # Utilidad.limpiar_pantalla()
                pedido = platos_menu("Postre", cliente)
                if pedido.get_platos():
                    pedido_cliente.get_platos().extend(pedido.get_platos())
            elif opcion == 5:
                # Utilidad.limpiar_pantalla()
                pedido = platos_menu("Infantil", cliente)
                if pedido.get_platos():
                    pedido_cliente.get_platos().extend(pedido.get_platos())
            elif opcion == 6:
                # Utilidad.limpiar_pantalla()
                pedido = platos_menu("Ninguno", cliente)
                if pedido.get_platos():
                    pedido_cliente.get_platos().extend(pedido.get_platos())
            else:
                if not pedido_cliente.get_platos():
                    print("Ingrese un valor válido [1 - 6]")
                else:
                    print("Fin pedido")
                    encendido2 = False

        pedidos.append(pedido_cliente)
        cliente.set_pedido(pedido_cliente)

    return pedidos

##Interaccion 3

def asignar_factura(pedidos):
    mesero = pedidos[0].get_mesero()
    mesa = mesero.get_mesa()

    for i, pedido in enumerate(pedidos):
        valor_factura = 0
        factura = Factura(pedido, valor_factura)
        mesa.get_facturas().append(factura)
        mesa.get_clientes()[i].set_factura(factura)

        for plato in pedido.get_platos():
            factura.aumentar_valor(plato.get_precio())

        print(factura)

    mesero.aumentar_ganancias_extra(5000)

    # Utilidad.limpiar_pantalla()

    return mesa.get_facturas()

# Funcionalidad 3
def dejar_restaurante():
    encendido = True
    while encendido:
        print("""¿Algún cliente desea dejar un restaurante?
        1. Sí.
        2. No.
        Escriba un número para elegir su opción.""")
        
        eleccion = int(input())
        
        if eleccion == 1:
            limpiar_pantalla()
            print("Ingrese el número de cédula del cliente que va a dejar el restaurante")
            cedula = int(input())
            cliente = buscar_cliente_por_cedula(cedula)  # Asumiendo que `buscar_cliente_por_cedula` es un método que devuelve el cliente
            mesa = cliente.get_mesa()  # Asumiendo que `get_mesa` devuelve la mesa del cliente
            cobrar_factura(mesa)
            encendido = False
            
        elif eleccion == 2:
            # limpiar_pantalla()
            # menu_principal()
            encendido = False
            
        else:
            # limpiar_pantalla()
            print("Ingrese un número válido [1 - 2].")

def cobrar_factura(mesa):
    encendido = True
    while encendido:
        print("Interacción 1.")
        valor_factura = 0
        
        for cliente in mesa.get_clientes():  # Asumiendo que `get_clientes` devuelve la lista de clientes en la mesa
            valor_factura += cliente.get_factura().calcular_valor()  # Asumiendo que `calcular_valor` devuelve el valor de la factura
            
        print(f"El valor de la factura es: {valor_factura}")
        print("""¿Desea agregar propina?
        1. Sí.
        2. No.
        Escriba un número para elegir su opción.""")
        
        eleccion = int(input())
        
        if eleccion == 1:
            print("Por favor ingrese el valor de la propina.")
            propina = int(input())
            valor_factura += propina
            mesa.set_valor_total(valor_factura)  # Asumiendo que `set_valor_total` establece el valor total en la mesa
            print(f"El valor de la factura con propina es: {valor_factura}")
            separar_factura(mesa)  # Asumiendo que `separar_factura` es un método que divide la factura
            liberar_mesa(mesa)  # Asumiendo que `liberar_mesa` es un método que libera la mesa
            encendido = False
            
        elif eleccion == 2:
            print(f"El valor de la factura sin propina es: {valor_factura}")
            mesa.set_valor_total(valor_factura)
            separar_factura(mesa)
            liberar_mesa(mesa)
            encendido = False
            
        else:
            print("Número no válido.")

def separar_factura(mesa):
    encendido = True
    while encendido:
        print("¿Desea separar la factura?")
        print("""
            1. Sí.
            2. No.
            Escriba un número para elegir su opción.""")
        eleccion = int(input())

        if eleccion == 1:
            print("Por favor ingrese el número de personas que van a pagar la factura.")
            numero_personas = int(input())

            if numero_personas == len(mesa.get_clientes()):
                print("¿Todos desean pagar el mismo monto?")
                print("""
                    1. Sí.
                    2. No.
                    Escriba un número para elegir su opción.""")
                eleccion2 = int(input())

                if eleccion2 == 1:
                    valor_factura = mesa.get_valor_total()
                    valor_por_persona = valor_factura // numero_personas
                    print(f"El valor por persona es: {valor_por_persona}")
                    
                    clientes_pagadores = mesa.get_clientes()

                    for cliente_pagador in clientes_pagadores:
                        escoger_metodo_pago(cliente_pagador)
                        valor_final_por_persona = aplicar_descuentos_cuenta(cliente_pagador, valor_por_persona)
                        transaccion_confirmada = False
                        while not transaccion_confirmada:
                            print(f"Descuento por afiliación: {valor_por_persona - valor_final_por_persona}")
                            print(f"¿Desea confirmar la transacción con un valor de: {valor_final_por_persona}?")
                            print("""
                                1. Sí.
                                2. No.
                                Escriba un número para elegir su opción.""")
                            confirmacion = int(input())
                            if confirmacion == 1:
                                print("Transacción confirmada.")
                                cliente_pagador.get_factura().pagar()
                                mesa.set_valor_total(mesa.get_valor_total() - valor_por_persona)
                                transaccion_confirmada = True
                            elif confirmacion == 2:
                                continue
                            else:
                                print("Número no válido.")

                    if mesa.get_valor_total() == 0:
                        print("La factura ha sido pagada. ¡Esperamos que vuelvan pronto!")
                
                elif eleccion2 == 2:
                    print("Cada persona pagará lo que consumió.")
                    for cliente in mesa.get_clientes():
                        print(f"{cliente.get_nombre()} debe pagar: {cliente.get_factura().get_valor()}")
                        escoger_metodo_pago(cliente)
                        valor_final_factura = aplicar_descuentos_cuenta(cliente, cliente.get_factura().get_valor())
                        transaccion_confirmada = False
                        while not transaccion_confirmada:
                            print(f"¿Desea confirmar la transacción con un valor de: {valor_final_factura}?")
                            print("""
                                1. Sí.
                                2. No.
                                Escriba un número para elegir su opción.""")
                            confirmacion = int(input())
                            if confirmacion == 1:
                                print("Transacción confirmada.")
                                cliente.get_factura().pagar()
                                mesa.set_valor_total(mesa.get_valor_total() - cliente.get_factura().get_valor())
                                transaccion_confirmada = True
                            elif confirmacion == 2:
                                continue
                            else:
                                print("Número no válido.")

                    if mesa.get_valor_total() == 0:
                        print("La factura ha sido pagada. ¡Esperamos que vuelvan pronto!")
                
            else:
                clientes_pagadores = []
                personas_procesadas = 0
                while mesa.get_valor_total() > 0 and personas_procesadas < numero_personas:
                    for j in range(numero_personas):
                        print("Ingrese la cédula de la persona que pagará la factura.")
                        cedula = int(input())
                        
                        cliente_pagador = None
                        for cliente in mesa.get_clientes():
                            if cliente.get_cedula() == cedula:
                                cliente_pagador = cliente
                                clientes_pagadores.append(cliente)
                                break

                        if cliente_pagador:
                            print("Ingrese la cantidad que desea pagar.")
                            valor = int(input())
                            if valor > mesa.get_valor_total():
                                print("El valor ingresado es mayor al valor de la factura.")
                            else:
                                escoger_metodo_pago(cliente_pagador)
                                valor_final_persona = aplicar_descuentos_cuenta(cliente_pagador, valor)
                                mesa.set_valor_total(mesa.get_valor_total() - valor + (valor - valor_final_persona))
                                print(f"El pago final fue: {valor_final_persona}")
                                print(f"El valor restante de la factura es: {mesa.get_valor_total()}")
                            
                            personas_procesadas += 1
                            if mesa.get_valor_total() <= 0:
                                break
                        else:
                            print("Cédula no válida.")

                if mesa.get_valor_total() != 0:
                    print("La factura aún no ha sido pagada.")
                    print("Seleccione el cliente que pagará la factura.")
                    for i, cliente in enumerate(clientes_pagadores, start=1):
                        print(f"{i}. {cliente.get_nombre()}")
                    
                    cliente_a_pagar = int(input()) - 1
                    print(f"Debe pagar el total restante de: {mesa.get_valor_total()}")
                    print("¿Desea confirmar la transacción?")
                    print("""
                        1. Sí.
                        2. No.
                        Escriba un número para elegir su opción.""")
                    confirmacion = int(input())
                    if confirmacion == 1:
                        print("Transacción confirmada.")
                        mesa.set_valor_total(0)
                    else:
                        print("Número no válido.")
                
                print("La factura ha sido pagada.")

            encendido = False
        
        elif eleccion == 2:
            print("Ingrese la cédula del cliente que realizará el pago.")
            cedula_cliente = int(input())
            for cliente in mesa.get_clientes():
                if cliente.get_cedula() == cedula_cliente:
                    escoger_metodo_pago(cliente)
                    valor_final_factura = aplicar_descuentos_cuenta(cliente, mesa.get_valor_total())
                    transaccion_confirmada = False
                    while not transaccion_confirmada:
                        print(f"¿Desea confirmar la transacción con un valor de: {valor_final_factura}?")
                        print("""
                            1. Sí.
                            2. No.
                            Escriba un número para elegir su opción.""")
                        confirmacion = int(input())
                        if confirmacion == 1:
                            print("Transacción confirmada.")
                            for clientes in mesa.get_clientes():
                                clientes.get_factura().pagar()
                            mesa.set_valor_total(0)
                            transaccion_confirmada = True
                        elif confirmacion == 2:
                            continue
                        else:
                            print("Número no válido.")

                if mesa.get_valor_total() == 0:
                    print("La factura ha sido pagada. ¡Esperamos que vuelvan pronto!")

            encendido = False
        
        else:
            print("Número no válido.")

def escoger_metodo_pago(cliente_pagador):
    print(f"Por favor escoja el método de pago: {cliente_pagador.get_nombre()}")
    print("""
        1. Efectivo.
        2. Tarjeta.
        3. Cheque.
        Escriba un número para elegir su opción.""")
    
    metodo_pago = int(input())
    metodos_pago = []
    
    if metodo_pago == 1:
        cliente_pagador.get_factura().set_metodo_pago("Efectivo")
        metodos_pago.append("Efectivo")
    elif metodo_pago == 2:
        cliente_pagador.get_factura().set_metodo_pago("Tarjeta")
        metodos_pago.append("Tarjeta")
    elif metodo_pago == 3:
        cliente_pagador.get_factura().set_metodo_pago("Cheque")
        metodos_pago.append("Cheque")
    else:
        print("Número no válido")
        escoger_metodo_pago(cliente_pagador)

def liberar_mesa(mesa):
    encendido = True
    while encendido:
        print("Interacción 2.")
        print("¿Algún cliente desea reservar nuevamente?")
        print("""
            1. Sí.
            2. No.
            Escriba un número para elegir su opción.""")
        
        eleccion = int(input())
        if eleccion == 1:
            print("¿Cuántos clientes desean hacer una reservación?")
            numero_clientes = int(input())
            for _ in range(numero_clientes):
                print("Ingrese la cédula del cliente que desea reservar.")
                cedula = int(input())
                for cliente in mesa.get_clientes():
                    if cliente.get_cedula() == cedula:
                        if cliente.get_afiliacion() != Cliente.Afiliacion.NINGUNA:
                            reservarMesa()
                        else:
                            print("¿Desea afiliarse?")
                            print("""
                                1. Sí.
                                2. No.
                                Escriba un número para elegir su opción.""")
                            
                            eleccion2 = int(input())
                            if eleccion2 == 1:
                                print("¿Qué nivel de afiliación desea?")
                                print("""
                                    1. Estrellita.
                                    2. Estrella.
                                    3. Super estrellota.
                                    Escriba un número para elegir su opción.""")
                                
                                nivel_afiliacion = int(input())
                                if nivel_afiliacion == 1:
                                    transaccion_confirmada = False
                                    while not transaccion_confirmada:
                                        print("¿Desea confirmar la transacción con un valor de: 35.900?")
                                        print("""
                                            1. Sí.
                                            2. No.
                                            Escriba un número para elegir su opción.""")
                                        
                                        confirmacion = int(input())
                                        if confirmacion == 1:
                                            print("Transacción confirmada.")
                                            cliente.set_afiliacion(Cliente.Afiliacion.ESTRELLITA)
                                            transaccion_confirmada = True
                                        elif confirmacion == 2:
                                            print("Afiliación no confirmada.")
                                        else:
                                            print("Número no válido.")
                                elif nivel_afiliacion == 2:
                                    transaccion_confirmada = False
                                    while not transaccion_confirmada:
                                        print("¿Desea confirmar la transacción con un valor de: 48.900?")
                                        print("""
                                            1. Sí.
                                            2. No.
                                            Escriba un número para elegir su opción.""")
                                        
                                        confirmacion = int(input())
                                        if confirmacion == 1:
                                            print("Transacción confirmada.")
                                            cliente.set_afiliacion(Cliente.Afiliacion.ESTRELLA)
                                            transaccion_confirmada = True
                                        elif confirmacion == 2:
                                            print("Afiliación no confirmada.")
                                        else:
                                            print("Número no válido.")
                                elif nivel_afiliacion == 3:
                                    transaccion_confirmada = False
                                    while not transaccion_confirmada:
                                        print("¿Desea confirmar la transacción con un valor de: 65.900?")
                                        print("""
                                            1. Sí.
                                            2. No.
                                            Escriba un número para elegir su opción.""")
                                        
                                        confirmacion = int(input())
                                        if confirmacion == 1:
                                            print("Transacción confirmada.")
                                            cliente.set_afiliacion(Cliente.Afiliacion.SUPERESTRELLOTA)
                                            transaccion_confirmada = True
                                        elif confirmacion == 2:
                                            print("Afiliación no confirmada.")
                                        else:
                                            print("Número no válido.")
                                else:
                                    print("Número no válido.")
                                reservarMesa()
                            elif eleccion2 == 2:
                                reservarMesa()
        elif eleccion == 2:
            for cliente in mesa.get_clientes():
                if cliente.get_afiliacion() == Cliente.Afiliacion.NINGUNA:
                    print(f"{cliente.get_nombre()}, ¿desea afiliarse?")
                    print("""
                        1. Sí.
                        2. No.
                        Escriba un número para elegir su opción.""")
                    
                    eleccion3 = int(input())
                    if eleccion3 == 1:
                        print("¿Qué nivel de afiliación desea?")
                        print("""
                            1. Estrellita.
                            2. Estrella.
                            3. Super estrellota.
                            Escriba un número para elegir su opción.""")
                        
                        nivel_afiliacion = int(input())
                        if nivel_afiliacion == 1:
                            transaccion_confirmada = False
                            while not transaccion_confirmada:
                                print("¿Desea confirmar la transacción con un valor de: 35.900?")
                                print("""
                                    1. Sí.
                                    2. No.
                                    Escriba un número para elegir su opción.""")
                                
                                confirmacion = int(input())
                                if confirmacion == 1:
                                    print("Transacción confirmada.")
                                    cliente.set_afiliacion(Cliente.Afiliacion.ESTRELLITA)
                                    transaccion_confirmada = True
                                elif confirmacion == 2:
                                    print("Afiliación no confirmada.")
                                else:
                                    print("Número no válido.")
                        elif nivel_afiliacion == 2:
                            transaccion_confirmada = False
                            while not transaccion_confirmada:
                                print("¿Desea confirmar la transacción con un valor de: 48.900?")
                                print("""
                                    1. Sí.
                                    2. No.
                                    Escriba un número para elegir su opción.""")
                                
                                confirmacion = int(input())
                                if confirmacion == 1:
                                    print("Transacción confirmada.")
                                    cliente.set_afiliacion(Cliente.Afiliacion.ESTRELLA)
                                    transaccion_confirmada = True
                                elif confirmacion == 2:
                                    print("Afiliación no confirmada.")
                                else:
                                    print("Número no válido.")
                        elif nivel_afiliacion == 3:
                            transaccion_confirmada = False
                            while not transaccion_confirmada:
                                print("¿Desea confirmar la transacción con un valor de: 65.900?")
                                print("""
                                    1. Sí.
                                    2. No.
                                    Escriba un número para elegir su opción.""")
                                
                                confirmacion = int(input())
                                if confirmacion == 1:
                                    print("Transacción confirmada.")
                                    cliente.set_afiliacion(Cliente.Afiliacion.SUPERESTRELLOTA)
                                    transaccion_confirmada = True
                                elif confirmacion == 2:
                                    print("Afiliación no confirmada.")
                                else:
                                    print("Número no válido.")
                        else:
                            print("Número no válido.")
                    elif eleccion3 == 2:
                        pass
                calificar_restaurante(cliente)
        mesa.set_clientes(None)
        for cliente in mesa.get_clientes():
            cliente.set_mesa(None)
            cliente.set_factura(None)

def calificar_restaurante(cliente):
    print(f"Por favor {cliente.get_nombre()} califique el restaurante con una nota del 1 al 5.")
    calificacion = float(input())
    
    if 1 <= calificacion <= 5:
        print("Gracias por su calificación.")
        cliente.get_mesa().get_restaurante().set_calificacion(calificacion)
    else:
        print("Ingrese una calificación válida.")
    
    print("¿Desea añadir una reseña?")
    print("""
        1. Sí.
        2. No.
        Escriba un número para elegir su opción.""")
    
    eleccion = int(input())
    
    if eleccion == 1:
        print("Por favor ingrese su reseña.")
        resena = input()
        cliente.get_mesa().get_restaurante().anadir_reserva(resena)
        
        if cliente.get_afiliacion() is not None:
            cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 1)
            print("Gracias por su reseña. Obtuvo un punto extra por ayudarnos a mejorar.")
        else:
            print("Gracias por su reseña.")
    
    elif eleccion != 2:
        print("Número no válido.")
    
    print("Ingrese una calificación para su plato entre 1 y 5.")
    calificacion_plato = float(input())
    
    for plato in cliente.get_factura().get_pedido().get_platos():
        if 1 <= calificacion_plato <= 5:
            if calificacion_plato >= 4.5:
                cliente.agregar_plato_favorito(plato)
            if calificacion_plato >= 3:
                cliente.get_reserva().set_satisfaccion(True)
            plato.set_calificacion(calificacion_plato)
            Cliente.despedida(cliente)  # Caso #1 Ligadura dinámica
            print("Gracias por su calificación.")
            actualizar_platos(plato, cliente.get_mesa())
            actualizar_menu(cliente.get_mesa())
        else:
            print("Ingrese una calificación válida.")

def actualizar_platos(plato_calificado, mesa):
    if plato_calificado.get_calificacion() >= 4.5 and plato_calificado.get_cantidad_calificaciones() >= 3:
        mesa.get_restaurante().agregar_plato_recomendado(plato_calificado)
        plato_calificado.set_recomendado(True)
        nuevo_precio = int(plato_calificado.get_precio() + (plato_calificado.get_precio() * 0.2))
        plato_calificado.set_precio(nuevo_precio)
    
    if plato_calificado.get_calificacion() <= 3.7 and plato_calificado.get_cantidad_calificaciones() >= 3:
        mesa.get_restaurante().agregar_plato_descuento(plato_calificado)
        nuevo_precio = int(plato_calificado.get_precio() - (plato_calificado.get_precio() * 0.15))
        plato_calificado.set_precio(nuevo_precio)


def actualizar_menu(mesa):
    restaurante = mesa.get_restaurante()
    
    for plato in restaurante.get_platos_recomendados():
        if plato.get_pedidos_recomendados() >= 2:
            if plato.get_calificacion() <= 4.5:
                restaurante.eliminar_plato_recomendado(plato)
                nuevo_precio = int(plato.get_precio() - (plato.get_precio() * 0.2))
                plato.set_precio(nuevo_precio)
    
    for plato in restaurante.get_platos_descuento():
        if plato.get_pedidos_recomendados() >= 2:
            if plato.get_calificacion() < 3.7:
                restaurante.eliminar_plato(plato)
                print(f"El plato {plato.get_nombre()} ha sido eliminado del menú.")
                print("¿Qué desea hacer?")
                print("""
                    1. Añadir otro plato.
                    2. Traer un plato de otra sede.
                    Escriba un número para elegir su opción.""")
                eleccion = int(input())
                
                if eleccion == 1:
                    plato_nuevo = crear_plato()
                    restaurante.agregar_plato(plato_nuevo)
                    print("Se ha añadido un nuevo plato al menú.")
                elif eleccion == 2:
                    mejores_platos = Utilidad.listado_platos_calificacion()
                    while True:
                        print("¿Cuál de los platos presentados desea agregar al menú del restaurante?")
                        eleccion_plato = int(input())
                        if eleccion_plato < 1 or eleccion_plato > len(mejores_platos):
                            print(f"Ingrese un valor válido [1 - {len(mejores_platos)}].")
                        else:
                            restaurante.get_menu().append(mejores_platos[eleccion_plato - 1])
                            print("Nuevo plato añadido al menú.")
                            break
                else:
                    print("Número no válido.")
            else:
                restaurante.eliminar_plato_descuento(plato)
                nuevo_precio = int(plato.get_precio() + (plato.get_precio() * 0.15))
                plato.set_precio(nuevo_precio)
    
    return restaurante

def aplicar_descuentos_cuenta(cliente, valor_por_persona):
    valor_final = 0
    
    if cliente.get_afiliacion() != "NINGUNA":
        valor_final = valor_por_persona
        print("Se aplicaron descuentos por su nivel de afiliación.")
        
        if cliente.get_afiliacion() == "ESTRELLITA":
            metodo_pago = cliente.get_factura().get_metodo_pago()
            if metodo_pago == "Efectivo":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.05))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 1)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.07))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 2)
            elif metodo_pago == "Tarjeta":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.03))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 1)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.05))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 2)
            elif metodo_pago == "Cheque":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.02))
                    cliente.set_puntos_acumulados(0)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.03))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 1)
            elif metodo_pago == "Puntos":
                pass
        
        elif cliente.get_afiliacion() == "ESTRELLA":
            metodo_pago = cliente.get_factura().get_metodo_pago()
            if metodo_pago == "Efectivo":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.07))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 2)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.15))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 4)
            elif metodo_pago == "Tarjeta":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.08))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 2)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.15))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 4)
            elif metodo_pago == "Cheque":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.02))
                    cliente.set_puntos_acumulados(0)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.1))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 1)
            elif metodo_pago == "Puntos":
                pass
        
        elif cliente.get_afiliacion() == "SUPERESTRELLOTA":
            metodo_pago = cliente.get_factura().get_metodo_pago()
            if metodo_pago == "Efectivo":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.1))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 6)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.2))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 8)
            elif metodo_pago == "Tarjeta":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.15))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 6)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.25))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 8)
            elif metodo_pago == "Cheque":
                if cliente.get_factura().get_valor() < 30000:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.05))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 1)
                else:
                    valor_final = int(valor_por_persona - (valor_por_persona * 0.08))
                    cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 2)
            elif metodo_pago == "Puntos":
                pass
    
    else:
        valor_final = valor_por_persona
    
    if cliente.get_puntos_acumulados() >= 10:
        print("Felicidades, ha obtenido un descuento de 10.000 por sus puntos acumulados.")
        valor_final -= 10000
        cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() - 10)
    
    return valor_final

# Funcionalidad 4
def agregarSede():
    restaurante = Restaurante()
    encendido = True
    while encendido:
        print("""
        ¿Desea añadir una nueva sede?
        1. Sí.
        2. No.
        Escriba un número para elegir su opción.
        """)
        eleccion = Utilidad.readInt()

        if eleccion == 1:
            
            print("Interacción 1.")
            restaurante = elegirZona(restaurante)
            establecerDisposicion(restaurante)
            establecerMenuYEncargos(restaurante)
            encendido = False
        elif eleccion == 2:
            # Volver al menú
            # menu_principal()
            encendido = False
        else:
            
            print("Ingrese un número válido [1 - 2].")

    return restaurante

def elegirZona(restaurante):
    encendido1 = True
    while encendido1:
        # Se muestran las ciudades de las que se tienen datos
        for zona in Zona.get_zonas():
            print(zona.get_nombre())
        print("Ciudades:")
        Utilidad.listado_ciudades()
        print("Escriba un número para elegir la ciudad.\nEn caso de no encontrar la ciudad requerida escriba 0.")
        eleccion1 = Utilidad.readInt()

        if eleccion1 > len(Ciudad.get_ciudades()) or eleccion1 < 0:
            print(f"Ingrese un número válido [1 - {len(Ciudad.get_ciudades())}].")
        else:
            
            if eleccion1 != 0:  # Si se encuentra la ciudad
                ciudad = Ciudad.get_ciudades()[eleccion1 - 1]
                if not ciudad.get_restaurantes():  # Si la ciudad no tiene restaurantes
                    parametrosBasicos(ciudad, restaurante)
                else:  # Si la ciudad tiene restaurantes
                    # Análisis de reservas
                    reservas_ultimos_treinta = []
                    intentos_ultimos_treinta = []
                    mesas_restaurantes = []

                    reservas_satisfactorias = 0
                    total_intentos = 0

                    # Agregamos los datos que corresponden a los últimos 30 días de funcionamiento de los restaurantes de la ciudad correspondiente.
                    for zona in ciudad.get_zonas_ciudad():
                        for restaurante_zona in zona.get_restaurantes():
                            reservas_restaurante = []
                            intentos_restaurante = []
                            for reserva in restaurante_zona.get_historial_reservas():
                                if reserva.is_satisfaccion():
                                    reservas_satisfactorias += 1
                                fecha_to_date_time = datetime.datetime(reserva.get_fecha()[0], reserva.get_fecha()[1], reserva.get_fecha()[2], reserva.get_fecha()[3], 0)
                                if datetime.now() - datetime.timedelta(days=30) < fecha_to_date_time < datetime.now() and fecha_to_date_time not in reservas_restaurante:
                                    reservas_restaurante.append(reserva)
                            if restaurante_zona.get_intentos_reserva() is not None:
                                for intento in restaurante_zona.get_intentos_reserva():
                                    total_intentos += 1
                                    fecha_to_date = datetime.date(intento[0], intento[1], intento[2])
                                    if datetime.date.today() - datetime.timedelta(days=30) < fecha_to_date < datetime.date.today():
                                        intentos_restaurante.append(intento)

                            for mesa in restaurante_zona.get_mesas():
                                mesas_restaurantes.append(mesa)

                            reservas_ultimos_treinta.extend(reservas_restaurante)
                            intentos_ultimos_treinta.extend(intentos_restaurante)

                    # Demanda por Hora
                    intentos_reserva = len(intentos_ultimos_treinta)
                    horas_funcionamiento = len(reservas_ultimos_treinta)
                    total_mesas = len(mesas_restaurantes)

                    if total_mesas != 0 and horas_funcionamiento != 0:
                        demanda_por_hora = (intentos_reserva / horas_funcionamiento) / total_mesas

                        # Satisfacción del Cliente
                        satisfaccion_del_cliente = (reservas_satisfactorias / total_mesas) * 100

                        # Conclusión Análisis
                        conclusion = (demanda_por_hora + satisfaccion_del_cliente) / 2

                        if conclusion < 0.5:
                            print(f"Según el algoritmo de análisis hecho, no es recomendable crear un nuevo restaurante en {ciudad.get_nombre()}.\nEsto se debe a que los restaurantes de la ciudad tienen un flujo bajo de clientes y no están cumpliendo con las expectativas de la gran mayoría de sus usuarios.\nTeniendo esto en cuenta, ¿Desea crear una nueva sede?\n1. Sí.\n2. No.")
                            encendido2 = True
                            while encendido2:
                                eleccion2 = Utilidad.readInt()
                                if eleccion2 == 1:
                                    parametrosBasicos(ciudad, restaurante)
                                    encendido2 = False
                                elif eleccion2 == 2:
                                    encendido2 = False
                                else:
                                    print("Ingrese un valor válido [1 - 2].")
                        elif 0.5 <= conclusion <= 0.7:
                            print(f"Según el algoritmo de análisis hecho, es medianamente recomendable crear un nuevo restaurante en {ciudad.get_nombre()}.\nEsto se debe a que los restaurantes tienen un flujo medio de clientes y están cumpliendo con las expectativas la mayoría de los usuarios.\nTeniendo esto en cuenta, ¿Desea crear una nueva sede?\n1. Sí.\n2. No.")
                            encendido3 = True
                            while encendido3:
                                eleccion2 = Utilidad.readInt()
                                if eleccion2 == 1:
                                    parametrosBasicos(ciudad, restaurante)
                                    encendido3 = False
                                elif eleccion2 == 2:
                                    encendido3 = False
                                else:
                                    print("Ingrese un valor válido [1 - 2].")
                        else:
                            parametrosBasicos(ciudad, restaurante)
                    else:
                        parametrosBasicos(ciudad, restaurante)

            else:  # Si no se encuentra la ciudad
                print("Por favor ingrese el nombre de la ciudad.")
                ciudad = Ciudad(input().capitalize())
                print("Por favor ingrese la cantidad de zonas que tiene la ciudad.")
                cantidad_zonas = Utilidad.readInt()
                # Este ciclo for se encarga de la creación de las zonas de la nueva ciudad.
                for i in range(1, cantidad_zonas + 1):
                    print(f"Por favor ingrese el nombre de la zona #{i}.")
                    nombre_zona = input().capitalize()
                    print(f"Por favor ingrese la población de la zona #{i}.")
                    poblacion_zona = Utilidad.readInt()
                    ciudad.get_zonas_ciudad().append(Zona(poblacion_zona, nombre_zona.capitalize(), ciudad))
                    ciudad.actualizar_poblacion()
                    print(ciudad.get_zonas_ciudad()[-1])
                
                parametrosBasicos(ciudad, restaurante)

            encendido1 = False
    return restaurante

def obtenerPromedios():
    valores = [0] * 5
    ancho = 0  # 0
    alto = 0  # 1
    mesas_estandar = 0  # 2
    mesas_vip = 0  # 3
    ventanas = 0  # 4

    for zona in Zona.get_zonas():
        for restaurante in zona.get_restaurantes():
            valores[0] += restaurante.get_coord_x()
            valores[1] += restaurante.get_coord_y()
            for mesa in restaurante.get_mesas():
                if not mesa.is_vip():
                    valores[2] += 1
                else:
                    valores[3] += 1
            for i in range(1, restaurante.get_coord_y() + 1):
                for string in restaurante.get_disposicion().get(i):
                    if string == "W":
                        valores[4] += 1

    return valores

# Este método se encarga de definir los parámetros básicos del restaurante: Ciudad, Zona, Zona VIP y Calificación.
def parametrosBasicos(ciudad, restaurante):
    print(ciudad.get_zonas_ciudad())
    print("Zonas de " + ciudad.get_nombre() + ":")
    Utilidad.listado_zonas_ciudad(ciudad)
    print("Escriba un número para elegir la zona.\nEn caso de no encontrar la zona requerida escriba 0.")
    eleccion_zona1 = Utilidad.readInt()
    
    if eleccion_zona1 > len(Ciudad.get_ciudades()) or eleccion_zona1 < 0:
        print("Ingrese un número válido [1 - " + str(len(ciudad.get_zonas_ciudad())) + "].")
        parametrosBasicos(ciudad, restaurante)
    else:
        
        if eleccion_zona1 != 0:  # Si se encuentra la zona
            zona_elegida = ciudad.get_zonas_ciudad()[eleccion_zona1 - 1]
            # Se evalúa si existen restaurantes enlazados a esta zona.
            if not zona_elegida.get_restaurantes():  # Si la zona elegida no tiene restaurantes
                # Se enlaza la ciudad al restaurante
                restaurante.set_ciudad(ciudad)
                # Se enlaza la zona al restaurante
                restaurante.set_zona(ciudad.get_zonas_ciudad()[eleccion_zona1 - 1])
                # Se enlaza el restaurante a la zona
                ciudad.get_zonas_ciudad()[eleccion_zona1 - 1].get_restaurantes().append(restaurante)
                # Se enlaza el restaurante a la ciudad
                ciudad.get_restaurantes().append(restaurante)
                # Se establecen los parámetros básicos del restaurante
                print("Ingrese el nombre del restaurante:")
                nombre = input().capitalize()
                restaurante.set_nombre(nombre)
                print("¿El restaurante tendrá zona VIP?\n1. Sí.\n2. No.\nEscriba un número para elegir.")
                tiene_vip = Utilidad.readInt()
                if tiene_vip == 1:
                    restaurante.set_zona_vip(True)
                elif tiene_vip == 2:
                    pass
                else:
                    print("Número no válido")
                restaurante.set_calificacion(int((random.random() * 5) + 1))
            else:  # Si la zona elegida tiene restaurantes
                # Análisis de reservas
                reservas_ultimos_treinta = []
                intentos_ultimos_treinta = []
                mesas_restaurantes = []

                reservas_satisfactorias = 0
                total_intentos = 0

                # Agregamos los datos que corresponden a los últimos 30 días de funcionamiento de los restaurantes de la ciudad correspondiente.
                for restaurante_zona in zona_elegida.get_restaurantes():
                    reservas_restaurante = []
                    intentos_restaurante = []
                    for reserva in restaurante_zona.get_historial_reservas():
                        if reserva.is_satisfaccion():
                            reservas_satisfactorias += 1
                        fecha_to_date_time = datetime.datetime(reserva.get_fecha()[0], reserva.get_fecha()[1], reserva.get_fecha()[2], reserva.get_fecha()[3], 0)
                        if (fecha_to_date_time > datetime.now() - datetime.timedelta(days=30)) and (fecha_to_date_time < datetime.now()):
                            if fecha_to_date_time not in reservas_restaurante:
                                reservas_restaurante.append(reserva)
                    if restaurante_zona.get_intentos_reserva() is not None:
                        for intento in restaurante_zona.get_intentos_reserva():
                            total_intentos += 1
                            fecha_to_date = datetime.date(intento[0], intento[1], intento[2])
                            if (fecha_to_date > datetime.date.today() - datetime.timedelta(days=30)) and (fecha_to_date < datetime.date.today()):
                                intentos_restaurante.append(intento)

                    for mesa in restaurante_zona.get_mesas():
                        mesas_restaurantes.append(mesa)

                    reservas_ultimos_treinta.extend(reservas_restaurante)
                    intentos_ultimos_treinta.extend(intentos_restaurante)

                # Demanda por Hora
                intentos_reserva = len(intentos_ultimos_treinta)
                horas_funcionamiento = len(reservas_ultimos_treinta)
                total_mesas = len(mesas_restaurantes)

                if total_mesas != 0 and horas_funcionamiento != 0:
                    demanda_por_hora = (intentos_reserva / horas_funcionamiento) / total_mesas

                    # Satisfacción del Cliente
                    satisfaccion_del_cliente = (reservas_satisfactorias / total_mesas) * 100

                    # Conclusión Análisis
                    conclusion = (demanda_por_hora + satisfaccion_del_cliente) / 2

                    if conclusion < 0.5:
                        print("Según el algoritmo de análisis hecho, no es recomendable crear un nuevo restaurante en " + ciudad.get_nombre() + ".\nEsto se debe a que los restaurantes de la ciudad tienen un flujo bajo de clientes y no están cumpliendo con las expectativas de la gran mayoría de sus usuarios.\nTeniendo esto en cuenta, ¿Desea crear una nueva sede?\n1. Sí.\n2. No.")
                        encendido2 = True
                        while encendido2:
                            eleccion2 = Utilidad.readInt()
                            if eleccion2 == 1:
                                encendido2 = False
                            elif eleccion2 == 2:
                                agregarSede()
                                encendido2 = False
                            else:
                                print("Ingrese un valor válido [1 - 2].")
                    elif 0.5 <= conclusion <= 0.7:
                        print("Según el algoritmo de análisis hecho, es medianamente recomendable crear un nuevo restaurante en " + ciudad.get_nombre() + ".\nEsto se debe a que los restaurantes tienen un flujo medio de clientes y están cumpliendo con las expectativas la mayoría de los usuarios.\nTeniendo esto en cuenta, ¿Desea crear una nueva sede?\n1. Sí.\n2. No.")
                        encendido3 = True
                        while encendido3:
                            eleccion2 = Utilidad.readInt()
                            if eleccion2 == 1:
                                encendido3 = False
                            elif eleccion2 == 2:
                                agregarSede()
                                encendido3 = False
                            else:
                                print("Ingrese un valor válido [1 - 2].")

                # Se enlaza la ciudad al restaurante
                restaurante.set_ciudad(ciudad)
                # Se enlaza la zona al restaurante
                restaurante.set_zona(ciudad.get_zonas_ciudad()[eleccion_zona1 - 1])
                # Se enlaza el restaurante a la zona
                ciudad.get_zonas_ciudad()[eleccion_zona1 - 1].get_restaurantes().append(restaurante)
                # Se enlaza el restaurante a la ciudad
                ciudad.get_restaurantes().append(restaurante)
                # Se establecen los parámetros básicos del restaurante
                print("Ingrese el nombre del restaurante:")
                nombre = input().capitalize()
                restaurante.set_nombre(nombre)
                print("¿El restaurante tendrá zona VIP?\n1. Sí.\n2. No.\nEscriba un número para elegir.")
                tiene_vip = Utilidad.readInt()
                if tiene_vip == 1:
                    restaurante.set_zona_vip(True)
                elif tiene_vip == 2:
                    pass
                else:
                    print("Número no válido")
                restaurante.set_calificacion(int((random.random() * 5) + 1))

        else:  # Si no se encuentra la zona
            print("Por favor ingrese el nombre de la zona.")
            nombre_zona = input().capitalize()
            print("Por favor ingrese la población de la zona.")
            poblacion_zona = Utilidad.readInt()
            ciudad.get_zonas_ciudad().append(Zona(poblacion_zona, nombre_zona.capitalize(), ciudad))
            ciudad.actualizar_poblacion()
            restaurante.set_ciudad(ciudad)
            print("Zonas de " + ciudad.get_nombre() + ":")
            Utilidad.listado_zonas_ciudad(ciudad)
            print("Escriba un número para elegir la zona.\nEn caso de no encontrar la zona requerida escriba 0.")
            eleccion_zona2 = Utilidad.readInt()
            if eleccion_zona2 > len(Ciudad.get_ciudades()) or eleccion_zona2 < 0:
                print("Ingrese un número válido [1 - " + str(len(ciudad.get_zonas_ciudad())) + "].")
            else:
                
                # Se enlaza la ciudad al restaurante
                restaurante.set_ciudad(ciudad)
                # Se enlaza la zona al restaurante
                restaurante.set_zona(ciudad.get_zonas_ciudad()[eleccion_zona2 - 1])
                # Se enlaza el restaurante a la zona
                ciudad.get_zonas_ciudad()[eleccion_zona2 - 1].get_restaurantes().append(restaurante)
                # Se establecen los parámetros básicos del restaurante
                print("¿El restaurante tendrá zona VIP?\n1. Sí.\n2. No.\nEscriba un número para elegir.")
                tiene_vip = Utilidad.readInt()
                if tiene_vip == 1:
                    restaurante.set_zona_vip(True)
                else:
                    pass
                restaurante.set_calificacion(int((random.random() * 5) + 1))


# Método para establecer la disposición del restaurante.
def establecerDisposicion(restaurante):
    if len(Restaurante.get_restaurantes()) > 3:
        promedio_area, promedio_mesas, promedio_sillas = 0, 0, 0

        for restaurant in Restaurante.get_restaurantes():
            promedio_area += restaurant.get_area()
            promedio_mesas += restaurant.get_mesas()
            promedio_sillas += restaurant.get_sillas()

        promedio_area = promedio_area / len(Restaurante.get_restaurantes())
        promedio_mesas = promedio_mesas / len(Restaurante.get_restaurantes())
        promedio_sillas = promedio_sillas / len(Restaurante.get_restaurantes())

        print(f"Promedio Área: {promedio_area:.2f}m²\nPromedio Mesas: {promedio_mesas}\nPromedio Sillas: {promedio_sillas}")
        print("¿Desea establecer el tamaño y la disposición del nuevo restaurante basado en estos promedios?\n1. Sí.\n2. No.")
        eleccion = Utilidad.readInt()
        if eleccion == 1:
            restaurante.set_area(promedio_area)
            restaurante.set_mesas(promedio_mesas)
            restaurante.set_sillas(promedio_sillas)
        else:
            restaurante.editar_restaurante()
    else:
        restaurante.set_area(150)
        restaurante.set_mesas(20)
        restaurante.set_sillas(80)

def cambiarElemento(restaurante, coord_x, coord_y, chars, top_row, separator, bottom_row):
    print("Escribe la coordenada en X:")
    mod_coord_x = Utilidad.readInt()
    print("Escribe la coordenada en Y:")
    mod_coord_y = Utilidad.readInt()
    casilla = eliminarCasillasRepetidas(restaurante, mod_coord_x, mod_coord_y)
    
    if mod_coord_y < 1 or mod_coord_y > coord_y or mod_coord_x < 1 or mod_coord_x > coord_x:
        print(f"Escribe valores válidos para ambas coordenadas\nX = [1 - {coord_x}]\nY = [1 - {coord_y}]")
        cambiarElemento(restaurante, coord_x, coord_y, chars, top_row, separator, bottom_row)
    else:
        if (mod_coord_y == 1 and mod_coord_x == 1) or (mod_coord_y == 1 and mod_coord_x == coord_x) or \
           (mod_coord_y == coord_y and mod_coord_x == 1) or (mod_coord_y == coord_y and mod_coord_x == coord_x):
            print("No es posible realizar cambios en las esquinas del restaurante.")
            cambiarElemento(restaurante, coord_x, coord_y, chars, top_row, separator, bottom_row)
        elif mod_coord_y == 1 or mod_coord_y == coord_y or mod_coord_x == 1 or mod_coord_x == coord_x:
            print("Reemplazar por:\n1. Pared (B).\n2. Ventana (W).\n3. Entrada (E).")
            tile_type = Utilidad.readInt()
            if tile_type == 1:
                restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = "B"
                restaurante.get_casillas().remove(casilla)
            elif tile_type == 2:
                restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = "W"
                restaurante.get_casillas().remove(casilla)
                restaurante.get_casillas().append(Casilla(1, mod_coord_x, mod_coord_y))
            elif tile_type == 3:
                restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = "E"
                restaurante.get_casillas().remove(casilla)
                restaurante.get_casillas().append(Casilla(2, mod_coord_x, mod_coord_y))
            else:
                print("Dato inválido. Se reemplazará por una pared.")
                restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = "B"
                restaurante.get_casillas().remove(casilla)
        else:
            print("Reemplazar por:\n1. Espacio Vacío ( ).\n2. Mesa Estándar (T).\n3. Mesa VIP (V).")
            tile_type = Utilidad.readInt()
            if tile_type == 1:
                restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = " "
                restaurante.get_casillas().remove(casilla)
                restaurante.get_mesas().remove(casilla)
            elif tile_type == 2:
                restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = "T"
                restaurante.get_casillas().remove(casilla)
                restaurante.get_mesas().remove(casilla)
                mesa = Mesa(0, mod_coord_x, mod_coord_y, False, 4)
                restaurante.get_casillas().append(mesa)
                restaurante.get_mesas().append(mesa)
                mesa.set_fechas_disponibles(generarFechas())
            elif tile_type == 3:
                if restaurante.is_zona_vip():
                    restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = "V"
                    restaurante.get_casillas().remove(casilla)
                    restaurante.get_mesas().remove(casilla)
                    mesa = Mesa(0, mod_coord_x, mod_coord_y, True, 4)
                    restaurante.get_casillas().append(mesa)
                    restaurante.get_mesas().append(mesa)
                    mesa.set_fechas_disponibles(generarFechas())
                else:
                    restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = "T"
                    restaurante.get_casillas().remove(casilla)
                    restaurante.get_mesas().remove(casilla)
                    mesa = Mesa(0, mod_coord_x, mod_coord_y, False, 4)
                    restaurante.get_casillas().append(mesa)
                    restaurante.get_mesas().append(mesa)
                    mesa.set_fechas_disponibles(generarFechas())
            else:
                print("Dato inválido. Se reemplazará por un espacio vacío.")
                restaurante.get_casillas().remove(casilla)
                restaurante.get_mesas().remove(casilla)
                restaurante.get_disposicion()[mod_coord_y][mod_coord_x - 1] = " "
        
        
        imprimirDisposicionRestaurante(restaurante.get_disposicion(), coord_x, coord_y, chars, top_row, separator, bottom_row)

def generarFechas():
    fechas_disponibles = []
    hoy = date.today()
    fin = hoy + relativedelta(months=6)
    while hoy <= fin:
        fechas = [hoy.year, hoy.month, hoy.day, 10, 12, 14, 16, 18, 20]
        fechas_disponibles.append(fechas)
        hoy += timedelta(days=1)
    
    return fechas_disponibles

def eliminarCasillasRepetidas(restaurante, mod_coord_x, mod_coord_y):
    casilla_obsoleta = Casilla()
    for casilla in restaurante.get_casillas():
        if casilla.get_coord_x() == mod_coord_x and casilla.get_coord_y() == mod_coord_y:
            casilla_obsoleta = casilla
            break
    return casilla_obsoleta

def imprimirDisposicionRestaurante(plano_restaurante, coord_x, coord_y, chars, top_row, separator, bottom_row):
    print(top_row)
    for i in range(1, coord_y + 1):
        j = 0
        border_row = chars[4] + chars[11] + plano_restaurante[i][j] + chars[11]
        for k in range(2, coord_x):
            j += 1
            border_row += chars[4] + chars[11] + plano_restaurante[i][j] + chars[11]
        border_row += chars[4] + chars[11] + plano_restaurante[i][j + 1] + chars[11] + chars[4]
        print(border_row)
        if i == coord_y:
            print(bottom_row)
        else:
            print(separator)

def establecerMenuYEncargos(restaurante):
    if Restaurante.restaurantes_creados > 2:
        # Establecer Menú
        menu_transitorio = Utilidad.listado_platos_calificacion()  # Listado de platos con mejor calificación.
        print("¿Desea modificar el menú generado?\n1. Sí.\n2. No.")
        eleccion1 = Utilidad.readInt()

        if eleccion1 == 2:  # Si se quiere adoptar el menú generado
            restaurante.set_menu(menu_transitorio)
        elif eleccion1 == 1:  # Si no se quiere adoptar el menú generado
            encendido1 = True
            while encendido1:
                print("¿Qué desea hacer?\n1. Agregar.\n2. Eliminar.")
                eleccion2 = Utilidad.readInt()

                if eleccion2 == 1:  # Agregar
                    print("Platos existentes:")
                    for plato in Plato.get_platos():
                        if plato not in menu_transitorio:
                            print(plato.get_nombre().capitalize())

                    print("En caso de que quiera agregar uno de los platos mostrados en la lista, ingrese el nombre tal como allí aparece.")
                    plato = crearPlato()
                    menu_transitorio.append(plato)

                    print("¿Desea realizar otra modificación?\n1. Sí.\n2. No.")
                    eleccion3 = Utilidad.readInt()
                    if eleccion3 != 1:
                        encendido1 = False

                elif eleccion2 == 2:  # Eliminar
                    for i, plato_transitorio in enumerate(menu_transitorio, start=1):
                        print(f"{i}. {plato_transitorio.get_nombre()}")

                    print(f"Ingrese el número del plato a eliminar [1 - {len(menu_transitorio)}].")
                    eleccion4 = Utilidad.readInt()

                    if eleccion4 < 1 or eleccion4 > len(menu_transitorio):
                        print("Número inválido.")
                    else:
                        menu_transitorio.pop(eleccion4 - 1)

                    print("¿Desea realizar otra modificación?\n1. Sí.\n2. No.")
                    eleccion3 = Utilidad.readInt()
                    if eleccion3 != 1:
                        encendido1 = False

                else:
                    print("Ingrese un valor válido [1 - 2].")

            restaurante.set_menu(menu_transitorio)
        else:
            print("Ingrese un valor válido [1 - 2].")
            establecerMenuYEncargos(restaurante)

        # Establecer Encargos
        cargamento(restaurante)

    else:
        # Establecer Menú
        menu_restaurante = []
        print("Ingrese la cantidad de platos que tendrá el menú:")
        eleccion4 = Utilidad.readInt()
        for i in range(eleccion4):
            menu_restaurante.append(crearPlato())

        restaurante.set_menu(menu_restaurante)

        # Establecer Encargos
        cargamento(restaurante)



def cargamento(restaurante):
    cargamento = Cargamento()

    print("Seleccione la cantidad de ingredientes a encargar")
    for plato in restaurante.get_menu():
        print(f"Nombre: {plato.get_nombre()}\nVeces pedido: {plato.get_veces_pedido()}")
        print("Ingredientes:")
        plato.get_cantidad_ingredientes()
        for cantidad_ingredientes in plato.get_cantidad_ingredientes():
            print(f"Cantidad de {cantidad_ingredientes[0]} necesaria: {cantidad_ingredientes[1]}")
            print(f"¿Cuánto de {cantidad_ingredientes[0]} quieres agregar?")
            cantidad_agregar = Utilidad.readInt()
            cargamento.aumentar_cantidad_ingrediente([cantidad_ingredientes[0], str(cantidad_agregar)])

    print("Seleccione la cantidad de utilidades a encargar")
    for utilidad in Cargamento.UTILIDADES:
        print(f"Nombre: {utilidad}")
        print(f"¿Cuánto de {utilidad} quieres agregar?")
        cantidad_agregar = Utilidad.readInt()
        cargamento.get_utilidades().append(cantidad_agregar)

    fecha_actual = datetime.now()
    print("¿Cada cuántos días quiere que venga el cargamento?")
    frecuencia = Utilidad.readInt()
    cargamento.set_frecuencia(frecuencia)
    cargamento.set_proxima_entrega([fecha_actual.year, fecha_actual.month, fecha_actual.day])

    restaurante.set_cargamento(cargamento)
    cargamento.set_restaurante(restaurante)

def crearPlato():
    print("Ingrese el nombre del plato:")
    nombre = input().capitalize()
    existe = False
    indice_existe = 0
    plato_retorno = Plato()
    cantidad_ingredientes = []

    if not Plato.get_platos():
        for plato in Plato.get_platos():
            if plato.get_nombre() == nombre:
                existe = True
                indice_existe = Plato.get_platos().index(plato)
                break

    if not existe:
        print("Ingrese el tipo del plato:\n1. Entradas.\n2. Platos Fuertes.\n3. Bebidas.\n4. Postres.\n5. Menú Infantil.\n6. Todos.")
        eleccion_tipo = Utilidad.readInt()

        tipo_plato = {
            1: "Entrada",
            2: "Plato Fuerte",
            3: "Bebida",
            4: "Postre",
            5: "Menú Infantil"
        }.get(eleccion_tipo, "Todos")

        plato_retorno.set_tipo(tipo_plato)

        print("Ingrese el precio del plato, sin decimales.")
        precio = Utilidad.readInt()
        print("Ingrese la cantidad de ingredientes que tiene el plato.")
        num_ingredientes = Utilidad.readInt()

        if num_ingredientes < 1:
            num_ingredientes = 1

        
        lista_ingredientes = Utilidad.listado_ingredientes()

        if lista_ingredientes:
            for i, ingrediente in enumerate(lista_ingredientes):
                print(f"{i + 1}. {ingrediente.get_nombre()}.")

            ingredientes_plato = []
            print("\nElija la opción que mejor se acomode a su situación actual con respecto a la lista presentada:\n1. Todos los ingredientes están presentes.\n2. Algunos ingredientes están presentes.\n3. Ningún ingrediente está presente.")
            encendido1 = True

            while encendido1:
                eleccion = Utilidad.readInt()

                if eleccion == 1:
                    print(f"Escriba el número de lista donde está cada uno de los {num_ingredientes} ingredientes necesarios.")
                    for i in range(num_ingredientes):
                        print(f"Ingresa el número del ingrediente #{i + 1}")
                        indice = Utilidad.readInt() - 1
                        ingrediente = Ingrediente.get_ingredientes()[indice]
                        ingredientes_plato.append(ingrediente)

                        print("Ingresa la cantidad necesaria de este ingrediente para la preparación del plato")
                        cantidad_ingrediente = Utilidad.readInt()
                        if cantidad_ingrediente < 1:
                            cantidad_ingrediente = 1

                        cantidad_ingredientes.append([ingrediente.get_nombre(), str(cantidad_ingrediente)])

                    encendido1 = False

                elif eleccion == 2:
                    print("Ingrese la cantidad de ingredientes que ya están presentes.")
                    num_ing_existentes = Utilidad.readInt()

                    if num_ing_existentes < 1:
                        num_ing_existentes = 1

                    print(f"Escriba el número de lista donde está cada uno de los {num_ing_existentes} ingredientes necesarios.")
                    for i in range(num_ing_existentes):
                        print(f"Ingresa el número del ingrediente #{i + 1}")
                        indice = Utilidad.readInt() - 1
                        ingrediente = Ingrediente.get_ingredientes()[indice]
                        ingredientes_plato.append(ingrediente)

                        print("Ingresa la cantidad necesaria de este ingrediente para la preparación del plato")
                        cantidad_ingrediente = Utilidad.readInt()
                        if cantidad_ingrediente < 1:
                            cantidad_ingrediente = 1

                        cantidad_ingredientes.append([ingrediente.get_nombre(), str(cantidad_ingrediente)])

                    for i in range(num_ingredientes - num_ing_existentes):
                        cantidad_ingredientes = crear_ingrediente(cantidad_ingredientes, ingredientes_plato)

                    encendido1 = False

                elif eleccion == 3:
                    for i in range(num_ingredientes):
                        cantidad_ingredientes = crear_ingrediente(cantidad_ingredientes, ingredientes_plato)

                    encendido1 = False

                else:
                    print("Ingrese un valor válido [1 - 3].")

            plato_retorno = Plato(nombre, precio, ingredientes_plato, cantidad_ingredientes, 3)

        else:
            ingredientes_plato = []
            for i in range(num_ingredientes):
                cantidad_ingredientes = crear_ingrediente(cantidad_ingredientes, ingredientes_plato)

            plato_retorno = Plato(nombre, precio, ingredientes_plato, cantidad_ingredientes, 3)

    else:
        plato_retorno = Plato.get_platos()[indice_existe]

    for cantidad in cantidad_ingredientes:
        plato_retorno.get_cantidad_ingredientes().append(cantidad)

    return plato_retorno

def crear_ingrediente(cantidad_ingredientes, ingredientes_plato):
    print("Ingrese el nombre del nuevo ingrediente.")
    nombre_ingrediente = input().capitalize()
    
    print("Ingrese el precio unitario del nuevo ingrediente.")
    precio_ingrediente = Utilidad.readInt()
    
    if precio_ingrediente < 1:
        precio_ingrediente = 1
    
    ingrediente = Ingrediente(nombre_ingrediente, precio_ingrediente)
    ingredientes_plato.append(ingrediente)
    
    print("Ingresa la cantidad necesaria de este ingrediente para la " +
          "preparación del plato")
    cantidad_ingrediente = Utilidad.readInt()
    
    if cantidad_ingrediente < 1:
        cantidad_ingrediente = 1
    
    cantidad_ingredientes.append([ingrediente.get_nombre(), str(cantidad_ingrediente)])
    
    return cantidad_ingredientes


#Funcionalidad 5

def crear_evento():
    restaurante = Restaurante()
    factura = Factura()
    encendido = True
    while encendido:
        print("""
        ¿Desea un evento?
        1. Sí.
        2. No.
        Escriba un número para elegir su opción.
        """)
        eleccion = Utilidad.readInt()
        if eleccion == 1:
            print("Ciudades:")
            Utilidad.listado_ciudades()

            encendido1 = False
            ciudad = Ciudad()
            while encendido1:
                print("Escriba un número para elegir la ciudad.\nEn caso de no encontrar la ciudad requerida, escriba 0.")
                eleccion1 = Utilidad.readInt()
                if eleccion1 > len(Ciudad.get_ciudades()) or eleccion1 < 0:
                    print(f"Ingrese un número válido [1 - {len(Ciudad.get_ciudades())}].")
                    encendido1 = True
                else:
                    ciudad = Ciudad.get_ciudades()[eleccion1 - 1]

            # Interacción 1
            cliente = recomendar_localizacion(ciudad)
            restaurante = cliente[0].get_restaurante()

            # Interacción 2
            factura = recomendar_evento()

            # Interacción 3
            if factura.get_evento() != Factura().get_evento():
                datos_hora_reserva(restaurante, factura)

            encendido = False
        elif eleccion == 2:
            encendido = False
        else:
            print("Ingrese un número válido [1 - 2].")

# INTERACCIÓN #1 recomendar_localización
def recomendar_localizacion(ciudad):
    cliente = Cliente()
    restaurante = None

    # Primera parte: se pide la ciudad y se hacen las recomendaciones respectivas
    print("Desea que le recomendemos el restaurante con mayor capacidad:\n1. Sí, por favor.\n2. No, deseo conocerlos todos")
    eleccion_recomendacion = Utilidad.readInt()
    if eleccion_recomendacion == 1:  # Si quiere que se le recomiende restaurante automáticamente
        if ciudad:
            restaurante = get_restaurante(ciudad)
            cliente.set_restaurante(restaurante)
    elif eleccion_recomendacion == 2:
        print("Zonas:")
        Utilidad.listado_zonas_ciudad(ciudad)
        encendido2 = False
        while encendido2:
            eleccion_zona = Utilidad.readInt()
            if eleccion_zona < 1 or eleccion_zona > len(ciudad.get_zonas_ciudad()):
                encendido2 = True
            else:
                zona = ciudad.get_zonas_ciudad()[eleccion_zona - 1]
                print("Restaurantes:")
                Utilidad.listado_restaurantes_zona(zona)
                encendido3 = False
                while encendido3:
                    eleccion_restaurante = Utilidad.readInt()
                    if eleccion_restaurante < 1 or eleccion_restaurante > len(zona.get_restaurantes()):
                        encendido3 = True
                    else:
                        restaurante = zona.get_restaurantes()[eleccion_restaurante - 1]
                        cliente.set_restaurante(restaurante)

    print("Estimado Cliente, nos permite los siguientes datos:\nCédula:")
    cedula_cliente = Utilidad.readInt()
    print("Nombre:")
    nombre_cliente = input()
    clientes = []

    cliente.set_nombre(nombre_cliente)
    cliente.set_cedula(cedula_cliente)

    if Utilidad.existe_cliente(cliente):
        cliente = Utilidad.cliente_cedula(cliente)
        clientes.append(cliente)
    else:
        Cliente.get_clientes().append(cliente)
        clientes.append(cliente)

    reserva = Reserva()
    reserva.set_clientes(clientes)
    reserva.set_restaurante(restaurante)

    restaurante.get_historial_reservas().append(reserva)
    restaurante.set_clientes(clientes)

    encendido1 = False
    while encendido1:
        fecha = []
        print("Ingrese el día de la reserva:")
        fecha.append(Utilidad.readInt())
        print("Ingrese el mes de la reserva:")
        fecha.append(Utilidad.readInt())
        print("Ingrese el año de la reserva:")
        fecha.append(Utilidad.readInt())

        reserva.set_fecha(fecha)

        # Comprobar que no hay reservas para el día elegido.
        reservas_existentes = restaurante.get_historial_reservas()
        for reserva1 in reservas_existentes:
            if reserva1.get_fecha()[:3] == reserva.get_fecha():
                print("Ya existe una reserva para la fecha elegida.")
                encendido1 = True

    return clientes

# Método de la Interacción 1, que busca los restaurantes con mayor capacidad para el evento
def get_restaurante(ciudad):
    restaurante_mayor_capacidad = None
    mayor_capacidad = 0
    for zona in ciudad.get_zonas_ciudad():
        for restaurante in zona.get_restaurantes():
            if restaurante.get_capacidad() > mayor_capacidad:
                restaurante_mayor_capacidad = restaurante
                mayor_capacidad = restaurante.get_capacidad()
    return restaurante_mayor_capacidad

# Método de la Interacción 1
def listado_platos_evento(evento):
    platos_evento = evento.get_platos()
    for i, plato in enumerate(platos_evento, start=1):
        print(f"{i}. {plato.get_nombre()}")

##Metodos interaccion 2

# Método para listar platos del evento según el número de invitados y opción seleccionada (vino o champaña)
def listado_platos_evento(evento, numero_invitados, opcion):
    vinos_champanas = evento.get_platos()
    vinos_lista = []
    champanas_lista = []
    vinos_champan_ultimos = Plato()
    contador = 0

    if opcion == 1:
        for nombre_vino in vinos_champanas:
            if "vino" in nombre_vino.get_nombre().lower():
                vinos_lista.append(nombre_vino)
                contador += 1
                print(f"{contador}. {nombre_vino.get_nombre()}")
        vinos_champan_ultimos = recomendacion_meeting(numero_invitados, vinos_lista)

    elif opcion == 2:
        for nombre_champa in vinos_champanas:
            if "vino" not in nombre_champa.get_nombre().lower():
                champanas_lista.append(nombre_champa)
                contador += 1
                print(f"{contador}. {nombre_champa.get_nombre()}")
        vinos_champan_ultimos = recomendacion_meeting(numero_invitados, champanas_lista)

    return vinos_champan_ultimos

# Método que recomienda platos (vinos o champañas) según el número de invitados
def recomendacion_meeting(numero_invitados, eleccion):
    plato_final = Plato()
    print("""
    ¿Deseas conocer nuestras recomendaciones?:
    1. Sí, tomo la recomendación
    2. No, deseo ordenar por mi cuenta
    """)
    opinion = Utilidad.readInt()

    if opinion == 1:
        if 0 < numero_invitados <= 8:  # Recomendación para pocos invitados
            print("Son pocas personas, suponiendo su alto rango, os recomendamos:")
            botellas_a_llevar = [caros for caros in eleccion if caros.get_precio() > 170000]
            for i, finales in enumerate(botellas_a_llevar):
                print(f"{i + 1}. {finales.get_nombre()}")
            opcion_media = Utilidad.readInt()
            producto_ofrecido = botellas_a_llevar[opcion_media - 1]

            botellas_cantidad = 1 if numero_invitados <= 4 else 2
            plato_final = Plato(producto_ofrecido.get_nombre(), botellas_cantidad, producto_ofrecido.get_precio())

        else:
            print("Son bastantes invitados, para su economía os recomendamos:")
            botellas_a_llevar = [baratos for baratos in eleccion if baratos.get_precio() < 60000]
            for i, finales in enumerate(botellas_a_llevar):
                print(f"{i + 1}. {finales.get_nombre()}")
            opcion_media = Utilidad.readInt()
            producto_ofrecido = botellas_a_llevar[opcion_media - 1]

            cuenta_botellas = int((numero_invitados + producto_ofrecido.get_porciones() - 1) / producto_ofrecido.get_porciones())
            print(f"Un total de {cuenta_botellas} botellas")
            plato_final = Plato(producto_ofrecido.get_nombre(), cuenta_botellas, producto_ofrecido.get_precio())

    else:
        print("¿Cuál desea?")
        for i, plato in enumerate(eleccion):
            print(f"{i + 1}. {plato.get_nombre()}")
        opcion = Utilidad.readInt()
        escogido = eleccion[opcion - 1]
        print(f"De {escogido.get_nombre()} tenemos {escogido.get_cantidad_de_plato()} en bodega. ¿Cuántos desea?")
        cantidad_escogida = Utilidad.readInt()

        if cantidad_escogida <= escogido.get_cantidad_de_plato():
            cantidad_bebida = cantidad_escogida
            print("Excelente")
        else:
            print("No poseemos esa cantidad, le venderemos la máxima cantidad disponible")
            cantidad_bebida = escogido.get_cantidad_de_plato()

        plato_final = Plato(escogido.get_nombre(), cantidad_bebida, escogido.get_precio())

    return plato_final

# Método para obtener la lista final de platos según el tipo de gastronomía escogida
def listado_final(gastronomia_escogida):
    for listado_general in Plato.get_platos_gastronomias():
        for plato in listado_general:
            if plato.get_tipo() == gastronomia_escogida:
                return listado_general
    return None

# Método para mostrar los platos disponibles según la gastronomía escogida
def gastronomias_mundiales(opcion_gastronomias, gastronomias_nombres):
    gastronomia_escogida = gastronomias_nombres[opcion_gastronomias - 1]
    escogidos = listado_final(gastronomia_escogida)
    print("Para ello, ha preparado los siguientes platos:")
    for i, plato in enumerate(escogidos):
        print(f"{i + 1}. {plato.get_nombre()}")
    return escogidos

# Método para elegir un cocinero según la especialidad en la gastronomía escogida
def cocinero_elegido(opcion_gastronomias, gastronomias_nombres):
    gastronomia_escogida = gastronomias_nombres[opcion_gastronomias - 1]
    for trabajador_elegido in Trabajador.get_cocineros():
        if trabajador_elegido.get_especialidad() == gastronomia_escogida:
            return trabajador_elegido
    return None

# Método para recomendar un plato según la cantidad de invitados
def recomendacion_por_cantidad(evento, numero_invitados):
    platos_evento = evento.get_platos()
    plato_recomendado = None
    diferencia_minima = float('inf')

    for plato in platos_evento:
        diferencia = plato.get_porciones() - numero_invitados
        if diferencia >= 0 and diferencia < diferencia_minima:
            diferencia_minima = diferencia
            plato_recomendado = plato

    print(f"Vemos que son {numero_invitados} personas. Les recomendamos la torta: {plato_recomendado.get_nombre()}, que tiene porciones para {plato_recomendado.get_porciones()} personas.")

## Interacción 2

def recomendar_evento():
    # Utilidad.limpiar_pantalla()
    evento1 = Evento()
    factura = Factura()
    cliente = Cliente()

    print("""
        ¿Eres afiliado?
        1. Sí
        2. No
    """)
    respuesta_afiliacion = Utilidad.readInt()
    if respuesta_afiliacion == 1:
        cliente.es_afiliado()
    else:
        print("Dale, no hay lío")

    encendido1 = True
    encendido2 = True

    while encendido1:
        print("¿Desea conocer las temáticas de Eventos especiales que tenemos?")
        print("1. Sí, por favor")
        print("2. No")
        opcion_evento = Utilidad.readInt()

        if opcion_evento == 1:
            while encendido2:
                print("""
                    1. Cumpleaños
                    2. Meetings Empresariales
                    3. Gastronomías Mundiales
                    4. No, salir
                    Escriba un número para elegir su opción.
                """)
                opcion_final = Utilidad.readInt()

                if opcion_final == 1:
                    factura_cumple = Factura()
                    print("¿Cuántos invitados son?")
                    numero_invitados = Utilidad.readInt()
                    print("El Evento tiene un coste de 210.000$, ¿Desea continuar?")
                    print("1. Sí")
                    print("2. No")
                    respuesta_cumple = Utilidad.readInt()

                    if respuesta_cumple == 1:
                        torta_seleccionada = None
                        nombre_respuesta = "Cumpleanos Feliz"
                        coste = 210000

                        for elemento in Evento.get_eventos():
                            if elemento.get_nombre() == nombre_respuesta:
                                evento1 = elemento

                        print("Perfecto! Danos el nombre del festejado:")
                        nombre_festejado = input()
                        descripcion_evento = f"Feliz Cumpleaños!!! Te deseamos lo mejor en esta etapa {nombre_festejado}"
                        print("A continuación verá las tortas para la ocasión:")
                        listado_platos_evento(evento1)
                        recomendacion_por_cantidad(evento1, numero_invitados)

                        print("Digite la opción de la torta:")
                        pastel_escogido = Utilidad.readInt()

                        if pastel_escogido != 0:
                            torta_seleccionada = evento1.get_platos()[pastel_escogido - 1]
                            torta_seleccionada.descontar_plato(1)

                        platos_de_este_evento = []
                        platos_de_este_evento.append(torta_seleccionada)

                        evento1.set_nombre_evento(nombre_respuesta)
                        evento1.set_descripcion(descripcion_evento)
                        evento1.set_coste(coste)
                        evento1.set_platos(platos_de_este_evento)
                        factura_cumple.set_evento(evento1)
                        factura = factura_cumple
                        encendido2 = False
                    else:
                        print("No hay problema, te mostraremos de nuevo el menú de eventos")
                        encendido2 = True

                elif opcion_final == 2:
                    factura_meeting = Factura()
                    print("El Evento tiene un coste de 450.000$, ¿Desea continuar?")
                    print("1. Sí")
                    print("2. No")
                    respuesta_meeting = Utilidad.readInt()

                    if respuesta_meeting == 1:
                        print("¿Cuántos asistentes son?")
                        numero_invitados_meeting = Utilidad.readInt()
                        print("Digite el NIT de la empresa:")
                        nit = Utilidad.readInt()

                        platos_meeting = []
                        descripcion_evento = "Una empresa que demuestra su talento, seriedad y humanidad"
                        nombre_respuesta = "Meeting Empresarial"
                        coste = 450000

                        for elemento in Evento.get_eventos():
                            if elemento.get_nombre() == nombre_respuesta:
                                evento1 = elemento

                        print("""
                            Tenemos las siguientes opciones para acompañar el meeting:
                            1. Vino
                            2. Champaña
                        """)
                        opcion_vino_champana = Utilidad.readInt()
                        vino_champana_final = listado_platos_evento(evento1, numero_invitados_meeting, opcion_vino_champana)
                        platos_meeting.append(vino_champana_final)

                        if cliente.es_afiliado():
                            print("""
                                Vemos que eres afiliado, ¿deseas redimir tu derecho?
                                1. Sí
                                2. No
                            """)
                            opcion_cumple_final = Utilidad.readInt()

                            if opcion_cumple_final == 1:
                                for cocinero_en_cuestion in Trabajador.get_cocineros():
                                    if cocinero_en_cuestion.get_especialidad() == "Sonmerlier":
                                        cocinero_ocasion = cocinero_en_cuestion
                                        cocinero_en_cuestion.pago_extra_servicio(Evento.get_eventos(), cocinero_en_cuestion.get_especialidad())

                                        platos_afiliacion_meeting = []
                                        for plato in Plato.get_platos_varios():
                                            if plato.get_nombre() == "Bagget":
                                                platos_afiliacion_meeting.append(plato)
                                                plato.descontar_plato(numero_invitados_meeting)

                                        for plato in Plato.get_platos_varios():
                                            if plato.get_nombre() == "Queso mediterráneo":
                                                platos_afiliacion_meeting.append(plato)
                                                plato.descontar_plato(numero_invitados_meeting)

                                        print(f"Excelente, de nuestra parte os damos a nuestro mejor sommelier {cocinero_ocasion.get_nombre()} que ha de preparar el mejor {platos_afiliacion_meeting[1].get_nombre()} acompañado de unos deliciosos {platos_afiliacion_meeting[0].get_nombre()}")

                        evento1.set_nombre_evento(nombre_respuesta)
                        evento1.set_descripcion(descripcion_evento)
                        evento1.set_coste(coste)
                        evento1.set_platos(platos_meeting)
                        factura_meeting.set_evento(evento1)
                        factura = factura_meeting
                        encendido2 = False
                    else:
                        print("Te retornaremos al menú de eventos")
                        encendido2 = True


                elif opcion_final==3:
                    platos_afiliacion_gastro = []
                    gastronomias_nombres = ["Italiana", "Japonesa", "Marroquí", "Francesa"]
                    
                    print("""
                        El servicio tiene un costo de 345000, ¿deseas continuar?
                        1. Sí, por favor.
                        2. No, así está bien.
                    """)
                    respuesta = Utilidad.leer_int()
                    
                    if respuesta == 1:
                        print("""
                            Gastronomías mundiales, escoge la de tu preferencia:
                            1. Italiana
                            2. Japonesa
                            3. Marroquí
                            4. Francesa
                            Digite la opción de su preferencia:
                        """)
                        opcion_gastronomias = Utilidad.leer_int()
                        
                        print("¿Cuántos comensales son?")
                        numero_invitados_gastro = Utilidad.leer_int()
                        
                        tipo_evento = gastronomias_nombres[opcion_gastronomias - 1]
                        chef = cocinero_elegido(opcion_gastronomias, gastronomias_nombres)
                        print(f"El/la chef {chef.nombre} te va a acompañar en esta velada")
                        
                        final_gastro_evento = gastronomias_mundiales(opcion_gastronomias, gastronomias_nombres)
                        platos_pedidos = []
                        
                        print("Cuál de ellos gusta:")
                        leer = Utilidad.leer_int()
                        primer_plato = final_gastro_evento[leer - 1]
                        
                        print(f"Excelente, de ese plato tenemos {primer_plato.cantidad_de_plato} unidades, ¿cuántas desea?")
                        cantidad_pedida = Utilidad.leer_int()
                        
                        primer_plato.veces_pedido = cantidad_pedida
                        primer_plato.descontar_plato(cantidad_pedida)
                        platos_pedidos.append(primer_plato)
                        final_gastro_evento.remove(primer_plato)
                        
                        print("""
                            ¿Desea ordenar otros platos?
                            1. Sí, deseo ordenar más platos.
                            2. No, así está bien.
                        """)
                        leer2 = Utilidad.leer_int()
                        
                        if leer2 == 1:
                            while encendido1:
                                if final_gastro_evento:
                                    print("Por supuesto, aquí está de nuevo el menú con el resto de platos:")
                                    for idx, plato in enumerate(final_gastro_evento, start=1):
                                        print(f"{idx}. {plato.nombre}")
                                    
                                    print("Digite el que guste pedir:")
                                    leer3 = Utilidad.leer_int()
                                    
                                    if 1 <= leer3 <= len(final_gastro_evento):
                                        plato_seleccionado = final_gastro_evento[leer3 - 1]
                                        
                                        print(f"Listo, este plato cuenta con {plato_seleccionado.cantidad_de_plato} existencias, ¿cuántas desea?")
                                        cantidad_pedida = Utilidad.leer_int()
                                        
                                        if cantidad_pedida <= plato_seleccionado.cantidad_de_plato:
                                            plato_seleccionado.veces_pedido = cantidad_pedida
                                            plato_seleccionado.descontar_plato(cantidad_pedida)
                                            platos_pedidos.append(plato_seleccionado)
                                            final_gastro_evento.remove(plato_seleccionado)
                                        else:
                                            print(f"La cantidad de los pedidos excede la cantidad de existencias, por lo que asignaremos todos los platos disponibles.")
                                            plato_seleccionado.veces_pedido = plato_seleccionado.cantidad_de_plato
                                            plato_seleccionado.descontar_plato(plato_seleccionado.cantidad_de_plato)
                                            platos_pedidos.append(plato_seleccionado)
                                            final_gastro_evento.remove(plato_seleccionado)
                                        
                                        print("""
                                            ¿Desea seguir ordenando?
                                            1. Sí.
                                            2. No.
                                        """)
                                        respuesta2 = Utilidad.leer_int()
                                        
                                        if final_gastro_evento and respuesta2 == 1:
                                            encendido1 = True
                                        else:
                                            print("Un gusto haberle atendido.")
                                            encendido1 = False
                                    else:
                                        print("Digite un número dentro del rango expuesto.")
                                        encendido1 = True
                                else:
                                    print("Lo sentimos, pero no hay más platos para mostrarte.")
                                    break
                        else:
                            print("Agradecemos tu confianza.")
                        
                        if cliente.es_afiliado():
                            print("""
                                Vemos que eres afiliado, ¿deseas redimir tu derecho?
                                1. Sí
                                2. No
                            """)
                            opcion_cumple_final = Utilidad.leer_int()
                            
                            if opcion_cumple_final == 1:
                                for plato in Plato.get_platos_varios():
                                    if plato.tipo == tipo_evento:
                                        platos_afiliacion_gastro.append(plato)
                                        plato.descontar_plato(numero_invitados_gastro)
                                        print(f"Excelente, el chef {chef.nombre} ha preparado {numero_invitados_gastro} {plato.nombre}")
                        
                        evento_gastronomias = Evento("Gastronomías mundiales", 345000, platos_pedidos, tipo_evento)
                        evento_gastronomias.nombre_motivo = gastronomias_nombres[opcion_gastronomias - 1]
                        evento_gastronomias.coste = 345000
                        evento_gastronomias.descripcion = "Cata gastronómica"
                        
                        evento1 = evento_gastronomias
                        factura.evento = evento_gastronomias
                        encendido2 = False
                    else:
                        print("Te retornaremos al menú de eventos.")
                        encendido2 = True
                elif opcion_final == 4:
                    encendido2 = False
        else:
            encendido1 = False
    
    return factura        

##Metodos de la tercera interacción 

def listado_precios_factura(factura, reserva, dia_fin_de_semana):
    platos = factura.get_evento().get_platos()
    print("He aquí su consumo:")
    acomulado_total = 0
    
    for plato in platos:
        print(f"{plato.get_nombre()}   X{plato.get_veces_pedido()}   ... {plato.get_veces_pedido() * plato.get_precio()}")
        acomulado_total += plato.get_veces_pedido() * plato.get_precio()
    
    if dia_fin_de_semana:
        if reserva[3] > 20:
            acomulado_total += int(acomulado_total * 0.08)
        else:
            acomulado_total += int(acomulado_total * 0.03)
    
    acomulado_total += factura.get_evento().get_coste()
    
    print(f"El total de su factura es: {acomulado_total}")

def formato_factura_evento(restaurante, factura, reserva, dia_fin_de_semana):
    # Utilidad.limpiar_pantalla()
    evento_factura = factura.get_evento()
    
    print(f".............. {restaurante.get_nombre()} ..............")
    print(f"Cliente: {restaurante.get_clientes()[0].get_nombre()}")
    print(f"Cédula: {restaurante.get_clientes()[0].get_cedula()}")
    
    listado_precios_factura(factura, reserva, dia_fin_de_semana)
    
    if evento_factura.get_nombre() == "Meetigns Empresarial":
        print(evento_factura.get_descripcion())
    elif evento_factura.get_nombre() == "Cumpleanos Feliz":
        print(evento_factura.get_descripcion())
    elif evento_factura.get_nombre() == "Gastronomias mundiales":
        print(f".............. {evento_factura.get_descripcion()} ..............")
        
        if evento_factura.get_tipo_evento() == "Italiana":
            print(".....grazie per aver fiducia nel nostro ristorante....")
        elif evento_factura.get_tipo_evento() == "Japonesa":
            print("..Toten o shinrai shite itadaki arigatogozaimasu..")
        elif evento_factura.get_tipo_evento() == "Marroquí":
            print(".......شكرا لك على الثقة في مطعمنا........")
        elif evento_factura.get_tipo_evento() == "Francesa":
            print(".....Merci de faire confiance à notre restaurante")

def datos_hora_reserva(restaurante, factura):
    # Utilidad.limpiar_pantalla()
    print("""
        Estimado Cliente, el día de su reserva se encuentra entre Viernes, Sábado o Domingo:
        1. Si
        2. No
        """)
    
    dia_fin_de_semana = False
    reserva = []
    
    respuesta = Utilidad.readInt()
    if respuesta == 1:
        print("Listo, por ello tenemos un recargo del 8%")
        dia_fin_de_semana = True
        print("Estimado Cliente, nos regala la hora a la que desea el evento (HH:MM): ")
        hora_evento = input()
        fraccion = hora_evento.split(":")
        hora_evento_real = int(fraccion[0])
        reserva = restaurante.get_historial_reservas()[-1].get_fecha()
        reserva.append(hora_evento_real)
        print(reserva)
    elif respuesta == 2:
        print("Ten una maravillosa velada")
        reserva = None
    
    formato_factura_evento(restaurante, factura, reserva, dia_fin_de_semana)
    return None