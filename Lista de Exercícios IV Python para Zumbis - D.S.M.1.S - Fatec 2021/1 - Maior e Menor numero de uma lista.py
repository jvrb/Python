import random
print("menor e maior de uma lista")
lista = random.sample(range(100), 10)
maior, menor = lista[0], lista[0]
for numero in lista:
    if numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero

print(f'LISTA GERADA!!\n{lista}')
print(f'Maior Numero da lista: {maior}\nMenor Numero da lista: {menor}')
    
