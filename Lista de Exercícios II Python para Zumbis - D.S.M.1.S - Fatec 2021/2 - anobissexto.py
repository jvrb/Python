#2.   Determine se um ano é bissexto. Verifique no Google como fazer isso...

import calendar
print("Programa para saber se um ano é Bissexto!!")
ano = int(input("Ano a ser analisado: "))
if calendar.isleap(ano) == True:
    print("O ano {} é BISSEXTO!!" .format(ano))
else:
    print("O ano {} NÃO é BISSEXTO!!" .format(ano))
