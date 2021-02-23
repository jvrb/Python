salario_aumento = 0
val_aumento = 0
print("Calculo de salario")
salario = int(input("Valor do salario: "))
aumento = int(input("Quantos % de aumento: "))
salario_aumento = salario + (salario * (aumento / 100))
print("Seu novo salario sera de {}" . format(salario_aumento))
