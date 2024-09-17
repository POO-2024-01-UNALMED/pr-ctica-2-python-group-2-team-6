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

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

contador_clicks_cv = 0
contador_pasa_img_res = 0
funcionalidad_actual = 0

def dejar_restaurante():
    print("Funcionalidad 3")
    global label_procesos_bottom
    global label_procesos_mid
    restaurante1 = Restaurante()
    mesa1 = Mesa(3, False)
    restaurante1.agregar_mesa(mesa1)
    mesa1.set_restaurante(restaurante1)

    clientes_mesa1 = []
    cliente1 = Cliente("Juan", 123, Afiliacion.ESTRELLA, "1234567")
    cliente1.set_mesa(mesa1)
    clientes_mesa1.append(cliente1)

    cliente2 = Cliente("Pedro", 456, Afiliacion.ESTRELLITA, "7654321")
    cliente2.set_mesa(mesa1)
    clientes_mesa1.append(cliente2)

    cliente3 = Cliente("María", 789, Afiliacion.SUPERESTRELLOTA, "9876543")
    cliente3.set_mesa(mesa1)
    clientes_mesa1.append(cliente3)

    mesa1.set_clientes(clientes_mesa1)
    restaurante1.set_clientes(clientes_mesa1)

    # Creación de ingredientes y platos
    tomate = Ingrediente("Tomate", 500)
    lechuga = Ingrediente("Lechuga", 300)
    ingredientes_ensalada = [tomate, lechuga]
    ensalada = Plato("Ensalada", 19000, ingredientes_ensalada)

    carne = Ingrediente("Carne", 1000)
    pan = Ingrediente("Pan", 500)
    ingredientes_hamburguesa = [carne, pan]
    hamburguesa = Plato("Hamburguesa", 25000, ingredientes_hamburguesa)

    arroz = Ingrediente("Arroz", 800)
    pollo = Ingrediente("Pollo", 700)
    ingredientes_arroz_con_pollo = [arroz, pollo]
    arroz_con_pollo = Plato("Arroz con pollo", 20000, ingredientes_arroz_con_pollo)

    # Creación de pedidos
    pedido1 = Pedido()
    pedido2 = Pedido()
    pedido3 = Pedido()

    pedido1.agregar_plato(ensalada)
    pedido2.agregar_plato(hamburguesa)
    pedido3.agregar_plato(arroz_con_pollo)

    # Creación de facturas
    factura1 = Factura(pedido=pedido1, valor= 0, pago_preconsumo=False, propina=0)
    factura2 = Factura(pedido=pedido2, valor= 0, pago_preconsumo=False, propina=0)
    factura3 = Factura(pedido=pedido3, valor= 0, pago_preconsumo=False, propina=0)

    cliente1.set_factura(factura1)
    cliente2.set_factura(factura2)
    cliente3.set_factura(factura3)    

    def f3_i1_cobrar_factura():
        global label_procesos_bottom
        label_procesos_mid.config(text="Ingrese la cédula del cliente que va a abandonar el restaurante.")

        # Función para buscar cliente por cédula
        def f3_i1_buscar_cedula():
            global label_procesos_bottom
            # Obtener el valor ingresado en el FieldFrame
            cedula_ingresada = int(label_procesos_bottom.valores[0])
            
            # Verificar si la cédula existe en la lista de clientes
            cliente_encontrado = None
            for cliente in restaurante1.get_clientes():
                if cliente.cedula == cedula_ingresada:  # Convertir la entrada en entero
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado is None:
                try:
                    raise ExcepcionDatosErroneos([cedula_ingresada])
                except ExcepcionDatosErroneos as e:
                    # Mostrar el error y permitir al usuario ingresar otra cédula
                    print("Error:", e.mensaje_error_valor)
                    label_procesos_bottom.limpiarEntradas()
            
            mesa_cliente = cliente_encontrado.get_mesa()
            valor_factura = 0
            for cliente in mesa_cliente.get_clientes():
                valor_factura += cliente.get_factura().calcular_valor()
            label_procesos_mid.config(text="Mostrando el valor de la factura de la mesa. Si desea añadir propina escriba el valor y presione aceptar.")
            propina = 0

            def f3_i1_aceptar_propina():
                global label_procesos_bottom
                global label_procesos_mid
                propina = int(label_procesos_bottom.valores[1])
                valor_factura = int(label_procesos_bottom.valores[0]) + propina
                label_procesos_mid.config(text="Valor total de la factura: " + str(valor_factura))

                def f3_i1_separar_factura():
                    global label_procesos_bottom
                    global label_procesos_mid
                    label_procesos_mid.config(text="Cada persona debe pagar: " + str(valor_factura // len(mesa_cliente.get_clientes())))
                    
                    def clientes_pagan_factura():
                        global label_procesos_bottom
                        global label_procesos_mid
                        valor_por_persona = valor_factura // len(mesa_cliente.get_clientes())
                        for cliente in mesa_cliente.get_clientes():
                            escoger_metodo_pago(cliente, valor_por_persona)
                            
                                                      

                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="", criterios=None, tituloValores="", tipo=1, comandoContinuar=clientes_pagan_factura)
                    label_procesos_bottom.grid(sticky="nsew")
                
                def f3_i1_pago_unitario():
                    global label_procesos_bottom
                    global label_procesos_mid
                    label_procesos_mid.config(text="Indique el número de cédula de quién va a pagar la factura.")

                    def f3_i1_buscar_cedula():
                        global label_procesos_bottom
                        global label_procesos_mid
                        label_procesos_mid.config(text="¿Desea pagar la factura?")
                        cedula_cliente = int(label_procesos_bottom.valores[0])
                        
                        cliente_pagador = None
                        for cliente in mesa_cliente.get_clientes():
                            if cliente.cedula == cedula_cliente:
                                cliente_pagador = cliente
                                break
                        if cliente_pagador is None:
                            try:
                                raise ExcepcionDatosErroneos([cedula_ingresada])
                            except ExcepcionDatosErroneos as e:
                                print("Error:", e.mensaje_error_valor)
                                label_procesos_bottom.limpiarEntradas()
                        else:
                            escoger_metodo_pago(cliente_pagador, valor_factura)

                    label_procesos_bottom.destroy()
                    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Información solicitada", criterios=["Cédula de quién realizará el pago"], tituloValores="Espacio para diligenciar información", tipo=0, comandoContinuar=f3_i1_buscar_cedula, comandoCancelar=funcionalidad_0)
                    label_procesos_bottom.grid(sticky="nsew")

                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desean separar la factura?", criterios=None, tituloValores="", tipo=1, comandoContinuar=f3_i1_separar_factura, comandoCancelar=f3_i1_pago_unitario)
                label_procesos_bottom.grid(sticky="nsew")
    
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Información solicitada", criterios=["Valor parcial", "Propina"], tituloValores="Espacios para llenar", valores= [valor_factura, propina], tipo=0, habilitado=[False, True], comandoContinuar=f3_i1_aceptar_propina)
            label_procesos_bottom.grid(sticky="nsew")

        # Destruir el frame antiguo antes de crear uno nuevo
        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Cédula", criterios=["Cédula"], tituloValores="Valor ingresado", tipo=0, comandoContinuar=f3_i1_buscar_cedula)
        label_procesos_bottom.grid(sticky="nsew")
    
    label_procesos_mid.config(text="Seleccione sí o no dependiendo de si quiere continuar")
    #Sí o No desea continuar con la funcionalidad 3
    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Algún cliente desea", criterios=None, tituloValores="abandonar el restaurante?", tipo=1, comandoContinuar=f3_i1_cobrar_factura, comandoCancelar=funcionalidad_0)
    label_procesos_bottom.grid(sticky="nsew")
       

def comando_prueba():
    print("Comando de prueba.")

# def escoger_metodo_pago(clientes):
#     global label_procesos_bottom
#     global label_procesos_mid

#     metodos_pago = ["Tarjeta", "Efectivo", "Puntos"]
#     for cliente in clientes:
#         label_procesos_mid.config(text=f"Seleccione el método de pago {cliente.nombre}.")
#         metodo_pago = label_procesos_bottom.valores[0]
#         cliente.get_factura().set_metodo_pago(metodo_pago)
    
#     label_procesos_bottom.destroy()
#     label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Información solicitada", criterios=["Método de pago"], tituloValores="Información proveída", valores=[metodos_pago], tipo=2, comandoContinuar=comando_prueba, comandoCancelar=funcionalidad_0)
#     label_procesos_bottom.grid(sticky="nsew")        




def escoger_metodo_pago(cliente_pagador, valor_por_persona):
    global label_procesos_bottom
    global label_procesos_mid
    metodos_pago = ["Tarjeta", "Efectivo", "Puntos"]
    label_procesos_mid.config(text=f"Seleccione el método de pago {cliente_pagador.nombre}.")
   
    metodo_pago = label_procesos_bottom.valores[0]
    cliente_pagador.get_factura().set_metodo_pago(metodo_pago)
    def aplicar_descuentos_cuenta():
        global label_procesos_bottom
        global label_procesos_mid
        valor_final = valor_por_persona

        if cliente_pagador.get_afiliacion() != Afiliacion.NINGUNA:
            print("Se aplicaron descuentos por su nivel de afiliación.")
            metodo_pago = cliente_pagador.get_factura().get_metodo_pago()
            valor_factura = cliente_pagador.get_factura().get_valor()

            # Afiliación ESTRELLITA
            if cliente_pagador.get_afiliacion() == Afiliacion.ESTRELLITA:
                if metodo_pago == "Efectivo":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.05
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 1)
                    else:
                        valor_final -= valor_por_persona * 0.07
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 2)
                elif metodo_pago == "Tarjeta":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.03
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 1)
                    else:
                        valor_final -= valor_por_persona * 0.05
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 2)
                elif metodo_pago == "Cheque":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.02
                    else:
                        valor_final -= valor_por_persona * 0.03
                    cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 1)

            # Afiliación ESTRELLA
            elif cliente_pagador.get_afiliacion() == Afiliacion.ESTRELLA:
                if metodo_pago == "Efectivo":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.07
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 2)
                    else:
                        valor_final -= valor_por_persona * 0.15
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 4)
                elif metodo_pago == "Tarjeta":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.08
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 2)
                    else:
                        valor_final -= valor_por_persona * 0.15
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 4)
                elif metodo_pago == "Cheque":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.02
                    else:
                        valor_final -= valor_por_persona * 0.10
                    cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 1)

            # Afiliación SUPERESTRELLOTA
            elif cliente_pagador.get_afiliacion() == Afiliacion.SUPERESTRELLOTA:
                if metodo_pago == "Efectivo":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.10
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 6)
                    else:
                        valor_final -= valor_por_persona * 0.20
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 8)
                elif metodo_pago == "Tarjeta":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.15
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 6)
                    else:
                        valor_final -= valor_por_persona * 0.25
                        cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 8)
                elif metodo_pago == "Cheque":
                    if valor_factura < 30000:
                        valor_final -= valor_por_persona * 0.05
                    else:
                        valor_final -= valor_por_persona * 0.08
                    cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() + 2)

        # Descuento por puntos acumulados
                if cliente_pagador.get_puntos_acumulados() >= 10:
                    print("Felicidades, ha obtenido un descuento de 10.000 por sus puntos acumulados.")
                    valor_final -= 10000
                    cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() - 10)
            label_procesos_mid.config(text=f"Obtuvo un descuento de: {valor_por_persona - valor_final}, el valor a pagar por {cliente_pagador.nombre} es de {valor_final}.")
        
        else:
            valor_final = valor_por_persona
            label_procesos_mid.config(text=f"El valor a pagar por {cliente_pagador.nombre} es de {valor_final}.")
        
        if cliente_pagador.get_puntos_acumulados() >= 10:
            print("Felicidades, ha obtenido un descuento de 10.000 por sus puntos acumulados.")
            valor_final -= 10000
            cliente_pagador.set_puntos_acumulados(cliente_pagador.get_puntos_acumulados() - 10)
        
        

        
        def confirmar_transaccion():
            global label_procesos_bottom
            global label_procesos_mid
            label_procesos_mid.config(text="¿Desea confirmar la transacción?")

            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Confirmar transacción", criterios=None, tituloValores="", tipo=1, comandoContinuar=lambda: liberar_mesa(cliente_pagador.get_mesa()), comandoCancelar=funcionalidad_0)
            label_procesos_bottom.grid(sticky="nsew")

        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Información solicitada", criterios=["Presione aceptar para continuar"], tituloValores="", tipo=3, comandoContinuar=confirmar_transaccion)
        label_procesos_bottom.grid(sticky="nsew")
        

    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Información solicitada", criterios=["Método de pago"], tituloValores="Seleccione un método de pago", valores=[metodos_pago], tipo=2, comandoContinuar=aplicar_descuentos_cuenta, comandoCancelar=funcionalidad_0)
    label_procesos_bottom.grid(sticky="nsew")

