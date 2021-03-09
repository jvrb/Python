import random

print('programa impar ou par')
lista = random.sample(range(100), 10)
impar = []
par = []
for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'LISTA GERADA!\n{lista}')
print(f'LISTA DOS NUMEROS IMPARES\n{impar}')
print(f'LISTA DOS NUMEROS PARES\n{par}')
    
