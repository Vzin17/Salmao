def converter_maiuscula_para_minuscula(letra):
    
    if ord('A') <= ord(letra) <= ord('Z'):
        diferenca = ord('a') - ord('A')
        letra_minuscula = chr(ord(letra) + diferenca)
        return letra_minuscula
    
    else:
        return "Por favor, insira uma letra maiúscula como entrada."

letra_maiuscula = input("Digite uma letra maiúscula: ")
letra_minuscula = converter_maiuscula_para_minuscula(letra_maiuscula)
print("A letra minúscula correspondente é:", letra_minuscula)
