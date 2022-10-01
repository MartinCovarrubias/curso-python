palabra1 = input("Introduce la palabra 1: ")
palabra2 = input("Introduce la palabra 2: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("Las palabras deben tener al menos 3 caracteres")
elif palabra1[-3:] == palabra2[-3:]:
    print("las palabras riman")
elif palabra1[-2:] == palabra2[-2:]:
    print("las palabras riman un poco")
else:
    print("las palabras no riman")
   




