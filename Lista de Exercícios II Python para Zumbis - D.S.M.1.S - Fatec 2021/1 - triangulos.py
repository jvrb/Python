'''1.  Faça um Programa que peça os três lados de um triângulo. O
programa deverá informar se os valores podem ser um triângulo. Indique,
caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles
ou escaleno.'''

print("Programa de Triângulo")
seg_ab = int(input("Digite o valor do Segmento AB: "))
seg_bc = int(input("Digite o valor do Segmento BC: "))
seg_cd = int(input("Digite o valor do Segmento CD: "))
'''Verificar se é possivel formar um triângulo seguindo as regras de
se a soma das medidas de dois deles é sempre maior que a medida do terceiro,
então, eles podem formar um triângulo'''
if (seg_ab + seg_bc) > seg_cd and (seg_ab + seg_cd) > seg_bc and (seg_bc + seg_cd) > seg_ab:
    print("As medidas PODEM formar um Triâgulo!!")
    if seg_ab == seg_bc or seg_ab == seg_cd:
        print("As medidas forma um Triângulo Isósceles!")
        #triângulo que possui três lados com medidas iguais
    elif seg_ab == seg_bc and seg_cd == seg_cd:
        print("As medidas forma um Triângulo Equilátero!")
        #triângulo que possui dois lados com medidas iguais
    elif seg_ab != seg_bc and seg_ab != seg_cd and seg_bc != seg_cd:
        print("As medidas forma um Triângulo Escaleno!")
        #triângulo que possui todos os lados com medidas diferentes
else:
    print("As medidas NÃO PODEM formar um Triâgulo!!")
