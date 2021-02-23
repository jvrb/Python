#10) Escreva um programa para  calcular a redução do tempo  de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

print("Tempo de vida de um fumante")
qtdCigarro = int(input("Digite a quantidade de cigarros fumados por dia: "))
qtdAnos = int(input("Digite por quantos anos voce fumou: "))
totCigarros = qtdCigarro * (qtdAnos * 365) #Calc a quantidade de cigarros total
diasPerdidos = ((totCigarros * 10) / 60) / 24 #Calc quantos minutos foram perdidos
print("dias de vida perdidos: {}".format(diasPerdidos))
