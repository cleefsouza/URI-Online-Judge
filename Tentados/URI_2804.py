n, m = [int(i) for i in input().split(" ")]
x = []
f = True  
for i in range(n):
  y = []
  y = [int(j) for j in input().split(" ")]
  x.append(y)

c = 0
for k in range(n-1):
  if(c<n-1):
    if(x[k][k+1]!=x[k+1][k]):
      print("*")
      f = False
      break
  else:
    if(x[k][k+1]!=x[k][k]):
      print("*")
      f = False
      break
  c+=1
if(f!=False):
  lm = []
  for l in range(n-1):
    lm.append(max(x[l]))
  lm = max(lm)

  if(lm%2==0):
    print(int(lm/10))
  else:
    resu = []
    for i in range(n):
      for j in range(n):
        resu.append(x[i][j])
    lo = (max(resu)*resu.count(max(resu)))
    ln = sum(resu)-(max(resu)*resu.count(max(resu)))
    print(int(ln/lo)*10)
