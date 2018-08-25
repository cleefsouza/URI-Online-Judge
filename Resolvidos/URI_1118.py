i = 1
while True:
  if(i>2):
    print("novo calculo (1-sim 2-nao)")
    i = int(input())
  elif(i==2):
    break
  elif(i==1):
    v = []
    while True:
      n = float(input())
      if(n < 0 or n > 10):
        print("nota invalida")
      else:
        v.append(float(n))
      
      if(len(v)==2):
        print("media = {:.2f}".format((v[0]+v[1])/2))
        i = 3
        break