def reservar_mesa():
    print("Reservó")

def liberar_mesa(mesa):
    global label_procesos_bottom
    global label_procesos_mid
    # from main import reser
    for cliente in mesa.get_clientes():
        if cliente.get_afiliacion() is Afiliacion.NINGUNA:
            label_procesos_mid.config(text=f"{cliente.get_nombre()}, no está afiliado al restaurante, lo invitamos a que escoja uno de los niveles de afiliación.")
            def afiliar_cliente():
                global label_procesos_bottom
                global label_procesos_mid
                if label_procesos_bottom.valores[0] == "Ninguna":
                    afiliacion = Afiliacion.NINGUNA
                elif label_procesos_bottom.valores[0] == "Estrella":
                    afiliacion = Afiliacion.ESTRELLA
                elif label_procesos_bottom.valores[0] == "Estrellita":
                    afiliacion = Afiliacion.ESTRELLITA
                elif label_procesos_bottom.valores[0] == "Superestrellota":
                    afiliacion = Afiliacion.SUPERESTRELLOTA
                cliente.set_afiliacion(afiliacion)
                label_procesos_mid.config(text=f"{cliente.get_nombre()} ha sido afiliado con éxito.")
                label_procesos_bottom.destroy()
                label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Proceda a calificar el restaurante", criterios=None, tituloValores="", tipo=3)
                label_procesos_bottom.grid(sticky="nsew")
            
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Afiliación", criterios=["Afiliación"], tituloValores="Seleccione una afiliación", valores=["Ninguna", "Estrella", "Estrellita", "Superestrellota"], tipo=2, comandoContinuar=afiliar_cliente, comandoCancelar=funcionalidad_0)
            label_procesos_bottom.grid(sticky="nsew")

    label_procesos_mid.config(text="Indique si algún cliente desea hacer una nueva reservación.")

    def calificar_restaurante(cliente):
        global label_procesos_bottom
        global label_procesos_mid
        label_procesos_mid.config(text=f"Por favor {cliente.get_nombre()} califique el restaurante con una nota del 1 al 5.")
        calificacion = int(label_procesos_bottom.valores[0])

        if 1 <= calificacion <= 5:
            label_procesos_mid.config(text="Gracias por su calificación.")
            cliente.get_mesa().get_restaurante().set_calificacion(calificacion)
        else:
            raise ExcepcionFueraRango(calificacion, "1 - 5")
        
        def escribir_resena():
            global label_procesos_bottom
            global label_procesos_mid
            label_procesos_mid.config(text="Escriba la reseña.")
            resena = label_procesos_bottom.valores[0]
            cliente.get_mesa().get_restaurante().anadir_reserva(resena)
            if cliente.get_afiliacion() is not None:
                cliente.set_puntos_acumulados(cliente.get_puntos_acumulados() + 1)
                label_procesos_mid.config(text="Gracias por su reseña. Obtuvo un punto extra por ayudarnos a mejorar.")
            else:
                label_procesos_mid.config(text="Gracias por su reseña.")
            
            label_procesos_bottom.destroy()
            label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Finalizar proceso", criterios=None, tituloValores="", tipo=3)
            label_procesos_bottom.grid(sticky="nsew")


        label_procesos_bottom.destroy()
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Desea añadir una reseña?", criterios=None, tituloValores="Escriba su reseña", tipo=1, comandoContinuar=escribir_resena, comandoCancelar=funcionalidad_0)
        label_procesos_bottom.grid(sticky="nsew")


    label_procesos_bottom.destroy()
    label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="¿Algún cliente desea", criterios=None, tituloValores="reservar nuevamente?", tipo=1, comandoContinuar=reservar_mesa, comandoCancelar=calificar_restaurante, argComando=cliente)
    label_procesos_bottom.grid(sticky="nsew")










    


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
        ["Juan José Arango Marín\nTeléfono: 304 386 4396\nEdad: 19\nPregrado: Ingeniería en Sistemas e Informática\nConocimientos: Java, Cáida libre, AntiJudio 卐卐卐卐卐\nAlgo más: Mueran todos los negros"],
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
        label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Descripción", tituloValores="funcionamiento" , criterios=["Para acceder a las funcionalidades diríjase a la pestaña Procesos y Consultas.\nPosteriormente seleccione la funcionalidad a la que desea acceder."], tipo=3)
        label_procesos_bottom.grid(sticky="nsew")
    elif num_func == 1:
        label_procesos_top.config(text="Reservar Mesa")
        reservar_mesa()
    elif num_func == 3:
        label_procesos_top.config(text="Dejar Restaurante")
        dejar_restaurante()
        
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
menu_inicial.add_command(label = "Salir", command = ventana_inicio.quit)

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
right_top = Label(frame_right_top, text = "Hoja de Vida de los desarrolladores", bg = "#545454", fg="#fff")
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
label_procesos_bottom = FieldFrame(frame_procesos_bottom, tituloCriterios="Descripción", tituloValores="funcionamiento" , criterios=["Para acceder a las funcionalidades diríjase a la pestaña Procesos y Consultas.\nPosteriormente seleccione la funcionalidad a la que desea acceder."], tipo=3)
label_procesos_bottom.grid(sticky="nsew")

menu_inicio()

#Asegurarse que al cerrar la ventana se cierre la ventana
def cerrado():
    ventana_inicio.quit()

ventana_inicio.protocol("WM_DELETE_WINDOW", cerrado)
ventana_funcional.protocol("WM_DELETE_WINDOW", cerrado)

ventana_inicio.mainloop()