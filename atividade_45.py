####
# Calcule a média de um aluno na disciplina de ED. Para isso solicite o nome do aluno, a
# nota da prova e a nota qualitativa. Sabe-se que a nota da prova tem peso 2 e a nota
# qualitativa peso 1. Mostre a média como resultado.
####
Nome_aluno = input("Digite seu nome: ")
Nota_prova = float(input("Digite a nota da prova: "))
Nota_Quali = float(input("Digite a nota qualitativa: "))
Result = (Nota_prova*2+Nota_Quali) /3
print(f"{Nome_aluno} tem a media de: {Result}")
