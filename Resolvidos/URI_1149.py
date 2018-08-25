x = [int(i) for i in input().split(" ")]
y = int(x[0])
z = x[1:]
a,n = 0,0
for i in z:
    if(i>0):
        n+=i

for i in range(0,n):
    a += y+i

print(a)
