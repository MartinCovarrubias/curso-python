#// todo: Solicita al usuario que ingrese un dato por teclado y lo muestra en pantalla

#** Nota
#** saber que tipo de dato es
#** los datos que  se ingresan seran guardados en una variable
#** tener cuidado con los cambios de valor en la variable (No exiten variables constantes).

#** Entrada de datos por teclado

from traceback import print_tb


nombre = input("ingrese su nombre:") # input() es una funcion que permite ingresar datos por teclado
#**Nota** 
#Cuando los datos ingresados son string, no es necesario indicar el tipo de dato
print("Su nombre es:", nombre)

edad = int(input("ingrese su edad: ")) # int() es una funcion que permite convertir un string a entero
print("Su edad es:", edad)
#**Nota**
#Si los datos son float, se debe convertir a float

precio = float(input("ingrese el precio: ")) # float() es una funcion que permite convertir un string a float
print("El precio es:", precio)