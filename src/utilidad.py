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

#Es posible que ni siquiera se usen estos métodos, así que de ser necesarios, los traduzco.