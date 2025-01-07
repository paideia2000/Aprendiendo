#list sample utilizada para un ejercicio
sample = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
diccionario = {}
# funsion para almacenar en 'diccionario' los valores repetidos de 'sample' y su cantidad de repeticiones
def crear_diccionario(sample):
    for numero in sample:
        if numero not in diccionario:
            diccionario[numero] = 1
        else:
            diccionario[numero] += 1
    return diccionario

print(crear_diccionario(sample))