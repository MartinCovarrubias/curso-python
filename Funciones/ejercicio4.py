# calcular factura pasando precio y el iva

def calcular_factura ():
    precio = float ( input ( "Introduce el precio: " ))
    iva = int ( input ( "Introduce el iva: " ))

    if iva!=0:
        if iva > 0:
            total = precio + (precio * iva / 100)
            return total
        else:
            return "El iva no puede ser negativo"
    else:
        total = precio + (precio * 21 / 100)
        return total

print ("El total de la factura es: " , calcular_factura ())