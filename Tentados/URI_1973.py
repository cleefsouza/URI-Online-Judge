n = int(input())
x = [int(i) for i in input().split(" ")]

attackedStar, y = 0, 0
nRoub = sum(x)
i = 0
while(True):
  if(i<0):
    break;
  elif(i>=len(x)):
    break;

  if(x[i]%2==0):
    x[i] = x[i]-1
    i, y = i-1, 1
  else:
    x[i] = x[i]-1
    attackedStar+=1
    i+=1

nRoub-=attackedStar
print(n-y, nRoub)