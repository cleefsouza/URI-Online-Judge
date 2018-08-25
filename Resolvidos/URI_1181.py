l = int(input())
t = str(input())
x = []
for i in range(12):
    y = []
    for j in range(12):
        v = float(input())
        y.append(v)
    x.append(y)

if(t=="S"):
    print("{:.1f}".format(sum(x[l])))
elif(t=="M"):
    m = sum(x[l])/len(x[l])
    print("{:.1f}".format(m))
