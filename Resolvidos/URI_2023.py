l = []
x=0
while True:
  try:
    n = input()
    l.append(n)
  except EOFError:
    break

  for i in range(1,len(l)):
    atual = i
 
    while ((atual > 0) and (l[atual - 1].lower() > l[atual].lower())):
      l[atual - 1],l[atual] = l[atual],l[atual - 1]
      atual -= 1
 
print("{}".format(l[-1]))