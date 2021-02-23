valorAPagar = 0
print("Programa Carro Alugado")
km = float(input("Digite a quantidade de Km percorrido com o veiculo: "))
dias = int(input("Digite por quantos o carro ficou alugado: "))
valorAPagar = (60 * dias) + (0.15 * km)
print("Valor a pagar: {}".format(valorAPagar))
