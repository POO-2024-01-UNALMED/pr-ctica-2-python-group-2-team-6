from utilidad import Utilidad
from gestorAplicacion import *
import datetime
from datetime import datetime
import random

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
                                if datetime.datetime.now() - datetime.timedelta(days=30) < fecha_to_date_time < datetime.datetime.now() and fecha_to_date_time not in reservas_restaurante:
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
                ciudad = Ciudad(Utilidad.capitalize(Utilidad.read_string()))
                print("Por favor ingrese la cantidad de zonas que tiene la ciudad.")
                cantidad_zonas = Utilidad.readInt()
                # Este ciclo for se encarga de la creación de las zonas de la nueva ciudad.
                for i in range(1, cantidad_zonas + 1):
                    print(f"Por favor ingrese el nombre de la zona #{i}.")
                    nombre_zona = Utilidad.capitalize(Utilidad.read_string())
                    print(f"Por favor ingrese la población de la zona #{i}.")
                    poblacion_zona = Utilidad.readInt()
                    ciudad.get_zonas_ciudad().append(Zona(poblacion_zona, Utilidad.capitalize(nombre_zona), ciudad))
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
                nombre = Utilidad.capitalize(Utilidad.read_string())
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
                        if (fecha_to_date_time > datetime.datetime.now() - datetime.timedelta(days=30)) and (fecha_to_date_time < datetime.datetime.now()):
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
                nombre = Utilidad.capitalize(Utilidad.read_string())
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
            nombre_zona = Utilidad.capitalize(Utilidad.read_string())
            print("Por favor ingrese la población de la zona.")
            poblacion_zona = Utilidad.readInt()
            ciudad.get_zonas_ciudad().append(Zona(poblacion_zona, Utilidad.capitalize(nombre_zona), ciudad))
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
                            print(Utilidad.capitalize(plato.get_nombre()))

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
    nombre = Utilidad.capitalize(Utilidad.read_string())
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
    nombre_ingrediente = Utilidad.capitalize(Utilidad.read_string())
    
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
