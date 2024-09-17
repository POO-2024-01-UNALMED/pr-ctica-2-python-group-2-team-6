from tkinter import messagebox

class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def __str__(self):
        return f"Error en la aplicación: {self.mensaje}"
    
class ExcepcionCajaCombo(ErrorAplicacion):
    def __init__(self, mensaje_error_hijo):
        if mensaje_error_hijo is not None:
            self.mensaje_error_inicio = f"Ha ocurrido un error en el Cajacombo: {mensaje_error_hijo}"
        else:
            self.mensaje_error_inicio = "Ha ocurrido un error en el Cajacombo"
        super().__init__(self.mensaje_error_inicio)
    
    def __str__(self):
        return f"Error en la aplicación: {self.mensaje}"

class ExcepcionFueraRango(ExcepcionCajaCombo):
    def __init__(self, valor, rango):
        self.mensaje_error_valor = f"El valor {valor} está fuera del rango permitido: {rango}"
        messagebox.showerror("Error: Fuera de Rango", self.mensaje_error_valor)
        super().__init__(self.mensaje_error_valor)

class ExcepcionDatosErroneos(ExcepcionCajaCombo):
    def __init__(self, valores = []):
        self.mensaje_error_valor = f"El dato(s) ingresado(s) es incorrecto(s): {valores}"
        messagebox.showerror("Error: Datos Erróneos", self.mensaje_error_valor)
        super().__init__(self.mensaje_error_valor)
    

class ExcepcionSeleccionVacia(ExcepcionCajaCombo):
    def __init__(self, campos_vacios):
        self.mensaje_error = f"Los siguientes campos están vacíos: {campos_vacios}"
        messagebox.showerror("Error: Selección Vacía", self.mensaje_error)
        super().__init__(self.mensaje_error)
    
class ExcepcionDatosEntry(ErrorAplicacion):
    def __init__(self, mensaje_error_hijo):
        if mensaje_error_hijo is not None:
            self.mensaje_error_inicio = f"Ha ocurrido un error en el Entry: {mensaje_error_hijo}"
            messagebox.showerror("Error: Datos erróneos", self.mensaje_error_inicio)
        else:
            self.mensaje_error_inicio = "Ha ocurrido un error en el Entry"
        super().__init__(self.mensaje_error_inicio)
    
    def __str__(self):
        return f"Error en la aplicación: {self.mensaje}"

class ExcepcionCedulasRepetidas(ExcepcionDatosEntry):
    def __init__(self, cedula_repetida):
        self.mensaje_error = f"Hay cédulas de acompañantes repetidas: Cédula de número {cedula_repetida}"
        messagebox.showerror("Error: Selección Vacía", self.mensaje_error)
        super().__init__(self.mensaje_error)

class ExcepcionNombreInvalido(ExcepcionDatosEntry):
    def __init__(self, nombre_invalido):
        self.mensaje_error = f"El nombre ingresado es inválido: {nombre_invalido}"
        messagebox.showerror("Error: Nombre Inválido", self.mensaje_error)
        super().__init__(self.mensaje_error)

class ExcepcionPlacaVehiculoInvalida(ExcepcionDatosEntry):
    def __init__(self, placa_invalida):
        self.mensaje_error = f"La placa del vehículo es inválida: {placa_invalida}"
        messagebox.showerror("Error: Placa Inválida", self.mensaje_error)
        super().__init__(self.mensaje_error)