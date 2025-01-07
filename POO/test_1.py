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
        return f"Ahora tu fuerza es: {self.fuerza}, tu inteligencia es: {self.inteligencia}, y tu defensa e: {self.defensa}"
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

class guerrero(Personaje):
        
    def __init__(self, nombre, vida, inteligencia, defensa, fuerza, espada):
        super().__init__(nombre, vida, inteligencia, defensa, fuerza)
        self.espada = espada
    def cambiar_arma(self):
        while True:    
            try:    
                elejir_arma = int(input("Presiona (1) para espada de fuergo y (2) para espada de hielo: "))
                if elejir_arma == 1:
                    self.espada = 8
                    print(f"Has cambiado a ¡Espada de fuego!, el daño es igual a {self.espada}")
                    break
                elif elejir_arma == 2:
                    self.espada = 10
                    print(f"Has cambiado a ¡Espada de hielo!, el daño es igual a {self.espada}")
                    break
                else:
                    print("Error:¡Arma no disponible!")
            except ValueError:
                print("Error: Debes elejir las armas por su valor en el inventario") 

supreme = Personaje("Supreme", 150, 50, 65, 40,)
horco = guerrero("Enemigo", 100, 30, 45, 20, 5)

horco.cambiar_arma()



