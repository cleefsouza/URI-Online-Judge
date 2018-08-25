while True:
  x = int(input())
  if(x==0):
    break
  else:
    soma = 0
    for i in range(10):
      if(x%2==0):        
        soma+=x
      x+=1
    print(soma)