x,y,z = [], [], []
for i in range(20):
  if(len(x)<10):  
    x.append(int(input()))
    if(len(x)==10):
      x.reverse()
  else:
    y.append(int(input()))
    if(len(y)==10):
      y.reverse()

for i in y:
  z.append(i)
for i in x:
  z.append(i)
  
for i in range(20):
  print("N[{}] = {}".format(i,z[i]))
