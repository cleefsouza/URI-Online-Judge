n = int(input())
rpms = [int(i) for i in input().split(' ')]

queda = False
for i in range(1, n):
    y = i - 1

    if(rpms[i] < rpms[y]):
        pos = rpms.index(rpms[i])
        print(pos + 1)
        queda = True
        break

if(not queda):
    print(0)
