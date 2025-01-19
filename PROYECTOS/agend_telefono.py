#agenda telefonica

def consultar_agenda():
    print("Nombre".ljust(20) + "N-Contacto")#espaciando 20 casillas en el str(nombre) y el str(N-Contacto) con .ljust(20)
    print("-" * 30)
    for nombre, contacto in agenda.items():
        print(nombre.ljust(20) + contacto)#espaciando 20 casillas en la keys(nombre) y el value(N-Contacto) con .ljust(20)

def insertar_nombre():
    nombre = input("\nIngrese el nombre del contacto que desea agregar.: ")# obtener el nombre del contacto que quiere agregar
    while True:
        try:
            numero = int(input("Ingrese un numero con (7) digitos por favor.: "))# obtener el numero del contacto que quiere agregar
            if len(str(numero)) < 7 or len(str(numero)) > 7:
                print("¡Error!: debe insertar un numero de (7) digitos.")
                continue
            else:
                agenda[nombre] = str(numero)
                print("El contacto se ha añadido correctamente.")
                return agenda
        except ValueError:
            print("¡Valor invàlido!. Debe insertar un numero entero de (7) cifras.")

def elminar_contacto(contacto):
    if contacto in agenda:
        print(f"El contacto '{contacto}' ha sido elminado satifactoriamente.")
        return agenda.pop(contacto)
    else:
        print("Ese contacto no existe en tu agenda.")

def buscar_contacto(nombre_contacto):
    if nombre_contacto not in agenda:
        print("Lo sentimos, ese conacto no se encuentra en su agenda.")
    else:
        print(f"El numero del contacto '{nombre_contacto}' es: {agenda[nombre_contacto]}")
        
def ejecutar():#interfaz que se le muestra al usuario
    agenda = {}
    print("\n--- Bienvenido a la Agenda ---")
    print("-> Ingrese el digito (1) para ver sus contactos.")
    print("-> Ingrese el digito (2) para insertar un nuevo contacto.")
    print("-> Ingrese el digito (3) para eliminar un contacto.")
    print("-> Ingrese el digito (4) para buscar un contacto.")
    print("-> Ingrese el digito (5) para salir del programa.")
    
    while True:#Ejecucion del programa
        try:            
            accion_usuario = int(input("\nCual de las anteriores acciònes desea realizar?. "))
            if accion_usuario == 5:
                print("Nos volveremos a ver, Hasta la proxima.")
                break
            elif accion_usuario == 4:
                buscar_nombre = input("Ingrese el nombre del usuario que desea encontrar.: ")
                buscar_contacto(buscar_nombre)
            elif accion_usuario == 3:
                contacto = input("\nIndiquenos el Nombre del contacto que desea eliminar.: ").strip()
                elminar_contacto(contacto)
                continue
            elif accion_usuario == 2:
                insertar_nombre()
            elif accion_usuario == 1:
                if not agenda:
                    print("La agenda esta vacia")
                else:
                    consultar_agenda()
            else:
                print("¡Error!, elija unas de las opciones definidas anteriormente")
        except ValueError:
            print("¡Error!: Ingrese un valor numerico.")
    
if __name__ == "__main__":
        
    ejecutar()
            
            
            
            
            
    
