def custo_ao_consumidor(custo_fabrica):
    porcentagem_distribuidor = 0.12
    porcentagem_impostos = 0.45
    
    custo_distribuidor = custo_fabrica * porcentagem_distribuidor
    custo_impostos = custo_fabrica * porcentagem_impostos
    custo_consumidor = custo_fabrica + custo_distribuidor + custo_impostos
    
    return custo_consumidor

custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

custo_total = custo_ao_consumidor(custo_fabrica)

print("O custo ao consumidor do carro é de R$", custo_total)
