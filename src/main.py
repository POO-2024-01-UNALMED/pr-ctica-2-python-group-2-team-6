from utilidad import Utilidad
from FieldFrame import FieldFrame
from uiMain.errorAplicacion import *

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
from gestorAplicacion.Usuario.cliente import Afiliacion
from gestorAplicacion.Usuario.persona import Persona
from gestorAplicacion.Usuario.trabajador import Trabajador
from baseDatos.serializador import Serializador
from baseDatos.deserializador import Deserializador

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

contador_clicks_cv = 0
contador_pasa_img_res = 0
funcionalidad_actual = 0
contador_platos = 0
contador_ingredientes = 0
cantidad_platos = 0
#Funcionalidad 1 Interacción 1

def generar_fechas():
    fechas_disponibles = []
    hoy = datetime.now().date()
    fin = hoy + relativedelta(months=6)
    while hoy <= fin:
        fechas = [hoy.year, hoy.month, hoy.day, 10, 12, 14, 16, 18, 20]
        fechas_disponibles.append(fechas)
        hoy += timedelta(days=1)
    
    return fechas_disponibles

def reservar_mesa():
    Ciudad.get_ciudades().pop(0)
    Zona.get_zonas().pop(0)
    comala = Ciudad("Comala")
    zona_centro = Zona(14, "Centro", comala)
    comala.agregar_zona(zona_centro)
    casa_stiven = Restaurante(10, "Casa Stiven", [], comala, zona_centro, False)
    zona_centro.get_restaurantes().append(casa_stiven)

    global label_procesos_bottom

    def f1_i1_seleccion_ciudad():
        global label_procesos_bottom
        label_procesos_mid.config(text="Seleccione la ciudad donde desea reservar su mesa.")

        def f1_i1_seleccion_zona():
            global label_procesos_bottom
            label_procesos_mid.config(text="Seleccione la zona donde desea reservar su mesa.")
            nombre_ciudad_elegida = label_procesos_bottom.valores[0] #Obtener valor seleccionado
            
            def f1_i1_seleccion_restaurante():
                global label_procesos_bottom
                label_procesos_mid.config(text="Selecciona el restaurante donde desea reservar su mesa")
                nombre_zona_elegida = label_procesos_bottom.valores[0] #Obtener valor seleccionado
                
                def llamar_interacciones():
                    global retorno_seleccion_mesa
                    #Definimos el restaurante seleccionado
                    restaurante_actual = None

                    nombre_restaurante_elegido = label_procesos_bottom.valores[0] #Obtener valor seleccionado
                    
                    for restaurante in Restaurante.get_restaurantes():
                        if restaurante.get_nombre() == nombre_restaurante_elegido:
                            restaurante_actual = restaurante
                            break
                    
                    #Llamamos a seleccion_mesa y le pasamos como parámetro el restaurante seleccionado.
                    seleccion_mesa(restaurante_actual)
                
                #Elegir restaurante donde reservar mesa
                zona_actual = None
                for zona in Zona.get_zonas(): 
                    if zona.get_nombre() == nombre_zona_elegida:
                        zona_actual = zona
                        break
                
                nombre_restaurantes = []
                for restaurante in zona_actual.get_restaurantes():
                    nombre_restaurantes.append(restaurante.get_nombre())

                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Restaurante"], tituloValores = "Valor ingresado", valores = [nombre_restaurantes], tipo = 2, comandoContinuar = llamar_interacciones, habilitado = [True])
                label_procesos_bottom.grid(sticky="nsew")
            
            #Elegir zona donde reservar mesa
            ciudad_actual = None
            for ciudad in Ciudad.get_ciudades(): 
                if ciudad.get_nombre() == nombre_ciudad_elegida:
                    ciudad_actual = ciudad
                    break
            
            nombre_zonas = []
            for zona in ciudad_actual.get_zonas_ciudad():
                if zona.get_restaurantes() != []:
                    nombre_zonas.append(zona.get_nombre())
            
            
            print("Zonas:", nombre_zonas)


            print("Zonas:", nombre_zonas)

            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Zona"], tituloValores = "Valor ingresado", valores = [nombre_zonas], tipo = 2, comandoContinuar = f1_i1_seleccion_restaurante, habilitado = [True])
            label_procesos_bottom.grid(sticky="nsew")

        #Elegir ciudad donde reservar mesa
        nombre_ciudades = []
        for ciudad in Ciudad.get_ciudades(): 
            nombre_ciudades.append(ciudad.get_nombre())
        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Ciudad"], tituloValores = "Valor ingresado", valores = [nombre_ciudades], tipo = 2, comandoContinuar = f1_i1_seleccion_zona, habilitado = [True])
        label_procesos_bottom.grid(sticky="nsew")
    
    label_procesos_mid.config(text="Seleccione sí o no dependiendo de si quiere continuar")
    #Sí o No desea continuar con la funcionalidad 1
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea", criterios=None, tituloValores="continuar?", tipo=1, comandoContinuar=f1_i1_seleccion_ciudad, comandoCancelar=funcionalidad_0)
    label_procesos_bottom.grid(sticky="nsew")

def seleccion_mesa(restaurante):
    Ciudad.get_ciudades().pop(0)
    Zona.get_zonas().pop(0)
    comala = Ciudad("Comala")
    zona_centro = Zona(14, "Centro", comala)
    comala.agregar_zona(zona_centro)
    restaurante = Restaurante(10, "Casa Stiven", [], comala, zona_centro, False)
    zona_centro.get_restaurantes().append(restaurante)

    disposicion = [ 
        ["╔", "═", "╦", "╗", "║", "╠", "╬", "╣", "╚", "╩", "╝", " "], 
        ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B"], 
        ["B", " ", "V", " ", "V", " ", "V", " ", "V", "B"], 
        ["W", " ", " ", " ", " ", " ", " ", " ", " ", "W"], 
        ["B", " ", "T", " ", "T", " ", "T", " ", "T", "B"], 
        ["B", " ", " ", " ", " ", " ", " ", " ", " ", "B"], 
        ["B", " ", "T", " ", "T", " ", "T", " ", " ", "B"], 
        ["B", " ", " ", " ", " ", " ", " ", " ", " ", "B"], 
        ["W", " ", "T", " ", "T", " ", "T", " ", " ", "W"], 
        ["B", " ", " ", " ", " ", " ", " ", " ", " ", "B"], 
        ["B", "B", "B", "B", "B", "B", "B", "E", "B", "B"]
    ]


    restaurante.set_disposicion(disposicion)
    restaurante.set_capacidad(1234)

    # Mesas
    mesa1 = Mesa(0, 3, 2, True, 4)
    mesa1.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa1)
    restaurante.get_mesas().append(mesa1)

    mesa2 = Mesa(0, 5, 2, True, 4)
    mesa2.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa2)
    restaurante.get_mesas().append(mesa2)

    mesa3 = Mesa(0, 7, 2, True, 4)
    mesa3.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa3)
    restaurante.get_mesas().append(mesa3)

    mesa4 = Mesa(0, 9, 2, True, 4)
    mesa4.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa4)
    restaurante.get_mesas().append(mesa4)

    mesa5 = Mesa(0, 3, 4, False, 4)
    mesa5.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa5)
    restaurante.get_mesas().append(mesa5)

    mesa6 = Mesa(0, 5, 4, False, 4)
    mesa6.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa6)
    restaurante.get_mesas().append(mesa6)

    mesa7 = Mesa(0, 7, 4, False, 4)
    mesa7.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa7)
    restaurante.get_mesas().append(mesa7)

    mesa8 = Mesa(0, 9, 4, False, 4)
    mesa8.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa8)
    restaurante.get_mesas().append(mesa8)

    mesa9 = Mesa(0, 3, 6, False, 4)
    mesa9.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa9)
    restaurante.get_mesas().append(mesa9)

    mesa10 = Mesa(0, 5, 6, False, 4)
    mesa10.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa10)
    restaurante.get_mesas().append(mesa10)

    mesa11 = Mesa(0, 7, 6, False, 4)
    mesa11.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa11)
    restaurante.get_mesas().append(mesa11)

    mesa12 = Mesa(0, 3, 8, False, 4)
    mesa12.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa12)
    restaurante.get_mesas().append(mesa12)

    mesa13 = Mesa(0, 5, 8, False, 4)
    mesa13.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa13)
    restaurante.get_mesas().append(mesa13)

    mesa14 = Mesa(0, 7, 8, False, 4)
    mesa14.set_restaurante(restaurante)
    restaurante.get_casillas().append(mesa14)
    restaurante.get_mesas().append(mesa14)

    for mesa in restaurante.get_mesas():
        mesa.set_fechas_disponibles(generar_fechas())
    
    restaurante.actualizar_fechas_disponibles()

    # Casillas
    casilla1 = Casilla(1, 1, 3)
    restaurante.get_casillas().append(casilla1)

    casilla2 = Casilla(1, 1, 8)
    restaurante.get_casillas().append(casilla2)

    casilla3 = Casilla(1, 10, 3)
    restaurante.get_casillas().append(casilla3)

    casilla4 = Casilla(1, 10, 8)
    restaurante.get_casillas().append(casilla4)

    casilla5 = Casilla(2, 8, 10)
    restaurante.get_casillas().append(casilla5)


    clientes = []

    global label_procesos_bottom
    label_procesos_mid.config(text="Ingrese sus datos personales.\nEn caso de no tener vehículo ingrese únicamente el número 0.")
    
    def f1_i1_datos_clientes():
        global label_procesos_bottom
        nombre_cliente = label_procesos_bottom.valores[0]
        try:
            cedula_cliente = int(label_procesos_bottom.valores[1])
        except:
            messagebox.showerror("Error: Tipo de dato erróneo", "Se intentó ingresar un dato erróneo en la el dato: Cédula")
        placa_cliente = label_procesos_bottom.valores[2]
        if placa_cliente == "0":
            placa_cliente = "Ninguna"
        try:
            num_acompanantes = int(label_procesos_bottom.valores[3])
        except:
            messagebox.showerror("Error: Tipo de dato erróneo", "Se intentó ingresar un dato erróneo en la el dato: Número de Acompañantes")
        
        cliente = Cliente(nombre_cliente, cedula_cliente, placa_cliente, Factura())
        

        if Utilidad.existe_cliente(cliente):
            cliente = Utilidad.cliente_cedula(cliente)
        else:
            restaurante.get_clientes().append(cliente)

        clientes.append(cliente)

        def f1_i1_preferencias():
            global label_procesos_bottom
            tipo_mesa_seleccionado = label_procesos_bottom.valores[0]
            preferencia_seleccionada = label_procesos_bottom.valores[1]
            for cliente in clientes:
                cliente.set_restaurante(restaurante)
            
            tipo_mesa = False

            if tipo_mesa_seleccionado == "Estándar":
                if not any(mesa.is_vip() == tipo_mesa for mesa in restaurante.get_mesas()):
                    tipo_mesa = True
            elif tipo_mesa_seleccionado == "VIP":
                tipo_mesa = True
                if not any(mesa.is_vip() == tipo_mesa for mesa in restaurante.get_mesas()):
                    tipo_mesa = False
            
            mesas_elegidas = []

            if preferencia_seleccionada in ["Puerta", "Ventana"]: # Eleccion2 es la preferencia de cercanía
                mesas_elegidas = Utilidad.calcular_distancia(restaurante, preferencia_seleccionada, tipo_mesa)
            elif preferencia_seleccionada == "Ninguna":
                for mesa in restaurante.get_mesas():
                    mesa.set_distancia_puerta(0)
                    mesa.set_distancia_ventana(0)
            
            seleccion_fecha(restaurante, tipo_mesa, mesas_elegidas, clientes)
        
        if num_acompanantes > 0:
            num_acompanantes = min(num_acompanantes, 4)
            criterios_acompanantes = []
            habilitado = []

            for i in range(num_acompanantes):
                criterios_acompanantes.append(f"Nombre Acompañante #{i+1}")
                criterios_acompanantes.append(f"Cédula Acompañante #{i+1}")
                habilitado.append(True)
                habilitado.append(True)
            
            
            print(criterios_acompanantes, habilitado)


            print(criterios_acompanantes, habilitado)

            def f1_i1_datos_acompanantes():
                global label_procesos_bottom
                nombres_acompanantes = []
                cedulas_acompanantes = []
                # Guardar datos acompañantes
                for i in range(len(label_procesos_bottom.valores)):
                    if i % 2 == 0:
                        nombres_acompanantes.append(label_procesos_bottom.valores[i])
                    else:
                        try:
                            comprobantes = int(label_procesos_bottom.valores[i]) in cedulas_acompanantes
                        except:
                            messagebox.showerror("Error: Tipo de dato erróneo", "Se intentó ingresar un dato erróneo en la el dato: Cédula")
                        if comprobantes:
                            raise ExcepcionCedulasRepetidas(label_procesos_bottom.valores[i])
                        else:
                            cedulas_acompanantes.append(int(label_procesos_bottom.valores[i]))
                                
                for i in range(len(nombres_acompanantes)):
                    acompanante = Cliente(nombres_acompanantes[i], cedulas_acompanantes[i])
                    if Utilidad.existe_cliente(acompanante):
                        acompanante = Utilidad.cliente_cedula(acompanante)
                    else:
                        restaurante.get_clientes().append(acompanante)
                    clientes.append(acompanante)
                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Tipo mesa", "Cercanía"], tituloValores = "Valor ingresado", valores=[["Estándar", "VIP"], ["Puerta", "Ventana", "Ninguna"]], tipo = 2, habilitado = [True, True], comandoContinuar=f1_i1_preferencias)
                label_procesos_bottom.grid(sticky="nsew")

            #Preguntar datos acompañanates
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = criterios_acompanantes, tituloValores = "Valor ingresado", tipo = 0, habilitado = habilitado, comandoContinuar=f1_i1_datos_acompanantes)
            label_procesos_bottom.grid(sticky="nsew")

        else:
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Tipo mesa", "Cercanía"], tituloValores = "Valor ingresado", valores=[["Estándar", "VIP"], ["Puerta", "Ventana", "Ninguna"]], tipo = 2, habilitado = [True, True], comandoContinuar=f1_i1_preferencias)
            label_procesos_bottom.grid(sticky="nsew")
    
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Nombre", "Cédula", "Placa Vehículo", "Número de Acompañantes"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True, True, True, True], comandoContinuar=f1_i1_datos_clientes)
    label_procesos_bottom.grid(sticky="nsew")

def continuar_seleccion_mesa(restaurante, fecha_elegida_reservar_mesa, tipo_mesa, clientes):
    global label_procesos_bottom, retorno_seleccion_mesa
    mesas_disponibles = []
    for mesa in restaurante.get_mesas():
        for fecha in mesa.get_fechas_disponibles():

            if (fecha[0] == fecha_elegida_reservar_mesa[0] and fecha[1] == fecha_elegida_reservar_mesa[1] and
                    fecha[2] == fecha_elegida_reservar_mesa[2] and mesa.is_vip() == tipo_mesa and len(fecha) > 3):
                mesas_disponibles.append(mesa.get_num_mesa())

    def f1_i1_escoger_num_mesa():
        ### VOY ACÁ ###
        global label_procesos_bottom
        mesa_elegida = int(label_procesos_bottom.valores[0])

        for mesa in restaurante.get_mesas():
            if mesa.get_num_mesa() == mesa_elegida:
                mesa_elegida = mesa
                break
        
        indice_fecha_elegida = next(i for i, fecha in enumerate(mesa_elegida.get_fechas_disponibles())
                                    if fecha[1] == fecha_elegida_reservar_mesa[1] and fecha[2] == fecha_elegida_reservar_mesa[2])

        mesa_elegida.set_ultima_fecha_reserva(indice_fecha_elegida)

        horarios_disponibles = []
        for i in range(3, len(mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida])):
            horarios_disponibles.append(f"{mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida][i]}:00")

        def f1_i1_escoger_horario():
            global label_procesos_bottom
            hora_elegida = int(label_procesos_bottom.valores[0].replace(":00", ""))
            if hora_elegida == 10:
                hora_elegida = 1
            elif hora_elegida == 12:
                hora_elegida = 2
            elif hora_elegida == 14:
                hora_elegida = 3
            elif hora_elegida == 16:
                hora_elegida = 4
            elif hora_elegida == 18:
                hora_elegida = 5
            elif hora_elegida == 20:
                hora_elegida = 6

            fecha_elegida_reservar_mesa.append(mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida][hora_elegida + 2])
            reserva = Reserva(clientes, fecha_elegida_reservar_mesa)
            reserva.set_restaurante(restaurante)
            mesa_elegida.get_fechas_disponibles()[indice_fecha_elegida].pop(hora_elegida + 2)
            restaurante.get_historial_reservas().append(reserva)

            for cliente in clientes:
                cliente.set_reserva(reserva)
                cliente.set_mesa(mesa_elegida)
                cliente.set_factura(Factura(Pedido()))

            extras_reserva(retorno_seleccion_mesa)

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Horario mesa"], tituloValores = "Valor ingresado", valores=[horarios_disponibles], tipo = 2, habilitado = [True], comandoContinuar=f1_i1_escoger_horario)
        label_procesos_bottom.grid(sticky="nsew")
    
    label_procesos_mid.config(text="Seleccione el número de la mesa de su preferencia.") 
    #Idea: Agregar pop up con la distribución del restaurante
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Número mesa"], tituloValores = "Valor ingresado", valores=[mesas_disponibles], tipo = 2, habilitado = [True], comandoContinuar=f1_i1_escoger_num_mesa)
    label_procesos_bottom.grid(sticky="nsew")

    retorno_seleccion_mesa = clientes[0]

