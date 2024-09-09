import datetime
from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# def mostrar_imagenes_redimensionadas(frame, rutas_imagenes, tamaño):
#     # Lista para almacenar las imágenes convertidas y redimensionadas
#     imagenes_tk = []

#     # Cargar y redimensionar las imágenes
#     for ruta in rutas_imagenes:
#         imagen = Image.open(ruta)
#         imagen_redimensionada = imagen.resize(tamaño)  # Redimensionar la imagen
#         imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
#         imagenes_tk.append(imagen_tk)

#     # Mostrar las imágenes en el frame
#     for img in imagenes_tk:
#         label = Label(frame, image=img)
#         label.image = img  # Para evitar que Python libere la imagen
#         label.pack(side="left", padx=5, pady=5)
contador_clicks_cv = 0


def cargar_imagen(ruta):
    try:
        return ImageTk.PhotoImage(Image.open(ruta))  # Cargar la imagen sin redimensionar
    except Exception as e:
        print(f"Error al cargar la imagen {ruta}: {e}")
        return None

# Función para cambiar las imágenes en los labels
def cambiar_imagen():
    global ruta_rb_b, ruta_rb_lt, ruta_rb_rt, contador_clicks_cv

    contador_clicks_cv = contador_clicks_cv % 3  # Mantener el contador dentro del rango de 0 a 2

    rutas = [
        ["src/Imagenes/desarrolladores/arangoPrueba1.png", "src/Imagenes/desarrolladores/arangoPrueba2.png", "src/Imagenes/desarrolladores/arangoPrueba3.png"],
        ["src/Imagenes/desarrolladores/coloradoPrueba1.png", "src/Imagenes/desarrolladores/coloradoPrueba2.png", "src/Imagenes/desarrolladores/coloradoPrueba3.png"],
        ["src/Imagenes/desarrolladores/stivenPrueba1.png", "src/Imagenes/desarrolladores/stivenPrueba2.png", "src/Imagenes/desarrolladores/stivenPrueba3.png"]
    ]

    # Actualizar las rutas de las imágenes
    ruta_rb_lt = rutas[contador_clicks_cv][0]
    ruta_rb_rt = rutas[contador_clicks_cv][1]
    ruta_rb_b = rutas[contador_clicks_cv][2]

    # Cargar las imágenes sin redimensionar
    img_lt = cargar_imagen(ruta_rb_lt)
    img_rt = cargar_imagen(ruta_rb_rt)
    img_b = cargar_imagen(ruta_rb_b)

    # Actualizar el contenido de los Labels
    if img_rt:
        frame_rb_rt.config(image=img_rt)
        frame_rb_rt.image = img_rt  # Mantener referencia a la imagen

    if img_lt:
        frame_rb_lt.config(image=img_lt)
        frame_rb_lt.image = img_lt  # Mantener referencia a la imagen

    if img_b:
        frame_rb_b.config(image=img_b)
        frame_rb_b.image = img_b  # Mantener referencia a la imagen

    # Incrementar el contador para la próxima vez
    contador_clicks_cv += 1
ruta_rb_lt = "src/Imagenes/desarrolladores/arangoPrueba1.png"
ruta_rb_rt = "src/Imagenes/desarrolladores/arangoPrueba2.png"
ruta_rb_b = "src/Imagenes/desarrolladores/arangoPrueba3.png"


def info_aplicacion():
    messagebox.showinfo(title="Información de la aplicación", message="Esta aplicación simula el funcionamiento de una cadena de restaurantes a través de distintas funcionalidades como la de reservar una mesa, ordenar comida, agregar sedes y organizar eventos.")

def salir_de_acoustic():
    menu_inicio()

def menu_inicio():
    ventana_acoustic.withdraw()
    ventana_inicio.deiconify()

hojas_de_vida = ["Juan José",  "Colorado", "Stiven"]



def menu_acoustic():
    ventana_inicio.withdraw()
    ventana_acoustic.deiconify()
    
#MENU INICIO
ventana_inicio = Tk()
ventana_inicio.title("Menú Inicio")
ventana_inicio.resizable(True, True)
ventana_inicio.geometry("500x700")
ventana_inicio.iconbitmap("src/Imagenes/Aa.ico") #src/Imagenes
frame_left = Frame(ventana_inicio, bg = "red", bd = 2, relief="solid", width=100)
frame_left.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)
frame_left.pack_propagate(False)

frame_right = Frame(ventana_inicio, bg = "blue", bd = 2, relief="solid", width=100)
frame_right.pack(side = RIGHT, fill = BOTH, expand = True, padx = 10, pady = 10)
frame_right.pack_propagate(False)

