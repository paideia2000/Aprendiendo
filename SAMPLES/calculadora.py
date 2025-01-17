#calculadora simple

#interfaz de usuario
def interfaz():
    print("\n" + "--- Bienvenido a la Calculadora ---".center(100))
    print(" Operadores Disponibles -> (+ , - , * , / , %)".center(190))

    
#ejecutar el programa
def ejecutar():
    while True:
        number_1 = float(input("Ingrese el primer numero.: "))
        operador = input( "-> (+ , - , * , / ):  ").strip()#indicar que operador usar
        number_2 = float(input("Ingrese el segundo numero.: "))
        
        if operador == "+":
            suma = lambda num1, numb2: num1 + numb2
            print("\n" + "El resultado de la suma es: {}".format(suma(number_1, number_2)))
        
        elif operador == "-":
            resta = lambda num1, num2: num1 - num2
            print("El resultado de la resta es: {}".format(resta(number_1, number_2)))
        
        elif operador == "*":
            multi = lambda num1, num2: num1 * num2
            print("El resultado de la multiplicacion es: {}".format(multi(number_1, number_2)))
        
        elif operador == "/":
            divi = lambda num1, num2: num1 / num2
            print("El resultado de la divicion  es: {}".format(divi(number_1, number_2)))
        
        elif operador == "%":
            multi = lambda num1, num2: num1 * num2
            print("El resultado de la multiplicacion es: {}".format(multi(number_1, number_2)))
            
        else:
            print("\n" + "¡Operador invàlido!, indique alguno de los cuales se les muestra")

        
            
        
        


ejecutar()



#if operador == "%":
#   if int(number_1) % 2 == 0:
#      print(f"'{number_1}' es un numero par.")
# else:
#     print(f"'{number_1}' es un numero impar.")