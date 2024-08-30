class Utilidad:

    def readInt():
        try:
            num = int(input("Ingrese el número: "))
            return num
        except:
            print("Ingrese un número entero.")
            Utilidad.readInt()

