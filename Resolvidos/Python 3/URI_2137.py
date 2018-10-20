while True:
    try:
        x = []
        for i in range(int(input())):
            x.append(input())

        x.sort()
        for y in x:
            print(y)

    except EOFError:
        break