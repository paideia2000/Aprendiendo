from random import randint



def choise_user():#identificar el numero ganador o continuar bucle sino
    while True:
        numero = randint(1,10)#generar numero aleatorios
        while True:
            try:
                choise = int(input("Ingrese el numero que usted cree ganador en el rango del (1-10): "))
                if choise < 1 or choise >  10:
                    print("Error: Inserte numero en el rango del 1-10")
                elif choise > numero:
                    print("Uff, se ha pasado un poco, vuelva a intentar reduciendo el numero")
                elif choise < numero:
                    print("Uff, se ha quedado corto, vuelva a intentar aumentando  el numero")
                else:
                    print("Has aceptado tu ganas")
                    break
            except ValueError:
                print("Error: Inserte numero por favor")
    
        cerrar = input("Desea cerrar el juego? (SI/NO): ").lower().strip()
        if cerrar == "si":
            print("¡Hasta la proxima!")
            break
        elif cerrar == "no":
            print("\n¡Nuevo juego iniciado!")
        else:
            print("Incinuamos que quizo cerrar el programa. ¡Hasta la proxima!")
            break
            


choise_user()




