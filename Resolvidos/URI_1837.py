a, b = [int(i) for i in input().split(" ")]
q, r = 0, 0

for r in range(abs(b)):
    if(((a-r)%b)==0):
        q = (a-r)/b
        break
    
print(int(q), int(r))
