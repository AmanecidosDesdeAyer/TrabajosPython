#Ingreso de datos en variables
persona1 = int(input("Cuanto dinero va a depositar: "))
persona2 = int(input("Cuanto dinero va a depositar: "))
persona3 = int(input("Cuanto dinero va a depositar: "))

#La suma de los 3 depositos y lo imprimo en pantalla
sumatoria= (persona1+persona2+persona3)
print("La cantidad total sumada de dinero es: "+str(sumatoria))

#Saco el porcentaje
print("La persona N°1 deposito: "+str((persona1/sumatoria)*100)+" %")
print("La persona N°2 deposito: "+str((persona2/sumatoria)*100)+" %")
print("La persona N°3 deposito: "+str((persona3/sumatoria)*100)+" %")

