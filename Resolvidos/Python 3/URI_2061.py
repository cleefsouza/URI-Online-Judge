values = input().split(" ")
abas, acoes = int(values[0]), int(values[1])

for i in range(0, acoes):
	acao = input()
	if(acao == 'fechou'):
		abas -= 1
		abas += 2
	else:
		abas -= 1
	
print(abas)
