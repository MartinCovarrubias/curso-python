#mostrar datos por pantalla

nombre = input("Introduce tu nombre: ")
edad= int(input("Introduce tu edad: "))

print (nombre) #mostar el nombre por consola
print (edad) #mostrar la edad por consola

print ("Hola", nombre, "tienes", edad, "años") #mostrar datos por consola concatenando

print("hola {} tienes {} años".format(nombre, edad)) #mostrar datos por consola concatenando con format

#* las variables se sustituyen en el orden en el que se introducen en el format