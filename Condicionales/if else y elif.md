# Condicionales
--- Son situaciones que pueden darse dentro de un programa, y que dependiendo de si se cumplen o no, se ejecutan unas instrucciones u otras.

## if
--- La estructura de control if, es la más básica de las estructuras de control, y se utiliza para ejecutar un bloque de código si se cumple una condición.

## else
--- La estructura de control else, se utiliza para ejecutar un bloque de código si no se cumple la condición del if.


## elif
--- Se utiliza cuando se necesitan más de dos condiciones, y se ejecuta el bloque de código si se cumple la condición del elif.


## ejemplo if
--- El siguiente ejemplo muestra como se utiliza la estructura de control if.

    if 5 > 3:
        print("5 es mayor que 3")

## ejemplo else
--- El siguiente ejemplo muestra como se utiliza la estructura de control else.

    if 5 < 3:
        print("5 es menor que 3")
    else:
        print("5 es mayor que 3")

## ejemplo elif
--- El siguiente ejemplo muestra como se utiliza la estructura de control elif.

    if 5 < 3:
        print("5 es menor que 3")
    elif 5 == 3:
        print("5 es igual que 3")
    else:
        print("5 es mayor que 3")