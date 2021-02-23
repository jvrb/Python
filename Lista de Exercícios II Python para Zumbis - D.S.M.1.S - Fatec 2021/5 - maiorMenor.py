#5.   Faça um Programa que leia três números e mostre o maior e o menor deles.

print("Programa para mostrar o maior e o menor numero!")
n1 = float(input("Digite o 1º Número: "))
n2 = float(input("Digite o 2º Número: "))
n3 = float(input("Digite o 3º Número: "))

if n1 > n2 and n1 > n3:
    maior = n1
    #A variavel menor recebe n2 SE n2 < n3 SENAO recebe n3 (Operador Ternario)
    menor = n2 if n2 < n3 else n3
elif n2 > n1 and n2 > n3:
    maior = n2
    menor = n1 if n1 < n3 else n3
else:
    maior = n3
    menor = n1 if n1 < n2 else n1

print("O MAIOR número digitado é {}\nO MENOR número digitado é {}" .format(maior,menor))
    
