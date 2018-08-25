for n in range(int(input())):
    at = str(input())
    df = float(input())
    nt = [float(i) for i in input().split(" ")]
    nt.sort()
    nt.remove(max(nt))
    nt.remove(min(nt))
    print("{} {:.2f}".format(at, (sum(nt)*df)))