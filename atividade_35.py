def inverter_digitos(numero):
    numero_str = str(numero)
    numero_invertido_str = numero_str[::-1]
    numero_invertido = int(numero_invertido_str)
    return numero_invertido

def verificar_numero(numero):
    return 100 <= numero <= 999

while True:
    try:
        numero = int(input("Digite um número inteiro de três dígitos (de 100 a 999): "))
        if verificar_numero(numero):
            break
        else:
            print("Por favor, insira um número dentro do intervalo especificado.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

numero_invertido = inverter_digitos(numero)

print("O número invertido é:", numero_invertido)
