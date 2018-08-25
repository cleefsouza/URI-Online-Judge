xvalores = []
for i in range(100):
    xvalores.append(int(input()))

print(max(xvalores))
print(xvalores.index(max(xvalores))+1)
