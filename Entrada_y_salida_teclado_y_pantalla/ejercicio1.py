from math import sqrt # Importamos la función raíz cuadrada

a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el  valor de b: "))
c = int(input("ingrese el valor de c: "))
x1=0
x2=0

if((b**2)-(4*a*c)) < 0: # Si el discriminante es menor que cero, no hay solución
    print("No tiene solución")
else:
    x1 = (-b + sqrt(((b**2) - (4*a*c))))/(2*a) #formula general
    x2 = (-b - sqrt(((b**2) - (4*a*c))))/(2*a)
    print("Las soluciones son: ", x1, " y ", x2)

