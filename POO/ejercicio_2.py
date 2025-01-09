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
                cant_ingresada = float(input("Añada dinero a su cuenta: "))
                if cant_ingresada <= 0:
                    print("Error: Debe de añadir numeros positivos o encima de 0")
                else:
                    self.cantidad = self.cantidad + cant_ingresada
                    print("Igreso realizado correctamente, se ha añadido {}$ a su cuenta, ahora tienes {}$".format(cant_ingresada, self.cantidad))
                    break
            except ValueError:
                print("Error: No se permite ingresar valor de texto, pruebe con numeros positivos")
                
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

cliente = Cuenta("Rene Medina")
cliente.atributos()