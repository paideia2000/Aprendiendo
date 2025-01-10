class Robot():
    def __init__(self, nombre):
        self.posicion = [0,0]
        self.nombre = nombre
        
    def movimiento_robot(self, secuencia):
        for letras in secuencia:
            if letras in ["a", "r", "i", "d"]:
                self.actualizar_posicio(letras)
            else:
                print("Error:. Ingrese una secuencia valida por favor")
    
    def actualizar_posicio(self, secuencia):
        if secuencia == "a":
            self.posicion[0] += 1
        elif secuencia == "r":
            self.posicion[0] -= 1
        elif secuencia == "d":
            self.posicion[1] += 1
        else:
            self.posicion[1] -= 1
        print(f"Ahora {self.nombre} esta en la posicion {self.posicion}")
            

    def ejecutar_accion(self):
        while True:
            secuencia = input("Ingrese secuencia (ej:'AIDRDAR') para poder mover al robot o (FIN) para salir.: ").lower().strip()
            if secuencia == "fin":
                print("Hasta luego")
                break
            else:
                self.movimiento_robot(secuencia)



robot = Robot("Machinariun")
robot.ejecutar_accion()
            
    
