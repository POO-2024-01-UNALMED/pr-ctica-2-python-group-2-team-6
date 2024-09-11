from tkinter import *

class FieldFrame(Frame):

    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, tipo = 1):
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

    def crearBoton(self, texto, comando, col):
        Button(self, text=texto, command=comando, font=("Arial", 11)).grid(row=(len(self.criterios) + 1), column=col, padx=10, pady=10)

    def limpiarEntradas(self):
        for entrada in self.entradas:
            entrada.delete(0, END)

    def getValores(self):
        self.valores = [valor.get() for valor in self.entradas]

    def getValue(self, criterio):
        i = self.criterios.index(criterio)
        return self.entradas[i].get()

    def aceptar(self):
        self.getValores()
        print("Valores aceptados:", self.valores)


def main():
    root = Tk()
    root.title("FieldFrame Example")
    root.geometry("500x400")

    criterios = ["Nombre", "Apellido", "Edad", "Tamaño", "Educacion"]
    valores = ["Pekín del Norte", "", "", "", ""]
    habilitado = [False, True, True, True, True]

    # Crear el FieldFrame y agregarlo a la ventana
    frame = FieldFrame(root, tituloCriterios="Componentes", criterios=criterios, tituloValores="Valores", valores=valores, habilitado=habilitado)
    frame.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
