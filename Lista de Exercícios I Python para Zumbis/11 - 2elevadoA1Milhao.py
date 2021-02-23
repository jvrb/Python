#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

print("2 elevado a 1 milhão")
conta = str(int(2**1000000))
print("2 elevado a 1 milhão é {}" .format(len(conta)))
