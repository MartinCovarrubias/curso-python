# Es una lista que no se puede modificar
# Se usa para almacenar datos que no se van a modificar
# Se usa para devolver varios valores de una función


tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #definir tupla con parentesis para 
# buena practica

#tambien pueden definirse sin parentesis
tupla2 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#acceder a elementos de la tupla
print(tupla[0]) #imprime el primer elemento de la tupla

#debanado de tuplas
print(tupla[0:3]) #imprime los elementos desde el 0 hasta el 3

#concatenar tuplas
tupla3 = tupla + tupla2
print(tupla3)