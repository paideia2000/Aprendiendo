class coche:
    def __init__(self, matricula, marca, kilometros_recorridos, gasolina):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.gasolina = gasolina
        
    def avanzar(self, km_a_conducir):
        self.kilometros_recorridos += km_a_conducir
        self.gasolina -= self.kilometros_recorridos * 0.1
        if self.gasolina <  0:
            print("Es necesario repostar para recorrer la cantidad indicada de kilómetros")
    
    def repostar(self, litros):
        self.litros = litros + self.gasolina
    

mi_coche = coche("000000", "Ford", 100, 40)
mi_coche.avanzar(100)
mi_coche.repostar(10)
print(f"Si queremos avanzar {mi_coche.kilometros_recorridos} km, necesitamos {mi_coche.gasolina} litros de gasolina y si queremos continuar avanzando 50 km màs,necesitaremos {mi_coche.litros} litros de gasolina")