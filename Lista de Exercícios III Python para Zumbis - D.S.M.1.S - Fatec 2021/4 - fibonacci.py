num = int(input("Digite um numero: "))
total = 0
num_anterior = 1 #O primeiro elemento
num_atual = 1
fib = 2
while fib < num:
  total = num_anterior + num_atual 
  num_anterior = num_atual
  num_atual = total
  fib = fib + 1

print("Sequenacia de Fibonacci: {}".format(total))
