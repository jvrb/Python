#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print("Programa Carro Alugado")
km = float(input("Digite a quantidade de Km percorrido com o veiculo: "))
dias = int(input("Digite por quantos o carro ficou alugado: "))
valorAPagar = (60 * dias) + (0.15 * km)
print("Valor a pagar: {}".format(valorAPagar))
