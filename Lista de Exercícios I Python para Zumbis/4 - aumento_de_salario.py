#4)  Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

print("Calculo de salario")
salario = int(input("Valor do salario: "))
aumento = int(input("Quantos % de aumento: "))
salario_aumento = salario + (salario * (aumento / 100))
print("Seu novo salario sera de {}" . format(salario_aumento))
