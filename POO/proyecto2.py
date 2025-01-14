#agenda telefonica
agenda = {"Rene": "613121861", "Ruben": "613126861"}

def consultar_contacto():
    name = input("Ingrese el nombre del contacto que desea buscar: ").capitalize().strip()
    if name in agenda:
        print("El numero de {} es: {}".format(name, agenda[name]))
    else:
        print("Lo sentimos, ese contacto no lo hemos encontrado en su agenda.")
        
