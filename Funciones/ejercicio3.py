def numeros ():
    num1 = int ( input ( "Introduce el primer número: " ))
    num2 = int ( input ( "Introduce el segundo número: " ))
    if num1 > num2 :
        return 1
    elif num1 < num2 :
        return - 1
    else :
        return 0

print (numeros())
