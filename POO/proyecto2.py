#agenda telefonica

agenda = {}#"Rene": "613121861", "Ruben": "613126861"

def consultar_contacto():
    print("Nombre".ljust(20) + "N-Contacto")
    print("-" * 30)
    for nombre, contacto in agenda.items():
        print(nombre.ljust(20) + contacto)

def insertar_nombre():
    pedir_nombre = input("Ingrese el nombre del contacto que desea agregar.: ")#nombre del contacto que quiere agregar
    print(f"Su nuevo nombre de contacto '{pedir_nombre}' se ha agregado correctamente.")

def insertar_numero():
    try:
        pedir_numero = int(input("\nIngrese un numero con (7) digitos por favor.:"))
        if len(str(pedir_numero)) != 7:
            print("¡Contacto invàlido!, debe insertar un numero de 7 digitos.")
        else:
            print(f"El numero '{pedir_numero}' se ha añadido correctamente.")
    except ValueError:
        print("¡Error!. Debe añadir un valor numèrico al campo anterior.")





if __name__ == "__main__":
    pass