''' 7. Faça um programa para uma loja de tintas. O programa deverá pedir
o tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
tinta é vendida em  latas  de 18  litros,  que  custam  R$  80,00.
Informe  ao  usuário  a  quantidades  de  latas  de  tinta  a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro
de latas.
'''

print("Loja de Tintas")
tam_parede = float(input("Insira o tamanho da parede: "))
uma_lata = 18 * 3
latas = tam_parede // uma_lata
if tam_parede % uma_lata != 0:
    latas += 1
total = latas * 80
print("Para pintar uma parede de {}m, vamos precisar de {} latas\nPreço Total: R${}" .format(tam_parede,int(latas), total))
