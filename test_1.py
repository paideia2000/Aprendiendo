numeros_pares = []# AÑADIRLOS NUMEROS PARES

def detectar_pares():
    while True:
        try:
            ask_numb = input("Ingrese los valores por favor o escriba (FIN) para cerrar elprograma: ").lower().strip()
            if ask_numb == "fin":
                print("Hasta luego")
                break
            elif int(ask_numb) % 2 != 1:
                numeros_pares.append(ask_numb)
        except ValueError:
            print("Error: Por favor ingrese un valor valido o (FIN) para salir, GRACIAS")
            
detectar_pares()
if numeros_pares:
    print(f"Los numeros pares que has ingresado son : {numeros_pares}")
else:
    print(f"No agrego ningun valor a la lista")
    