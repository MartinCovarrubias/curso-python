
jugador ={1:"Casillas", 15:"Ramos",
3:"Pique", 5:"Puyol", 11:"Capdevila",
14:"Xabi Alonso", 16:"Busquets",
8:"Xavi Hernandez", 18:"Pedrito",
6:"Iniesta", 7:"Villa"}

numeroJuagador = int(input("Introduce el numero del jugador: "))

if numeroJuagador in jugador:
    print(jugador.get(numeroJuagador))
else:
    print("El jugador no esta en la lista")