def seleccion_fecha(restaurante, tipo_mesa, mesas_elegidas, clientes):
    global label_procesos_bottom
    anios = []
    meses = []

    for fechas_mes in restaurante.get_fechas_disponibles():
        if fechas_mes[0] not in anios:
            anios.append(fechas_mes[0])
    
    def f1_i1_escoger_mesa():
        global label_procesos_bottom
        anio_elegido = int(label_procesos_bottom.valores[2])

        for fechas_mes in restaurante.get_fechas_disponibles():
            if anios[anio_elegido - 1] == fechas_mes[0] and fechas_mes[1] not in meses:
                meses.append(fechas_mes[1])
            
        anio_elegido = anios[anio_elegido - 1]

        def f1_i1_escoger_dia():
            global label_procesos_bottom
            mes_elegido = int(label_procesos_bottom.valores[0])

            indice_mes = 0

            for i in range(len(restaurante.get_fechas_disponibles())):
                if mes_elegido == restaurante.get_fechas_disponibles()[i][1]:
                    indice_mes = i
                    break
            
            def f1_i1_definir_fecha_elegida():
                global label_procesos_bottom
                dia_elegido = int(label_procesos_bottom.valores[0])
                fecha_elegida_reservar_mesa = [anio_elegido, mes_elegido, dia_elegido]
                continuar_seleccion_mesa(restaurante, fecha_elegida_reservar_mesa, tipo_mesa, clientes)

            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Día"], tituloValores = "Valor ingresado", tipo = 2, valores=[restaurante.get_fechas_disponibles()[indice_mes][2::]], habilitado = [True], comandoContinuar=f1_i1_definir_fecha_elegida)
            label_procesos_bottom.grid(sticky="nsew")
        
        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Mes"], tituloValores = "Valor ingresado", tipo = 2, valores=[meses], habilitado = [True], comandoContinuar=f1_i1_escoger_dia)
        label_procesos_bottom.grid(sticky="nsew")
    
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Año 1", "Año 2", "Año"], tituloValores = "Valor ingresado", tipo = 2, valores=[[anios[0]], [anios[1]], [1,2]], habilitado = [False, False, True], comandoContinuar=f1_i1_escoger_mesa)
    label_procesos_bottom.grid(sticky="nsew")

#Funcionalidad 1 Interacción 2

def extras_reserva(cliente):
    global label_procesos_bottom, retorno_extras_reserva
    restaurante = cliente.get_restaurante()
    retorno_extras_reserva = restaurante
    label_procesos_mid.config(text="Desde la cadena de restaurantes ofrecemos los servicios de\nreserva de parqueadero y decoraciones para la mesa.\nElija un servicio en caso de necesitarlo:")

    def f1_i2_decoraciones():
        global label_procesos_bottom
        tipo_decoracion_elegido = label_procesos_bottom.valores[0]
        if tipo_decoracion_elegido == "Reserva de Parqueadero":
            tipo_decoracion_elegido = 1
        elif tipo_decoracion_elegido == "Decoraciones para la mesa":
            tipo_decoracion_elegido = 2
        else:
            tipo_decoracion_elegido = 3
        
        if tipo_decoracion_elegido == 1:
            label_procesos_mid.config(text="Reserva de Parqueadero")
            placa = ""
            if cliente.get_afiliacion() == Afiliacion.NINGUNA:
                def f1_i2_parqueo_ninguna():
                    cliente.get_factura().aumentar_valor(10000)
                    indice_celda = restaurante.get_parqueadero().index(False)
                    celda_parqueo = indice_celda + 1
                    if cliente.get_placa_vehiculo() != "Ninguna":
                        placa = cliente.get_placa_vehiculo()
                
                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="El servicio cuesta 10000.", criterios=None, tituloValores="¿Desea continuar?", tipo=1, comandoContinuar=f1_i2_parqueo_ninguna, comandoCancelar=extras_reserva(cliente))
                label_procesos_bottom.grid(sticky="nsew")
            else:
                indice_celda = restaurante.get_parqueadero().index(False)
                celda_parqueo = indice_celda + 1
                if cliente.get_placa_vehiculo() != "Ninguna":
                    placa = cliente.get_placa_vehiculo()
                pago_anticipado(cliente.get_restaurante())

        elif tipo_decoracion_elegido == 2:
            label_procesos_mid.config(text="Decoraciones para la mesa")

            if cliente.get_afiliacion() != Afiliacion.NINGUNA:
                cliente.get_factura().aumentar_valor(42500)
            else:
                cliente.get_factura().aumentar_valor(50000)
            
            def f1_i2_elegir_decoracion():
                global label_procesos_bottom, cargo_extra2
                decoracion_elegida = label_procesos_bottom.valores[0]
                if decoracion_elegida == "Cena romántica (30000$)":
                    decoracion_elegida = 1
                elif decoracion_elegida == "Graduación (1200$ + 5000$ por cada comensal)":
                    decoracion_elegida = 2
                elif decoracion_elegida == "Descubrimiento (1200$ + 6000$ por cada comensal)":
                    decoracion_elegida = 3
                
                if decoracion_elegida == 1:
                    print("Cena")
                    # restaurante.restar_de_bodega(indice_bodega_items("rosa", restaurante), 1)
                    # restaurante.restar_de_bodega(indice_bodega_items("vela", restaurante), 3)
                    # restaurante.restar_de_bodega_ingrediente(indice_bodega_ingredientes("vino blanco", restaurante), 1)
                    cliente.get_factura().aumentar_valor(30000)
                    pago_anticipado(cliente.get_restaurante())
                elif decoracion_elegida == 2:
                    print("Graduación")
                    # restaurante.restar_de_bodega(indice_bodega_items("globo negro", restaurante), 3)
                    # restaurante.restar_de_bodega(indice_bodega_items("globo dorado", restaurante), 3)
                    # restaurante.restar_de_bodega(indice_bodega_items("birrete", restaurante), cliente.get_mesa().get_clientes().size())
                    cargo_birretes = 5000 * len(cliente.get_mesa().get_clientes())
                    cliente.get_factura().aumentar_valor(1200 + cargo_birretes)
                    pago_anticipado(cliente.get_restaurante())
                elif decoracion_elegida == 3:
                    def f1_i2_cobrar():
                        global cargo_extra2
                        genero_elegido = label_procesos_bottom.valores[0]
                        if genero_elegido == "Niño":
                            genero_elegido = 1
                        elif genero_elegido == "Niña":
                            genero_elegido = 2
                        if genero_elegido == 1:
                            pass
                            # restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo azul", restaurante), 3)
                            # restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo blanco", restaurante), 3)
                            # restaurante.restar_de_bodega(Utilidad.indice_bodega_items("angel varon", restaurante), cliente.get_mesa().get_clientes().size())
                        elif genero_elegido == 2:
                            pass
                            # restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo rosado", restaurante), 3)
                            # restaurante.restar_de_bodega(Utilidad.indice_bodega_items("globo blanco", restaurante), 3)
                            # restaurante.restar_de_bodega(Utilidad.indice_bodega_items("angel femenino", restaurante), cliente.get_mesa().get_clientes().size())

                        cargo_angeles = 6000 * len(cliente.get_mesa().get_clientes())
                        cliente.get_factura().aumentar_valor(1200 + cargo_angeles)

                        pago_anticipado(cliente.get_restaurante())
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Género"], tituloValores = "Valor ingresado", valores = [["Niño", "Niña"]], tipo = 2, comandoContinuar = f1_i2_cobrar, habilitado = [True])
                    label_procesos_bottom.grid(sticky="nsew")
            
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Elegir decoración"], tituloValores = "Valor ingresado", valores = [["Cena romántica (30000$)", "Graduación (1200$ + 5000$ por cada comensal)", "Descubrimiento (1200$ + 6000$ por cada comensal)"]], tipo = 2, comandoContinuar = f1_i2_elegir_decoracion, habilitado = [True])
            label_procesos_bottom.grid(sticky="nsew")

            print(cliente.get_factura())
            #Llamar tercera

        else:
            pago_anticipado(cliente.get_restaurante())

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Decoraciones"], tituloValores = "Valor ingresado", valores = [["Reserva de Parqueadero", "Decoraciones para la mesa", "No desea ningún servicio extra"]], tipo = 2, comandoContinuar = f1_i2_decoraciones, habilitado = [True])
    label_procesos_bottom.grid(sticky="nsew")

#Funcionalidad 1 Interacción 3

def pago_anticipado(restaurante):
    global label_procesos_bottom
    reserva = restaurante.get_historial_reservas()[-1]
    clientes = reserva.get_clientes()
    factura = clientes[0].get_factura()

    def f1_i3_continuar_pago():
        global label_procesos_bottom
        pagar_ya = label_procesos_bottom.valores[0]

        if pagar_ya == 1:
            if clientes[0].get_afiliacion() == Afiliacion.NINGUNA:
                def f1_i3_afiliarse():
                    afiliarse = label_procesos_bottom.valores[0]
                    if afiliarse == 1:
                        factura.aumentar_valor(13500)  # Aplicar 10% de descuento al valor de la reserva.
                        pagar_reserva(restaurante, reserva, clientes, factura)
                    else:
                        factura.aumentar_valor(15000)
                        pagar_reserva(restaurante, reserva, clientes, factura)
                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea afiliarse?", criterios=None, tituloValores="Recibirá un descuento si lo hace.", tipo=1, comandoContinuar=f1_i3_afiliarse, comandoCancelar=funcionalidad_0)
                label_procesos_bottom.grid(sticky="nsew")

            else:
                factura.aumentar_valor(14300)  # Aplicar 5% de descuento al valor de la reserva.
                pagar_reserva(restaurante, reserva, clientes, factura)
            clientes[0].get_factura().set_pago_preconsumo(True)
        else:
            factura.aumentar_valor(15000)
            confirmar_reserva(restaurante, reserva, clientes)
            clientes[0].get_factura().set_pago_preconsumo(False)
    
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea pagar ya", criterios=None, tituloValores="mismo su reserva?", tipo=1, comandoContinuar=f1_i3_continuar_pago, comandoCancelar=funcionalidad_0)
    label_procesos_bottom.grid(sticky="nsew")

def pagar_reserva(restaurante, reserva, clientes, factura):
    global label_procesos_bottom
    if confirmar_reserva(restaurante, reserva, clientes):
        escoger_metodo_pago(clientes[0])
        factura.calcular_valor()
        def f1_i3_confirmar_pago():
            clientes[0].get_factura().set_valor(0)
        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea confirmar la transacción", criterios=None, tituloValores=f"con un valor de: {factura.get_valor()}?", tipo=1, comandoContinuar=f1_i3_confirmar_pago, comandoCancelar=funcionalidad_0)
        label_procesos_bottom.grid(sticky="nsew")

def confirmar_reserva(restaurante, reserva, clientes):
    global label_procesos_bottom
    # confirmada = False
    fecha_intento = datetime.now()
    restaurante.get_intentos_reserva().append([fecha_intento.year, fecha_intento.month, fecha_intento.day])

    def f1_i3_confirmar_final():
        global label_procesos_bottom
        confirmar = label_procesos_bottom.valores[0]
        if confirmar == 1:
            # confirmada = True
            print("Reserva confirmada.")
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Reserva confirmada", tituloValores="" , criterios=[f"Su código de reserva es: {reserva.get_codigo_reserva()}"], tipo=3, comandoContinuar=funcionalidad_0)
            label_procesos_bottom.grid(sticky="nsew")
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

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea confirmar", criterios=None, tituloValores=f"la reservación?", tipo=1, comandoContinuar=f1_i3_confirmar_final, comandoCancelar=f1_i3_confirmar_final)
    label_procesos_bottom.grid(sticky="nsew")

#Funcionalidad 4 Interacción 1

def agregar_sede():
    Ciudad.get_ciudades().pop(0)
    Zona.get_zonas().pop(0)
    comala = Ciudad("Comala")
    zona_centro = Zona(14, "Centro", comala)
    comala.agregar_zona(zona_centro)
    restaurante_sti = Restaurante(10, "Casa Stiven", [], comala, zona_centro, False)
    zona_centro.get_restaurantes().append(restaurante_sti)
    comala.get_restaurantes().append(restaurante_sti)

    global label_procesos_bottom
    restaurante_creado = Restaurante()

    def f4_i1_continuar_interaccion():
        restaurante = elegir_zona(restaurante_creado)

    label_procesos_mid.config(text="Seleccione sí o no dependiendo de si quiere continuar")
    #Sí o No desea continuar con la funcionalidad 4
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea", criterios=None, tituloValores="continuar?", tipo=1, comandoContinuar=f4_i1_continuar_interaccion, comandoCancelar=funcionalidad_0)
    label_procesos_bottom.grid(sticky="nsew")

def elegir_zona(restaurante):
    global label_procesos_bottom

    def f4_i1_establecer_parametros():
        global label_procesos_bottom
        nombre_ciudad_elegida = label_procesos_bottom.valores[0]
        print(nombre_ciudad_elegida)
        ciudad_actual = None
        for ciudad in Ciudad.get_ciudades(): 
            if ciudad.get_nombre() == nombre_ciudad_elegida:
                ciudad_actual = ciudad
                break
        print(ciudad_actual)
        
        if not ciudad_actual.get_restaurantes():
            print(ciudad_actual.get_zonas_ciudad())
            parametros_basicos(ciudad_actual, restaurante)
        else:
            def f4_i1_confirmar_establecer_parametros():
                global label_procesos_bottom
                continuar_proceso = label_procesos_bottom.valores[0]

                if continuar_proceso == 1:
                    parametros_basicos(ciudad_actual, restaurante)

            label_procesos_mid.config(text="Seleccione sí o no.")
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="La ciudad ya tiene restaurantes.", criterios=None, tituloValores="¿Desea continuar igualmente?", tipo=1, comandoContinuar=f4_i1_confirmar_establecer_parametros, comandoCancelar=funcionalidad_0)
            label_procesos_bottom.grid(sticky="nsew")

    label_procesos_mid.config(text="Seleccione la ciudad donde desea agregar la sede.")
    nombre_ciudades = []
    for ciudad in Ciudad.get_ciudades(): 
        nombre_ciudades.append(ciudad.get_nombre())

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Ciudad"], tituloValores = "Valor ingresado", valores = [nombre_ciudades], tipo = 2, comandoContinuar = f4_i1_establecer_parametros, habilitado = [True])
    label_procesos_bottom.grid(sticky="nsew")

    return restaurante

