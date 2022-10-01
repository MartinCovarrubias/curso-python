
numero = int(input("Introduce un número: "))

if numero > 0:
    print("El valor absoluto de", numero, "es:", numero)
else:
  
   print("El valor absoluto de", numero, "es:", numero * -1)

# utilizando la funcion abs()

if numero > 0:
    print("El valor absoluto de", numero, "es:", numero)
else:
  
   print("El valor absoluto de", numero, "es:", abs(numero))