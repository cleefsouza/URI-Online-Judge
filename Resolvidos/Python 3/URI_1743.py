l1 = [int(i) for i in input().split(" ")]
l2 = [int(i) for i in input().split(" ")]
res = "Y"
for i in range(5):
   if(l1[i] == l2[i]):
       res = "N"
       break

print(res)
