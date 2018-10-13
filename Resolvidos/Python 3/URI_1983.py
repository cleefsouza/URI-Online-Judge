dic = {}
for i in range(int(input())):
  l = input().split() 
  dic[float(l[1])] = int(l[0])

if(max(dic)>=8):
  print(int(dic[max(dic)]))
else:
  print("Minimum note not reached")