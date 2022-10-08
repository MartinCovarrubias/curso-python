# una funcion puede devolver un valor
# algunas lo hacen de manera predeterminada
# otras lo hacen mediante la palabra reservada return
# return se puede usar con cualquier tipo de dato
def suma(a, b):
    return a + b
#para ver un return debe usar print
print("la suma es",suma(1, 2))

def decimal_a_binario(decimal):
    return bin(decimal)

print("el numero binario es", decimal_a_binario(10))

#return por asignacion
def asignacion():
    return 1, 2, 3, 4, 5

a, b, c, d, e = asignacion()
print(a, b, c, d, e)