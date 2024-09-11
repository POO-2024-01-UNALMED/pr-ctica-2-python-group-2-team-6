from tkinter import *
from tkinter.ttk import Combobox as Cajacombo

class FieldFrame(Frame):

    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, tipo=0):
        super().__init__(root, width=400, height=300, bg="white")
        self.root = root
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios if criterios is not None else []
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

        if tipo == 1:  # El usuario elige Sí o No
            # Crear botones para Sí y No
            self.crearBoton("Sí", self.yessir, 0)
            self.crearBoton("No", self.abortarMision, 1)

    def crearBoton(self, texto, comando, columna):
        Button(self, text=texto, command=comando, font=("Arial", 11)).grid(row=(len(self.criterios) + 1), column=columna, padx=10, pady=10)

    def yessir(self):
        self.valores = ["Sí"]
        print("Has seleccionado: Sí")
        # Aquí podrías continuar con más lógica si elige "Sí"

    def abortarMision(self):
        self.valores = ["No"]
        print("Has seleccionado: No")
        self.destroy()
        # Restaurar el frame anterior
        reservarMesaAnterior()

    def getValue(self, criterio):
        return self.valores[0] if self.valores else None

def reservarMesaAnterior():
    global frame_procesos_bottom

    # Aquí puedes restaurar el contenido anterior del frame_procesos_bottom
    Label(frame_procesos_bottom, text="Bienvenido de nuevo al frame anterior", font=("Arial", 14)).pack(padx=20, pady=20)

def reservarMesa():
    global label_procesos_bottom

    # Si ya existe un label_procesos_bottom, lo destruimos
    if label_procesos_bottom:
        label_procesos_bottom.destroy()

    # Crear un nuevo FieldFrame
    label_procesos_bottom = FieldFrame(
        frame_procesos_bottom,
        tituloCriterios="¿Desea",
        criterios=["Opción"],
        tituloValores="continuar?",
        tipo=1  # Usamos tipo 1 para botones Sí o No
    )
    label_procesos_bottom.pack(padx=20, pady=20)

    # Añadir un botón para confirmar la elección
    Button(frame_procesos_bottom, text="Confirmar", command=confirmarEleccion).pack(pady=10)

def confirmarEleccion():
    eleccion = label_procesos_bottom.getValue("Opción")  # Obtener valor de la opción seleccionada
    if eleccion == "Sí":
        print("Has confirmado que deseas continuar.")
        # Lógica adicional si elige "Sí"
    elif eleccion == "No":
        print("Has cancelado la operación.")
        # Lógica adicional si elige "No"

# Ejemplo de cómo instanciar todo
def main():
    global frame_procesos_bottom, label_procesos_bottom
    root = Tk()
    root.title("Reserva de Mesa")
    root.geometry("600x400")

    frame_procesos_bottom = Frame(root)
    frame_procesos_bottom.pack(expand=True, fill="both")

    # Inicialmente sin ningún FieldFrame creado
    label_procesos_bottom = None

    # Iniciar la función reservarMesa
    reservarMesa()

    root.mainloop()

if __name__ == "__main__":
    main()

