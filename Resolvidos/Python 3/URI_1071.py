x = int(input())
y = int(input())
soma = 0
if x < y:
    soma = sum([numero for numero in range(1+x, y ) if numero % 2 != 0])
else:
    soma = sum([numero for numero in range(1+y, x ) if numero % 2 != 0])

print(soma)