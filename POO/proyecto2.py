#agenda telefonica
agenda = {}#"Rene": "613121861", "Ruben": "613126861"

def consultar_agenda():
    print("Nombre".ljust(20) + "N-Contacto")
    print("-" * 30)
    for nombre, contacto in agenda.items():
        print(nombre.ljust(20) + contacto)

def elminar_contacto(contacto):
    if contacto in agenda:
        print(f"El contacto '{contacto}' ha sido elminado satifactoriamente.")
        return agenda.pop(contacto)
    else:
        print("Ese contacto no existe en tu agenda.")
        
def ejecutar():
    #interfaz que se le muestra al usuario
    print("\n--- Bienvenido a la Agenda ---")
    print("-> Ingrese el digito (1) para ver sus contactos.")
    print("-> Ingrese el digito (2) para insertar un nuevo contacto.")
    print("-> Ingrese el digito (3) para eliminar un contacto.")
    print("-> Ingrese el digito (4) para salir del programa.")
    
    #Ejecucion del programa
    
    while True:
        accion_usuario = input("\nCual de las anteriores acciònes desea realizar?. ")
        if accion_usuario == "4":
            print("Nos volveremos a ver, Hasta la proxima.")
            break
        elif accion_usuario == "3":
            contacto = input("\nIndiquenos el Nombre del contacto que desea eliminar.: ").strip()
            elminar_contacto(contacto)
            continue
        elif accion_usuario == "2":
            nombre = input("\nIngrese el nombre del contacto que desea agregar.: ")# obtener el nombre del contacto que quiere agregar
            numero = input("Ingrese un numero con (7) digitos por favor.: ")# obtener el numero del contacto que quiere agregar
            agenda[nombre] = numero
            print("El contacto se ha añadido correctamente")
        elif accion_usuario == "1":
            if not agenda:
                print("La agenda esta vacia")
            else:
                consultar_agenda()
            break
        else:
            print("¡Error!, elija unas de las opciones definidas anteriormente")
                    

if __name__ == "__main__":
    ejecutar()
    
