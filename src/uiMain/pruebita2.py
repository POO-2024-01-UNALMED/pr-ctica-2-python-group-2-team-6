
from tkinter import *
from PIL import Image, ImageTk

contador_clicks_cv = 0

# Función para cambiar la imagen cuando el ratón pasa por encima
def cambiar_imagen_hover(event):
    global contador_clicks_cv

    # Listas de rutas de imágenes
    rutas = [
        ["src/Imagenes/desarrolladores/arangoPrueba1.png", "src/Imagenes/desarrolladores/arangoPrueba2.png", "src/Imagenes/desarrolladores/arangoPrueba3.png"],
        ["src/Imagenes/desarrolladores/coloradoPrueba1.png", "src/Imagenes/desarrolladores/coloradoPrueba2.png", "src/Imagenes/desarrolladores/coloradoPrueba3.png"],
        ["src/Imagenes/desarrolladores/stivenPrueba1.png", "src/Imagenes/desarrolladores/stivenPrueba2.png", "src/Imagenes/desarrolladores/stivenPrueba3.png"]
    ]

    # Actualizar las rutas de las imágenes de acuerdo al contador de clics
    ruta_rb_lt = rutas[contador_clicks_cv][0]
    
    # Cargar y redimensionar la imagen
    img_lt = Image.open(ruta_rb_lt).resize((150, 150))

    # Convertir la imagen a PhotoImage
    photo_lt = ImageTk.PhotoImage(img_lt)

    # Actualizar la imagen en el label
    frame_rb_lt_img.config(image=photo_lt)
    frame_rb_lt_img.image = photo_lt

    # Incrementar el contador para la próxima rotación
    contador_clicks_cv = (contador_clicks_cv + 1) % len(rutas)

# Inicializar la ventana principal
ventana_inicio = Tk()
ventana_inicio.title("Menú Inicio")
ventana_inicio.geometry("500x700")

# Frame para la imagen
frame_right_bottom = Frame(ventana_inicio, bg="orange", bd=2, relief="solid")
frame_right_bottom.pack(side=BOTTOM, fill=BOTH, expand=True, padx=10, pady=10)

frame_rb_lt = Frame(frame_right_bottom, bg="pink", bd=2, relief="solid")
frame_rb_lt.pack(pady=20)

# Inicializar el label para la imagen
frame_rb_lt_img = Label(frame_rb_lt)
frame_rb_lt_img.pack()

# Asignar los eventos de ratón al label
frame_rb_lt_img.bind("<Enter>", cambiar_imagen_hover)  # Cambiar imagen al entrar
frame_rb_lt_img.bind("<Leave>", cambiar_imagen_hover)  # Cambiar imagen al salir

# Ejecutar la ventana
ventana_inicio.mainloop()