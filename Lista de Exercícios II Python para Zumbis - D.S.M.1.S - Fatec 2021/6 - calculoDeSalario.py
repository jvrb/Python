'''
6. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa
que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao
sindicato e o salário líquido. Observe que Salário Bruto - Descontos =
Salário Líquido. Calcule os descontos e o salário líquido, conforme a
tabela abaixo:
a.  + Salário Bruto : R$
b.  - IR (11%) : R$
c.  - INSS
(8%) : R$
d.  - Sindicato ( 5%) : R$
e.  = Salário Liquido : R$
'''

print("Calculo de Salário!!")
sal_bruto = float(input("Sálario Bruto: R$"))
imp_renda = sal_bruto * (11 / 100)
inss = sal_bruto * (8 / 100)
sindicato = sal_bruto * (5 / 100)
sal_liq = sal_bruto - (imp_renda + inss + sindicato)
print("Salário Bruto: R$ {}" .format(sal_bruto))
print("Descontos: R$ {}" .format(imp_renda + inss + sindicato))
print("Salário Líquido: R$ {}" .format(sal_liq))
