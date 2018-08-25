o = str(input())
x = []
for i in range(12):
    y = []
    for j in range(12):
        v = float(input())
        y.append(v)
    y = y[::-1]
    x.append(y)
    
x = x[::-1]
if(o=="S"):
    s = []
    z = 0
    for i in range(12):
        s.append(x[i][i+1:])
        z += sum(s[i])
    print("{:.1f}".format(z))
    
elif(o=="M"):
    s = []
    z = 0
    m = 0
    for i in range(12):
        s.append(x[i][i+1:])
        z += sum(s[i])
        m +=len(s[i])
    print("{:.1f}".format(z/m))
