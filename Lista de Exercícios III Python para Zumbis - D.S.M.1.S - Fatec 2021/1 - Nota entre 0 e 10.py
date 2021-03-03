print("Programa para mostrar nota!!")
nota = int(input("Digite a nota entre 0 e 10: "))
while nota < 0 or nota > 10:
    print("NOTA INVÁLIDA!!")
    nota = int(input("Digite novamente: "))

print("Sua nota final {}" .format(nota))
    
    