#Este método obtiene promedios necesarios para luego
def obtener_promedios():
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
def parametros_basicos(ciudad, restaurante):
    global label_procesos_bottom

    def f4_i1_continuar_parametros():
        global label_procesos_bottom

        nombre_zona_elegida = label_procesos_bottom.valores[0]

        zona_actual = None
        for zona in Zona.get_zonas(): 
            if zona.get_nombre() == nombre_zona_elegida:
                zona_actual = zona
                break

        # Se evalúa si existen restaurantes enlazados a esta zona.
        if not zona_actual.get_restaurantes():  # Si la zona elegida no tiene restaurantes
            # Se enlaza la ciudad al restaurante
            restaurante.set_ciudad(ciudad)
            # Se enlaza la zona al restaurante
            restaurante.set_zona(zona_actual)
            # Se enlaza el restaurante a la zona
            zona_actual.get_restaurantes().append(restaurante)
            # Se enlaza el restaurante a la ciudad
            ciudad.get_restaurantes().append(restaurante)

            def f4_i1_establecer_parametros():
                global label_procesos_bottom
                restaurante.set_nombre(label_procesos_bottom.valores[0].capitalize())

                def f4_i1_terminar_parametros():
                    global label_procesos_bottom
                    if label_procesos_bottom.valores[0] == 1:
                        restaurante.set_zona_vip(True)
                    elif label_procesos_bottom.valores[0] == 2:
                        restaurante.set_zona_vip(False)
                    restaurante.set_calificacion(int((random.random() * 5) + 1))
                    print(restaurante)
                
                label_procesos_mid.config(text="Seleccione sí o no.")

                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios=f"¿{label_procesos_bottom.valores[0].capitalize()}", criterios=None, tituloValores="tendrá zona VIP?", tipo=1, comandoContinuar=f4_i1_terminar_parametros, comandoCancelar=f4_i1_terminar_parametros)
                label_procesos_bottom.grid(sticky="nsew")

            label_procesos_mid.config(text="Escriba el nombre del nuevo restaurante.")
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Nombre restaurante"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True], comandoContinuar=f4_i1_establecer_parametros)
            label_procesos_bottom.grid(sticky="nsew")

        else:  # Si la zona elegida tiene restaurantes
            print("Entró al análisis")
            # Análisis de reservas
            reservas_ultimos_treinta = []
            intentos_ultimos_treinta = []
            mesas_restaurantes = []

            reservas_satisfactorias = 0
            total_intentos = 0

            # Agregamos los datos que corresponden a los últimos 30 días de funcionamiento de los restaurantes de la ciudad correspondiente.
            for restaurante_zona in zona_actual.get_restaurantes():
                print(restaurante_zona)
                reservas_restaurante = []
                intentos_restaurante = []
                for reserva in restaurante_zona.get_historial_reservas():
                    if reserva.is_satisfaccion():
                        reservas_satisfactorias += 1
                    fecha_to_date_time = datetime.datetime(reserva.get_fecha()[0], reserva.get_fecha()[1], reserva.get_fecha()[2], reserva.get_fecha()[3], 0)
                    if (fecha_to_date_time > datetime.now() - datetime.timedelta(days=30)) and (fecha_to_date_time < datetime.now()):
                        if fecha_to_date_time not in reservas_restaurante:
                            reservas_restaurante.append(reserva)
                
                print(restaurante_zona.get_intentos_reserva())
                if restaurante_zona.get_intentos_reserva() is not []:
                    for intento in restaurante_zona.get_intentos_reserva():
                        total_intentos += 1
                        fecha_to_date = datetime.date(intento[0], intento[1], intento[2])
                        if (fecha_to_date > datetime.date.today() - datetime.timedelta(days=30)) and (fecha_to_date < datetime.date.today()):
                            intentos_restaurante.append(intento)

                for mesa in restaurante_zona.get_mesas():
                    print(mesa)
                    mesas_restaurantes.append(mesa)

                reservas_ultimos_treinta.extend(reservas_restaurante)
                intentos_ultimos_treinta.extend(intentos_restaurante)

            # Demanda por Hora
            intentos_reserva = len(intentos_ultimos_treinta)
            horas_funcionamiento = len(reservas_ultimos_treinta)
            total_mesas = len(mesas_restaurantes)

            if total_mesas >= 0 and horas_funcionamiento >= 0:
                if total_mesas == 0:
                    total_mesas = 1
                if horas_funcionamiento == 0:
                    horas_funcionamiento = 1
                print("Entró al análisis profundo")
                demanda_por_hora = (intentos_reserva / horas_funcionamiento) / total_mesas

                # Satisfacción del Cliente
                satisfaccion_del_cliente = (reservas_satisfactorias / total_mesas) * 100

                # Conclusión Análisis
                conclusion = (demanda_por_hora + satisfaccion_del_cliente) / 2

                def f4_i1_crear_igualmente():
                    global label_procesos_bottom
                    # Se enlaza la ciudad al restaurante
                    restaurante.set_ciudad(ciudad)
                    # Se enlaza la zona al restaurante
                    restaurante.set_zona(zona_actual)
                    # Se enlaza el restaurante a la zona
                    zona_actual.get_restaurantes().append(restaurante)
                    # Se enlaza el restaurante a la ciudad
                    ciudad.get_restaurantes().append(restaurante)

                    def f4_i1_establecer_parametros():
                        global label_procesos_bottom
                        restaurante.set_nombre(label_procesos_bottom.valores[0].capitalize())

                        def f4_i1_terminar_parametros():
                            global label_procesos_bottom
                            if label_procesos_bottom.valores[0] == 1:
                                restaurante.set_zona_vip(True)
                            elif label_procesos_bottom.valores[0] == 2:
                                restaurante.set_zona_vip(False)
                            restaurante.set_calificacion(int((random.random() * 5) + 1))
                            establecer_disposicion(restaurante)
                        
                        label_procesos_mid.config(text="Seleccione sí o no.")

                        label_procesos_bottom.destroy()
                        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios=f"¿{label_procesos_bottom.valores[0].capitalize()}", criterios=None, tituloValores="tendrá zona VIP?", tipo=1, comandoContinuar=f4_i1_terminar_parametros, comandoCancelar=f4_i1_terminar_parametros)
                        label_procesos_bottom.grid(sticky="nsew")

                    label_procesos_mid.config(text="Escriba el nombre del nuevo restaurante.")
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Nombre restaurante"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True], comandoContinuar=f4_i1_establecer_parametros)
                    label_procesos_bottom.grid(sticky="nsew")

                if conclusion < 0.5:
                    label_procesos_mid.config(text="Seleccione sí o no dependiendo de si quiere continuar.")
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Según el algoritmo de análisis hecho, no es recomendable crear un nuevo restaurante en " + ciudad.get_nombre() + ".\nEsto se debe a que los restaurantes de la ciudad tienen un flujo bajo de clientes y\nno están cumpliendo con las expectativas de la gran mayoría de sus usuarios.\nTeniendo esto en cuenta, ¿Desea crear una nueva sede?", criterios=None, tituloValores="", tipo=1, comandoContinuar=f4_i1_crear_igualmente, comandoCancelar=funcionalidad_0)
                    label_procesos_bottom.grid(sticky="nsew")

                elif 0.5 <= conclusion <= 0.7:
                    label_procesos_mid.config(text="Seleccione sí o no dependiendo de si quiere continuar.")
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Según el algoritmo de análisis hecho, es medianamente recomendable crear un nuevo restaurante en " + ciudad.get_nombre() + ".\nEsto se debe a que los restaurantes tienen un flujo medio de clientes y\nestán cumpliendo con las expectativas la mayoría de los usuarios.\nTeniendo esto en cuenta, ¿Desea crear una nueva sede?", criterios=None, tituloValores="", tipo=1, comandoContinuar=f4_i1_crear_igualmente, comandoCancelar=funcionalidad_0)
                    label_procesos_bottom.grid(sticky="nsew")

                else:
                    label_procesos_mid.config(text="Seleccione sí o no dependiendo de si quiere continuar.")
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Según el algoritmo de análisis hecho, es altamente recomendable crear un nuevo restaurante en " + ciudad.get_nombre() + ".\nEsto se debe a que los restaurantes tienen un flujo alto de clientes y\nestán cumpliendo con las expectativas la gran mayoría de los usuarios.\nTeniendo esto en cuenta, ¿Desea crear una nueva sede?", criterios=None, tituloValores="", tipo=1, comandoContinuar=f4_i1_crear_igualmente, comandoCancelar=funcionalidad_0)
                    label_procesos_bottom.grid(sticky="nsew")


    label_procesos_mid.config(text="Seleccione la zona donde desea agregar la sede.")

    nombre_zonas = []
    for zona in ciudad.get_zonas_ciudad():
        nombre_zonas.append(zona.get_nombre())

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Zona"], tituloValores = "Valor ingresado", valores = [nombre_zonas], tipo = 2, comandoContinuar = f4_i1_continuar_parametros, habilitado = [True])
    label_procesos_bottom.grid(sticky="nsew")

#Funcionalidad 4 Interacción 2

ciclo_esquinas = ['B']
ciclo_bordes = ['B', 'W', 'E']
ciclo_central = [' ', 'T', 'V']

# Variable para verificar si los cambios han sido guardados
cambios_guardados = False

def cambiar_estado(boton, fila, columna, estado_actual, M, N):
    global cambios_guardados
    cambios_guardados = False  # Cambios no guardados
    # Identificar la zona del botón: esquina, borde, o central
    if (fila == 0 or fila == M-1) and (columna == 0 or columna == N-1):
        # Esquinas
        ciclo = ciclo_esquinas
    elif fila == 0 or fila == M-1 or columna == 0 or columna == N-1:
        # Bordes (excepto esquinas)
        ciclo = ciclo_bordes
    else:
        # Centro
        ciclo = ciclo_central
    
    # Cambiar al siguiente estado en el ciclo correspondiente
    nuevo_estado = (estado_actual + 1) % len(ciclo)
    boton.config(text=ciclo[nuevo_estado])

    fuente_normal = ("Arial", 10)
    fuente_bold = ("Arial", 10, "bold")

    # Cambiar la fuente a negrita si es 'Ventana' o 'Puerta' en los bordes
    if ciclo == ciclo_bordes and (ciclo[nuevo_estado] == 'W' or ciclo[nuevo_estado] == 'E'):
        boton.config(font=fuente_bold)  # Texto en negrita
    elif ciclo == ciclo_central and (ciclo[nuevo_estado] == "T" or ciclo[nuevo_estado] == "V"):
        boton.config(font=fuente_bold)
    else:
        boton.config(font=fuente_normal)  # Texto normal para otros estados
    
    # Actualizar el estado actual
    matriz_estados[fila][columna] = nuevo_estado

def generar_lista_estados(alto, ancho):
    # Crear la lista de estados basada en el contenido actual de los botones
    lista_estados = []
    for fila in range(alto):
        for columna in range(ancho):
            texto_boton = matriz_botones[fila][columna].cget('text')
            lista_estados.append(((columna+1, fila+1), texto_boton))
    return lista_estados

def validar_estados(lista_estados):
    # Comprobar que hay al menos una Ventana, una Puerta y una Mesa
    tiene_ventana = any('W' in fila for fila in lista_estados)
    tiene_puerta = any('E' in fila for fila in lista_estados)
    tiene_mesa = any('T' in fila for fila in lista_estados) or any('V' in fila for fila in lista_estados)

    return tiene_ventana and tiene_puerta and tiene_mesa

disposicion_nuevo_restaurante = []

def establecer_disposicion(restaurante):
    global label_procesos_bottom
    # Verificar si hay más de 3 restaurantes creados
    print(restaurante.get_ciudad().get_restaurantes())
    restaurante.get_ciudad().get_restaurantes().pop(0)
    print(restaurante.get_ciudad().get_restaurantes())


    if restaurante.get_ciudad().get_restaurantes() != []:
        promedios = obtener_promedios()
        label_procesos_mid.config(text=f"""Recomendación: Ancho = {promedios[0]}\tLargo = {promedios[1]}
        Cantidad Mesas: Estándar = {promedios[2]}\tVIP = {promedios[3]} (En caso de tener Zona VIP)
        Ventanas = {promedios[4]}""")
    else:
        label_procesos_mid.config(text="""Recomendación: Ancho = 10\tLargo = 10
        Cantidad Mesas: Estándar = 2\tVIP = 1 (En caso de tener Zona VIP)
        Ventanas = 2""")

    def f4_i2_disposicion_interactiva():
        global label_procesos_bottom, matriz_estados, matriz_botones
        label_procesos_mid.config(text="Al darle click a las casillas estas cambiarán.\nB = Pared; W = Ventana; E = Puerta\nT = Mesa Estándar; V = Mesa VIP")

        try:
            alto_elegido = int(label_procesos_bottom.valores[0])
        except:
            raise ExcepcionDatosErroneos("Alto")
        try:
            ancho_elegido = int(label_procesos_bottom.valores[1])
        except:
            raise ExcepcionDatosErroneos("Ancho")
        matriz_estados = [[0 for _ in range(ancho_elegido)] for _ in range(alto_elegido)]  # Inicializar todos los botones con el estado 0
        matriz_botones = [[None for _ in range(ancho_elegido)] for _ in range(alto_elegido)] 
        
        ultimo_row = 0

        def f4_i2_guardar_cambios():
            global cambios_guardados, disposicion_nuevo_restaurante, label_procesos_bottom, frame_procesos_bottom
            disposicion_nuevo_restaurante = generar_lista_estados(alto_elegido, ancho_elegido)
            
            def f4_i2_instanciar_elementos():
                global disposicion_nuevo_restaurante
                for casilla in disposicion_nuevo_restaurante:
                    if casilla[1] == "W":
                        restaurante.get_casillas().append(Casilla(1, casilla[0][0], casilla[0][1]))
                    elif casilla[1] == "E":
                        restaurante.get_casillas().append(Casilla(2, casilla[0][0], casilla[0][1]))
                    elif casilla[1] == "T":    
                        mesa = Mesa(0, casilla[0][0], casilla[0][1], False)
                        restaurante.get_casillas().append(mesa)
                        restaurante.get_mesas().append(mesa)
                        mesa.set_fechas_disponibles(generar_fechas())
                    elif casilla[1] == "V":
                        if restaurante.is_zona_vip() == False:
                            mesa = Mesa(0, casilla[0][0], casilla[0][1], False)
                            restaurante.get_casillas().append(mesa)
                            restaurante.get_mesas().append(mesa)
                            mesa.set_fechas_disponibles(generar_fechas())
                        else:
                            mesa = Mesa(0, casilla[0][0], casilla[0][1], True)
                            restaurante.get_casillas().append(mesa)
                            restaurante.get_mesas().append(mesa)
                            mesa.set_fechas_disponibles(generar_fechas())
                print("Casillas Instanciadas:", restaurante.get_casillas())
                establecer_menu_y_encargos(restaurante)

            if validar_estados([estado for _, estado in disposicion_nuevo_restaurante]):
                # Aquí puedes hacer lo que desees con la lista generada
                print(disposicion_nuevo_restaurante)
                for widget in frame_procesos_bottom.winfo_children():
                    widget.destroy()
                
                frame_procesos_bottom = Frame(frame_procesos, bd = 2, height = 300, relief="solid", bg = "#545454")
                frame_procesos_bottom.grid(row = 2, padx = 10, pady = 10, sticky="nsew")
                frame_procesos_bottom.grid_propagate(False)
                frame_procesos_bottom.grid_rowconfigure(0, weight=1)
                frame_procesos_bottom.grid_columnconfigure(0, weight=1)

                label_procesos_mid.config(text="Seleccione sí o no.")
                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Disposición guardada con éxito.", criterios=None, tituloValores="¿Desea continuar?", tipo=1, comandoContinuar=f4_i2_instanciar_elementos, comandoCancelar=funcionalidad_0)
                label_procesos_bottom.grid(sticky="nsew")
            else:
                # Mostrar un mensaje de advertencia
                messagebox.showwarning("Advertencia", "Debe haber al menos una Ventana (W), una Puerta (E) y una Mesa (T o V).")

        if alto_elegido < 8 or ancho_elegido < 8 or alto_elegido > 16 or ancho_elegido > 20:
            raise ExcepcionDatosEntry("7 < alto < 17 & 7 < ancho < 21")
        else:
            label_procesos_bottom.destroy()
            label_procesos_bottom = Frame(frame_procesos_bottom)
            for i in range(alto_elegido):
                frame_procesos_bottom.grid_rowconfigure(i, weight=1)
                for j in range(ancho_elegido):
                    print("Hola")
                    frame_procesos_bottom.grid_columnconfigure(j, weight=1)
                    # Crear botones y asignar la función de cambio de estado
                    boton = Button(frame_procesos_bottom, text=ciclo_central[0], bg="#545454", font=("Arial", 10), fg="#fff")
                    boton.grid(row=i, column=j, sticky="nsew")
                    ultimo_row = i
                    matriz_botones[i][j] = boton  # Almacenar referencia al botón
                    # Determinar el ciclo inicial de acuerdo a la posición del botón
                    if (i == 0 or i == alto_elegido-1) and (j == 0 or j == ancho_elegido-1):
                        # Esquinas
                        boton.config(text=ciclo_esquinas[0])
                    elif i == 0 or i == alto_elegido-1 or j == 0 or j == ancho_elegido-1:
                        # Bordes
                        boton.config(text=ciclo_bordes[0])
                    else:
                        # Centro
                        boton.config(text=ciclo_central[0])

                    # Vincular la función al evento de clic
                    boton.config(command=lambda b=boton, fila=i, col=j: cambiar_estado(b, fila, col, matriz_estados[fila][col], alto_elegido, ancho_elegido))

            # Crear botón "Aceptar"
            boton_aceptar = Button(frame_procesos_bottom, text="Aceptar", command=f4_i2_guardar_cambios, bg="#545454", font=("Arial", 10), fg="#fff")
            boton_aceptar.grid(row=ultimo_row+1, column=0, columnspan=ancho_elegido, sticky="we")
            
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Alto", "Ancho"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True, True], comandoContinuar=f4_i2_disposicion_interactiva)
    label_procesos_bottom.grid(sticky="nsew")

