
class FabricaTelefono(): # Clase padre
    marca = "Nokia"      # Atributo de clase
    color = "negro"
    memoriaRam = 6
    almacenamiento = 32

#? Cada vez que creemos un objeto de la clase podremos tener acceso a los atributos de clase padre
    #creamos el metodo llamar
    def llamar(self, mensaje): #metodo de instancia es aquel que nosotros codificamos, self es el objeto que se crea
        return mensaje

    def escucharMusica(self):
        return "Escuchando musica" #se ejecuta cada sentencia que este dentro del metodo

#creamos el objeto de la clase
telefono = FabricaTelefono() # Instanciar la clase
telefono.marca #asignar un atributo de clase
telefono.color
telefono.memoriaRam
telefono.almacenamiento
telefono.llamar("Hola") # Llamamos al metodo llamar y le pasamos el parametro "Hola"
telefono.escucharMusica() # Llamamos al metodo escucharMusica

print (telefono.marca) # Nokia