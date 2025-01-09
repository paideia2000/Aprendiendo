#Ejercicios extraidos de: (https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u42/)
class Cuenta():
    def __init__(self, titular):
        self.titular = titular
        self.cantidad = 0
        
    def atributos(self):#mostrar atributos
        print("El titular de la cuenta es: {}".format(self.titular))
        print("La cantidad de cash en su cuenta es: {}".format(self.cantidad))
        
    def ingresar_dinero(self):
        while True:
            try:           
                cant_ingresada = float(input("Añada dinero a su cuenta.: "))
                if cant_ingresada <= 0:
                    print("Error: Numero invalido. Tiene que ser una valor superior a ¡0!")
                else:
                    self.cantidad = self.cantidad + cant_ingresada
                    print("Igreso realizado correctamente. Se ha añadido {}$ a su cuenta, ahora tienes {}$.".format(cant_ingresada, self.cantidad))
                    break
            except ValueError:
                print("Error: No se permite ingresar textos. Por favor añade un valor numerico.")
                
    def retirar_dinero(self):
        while True:
            try:           
                cant_retirada = float(input("Ingrese la cantidad que desea retirar de su cuenta: "))
                if cant_retirada < self.cantidad:
                    self.cantidad -= cant_retirada
                    print("Has retirado {}$, te has quedado con {}$".format(cant_retirada, self.cantidad))
                elif cant_retirada == self.cantidad:
                    self.cantidad -= cant_retirada
                    print("Has retirado {}$ dinero, te has quedado con {}$".format(cant_retirada, self.cantidad))
                else:
                    self.cantidad -= cant_retirada
                    print("Has retirado {}$ dinero, te has quedado debiendonos {}$".format(cant_retirada, self.cantidad))
                break
            except ValueError:
                print("Error: No se permite ingresar valor de texto, pruebe con numeros positivos")

class CuentaJoven(Cuenta):#clase heredada de 'SuperClase(Cuenta)
    def __init__(self, titular, bonificacion):
        super().__init__(titular)
        self.cantidad = 0
        self.bonificacion = bonificacion
        
    def validar_titular(self, edad):
        if edad >= 18 and edad <= 25:
            return True
        else:
            return False
        
    def retirar_dinero(self, edad):
        while True:
                ask_extract_money =  input("Desea extraer dinero (SI/NO)?: ").lower().strip()   
                if ask_extract_money == "no":
                    print("Gracias por su visita, ¡Hasta luego!.")
                    break   
                elif ask_extract_money == "si":       
                    if edad == True:
                        extract_money = float(input("Amount you want to extract: "))
                        if extract_money <= 0:
                            print("Erorr: Por favor ingrese un numero valido.")
                            continue
                        elif extract_money <= self.cantidad:
                            self.cantidad -= extract_money
                            print(f"Has retirado {extract_money}$, ahora solo te queda {self.cantidad}")
                        else:
                            self.cantidad -= extract_money
                            print(f"Has retirado {extract_money}$ ahora te queda 0$, ademas te quedaras debiendo {self.cantidad}$")
                    else:
                        print("Erorr: You can't extract the money, because you're a minor or you're over 25 years old")
                        break
                else:
                    print("Error: Por favor ingrese una de las 2 opciones anteriores")

titular = Cuenta("Rene")#Intanciacion de la variable, a traves del objeto Cuenta de la clase            
titutar_joven = CuentaJoven("Ruben", "2%")#Intanciacion de la variable, a traves del objeto CuentaJoven de la clase 
