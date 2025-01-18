#calculadora simple
def calcular(operador, number_1, number_2):
    if operador == "+":
        suma = lambda num1, numb2: num1 + numb2# funsion lambda
        print("El resultado de sumar {} + {} = {}.".format(number_1, number_2, suma(number_1, number_2)))
    elif operador == "-":
        return number_1 - number_2
    elif operador == "*":
        return number_1 * number_2
    elif operador == "/":
        if number_2 == 0:
            raise ValueError("¡Error!. No se puede dividir por cero'0'.")
        return number_1 / number_2
    else:
        raise ValueError (f"El operador {operador} no es vàlido.")            

def main():#probando una funciòn (lambda), funciòn principal
    print("\n" + "--- Bienvenido a la Calculadora ---".center(100))
    operaciones = ["+", "-", "*", "/"]
    
    while True:
        try:
            operador = input("\n""Cual operaciòn desea realizar -> (+ , - , * , / ): ").strip().lower()#indicar que operador usar
            if operador not in operaciones:
                print("Error: ¡Operador Invàlido!.")
                continue

            number_1 = float(input("Ingrese el primer numero.: "))
            number_2 = float(input("Ingrese el segundo numero.: "))

            resultado = calcular(operador, number_1, number_2)
            print(f"El resultado es {resultado}")
            break
        
        except ValueError as v:
            print(f"Error: {v}")

if __name__ == "__main__":
    main()
        
        
        
        



