#2.   Determine se um ano é bissexto. Verifique no Google como fazer isso...

print("Programa para saber se um ano é Bissexto!!")
ano = int(input("Ano a ser analisado: "))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano é bissexto (tem 366 dias)")
    else:
        print("O ano é bissexto (tem 366 dias)")
else:
    print("O ano não é um ano bissexto (tem 365 dias)")