#Funcionalidad 4 Interacción 3
def establecer_menu_y_encargos(restaurante):
    global label_procesos_bottom
    # Establecer Menú
    menu_transitorio = []
    for i in range(0, 10):
        try:
            menu_transitorio.append(Plato.get_platos().sort()[i])
        except:
            continue
    
    menu_transitorio_nombres = []
    for plato in menu_transitorio:
        menu_transitorio_nombres.append(plato.get_nombre())
    
    if menu_transitorio_nombres == []:
        menu_transitorio_nombres = "Menú vacío. Elegir No"

    def f4_i3_adoptar_o_crear():
        global label_procesos_bottom
        conservar = label_procesos_bottom.valores[0]
        if conservar == 1:  # Si se quiere adoptar el menú generado
            restaurante.set_menu(menu_transitorio)
            cargamento()
        elif conservar == 2:  # Si no se quiere adoptar el menú generado
            def f4_i3_crear_platos():
                global label_procesos_bottom, contador_platos, cantidad_platos
                if contador_platos == 0:
                    try:
                        cantidad_platos = int(label_procesos_bottom.valores[0])
                    except:
                        raise ExcepcionDatosErroneos("Cantidad de Platos")
                # else:
                #     label_procesos_bottom.destroy()
                #     label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Creando...", criterios = ["Todavía tienes platos por crear"], tituloValores = "", tipo = 3, comandoContinuar=f4_i3_crear)
                #     label_procesos_bottom.grid(sticky="nsew")
                def f4_i3_crear():
                    global label_procesos_bottom
                    label_procesos_mid.config(text="Seleccione aceptar.")
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Crear plato", criterios = ["Ir a la creación de plato"], tituloValores = "Valor ingresado", tipo = 3, comandoContinuar=crear_plato)
                    label_procesos_bottom.grid(sticky="nsew")
                if contador_platos < cantidad_platos:
                    label_procesos_mid.config(text="Seleccione aceptar.")
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Creando...", criterios = ["Todavía tienes platos por crear"], tituloValores = "", tipo = 3, comandoContinuar=f4_i3_crear)
                    label_procesos_bottom.grid(sticky="nsew")
                    contador_platos += 1
                else:
                    cargamento(restaurante)
            
            def crear_plato():
                global label_procesos_bottom

                def f4_i3_continuar_creacion_plato():
                    global label_procesos_bottom

                    existe = False
                    indice_existe = 0
                    plato_retorno = Plato()
                    cantidad_ingredientes = []
                    nombre = label_procesos_bottom.valores[0]

                    if not Plato.get_platos():
                        for plato in Plato.get_platos():
                            if plato.get_nombre() == nombre:
                                existe = True
                                indice_existe = Plato.get_platos().index(plato)
                                break

                    if not existe:
                        def f4_i3_establecer_tipo():
                            global label_procesos_bottom
                            tipo_plato = label_procesos_bottom.valores[0]

                            plato_retorno.set_tipo(tipo_plato)

                            def f4_i3_establecer_ingredientes_plato():
                                global label_procesos_bottom, contador_ingredientes
                                try:
                                    precio_plato = int(label_procesos_bottom.valores[0])
                                except:
                                    raise ExcepcionDatosErroneos("Precio Plato")
                                try:
                                    num_ingredientes = int(label_procesos_bottom.valores[1])
                                except:
                                    raise ExcepcionDatosErroneos("Número de Ingredientes")

                                if num_ingredientes < 1:
                                    num_ingredientes = 1

                                ingredientes_plato = []
                                cantidad_ingredientes = []
                                contador_ingredientes = 1
                                def f4_i3_recursiva():
                                    global label_procesos_bottom
                                # for i in range(num_ingredientes):
                                    def f4_i3_establecer_ingrediente():
                                        global label_procesos_bottom, contador_ingredientes
                                        nombre_ingrediente = label_procesos_bottom.valores[0]
                                        try:
                                            precio_ingrediente = int(label_procesos_bottom.valores[1])
                                        except:
                                            raise ExcepcionDatosErroneos(["Precio Ingrediente"])
                                        try:
                                            cantidad_ingrediente = int(label_procesos_bottom.valores[2])
                                        except:
                                            raise ExcepcionDatosErroneos(["Cantidad Ingrediente"])

                                        if precio_ingrediente < 1:
                                            precio_ingrediente = 1
                                        
                                        if cantidad_ingrediente < 1:
                                            cantidad_ingrediente = 1

                                        ingrediente = Ingrediente(nombre_ingrediente, precio_ingrediente)
                                        ingredientes_plato.append(ingrediente)
                                        
                                        cantidad_ingredientes.append([ingrediente.get_nombre(), str(cantidad_ingrediente)])

                                        def f4_i3_definir_plato_retorno(nombre, precio, ingredientes, cantidad):
                                            print("Se accede a definir plato retorno")
                                            restaurante.get_menu().append(Plato(nombre, precio, ingredientes, cantidad))
                                            f4_i3_crear_platos()

                                        if contador_ingredientes == num_ingredientes:
                                            f4_i3_definir_plato_retorno(nombre, precio_plato, ingredientes_plato, cantidad_ingredientes)
                                        
                                        if contador_ingredientes < num_ingredientes:
                                            print("Antes de sumar", contador_ingredientes)
                                            contador_ingredientes += 1
                                            print("Despues de sumar", contador_ingredientes)
                                            f4_i3_recursiva()
                                            # f4_i3_definir_plato_retorno(nombre_ingrediente, precio_ingrediente, ingredientes_plato, cantidad_ingredientes)
                                    
                                    label_procesos_mid.config(text="Ingrese los datos del ingrediente.")
                                    label_procesos_bottom.destroy()
                                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Nombre Ingrediente", "Precio Ingrediente", "Cantidad Ingrediente"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True, True, True], comandoContinuar=f4_i3_establecer_ingrediente)
                                    label_procesos_bottom.grid(sticky="nsew")
                                
                                f4_i3_recursiva()

                            label_procesos_mid.config(text="Ingrese los datos del plato.")
                            label_procesos_bottom.destroy()
                            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Precio Plato", "Número de Ingredientes"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True, True, True], comandoContinuar=f4_i3_establecer_ingredientes_plato)
                            label_procesos_bottom.grid(sticky="nsew")
                        
                        label_procesos_mid.config(text="Seleccione el tipo del plato.")
                        label_procesos_bottom.destroy()
                        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Tipo Plato"], tituloValores = "Valor ingresado", valores = [["Entradas", "Platos Fuertes", "Bebidas", "Postres", "Menú Infantil", "Todos"]], tipo = 2, comandoContinuar = f4_i3_establecer_tipo, habilitado = [True])
                        label_procesos_bottom.grid(sticky="nsew")

                    else:
                        plato_retorno = Plato.get_platos()[indice_existe]

                    for cantidad in cantidad_ingredientes:
                        plato_retorno.get_cantidad_ingredientes().append(cantidad)
                
                label_procesos_mid.config(text="Ingrese el nombre del plato a agregar.")
                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Nombre Plato"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True], comandoContinuar=f4_i3_continuar_creacion_plato)
                label_procesos_bottom.grid(sticky="nsew")

            label_procesos_mid.config(text="Ingrese la cantidad de platos a crear.")
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Cantidad de Platos"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True], comandoContinuar=f4_i3_crear_platos)
            label_procesos_bottom.grid(sticky="nsew")
    
    label_procesos_mid.config(text="Menú generado por orden de calificación de los platos.\nSeleccione sí o no.")
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios=f"Menú generado:\n{menu_transitorio_nombres}\n¿Desea conservar", criterios=None, tituloValores="el menú?", tipo=1, comandoContinuar=f4_i3_adoptar_o_crear, comandoCancelar=f4_i3_adoptar_o_crear)
    label_procesos_bottom.grid(sticky="nsew")

def cargamento(restaurante):
    print(len(restaurante.get_menu()), restaurante.get_menu())
    for plato in restaurante.get_menu():
        print(plato)
    global label_procesos_bottom
    cargamento = Cargamento()

    def f4_i3_establecer_parametros():
        global label_procesos_bottom
        try:
            cantidad_ingredientes_encargo = label_procesos_bottom.valores[0]
        except:
            raise ExcepcionDatosErroneos("Cantidad de ingredientes a encargar")
        try:
            cantidad_utilidades = label_procesos_bottom.valores[1]
        except:
            raise ExcepcionDatosErroneos("Cantidad de utilidades a encargar")
        try:
            frecuencia_dias = label_procesos_bottom.valores[2]
        except:
            raise ExcepcionDatosErroneos("¿Cada cuántos días quiere que venga el cargamento?")

        for plato in restaurante.get_menu():
            for cantidad_ingredientes in plato.get_cantidad_ingredientes():
                cargamento.aumentar_cantidad_ingrediente([cantidad_ingredientes[0], str(cantidad_ingredientes_encargo)])

        for utilidad in Cargamento.UTILIDADES:
            cargamento.get_utilidades().append(cantidad_utilidades)

        fecha_actual = datetime.now()

        cargamento.set_frecuencia(frecuencia_dias)
        cargamento.set_proxima_entrega([fecha_actual.year, fecha_actual.month, fecha_actual.day])

        restaurante.set_cargamento(cargamento)
        cargamento.set_restaurante(restaurante)

        funcionalidad_0()
    
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Cantidad de ingredientes a encargar", "Cantidad de utilidades a encargar", "¿Cada cuántos días quiere que venga el cargamento?"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True, True, True], comandoContinuar=f4_i3_establecer_parametros)
    label_procesos_bottom.grid(sticky="nsew")

###Parte de FUNCIONALIDAD 5
class EstadoGlobal:
    cliente_final = None
    factura_final = None
    evento_final = None
    hora_reserva = None


def crearEvento():
    global label_procesos_bottom, label_procesos_mid
    Ciudad.get_ciudades().clear()
    Zona.get_zonas().clear()

    # Crear ciudades y zonas
    comala = Ciudad("Comala")
    medellin = Ciudad("Medellin")
    zona_centro = Zona(14, "Centro", comala)
    zona_centro1 = Zona(14, "CentroMede", medellin)
    comala.agregar_zona(zona_centro)
    medellin.agregar_zona(zona_centro1)

    # Crear restaurantes
    restaurantes_comala = [
        Restaurante(10, "Casa Stiven", [], comala, zona_centro, False),
        Restaurante(12, "Casa Stiven2", [], comala, zona_centro, False),
        Restaurante(13, "Casa Stiven3", [], comala, zona_centro, False),
        Restaurante(14, "Casa Stiven4", [], comala, zona_centro, False)
    ]
    for restaurante in restaurantes_comala:
        zona_centro.get_restaurantes().append(restaurante)

    restaurantes_medellin = [
        Restaurante(10, "Casa Stiven1", [], medellin, zona_centro1, False)
    ]
    for restaurante in restaurantes_medellin:
        zona_centro1.get_restaurantes().append(restaurante)

    # Llamar la primera interacción
    interaccion1_ciudad()

def interaccion1_ciudad():
    global label_procesos_bottom

    # Mostrar opciones de ciudades
    nombre_ciudades = [ciudad.get_nombre() for ciudad in Ciudad.get_ciudades()]
    label_procesos_mid.config(text="Seleccione la ciudad donde desea el evento")

    # Destruir el campo anterior y generar el nuevo
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Ciudad",
        criterios=["Ciudad"],
        tituloValores="Valor ingresado",
        valores=[nombre_ciudades],
        tipo=2,
        comandoContinuar=interaccion1_zona,
        habilitado=[True]
    )
    label_procesos_bottom.grid(sticky="nsew")

def interaccion1_zona():
    global label_procesos_bottom

    # Obtener la ciudad seleccionada
    nombre_ciudad_elegida = label_procesos_bottom.valores[0]
    ciudad_actual = next(ciudad for ciudad in Ciudad.get_ciudades() if ciudad.get_nombre() == nombre_ciudad_elegida)

    # Mostrar opciones de zonas
    nombre_zonas = [zona.get_nombre() for zona in ciudad_actual.get_zonas_ciudad() if zona.get_restaurantes()]
    label_procesos_mid.config(text="Seleccione la zona donde desea su evento")

    # Destruir el campo anterior y generar el nuevo
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Zona",
        criterios=["Zona"],
        tituloValores="Valor ingresado",
        valores=[nombre_zonas],
        tipo=2,
        comandoContinuar=llamar_interacciones,
        habilitado=[True]
    )
    label_procesos_bottom.grid(sticky="nsew")

def llamar_interacciones():
    global label_procesos_bottom

    # Obtener la zona seleccionada
    zona_elegida = label_procesos_bottom.valores[0]
    zona_actual = next(zona for zona in Zona.get_zonas() if zona.get_nombre() == zona_elegida)

    # Llamar a la siguiente interacción
    interaccion1_recomendacionRestaurante(zona_actual)

    # Aquí necesitas asegurarte de que cliente_final se ha actualizado
    # Puedes usar un bucle o esperar algún evento para verificar la actualización
    while EstadoGlobal.cliente_final is None:
        frame_procesos_bottom.update()  # Actualizar la interfaz gráfica

    cliente_final = EstadoGlobal.cliente_final
    interaccion2_recomendarEvento()

    while EstadoGlobal.evento_final is None:
        frame_procesos_bottom.update()
    while EstadoGlobal.factura_final is None:
        frame_procesos_bottom.update()

    print(EstadoGlobal.factura_final.get_evento().get_platos()[0].get_nombre())
    print(EstadoGlobal.factura_final.get_evento().get_coste())
    print(EstadoGlobal.factura_final.get_evento().get_descripcion())
    hora_reserva_funcion()
    while EstadoGlobal.hora_reserva is None:
        frame_procesos_bottom.update()
    print(EstadoGlobal.hora_reserva)
    mensaje = diseno_de_factura(EstadoGlobal.factura_final, EstadoGlobal.cliente_final, EstadoGlobal.hora_reserva)
    factura_final(mensaje)


##########Interacción 1 Comienza acá

def interaccion1_recomendacionRestaurante(zona_actual):
    global label_procesos_mid, label_procesos_bottom

    def interaccion1_mayorCapacidad():
        restaurante_mayor_capacidad = max(zona_actual.get_restaurantes(), key=lambda r: r.get_capacidad())
        label_procesos_mid.config(text=f"El restaurante recomendado es {restaurante_mayor_capacidad.get_nombre()}")
        
        # Pedir datos del evento, después actualizar cliente_final
        EstadoGlobal.cliente_final = pedir_datos_evento(restaurante_mayor_capacidad)
        


    def interaccion1_EscogerRestaurante():
        global label_procesos_bottom

        def pedir_datos():
            global label_procesos_bottom
            restaurante_seleccionado = label_procesos_bottom.valores[0]
            restaurante_final = next((r for r in zona_actual.get_restaurantes() if r.get_nombre() == restaurante_seleccionado), None)
            if restaurante_final:
                label_procesos_mid.config(text=f"Restaurante seleccionado: {restaurante_final.get_nombre()}")
                EstadoGlobal.cliente_final = pedir_datos_evento(restaurante_final)
            else:
                label_procesos_mid.config(text="Error al seleccionar el restaurante. Intente de nuevo.")


        restaurantes_zona = [restaurante.get_nombre() for restaurante in zona_actual.get_restaurantes()]
        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
            frame_procesos_bottom,
            tituloCriterios=["Restaurantes"],
            criterios=["Restaurantes"],
            tituloValores="Seleccione",
            valores=[restaurantes_zona],
            tipo=2,
            comandoContinuar=pedir_datos,
            habilitado=[True]
        )
        label_procesos_bottom.grid(sticky="nsew")

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Desea una recomendación",
        criterios=None,
        tituloValores="Continuar",
        tipo=1,
        comandoContinuar=interaccion1_mayorCapacidad,
        comandoCancelar=interaccion1_EscogerRestaurante
    )
    label_procesos_bottom.grid(sticky="nsew")

