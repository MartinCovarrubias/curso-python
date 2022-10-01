voto = input ("Introduce tu voto (A,B,C): ")

if voto.upper() == "A":
    print("Voto por el partido rojo")
elif voto.upper() == "B":
    print("Voto por el partido verde")
elif voto.upper() == "C":
    print("Voto por el partido azul")
else:
    print("opcion invalida")