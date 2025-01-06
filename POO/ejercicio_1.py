class Robot():
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = (0, 0)

    
    def obtener_movimiento(self):    
        while True:
                obtener_mov = input("Ingresa (A) para ir hacia adelante; (R) para Retroceder; (I) Izquierda; (D) Derecha: ").lower().strip()
                if obtener_mov in ["a", "r", "i" ,"d"]:
                    return obtener_mov
                elif obtener_mov == "fin":
                    print("Hasta luego")
                    break
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
        mov_obtenido = self.obtener_movimiento()
        mi_robot.posicion_tablero(mov_obtenido)


    
mi_robot = Robot("Supreme")

mi_robot.ejecutar()
