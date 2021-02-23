print("Tempo de vida de um fumante")
qtdCigarro = int(input("Digite a quantidade de cigarros fumados por dia: "))
qtdAnos = int(input("Digite por quantos anos voce fumou: "))
resultado = 0
totCigarros = qtdCigarro * (qtdAnos * 365) #Calc a quantidade de cigarros total
diasPerdidos = ((totCigarros * 10) / 60) / 24 #Calc quantos minutos foram perdidos
print("dias de vida perdidos: {}".format(diasPerdidos))
