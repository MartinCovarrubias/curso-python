#actualizar datos de una lista
lista = [1,2,3,"hola","mundo",4,5]

print(lista[3])

lista[3] = "adios" # actualiza el elemento de la posicion 3 por el elemento "adios"

print(lista[3])


#pop() elimina el ultimo elemento de la lista
lista.pop() #no lleva argumentos, solo elimina el ultimo elemento de la lista
print(lista)

#remove() elimina el elemento que se le indique

lista.remove(2) #elimina el elemento 2 de la lista
print(lista)