# excepciones en python
# try sirve para probar un bloque de codigo
# except sirve para manejar el error
# finally se ejecuta sin importar si hay error o no
# raise sirve para lanzar una excepcion
while True: # while True es un ciclo infinito que se ejecuta hasta que se cumpla la condicion
    try: # try sirve para probar un bloque de codigo
        edad = int(input("Introduce tu edad: ")) # int(input("Introduce tu edad: ")) es una funcion que convierte un string a entero
        print("Tu edad es: ", edad) # print("Tu edad es: ", edad) es una funcion que imprime en pantalla
        break # break es una funcion que rompe el ciclo
    except: # except sirve para manejar el error
        print("Ha ocurrido un error, introduce bien la edad") # print("Ha ocurrido un error, introduce bien la edad") es una funcion que imprime en pantalla
    finally :   # finally se ejecuta sin importar si hay error o no
        print("Fin de la iteracion")    # print("Fin de la iteracion") es una funcion que imprime en pantalla