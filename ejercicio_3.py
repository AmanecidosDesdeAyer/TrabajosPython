#Ingreso de datos en variables
nombre = input("Ingrese su nombre: ")
horast= int(input("Ingrese sus horas trabajadas: "))
salarioh= int(input("Ingrese el salario por hora: "))

#Imprimo los datos que ingreso anteriormente
print(f"su nombre es {nombre}, ha trabajado {horast} horas, y su salario por hora es de {salarioh} soles")

#Calculo del sueldo
sueldo = (horast * salarioh)
print(f"Su sueldo final es de {sueldo} soles")

#Aplico el aumento del 15% en una variable
sueldoAumentado= (15/100*sueldo)

#Sumo el 15% con el sueldo
sueltoTotal = sueldoAumentado + sueldo


#Imprimo el sueldo mas el aumento (SueltoTotal)
print( )
print(f"Hemos decidido hacerle un aumento del 15% haci que su sueldo es de {sueltoTotal} soles")
