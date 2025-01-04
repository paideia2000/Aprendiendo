#Empezando con POO
class Personaje:
#Inicializando la clase
    def __init__(self, nombre, vida, inteligencia, defensa, fuerza):
    #Atributos de la clase
        self.nombre = nombre
        self.vida = vida
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.fuerza = fuerza
#Mostrar los atributos de la clase        
    def atributos(self):
        print("Nombre: ", self.nombre, sep="")
        print("Vida:", self.vida)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Fuerza:", self.fuerza)
#Agregarles valores a los atributos de la clase, a traves del metodo subir_nivel        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
#Metodo que indica si el personaje esta vivo o mmuerto
    def vivo_muerto(self):
        if self.vida > 0:
            return "Aun vive"
        else:
            self.vida = 0
            return "Ha muerto"
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha atacado a", enemigo.nombre)
        print("El enemigo ha recicbido", daño, "de daño")
        print(enemigo.vivo_muerto())
    


#Objetos de la clase Personaje
#mi_personaje = Personaje("Renesongo", 100, 50, 30, 20)
#mi_enemigo = Personaje("Enemigo", 100, 40, 15, 10)  


class guerrero(Personaje):
    
    def __init__(self, nombre, vida, inteligencia, defensa, fuerza, espada):
        super().__init__(nombre, vida, inteligencia, defensa, fuerza)
        self.espada = espada
        
    def cambiar_arma(self):
        elejir_arma = int(input("Presiona (1) para espada de fuergo y (2) para espada de hielo: "))
        if elejir_arma == 1:
            self.espada = 8
        elif elejir_arma == 2:
            self.espada = 10
        else:
            print("Error:¡Arma no disponible!")
        

supreme = guerrero("Supreme", 100, 30, 45, 20, 5)

print(supreme.cambiar_arma())