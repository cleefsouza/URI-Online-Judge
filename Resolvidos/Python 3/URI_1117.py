v = []
while True:
  n = float(input())
  if(n < 0 or n > 10):
    print("nota invalida")
  else:
    v.append(float(n))
  
  if(len(v)==2):
    print("media = {:.2f}".format((v[0]+v[1])/2))
    break
