import math as mt

def binet(n):
    x = mt.pow(((1 + mt.sqrt(5)) / 2), n)
    y = mt.pow(((1 - mt.sqrt(5)) / 2), n)
    fibonacci = (x - y) / mt.sqrt(5)

    return fibonacci

n = int(input())
print('{:.1f}'.format(binet(n)))
