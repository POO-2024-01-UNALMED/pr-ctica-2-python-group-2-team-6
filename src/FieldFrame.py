from tkinter import *
from tkinter.ttk import Combobox as Cajacombo


class FieldFrame(Frame):

    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, tipo = 0):
        super().__init__(root, width=400, height=300, bg="white")
        self.root = root
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores if valores is not None else []
        self.entradas = []
        self.habilitado = habilitado
        self.tipo = tipo

        # Crear las etiquetas de criterios y valores
        self.criteriosLabel = Label(self, text=self.tituloCriterios, bg="white", font=("Arial", 11))
        self.criteriosLabel.grid(row=0, column=0, padx=10, pady=10)

        self.valoresLabel = Label(self, text=self.tituloValores, bg="white", font=("Arial", 11))
        self.valoresLabel.grid(row=0, column=1, padx=10, pady=10)

        if tipo == 0:
            # Crear las entradas de texto
            for i in range(len(self.criterios)):
                Label(self, text=self.criterios[i], bg="white", font=("Arial", 11)).grid(row=(i + 1), column=0, padx=10, pady=5)
                valor = Entry(self, width=40)
                valor.grid(row=(i + 1), column=1, padx=10, pady=5)
                if self.valores:
                    valor.insert(0, self.valores[i])
                self.entradas.append(valor)
                if self.habilitado is not None and not self.habilitado[i]:
                    valor.configure(state="disabled")

            # Crear botones
            self.crearBoton("Limpiar campos", self.limpiarEntradas, 1)
        if self.habilitado is None:
            self.crearBoton("Aceptar", self.aceptar, 0)
            pass

        elif tipo == 1: #Sí o No
            # Crear botones
            self.crearBoton("Sí", self.yessir, 0)
            self.crearBoton("No", self.abortarMision, 1)
            pass

        elif tipo == 2:
            # Crear las cajacombos
            for i in range(len(self.criterios)):
                Label(self, text=self.criterios[i], bg="white", font=("Arial", 11)).grid(row=(i + 1), column=0, padx=10, pady=5)
                self.valores[i].insert(0, "↓↓ Escoja una opción ↓↓")
                valor = Cajacombo(self, width=40, values=valores[i][1:])
                valor.grid(row=(i + 1), column=1, padx=10, pady=5)
                if self.valores:
                    valor.insert(0, self.valores[i][0])
                self.entradas.append(valor)
                if self.habilitado is not None and not self.habilitado[i]:
                    valor.configure(state="disabled")
            pass

    def crearBoton(self, texto, comando, columna):
        Button(self, text=texto, command=comando, font=("Arial", 11)).grid(row=(len(self.criterios) + 1), column=columna, padx=10, pady=10)

    def limpiarEntradas(self):
        for entrada in self.entradas:
            entrada.delete(0, END)

    def yessir(self):
        pass
        
    def abortarMision(self):
        pass

    def getValores(self):
        self.valores = [valor.get() for valor in self.entradas]

    def getValue(self, criterio):
        i = self.criterios.index(criterio)
        return self.entradas[i].get()

    def aceptar(self):
        self.getValores()
        print("Valores aceptados:", self.valores)

# Función para ejecutar la ventana principal
def main():
    root = Tk()
    root.title("FieldFrame Example")
    root.geometry("500x300")

    criterios = ["Nombre", "Apellido", "Edad", "Tamaño", "Educacion"]
    valores = [["Caja", "Combo", "Muy", "Mela", "Sí"], ["Cajita2"], ["Cajita3"], ["Cajita4"], ["Cajita5"]]
    habilitado = [True, True, True, True, True]

    # Crear el FieldFrame y agregarlo a la ventana
    frame = FieldFrame(root, tituloCriterios= "¿Desea", criterios= criterios, tituloValores = "continuar?", valores = valores, habilitado = habilitado, tipo = 2)
    frame.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()