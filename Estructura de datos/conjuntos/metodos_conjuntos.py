#metodos usados en conjuntos

conjunto = {1,2,3,4,5,"hola"}

#metodo add agrega un elemento al conjunto
conjunto.add(6)
print (conjunto)

#metodo remove o discard elimina un elemento del conjunto
#sintaaxis: conjunto.remove(elemento)
conjunto.remove(6) # o conjunto.discard(6)
print (conjunto)

#metodo pop elimina un elemento aleatorio del conjunto
#sintaaxis: conjunto.pop()
conjunto.pop()
print (conjunto)

#metodo update agrega varios elementos al conjunto 
#sintaaxis: conjunto.update([elemento1, elemento2, elemento3, ...])
conjunto.update([6,7,8,9])
print (conjunto)

#metodo clear elimina todos los elementos del conjunto
#sintaaxis: conjunto.clear()
conjunto.clear()
print (conjunto)