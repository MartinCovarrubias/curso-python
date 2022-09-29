#uso de operadores aritmeticos con strings

cadena = "esto es un ejemplo"
cadena2 = " de concatenacion"

 #concatenacion *union de dos strings*
print(cadena + cadena2) # uso del operador + para concatenar strings

#concatenar un mensaje con una variable
print("soy un mensaje" + cadena) 

#otra forma de concatenar
print("soy un mensaje", cadena)

#repetir strings
print(cadena * 3) #uso del operador * para repetir strings

#Convertir un numero a string
numero = 10
print("el numero es: " + str(numero))
print(type(str(numero))) #convertir un numero a string e imprimir el tipo de dato

