#liga de futboll con programas: clases(Equipos,Partidos,Liga)
import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        
    def update_puntos(self, goles_a_favor, goles_en_contra):
        self.goles_a_favor += goles_a_favor
        self.goles_en_contra += goles_en_contra
        if goles_a_favor > goles_en_contra:
            self.puntos += 3
        elif goles_a_favor == goles_en_contra:
            self.puntos += 1
        
#Partidos
class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def jugar(self):
        goles_equipo1 = random.randint(0, 7)
        goles_equipo2 = random.randint(0, 7)
        self.equipo1.update_puntos(goles_equipo1, goles_equipo2)
        self.equipo2.update_puntos(goles_equipo2, goles_equipo1)
        print(f"{self.equipo1.nombre} {goles_equipo1} - {goles_equipo2} {self.equipo2.nombre}")

#Clase liga
class Liga:
    def __init__(self, equipos):
        self.equipos = equipos
        
    def tabla_posiciones(self):
        self.equipos.sort(key=lambda x: x.puntos, reverse=True)
        print("Tabla de Posiciones\n".center(100))
        for equipo in self.equipos:
            print(f"{equipo.nombre}: {equipo.puntos} puntos -- Goles_a_Favor {equipo.goles_a_favor}, -- Goles_en_Contra {equipo.goles_en_contra}")
    
    def enfrentamiento(self):
        print("Partidos Jugados\n".center(100))
        for i in range(len(self.equipos)):
            for j in range(i+1, len(self.equipos)):
                partidos = Partido(self.equipos[i], equipos[j])
                partidos.jugar()
        
    



python = Equipo("Python")
java = Equipo("Java")
c = Equipo("C")
go = Equipo("Goo")

equipos = [python, java, c, go]
liga = Liga(equipos)
liga.enfrentamiento()
liga.tabla_posiciones()







