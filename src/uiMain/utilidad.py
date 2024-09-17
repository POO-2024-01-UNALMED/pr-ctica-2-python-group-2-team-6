from gestorAplicacion.Entorno.ciudad import Ciudad
from gestorAplicacion.Usuario.cliente import Cliente


class Utilidad:

    def readInt():
        try:
            num = int(input("Ingrese el número: "))
            return num
        except:
            print("Ingrese un número entero.")
            Utilidad.readInt()
    
    def readFloat():
        try:
            num = float(input("Ingrese el número: "))
            return num
        except:
            print("Ingrese un número entero.")
            Utilidad.readFloat()

    def listado_ciudades():
        if len(Ciudad.get_ciudades()) != 0:
            for i in range(0, len(Ciudad.get_ciudades())):
                print(f"{i + 1}. {Ciudad.get_ciudades()[i].get_nombre()}")
        else: 
            pass

    def listado_zonas_ciudad(ciudad = Ciudad()):
        if len(ciudad.get_zonas_ciudad()) != 0:
            ciudad.get_zonas_ciudad().sort(key = lambda zona: zona.get_nombre(), reverse = True)
            for i in range(0, len(ciudad.get_zonas_ciudad())):
                print(f"{i + 1}. {ciudad.get_zonas_ciudad()[i].get_nombre()}")
        else:
            print("La ciudad no tiene zonas")
    
    def existe_cliente(cliente_consulta):
        for cliente in Cliente.get_clientes():
            if cliente_consulta.get_cedula() == cliente.get_cedula():
                return True
            else:
                return False
    
    def cliente_cedula(cliente_consulta):
        for cliente in Cliente.get_clientes():
            if cliente_consulta.get_cedula() == cliente.get_cedula():
                return cliente
    
    def calcular_distancia(restaurante, preferencia, tipo_mesa):
        mesas = []
        mesas_elegidas = []
        menor_distancia = 9999
        
        for mesa in restaurante.get_mesas():
            if mesa.is_vip() == tipo_mesa:
                mesas.append(mesa)
        
        if preferencia == "Puerta":  # Puerta
            puertas = []
            for casilla in restaurante.get_casillas():
                if casilla.get_tipo() == "PUERTA":
                    puertas.append(casilla)
            
            # Ver mesas más cercanas a una puerta
            for casilla in puertas:
                for mesa in mesas:
                    distancia_puerta = abs((casilla.get_coordX() - mesa.get_coordX()) + 
                                        (casilla.get_coordY() - mesa.get_coordY()))
                    mesa.set_distancia_puerta(distancia_puerta)
                    if distancia_puerta < menor_distancia:
                        menor_distancia = distancia_puerta
            
            for mesa in mesas:
                if mesa.get_distancia_puerta() == menor_distancia:
                    mesas_elegidas.append(mesa.get_num_mesa())
        
        else:  # Ventana
            ventanas = []
            for casilla in restaurante.get_casillas():
                if casilla.get_tipo() == "VENTANA":
                    ventanas.append(casilla)
            
            # Ver mesas más cercanas a una ventana
            for casilla in ventanas:
                for mesa in mesas:
                    distancia_ventana = abs(casilla.get_coordX() - mesa.get_coordX()) + \
                                        abs(casilla.get_coordY() - mesa.get_coordY())
                    mesa.set_distancia_ventana(distancia_ventana)
                    if distancia_ventana < menor_distancia:
                        menor_distancia = distancia_ventana
            
            for mesa in mesas:
                if mesa.get_distancia_ventana() == menor_distancia:
                    mesas_elegidas.append(mesa.get_num_mesa())
        
        return mesas_elegidas


#Es posible que ni siquiera se usen estos métodos, así que de ser necesarios, los traduzco.