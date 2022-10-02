
diccionario = {"nombre":"Juan", "apellido":"Perez", "edad":23}

#metodo keys() devuelve una lista con las claves del diccionario
print(diccionario.keys())

#metodo values() devuelve una lista con los valores del diccionario
print(diccionario.values())

#mandar a llamar un valor por su clave
print(diccionario["nombre"])

#agrergar un nuevo elemento al diccionario
diccionario["carrera"] = "Ingenieria en computacion"
print(diccionario)

#modificar un valor del diccionario
# modifica la clave y el valor 
diccionario["nombre"] = "Pedro"
print(diccionario)