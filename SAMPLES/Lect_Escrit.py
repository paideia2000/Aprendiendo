print("LECTURA Y ESCRITURA DE ARCHIVOS")

#Muestra por consola lo que contiene un archivo.

archivo = open("ejercicio_1.py", "r")
contenido_del_archivo = archivo.read()
print(contenido_del_archivo)
archivo.close()


#Crea un archivo y escribe dentro
archivo = open("prueba.py", "w")# la (W) indica que abriremos el archivo si existe en modo escritura y sino existe se creara uno con el nombre "prueba.py"
archivo.write("Hola Mundo")#se utiliza el metodo write para escribir un texto dentro del archivo
archivo.close