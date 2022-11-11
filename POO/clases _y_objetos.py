
# forma para crear una clase

class Fabrica(): # nombre de la clase se recomienda que empiece con mayuscula
    pass # palabra reservada para indicar que no se va a hacer nada

print (type(Fabrica)) # <class 'type'> es una clase no un tipo de dato

# crear un objeto de la clase Fabrica
celular = Fabrica() # instanciar la clase
celular2 = Fabrica() # instanciar la clase
print (type(celular)) # <class '__main__.Fabrica'> es una clase no un tipo de dato
print (type(celular2)) # <class '__main__.Fabrica'> es una clase no un tipo de dato

##! No confundir class con def (def es para funciones) ##!
##! No poner el mismo nombre ##!
