from Entorno.ciudad import Ciudad



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

    def listadoCiudades():
        if len(Ciudad.get_ciudades) != 0:
            Ciudad.get_ciudades().sort(key = lambda ciudad: ciudad.get_nombre(), reverse = True)
            for i in range(0, len(Ciudad.get_ciudades())):
                print(f"{i + 1}. {Ciudad.get_ciudades[i].get_nombre()}")
        else: 
            pass

    def listadoZonasCiudad(ciudad = Ciudad()):
        if len(ciudad.get_zonas_ciudad()) != 0:
            ciudad.get_zonas_ciudad().sort(key = lambda zona: zona.get_nombre(), reverse = True)
            for i in range(0, len(ciudad.get_zonas_ciudad())):
                print(f"{i + 1}. {ciudad.get_zonas_ciudad()[i].get_nombre()}")
        else:
            pass

#Es posible que ni siquiera se usen estos métodos, así que de ser necesarios, los traduzco.