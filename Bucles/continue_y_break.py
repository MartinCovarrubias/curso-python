#continue sirve para saltar una iteración
#break sirve para salir del bucle
#el break se combina con un if
#el continue se combina con un if
#ejemplo
for i in range(1,11):
   # print(i)
    if i == 5:
        break #sale del bluce cuando i vale 5

#ejemplo con continue
for i in range(1,11):
    if i == 5:
        continue #salta la iteración cuando i vale 5 y continua con la siguiente
    print(i)