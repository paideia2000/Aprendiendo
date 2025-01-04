#Empezando con POO
class Personaje:
#Inicializando la clase
    def __init__(self, nombre, vida, inteligencia, defensa, fuerza):
    #Atributos de la clase
        self.__nombre = nombre
        self.__vida = vida
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__fuerza = fuerza
        self.__aguante = fuerza + defensa
#Mostrar los atributos de la clase        
    def atributos(self):
        print("Nombre: ", self.__nombre, sep="")
        print("Vida:", self.__vida)
        print("Inteligencia:", self.__inteligencia)
        print("Defensa:", self.__defensa)
        print("Fuerza:", self.__fuerza)
#Agregarles valores a los atributos de la clase, a traves del metodo subir_nivel        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa
#Metodo que indica si el personaje esta vivo o mmuerto
    def __vivo_muerto(self):
        if self.__vida > 0:
            return "Aun vive"
        else:
            self.__vida = 0
            return "Ha muerto"
        
    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida -= daño
        print(self.__nombre, "ha atacado a", enemigo.__nombre)
        print("El enemigo ha recicbido", daño, "de daño")
        print(enemigo.__vivo_muerto())
    
    #metodo (getter) que devuelve el valor del atributo encapsulado
    def get__inteligencia(self):
        return self.__inteligencia
    #metodo (setter) que modifica el valor del atributo encapsulado
    def set__fuerza(self, fuerza):
        if fuerza < 0:
            print("Error: No se puede tener una fuerza negativa")
        else:
            self.__fuerza = fuerza

#Objetos de la clase Personaje
mi_personaje = Personaje("Renesongo", 100, 50, 30, 20)
mi_enemigo = Personaje("Enemigo", 100, 40, 15, 10)  


#Aunque los metodos y atributos esten encapsulados, se pueden acceder a ellos como se muestra a continuacion (no es recomendable)
#print(mi_personaje._Personaje__vivo_muerto())

print(mi_personaje.get__inteligencia())