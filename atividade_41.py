def custo_cercar_terreno(comprimento, largura, preco_metro_tela):
    perimetro = 2 * (comprimento + largura)
    custo_total = perimetro * preco_metro_tela
    return custo_total

comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))
largura_terreno = float(input("Digite a largura do terreno em metros: "))
preco_metro_tela = float(input("Digite o preço do metro de tela em reais: "))

custo_total = custo_cercar_terreno(comprimento_terreno, largura_terreno, preco_metro_tela)

print("O custo para cercar o terreno com tela é de R$", custo_total)
