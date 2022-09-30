# es aquel que une varias expresiones lógicas en una sola

# Operador logicos simbolos
# && and
# || or
# ! not
# //todo: en python se usa and, or, not como operadores logicos

# Operador logico and
print (10>2 and 10>5) # True, ambos valores son verdaderos
print (10>2 and 10<5) # False, uno de los valores es falso
print (10<2 and 10<5) # False, ambos valores son falsos

# Operador logico or
print (10>2 or 10>5) # True, ambos valores son verdaderos
print (10>2 or 10<5) # True, uno de los valores es falso
print (10<2 or 10<5) # False, ambos valores son falsos

# Operador logico not
print (not 10>2) # False, el valor es verdadero
print (not 10<2) # True, el valor es falso