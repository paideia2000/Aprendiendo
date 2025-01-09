#Ejercicios extraidos de: (https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u42/)
class Persona():
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def get__nombre(self):
        return self.__nombre
    
    def get__edad(self):
        print(self.__edad)
    
    def get__dni(self):
        print(self.__dni)
        
    def mostrar(self):
        print("Su nombre es: {}".format(self.__nombre))
        print("Su edad es: {}".format(self.__edad)) 
        print("Su dni es: {}".format(self.__dni))
        
    def mayor_o_menor(self):
        if self.__edad < 18:
            print(f"{self.__nombre} tiene {self.__edad} años, por lo tanto es menor de edad")
        else:
            print(f"{self.__nombre} tiene {self.__edad} años, por lo tanto es mayor de edad")
            
    def set__nombre(self, otro_nombre):
        self.__nombre = otro_nombre
        return self.__nombre
        
    def set__edad(self, otra_edad):
        self.__edad = otra_edad
        return self.__edad
    
    def set__dni(self, otro_dni):
        self.__dni = otro_dni
        return self.__dni
        
persoan1 = Persona("Rene", 24, "07294960G")
persoan1.mostrar()

print("\nSe ha modificado el nombre a: {}".format(persoan1.set__nombre("Ruben")))
print("Se ha modificado la edad a: {}".format(persoan1.set__edad(24)))
print("Se ha modificado el dni a: {}".format(persoan1.set__dni("07295960G")))
