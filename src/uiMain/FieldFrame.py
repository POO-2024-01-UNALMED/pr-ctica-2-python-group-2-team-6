from tkinter import *
from tkinter.ttk import Style
from tkinter.ttk import Combobox as Cajacombo
from uiMain.errorAplicacion import ExcepcionSeleccionVacia

class FieldFrame(Frame):
    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, tipo=0, comandoContinuar=None, comandoCancelar=None, comandoOpcion3=None, comandoOpcion4 = None, argComando = None):
        super().__init__(root, width=400, height=300, bg = "#545454")
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
        self.comandoOpcion3 = comandoOpcion3
        self.comandoOpcion4 = comandoOpcion4
        self.argComando = argComando

        # Configurar el grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(10, weight=1)
        self.grid_rowconfigure(11, weight=1)
        self.grid_rowconfigure(12, weight=1)
        self.grid_rowconfigure(13, weight=1)
        self.grid_rowconfigure(14, weight=1)
        self.grid_rowconfigure(15, weight=1)

        # Guardar los widgets originales para poder restaurarlos
        self.original_widgets = []  # Para almacenar widgets
        self.widget_positions = []  # Para almacenar sus posiciones (row, column)

        # Crear las etiquetas de criterios y valores
        self.criteriosLabel = Label(self, text=self.tituloCriterios, font=("Arial", 20, "bold"), bg = "#545454", fg="#fff")
        self.criteriosLabel.grid(row=0, column=0, padx=10, pady=10)
        self.valoresLabel = Label(self, text=self.tituloValores, font=("Arial", 20, "bold"), bg = "#545454", fg="#fff")
        self.valoresLabel.grid(row=0, column=1, padx=10, pady=10)

        # Guardar los widgets originales
        self.save_original_widget(self.criteriosLabel, 0, 0)
        self.save_original_widget(self.valoresLabel, 0, 1)

        if tipo == 0:  # El usuario escribe
            # Crear las entradas de texto

            for i in range(len(self.criterios)):
                criterio_label = Label(self, text=self.criterios[i], font=("Arial", 15), bg = "#545454", fg="#fff")
                criterio_label.grid(row=(i + 1), column=0, padx=0, pady=0)
                valor = Entry(self, width=30, font=("Arial", 15))
                valor.grid(row=(i + 1), column=1, padx=10, pady=5)
                if self.valores:
                    valor.insert(0, self.valores[i])
                self.entradas.append(valor)
                if self.habilitado is not None and not self.habilitado[i]:
                    valor.configure(state="disabled")

            # Crear botones
            self.crearBoton("Limpiar campos", self.limpiarEntradas, 0)
            # if self.habilitado is None:
            self.crearBoton("Aceptar", self.aceptar, 1)

        elif tipo == 1:  # El usuario elige Sí o No
            self.valoresLabel.destroy()

            self.criteriosLabel.config(text=self.tituloCriterios + " " + self.tituloValores, font=("Arial", 20), bg = "#545454", fg="#fff")
            self.criteriosLabel.grid(columnspan=2)
            # Crear botones
            self.crearBoton("Sí", self.yessir, 0)
            self.crearBoton("No", self.abortarMision, 1)

        elif tipo == 2: # Cajacombos
            for i in range(len(self.criterios)):
                Label(self, text=self.criterios[i], font=("Arial", 15), bg = "#545454", fg="#fff").grid(row=(i + 1), column=0, padx=10, pady=5)
                valor = Cajacombo(self, width=40, values=self.valores[i])
                valor.grid(row=(i + 1), column=1, padx=10, pady=5)
                # Valor predeterminado no editable
                valor.set("↓↓ Escoja una opción ↓↓")
                valor.bind("<<ComboboxSelected>>", self.on_select)  # Bind event to update default value
                self.entradas.append(valor)
                if self.habilitado is not None and not self.habilitado[i]:
                    valor.set(self.valores[i])
                    valor.configure(state="readonly")  # Cambiar a normal si habilitado es False
                else:
                    valor.configure(state="readonly")
                
                self.crearBoton("Aceptar", self.aceptar, 0, 2)

        elif tipo == 3: #Mensaje
            self.valoresLabel.destroy()

            self.criteriosLabel.config(text=self.tituloCriterios, font=("Arial", 20), bg = "#545454", fg="#fff")
            self.criteriosLabel.grid(columnspan=2)

            label_mensaje = Label(self, text = criterios[0], font=("Arial", 15), bg = "#545454", fg="#fff")
            label_mensaje.grid(row=1, column=0, columnspan=2)

            if comandoContinuar != None:
                self.crearBoton("Aceptar", self.yessir, 0, 2)
        
        elif tipo == 4:  # Tres botones
            for i in range(len(self.criterios)):
                Label(self, text=self.criterios[i], font=("Arial", 15), bg="#545454", fg="#fff").grid(row=(i + 1), column=0, padx=10, pady=5, sticky="w")

            # Agregar los botones en una fila (row) con la misma llamada a crearBoton
            self.crearBoton("Cumpleaños", self.comandoContinuar, columna=0)  # Primer botón
            self.crearBoton("Meetings Empresariales", self.comandoCancelar, columna=1)  # Segundo botón
            self.crearBoton("Gastronomias Mundiales", self.comandoOpcion3, columna=2)  # Tercer botón
            self.crearBoton("No, deseo salir", self.comandoOpcion4, columna=3)  # Cuarto botón

            # Configurar el grid para que los botones se distribuyan simétricamente
            for i in range(4):  # Ajustar el tamaño de las columnas
                self.grid_columnconfigure(i, weight=1)

            # Configuración adicional para espaciado simétrico y distribución uniforme de botones
            self.grid_rowconfigure(len(self.criterios) + 1, weight=1)

        elif tipo == 5:  # Tres botones
            for i in range(len(self.criterios)):
                Label(self, text=self.criterios[i], font=("Arial", 15), bg="#545454", fg="#fff").grid(row=(i + 1), column=0, padx=10, pady=5, sticky="w")

            # Agregar los botones en una fila (row) con la misma llamada a crearBoton
            self.crearBoton("Vinos", self.comandoContinuar, columna=0)  # Primer botón
            self.crearBoton("Champañas", self.comandoCancelar, columna=1)  # Segundo botón

            # Configurar el grid para que los botones se distribuyan simétricamente
            for i in range(2):  # Ajustar el tamaño de las columnas
                self.grid_columnconfigure(i, weight=1)

            # Configuración adicional para espaciado simétrico y distribución uniforme de botones
            self.grid_rowconfigure(len(self.criterios) + 1, weight=1)


            if self.comandoContinuar is not None:
                self.crearBoton("Aceptar", self.yessir, 0)

    def save_original_widget(self, widget, row, column):
        """Guardar el widget y su posición"""
        self.original_widgets.append(widget)
        self.widget_positions.append((row, column))

    def crearBoton(self, texto, comando, columna, spancolumna = 1):
        boton = Button(self, text = texto, command = comando, font = ("Arial", 15), bg="#434343", fg="#fff")
        boton.grid(row = (len(self.criterios) + 1), column = columna, columnspan = spancolumna, padx = 10, pady = 10)

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
        print("Valores aceptados:", self.valores)
        
    def abortarMision(self):
        self.valores = [2]
        if self.comandoCancelar != None:
            if self.argComando != None:
                self.comandoCancelar(self.argComando)
            else:
                self.comandoCancelar()
        print("Valores aceptados:", self.valores)

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
            indice = 0
            for ocurrencia in self.valores:
                if ocurrencia == '↓↓ Escoja una opción ↓↓':
                    campos_vacios.append(self.criterios[indice])
                indice += 1
            raise(ExcepcionSeleccionVacia(campos_vacios))
        else:
            self.comandoContinuar()
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
    frame = FieldFrame(root, tituloCriterios= "¿Desea", criterios= criterios, tituloValores = "continuar?", valores = valores, habilitado = habilitado, tipo = 0)
    frame.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
