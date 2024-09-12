from tkinter import *
from tkinter.ttk import Combobox as Cajacombo
from uiMain.errorAplicacion import ExcepcionSeleccionVacia

class FieldFrame(Frame):
    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, tipo=0, comandoContinuar=None, comandoCancelar=None):
        super().__init__(root, width=400, height=300, bg="white")
        self.root = root
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios if criterios is not None else []
        self.tituloValores = tituloValores
        self.valores = valores if valores is not None else []
        self.entradas = []
        self.habilitado = habilitado
        self.tipo = tipo
        self.comandoContinuar = comandoContinuar
        self.comandoCancelar = comandoCancelar

        # Guardar los widgets originales para poder restaurarlos
        self.original_widgets = []  # Para almacenar widgets
        self.widget_positions = []  # Para almacenar sus posiciones (row, column)

        # Crear las etiquetas de criterios y valores
        self.criteriosLabel = Label(self, text=self.tituloCriterios, bg="white", font=("Arial", 11))
        self.criteriosLabel.grid(row=0, column=0, padx=10, pady=10)
        self.valoresLabel = Label(self, text=self.tituloValores, bg="white", font=("Arial", 11))
        self.valoresLabel.grid(row=0, column=1, padx=10, pady=10)

        # Guardar los widgets originales
        self.save_original_widget(self.criteriosLabel, 0, 0)
        self.save_original_widget(self.valoresLabel, 0, 1)

        if tipo == 0:  # El usuario escribe
            # Crear las entradas de texto
            for i in range(len(self.criterios)):
                criterio_label = Label(self, text=self.criterios[i], bg="white", font=("Arial", 11))
                criterio_label.grid(row=(i + 1), column=0, padx=10, pady=5)
                valor = Entry(self, width=40)
                valor.grid(row=(i + 1), column=1, padx=10, pady=5)
                if self.valores:
                    valor.insert(0, self.valores[i])
                self.entradas.append(valor)
                if self.habilitado is not None and not self.habilitado[i]:
                    valor.configure(state="disabled")

                # Guardar los widgets originales
                self.save_original_widget(criterio_label, i + 1, 0)
                self.save_original_widget(valor, i + 1, 1)

            # Crear botones
            self.crearBoton("Limpiar campos", self.limpiarEntradas, 1)
            if self.habilitado is None:
                self.crearBoton("Aceptar", self.aceptar, 0)

        elif tipo == 1:  # El usuario elige Sí o No
            # Crear botones
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
                    valor.configure(state="readonly")
                
                self.crearBoton("Aceptar", self.aceptar, 1)

        elif tipo == 3:
            print("Tipo 3")
            Label(self, text = criterios[0]).grid(row=1, column=0, columnspan=2)

    def save_original_widget(self, widget, row, column):
        """Guardar el widget y su posición"""
        self.original_widgets.append(widget)
        self.widget_positions.append((row, column))

    def crearBoton(self, texto, comando, columna):
        Button(self, text=texto, command=comando, font=("Arial", 11)).grid(row=(len(self.criterios) + 1), column=columna, padx=10, pady=10)

    def limpiarEntradas(self):
        for entrada in self.entradas:
            entrada.delete(0, END)

    def on_select(self, event):
        combobox = event.widget
        if combobox.get() == "↓↓ Escoja una opción ↓↓":
            combobox.set("")

    def yessir(self):
        self.valores = [1]
        self.comandoContinuar()
        
    def abortarMision(self):
        self.valores = [2]
        self.comandoCancelar()

    def restore_original_widgets(self):
        """Volver a mostrar los widgets originales en sus posiciones originales"""
        for widget, pos in zip(self.original_widgets, self.widget_positions):
            widget.grid(row=pos[0], column=pos[1])

    def getValores(self):
        self.valores = [valor.get() for valor in self.entradas]

    def getValue(self, criterio):
        i = self.criterios.index(criterio)
        return self.entradas[i].get()

    def aceptar(self):
        self.getValores()
        if '↓↓ Escoja una opción ↓↓' in self.valores:
            campos_vacios = []
            for ocurrencia in self.valores:
                if ocurrencia == '↓↓ Escoja una opción ↓↓':
                    campos_vacios.append(self.criterios[self.valores.index(ocurrencia)])
            raise(ExcepcionSeleccionVacia(campos_vacios))
        else:
            print("Valores aceptados:", self.valores)

# Función para ejecutar la ventana principal
def main():
    root = Tk()
    root.title("FieldFrame Example")
    root.geometry("500x300")

    criterios = ["Nombre"]
    valores = [["Caja"]]
    habilitado = [True]

    # Crear el FieldFrame y agregarlo a la ventana
    frame = FieldFrame(root, tituloCriterios= "¿Desea", criterios= criterios, tituloValores = "continuar?", valores = valores, habilitado = habilitado, tipo = 2)
    frame.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
