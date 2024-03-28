Produto = float(input("Digite o valor do produto: "))
Desconto = Produto*0.10
DescontoV = Produto-Desconto
Parcela = Produto/3
Comissao = DescontoV*0.05
A_Vista = DescontoV-Comissao
Comissao2 = Produto*0.05
Desc = Produto-Comissao2
print(f'''
        Valor com desconto: {DescontoV}
        Valor parcelado: {Parcela}
        Comissao do vendedor com desconto: {A_Vista}
        Comissao do vendedor sobre o valor total: {Desc}
        ''')
