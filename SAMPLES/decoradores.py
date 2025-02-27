#Ejercicios extraidos de: (https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u42/)
class Persona():
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    @property#decorador para conseguir nombre, convierte la funsion en un atributo
    def nombre(self):
        print(self.__nombre)
    
    def get__edad(self):
        print(self.__edad)
    
    def get__dni(self):
        print(self.__dni)
    #se usa la funsion magica __str__ para un metodo que realice una impresion por pantalla    
    def __str__(self):
        return f"Su nombre es: {self.__nombre}\nSu edad es: {self.__edad}\nSu dni es: {self.__dni}"
        
    def mayor_o_menor(self):
        if self.__edad < 18:
            print(f"{self.__nombre} tiene {self.__edad} años, por lo tanto es menor de edad")
        else:
            print(f"{self.__nombre} tiene {self.__edad} años, por lo tanto es mayor de edad")
            
    
    @nombre.setter#decorador, para editar nombre, cobvierte la funsion en un atributo
    def nombre(self, nombre):
        self.__nombre = nombre
        print(self.__nombre)
    
    def set__edad(self, otra_edad):
        self.__edad = otra_edad
        return self.__edad
    
    def set__dni(self, otro_dni):
        self.__dni = otro_dni
        return self.__dni
        
persoan1 = Persona("Rene", 24, "07294960G")
print(str(persoan1))




#print("\nSe ha modificado el nombre a: {}".format(persoan1.set__nombre("Ruben")))
#print("Se ha modificado la edad a: {}".format(persoan1.set__edad(24)))
#print("Se ha modificado el dni a: {}".format(persoan1.set__dni("07295960G")))
