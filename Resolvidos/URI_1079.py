n = int(input())
for i in range(n):
    n1, n2, n3 = [float(i) for i in input().split(" ")]
    media = ((2*n1) + (3*n2) + (5*n3)) / (2+3+5)
    print('{:.1f}'.format(media))