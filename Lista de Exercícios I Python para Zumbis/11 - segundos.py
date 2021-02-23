print("Programa para calcular segundos")
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
#variavel criada para tranformar os dias em horas
aux_hora = dias * 24
#variavel criada para tranformar as horas em minutos
aux_minutos = (aux_hora + horas) * 60
#variavel criada para tranformar os minutos em segundos
aux_segundos = (aux_minutos * 60) + segundos
print("Somando {} dias, {} horas, {} minutos, {} segundos. Da o total de {} segundos" .format(dias,horas,minutos,segundos,aux_segundos))
