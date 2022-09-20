num1 = 100
num2 = 50
num3 = 10
num4 = 5
print (num1 + num2 * num3) # 100 + 50 * 10 = 100 + 500 = 600

#cuando este entre parentesis se ejecuta primero
print ((num1 + num2) * num3) # (100 + 50) * 10 = 150 * 10 = 1500

print (num1 + num2 * num3 - num4) # 100 + 50 * 10 - 5 = 100 + 500 - 5 = 595

#cuando este entre parentesis se ejecuta primero
print ((num1+num2)*( num3 - num4)) # (100 + 50) * (10 - 5) = 150 * 5 = 750