def pedir_datos_evento(restaurante):
    global label_procesos_bottom

    def reserva_de_los_clientes():
        global label_procesos_bottom
        nombre_cliente = label_procesos_bottom.getValue("Nombre")
        try:
            cedula_cliente = int(label_procesos_bottom.getValue("Cédula"))
        except ValueError:
            messagebox.showerror("Error: Tipo de dato erróneo", "Cédula debe ser un número")
            return
        
        EstadoGlobal.cliente_final = Cliente(nombre_cliente, cedula_cliente)
        EstadoGlobal.cliente_final.set_restaurante(restaurante)
        label_procesos_bottom.destroy()




    # Inicializar la primera pantalla para datos del cliente
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Datos del Cliente",
        criterios=["Nombre", "Cédula"],
        tituloValores="Ingrese los datos",
        valores=[],
        tipo=0,
        comandoContinuar=reserva_de_los_clientes,
        habilitado=[True, True]
    )
    label_procesos_bottom.grid(sticky="nsew")
    # label_procesos_bottom.destroy()


    # Retorna None inicialmente, el valor real se actualizará en reserva_de_los_clientes
    return None
###############################Interacción 1 Lista Termina acá
###############################Interacción 2


# ##INTERACCIÓN 1 FINALIZA ACÁ


# ###################INTERACCIÓN 2
def interaccion2_recomendarEvento():
    ##CREAR LOS OBJETOS
    ##PRIMERO CUMPLEAÑOS
    global label_procesos_bottom, label_procesos_mid

    label_procesos_mid.config(text="Tenemos los siguientes eventos, ¿cual desea?")

    ###Aca irian las sub interacciones
    def opcion_cumpleanos():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="El evento tiene un costo de 210.000$")

        def opcion_cumpleanos_si():
            global label_procesos_bottom, label_procesos_mid

            def invitados_cumple_nombre():
                global label_procesos_bottom
                try:
                    nombre_festejado = label_procesos_bottom.getValue("Nombre del Festejado")
                    cantidad_invitados = label_procesos_bottom.getValue("Numero de acompañantes")

                    if not nombre_festejado:
                        raise ExcepcionDatosErroneos("Nombre del Festejado no puede estar vacío")

                    if not (1 <= int(cantidad_invitados) <= 40):
                        raise ExcepcionFueraRango(cantidad_invitados, "1-40 (El restaurante solo tiene capacidad para esto 😞)")

                    coste_evento = 210000
                    descripcion_evento = "¡Feliz Cumpleaños! Te deseamos lo mejor en esta etapa, " + nombre_festejado
                    nombre_evento = "Feliz Cumpleaños"
                    evento_elegido = Evento(nombre_evento, coste_evento)
                    evento_elegido.set_descripcion(descripcion_evento)
                    EstadoGlobal.evento_final = evento_elegido
                    EstadoGlobal.factura_final = Factura()
                    EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)
                    recomendar_torta(cantidad_invitados)

                except ExcepcionFueraRango as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error de Invitados", str(e))
                
                except ErrorAplicacion as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error de Aplicación", str(e))

                except ValueError:
                    messagebox.showerror("Error de Formato", "El número de acompañantes debe ser un número entero válido.")
        
                            
            

            mensaje_cumpleanos = ("Nosotros encantados de atenderte en tu cumpleaños.\n"
                                "Somos felices de tenerlos en el restaurante 😈.\n"
                                "Por favor, danos los siguientes datos del cumpleañero:")
    
    # Configura el label con texto ajustado para imprimir
            label_procesos_mid.config(text=mensaje_cumpleanos, wraplength=400, justify="left", font=("Arial", 8), fg="#fff")
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(
                frame_procesos_bottom,
                tituloCriterios="Rellena por favor algunos daticos",
                criterios=["Nombre del Festejado", "Numero de acompañantes"],
                tituloValores="Digite uno por uno",
                valores=[],
                tipo=0,
                comandoContinuar=invitados_cumple_nombre,
                habilitado=[True, True]
                )
            label_procesos_bottom.grid(sticky="nsew")

            print("Si se mete")
        
        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Desea",
        criterios=None,
        tituloValores="continuar con el evento?",
        tipo=1,
        comandoContinuar=opcion_cumpleanos_si,
        comandoCancelar=interaccion2_recomendarEvento
        )
        label_procesos_bottom.grid(sticky="nsew")



    def opcion_meetings():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="El evento de meetings tiene un coste de 410.000%")
        
        def opcion_meetings_si():
            global label_procesos_bottom, label_procesos_mid

            def caracteristicas_de_la_empresa():
                global label_procesos_bottom
                try:
                    NIT_empresa = label_procesos_bottom.getValue("NIT")
                    cantidad_proletariado = label_procesos_bottom.getValue("Cantidad de Asistentes")

                    if not NIT_empresa.isdigit() or len(NIT_empresa) != 7:
                        raise ExcepcionDatosErroneos("El NIT debe ser un número, aparte de ello contener 7 números")

                    if not (1 <= int(cantidad_proletariado) <= 40):
                        raise ExcepcionFueraRango(cantidad_proletariado, "1-40 (El restaurante solo tiene capacidad para esto 😞)")

                    cata_vinos_champagne(cantidad_proletariado)

                except ExcepcionFueraRango as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error de Invitados", str(e))
                
                except ErrorAplicacion as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error de Aplicación", str(e))

                except ValueError:
                    messagebox.showerror("Error de Formato", "El número de acompañantes debe ser un número entero válido.")               
                
            mensaje_meeting = ("Ningún mejor lugar para tus esclavos laborales que este\n"
                                "Somos felices de tenerlos en el restaurante 😈.\n"
                                "Por favor, danos los siguientes datos de la empresa:")
    
    # Configura el label con texto ajustado para imprimir
            label_procesos_mid.config(text=mensaje_meeting, wraplength=400, justify="left", font=("Arial", 10), fg="#fff")
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(
                frame_procesos_bottom,
                tituloCriterios="Rellena por favor algunos daticos",
                criterios=["NIT", "Cantidad de Asistentes"],
                tituloValores="Digite uno por uno",
                valores=[],
                tipo=0,
                comandoContinuar=caracteristicas_de_la_empresa,
                habilitado=[True, True]
                )
            label_procesos_bottom.grid(sticky="nsew")

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Desea",
        criterios=None,
        tituloValores="continuar con el evento Meetings?",
        tipo=1,
        comandoContinuar=opcion_meetings_si,
        comandoCancelar=interaccion2_recomendarEvento
        )
        label_procesos_bottom.grid(sticky="nsew")
        




    def opcion_gastronomias():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="El servicio tiene un costo de 345000, ¿deseas continuar?")
        def opcione_gastronomias_si():
            global label_procesos_bottom, label_procesos_mid
            listado_nombres_gastronomias = ["Japonesa", "Marroquí", "Francesa", "Italiana"]
            mensaje = ("En esta sección conoceras las gastronomias de todas las /n"
                    "partes del mundo, en especial las 4 más relevantes en /n"
                    "termino de gusto, calidad y ricura😏😏😏")
            label_procesos_mid.config(text=mensaje, wraplength=400, justify="left", font=("Arial", 10), fg="#fff")
            def gastronomias_escoger():
                gastronomia_requerida = label_procesos_bottom.valores[0]
                gastronomias_semi_final(gastronomia_requerida)

            
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(
                frame_procesos_bottom,
                tituloCriterios="Gastronomias Mundiales",
                criterios=["Referentes"],
                tituloValores="al Pais",
                valores=[listado_nombres_gastronomias],
                tipo=2,
                comandoContinuar=gastronomias_escoger,
                habilitado=[True])
            label_procesos_bottom.grid(sticky="nsew")




        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Desea",
        criterios=None,
        tituloValores="continuar con las opciones gastronomicas?",
        tipo=1,
        comandoContinuar=opcione_gastronomias_si,
        comandoCancelar=interaccion2_recomendarEvento
        )
        label_procesos_bottom.grid(sticky="nsew")


    ###Hasta acá irían
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Eventos disponibles: ",
        criterios=None,
        tituloValores="",
        tipo=4,
        comandoContinuar=opcion_cumpleanos,
        comandoCancelar=opcion_meetings,
        comandoOpcion3=opcion_gastronomias,
        comandoOpcion4=funcionalidad_0
    )
    label_procesos_bottom.pack(expand=True, fill="both",padx=10, pady=20)
    label_procesos_bottom.grid(sticky="nsew")
    # label_procesos_bottom.destroy()
##################################################3




##Metodos Interacción 2 sub interacción 1
def recomendar_torta(cantidad_invitados):
    global label_procesos_bottom, label_procesos_mid
    torta_pequena = Plato("Torta Pequeña", 120500, porciones=19)
    torta_grande = Plato("Torta Grande", 350000, porciones=40)
    Plato.platos_cumple.append(torta_grande)
    Plato.platos_cumple.append(torta_pequena)    

    platos_evento = Plato.get_platos_cumple()
    plato_recomendado = None
    diferencia_minima = float('inf')

    for plato in platos_evento:
        diferencia = plato.get_porciones() - int(cantidad_invitados)
        if diferencia >= 0 and diferencia < diferencia_minima:
            diferencia_minima = diferencia
            plato_recomendado = plato
    label_procesos_mid.config(text=f"Vemos que son {cantidad_invitados}, le recomendamos la torta {plato_recomendado.get_nombre()}")

    # def finalizar_tortas(plato_recomendado):
    #     global label_procesos_bottom
    EstadoGlobal.evento_final.set_platos(plato_recomendado)
    EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)
    def finalizar():
        global label_procesos_bottom
        label_procesos_bottom.destroy()

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
    frame_procesos_bottom,
    tituloCriterios="Acepta la",
    criterios=None,
    tituloValores="recomendación de las tortas?",
    tipo=1,
    comandoContinuar= finalizar,
    comandoCancelar=interaccion2_recomendarEvento
)
    label_procesos_bottom.grid(sticky="nsew")




#Metodos Interaccion 2 sub interaccion 1

