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
        self.mesas_reservadas = {}#1: 'Rene',2: 'Ruben'
        self.pedidos = {}
        
    def realizar_pedido(self, mesa, platos):
        self.pedidos[mesa] = platos
        print(f"El pedido de la mesa ({mesa}) tienes estos platos -> {platos} ")

class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def reservar_mesas(self, mesa, nombre):
        if mesa not in self.mesas_reservadas:
            self.mesas_reservadas[mesa] = nombre
            print("Su reserva de la mesa '{}' se ha reservado correctamente con el nombre '{}'".format(mesa, nombre))
        else:
            print(f"Lo sentimos, la mesa {mesa} esta reservada por {self.mesas_reservadas[mesa]}")

    def eliminar_reserva(self, mesa):
        if mesa  in self.mesas_reservadas:
            self.mesas_reservadas.pop(mesa)
            print(f"La reservacion de la mesa: {mesa} ha sido cancelada")
        else:
            print(f"Lo sentimos la mesa: {mesa} no existe")

#intanciando los objetos con sla clase abstracta     
menu_ordinario = Menu_normal()
menu_no_ordinario = Menu_vegano()

#llamando al metodo abstracto para cada subclase
menu_ordinario.mostrar_menu()
menu_no_ordinario.mostrar_menu()

#instacian de la clase Restaurante y sus metodos
restaurante = Restaurante()
restaurante.reservar_mesas(1, "Rene")
restaurante.reservar_mesas(2, "Ruben")
restaurante.eliminar_reserva(1)















