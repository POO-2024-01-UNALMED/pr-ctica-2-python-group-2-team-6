from tkinter import *
from tkinter.ttk import Combobox as Cajacombo

class FieldFrame(Frame):

    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, tipo=0):
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
                    valor.configure(state="normal")
                else:
                    valor.configure(state="readonly")  # Cambiado a solo lectura

            # Crear botón "Limpiar campos"
            self.crearBoton("Limpiar campos", self.limpiarEntradas, 1)
            # Crear botón "Aceptar" si habilitado es None
            if self.habilitado is None:
                self.crearBoton("Aceptar", self.aceptar, 0)

        elif tipo == 1: # Botones Sí o No
            self.crearBoton("Sí", self.yessir, 0)
            self.crearBoton("No", self.abortarMision, 1)

        elif tipo == 2: # Cajacombos
            for i in range(len(self.criterios)):
                Label(self, text=self.criterios[i], bg="white", font=("Arial", 11)).grid(row=(i + 1), column=0, padx=10, pady=5)
                valor = Cajacombo(self, width=40, values=self.valores[i])
                valor.grid(row=(i + 1), column=1, padx=10, pady=5)
                # Valor predeterminado no editable
                valor.set("↓↓ Escoja una opción ↓↓")
                valor.bind("<<ComboboxSelected>>", self.on_select)  # Bind event to update default value
                self.entradas.append(valor)
                if self.habilitado is not None and not self.habilitado[i]:
                    valor.configure(state="normal")  # Cambiar a normal si habilitado es False
                else:
                    valor.configure(state="readonly")  # Cambiado a solo lectura

    def crearBoton(self, texto, comando, columna):
        Button(self, text=texto, command=comando, font=("Arial", 11)).grid(row=(len(self.criterios) + 1), column=columna, padx=10, pady=10)

    def limpiarEntradas(self):
        for entrada in self.entradas:
            if isinstance(entrada, Entry):
                entrada.delete(0, END)
            elif isinstance(entrada, Cajacombo):
                entrada.set("↓↓ Escoja una opción ↓↓")  # Reset default text

    def on_select(self, event):
        combobox = event.widget
        if combobox.get() == "↓↓ Escoja una opción ↓↓":
            combobox.set("")  # Clear the default text if a valid selection is made

    def yessir(self):
        print("Sí seleccionado")
        
    def abortarMision(self):
        print("No seleccionado")

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
    root.geometry("500x300")

    criterios = ["Nombre", "Apellido", "Edad", "Tamaño", "Educacion"]
    valores = [["Caja", "Combo", "Muy", "Mela", "Sí"], ["Cajita2"], ["Cajita3"], ["Cajita4"], ["Cajita5"]]
    habilitado = [True, True, True, True, True]

    # Crear el FieldFrame y agregarlo a la ventana
    frame = FieldFrame(root, tituloCriterios="¿Desea", criterios=criterios, tituloValores="continuar?", valores=valores, habilitado=habilitado, tipo=2)
    frame.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()