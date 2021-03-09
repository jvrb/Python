import random

print('programa intercala listas')
lista1 = random.sample(range(1, 100), 10)
lista2 = random.sample(range(1, 100), 10)
lista3 = []

for numero in range(len(lista1)):
    lista3.append(lista1[numero])
    lista3.append(lista2[numero])

print(f'1 - LISTA GERADA\n{lista1}')
print(f'2 - LISTA GERADA\n{lista2}')
print(f'3 - LISTA INTERCADA\n{lista3}')
