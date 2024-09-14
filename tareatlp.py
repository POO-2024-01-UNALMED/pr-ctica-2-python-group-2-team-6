import array

# Diccionario de especies con nombre, tipo, cantidad observada y hábitat
biodiversidad = {
    "Águila Real": ("animal", 5, "montañas"),
    "Roble": ("planta", 20, "bosques"),
}

# Función para actualizar la cantidad observada de una especie
def actualizar_cantidad(biodiversidad, especie, nueva_cantidad, resultado=None):
    if resultado is None:
        resultado = {}
    if not biodiversidad:
        return resultado
    especie_actual, info = list(biodiversidad.items())[0]
    nueva_info = (info[0], nueva_cantidad if especie_actual == especie else info[1], info[2])
    resultado[especie_actual] = nueva_info
    return actualizar_cantidad(dict(list(biodiversidad.items())[1:]), especie, nueva_cantidad, resultado)

# Función para cambiar el hábitat de una especie
def cambiar_habitat(biodiversidad, especie, nuevo_habitat, resultado=None):
    if resultado is None:
        resultado = {}
    if not biodiversidad:
        return resultado
    especie_actual, info = list(biodiversidad.items())[0]
    nueva_info = (info[0], info[1], nuevo_habitat if especie_actual == especie else info[2])
    resultado[especie_actual] = nueva_info
    return cambiar_habitat(dict(list(biodiversidad.items())[1:]), especie, nuevo_habitat, resultado)

# Función para listar especies por tipo
def listar_especies_por_tipo(biodiversidad, tipo_buscado, resultado=None):
    if resultado is None:
        resultado = []
    if not biodiversidad:
        return resultado
    especie_actual, info = list(biodiversidad.items())[0]
    if info[0] == tipo_buscado:
        resultado.append(especie_actual)
    return listar_especies_por_tipo(dict(list(biodiversidad.items())[1:]), tipo_buscado, resultado)

# Función para calcular el total de individuos observados
def calcular_total_individuos(biodiversidad):
    if not biodiversidad:
        return 0
    especie_actual, info = list(biodiversidad.items())[0]
    return info[1] + calcular_total_individuos(dict(list(biodiversidad.items())[1:]))

# Función para calcular el promedio de individuos observados usando arreglos
def promedio_individuos(cantidades, index=0, suma=0):
    if index == len(cantidades):
        return suma / len(cantidades) if len(cantidades) > 0 else 0
    return promedio_individuos(cantidades, index + 1, suma + cantidades[index])

# Imprimir el diccionario original
print("Diccionario original:", biodiversidad)

# Actualizar la cantidad de una especie 
nueva_biodiversidad = actualizar_cantidad(biodiversidad, "Águila Real", 7)
print("Diccionario tras actualizar cantidad:", nueva_biodiversidad)

# Cambiar el hábitat de una especie 
nueva_biodiversidad = cambiar_habitat(nueva_biodiversidad, "Pino", "montañas")
print("Diccionario tras cambiar hábitat:", nueva_biodiversidad)

# Listar especies animal
animales = listar_especies_por_tipo(nueva_biodiversidad, "animal")
print("Especies de tipo animal:", animales)

# Listar especies planta
plantas = listar_especies_por_tipo(nueva_biodiversidad, "planta")
print("Especies de tipo planta:", plantas)

# Calcular el total de individuos observados 
total_individuos = calcular_total_individuos(nueva_biodiversidad)
print("Total de individuos observados:", total_individuos)

# Calcular la cantidad promedio de individuos observados 
cantidades = array.array('i', map(lambda v: v[1], nueva_biodiversidad.values()))
promedio = promedio_individuos(cantidades)
print("Cantidad promedio de individuos observados:", promedio)