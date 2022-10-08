
lista = [] # Lista vacia
num = 0 # Variable para guardar el numero

def pedir_numeros(): # Funcion para pedir numeros
    i = 0 # Variable para contar los numeros
    while i < 5: # Mientras i sea menor que 5
        num = int(input("Introduce un numero: ")) # Pide un numero
        lista.append(num) # Lo añade a la lista
        i += 1 # Aumenta el contador de numeros pedidos

def ordenar ():
    lista.sort() # Ordena la lista de menor a mayor
    pares = []
    impares = []
    for i in lista: # Recorre la lista
        if i % 2 == 0: # Si el numero es par
            pares.append(i) # Lo añade a la lista de pares
        else:
            impares.append(i)
    print("Pares: ", pares)
    print("Impares: ", impares)

pedir_numeros()
ordenar()



