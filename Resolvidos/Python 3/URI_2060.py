x = int(input())
binoLista = input().split(' ')
xDois, xTres, xQuatro, xCinco = 0, 0, 0, 0

for j in binoLista:
	if(int(j) % 2 == 0): xDois += 1
	if(int(j) % 3 == 0): xTres += 1
	if(int(j) % 4 == 0): xQuatro += 1
	if(int(j) % 5 == 0): xCinco += 1

print('{} Multiplo(s) de 2'.format(xDois))
print('{} Multiplo(s) de 3'.format(xTres))
print('{} Multiplo(s) de 4'.format(xQuatro))
print('{} Multiplo(s) de 5'.format(xCinco))
