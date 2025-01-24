#biblioteca

class Persona():
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_atributos(self):
        print(f"Su nombre de usuario es: {self.nombre} y su email es: {self.email}")
        
class Usuario(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.libros_reservados = []
        self.libros_devueltos = []

    def adquirir_prestado(self, libro, biblioteca):
        if biblioteca.prestar_libro(libro):
            self.libros_reservados.append(libro)
            print(F"El libro:'{libro}', ha sido prestado ha:'{self.nombre}', su email es:'{self.email}'")
        else:
            print(f"El libro: {libro} no lo tenemos en la estanteria, lo sentimos.")

    def devolver_libro(self, libro):
        if libro in self.libros_reservados:
            self.libros_reservados.remove(libro), self.libros_devueltos.append(libro)
            biblioteca.recuperar_libro(libro)
            print(f"El libro: '{libro}', se ha devuelto correctamente")
        else:
            print(f"Error: El libro '{libro}', no esta en tu lista de reservas")
            

class Biblioteca():
    def __init__(self):
        self.estanteria = ["Padre Rico", "El Alquimista", "Cien Años de Soledad"]

    def prestar_libro(self, libro):
        if libro in self.estanteria:
            self.estanteria.remove(libro)
            return True
    
    def recuperar_libro(self, libro):
        if libro not in self.estanteria:
            self.estanteria.append(libro)
            return True
            
#intancias de las clases
biblioteca = Biblioteca()
usuario1 = Usuario("Rene", "poencima22@gmail.com")

#metodos de las clases
usuario1.adquirir_prestado("Padre Rico", biblioteca)
print(usuario1.libros_reservados)
usuario1.devolver_libro("Pade Rico")
print(usuario1.libros_reservados)
print(usuario1.libros_devueltos)

