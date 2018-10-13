n = int(input())
c = r = s = cont = 0
for i in range(n):
    cobaia = input().split(" ")
    if(cobaia[1]=="C"):
        c+=int(cobaia[0])
    elif(cobaia[1]=="R"):
        r+=int(cobaia[0])
    elif(cobaia[1]=="S"):
        s+=int(cobaia[0])
    cont+=int(cobaia[0])

print('Total: {} cobaias'.format(cont))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format((c*100)/cont))
print('Percentual de ratos: {:.2f} %'.format((r*100)/cont))
print('Percentual de sapos: {:.2f} %'.format((s*100)/cont))