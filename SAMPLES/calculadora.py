#calculadora simple

#interfaz de usuario
def interfaz():
    print("\n" + "--- Bienvenido a la Calculadora ---".center(100))
    print(" Operadores Disponibles -> (+ , - , * , / , %)".center(190))

    
#ejecutar el programa
def ejecutar():
    operaciones = ["+", "-", "*", "/"]
    while True:
        operador = input("\n""Cual operaciòn desea realizar -> (+ , - , * , / ): ").strip().lower()#indicar que operador usar
        if operador not in operaciones:
            print("¡Error!. Por favor inserte un operador vàlido")
            continue

        number_1 = float(input("Ingrese el primer numero.: "))
        number_2 = float(input("Ingrese el segundo numero.: "))
        
        if operador == "+":
            suma = lambda num1, numb2: num1 + numb2
            print("El resultado de sumar {} + {} = {}.".format(number_1, number_2, suma(number_1, number_2)))

        elif operador == "-":
            resta = lambda num1, num2: num1 - num2
            print("El resultado de restar {} - {} = {}.".format(number_1, number_2, resta(number_1, number_2)))

        elif operador == "*":
            multi = lambda num1, num2: num1 * num2
            print("El resultado de multiplicar {} * {} = {}.".format(number_1, number_2, multi(number_1, number_2)))

        else:
            if number_2 == 0:
                print("¡Error!. No se puede dividir por cero(0).")
            else:
                divi = lambda num1, num2: num1 / num2
                print("El resultado de dividir {} / {} = {}.".format(number_1, number_2, divi(number_1, number_2)))
            
ejecutar()

