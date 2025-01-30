#biblioteca
from abc import ABC, abstractmethod
        
class Usuario(ABC):
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.libros_reservados = []
        self.libros_devueltos = []
    
    @abstractmethod
    def mostrar_atributos(self):
        pass

class Adquirir_prestado(Usuario):
    def __init__(self,nombre, email):
        super().__init__(nombre, email)
    
    def mostrar_atributos(self):
        print(f"Su nombre de usuario es: {self.nombre} y su email es: {self.email}")
        
    def adquirir_prestado(self, libro, prestar):
        if prestar.prestar_libro(libro):
            self.libros_reservados.append(libro)
            print(F"El libro:'{libro}', ha sido prestado ha:'{self.nombre}'. Su email es:'{self.email}'")
        else:
            print(f"El libro: {libro} no lo tenemos en la estanteria, lo sentimos.")

class Devolver_libro(Usuario):
    def __init__(self,nombre, email):
        super().__init__(nombre, email)
        
    def mostrar_atributos(self):
        print(f"Su nombre de usuario es: {self.nombre} y su email es: {self.email}")
    
    def devolver_libro(self, libro):
        if libro in self.libros_reservados:
            self.libros_reservados.remove(libro), self.libros_devueltos.append(libro)
            recuperar.recuperar_libro(libro)
            print(f"El libro: '{libro}', se ha devuelto correctamente")
        else:
            print(f"Error: El libro '{libro}', no esta en tu lista de reservas")

class Biblioteca(ABC):
    def __init__(self):
        self.estanteria = ["Padre Rico", "El Alquimista", "Cien Años de Soledad"]
        self.libros_prestados = []

class Prestar_libro(Biblioteca):
    def prestar_libro(self, libro):
        if libro in self.estanteria:
            self.estanteria.remove(libro)
            self.libros_prestados.append(libro)
            return True
            
class Recuperar_libro(Biblioteca):
    def recuperar_libro(self, libro):
        if libro not in self.estanteria:
            self.estanteria.append(libro)
            return True


#intancias de las ABC Biblioteca
prestar = Prestar_libro()
recuperar = Recuperar_libro()

#intancias de las ABC Usuario
usuario1 = Adquirir_prestado("Rene", "poe22@gmail.com")
usuario1.mostrar_atributos()
usuario1.adquirir_prestado("Padre Rico", prestar)

usuario2 = Adquirir_prestado("Ruben", "rueb@gmail.com")
usuario2.mostrar_atributos()
usuario2.adquirir_prestado("Pae Rico", prestar)