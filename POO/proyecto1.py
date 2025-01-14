#sistema bancario simple

def consultar_saldo(saldo):
    print(f"Su saldo actual es de {round(saldo, 2)} euros")
    
def ingresar_dinero():
    añadir_dinero = float(input("Indicanos la cantidad que desea ingresar.: "))
    if añadir_dinero <= 0:
        print(f"La opcion que ha ingresado -> '{añadir_dinero}' no es vàlida.")
        return 0
    else:
        print(f"La cantidad se ha añadido correctamente.")
        return añadir_dinero
        
def retirar_dinero(saldo):
    extraer_dinero = float(input("Indicanos la cantidad que desea extraer.: "))
    if extraer_dinero > saldo: 
        print(f"Lo sentimos pero no puede retirar dinero si su saldo es de {saldo}$.")
        return 0
    elif extraer_dinero <= 0:
        print("Lo sentimos hubo un ¡Error!, ha ingresado un valor no vàlido.")
        return 0
    else:
        print(f"Su retiro se ha realizado con exito.")
        return extraer_dinero

def menu_principa():
    saldo = 0
    #creando interfaz
    print("\n--- Bienvenido a '4R' Bank " + " Su banco de confianza. ---")
    print("\nA continuacion accion le apareceran 4 acciones, cual desea realizar?.")
    print("-" * 50)
    print("-> Ingrese el digito (1) para consultar su saldo.")
    print("-> Ingrese el digito (2) para ingresar dinero.")
    print("-> Ingrese el digito (3) para extraer dinero.")
    print("-> Ingrese el digito (4) para salir del programa.\n")
    
    
    #entrada de datos por parte del cliente
    while True:
        try:    
            opcion = int(input("Cual opcion desea realizar?.:"))
            if opcion == 1:
                consultar_saldo(saldo)
            elif opcion == 2:
                saldo += ingresar_dinero()
            elif opcion == 3:
                saldo -= retirar_dinero(saldo)
            elif opcion == 4:
                print("Saludos, ¡Hasta luego!.")
                break
            else:
                print("Por favor ingrese un valor de los que se le indica anteriormente, ¡Gracias!.")
        except ValueError as v:
            print(v)
                
                
                

if __name__ == '__main__':
    menu_principa()


