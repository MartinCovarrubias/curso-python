
while True:
    try:
        num1 = int(input("Introduce un numero: "))
        resultado = 100/num1
        print("El resultado es: ", resultado)
        break # break es una funcion que rompe el ciclo
    except ZeroDivisionError: # ZeroDivisionError es una excepcion que se ejecuta cuando se divide entre cero
        print("No se puede dividir entre cero")


while True:
    try:
        edad = int(input("Introduce tu edad: "))
        print("Tu edad es: ", edad)
        break
    except ValueError: # ValueError es una excepcion que se ejecuta cuando se introduce un valor no numerico
        print("Ha ocurrido un error, introduce el valor correcto")

while True:
    try:
        edad = int(input("Introduce tu edad: "))
        print("Tu edad es: ", edad)
        break
    except KeyboardInterrupt: # KeyboardInterrupt es una excepcion que se ejecuta cuando se presiona ctrl+c
        print("has interrumpido la ejecucion")
        break