def cata_vinos_champagne(cantidad_proletariado):
    global label_procesos_bottom, label_procesos_mid, EstadoGlobal
    vino1 = Plato("Vino Catenna Deluxe", 128000, porciones=6, cantidad_de_plato=10)
    vino2 = Plato("Vino Bourgon Le Pin", 188000, porciones=6, cantidad_de_plato=10)
    vino3 = Plato("Vino del D1", 78000, porciones=8, cantidad_de_plato=10)
    vinos = [vino1, vino2, vino3]
    champagna1 = Plato("Champagna Mariscal G", 105000, porciones=6, cantidad_de_plato=10)
    champagna2 = Plato("Champagna Pierre Mersault", 112000, porciones=6, cantidad_de_plato=10)
    champagna3 = Plato("Champagna Cariñosa", 60000, porciones=6, cantidad_de_plato=10)
    champagna = [champagna1, champagna2, champagna3]
    Plato.vinos_champanas_meeting.append(vinos)
    Plato.vinos_champanas_meeting.append(champagna)

    def acepta_recomendacion():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="Desea vino o champagna?")
        def opcion_vinos():
            global label_procesos_bottom, label_procesos_mid, EstadoGlobal

            if 0 < int(cantidad_proletariado) <= 8:  # Recomendación para pocos invitados
                print("Son pocas personas, suponiendo su alto rango, os recomendamos:")
                botellas_a_llevar = [caros for caros in Plato.vinos_champanas_meeting[0] if caros.get_precio() > 100000]
                for i, finales in enumerate(botellas_a_llevar):
                    print(f"{i + 1}. {finales.get_nombre()}")
                nombres_vinos = []
                for idx in botellas_a_llevar:
                    nombres_vinos.append(idx.get_nombre())
                label_procesos_bottom.destroy()
                mensaje = ("Ya que son poquitos invitados (y suponemos son gerentes)\n"
                            "Estos son los vinos que les tenemos para ofecer")
                label_procesos_mid.config(text= mensaje)

                def vinos_pedidos():
                    nonlocal cantidad_proletariado
                    global label_procesos_bottom
                    
                    nombre_vino_elegido = label_procesos_bottom.valores[0]

                    for plato in Plato.vinos_champanas_meeting[0]:
                        if plato.get_nombre() == nombre_vino_elegido:
                            plato_vino_champana = plato
                    print("dsfsgdhfh")
                    
                    ##Definir la cantidad a llevar
                    cuenta_botellas = int((int(cantidad_proletariado) + plato_vino_champana.get_porciones() - 1) / plato_vino_champana.get_porciones())
                    print(f"Un total de {cuenta_botellas} botellas")


                    plato_vino_champana.set_veces_pedido(cuenta_botellas)
                    coste_evento = 450000
                    descripcion_evento = "Una empresa que demustra su talento, seriedad y humanidad"
                    nombre_evento = "Meetings Empresarial"
                    evento_elegido = Evento(nombre_evento, coste_evento, [plato_vino_champana])
                    evento_elegido.set_descripcion(descripcion_evento)
                    EstadoGlobal.evento_final = evento_elegido
                    EstadoGlobal.factura_final = Factura()
                    EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)

                    def finalizar():
                        label_procesos_bottom.destroy()
                        pass
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(
                    frame_procesos_bottom,
                    tituloCriterios="Vinos",
                    criterios="Estos son los mas cachés",
                    tituloValores="Seleccione",
                
                    tipo=1,
                    comandoContinuar=finalizar,
                    habilitado=[True]
                    )
                    label_procesos_bottom.grid(sticky="nsew")
                    return plato_vino_champana


                       
                label_procesos_bottom = FieldFrame(
                frame_procesos_bottom,
                tituloCriterios=["Vinos"],
                criterios=["Estos son los mas cachés"],
                tituloValores="Seleccione",
                valores=[nombres_vinos],
                tipo=2,
                comandoContinuar=vinos_pedidos,
                habilitado=[True]
                )
                label_procesos_bottom.grid(sticky="nsew")




            else:
                print("Son bastantes invitados, para su economía os recomendamos:")
                botellas_a_llevar = [baratos for baratos in Plato.vinos_champanas_meeting[0] if baratos.get_precio() < 100000]
                for i, finales in enumerate(botellas_a_llevar):
                    print(f"{i + 1}. {finales.get_nombre()}")
                nombres_vinos = []
                for idx in botellas_a_llevar:
                    nombres_vinos.append(idx.get_nombre())
                label_procesos_bottom.destroy()                
                

                # plato_final = Plato(producto_ofrecido.get_nombre(), cuenta_botellas, producto_ofrecido.get_precio())
                mensaje = ("Ya que son bastantes invitados (y suponemos son a termino indefinido)\n"
                            "Estos son los vinos que les tenemos para ofecer")
                label_procesos_mid.config(text= mensaje)

                
                def vinos_pedidos():
                    nonlocal cantidad_proletariado
                    global label_procesos_bottom
                    
                    nombre_vino_elegido = label_procesos_bottom.valores[0]

                    for plato in Plato.vinos_champanas_meeting[0]:
                        if plato.get_nombre() == nombre_vino_elegido:
                            plato_vino_champana = plato
                    print("dsfsgdhfh")
                    
                    ##Definir la cantidad a llevar
                    cuenta_botellas = int((int(cantidad_proletariado) + plato_vino_champana.get_porciones() - 1) / plato_vino_champana.get_porciones())
                    print(f"Un total de {cuenta_botellas} botellas")



                    plato_vino_champana.set_veces_pedido(cuenta_botellas)
                    coste_evento = 450000
                    descripcion_evento = "Una empresa que demustra su talento, seriedad y humanidad"
                    nombre_evento = "Meetings Empresarial"
                    evento_elegido = Evento(nombre_evento, coste_evento, [plato_vino_champana])
                    evento_elegido.set_descripcion(descripcion_evento)
                    EstadoGlobal.evento_final = evento_elegido
                    EstadoGlobal.factura_final = Factura()
                    EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)
                    def finalizar():
                        pass
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(
                    frame_procesos_bottom,
                    tituloCriterios="Vinos",
                    criterios="Estos son los mas cachés",
                    tituloValores="Seleccione",
                
                    tipo=1,
                    comandoContinuar=finalizar,
                    habilitado=[True]
                    )
                    label_procesos_bottom.grid(sticky="nsew")
                    return plato_vino_champana

                label_procesos_bottom = FieldFrame(
                frame_procesos_bottom,
                tituloCriterios=["Vinos"],
                criterios=["Estos son los mas baratos"],
                tituloValores="Seleccione",
                valores=[nombres_vinos],
                tipo=2,
                comandoContinuar=vinos_pedidos,
                habilitado=[True]
                )
                label_procesos_bottom.grid(sticky="nsew")

        def opcion_champanas():
            global label_procesos_bottom, label_procesos_mid
            if 0 < int(cantidad_proletariado) <= 8:  # Recomendación para pocos invitados
                print("Son pocas personas, suponiendo su alto rango, os recomendamos:")
                botellas_a_llevar = [caros for caros in Plato.vinos_champanas_meeting[1] if caros.get_precio() > 100000]
                for i, finales in enumerate(botellas_a_llevar):
                    print(f"{i + 1}. {finales.get_nombre()}")
                nombres_champanas = []
                for idx in botellas_a_llevar:
                    nombres_champanas.append(idx.get_nombre())
                label_procesos_bottom.destroy()
                mensaje = ("Ya que son poquitos invitados (y suponemos son gerentes)\n"
                            "Estos son las champanas que les tenemos para ofecer")
                label_procesos_mid.config(text= mensaje)

                def champanas_pedidos():
                    nonlocal cantidad_proletariado
                    global label_procesos_bottom
                    
                    nombre_vino_elegido = label_procesos_bottom.valores[0]

                    for plato in Plato.vinos_champanas_meeting[1]:
                        if plato.get_nombre() == nombre_vino_elegido:
                            plato_vino_champana = plato
                    print("dsfsgdhfh")
                    
                    ##Definir la cantidad a llevar
                    cuenta_botellas = int((int(cantidad_proletariado) + plato_vino_champana.get_porciones() - 1) / plato_vino_champana.get_porciones())
                    print(f"Un total de {cuenta_botellas} botellas")



                    plato_vino_champana.set_veces_pedido(cuenta_botellas)
                    coste_evento = 450000
                    descripcion_evento = "Una empresa que demustra su talento, seriedad y humanidad"
                    nombre_evento = "Meetings Empresarial"
                    evento_elegido = Evento(nombre_evento, coste_evento, [plato_vino_champana])
                    evento_elegido.set_descripcion(descripcion_evento)
                    EstadoGlobal.evento_final = evento_elegido
                    EstadoGlobal.factura_final = Factura()
                    EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)
                    # EstadoGlobal.evento_final.platos = plato_vino_champana
                    # EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)
                    def finalizar():
                        pass
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(
                    frame_procesos_bottom,
                    tituloCriterios="champmañas",
                    criterios="Estos son los mas cachés",
                    tituloValores="Seleccione",
                
                    tipo=1,
                    comandoContinuar=finalizar,
                    habilitado=[True]
                    )
                    label_procesos_bottom.grid(sticky="nsew")
                    return plato_vino_champana

                       
                label_procesos_bottom = FieldFrame(
                frame_procesos_bottom,
                tituloCriterios=["Champañas"],
                criterios=["Estos son los mas cachés"],
                tituloValores="Seleccione",
                valores=[nombres_champanas],
                tipo=2,
                comandoContinuar=champanas_pedidos,
                habilitado=[True]
                )
                label_procesos_bottom.grid(sticky="nsew")




            else:
                print("Son bastantes invitados, para su economía os recomendamos:")
                botellas_a_llevar = [baratos for baratos in Plato.vinos_champanas_meeting[1] if baratos.get_precio() < 100000]
                for i, finales in enumerate(botellas_a_llevar):
                    print(f"{i + 1}. {finales.get_nombre()}")
                nombres_champanas = []
                for idx in botellas_a_llevar:
                    nombres_champanas.append(idx.get_nombre())
                label_procesos_bottom.destroy()                
                

                # plato_final = Plato(producto_ofrecido.get_nombre(), cuenta_botellas, producto_ofrecido.get_precio())
                mensaje = ("Ya que son bastantes invitados (y suponemos son a termino indefinido)\n"
                            "Estos son las champañas que les tenemos para ofecer")
                label_procesos_mid.config(text= mensaje)

                def champanas_pedidos():
                    nonlocal cantidad_proletariado
                    global label_procesos_bottom
                    
                    nombre_vino_elegido = label_procesos_bottom.valores[0]

                    for plato in Plato.vinos_champanas_meeting[1]:
                        if plato.get_nombre() == nombre_vino_elegido:
                            plato_vino_champana = plato
                    print("dsfsgdhfh")
                    
                    ##Definir la cantidad a llevar
                    cuenta_botellas = int((int(cantidad_proletariado) + plato_vino_champana.get_porciones() - 1) / plato_vino_champana.get_porciones())
                    print(f"Un total de {cuenta_botellas} botellas")

                    plato_vino_champana.set_veces_pedido(cuenta_botellas)
                    coste_evento = 450000
                    descripcion_evento = "Una empresa que demustra su talento, seriedad y humanidad"
                    nombre_evento = "Meetings Empresarial"
                    evento_elegido = Evento(nombre_evento, coste_evento, [plato_vino_champana])
                    evento_elegido.set_descripcion(descripcion_evento)
                    EstadoGlobal.evento_final = evento_elegido
                    EstadoGlobal.factura_final = Factura()
                    EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)
                    def finalizar():
                        pass
                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(
                    frame_procesos_bottom,
                    tituloCriterios="Chamapñas",
                    criterios="Estos son los mas cachés",
                    tituloValores="Seleccione",
                
                    tipo=1,
                    comandoContinuar=finalizar,
                    habilitado=[True]
                    )
                    label_procesos_bottom.grid(sticky="nsew")
                    return plato_vino_champana

                       
                label_procesos_bottom = FieldFrame(
                frame_procesos_bottom,
                tituloCriterios=["Champañas"],
                criterios=["Estos son los mas baratos"],
                tituloValores="Seleccione",
                valores=[nombres_champanas],
                tipo=2,
                comandoContinuar=champanas_pedidos,
                habilitado=[True]
                )
                label_procesos_bottom.grid(sticky="nsew")

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
            frame_procesos_bottom,
            tituloCriterios="Conteste según sus deseos: ",
            criterios=None,
            tituloValores="",
            tipo=5,
            comandoContinuar=opcion_vinos,
            comandoCancelar=opcion_champanas,)
        label_procesos_bottom.pack(expand=True, fill="both",padx=10, pady=20)
        label_procesos_bottom.grid(sticky="nsew")
        

    def elige_por_su_cuenta():
        global label_procesos_bottom, label_procesos_mid, EstadoGlobal
        listado = Plato.vinos_champanas_meeting[0] + Plato.vinos_champanas_meeting[1]
        listado_bonito = []
        for idx in listado:
            listado_bonito.append(idx.get_nombre())

        def seleccionar_uno_mismo():
            global label_procesos_bottom, label_procesos_mid
            plato_vino_champana = label_procesos_bottom.valores[0]
            def cantidades():
                nonlocal plato_vino_champana, listado
                global label_procesos_bottom
                try:
                    cantidades = label_procesos_bottom.getValue("Miralas")
                    if not (1 <= int(cantidades) <= 7):
                        raise ExcepcionFueraRango(cantidades, "1-7 (Mas de 7 nos quiebra😞)")
                    if not cantidades.isdigit():
                        raise ValueError("Debes de ingresar un numero, no una letra")
                    bebida_final = None
                    for platos in listado:
                        if platos.get_nombre() == plato_vino_champana:
                            bebida_final = platos

                    bebida_final.set_veces_pedido(int(cantidades))
                    coste_evento = 450000
                    descripcion_evento = "Una empresa que demustra su talento, seriedad y humanidad"
                    nombre_evento = "Meetings Empresarial"
                    evento_elegido = Evento(nombre_evento, coste_evento, [bebida_final])
                    evento_elegido.set_descripcion(descripcion_evento)
                    EstadoGlobal.evento_final = evento_elegido
                    EstadoGlobal.factura_final = Factura()
                    EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)


                except ExcepcionFueraRango as e:
                        print(f"Error: {e}")
                        messagebox.showerror("Error de Invitados", str(e))
                    
                except ErrorAplicacion as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error de Aplicación", str(e))

                except ValueError:
                    messagebox.showerror("Error de Formato", "El número debe ser un número entero válido.")


            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(
            frame_procesos_bottom,
            tituloCriterios="Escoge las botellas que desees",
            criterios=["Miralas"],
            tituloValores="Seleccione",
            valores=[],
            tipo=0,
            comandoContinuar=cantidades,
            habilitado=[True]
            )
            label_procesos_bottom.grid(sticky="nsew")


        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios=["Todas las bebidas"],
        criterios=["Miralas"],
        tituloValores="Seleccione",
        valores=[listado_bonito],
        tipo=2,
        comandoContinuar=seleccionar_uno_mismo,
        habilitado=[True]
        )
        label_procesos_bottom.grid(sticky="nsew")

        

    label_procesos_mid.config(text = "¿Desea que le recomendemos según la cantidad de asistentes?")

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Conteste según sus deseos: ",
        criterios=None,
        tituloValores="",
        tipo=1,
        comandoContinuar=acepta_recomendacion,
        comandoCancelar=elige_por_su_cuenta,

    )
    label_procesos_bottom.pack(expand=True, fill="both",padx=10, pady=20)
    label_procesos_bottom.grid(sticky="nsew")


def gastronomias_semi_final(gastrononomia):
    global label_procesos_bottom, label_procesos_mid
    trabajador_italiano = Trabajador("Mario Guissepe", 876543, "Italiana", 2300000)
    trabajador_japones = Trabajador("Rika Miyuka", 575288, "Japonesa", 2300000)
    trabajador_marroqui = Trabajador("Hakin Hasan Ibrahim", 8428257, "Marroquí", 2300000)
    trabajador_frances = Trabajador("Emmanuel Macrom", 95175, "Francesa", 2300000)


    # Añadiendo cocineros
    Trabajador.get_cocineros().append(trabajador_italiano)
    Trabajador.get_cocineros().append(trabajador_japones)
    Trabajador.get_cocineros().append(trabajador_marroqui)
    Trabajador.get_cocineros().append(trabajador_frances)

    # Creación de platos varios
    bagget = Plato("Bagget", 2000, 100, "Meetings")
    queso = Plato("Queso mediterraneo", 50000, 100, "Meetings")
    mochi = Plato("Mochi", 4300, 100, "Japonesa")
    postre_napolitano = Plato("Postre Napolitano", 4300, 100, "Italiana")
    magrud = Plato("Maqrud", 4300, 100, "Marroquí")
    macarons = Plato("Macarons", 4300, 100, "Francesa")

    # Añadiendo platos varios
    Plato.get_platos_varios().append(bagget)
    Plato.get_platos_varios().append(queso)
    Plato.get_platos_varios().append(mochi)
    Plato.get_platos_varios().append(postre_napolitano)
    Plato.get_platos_varios().append(magrud)
    Plato.get_platos_varios().append(macarons)

    # Creación de platos italianos
    sopa_minestrone = Plato("Sopa Minnestrone", 54000, 5, "Italiana")
    ensalada_caprese = Plato("Ensalada Caprese", 35300, 8, "Italiana")
    carpaccio = Plato("Carpaccio", 44000, 1, "Italiana")
    vitello_tonnatoe = Plato("Vitello Tonnatoe", 74000, 4, "Italiana")

    # Añadiendo platos italianos
    Plato.get_gastronomias_italiana().append(sopa_minestrone)
    Plato.get_gastronomias_italiana().append(ensalada_caprese)
    Plato.get_gastronomias_italiana().append(carpaccio)
    Plato.get_gastronomias_italiana().append(vitello_tonnatoe)

    # Creación de platos japoneses
    sushi = Plato("Sushi Yarigato", 54000, 5, "Japonesa")
    tempura = Plato("Tempura Ora Ora", 35300, 8, "Japonesa")
    katsudon = Plato("Katsudon Primaveral", 44000, 3, "Japonesa")
    kaisedon = Plato("Kaisedon Hokkaido", 74000, 4, "Japonesa")

    # Añadiendo platos japoneses
    Plato.get_gastronomias_japonesa().append(sushi)
    Plato.get_gastronomias_japonesa().append(tempura)
    Plato.get_gastronomias_japonesa().append(katsudon)
    Plato.get_gastronomias_japonesa().append(kaisedon)

    # Creación de platos marroquíes
    tajin = Plato("Tajín Avepus", 54000, 5, "Marroquí")
    cuscus = Plato("Cuscús Adriático", 35300, 8, "Marroquí")
    harira = Plato("Harira Candente", 44000, 3, "Marroquí")
    briouat = Plato("Briouat Sur", 74000, 4, "Marroquí")

    # Añadiendo platos marroquíes
    Plato.get_gastronomias_marroqui().append(tajin)
    Plato.get_gastronomias_marroqui().append(cuscus)
    Plato.get_gastronomias_marroqui().append(harira)
    Plato.get_gastronomias_marroqui().append(briouat)

    # Creación de platos franceses
    ratatouille = Plato("Ratatouille Avignon", 54000, 5, "Francesa")
    escargots = Plato("Escargots D' Bourgogne", 35300, 8, "Francesa")
    fricase = Plato("Fricasé Le Mans", 44000, 1, "Francesa")
    gratin = Plato("Le gratin dauphinois", 74000, 1, "Francesa")

    # Añadiendo platos franceses
    Plato.get_gastronomias_francesa().append(ratatouille)
    Plato.get_gastronomias_francesa().append(escargots)
    Plato.get_gastronomias_francesa().append(fricase)
    Plato.get_gastronomias_francesa().append(gratin)

    # Añadiendo gastronomías al conjunto de platos
    Plato.get_platos_gastronomias().append(Plato.get_gastronomias_francesa())
    Plato.get_platos_gastronomias().append(Plato.get_gastronomias_italiana())
    Plato.get_platos_gastronomias().append(Plato.get_gastronomias_marroqui())
    Plato.get_platos_gastronomias().append(Plato.get_gastronomias_japonesa())

    if gastrononomia == "Japonesa":
        comida_japonesa()

    elif gastrononomia == "Italiana":
        comida_italiana()

    elif gastrononomia == "Marroquí":
        comida_marroqui() 

    elif gastrononomia == "Francesa":
        comida_francesa()

def comida_italiana():
    global label_procesos_bottom, label_procesos_mid
    chef_elegido = None
    for personal in Trabajador.cocineros:
        if personal.get_especialidad() == "Italiana":
            chef_elegido = personal
    nombre_platos=[]
    for platos in Plato.gastronomias_italiana:
        nombre_platos.append(platos.get_nombre())

    mensaje = (f"El/la chef {chef_elegido.get_nombre()} ha escogido los siguientes platos para ti\n"
            "Vi ringraziamo di avervi nel nostro ristorante La Sangue di Cristo ha Potere")
    label_procesos_mid.config(text=mensaje, wraplength=400, justify="center", font=("Arial", 12), fg="#fff")

    def cantidad_de_los_platos():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="Escoge la cantidad de platos que requieras en tu velada")
        plato_final = label_procesos_bottom.valores[0]

        def final_gastro():
            nonlocal plato_final
            global label_procesos_mid, label_procesos_bottom
            cantidad_final = label_procesos_bottom.valores[0]
            plato = None
            for platos in Plato.gastronomias_italiana:
                if platos.get_nombre() == plato_final:
                    plato = platos

            plato.set_veces_pedido(int(cantidad_final))
            coste_evento = 345000
            descripcion_evento = "..Toten o shinrai shite itadaki arigatogozaimasu.."
            nombre_evento = "Gastronomias Mundiales"
            evento_elegido = Evento(nombre_evento, coste_evento, [plato])
            evento_elegido.set_descripcion(descripcion_evento)
            EstadoGlobal.evento_final = evento_elegido
            EstadoGlobal.factura_final = Factura()
            EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)            

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Escoge la cantidad que desees",
        criterios=["Miralas"],
        tituloValores="Seleccione",
        valores=[],
        tipo=0,
        comandoContinuar=final_gastro,
        habilitado=[True]
        )
        label_procesos_bottom.grid(sticky="nsew")

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
    frame_procesos_bottom,
    tituloCriterios="Platos Italianos Disponibles",
    criterios=["Nombre"],
    tituloValores="El que usted desea mi rey",
    valores=[nombre_platos],
    tipo=2,
    comandoContinuar=cantidad_de_los_platos,
    habilitado=[True]
    )
    label_procesos_bottom.grid(sticky="nsew")


