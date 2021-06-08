#Ingreso de datos en variables
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))

#Comprobacion de variables

#Comprobando si num1 es mayor que todos
if (num1 > num2 and num1 > num3):

    print(f"El numero mayor es {num1}")


#Comprobando si num2 es mayor que todos
if (num2 > num1 and num2 > num3):

    print(f"El numero mayor es {num2}")
    

#Comprobando si num3 es mayor que todos
if (num3 > num1 and num3 > num2):
    
    print(f"El numero mayor es {num3}")
    
