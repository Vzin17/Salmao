def converter_segundos(segundos):
    horas = segundos // 3600

    minutos_restantes = segundos % 3600

    minutos = minutos_restantes // 60

    segundos_restantes = minutos_restantes % 60
    
    return horas, minutos, segundos_restantes

segundos = int(input("Digite o número de segundos: "))

horas, minutos, segundos_restantes = converter_segundos(segundos)

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_restantes)
