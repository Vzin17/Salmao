def calcular_proporcao(investimentos, total_investido):
    proporcoes = []
    for investimento in investimentos:
        proporcao = investimento / total_investido
        proporcoes.append(proporcao)
    return proporcoes

def calcular_ganhos(proporcoes, premio):
    ganhos = []
    for proporcao in proporcoes:
        ganho = proporcao * premio
        ganhos.append(ganho)
    return ganhos

investidor1 = float(input("Digite o valor investido pelo primeiro amigo: "))
investidor2 = float(input("Digite o valor investido pelo segundo amigo: "))
investidor3 = float(input("Digite o valor investido pelo terceiro amigo: "))

premio = float(input("Digite o valor total do prêmio: "))

total_investido = investidor1 + investidor2 + investidor3

proporcoes = calcular_proporcao([investidor1, investidor2, investidor3], total_investido)

ganhos = calcular_ganhos(proporcoes, premio)

print("O primeiro amigo ganharia:", ganhos[0])
print("O segundo amigo ganharia:", ganhos[1])
print("O terceiro amigo ganharia:", ganhos[2])
