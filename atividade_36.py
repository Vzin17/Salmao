def verificar_numero(numero):
    return 1000 <= numero <= 9999

while True:
    try:
        numero = int(input("Digite um número inteiro de quatro dígitos (de 1000 a 9999): "))
        if verificar_numero(numero):
            break
        else:
            print("Por favor, insira um número dentro do intervalo especificado.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

numero_str = str(numero)

for digito in numero_str:
    print(digito)
