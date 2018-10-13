n = int(input())
inp = out = 0
for i in range(n):
    x = int(input())
    if(x>=10 and x<=20):
        inp += 1
    else:
        out += 1
print('{} in'.format(inp))
print('{} out'.format(out))