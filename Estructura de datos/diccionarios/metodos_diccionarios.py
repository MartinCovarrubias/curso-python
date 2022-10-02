#metodos de diccionarios

diccionario = {"nombre":"Juan", "apellido":"Perez", "edad":23}

#metodo pop() remueve un elemento del diccionario
#sintaxis: diccionario.pop(clave)

diccionario.pop("nombre")
print(diccionario)

#metodo clear() remueve todos los elementos del diccionario 
#sintaxis: diccionario.clear()
diccionario.clear()
print(diccionario)

# metodo get() devuelve el valor de la clave indicada
# sintaxis: diccionario.get(clave)
diccionario = {"nombre":"Juan", "apellido":"Perez", "edad":23}
print(diccionario.get("nombre"))

#metodo setdefault() agrega un elemento al diccionario al final
#sintaxis: diccionario.setdefault(clave, valor)
diccionario.setdefault("xd", "Juans")
print(diccionario)

#metodo update() actualiza un elemento del diccionario
#sintaxis: diccionario.update({clave:valor})
diccionario.update({"xd":"Pedro"})
print(diccionario)

#tambien se puede actualizar un diccionario con otro diccionario
diccionario2 = {"nombre":"Pedro", "apellido":"Perez", "edad":23}
diccionario.update(diccionario2)
print(diccionario)

#metodo copy() devuelve una copia del diccionario
diccionario3 = diccionario.copy()
print(diccionario3)