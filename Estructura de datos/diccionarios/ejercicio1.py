paises = {"Guatemala": "Guatemala", "Honduras": "Tegucigalpa", "El Salvador": "San Salvador", "Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Belice": "Belice"}

pais = input("Ingrese el nombre de un pais: ")
#paisxd = pais.capitalize()

if pais.capitalize() in paises:
    print(paises.get(pais.capitalize()))
else:
    print("El pais no existe")

#metodo capitalize() convierte la primera letra de una cadena a mayuscula
#sintaxis: cadena.capitalize()