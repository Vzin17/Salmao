Altura = float(input("Digite a altura da escada: "))
Objetivo = float(input("Digite o quanto ele quer subir: "))
Altura_degrau = Altura/100
Altura_pessoa = Objetivo*Altura_degrau
R1 = Altura_pessoa*100*(Altura_degrau)
print(f"Ele devera subir: {R1}")
