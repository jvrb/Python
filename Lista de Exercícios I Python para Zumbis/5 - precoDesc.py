preco_prd = 0
print("Programa para calcular desconto")
prd = float(input("Digite o valor do produto: "))
desc = float(input("Digite o percentual de desconto: "))
preco_prd = prd - (prd * (desc / 100))
print("==========================")
print("Valor do produto: R${}\nValor do produto com desconto: R${}".format(prd,preco_prd))
