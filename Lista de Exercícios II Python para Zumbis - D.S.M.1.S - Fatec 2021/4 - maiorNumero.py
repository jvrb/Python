#4.   Faça um Programa que leia três números e mostre o maior deles.

print("Digite 3 número e mostraremos o maior deles")
num1 = float(input("Digite o 1º Numero: "))
num2 = float(input("Digite o 2º Numero: "))
num3 = float(input("Digite o 3º Numero: "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3:
    maior = num2
else:
    maior = num3

print("O maior Número digitado foi {}" .format(maior))
