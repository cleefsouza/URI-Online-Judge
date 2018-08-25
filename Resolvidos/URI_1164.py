n = int(input())
for i in range(n):
  x = int(input())
  l = []
  for j in range(1,x):
    if(x%j==0):
      l.append(j)
  if(sum(l)==x):
    print("{} eh perfeito".format(x))
  else:
    print("{} nao eh perfeito".format(x))