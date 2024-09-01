from utilidad import Utilidad
from gestorAplicacion import *
import datetime
from datetime import datetime
import random

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
            limpiar_pantalla()
            menu_principal()
            encendido = False
            
        else:
            limpiar_pantalla()
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
