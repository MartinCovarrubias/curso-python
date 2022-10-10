
#* Variables globales

#? Las variables globales son aquellas que se declaran fuera de las funciones y se pueden utilizar en cualquier parte del programa.

#! funcion estatica que no recibe parametros ni argumentos
def variables():
    global num #* se declara la variable global num
    global num2 #* se declara la variable global num2
    #! primero se engloblan las variables y despues se les asigna un valor
    num = 10
    num2 = 20
    resultado = num + num2
    return resultado

print(variables())

resta = num - num2 #* se puede utilizar la variable global num y num2 fuera de la funcion
print(resta)