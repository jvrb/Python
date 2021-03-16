cont = 0
for x in range(1,10): #Indo até 10 pois o 10 é exclusivo
    if x != 3:
        for y in range(1,7): #Indo até 7 pois o 10 é exclusivo
            print(x)
            cont += 1
print(f'quant: {cont}')
