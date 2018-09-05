n = int(input())
star = [int(i)for i in input().split()]

yRoub, nRoub, i = set(), 0, 0

while(True):

  if(n==0 or i>=n or i<0):
    break
  
  yRoub.add(i)

  if(star[i]==0):
    break
  
  star[i]-=1
  
  if(star[i]%2==0):
    i+=1
  else:
    i-=1

print(len(yRoub), sum(star))

