cont = 0
for x in range(18644, 33088): # até 33088 pq o ultimo numero é exclusivo
    if '2' in str(x) and '7' not in str(x):
        cont += 1

print(cont)