frame_left_top = Frame(frame_left, bg = "green", bd = 2, relief="solid")
frame_left_top.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)
mensajeCum = Label(frame_left_top, text="Bienvenidos sean al Restaurante Orientado a objetos", font=("Arial", 20), fg="#000", anchor="n")
mensajeCum.pack(fill = BOTH)

frame_left_bottom = Frame(frame_left, height=200, width=100, bg = "yellow", bd = 2, relief="solid")
frame_left_bottom.pack(side = BOTTOM, fill = BOTH, expand = True, padx = 10, pady = 10)
frame_left_bottom.pack_propagate(False)

frame_lb_top = Frame(frame_left_bottom, bg = "pink", bd = 2, relief="solid")
frame_lb_top.pack(side = TOP, fill = BOTH, expand = True)
frame_lb_bottom = Frame(frame_left_bottom, bg = "brown", bd = 2, relief="solid")
frame_lb_bottom.pack(side = BOTTOM, fill = BOTH, expand = True)

acoustic_button = Button(frame_lb_bottom, text="Iniciar procesos", font=("Arial", 20), fg="#000", anchor="n", command = lambda: menu_acoustic())   
acoustic_button.pack(expand=True, anchor='center')

frame_right_top = Frame(frame_right, bg = "purple", bd = 2, relief="solid")
frame_right_top.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

frame_right_bottom = Frame(frame_right, bg = "orange", bd = 2, relief="solid")
frame_right_bottom.pack(side = BOTTOM, fill = BOTH, expand = True, padx = 10, pady = 10)

frame_right_bottom.grid_rowconfigure(0, weight=1)
frame_right_bottom.grid_columnconfigure(0, weight=1)
frame_right_bottom.grid_rowconfigure(1, weight=1)
frame_right_bottom.grid_columnconfigure(1, weight=1)

frame_rb_lt = Frame(frame_right_bottom, bg = "pink", bd = 2, relief="solid")
frame_rb_lt.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
frame_rb_lt.pack_propagate(False)

frame_rb_rt = Frame(frame_right_bottom, bg = "brown", bd = 2, relief="solid")
frame_rb_rt.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
frame_rb_rt.pack_propagate(False)

frame_rb_b = Frame(frame_right_bottom, bd = 2, relief="solid")
frame_rb_b.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
frame_rb_b.pack_propagate(False)


# Imagen del recuadro superior izquiero del recuadro inferior derecho

imagen_rb_lt = PhotoImage(file = ruta_rb_lt)
frame_rb_lt_img = Label(frame_rb_lt, image = imagen_rb_lt)
frame_rb_lt_img.pack()

# Imagen del recuadro superior derecho del recuadro inferior derecho

imagen_rb_rt = PhotoImage(file = ruta_rb_rt)
frame_rb_rt_img = Label(frame_rb_rt, image = imagen_rb_rt)
frame_rb_rt_img.pack()

# Imagen del recuadro inferior del recuadro inferior derecho

imagen_rb_b = PhotoImage(file = ruta_rb_b)
frame_rb_b_img = Label(frame_rb_b, image = imagen_rb_b)
frame_rb_b_img.pack()



boton_right_top = Button(frame_right_top, bg = "white", text="Hoja de vida de los desarrolladores", font=("Arial",12), command=cambiar_imagen)
boton_right_top.pack(expand=True, fill = "both", padx=6, pady=6)

#MENU ACOUSTIC
ventana_acoustic = Tk()
ventana_acoustic.title("Menú Acoustic")
ventana_acoustic.resizable(True, True)
ventana_acoustic.geometry("500x700")
# ventana_acoustic.iconbitmap('./Imagenes/Aa.ico')

menu_bar = Menu(ventana_acoustic)
ventana_acoustic.config(menu = menu_bar)
menu_archivo = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Archivo", menu = menu_archivo)
menu_archivo.add_command(label = "Aplicación", command = info_aplicacion)
menu_archivo.add_separator()
menu_archivo.add_command(label = "Salir", command = salir_de_acoustic)
menu_procesos = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Procesos y Consultas", menu = menu_procesos)
menu_procesos.add_command(label = "Funcionalidad 1")
menu_procesos.add_separator()
menu_procesos.add_command(label = "Funcionalidad 2")
menu_procesos.add_separator()
menu_procesos.add_command(label = "Funcionalidad 3")
menu_procesos.add_separator()
menu_procesos.add_command(label = "Funcionalidad 4")
menu_procesos.add_separator()
menu_procesos.add_command(label = "Funcionalidad 5")
menu_ayuda = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label = "Ayuda", menu = menu_ayuda)
menu_ayuda.add_command(label = "Acerca de")

menu_inicio()

ventana_inicio.mainloop()