print("Programa Total de Habitantes Iguais")
a = 80000
b = 200000
anos = 0
while a < b:
    a = a + (a * (3 / 100))
    b = b + (b * (1.5 / 100))
    anos = anos + 1
print("Anos: {}".format(anos))
    
