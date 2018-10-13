for i in range(int(input())):
  t = int(input())
  a = t-2015
  if(a<0):
    a = a*-1
    print(a,"D.C.")
  else:
    a+=1
    print(a,"A.C.")
