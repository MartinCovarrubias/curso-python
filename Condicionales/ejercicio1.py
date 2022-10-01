letra = input("Ingrese una letra: ")

if letra == "a":
    print("Es una vocal")
elif letra == "e":
    print("Es una vocal")
elif letra == "i":
    print("Es una vocal")
elif letra == "o":
    print("Es una vocal")
elif letra == "u":
    print("Es una vocal")
else:
    print("No es una vocal")

# forma mas corta
#in sirve para ver si un elemento esta dentro de una lista
if letra in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")