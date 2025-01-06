class Robot():
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = (0, 0)


    
    def obtener_movimiento(self):    
        while True:
                obtener_mov = input("Ingresa (A) para ir hacia adelante; (R) para Retroceder; (I) Izquierda; (D) Derecha o (FIN) para salir del programa: ").lower().strip()
                if obtener_mov in ["a", "r", "i" ,"d", "fin"]:
                    return obtener_mov
                else:
                    print("Error: Tiene que ingresar algun valor que se le indica en la pregunta anterior. GRACIAS")

    def posicion_tablero(self, mov_obtenido):
        if  mov_obtenido == "a":
            print(f"{self.nombre} se ha movido hacia adelante, la posisicon es: {self.posicion[0], self.posicion[1] + 1}")
        elif mov_obtenido == "r":
            print(f"{self.nombre} se ha movido hacia atras, la posisicon es: {self.posicion[0], self.posicion[1] - 1}")
        elif mov_obtenido == "d":
            print(f"{self.nombre} se ha movido hacia la derecha, la posisicon es: {self.posicion[1] + 1, self.posicion[1]}")
        else:
            print(f"{self.nombre} se ha movido hacia la izquierda, la posisicon es: {self.posicion[1] - 1, self.posicion[1]}")

    def ejecutar(self):
        while True:
            mov_obtenido = self.obtener_movimiento()
            if mov_obtenido == "fin":
                print("Hasta luego gracias")
                break
            else:
                self.posicion_tablero(mov_obtenido)



    
mi_robot = Robot("Supreme")

mi_robot.ejecutar()
