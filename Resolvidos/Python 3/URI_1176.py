def fibonacci(n):
    a,b = 0, 1
    l = []
    for i in range(61):
        l.append(int(a))
        a, b = b, a+b
    return l[n]
        
for i in range(int(input())):
    n = int(input())
    print("Fib({}) = {}".format(n, fibonacci(n)))
