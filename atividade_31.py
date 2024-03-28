SalarioBase = float(input("Digite o salario base:"))
Imposto = SalarioBase*0.07
Aumento = SalarioBase*0.05
Salario = SalarioBase+Aumento
Salario1 = Salario-Imposto
print(f"Ele vai ganhar: {Salario1}")
