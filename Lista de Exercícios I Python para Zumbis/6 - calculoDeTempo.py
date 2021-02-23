tempo = 0
print("Programa para calcular o tempo de uma viagem")
distancia = float(input("Digite a distancia em KM a percorrer: "))
velocidade = int(input("Digite a velocidade media do veiculo: "))
tempo = distancia / velocidade
t1 = str(tempo)
print("O tempo de viagem será de {}".format(str(t1.replace(".", "h"))))

