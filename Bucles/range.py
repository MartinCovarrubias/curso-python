# tambien es un elemento iterable por el bucle for
# toma un punto de inicio, y un punto de final
# sintaaxis: range(inicio, final, salto)
# el salto es opcional, por defecto es 1
#el valor de la derecha no se incluye

for i in range(1,10):
    print(i)

# si no se especifica el inicio, por defecto es 0
for i in range(10):
    print(i)

#usando el salto
for i in range(1,10,2): #va de 1 a 9 de 2 en 2
    print(i)

#usando numeros negativos
for i in range(-10,-1,1): #va de -10 a -2 de 1 en 1
    print(i)