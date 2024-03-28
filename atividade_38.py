
def adicionar_segundos(hora, minuto, segundo, duracao):
    tempo_inicial_segundos = hora * 3600 + minuto * 60 + segundo
    tempo_final_segundos = tempo_inicial_segundos + duracao
    nova_hora = tempo_final_segundos // 3600
    novo_minuto = (tempo_final_segundos % 3600) // 60
    novo_segundo = (tempo_final_segundos % 3600) % 60
    return nova_hora, novo_minuto, novo_segundo

def verificar_horario(hora, minuto, segundo):
    return 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60

hora_inicial = int(input("Digite a hora de início (0-23): "))
minuto_inicial = int(input("Digite os minutos de início (0-59): "))
segundo_inicial = int(input("Digite os segundos de início (0-59): "))
duracao_segundos = int(input("Digite a duração em segundos: "))

if verificar_horario(hora_inicial, minuto_inicial, segundo_inicial):
    hora_final, minuto_final, segundo_final = adicionar_segundos(hora_inicial, minuto_inicial, segundo_inicial, duracao_segundos)
    
    print("Horário de término da experiência: {:02d}:{:02d}:{:02d}".format(hora_final, minuto_final, segundo_final))
else:
    print("Horário inicial inválido. Certifique-se de que os valores estejam dentro dos intervalos especificados.")
