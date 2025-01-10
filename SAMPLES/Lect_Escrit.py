print("LECTURA Y ESCRITURA DE ARCHIVOS")

#Muestra por consola lo que contiene un archivo.

archivo = open("ejercicio_1.py", "r")# la "R" indica que abriremos el archivo si existe en modo escritura 
contenido_del_archivo = archivo.read()# utilizamos el metodo read para mostrar el contenido del archivo por consola
print(contenido_del_archivo)
archivo.close()


#Crea un archivo y escribe dentro
archivo = open("prueba.py", "w")# la (W) indica que abriremos el archivo si existe en modo escritura y sino existe se creara uno con el nombre "prueba.py"
archivo.write("Hola Mundo")#se utiliza el metodo write para escribir un texto dentro del archivo
archivo.close