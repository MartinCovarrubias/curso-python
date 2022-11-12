
#init es el constructor de la clase
#self es el objeto que se crea al instanciar la clase

class FabricaTelefono():
    marca = "Samsung"

    def ElaborarHuawei(self):
        self.marca = "Huawei" #

telefono = FabricaTelefono()
telefono.ElaborarHuawei()
#print(telefono.marca)

# ! metodo init

class FabricaTelefono2():
    def __init__(self, marca, modelo): #se colocan los atributos que se van a usar
        self.marca = marca
        self.modelo = modelo

        telefono = FabricaTelefono2("Samsung", "S10")
        print(telefono.marca)
        print(telefono.modelo)
       
 
 #el init nos ahorra poner los atributos y crear el objeto
