n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
while n1 <= 0 or n2 <= 0:
  print("Digite numero inteiros positivos!!")
  n1 = int(input("Digite um numero: "))
  n2 = int(input("Digite um numero: "))
  
while n2 != 0:
  resto = n1 % n2
  n1,n2 = n2, resto

print(n1)
