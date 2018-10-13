m = []
while True:
    x = int(input())
    if(x<0):
        break
    else:
        m.append(x)
print("{:.2f}".format(sum(m)/len(m)))