def comida_japonesa():
    global label_procesos_bottom, label_procesos_mid
    chef_elegido = None
    for personal in Trabajador.cocineros:
        if personal.get_especialidad() == "Japonesa":
            chef_elegido = personal
    nombre_platos=[]
    for platos in Plato.gastronomias_japonesa:
        nombre_platos.append(platos.get_nombre())

    mensaje = (f"El/la chef {chef_elegido.get_nombre()} ha escogido los siguientes platos para ti\n"
            "Anata-tachi o watashitachi no resutoran, kawaī chūgoku no on'nanoko ni mukaeru koto o kansha shimasu.")
    label_procesos_mid.config(text=mensaje, wraplength=400, justify="center", font=("Arial", 12), fg="#fff")

    def cantidad_de_los_platos():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="Escoge la cantidad de platos que requieras en tu velada")
        plato_final = label_procesos_bottom.valores[0]

        def final_gastro():
            nonlocal plato_final
            global label_procesos_mid, label_procesos_bottom
            cantidad_final = label_procesos_bottom.valores[0]
            plato = None
            for platos in Plato.gastronomias_japonesa:
                if platos.get_nombre() == plato_final:
                    plato = platos

            plato.set_veces_pedido(int(cantidad_final))
            coste_evento = 345000
            descripcion_evento = "..Toten o shinrai shite itadaki arigatogozaimasu.."
            nombre_evento = "Gastronomias Mundiales"
            evento_elegido = Evento(nombre_evento, coste_evento, [plato])
            evento_elegido.set_descripcion(descripcion_evento)
            EstadoGlobal.evento_final = evento_elegido
            EstadoGlobal.factura_final = Factura()
            EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Escoge la cantidad que desees",
        criterios=["Miralas"],
        tituloValores="Seleccione",
        valores=[],
        tipo=0,
        comandoContinuar=final_gastro,
        habilitado=[True]
        )
        label_procesos_bottom.grid(sticky="nsew")

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
    frame_procesos_bottom,
    tituloCriterios="Platos Japoneses Disponibles",
    criterios=["Nombre"],
    tituloValores="El que usted desea mi rey",
    valores=[nombre_platos],
    tipo=2,
    comandoContinuar=cantidad_de_los_platos,
    habilitado=[True]
    )
    label_procesos_bottom.grid(sticky="nsew")

def comida_marroqui():
    global label_procesos_bottom, label_procesos_mid
    chef_elegido = None
    for personal in Trabajador.cocineros:
        if personal.get_especialidad() == "Marroquí":
            chef_elegido = personal
    nombre_platos=[]
    for platos in Plato.gastronomias_marroqui:
        nombre_platos.append(platos.get_nombre())

    mensaje = (f"El/la chef {chef_elegido.get_nombre()} ha escogido los siguientes platos para ti\n"
            "شكراً لكم على وجودكم في مطعمنا 'دم المسيح له القدرة")
    label_procesos_mid.config(text=mensaje, wraplength=400, justify="center", font=("Arial", 12), fg="#fff")

    def cantidad_de_los_platos():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="Escoge la cantidad de platos que requieras en tu velada")
        plato_final = label_procesos_bottom.valores[0]

        def final_gastro():
            nonlocal plato_final
            global label_procesos_mid, label_procesos_bottom
            cantidad_final = label_procesos_bottom.valores[0]
            plato = None
            for platos in Plato.gastronomias_marroqui:
                if platos.get_nombre() == plato_final:
                    plato = platos

            plato.set_veces_pedido(int(cantidad_final))
            coste_evento = 345000
            descripcion_evento = ".......شكرا لك على الثقة في مطعمنا........"
            nombre_evento = "Gastronomias Mundiales"
            evento_elegido = Evento(nombre_evento, coste_evento, [plato])
            evento_elegido.set_descripcion(descripcion_evento)
            EstadoGlobal.evento_final = evento_elegido
            EstadoGlobal.factura_final = Factura()
            EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Escoge la cantidad que desees",
        criterios=["Miralas"],
        tituloValores="Seleccione",
        valores=[],
        tipo=0,
        comandoContinuar=final_gastro,
        habilitado=[True]
        )
        label_procesos_bottom.grid(sticky="nsew")

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
    frame_procesos_bottom,
    tituloCriterios="Platos Marroquís Disponibles",
    criterios=["Nombre"],
    tituloValores="El que usted desea mi rey",
    valores=[nombre_platos],
    tipo=2,
    comandoContinuar=cantidad_de_los_platos,
    habilitado=[True]
    )
    label_procesos_bottom.grid(sticky="nsew")

def comida_francesa():
    global label_procesos_bottom, label_procesos_mid
    chef_elegido = None
    for personal in Trabajador.cocineros:
        if personal.get_especialidad() == "Francesa":
            chef_elegido = personal
    nombre_platos=[]
    for platos in Plato.gastronomias_francesa:
        nombre_platos.append(platos.get_nombre())

    mensaje = (f"El/la chef {chef_elegido.get_nombre()} ha escogido los siguientes platos para ti\n"
            "Je vous remercie de votre présence dans notre restaurant La Sangre de Cristo tiene Poder.")
    label_procesos_mid.config(text=mensaje, wraplength=400, justify="center", font=("Arial", 12), fg="#fff")

    def cantidad_de_los_platos():
        global label_procesos_bottom, label_procesos_mid
        label_procesos_mid.config(text="Escoge la cantidad de platos que requieras en tu velada")
        plato_final = label_procesos_bottom.valores[0]

        def final_gastro():
            nonlocal plato_final
            global label_procesos_mid, label_procesos_bottom
            cantidad_final = label_procesos_bottom.valores[0]
            plato = None
            for platos in Plato.gastronomias_francesa:
                if platos.get_nombre() == plato_final:
                    plato = platos

            plato.set_veces_pedido(int(cantidad_final))
            coste_evento = 345000
            descripcion_evento = ".....Merci de faire confiance à notre restaurante"
            nombre_evento = "Gastronomias Mundiales"
            evento_elegido = Evento(nombre_evento, coste_evento, [plato])
            evento_elegido.set_descripcion(descripcion_evento)
            EstadoGlobal.evento_final = evento_elegido
            EstadoGlobal.factura_final = Factura()
            EstadoGlobal.factura_final.set_evento(EstadoGlobal.evento_final)

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="Escoge la cantidad que desees",
        criterios=["Miralas"],
        tituloValores="Seleccione",
        valores=[],
        tipo=0,
        comandoContinuar=final_gastro,
        habilitado=[True]
        )
        label_procesos_bottom.grid(sticky="nsew")

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
    frame_procesos_bottom,
    tituloCriterios="Platos Franceses Disponibles",
    criterios=["Nombre"],
    tituloValores="El que usted desea mi rey",
    valores=[nombre_platos],
    tipo=2,
    comandoContinuar=cantidad_de_los_platos,
    habilitado=[True]
    )
    label_procesos_bottom.grid(sticky="nsew")

###Interacción 3 Final

def hora_reserva_funcion():
    global label_procesos_bottom, label_procesos_mid

    def obtener_hora():
        global label_procesos_bottom
        try:
            hora = label_procesos_bottom.getValue("Hora")
            minutos= label_procesos_bottom.getValue("Minutos")
            dia = label_procesos_bottom.getValue("Dia")
            mes = label_procesos_bottom.getValue("Mes")

            if (0> int(hora) >=24):
                raise ExcepcionFueraRango(hora, "La hora debe ser un número, aparte de ello ser menos de 24")
            if not hora.isdigit():
                raise ValueError("Ingrese un dato numérico")
            if not (1 <= int(minutos) <= 59):
                raise ExcepcionFueraRango(minutos, "1-59 (Acuerdate que los minutos de una hora son 60)")
            
            if not (1 <= int(dia) <= 31):
                raise ExcepcionFueraRango(minutos, "1-31 (Acuerdate que los dias maximos por mes son 31)")
            if not (1 <= int(mes) <= 12):
                raise ExcepcionFueraRango(minutos, "1-12 (Solo hay 12 meses, no más)")
            
            EstadoGlobal.hora_reserva = hora

        except ExcepcionFueraRango as e:
            print(f"Error: {e}")
            messagebox.showerror("Error de Digitación", str(e))
        
        except ErrorAplicacion as e:
            print(f"Error: {e}")
            messagebox.showerror("Error de Aplicación", str(e))

        except ValueError:
            messagebox.showerror("Error de Formato", "Ingrese un número válido.")               
        
    mensaje_meeting = ("Por favor indicar la fechas en formato militar (HH:MM). Digite por favor el día y el mes")

# Configura el label con texto ajustado para imprimir
    label_procesos_mid.config(text=mensaje_meeting, wraplength=400, justify="left", font=("Arial", 10), fg="#fff")
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="No indica por favor la hora de su reserva",
        criterios=["Hora", "Minutos", "Dia", "Mes", "Año"],
        tituloValores="Digite uno por uno",
        valores=[],
        tipo=0,
        comandoContinuar=obtener_hora,
        habilitado=[True, True, True, True, False]
        )
    label_procesos_bottom.grid(sticky="nsew")



def diseno_de_factura(evento, cliente, horario):
    evento1 = evento.get_evento()
    cliente1 = cliente
    horario1 = horario

    
    plato = evento1.get_platos()[0]
    cantidad = plato.get_veces_pedido()
    cantidad_a_pagar = (cantidad * plato.get_precio()) + evento1.get_coste()

    if int(horario1) > 20:
        cantidad_a_pagar += int(cantidad_a_pagar * 0.08)
    else:
        cantidad_a_pagar += int(cantidad_a_pagar * 0.03)

    valor = (f"{plato.get_nombre()}   X{plato.get_veces_pedido()}   ...   {plato.get_veces_pedido() * plato.get_precio()}\n")


    
    mensaje = (f"                                                                                             .......{cliente1.get_restaurante().get_nombre()}........\n\n"
            f"                                                                                             Cliente: {cliente1.get_nombre()}..............\n"
            f"                                                                                             Cédula: {cliente1.get_cedula()}..............\n\n\n"
            f"                                                                                             {valor}\n\n"
            f"                                                                                             Total a pagar ......... {cantidad_a_pagar}\n\n\n"
            f"                                                                               ........{evento1.get_descripcion()} .......\n\n\n"
            f"                                                                               ...............Mil Gracias a Todos y Todas..............")
    return mensaje


def factura_final(mensaje):
    global label_procesos_bottom

    # Verifica si el widget existe y lo destruye
    if label_procesos_bottom:
        label_procesos_bottom.destroy()

    # Crea un frame que contendrá el Text y la scrollbar
    frame_texto = Frame(frame_procesos_bottom, bg="#545454")
    frame_texto.grid(sticky="nsew")

    # Crea un widget Text
    texto_widget = Text(
        frame_texto,
        wrap=WORD,  # Ajusta el texto automáticamente a la siguiente línea
        font=("Arial", 14),  # Fuente ajustable
        bg="#545454",  # Fondo oscuro para que coincida con el diseño
        fg="#fff",  # Texto en color blanco
        relief="flat",  # Sin borde visible
        padx=10, pady=10  # Margen para que se vea mejor
    )

    # Barra de desplazamiento vertical
    scrollbar = Scrollbar(frame_texto, command=texto_widget.yview)
    texto_widget.config(yscrollcommand=scrollbar.set)

    # Inserta el mensaje
    texto_widget.insert(END, mensaje)

    # Deshabilita la edición del texto (solo lectura)
    texto_widget.config(state=DISABLED)

    # Ubica el widget Text y la scrollbar en el frame
    texto_widget.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configura el grid para que el Text se ajuste automáticamente
    frame_texto.grid_rowconfigure(0, weight=1)
    frame_texto.grid_columnconfigure(0, weight=1)




###HASTA ACÁ VA FUNCIONALIDAD 5

def redimensionar_imagen(image, width, height):
    return image.resize((width, height), Image.LANCZOS)

# Función para cambiar la imagen
def cambiar_cv(event):
    global contador_clicks_cv

    rb_lt_size = [frame_rb_lt_img.winfo_width(), frame_rb_lt_img.winfo_height()]
    rb_rt_size = [frame_rb_rt_img.winfo_width(), frame_rb_rt_img.winfo_height()]
    rb_lb_size = [frame_rb_lb_img.winfo_width(), frame_rb_lb_img.winfo_height()]
    rb_rb_size = [frame_rb_rb_img.winfo_width(), frame_rb_rb_img.winfo_height()]

    # Listas de rutas de imágenes
    cvs = [
        ["Juan José Arango Marín\nTeléfono: 304 386 4396\nEdad: 19\nPregrado: Ingeniería en Sistemas e Informática\nConocimientos: Java, Inglés, Fútbol\nExperiencia: Acompañamiento de eventos, \natención en mostrador."],
        ["Samuel Colorado Castrillon\nTeléfono: 305 224 6361\nEdad: 18\nPregrado: Ingeniería en Sistemas e Informática\nConocimientos: Java, Python\nHabilidades: Aprendizaje rápido, resolución de problemas"],
        ["Stiven Saldarriaga Mayorga\nTeléfono: 322 778 1217\nEdad: 18\nPregrado: Ingeniería en Sistemas e Informática\nConocimientos: Java, ColdFusion, Metafísica pura\nExperiencia: Five Pack Alliance"]
    ]

    rutas = [
        ["src/Imagenes/desarrolladores/arango1.png", "src/Imagenes/desarrolladores/arango2.png", "src/Imagenes/desarrolladores/arango3.png", "src/Imagenes/desarrolladores/arango4.png"],
        ["src/Imagenes/desarrolladores/colorado1.png", "src/Imagenes/desarrolladores/colorado2.png", "src/Imagenes/desarrolladores/colorado3.png", "src/Imagenes/desarrolladores/colorado4.png"],
        ["src/Imagenes/desarrolladores/saldarriaga1.png", "src/Imagenes/desarrolladores/saldarriaga2.png", "src/Imagenes/desarrolladores/saldarriaga3.png","src/Imagenes/desarrolladores/saldarriaga4.png"]
    ]
    #boton_right_top.config(text=cvs[contador_clicks_cv][0])
    # Actualizar las rutas de las imágenes de acuerdo al contador de clics
    ruta_rb_lt = rutas[contador_clicks_cv][0]
    ruta_rb_rt = rutas[contador_clicks_cv][1]
    ruta_rb_lb = rutas[contador_clicks_cv][2]
    ruta_rb_rb = rutas[contador_clicks_cv][3]
    
    # Cargar y redimensionar las imágenes
    img_lt = redimensionar_imagen(Image.open(ruta_rb_lt), rb_lt_size[0], rb_lt_size[1])
    img_rt = redimensionar_imagen(Image.open(ruta_rb_rt), rb_rt_size[0], rb_rt_size[1])
    img_lb = redimensionar_imagen(Image.open(ruta_rb_lb), rb_lb_size[0], rb_lb_size[1])
    img_rb = redimensionar_imagen(Image.open(ruta_rb_rb), rb_rb_size[0], rb_rb_size[1]) #Cambbiar si David dice que se puede pregunta #4

    # Convertir las imágenes a PhotoImage
    photo_lt = ImageTk.PhotoImage(img_lt)
    photo_rt = ImageTk.PhotoImage(img_rt)
    photo_lb = ImageTk.PhotoImage(img_lb)
    photo_rb = ImageTk.PhotoImage(img_rb)

    # Actualizar las imágenes en los labels
    frame_rb_lt_img.config(image=photo_lt)
    frame_rb_lt_img.image = photo_lt  # Necesario para evitar que la imagen se recolecte por el garbage collector

    frame_rb_rt_img.config(image=photo_rt)
    frame_rb_rt_img.image = photo_rt

    frame_rb_lb_img.config(image=photo_lb)
    frame_rb_lb_img.image = photo_lb

    frame_rb_rb_img.config(image=photo_rb)
    frame_rb_rb_img.image = photo_rb

    right_top.config(text=cvs[contador_clicks_cv][0])

    # Incrementar el contador para la próxima rotación
    contador_clicks_cv = (contador_clicks_cv + 1) % len(rutas)

