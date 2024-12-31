from random import randint

numeros = randint(0,10)#generar numeros aleatorios

def choise_user():#identificar el numero ganador o continuar bucle sino
    while True:
        try:
            choise = int(input("Ingrese el numero que usted cree ganador en el rango del (1-10): "))
            if choise > numeros:
                if choise > 10:
                    print("Error: por favor inserte un numero menor que (10)")
                    continue
                print("Uff, se ha pasado un poco, vuelva a intentar reduciendo el numero")
            elif choise < numeros:
                if choise <= 0:
                    print("Error: por favor inserte un numero mayor que (1)")
                    continue
                print("Uff, se ha quedado corto, vuelva a intentar aumentando  el numero")
            else:
                print("Has aceptado tu ganas")
                break
        except ValueError:
            print("Error: Inserte numeros por favor")

choise_user()

