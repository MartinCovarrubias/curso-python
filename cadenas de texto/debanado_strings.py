# Debanado de cadenas o substrings (nombre documental)

cadena = "este es un ejemplo de substring" 

#obtener longitud de la cadena
print(len(cadena)) #len es una funcion que devuelve la longitud de una cadena
 #valor de la cadena: 31

#obtener un caracter de la cadena
print(cadena[0]) #valor de la cadena: e

#debanadon de una cadena
print(cadena[0:4]) #valor de la cadena: este

#***********NOTA***********
#el debanado de cadenas de forma simple es recorrer una cadena de un punto a otro

print(cadena[:16]) #impresion de la cadena desde el inicio hasta el caracter 16
print(cadena[16:]) #impresion de la cadena desde el caracter 16 hasta el final
print (cadena[:]) #impresion de la cadena completa
print (cadena[::2]) #impresion de la cadena de dos en dos
print (cadena[:-1]) #impresion de la cadena desde el inicio hasta el penultimo caracter
print (cadena[-1:]) #impresion de la cadena desde el ultimo caracter hasta el final
print (cadena[::-1]) #impresion de la cadena al reves
print(cadena[0:31:2]) #impresion de la cadena desde el inicio hasta el final con saltos de 2 en 2