def cambiar_img_restaurante(event):
    global contador_pasa_img_res

    lb_top_size = [frame_lb_top.winfo_width(), frame_lb_top.winfo_height()]

    rutas = ["src/Imagenes/sistema/sistema1.png", "src/Imagenes/sistema/sistema2.png", "src/Imagenes/sistema/sistema3.png", "src/Imagenes/sistema/sistema4.png", "src/Imagenes/sistema/sistema5.png"]
    
    ruta = rutas[contador_pasa_img_res % 5]

    img = redimensionar_imagen(Image.open(ruta), lb_top_size[0], lb_top_size[1])

    photo = ImageTk.PhotoImage(img)
    
    frame_lb_top.config(image = photo)
    frame_lb_top.image = photo

    contador_pasa_img_res = (contador_pasa_img_res + 1) % 5

def tamano_texto(event, label):
    # Obtener las dimensiones del label
    label_width = event.width
    label_height = event.height

    # Calcular un tamaño de fuente adecuado basado en el tamaño del label
    new_font_size = min(label_width // 35, label_height // 8)
    
    # Establecer la nueva fuente
    label.config(font=("Arial", new_font_size))

def cambiar_proceso(event, num_func):
    global label_procesos_bottom
    if num_func == 0:
        label_procesos_top.config(text="Funcionalidades")
        label_procesos_mid.config(text="Descripciones")
        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Información", tituloValores="" , criterios=["Para acceder a las funcionalidades diríjase a la pestaña Procesos y Consultas.\nPosteriormente seleccione la funcionalidad a la que desea acceder."], tipo=3)
        label_procesos_bottom.grid(sticky="nsew")
    elif num_func == 1:
        label_procesos_top.config(text="Reservar Mesa")
        reservar_mesa()
    elif num_func == 2:
        label_procesos_top.config(text="Ordenar Comida")
    elif num_func == 4:
        label_procesos_top.config(text="Agregar Sede")
        restaurante = Restaurante()
        comala = Ciudad()
        comala.get_restaurantes().append(restaurante)
        restaurante.set_ciudad(comala)
        agregar_sede()
    elif num_func == 5:
        label_procesos_top.config(text="Crear Evento")
        crearEvento()


def info_aplicacion():
    messagebox.showinfo(title="Información de la aplicación", message="Esta aplicación simula el funcionamiento de una cadena de restaurantes a través de distintas funcionalidades como la de reservar una mesa, ordenar comida, agregar sedes y organizar eventos.")

def info_aplicacion_p3():
    mensaje_bienvenida.config(text="Esta aplicación simula el funcionamiento de una\ncadena de restaurantes a través de distintas\nfuncionalidades como la de reservar una mesa,\nordenar comida, agregar sedes y organizar eventos.")

def menu_inicio():
    ventana_funcional.withdraw()
    ventana_inicio.deiconify()
    ventana_inicio.state("zoomed")
    ventana_inicio.geometry("1080x750")

def menu_funcional():
    entrar()
    ventana_inicio.withdraw()
    ventana_funcional.deiconify()
    ventana_funcional.state("zoomed")
    ventana_funcional.geometry("1080x750")

def funcionalidad_0():
    cambiar_proceso(None, 0)

def funcionalidad_1():
    cambiar_proceso(None, 1)
    pass

def funcionalidad_2():
    cambiar_proceso(None, 2)
    pass

def funcionalidad_3():
    cambiar_proceso(None, 3)
    pass

def funcionalidad_4():
    cambiar_proceso(None, 4)
    pass

def funcionalidad_5():
    cambiar_proceso(None, 5)
    pass

def acerca_de():
    messagebox.showinfo("Acerca de", "Autores:\n- Juan José Arango Marín.\n- Samuel Colorado Castrillón.\n- Stiven Saldarriaga Mayorga.")

hojas_de_vida = ["Juan José",  "Colorado", "Stiven"]

def salir():
    Serializador.serializar_listas()
    ventana_inicio.quit()

def entrar():
    Deserializador.deserializar_listas()
    
#MENU INICIO
ventana_inicio = Tk()
ventana_inicio.title("Menú Inicio")
ventana_inicio.state("zoomed")
ventana_inicio.geometry("1080x750")
ventana_inicio.iconbitmap("src/Imagenes/susy-oveja.ico")
ventana_inicio.config(bg="#838383")

menu_bar_inicio = Menu(ventana_inicio)
ventana_inicio.config(menu = menu_bar_inicio)
menu_inicial = Menu(menu_bar_inicio, tearoff = 0)
menu_bar_inicio.add_cascade(label = "Inicio", menu = menu_inicial)
menu_inicial.add_command(label = "Descripción del sistema", command = info_aplicacion_p3)
menu_inicial.add_separator()
menu_inicial.add_command(label = "Salir", command = salir)

#Frame P1
frame_left = Frame(ventana_inicio, bg = "#696969", bd = 2, relief="solid", width=100)
frame_left.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)
frame_left.pack_propagate(False)

#Frame P3
frame_left_top = Frame(frame_left, bd = 2, relief="solid", bg = "#545454")
frame_left_top.pack(side = TOP, fill = BOTH, expand = True, padx=10, pady = 10)
frame_left_top.pack_propagate(False)

#Mensaje Bienvenida
mensaje_bienvenida = Label(frame_left_top, text="Bienvenidos sean al Restaurante Orientado a Objetos", bg = "#545454", fg="#fff")
mensaje_bienvenida.pack(expand = True, fill = BOTH, padx = 10, pady = 10)
mensaje_bienvenida.bind("<Configure>", lambda event: tamano_texto(event, mensaje_bienvenida))

#Frame P4
frame_left_bottom = Frame(frame_left, height=200, bg = "#545454", bd = 2, relief="solid")
frame_left_bottom.pack(side = BOTTOM, fill = BOTH, expand = True, padx = 10, pady = 10)
frame_left_bottom.pack_propagate(False)

funcional_button = Button(frame_left_bottom, text="Acceder a las funcionalidades", bd = 4, font=("Arial", 20), bg = "#434343", fg="#fff", command = lambda: menu_funcional())   
funcional_button.pack(side = BOTTOM, fill = X, padx = 10, pady = 10)

frame_lb_top = Label(frame_left_bottom, bg = "white", relief="solid", bd = 2)
frame_lb_top.bind("<Leave>", cambiar_img_restaurante)
frame_lb_top.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

ventana_inicio.update()

cambiar_img_restaurante(None)

#Frame P2
frame_right = Frame(ventana_inicio, bg = "#696969", bd = 2, relief="solid", width=100)
frame_right.pack(side = RIGHT, fill = BOTH, expand = True, padx = 10, pady = 10)
frame_right.pack_propagate(False)

#Frame P5
frame_right_top = Frame(frame_right, bd = 2, relief="solid", bg = "#545454")
frame_right_top.pack(side = TOP, fill = BOTH, expand = True, padx=10, pady = 10)
frame_right_top.pack_propagate(False)

#Descripción CV
right_top = Label(frame_right_top, bg = "#545454", fg="#fff", justify="left")
right_top.bind("<Button-1>", cambiar_cv)
right_top.bind("<Configure>", lambda event: tamano_texto(event, right_top))
right_top.pack(expand = True, fill = BOTH, padx = 10, pady = 10)

#Frame P6
frame_right_bottom = Frame(frame_right, height=200, width = 100, bg = "#545454", bd = 2, relief="solid")
frame_right_bottom.pack(side = BOTTOM, fill = BOTH, expand = True, padx = 10, pady = 10)
frame_right_bottom.grid_propagate(False)

frame_right_bottom.grid_rowconfigure(0, weight=1)
frame_right_bottom.grid_columnconfigure(0, weight=1)
frame_right_bottom.grid_rowconfigure(1, weight=1)
frame_right_bottom.grid_columnconfigure(1, weight=1)

#Imagen recuadro superior izquierdo del recuadro inferior derecho
frame_rb_lt_img = Label(frame_right_bottom, bd = 2, relief="solid")
frame_rb_lt_img.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

#Imagen recuadro superior derecho del recuadro inferior derecho
frame_rb_rt_img = Label(frame_right_bottom, bd = 2, relief="solid")
frame_rb_rt_img.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

#Imagen recuadro inferior del recuadro inferior derecho
frame_rb_lb_img = Label(frame_right_bottom, bd = 2, relief="solid")
frame_rb_lb_img.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

#Imagen recuadro inferior del recuadro inferior derecho
frame_rb_rb_img = Label(frame_right_bottom, bd = 2, relief="solid") #, width=456, height=272
frame_rb_rb_img.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

ventana_inicio.update()

cambiar_cv(None)

#Menu funcional
ventana_funcional = Tk()
ventana_funcional.title("Menú funcional")
ventana_funcional.state("zoomed")
ventana_funcional.geometry("1080x750")
ventana_funcional.iconbitmap('src/Imagenes/susy-oveja.ico')
ventana_funcional.config(bg="#838383")

#Formatear texto de las Cajacombo
ventana_funcional.option_add('*TCombobox*Listbox.font', ('Arial', 15))
ventana_funcional.option_add('*TCombobox.font', ('Arial', 15))

#Menu superior ventana funcional
menu_bar_funcional = Menu(ventana_funcional)
ventana_funcional.config(menu = menu_bar_funcional)
menu_archivo = Menu(menu_bar_funcional, tearoff = 0)
menu_bar_funcional.add_cascade(label = "Archivo", menu = menu_archivo)
menu_archivo.add_command(label = "Aplicación", command = info_aplicacion)
menu_archivo.add_separator()
menu_archivo.add_command(label = "Salir", command = menu_inicio)

menu_procesos = Menu(menu_bar_funcional, tearoff = 0)
menu_bar_funcional.add_cascade(label = "Procesos y Consultas", menu = menu_procesos)

#Ir a la funcionalidad 1
menu_procesos.add_command(label = "Funcionalidad 1", command = funcionalidad_1)
menu_procesos.add_separator()

#Ir a la funcionalidad 2
menu_procesos.add_command(label = "Funcionalidad 2", command = funcionalidad_2)
menu_procesos.add_separator()

#Ir a la funcionalidad 3
menu_procesos.add_command(label = "Funcionalidad 3", command = funcionalidad_3)
menu_procesos.add_separator()

#Ir a la funcionalidad 4
menu_procesos.add_command(label = "Funcionalidad 4", command = funcionalidad_4)
menu_procesos.add_separator()

#Ir a la funcionalidad 5
menu_procesos.add_command(label = "Funcionalidad 5", command = funcionalidad_5)

menu_ayuda = Menu(menu_bar_funcional, tearoff=0)
menu_bar_funcional.add_cascade(label = "Ayuda", menu = menu_ayuda)
menu_ayuda.add_command(label = "Acerca de", command = acerca_de)

#Frame donde estará la información de las funcionalidades
frame_procesos = Frame(ventana_funcional, bd = 2, relief="solid", bg="#696969")
frame_procesos.pack(fill = BOTH, expand = True, padx = 10, pady = 10)

frame_procesos.grid_rowconfigure(0, weight=1)
frame_procesos.grid_columnconfigure(0, weight=1)
frame_procesos.grid_rowconfigure(1, weight=1)
frame_procesos.grid_rowconfigure(2, weight=1)

#Frames frame_procesos
#Titulo funcionalidad
frame_procesos_top = Frame(frame_procesos, bd = 2, relief="solid")
frame_procesos_top.grid(row = 0, padx = 10, pady = 10, sticky="nsew")
frame_procesos_top.grid_propagate(False)
frame_procesos_top.grid_rowconfigure(0, weight=1)
frame_procesos_top.grid_columnconfigure(0, weight=1)
label_procesos_top = Label(frame_procesos_top, text="Funcionalidades", font=("Arial", 20), bg = "#545454", fg="#fff")
label_procesos_top.grid(sticky="nsew")

#Desripcion funcionalidad
frame_procesos_mid = Frame(frame_procesos, bd = 2, relief="solid")
frame_procesos_mid.grid(row = 1, padx = 10, pady = 10, sticky="nsew")
frame_procesos_mid.grid_propagate(False)
frame_procesos_mid.grid_rowconfigure(0, weight=1)
frame_procesos_mid.grid_columnconfigure(0, weight=1)
label_procesos_mid = Label(frame_procesos_mid, text="Descripciones", font=("Arial", 20), bg = "#545454", fg="#fff")
label_procesos_mid.grid(sticky="nsew")

#Campo FieldFrame
frame_procesos_bottom = Frame(frame_procesos, bd = 2, height = 300, relief="solid", bg = "#545454")
frame_procesos_bottom.grid(row = 2, padx = 10, pady = 10, sticky="nsew")
frame_procesos_bottom.grid_propagate(False)
frame_procesos_bottom.grid_rowconfigure(0, weight=1)
frame_procesos_bottom.grid_columnconfigure(0, weight=1)
label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Información", tituloValores="" , criterios=["Para acceder a las funcionalidades diríjase a la pestaña Procesos y Consultas.\nPosteriormente seleccione la funcionalidad a la que desea acceder."], tipo=3)
label_procesos_bottom.grid(sticky="nsew")

menu_inicio()

#Asegurarse que al cerrar la ventana se cierre la ventana
def cerrado():
    salir()

ventana_inicio.protocol("WM_DELETE_WINDOW", cerrado)
ventana_funcional.protocol("WM_DELETE_WINDOW", cerrado)

ventana_inicio.mainloop()

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
            # limpiar_pantalla()
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
                            reservar_mesa()
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
                                reservar_mesa()
                            elif eleccion2 == 2:
                                reservar_mesa()
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
# a
# a
# a
# a





# def crear_ingrediente(cantidad_ingredientes, ingredientes_plato):
#     global label_procesos_bottom
    
#     def f4_i3_establecer_ingrediente():
#         nombre_ingrediente = label_procesos_bottom.valores[0]
#         try:
#             precio_ingrediente = int(label_procesos_bottom.valores[1])
#         except:
#             raise ExcepcionDatosErroneos(["Precio Ingrediente"])
#         try:
#             cantidad_ingrediente = int(label_procesos_bottom.valores[2])
#         except:
#             raise ExcepcionDatosErroneos(["Cantidad Ingrediente"])

#         if precio_ingrediente < 1:
#             precio_ingrediente = 1
        
#         if cantidad_ingrediente < 1:
#             cantidad_ingrediente = 1

#         ingrediente = Ingrediente(nombre_ingrediente, precio_ingrediente)
#         ingredientes_plato.append(ingrediente)
        
#         print("Ingresa la cantidad necesaria de este ingrediente para la " +
#             "preparación del plato")
#         cantidad_ingrediente = Utilidad.readInt()
        
        
        
#         cantidad_ingredientes.append([ingrediente.get_nombre(), str(cantidad_ingrediente)])
    
#     label_procesos_bottom.destroy()
#     label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios = "Dato", criterios = ["Nombre Ingrediente", "Precio Ingrediente", "Cantidad Ingrediente"], tituloValores = "Valor ingresado", tipo = 0, habilitado = [True, True, True], comandoContinuar=f4_i3_establecer_ingrediente)
#     label_procesos_bottom.grid(sticky="nsew")
    
#     return cantidad_ingredientes


#Funcionalidad 5
# def reservar_mesa():
#     global label_procesos_bottom

#     label_procesos_bottom.destroy()
#     label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea", criterios=None, tituloValores="continuar?", tipo=1)
#     label_procesos_bottom.grid(sticky="nsew")

    

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

# if __name__ == "__main__":
#     Ciudad.get_ciudades().clear()
#     Zona.get_zonas().clear()
#     Ciudad("Medellin")
    
#     # print(Casilla.get_casillas())
#     # print(Ciudad.get_ciudades())
#     # print(Mesa.get_mesas())
#     # print(Zona.get_zonas())
#     # print(Cargamento.get_cargamentos())
#     # print(Evento.get_eventos())
#     # print(Factura.get_facturas())
#     # print(Ingrediente.get_ingredientes())
#     # print(Pedido.get_pedidos())
#     # print(Plato.get_platos())
#     # print(Reserva.get_reservas())
#     # print(Restaurante.get_restaurantes())
#     # print(Trabajador.get_cocineros())
#     # print(Cliente.get_clientes())
    
#     print("¿Qué desea hacer?")
#     print("1. Reservar mesa.")
#     print("2. Ordenar comida.")
#     print("3. Abandonar restaurante.")
#     print("4. Agregar sede.")
#     print("5. Organizar evento.")
#     print("6. Salir.")
#     eleccion = Utilidad.readInt()
#     if eleccion == 1:
#         reservar_mesa()
#     elif eleccion == 2:
#         ordenar_comida()
#     elif eleccion == 3:
#         dejar_restaurante()
#     elif eleccion == 4:
#         agregar_sede()
#     elif eleccion == 5:
#         crear_evento()
#     elif eleccion == 6:
#         print("Gracias por visitarnos.")