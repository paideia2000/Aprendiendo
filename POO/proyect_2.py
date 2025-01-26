#restaurant, reservaciones, clientes, mesas
from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def mostrar_menu(self):
        pass

class Menu_vegano(Menu):
    def __init__(self):
        self.items = {"Caldo Soja": "8$", "Hambuergeza vegetal": "15$", "Ensalda": "10$"}

    def mostrar_menu(self):
        print(f"Menu Vegano -->> {self.items}")

class Menu_normal(Menu):
    def __init__(self):
        self.items = {"Lomo": "10$","Costillas": "5$","Asado": "7$"}

    def mostrar_menu(self):
        print(f"Menu Normal -->> {self.items}")

class Restaurante:
    def __init__(self):
        self.mesas_reservadas = {}
        self.pedidos = {}
        
    def obtener_pedido(self, mesa, platos):
        self.pedidos[mesa] = platos
        print(f"El pedido de la mesa ({mesa}) tienes estos platos -> {platos} ")

class Cliente(ABC):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}"

    @abstractmethod
    def actualizar_reservas():
        pass

class Reservacion(Cliente):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
    
    #metodo polimorfico de la clase Cliente. Su funsion es reservar una mesa
    def actualizar_reservas(self, mesa):
        if mesa not in restaurant.mesas_reservadas:
            restaurant.mesas_reservadas[mesa] = self.nombre
            print("Ha reservado la mesa '{}' correctamente con el nombre de: '{}'".format(mesa, self.nombre))
        else:
            print(f"Lo sentimos, la mesa {mesa} esta reservada por {restaurant.mesas_reservadas[mesa]}")

class Cancelacion(Cliente):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
    
    #metodo polimorfico de la clase Cliente. Su funsion es eliminar una mesa reservada
    def actualizar_reservas(self, mesa):
        if mesa in restaurant.mesas_reservadas:
            if self.nombre == restaurant.mesas_reservadas[mesa]:
                restaurant.mesas_reservadas.pop(mesa)
                print(f"La reservacion de la mesa: {mesa} ha sido cancelada correctamente por '{self.nombre}'")
            else:
                print(f"Lo sentimos, no puede realizar la canelacion porque la mesa: {mesa} esta reservada por '{restaurant.mesas_reservadas[mesa]}'")    
        else:
            print(f"Lo sentimos la mesa: '{mesa}' no esta en su lista de reservaciones")

#intancias de las subclases de Menu 
menu_ordinario = Menu_normal()
menu_no_ordinario = Menu_vegano()
menu_ordinario.mostrar_menu()#llamando al metodo abstracto:(mostrar_menu) de la clase Menu, para cada subclase
menu_no_ordinario.mostrar_menu()#llamando al metodo abstracto:(mostrar_menu) de la clase Menu, para cada subclase

#instacia de la clase Restaurante
restaurant = Restaurante()
restaurant.obtener_pedido(1, ["lOMO", "COSTILLAS",])#Llamando al metodo(obtener.pedido)
restaurant.pedidos#mostrando los pedidos

#intancias de las subclases de Clientes
reservacion = Reservacion("Rene", 12345678)
cancelacion = Cancelacion("Rene", 12345678)
reservacion.actualizar_reservas(1)
cancelacion.actualizar_reservas(1)















