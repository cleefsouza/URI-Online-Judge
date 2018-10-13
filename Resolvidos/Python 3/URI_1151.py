def fibonacci(n):
    a,b = 0, 1
    for i in range(n-1):
        print(a, end=" ")
        a, b = b, a+b
    print(a)
        
n = int(input())
fibonacci(n)
