while True:
    try:
        l = int(input())
        n = [int(i) for i in input().split()]
        print(1 if max(n)<10 else 2 if max(n)>=10 and max(n)<20 else 3)       
    except EOFError:
        break
