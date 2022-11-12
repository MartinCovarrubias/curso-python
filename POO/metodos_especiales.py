#metodos especiales

class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("el objeto {} ha sido creado".format(self.marca))
#! dentro de la clase se utiliza self para referirse a los atributos de la clase
#destructor sirve para eliminar un objeto
    def __del__(self):
        print("Objeto eliminado")
        
telefono1 = FabricaTelefonos("Samsung","azul")
print(telefono1.marca)