n = int(input())

for i in range(n):
  soma = 0
  x, y = [int(i) for i in input().split(" ")]
  for j in range(y):
    while(x%2 == 0):
      x += 1
    soma += x
    x += 1
  print(soma)   
