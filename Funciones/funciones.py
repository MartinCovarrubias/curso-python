# como crear nuestras propias funciones
# que podemos hacer con las funciones
# y como podemos usarlas

# sintaxis de una funcion
# def nombre_funcion():
#     codigo de la funcion

def saludo(): # definimos la funcion saludo con la palabra reservada def
    print("Hola Mundo")

saludo() # llamamos a la funcion saludo

def tabla_del_7():
    for i in range(1, 11):
        print("7 x {} = {}".format(i, 7 * i))

tabla_del_7()