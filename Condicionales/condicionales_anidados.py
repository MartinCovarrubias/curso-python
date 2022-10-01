# Es aquel que estara dentro de otro condicional

#ejemplo if-else anidados

nombre = "Juan"
edad = 13

if nombre == "Juan":
    if edad == 18:
        print("Es Juan y tiene 18 años")
    else:
        print("Es Juan pero no tiene 18 años")
    #print("tu eres Juan")
else:
    print("tu no eres Juan")