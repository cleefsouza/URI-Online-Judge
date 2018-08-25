c = int(input())
t = str(input())
x = []
for i in range(12):
    y = []
    for j in range(12):
        v = float(input())
        y.append(v)
    x.append(y)

if(t=="S"):
    s = []
    for i in range(12):
        s.append(x[i][c])
    print("{:.1f}".format(sum(s)))
elif(t=="M"):
    m = []
    for i in range(12):
        m.append(x[i][c])
    print("{:.1f}".format(sum(m)/len(m)))
