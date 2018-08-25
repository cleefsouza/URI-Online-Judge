lista = input().split()
p, n = int(lista[0]), int(lista[1])
c = [int(i) for i in input().split()]
ant, atu, v = 0, 0, True

for i in range(n):
  ant = c[i]
  if(c[i]==c[-1]):
    atu = c[-1]
  else:
    atu = c[i+1]
  if(ant<atu):
    if(ant+p<atu):
      print("GAME OVER")
      v = False
      break
  else:
    if(atu+p<ant):
      print("GAME OVER")
      v = False
      break
if(v==True):
  print("YOU WIN")